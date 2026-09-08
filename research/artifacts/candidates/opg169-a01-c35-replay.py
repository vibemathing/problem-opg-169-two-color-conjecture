"""Bounded C35 generator/consumer replay. No trusted verifier identity."""
import ctypes
import ctypes.util
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

def limits():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(35,36))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});signal.alarm(40)
    name=ctypes.util.find_library('seccomp')
    if not name:raise RuntimeError('seccomp unavailable')
    lib=ctypes.CDLL(name);lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_load.argtypes=[ctypes.c_void_p];lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx:raise RuntimeError('seccomp init')
    for s in (b'socket',b'socketpair',b'connect'):
        num=lib.seccomp_syscall_resolve_name(s)
        if num<0 or lib.seccomp_rule_add(ctx,0x00050001,num,0)!=0:raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx)!=0:raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)


def main():
    if platform.python_version()!='3.13.5':raise RuntimeError('CPython 3.13.5 required')
    mode=sys.argv[1]
    if mode not in ('check','audit'):raise ValueError('mode check or audit')
    source=D/f'opg169-a01-c35-{mode}.py'; inp=D/'opg169-a01-c35-input.json'
    cert=D/'opg169-a01-c35-certificate.json'
    args=[str(source),str(inp)]+([str(cert)] if mode=='audit' else [])
    if '--child' in sys.argv:
        limits();os.execv(sys.executable,[sys.executable]+args)
    output=cert if mode=='check' else D/'opg169-a01-c35-audit-output.json'
    error=D/f'opg169-a01-c35-{mode}-stderr.txt';start=time.monotonic();timeout=False
    with output.open('wb') as out,error.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,mode,'--child'],stdout=out,stderr=err)
        try:code=p.wait(timeout=43)
        except subprocess.TimeoutExpired:p.kill();code=p.wait();timeout=True
    h=lambda b:hashlib.sha256(b).hexdigest();o,e=output.read_bytes(),error.read_bytes()
    record={'record_kind':'bounded_generator_execution','verdict':'candidate_only','trusted_verifier_receipt':False,
            'runtime':platform.python_version(),'command':['python3']+args,'exit_code':code,'timeout':timeout,
            'elapsed_seconds':round(time.monotonic()-start,6),'source_sha256':h(source.read_bytes()),
            'input_sha256':h(inp.read_bytes()),'wrapper_sha256':h(Path(__file__).read_bytes()),
            'executable_sha256':h(Path(sys.executable).read_bytes()),'stdout_sha256':h(o),'stdout_bytes':len(o),
            'stderr_sha256':h(e),'stderr_bytes':len(e),'limits':{'cpu_affinity_count':1,'memory_bytes':536870912,
            'cpu_seconds':35,'wall_alarm_seconds':40,'parent_timeout_seconds':43,'output_file_bytes':1048576,
            'network':'seccomp denied socket/socketpair/connect'},
            'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,
                          'elaboration':'not_run','axiom_report':None}}
    if mode=='audit':record['certificate_sha256']=h(cert.read_bytes())
    (D/f'opg169-a01-c35-{mode}-execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True));return code

if __name__=='__main__':sys.exit(main())
