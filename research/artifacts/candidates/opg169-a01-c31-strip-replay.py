"""Replay the exact C31 strip checker and capture a bounded generator record.
Run at the repository root with CPython 3.13.5. The child imposes resource
and network limits; the parent enforces an additional 30-second timeout.
"""
import hashlib
import json
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

PREFIX = Path('research/artifacts/candidates')
SOURCE = PREFIX / 'opg169-a01-c31-strip-check.py'
OUTPUT = PREFIX / 'opg169-a01-c31-strip-output.json'
RECORD = PREFIX / 'opg169-a01-c31-strip-execution.json'


def main():
    if platform.python_version() != '3.13.5':
        raise RuntimeError('CPython 3.13.5 required')
    err = PREFIX / 'opg169-a01-c31-strip-stderr.txt'
    start = time.monotonic()
    timed = False
    captured = PREFIX / 'opg169-a01-c31-strip-stdout.txt'
    with captured.open('wb') as out, err.open('wb') as stderr:
        proc = subprocess.Popen([sys.executable, str(SOURCE)], stdout=out, stderr=stderr)
        try:
            code = proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            proc.kill()
            code = proc.wait()
            timed = True
    h = lambda x: hashlib.sha256(x).hexdigest()
    o, e = captured.read_bytes(), err.read_bytes()
    data = json.loads(o) if code == 0 and not timed else {'complete':False}
    summary = dict(data)
    if 'cases' in summary:
        summary['cases'] = [{k:v for k,v in row.items() if k not in ('arcs','rotation','faces')} for row in summary['cases']]
    summary['storage'] = 'compact parsed stdout; complete profiles retained; rotations regenerate from source'
    summary['captured_stdout_sha256'] = h(o)
    OUTPUT.write_text(json.dumps(summary,sort_keys=True,separators=(',',':'))+'\n')
    d = {'verdict':'candidate_only','record_kind':'generator_execution',
         'trusted_verifier_receipt':False,'runtime':platform.python_version(),
         'command':['python3',str(SOURCE)],'exit_code':code,'timeout':timed,
         'elapsed_seconds':round(time.monotonic()-start,6),
         'executable_sha256':h(Path(sys.executable).read_bytes()),
         'source_sha256':h(SOURCE.read_bytes()),'wrapper_sha256':h(Path(__file__).read_bytes()),
         'stdout_bytes':len(o),'stderr_bytes':len(e),'stdout_sha256':h(o),'stderr_sha256':h(e),
         'published_summary_sha256':h(OUTPUT.read_bytes()),
         'limits':{'cpu_affinity_count':1,'cpu_seconds':20,'memory_bytes':536870912,
                   'network':'seccomp denied socket/socketpair/connect',
                   'output_file_bytes':65536,'wall_alarm_seconds':25,'parent_timeout_seconds':30},
         'lean_probe':{'lean_found':shutil.which('lean') is not None,
                       'elan_found':shutil.which('elan') is not None,
                       'elaboration':'not_run','axiom_report':None}}
    RECORD.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
    print(json.dumps(d,sort_keys=True))
    return code


if __name__ == '__main__':
    sys.exit(main())
