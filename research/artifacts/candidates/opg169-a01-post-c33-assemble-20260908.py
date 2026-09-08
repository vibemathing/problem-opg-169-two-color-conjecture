"""Reassemble exact archived inputs only; never extract the embedded draft packet.
Run this before the separate nine-donor audit. Existing nonidentical output fails.
"""
import base64,hashlib,json,lzma,platform,resource,signal,time
from pathlib import Path
D=Path('research/artifacts/candidates')
M=D/'opg169-a01-post-c33-supplied-manifest-20260908.json'
O=D/'opg169-a01-post-c33-supplied-archive-20260908.json'

def require(ok,label):
    if not ok:raise ValueError(label)

def main():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(10,11))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0));signal.alarm(15)
    start=time.monotonic();h=lambda b:hashlib.sha256(b).hexdigest()
    raw=M.read_bytes();require(len(raw)<16384,'manifest input limit');m=json.loads(raw)
    require(m['output_path']==str(O) and len(m['parts'])==4,'fixed output and four parts')
    chunks=[]
    for i,p in enumerate(m['parts']):
        expected=D/('opg169-a01-post-c33-supplied-part-'+str(i)+'-20260908.txt')
        require(p['path']==str(expected),'fixed part identity')
        data=expected.read_bytes();require(len(data)==p['bytes']<20000 and h(data)==p['sha256'],'part digest')
        require(data.endswith(b'\n') and b'\n' not in data[:-1],'one trailing newline')
        chunks.append(data[:-1].decode('ascii'))
    archive=dict(m['archive_header']);archive['data']=''.join(chunks)
    encoded=(json.dumps(archive,sort_keys=True,separators=(',',':'))+'\n').encode()
    require(len(encoded)==m['output_bytes'] and h(encoded)==m['output_sha256'],'assembled exact bytes')
    dec=lzma.LZMADecompressor();inner=dec.decompress(base64.b64decode(archive['data'],validate=True),max_length=1048577)
    require(dec.eof and not dec.unused_data and len(inner)==archive['decoded_bytes']<1048576 and h(inner)==archive['decoded_sha256'],'decoded exact bytes')
    files=json.loads(inner);require(len(files)==archive['file_count']==27,'exact archived file count')
    for name,text in files.items():
        p=Path(name);require(not p.is_absolute() and '..' not in p.parts and isinstance(text,str),'relative UTF8 map')
    if O.exists():require(O.read_bytes()==encoded,'refuse overwrite of nonidentical archive')
    else:O.write_bytes(encoded)
    print(json.dumps({'verdict':'candidate_only','record_kind':'archive_assembly','exit_code':0,
        'runtime':platform.python_version(),'elapsed_seconds':round(time.monotonic()-start,6),
        'source_sha256':h(Path(__file__).read_bytes()),'manifest_sha256':h(raw),
        'output_sha256':h(encoded),'output_bytes':len(encoded),'decoded_sha256':h(inner),
        'decoded_bytes':len(inner),'file_count':len(files),'extracted_files':0,
        'embedded_packet_is_historical_only':True,'trusted_verifier_receipt':False},sort_keys=True))
if __name__=='__main__':main()
