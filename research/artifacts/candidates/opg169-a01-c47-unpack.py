#!/usr/bin/env python3
"""Audit or reproduce the C47 corrected two-hole one-point capsule."""
from __future__ import annotations
import argparse,base64,hashlib,json,pathlib,subprocess,tempfile,zlib
ROOT=pathlib.Path(__file__).resolve().parents[3]
C=ROOT/'research/artifacts/candidates'
MAN=C/'opg169-a01-c47-capsule-manifest.json'
def h(b):return hashlib.sha256(b).hexdigest()
def decode():
    m=json.loads(MAN.read_text());chunks=[]
    for row in m['parts']:
        b=(C/row['name']).read_bytes();assert len(b)==row['size'] and h(b)==row['sha256'];chunks.append(b)
    cap=b''.join(chunks);assert len(cap)==m['assembled_size'] and h(cap)==m['assembled_sha256']
    outer=json.loads(cap)
    assert outer['format']=='opg169-c47-capsule-v1'
    raw=zlib.decompress(base64.b64decode(outer['zlib_b64']))
    assert len(raw)==outer['decoded_size'] and h(raw)==outer['decoded_sha256']
    inner=json.loads(raw);assert inner['format']=='opg169-c47-inner-file-map-v1'
    assert len(inner['files'])==outer['inner_file_count']
    for n,t in inner['files'].items():assert h(t.encode())==outer['inner_sha256'][n]
    return outer,inner
def audit():
    o,i=decode()
    return {'format':'opg169-c47-capsule-audit-v1','mode':'audit','status':'ok','inner_files':len(i['files']),'decoded_size':o['decoded_size'],'decoded_sha256':o['decoded_sha256']}
def reproduce():
    o,i=decode()
    with tempfile.TemporaryDirectory(prefix='opg169-c47-') as td:
        d=pathlib.Path(td)
        for n,t in i['files'].items():(d/n).write_text(t)
        p=subprocess.run(['python3',str(d/'opg169-a01-c47-two-hole-point-search.py'),'write'],cwd=d,check=True,capture_output=True,text=True,timeout=35)
        q=subprocess.run(['python3',str(d/'opg169-a01-c47-two-hole-point-audit.py')],cwd=d,check=True,capture_output=True,text=True,timeout=35)
        a=json.loads(p.stdout);b=json.loads(q.stdout)
        assert a['status']==b['status']=='ok' and a['tested_pairs']==b['tested_pairs']==8136
        assert a['successes']==0 and b['coverage']=={'ordinary_failure':8136}
    r=audit();r.update(mode='reproduce',tested_pairs=8136,strong_profile=0,ordinary_only=0,ordinary_failure=8136,all_pair_status_sha256=a['all_pair_status_sha256']);return r
def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['audit','reproduce'],nargs='?',default='audit');x=ap.parse_args();print(json.dumps(audit() if x.mode=='audit' else reproduce(),sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
