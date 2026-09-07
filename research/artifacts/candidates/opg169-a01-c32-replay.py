"""Bounded generator replay, not a trusted verifier or admission command.
Run from the repository root. Source/inputs remain unchanged by this wrapper.
"""
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

D = Path('research/artifacts/candidates')
S = D/'opg169-a01-c32-check.py'
I = D/'opg169-a01-c32-input.json'
O = D/'opg169-a01-c32-output.json'
E = D/'opg169-a01-c32-stderr.txt'


def constrain():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(95,96))
    resource.setrlimit(resource.RLIMIT_FSIZE,(65536,65536))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    signal.alarm(100)
    name = ctypes.util.find_library('seccomp')
    if not name:
        raise RuntimeError('libseccomp unavailable')
    lib = ctypes.CDLL(name)
    lib.seccomp_init.argtypes=[ctypes.c_uint32]
    lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_load.argtypes=[ctypes.c_void_p]
    lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx:
        raise RuntimeError('seccomp init')
    for s in (b'socket',b'socketpair',b'connect'):
        num=lib.seccomp_syscall_resolve_name(s)
        if num<0 or lib.seccomp_rule_add(ctx,0x00050001,num,0)!=0:
            raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx)!=0:
        raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)


def main():
    if platform.python_version()!='3.13.5':
        raise RuntimeError('CPython 3.13.5 required')
    if len(sys.argv)>1 and sys.argv[1]=='--child':
        constrain()
        os.execv(sys.executable,[sys.executable,str(S),str(I)])
    start=time.monotonic()
    timeout=False
    with O.open('wb') as out,E.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,'--child'],stdout=out,stderr=err)
        try:
            code=p.wait(timeout=105)
        except subprocess.TimeoutExpired:
            p.kill();code=p.wait();timeout=True
    h=lambda b:hashlib.sha256(b).hexdigest()
    o,e=O.read_bytes(),E.read_bytes()
    rec={'verdict':'candidate_only','record_kind':'generator_execution','trusted_verifier_receipt':False,
         'runtime':platform.python_version(),'command':['python3',str(S),str(I)],
         'exit_code':code,'timeout':timeout,'elapsed_seconds':round(time.monotonic()-start,6),
         'source_sha256':h(S.read_bytes()),'input_sha256':h(I.read_bytes()),
         'wrapper_sha256':h(Path(__file__).read_bytes()),'executable_sha256':h(Path(sys.executable).read_bytes()),
         'stdout_sha256':h(o),'stdout_bytes':len(o),'stderr_sha256':h(e),'stderr_bytes':len(e),
         'limits':{'cpu_affinity_count':1,'memory_bytes':536870912,'cpu_seconds':95,'wall_alarm_seconds':100,
                   'parent_timeout_seconds':105,'output_file_bytes':65536,'network':'seccomp denied socket/socketpair/connect'},
         'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,
                       'elaboration':'not_run','axiom_report':None}}
    (D/'opg169-a01-c32-execution.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True))
    return code


if __name__=='__main__':
    sys.exit(main())
