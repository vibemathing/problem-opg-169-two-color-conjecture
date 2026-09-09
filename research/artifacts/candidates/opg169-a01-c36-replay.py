"""Bounded generator/consumer execution. No trusted verification authority."""
import base64
import zlib
import ctypes
import ctypes.util
import datetime
import hashlib
import json
import os
import platform
import resource
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path
D=Path('research/artifacts/candidates')

def constrain():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(35,36))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    signal.alarm(40)
    name=ctypes.util.find_library('seccomp')
    if not name:raise RuntimeError('libseccomp required')
    lib=ctypes.CDLL(name)
    lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_load.argtypes=[ctypes.c_void_p];lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx:raise RuntimeError('seccomp init')
    for s in (b'socket',b'socketpair',b'connect'):
        n=lib.seccomp_syscall_resolve_name(s)
        if n<0 or lib.seccomp_rule_add(ctx,0x00050001,n,0)!=0:raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx)!=0:raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)

def main():
    if platform.python_version()!='3.13.5':raise RuntimeError('CPython 3.13.5 required')
    mode=sys.argv[1] if len(sys.argv)>1 else 'check'
    if mode not in ('check','audit'):raise ValueError('mode must be check or audit')
    src=D/('opg169-a01-c36-'+mode+'.py')
    if len(sys.argv)>2 and sys.argv[2]=='--child':
        constrain();os.execv(sys.executable,[sys.executable,str(src)])
    outpath=D/('opg169-a01-c36-certificate.json' if mode=='check' else 'opg169-a01-c36-audit-output.json')
    errpath=D/('opg169-a01-c36-'+mode+'-stderr.txt')
    start=time.monotonic();utc=datetime.datetime.now(datetime.timezone.utc).isoformat();timed=False
    with outpath.open('wb') as out,errpath.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,mode,'--child'],stdout=out,stderr=err)
        try:code=p.wait(timeout=43)
        except subprocess.TimeoutExpired:p.kill();code=p.wait();timed=True
    h=lambda b:hashlib.sha256(b).hexdigest()
    ob,eb=outpath.read_bytes(),errpath.read_bytes()
    inputs=[D/'opg169-a01-c36-input.json']
    if mode=='audit':inputs.append(D/'opg169-a01-c36-certificate-archive.json')
    rec={'record_kind':'generator_execution','verdict':'candidate_only','trusted_verifier_receipt':False,
         'command':['python3',str(src)],'runtime':platform.python_version(),'started_at':utc,
         'elapsed_seconds':round(time.monotonic()-start,6),'exit_code':code,'timeout':timed,
         'source_sha256':h(src.read_bytes()),'wrapper_sha256':h(Path(__file__).read_bytes()),
         'executable_sha256':h(Path(sys.executable).read_bytes()),
         'inputs':{str(x):h(x.read_bytes()) for x in inputs},
         'stdout_sha256':h(ob),'stdout_bytes':len(ob),'stderr_sha256':h(eb),'stderr_bytes':len(eb),
         'limits':{'cpu_affinity_count':1,'memory_bytes':536870912,'cpu_seconds':35,'wall_alarm_seconds':40,'parent_timeout_seconds':43,'output_file_bytes':1048576,'network':'seccomp denies socket/socketpair/connect'},
         'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,'elaboration':'not_run','axiom_report':None}}
    if mode=='check' and code==0:
        archive={'format':'c36-lossless-certificate-v1','encoding':'zlib-base64','decoded_bytes':len(ob),'decoded_sha256':h(ob),'data':base64.b64encode(zlib.compress(ob,9)).decode()}
        packed=(json.dumps(archive,sort_keys=True,separators=(',',':'))+'\n').encode()
        (D/'opg169-a01-c36-certificate-archive.json').write_bytes(packed)
        rec['archive_sha256']=h(packed)
        rec['archive_bytes']=len(packed)
    (D/('opg169-a01-c36-'+mode+'-execution.json')).write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True));return code
if __name__=='__main__':sys.exit(main())
