"""Pinned bounded generator replay; no trusted verifier/admission authority."""
import ctypes
import ctypes.util
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import subprocess
import sys
import tempfile
import time

SOURCE = 'research/artifacts/candidates/opg169-a01-root-boundary-20260907-patch-checker.py'
INPUT = 'research/artifacts/candidates/opg169-a01-root-boundary-20260907-patch.json'
SOURCE_HASH = 'f62b7783d71b1894051e3685734c7baaa14950313b79c8dddaf32a1a04ada184'
INPUT_HASH = 'b5305848186372232ebb8c95c13c360ada4d2e4bd2ee81eef72a294d0873b523'
REVISION = 'a6a32a2204523d9def3d72ac98767ade2ea60aca'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    if platform.python_version() != '3.13.5':
        raise RuntimeError('This replay is pinned to CPython 3.13.5')
    if platform.python_implementation() != 'CPython':
        raise RuntimeError('Wrong interpreter implementation')
    if digest(SOURCE) != SOURCE_HASH or digest(INPUT) != INPUT_HASH:
        raise RuntimeError('Frozen source or input mismatch')
    lib = ctypes.CDLL(ctypes.util.find_library('seccomp'))
    lib.seccomp_init.argtypes = [ctypes.c_uint32]
    lib.seccomp_init.restype = ctypes.c_void_p
    lib.seccomp_syscall_resolve_name.argtypes = [ctypes.c_char_p]
    lib.seccomp_syscall_resolve_name.restype = ctypes.c_int
    lib.seccomp_rule_add.argtypes = [ctypes.c_void_p, ctypes.c_uint32, ctypes.c_int, ctypes.c_uint]
    lib.seccomp_load.argtypes = [ctypes.c_void_p]
    lib.seccomp_release.argtypes = [ctypes.c_void_p]

    def constrain():
        resource.setrlimit(resource.RLIMIT_AS, (536870912, 536870912))
        resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
        resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
        ctx = lib.seccomp_init(0x7fff0000)
        if not ctx:
            raise RuntimeError('seccomp initialization failed')
        for name in [b'socket', b'socketpair', b'connect']:
            number = lib.seccomp_syscall_resolve_name(name)
            if number < 0 or lib.seccomp_rule_add(ctx, 0x50001, number, 0) != 0:
                raise RuntimeError('seccomp rule failed')
        if lib.seccomp_load(ctx) != 0:
            raise RuntimeError('seccomp load failed')
        lib.seccomp_release(ctx)

    env = dict(os.environ)
    for name in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS']:
        env[name] = '1'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['PYTHONHASHSEED'] = '0'
    started = datetime.now(timezone.utc).isoformat()
    timer = time.monotonic()
    expired = False
    with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
        proc = subprocess.Popen([sys.executable, SOURCE, INPUT], stdout=out, stderr=err,
                                env=env, preexec_fn=constrain, start_new_session=True)
        try:
            code = proc.wait(timeout=25)
        except subprocess.TimeoutExpired:
            expired = True
            os.killpg(proc.pid, 9)
            code = proc.wait()
        out.seek(0)
        err.seek(0)
        stdout, stderr = out.read(65537), err.read(65537)
    if len(stdout) > 65536 or len(stderr) > 65536:
        raise RuntimeError('Output cap exceeded')
    report = {
        'verdict': 'candidate_only', 'kind': 'generator_replay_record',
        'registered_verifier_receipt': False, 'source_revision': REVISION,
        'started_at_utc': started, 'command': ['python3', SOURCE, INPUT],
        'runtime': {'implementation': 'CPython', 'version': platform.python_version(),
                    'executable_sha256': digest(sys.executable)},
        'source_sha256': SOURCE_HASH, 'input_sha256': INPUT_HASH,
        'wrapper_sha256': digest(__file__),
        'limits': {'wall_seconds': 25, 'cpu_seconds': 20, 'memory_bytes': 536870912,
                   'cpu_affinity_count': 1, 'per_output_file_bytes': 65536,
                   'network': 'seccomp denies socket, socketpair, connect'},
        'exit_code': code, 'wall_timeout': expired,
        'elapsed_seconds': round(time.monotonic()-timer, 6),
        'stdout_sha256': hashlib.sha256(stdout).hexdigest(), 'stdout_bytes': len(stdout),
        'stderr_sha256': hashlib.sha256(stderr).hexdigest(), 'stderr_bytes': len(stderr),
        'lean_probe': {'method': 'PATH lookup', 'lean_found': bool(shutil.which('lean')),
                       'elan_found': bool(shutil.which('elan')), 'elaboration': 'not_run',
                       'axiom_report': None},
        'authorization': 'Direct user request for bounded candidate self-tests; no trusted runtime admission asserted',
        'summary': json.loads(stdout) if code == 0 and not expired else None
    }
    print(json.dumps(report, sort_keys=True, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
