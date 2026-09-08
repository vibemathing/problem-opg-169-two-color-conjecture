"""Reconstruct only the fixed C34 certificate input; hashes precede all use.
This is a storage integrity check, not a mathematical or trusted-verifier run.
"""
import base64
import hashlib
import json
import lzma
import resource
import signal
from pathlib import Path

D = Path('research/artifacts/candidates')
M = D / 'opg169-a01-c34-certificate-manifest.json'

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def need(ok, label):
    if not ok:
        raise ValueError(label)

def main():
    resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))
    resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1048576, 1048576))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    signal.alarm(8)
    raw = M.read_bytes()
    need(len(raw) < 65536, 'manifest cap')
    m = json.loads(raw)
    need(m['format'] == 'c34-certificate-parts-manifest-v1', 'format')
    need(len(m['data_files']) == 4, 'four segments')
    text = []
    for i, item in enumerate(m['data_files']):
        path = D / f'opg169-a01-c34-certificate-part-{i}.txt'
        need(str(path) == item['path'], 'fixed part path')
        part = path.read_bytes()
        need(len(part) == item['bytes'] and digest(part) == item['sha256'], 'part identity')
        need(part.endswith(b'\n') and b'\n' not in part[:-1], 'one line per part')
        text.append(part[:-1].decode('ascii'))
    envelope = dict(m['envelope'])
    envelope['data'] = ''.join(text)
    assembled = (json.dumps(envelope, sort_keys=True, separators=(',', ':')) + '\n').encode()
    need(len(assembled) == m['assembled_bytes'] and digest(assembled) == m['assembled_sha256'], 'assembled identity')
    need(envelope['decoded_bytes'] < 1048576, 'decoded cap')
    decoder = lzma.LZMADecompressor(memlimit=100000000)
    decoded = decoder.decompress(base64.b64decode(envelope['data'], validate=True), max_length=1048577)
    need(decoder.eof and not decoder.unused_data, 'complete single compressed stream')
    need(len(decoded) == envelope['decoded_bytes'] and digest(decoded) == envelope['decoded_sha256'], 'decoded identity')
    need(len(json.loads(decoded)) == 4, 'four batch certificates')
    target = D / 'opg169-a01-c34-lifting-certificate.json'
    need(str(target) == m['assembled_path'], 'fixed output path')
    if target.exists():
        need(target.read_bytes() == assembled, 'do not overwrite different input')
        status = 'identical_existing_input'
    else:
        with target.open('xb') as out:
            out.write(assembled)
        status = 'assembled'
    print(json.dumps({'verdict': 'candidate_only', 'check_kind': 'storage_integrity_only',
                      'status': status, 'manifest_sha256': digest(raw),
                      'assembled_sha256': digest(assembled), 'assembled_bytes': len(assembled),
                      'decoded_sha256': digest(decoded), 'decoded_bytes': len(decoded)}, sort_keys=True))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
