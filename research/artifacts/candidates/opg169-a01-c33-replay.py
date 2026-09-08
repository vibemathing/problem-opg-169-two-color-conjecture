"""Resource-bounded C33 generator replay. Does not sign trusted receipts."""
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
S=D/'opg169-a01-c33-check.py'
I=D/'opg169-a01-c33-input.json'
O=D/'opg169-a01-c33-summary.json'
E=D/'opg169-a01-c33-stderr.txt'


def constrain():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(85,86))
    resource.setrlimit(resource.RLIMIT_FSIZE,(524288,524288))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    signal.alarm(90)
    lib=ctypes.CDLL(ctypes.util.find_library('seccomp'))
    lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_load.argtypes=[ctypes.c_void_p];lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx:raise RuntimeError('seccomp init failed')
    for name in (b'socket',b'socketpair',b'connect'):
        num=lib.seccomp_syscall_resolve_name(name)
        if num<0 or lib.seccomp_rule_add(ctx,0x00050001,num,0)!=0:raise RuntimeError('seccomp rule failed')
    if lib.seccomp_load(ctx)!=0:raise RuntimeError('seccomp load failed')
    lib.seccomp_release(ctx)


def main():
    if platform.python_version()!='3.13.5':raise RuntimeError('requires CPython 3.13.5')
    if len(sys.argv)>1 and sys.argv[1]=='--child':
        constrain();os.execv(sys.executable,[sys.executable,str(S),str(I)])
    start=time.monotonic();utc=datetime.datetime.now(datetime.timezone.utc).isoformat();timeout=False
    with O.open('wb') as out,E.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,'--child'],stdout=out,stderr=err)
        try:code=p.wait(timeout=95)
        except subprocess.TimeoutExpired:p.kill();code=p.wait();timeout=True
    h=lambda data:hashlib.sha256(data).hexdigest()
    stdout,stderr=O.read_bytes(),E.read_bytes()
    rec={'verdict':'candidate_only','record_kind':'generator_execution','trusted_verifier_receipt':False,
         'authorization':'Direct user request for bounded finite local-type controls; no registry or profile promotion.',
         'runtime':platform.python_version(),'started_utc':utc,'exit_code':code,'timeout':timeout,
         'elapsed_seconds':round(time.monotonic()-start,6),'command':['python3',str(S),str(I)],
         'source_sha256':h(S.read_bytes()),'input_sha256':h(I.read_bytes()),
         'wrapper_sha256':h(Path(__file__).read_bytes()),'executable_sha256':h(Path(sys.executable).read_bytes()),
         'stdout_sha256':h(stdout),'stdout_bytes':len(stdout),'stderr_sha256':h(stderr),'stderr_bytes':len(stderr),
         'limits':{'cpu_affinity_count':1,'memory_bytes':536870912,'cpu_seconds':85,'wall_alarm_seconds':90,
                   'parent_timeout_seconds':95,'output_file_bytes':524288,'summary_cap_bytes':65536,
                   'network':'seccomp denied socket/socketpair/connect'},
         'compute_route':'CPU: finite integer-bitset and face-permutation checks; no floating or GPU operations.',
         'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,
                       'elaboration':'not_run','axiom_report':None}}
    (D/'opg169-a01-c33-execution.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True))
    return code


if __name__=='__main__':
    sys.exit(main())
