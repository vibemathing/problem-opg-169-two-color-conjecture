"""Bounded foreground replay; emits generator provenance, never trusted Evidence."""
import ctypes
import ctypes.util
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

D=Path(__file__).parent
MODES=('0','1','2','3','4','obstruction','audit')

def limits():
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
    resource.setrlimit(resource.RLIMIT_CPU,(35,36))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1<<20,1<<20))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    signal.alarm(40)
    name=ctypes.util.find_library('seccomp')
    if not name:raise RuntimeError('seccomp unavailable')
    lib=ctypes.CDLL(name)
    lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_load.argtypes=[ctypes.c_void_p];lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx:raise RuntimeError('seccomp init')
    for call in (b'socket',b'socketpair',b'connect'):
        nr=lib.seccomp_syscall_resolve_name(call)
        if nr<0 or lib.seccomp_rule_add(ctx,0x00050001,nr,0)!=0:raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx)!=0:raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    mode=sys.argv[1]
    if mode not in MODES:raise ValueError('unknown replay mode')
    if sys.version_info[:3]!=(3,13,5):raise RuntimeError('requires recorded CPython 3.13.5')
    source=D/('opg169-a01-c37-audit.py' if mode=='audit' else 'opg169-a01-c37-check.py')
    out=D/('opg169-a01-c37-'+mode+'-output.json');err=D/('opg169-a01-c37-'+mode+'-stderr.txt')
    args=[sys.executable,source.name]+([] if mode=='audit' else [mode])
    started=dt.datetime.now(dt.timezone.utc).isoformat();t=time.monotonic();timeout=False
    with out.open('wb') as o,err.open('wb') as e:
        try:r=subprocess.run(args,cwd=D,stdout=o,stderr=e,preexec_fn=limits,timeout=43,check=False);code=r.returncode
        except subprocess.TimeoutExpired:code=None;timeout=True
    record={'format':'c37-generator-run-v1','verdict':'candidate_only','mode':mode,'python':sys.version.split()[0],
            'started_at':started,'elapsed_seconds':round(time.monotonic()-t,6),'exit_code':code,'timeout':timeout,
            'source':source.name,'source_sha256':digest(source),'input_sha256':digest(D/'opg169-a01-c37-input.json'),
            'wrapper_sha256':digest(Path(__file__)),'interpreter_sha256':digest(Path(sys.executable)),
            'output':out.name,'output_bytes':out.stat().st_size,'output_sha256':digest(out),'stderr_bytes':err.stat().st_size,
            'stderr_sha256':digest(err),'limits':{'cpu_count':1,'memory_bytes':512<<20,'cpu_seconds':35,'alarm_seconds':40,'parent_timeout_seconds':43,'output_file_bytes':1<<20,'network':'socket/socketpair/connect denied'},
            'trusted_receipt':False,'lean_elaboration':'not_run','axiom_report':None}
    p=D/('opg169-a01-c37-'+mode+'-execution.json');p.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    if code!=0 or timeout:sys.exit(1)
if __name__=='__main__':main()
