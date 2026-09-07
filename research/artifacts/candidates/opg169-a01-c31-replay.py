"""Bounded C31 candidate replay, not a trusted verifier adapter.
Run from repository root. Requires Linux libseccomp and CPython 3.13.5.
"""
import ctypes
import ctypes.util
import hashlib
import json
import os
import platform
import resource
import shutil
import subprocess
import sys
import time
from pathlib import Path

PREFIX = Path('research/artifacts/candidates')
SOURCE = PREFIX / 'opg169-a01-c31-core-family-check.py'
INPUT = PREFIX / 'opg169-a01-c31-core-family-input.json'
OUTPUT = PREFIX / 'opg169-a01-c31-output.json'
RECORD = PREFIX / 'opg169-a01-c31-execution.json'


def limit_child():
    resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))
    resource.setrlimit(resource.RLIMIT_CPU, (35, 36))
    resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    lib = ctypes.CDLL(ctypes.util.find_library('seccomp'))
    lib.seccomp_init.argtypes = [ctypes.c_uint32]
    lib.seccomp_init.restype = ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes = [ctypes.c_char_p]
    lib.seccomp_rule_add.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint]
    lib.seccomp_load.argtypes = [ctypes.c_void_p]
    lib.seccomp_release.argtypes = [ctypes.c_void_p]
    ctx = lib.seccomp_init(0x7fff0000)
    if not ctx:
        raise RuntimeError('seccomp initialization')
    for name in (b'socket', b'socketpair', b'connect'):
        call = lib.seccomp_syscall_resolve_name(name)
        if call < 0 or lib.seccomp_rule_add(ctx, 0x00050001, call, 0) != 0:
            raise RuntimeError('seccomp rule')
    if lib.seccomp_load(ctx) != 0:
        raise RuntimeError('seccomp load')
    lib.seccomp_release(ctx)


def main():
    if platform.python_implementation() != 'CPython' or platform.python_version() != '3.13.5':
        raise RuntimeError('required CPython 3.13.5')
    if not ctypes.util.find_library('seccomp'):
        raise RuntimeError('required libseccomp')
    err = PREFIX / 'opg169-a01-c31-stderr.txt'
    start = time.monotonic()
    timed = False
    with OUTPUT.open('wb') as out, err.open('wb') as stderr:
        proc = subprocess.Popen([sys.executable, str(SOURCE), str(INPUT)],
                                stdout=out, stderr=stderr, preexec_fn=limit_child,
                                env={**os.environ, 'PYTHONHASHSEED':'0', 'OMP_NUM_THREADS':'1'})
        try:
            code = proc.wait(timeout=40)
        except subprocess.TimeoutExpired:
            proc.kill()
            code = proc.wait()
            timed = True
    h = lambda b: hashlib.sha256(b).hexdigest()
    stdout, stderr = OUTPUT.read_bytes(), err.read_bytes()
    record = {'verdict':'candidate_only', 'record_kind':'generator_execution',
              'trusted_verifier_receipt':False, 'runtime':platform.python_version(),
              'executable_sha256':h(Path(sys.executable).read_bytes()),
              'source_sha256':h(SOURCE.read_bytes()), 'input_sha256':h(INPUT.read_bytes()),
              'wrapper_sha256':h(Path(__file__).read_bytes()),
              'command':['python3',str(SOURCE),str(INPUT)], 'exit_code':code,
              'timeout':timed, 'elapsed_seconds':round(time.monotonic()-start,6),
              'limits':{'wall_seconds':40,'cpu_seconds':35,'memory_bytes':536870912,
                        'cpu_affinity_count':1,'output_file_bytes':65536,
                        'network':'seccomp denied socket/socketpair/connect'},
              'stdout_sha256':h(stdout),'stderr_sha256':h(stderr),
              'stdout_bytes':len(stdout),'stderr_bytes':len(stderr),
              'lean_probe':{'lean_found':shutil.which('lean') is not None,
                            'elan_found':shutil.which('elan') is not None,
                            'elaboration':'not_run','axiom_report':None}}
    RECORD.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps(record,sort_keys=True))
    return 1 if timed else code


if __name__ == '__main__':
    sys.exit(main())
