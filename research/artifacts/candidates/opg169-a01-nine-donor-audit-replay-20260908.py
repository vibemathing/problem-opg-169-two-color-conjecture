"""Resource-bounded generator replay. No trusted-verifier or admission authority."""
import ctypes,ctypes.util,datetime,hashlib,json,os,platform,resource,shutil,signal,subprocess,sys,time
from pathlib import Path
D=Path('research/artifacts/candidates')
S=D/'opg169-a01-nine-donor-audit-20260908.py'
O=D/'opg169-a01-nine-donor-audit-stdout.json'
E=D/'opg169-a01-nine-donor-audit-stderr.txt'

def constrain():
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
    resource.setrlimit(resource.RLIMIT_CPU,(80,81))
    resource.setrlimit(resource.RLIMIT_FSIZE,(1048576,1048576))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});signal.alarm(85)
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
    if len(sys.argv)>1 and sys.argv[1]=='--child':
        constrain();os.execv(sys.executable,[sys.executable,str(S)])
    start=time.monotonic();started=datetime.datetime.now(datetime.timezone.utc).isoformat();timeout=False
    with O.open('wb') as out,E.open('wb') as err:
        p=subprocess.Popen([sys.executable,__file__,'--child'],stdout=out,stderr=err)
        try:code=p.wait(timeout=90)
        except subprocess.TimeoutExpired:p.kill();code=p.wait();timeout=True
    h=lambda b:hashlib.sha256(b).hexdigest()
    out,err=O.read_bytes(),E.read_bytes()
    rec={'verdict':'candidate_only','record_kind':'generator_execution','trusted_verifier_receipt':False,
         'started_at_utc':started,'runtime':platform.python_version(),'command':['python3',str(S)],
         'exit_code':code,'timeout':timeout,'elapsed_seconds':round(time.monotonic()-start,6),
         'source_sha256':h(S.read_bytes()),'wrapper_sha256':h(Path(__file__).read_bytes()),
         'executable_sha256':h(Path(sys.executable).read_bytes()),'stdout_sha256':h(out),'stdout_bytes':len(out),
         'stderr_sha256':h(err),'stderr_bytes':len(err),
         'limits':{'cpu_affinity_count':1,'memory_bytes':536870912,'cpu_seconds':80,'wall_alarm_seconds':85,
                   'parent_timeout_seconds':90,'output_file_bytes':1048576,'network':'seccomp denied socket/socketpair/connect'},
         'lean_probe':{'lean_found':shutil.which('lean') is not None,'elan_found':shutil.which('elan') is not None,
                       'elaboration':'not_run','axiom_report':None}}
    (D/'opg169-a01-nine-donor-audit-execution-20260908.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True));return code

if __name__=='__main__':sys.exit(main())
