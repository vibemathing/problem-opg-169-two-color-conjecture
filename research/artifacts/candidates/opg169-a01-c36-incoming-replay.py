"""Bounded local generator/audit runner. Does not invoke a trusted principal."""
import ctypes
import ctypes.util
import datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import signal
import subprocess
import sys
import time
D=Path('research/artifacts/candidates')

def constrain():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(30,31))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});signal.alarm(35)
    name=ctypes.util.find_library('seccomp')
    if not name: raise RuntimeError('seccomp required')
    lib=ctypes.CDLL(name)
    lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_load.argtypes=[ctypes.c_void_p];lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx:raise RuntimeError('seccomp allocation')
    for s in (b'socket',b'socketpair',b'connect'):
        n=lib.seccomp_syscall_resolve_name(s)
        if n<0 or lib.seccomp_rule_add(ctx,0x00050001,n,0)!=0:raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx)!=0:raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)

def main():
    if platform.python_version()!='3.13.5':raise RuntimeError('CPython 3.13.5 required')
    mode=sys.argv[1] if len(sys.argv)>1 else 'check'
    if mode not in ('check','audit'):raise ValueError('mode must be check or audit')
    src=D/f'opg169-a01-c36-incoming-{mode}.py'
    if len(sys.argv)>2 and sys.argv[2]=='--child':
        constrain();os.execv(sys.executable,[sys.executable,str(src)])
    start_utc=datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic()
    outpath=D/f'opg169-a01-c36-incoming-{mode}-output.json';errpath=D/f'opg169-a01-c36-incoming-{mode}-stderr.txt'
    timeout=False
    with outpath.open('wb') as out,errpath.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,mode,'--child'],stdout=out,stderr=err)
        try:code=p.wait(timeout=38)
        except subprocess.TimeoutExpired:p.kill();code=p.wait();timeout=True
    sha=lambda b:hashlib.sha256(b).hexdigest()
    out,err=outpath.read_bytes(),errpath.read_bytes()
    record={'record_kind':'generator_execution','verdict':'candidate_only','trusted_verifier_receipt':False,
            'runtime':platform.python_version(),'started_at_utc':start_utc,'elapsed_seconds':round(time.monotonic()-start,6),
            'command':['python3',str(src)],'exit_code':code,'timeout':timeout,
            'source_sha256':sha(src.read_bytes()),'input_sha256':sha((D/'opg169-a01-c36-input.json').read_bytes()),
            'wrapper_sha256':sha(Path(__file__).read_bytes()),'executable_sha256':sha(Path(sys.executable).read_bytes()),
            'stdout_sha256':sha(out),'stdout_bytes':len(out),'stderr_sha256':sha(err),'stderr_bytes':len(err),
            'limits':{'cpu_affinity_count':1,'memory_bytes':536870912,'cpu_seconds':30,'wall_alarm_seconds':35,
                      'parent_timeout_seconds':38,'output_file_bytes':1048576,'network':'seccomp denied socket/socketpair/connect'},
            'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,
                          'elaboration':'not_run','axiom_report':None}}
    if mode=='audit':record['certificate_sha256']=sha((D/'opg169-a01-c36-incoming-certificate.json').read_bytes())
    (D/f'opg169-a01-c36-incoming-{mode}-execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    return code
if __name__=='__main__':sys.exit(main())
