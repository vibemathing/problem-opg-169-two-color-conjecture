#!/usr/bin/env python3
import base64, hashlib, json, pathlib, subprocess, sys, tempfile, zlib
D=pathlib.Path(__file__).resolve().parent

def need(x,m):
    if not x: raise SystemExit(m)

def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'audit'
    arc=json.loads((D/'opg169-a01-c40-audit-archive.json').read_text())
    raw=zlib.decompress(base64.b64decode(arc['zlib_b64']))
    need(len(raw)==arc['decoded_size'],'decoded audit size')
    need(hashlib.sha256(raw).hexdigest()==arc['decoded_sha256'],'decoded audit sha')
    with tempfile.TemporaryDirectory() as td:
        p=pathlib.Path(td)/'audit.json';p.write_bytes(raw)
        cp=subprocess.run([sys.executable,str(D/'opg169-a01-c40-audit.py'),str(p)],capture_output=True,text=True,check=False)
        need(cp.returncode==0 and not cp.stderr,'audit consumer')
        audit=json.loads(cp.stdout)
    summary=json.loads((D/'opg169-a01-c40-residual-summary.json').read_text())
    executions=json.loads((D/'opg169-a01-c40-executions.json').read_text())
    byid={tuple(x['id']):x for x in executions['residual_searches']}
    need(len(summary['rows'])==14,'summary rows')
    need(sum(x['catalog'] for x in summary['rows'])==6760,'catalog total')
    for row in summary['rows']:
        rec=byid[tuple(row['id'])]
        need(row['raw_sha256']==rec['stdout_sha256'],'raw output sha')
        need(row['raw_size']==rec['stdout_bytes'],'raw output size')
        need(row['catalog']==rec['catalog'] and rec['solution'] is None,'residual identity')
    out={'status':'ok','mode':mode,'audit':audit,'residual':{'files':14,'catalog_total':6760,'status':'ok'}}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
