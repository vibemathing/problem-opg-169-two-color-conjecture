#!/usr/bin/env python3
"""Reassemble and audit the exact S13 Cycle 4 transport capsule.

This is a transport-integrity tool, not a mathematical verifier. It does not
change or strengthen the statements inside the recovered package.
"""
from __future__ import annotations
import argparse, base64, hashlib, io, json, pathlib, tempfile, zipfile

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def need(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('manifest',type=pathlib.Path)
    ap.add_argument('--root',type=pathlib.Path,default=pathlib.Path('.'))
    ap.add_argument('--extract',type=pathlib.Path)
    ap.add_argument('--output',type=pathlib.Path)
    a=ap.parse_args()
    m=json.loads(a.manifest.read_text(encoding='utf-8'))
    need(m['format']=='opg169-s13-cycle4-text-capsule-v1','format')
    pieces=[]
    for row in m['chunks']:
        p=a.root/pathlib.Path(row['path']).name
        raw=p.read_bytes()
        need(sha(raw)==row['sha256'],f'chunk digest: {p.name}')
        text=raw.decode('ascii').strip()
        need(len(text)==row['chars_without_newline'],f'chunk length: {p.name}')
        pieces.append(text)
    encoded=''.join(pieces)
    need(len(encoded)==m['base64_chars'],'base64 length')
    archive=base64.b64decode(encoded,validate=True)
    need(len(archive)==m['zip_bytes'],'zip size')
    need(sha(archive)==m['zip_sha256'],'zip digest')
    expected={x['path']:x for x in m['members']}
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        need(z.testzip() is None,'zip CRC')
        need(sorted(z.namelist())==sorted(expected),'member set')
        for n,row in expected.items():
            need('/' not in n and '\\' not in n and n not in ('.','..'),'unsafe member')
            b=z.read(n)
            need(len(b)==row['bytes'],f'member size: {n}')
            need(sha(b)==row['sha256'],f'member digest: {n}')
        digest_text=z.read('r08_s13_cycle4_digests.txt').decode('utf-8')
        digest_rows={line.split('  ',1)[1]:line.split('  ',1)[0]
                     for line in digest_text.splitlines() if '  ' in line}
        for n,row in expected.items():
            if n!='r08_s13_cycle4_digests.txt':
                need(digest_rows.get(n)==row['sha256'],f'inner manifest: {n}')
        if a.extract:
            a.extract.mkdir(parents=True,exist_ok=True)
            for n in expected:
                (a.extract/n).write_bytes(z.read(n))
    result={
      'status':'transport_capsule_ok','verdict':'candidate_only',
      'chunk_count':len(m['chunks']),'archive_bytes':len(archive),
      'archive_sha256':sha(archive),'members':len(expected),
      'inner_digest_manifest_checked':True,
      'mathematical_verification_performed':False,
      'L_join':'not_certified','root_closed':False,
    }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':
    main()
