#!/usr/bin/env python3
from __future__ import annotations
import base64,hashlib,json,pathlib,subprocess,sys,tempfile,zlib
D=pathlib.Path(__file__).resolve().parent
MAN=D/'opg169-a01-s07-cycle5-capsule-manifest.json'

def need(x,msg):
    if not x: raise SystemExit(msg)
def sha(b): return hashlib.sha256(b).hexdigest()
def unpack(dst):
    m0=json.loads(MAN.read_text(encoding='utf-8'))
    need(m0['format']=='opg169-a01-s07-cycle5-segmented-capsule-v1','manifest format')
    pieces=[]
    for rec in m0['parts']:
        b=(D/rec['path']).read_bytes(); need(len(b)==rec['bytes'] and sha(b)==rec['sha256'],f"part hash {rec['path']}"); pieces.append(b)
    assembled=b''.join(pieces); need(len(assembled)==m0['assembled_bytes'] and sha(assembled)==m0['assembled_sha256'],'assembled capsule')
    c=json.loads(assembled.decode('utf-8'))
    need(c['format']=='opg169-a01-s07-cycle5-capsule-v1','capsule format')
    raw=zlib.decompress(base64.b64decode(c['zlib_b64']))
    need(len(raw)==c['decoded_size'],'decoded size')
    need(sha(raw)==c['decoded_sha256'],'decoded sha')
    m=json.loads(raw); need(m['format']=='opg169-a01-s07-cycle5-inner-file-map-v1','map format')
    need(len(m['files'])==c['file_count']==len(m['manifest']),'file count')
    for name,text in m['files'].items():
        b=text.encode('utf-8'); rec=m['manifest'][name]
        need(len(b)==rec['bytes'] and sha(b)==rec['sha256'],f'inner hash {name}')
        (dst/name).write_bytes(b)
    return c,m

def run(cmd,cwd,timeout):
    p=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
    need(p.returncode==0,f'command failed: {cmd}: {p.stderr.decode("utf-8","replace")}')
    need(not p.stderr,f'unexpected stderr: {cmd}')
    return p.stdout

def audit():
    with tempfile.TemporaryDirectory() as td0:
        c,m=unpack(pathlib.Path(td0))
    return {'format':'opg169-a01-s07-cycle5-transport-replay-v1','mode':'audit','status':'ok',
      'inner_files':c['file_count'],'decoded_bytes':c['decoded_size'],
      'decoded_sha256':c['decoded_sha256'],'verdict':'candidate_only'}

def reproduce():
    with tempfile.TemporaryDirectory() as td0:
        td=pathlib.Path(td0);c,m=unpack(td)
        replay=td/'opg169-a01-s07-cycle5-replay.py'
        a=run(['/usr/bin/python3','-S',str(replay),'audit'],td,60)
        need(a==(td/'opg169-a01-s07-cycle5-replay-audit-output.json').read_bytes(),'inner audit output')
        r=run(['/usr/bin/python3','-S',str(replay),'reproduce'],td,240)
        need(r==(td/'opg169-a01-s07-cycle5-replay-reproduce-output.json').read_bytes(),'inner reproduce output')
    return {'format':'opg169-a01-s07-cycle5-transport-replay-v1','mode':'reproduce','status':'ok',
      'inner_audit_sha256':sha(a),'inner_reproduce_sha256':sha(r),
      'cycle3_output_sha256':m['manifest']['opg169-a01-s07-cycle5-cycle3-merged02-output.json']['sha256'],
      'cycle4_certificate_decoded_sha256':'b1ce2a030f96b99bea1ade41dc9484552353bcc573434136026a7be221542ff5',
      'census_degrees':[4,5,6,7],'verdict':'candidate_only'}

def parent(n):
    need(n in (6,7,8,9),'parent must be 6,7,8,9')
    with tempfile.TemporaryDirectory() as td0:
        td=pathlib.Path(td0);unpack(td)
        replay=td/'opg169-a01-s07-cycle5-replay.py'
        raw=run(['/usr/bin/python3','-S',str(replay),'parent',str(n)],td,240)
        d=json.loads(raw);need(d['status']=='ok' and d['parent']==n,'parent replay')
    return {'format':'opg169-a01-s07-cycle5-transport-replay-v1','mode':'parent','parent':n,
      'stdout_bytes':d['stdout_bytes'],'stdout_sha256':d['stdout_sha256'],
      'status':'ok','verdict':'candidate_only'}

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'audit'
    need(mode in ('audit','reproduce','parent'),'usage: unpack.py [audit|reproduce|parent N]')
    if mode=='audit': out=audit()
    elif mode=='reproduce': out=reproduce()
    else:
        need(len(sys.argv)==3,'usage: unpack.py parent N');out=parent(int(sys.argv[2]))
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
