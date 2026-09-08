"""Bounded C34 generator replay. Run from a repository-shaped root.
No registered verification or admission authority is claimed.
"""
import ctypes, ctypes.util, hashlib, json, os, platform, resource
import shutil, signal, subprocess, sys, time
from pathlib import Path
D=Path('research/artifacts/candidates')
S=D/'opg169-a01-c34-check.py'; I=D/'opg169-a01-c34-input.json'
INDEX=int(sys.argv[-1])
if INDEX not in range(4): raise ValueError('batch index 0..3 required')
O=D/f'opg169-a01-c34-batch-{INDEX}-raw.json'; E=D/f'opg169-a01-c34-batch-{INDEX}-stderr.txt'
def constrain():
    resource.setrlimit(resource.RLIMIT_AS,(805306368,805306368))
    resource.setrlimit(resource.RLIMIT_CPU,(55,56))
    resource.setrlimit(resource.RLIMIT_FSIZE,(4194304,4194304))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});signal.alarm(60)
    lib=ctypes.CDLL(ctypes.util.find_library('seccomp'))
    lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint]
    lib.seccomp_load.argtypes=[ctypes.c_void_p];lib.seccomp_release.argtypes=[ctypes.c_void_p]
    ctx=lib.seccomp_init(0x7fff0000)
    if not ctx: raise RuntimeError('seccomp init')
    for call in (b'socket',b'socketpair',b'connect'):
        num=lib.seccomp_syscall_resolve_name(call)
        if num<0 or lib.seccomp_rule_add(ctx,0x00050001,num,0): raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx): raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)
def main():
    if platform.python_version()!='3.13.5': raise RuntimeError('CPython 3.13.5 required')
    if len(sys.argv)>1 and sys.argv[1]=='--child':
        constrain();os.execv(sys.executable,[sys.executable,str(S),str(I),str(INDEX)])
    if O.exists() or E.exists(): raise RuntimeError('preserve existing output; use a clean replay workspace')
    start=time.monotonic();timeout=False
    with O.open('wb') as out,E.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,'--child',str(INDEX)],stdout=out,stderr=err)
        try: code=p.wait(timeout=65)
        except subprocess.TimeoutExpired: p.kill();code=p.wait();timeout=True
    h=lambda raw:hashlib.sha256(raw).hexdigest();o=O.read_bytes();e=E.read_bytes()
    record={'verdict':'candidate_only','record_kind':'generator_execution','trusted_verifier_receipt':False,
      'command':['python3',str(S),str(I),str(INDEX)],'runtime':platform.python_version(),
      'exit_code':code,'timeout':timeout,'elapsed_seconds':round(time.monotonic()-start,6),
      'source_sha256':h(S.read_bytes()),'input_sha256':h(I.read_bytes()),
      'wrapper_sha256':h(Path(__file__).read_bytes()),'executable_sha256':h(Path(sys.executable).read_bytes()),
      'stdout_sha256':h(o),'stdout_bytes':len(o),'stderr_sha256':h(e),'stderr_bytes':len(e),
      'limits':{'memory_bytes':805306368,'cpu_seconds':55,'wall_alarm_seconds':60,
        'parent_timeout_seconds':65,'cpu_affinity_count':1,'output_file_bytes':4194304,
        'network':'seccomp denied socket/socketpair/connect'},
      'routing':'CPU exact finite bitset graph tests; no GPU or floating-point result used',
      'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,
                    'elaboration':'not_run','axiom_report':None}}
    (D/f'opg169-a01-c34-batch-{INDEX}-execution.json').write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True));return code
if __name__=='__main__': sys.exit(main())
