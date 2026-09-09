"""Verify/extract the C38 capsule and run one bounded foreground audit.
Only candidate-relative paths are created. Original execution records stay
immutable; a separate subdirectory holds any newly generated records.
"""
import base64
import hashlib
import json
import lzma
import platform
import subprocess
import sys
from pathlib import Path, PurePosixPath

D=Path('research/artifacts/candidates')
def digest(b):return hashlib.sha256(b).hexdigest()
def put(path,data):
    if path.is_symlink():raise ValueError('symlink is not allowed')
    if path.exists():
        if path.read_bytes()!=data:raise ValueError('existing input differs: '+str(path))
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'audit'
    if mode not in ('audit','check','extract'):raise ValueError('use audit, check or extract')
    cap=json.loads((D/'opg169-a01-c38-capsule.json').read_text())
    decoder=lzma.LZMADecompressor(memlimit=134217728)
    chunks=[]
    for part in cap['parts']:
        data=Path(part['path']).read_bytes()
        if len(data)!=part['bytes'] or digest(data)!=part['sha256']:raise ValueError('part digest mismatch')
        chunks.append(data.decode().strip())
    raw=decoder.decompress(base64.b64decode(''.join(chunks),validate=True),max_length=4194305)
    if not decoder.eof or len(raw)!=cap['decoded_bytes'] or len(raw)>4194304 or digest(raw)!=cap['decoded_sha256']:
        raise ValueError('capsule identity/size mismatch')
    files=json.loads(raw)['files']
    if set(files)!=set(cap['file_hashes']) or len(files)>32:raise ValueError('file inventory mismatch')
    root=D/'opg169-a01-c38-replay-work';run=root/'fresh-run'
    for name,text in files.items():
        p=PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts or not name.startswith('research/artifacts/candidates/'):
            raise ValueError('non-candidate relative path')
        data=text.encode();expected=cap['file_hashes'][name]
        if len(data)!=expected['bytes'] or digest(data)!=expected['sha256']:raise ValueError('file digest mismatch')
        put(root/p,data)
        if p.name in {'opg169-a01-c38-'+s for s in ('check.py','audit.py','replay.py','input.json','certificate.json')}:
            put(run/p,data)
    print(json.dumps({'capsule_verified':True,'files':len(files),'verdict':'candidate_only'}),flush=True)
    if mode!='extract':
        if platform.python_version()!='3.13.5':raise RuntimeError('selected replay requires CPython3.13.5')
        subprocess.run([sys.executable,str(D/'opg169-a01-c38-replay.py'),mode],cwd=run,check=True,timeout=45)
if __name__=='__main__':main()
