#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,subprocess,tempfile
ROOT=pathlib.Path(__file__).resolve().parent
TABLE_SHA='c615ca7f9da951061aed0c96fb2c4723856edf7cc5161bdbd9e5db3120554eda'

def reproduce():
    with tempfile.TemporaryDirectory() as td:
        p=pathlib.Path(td)/'table.json'
        r=subprocess.run(['python3',str(ROOT/'opg169-a01-c46-check.py')],capture_output=True,timeout=30)
        assert r.returncode==0 and not r.stderr
        assert hashlib.sha256(r.stdout).hexdigest()==TABLE_SHA
        p.write_bytes(r.stdout)
        a=subprocess.run(['python3',str(ROOT/'opg169-a01-c46-audit.py'),str(p)],capture_output=True,text=True,timeout=30)
        assert a.returncode==0 and not a.stderr
        out=json.loads(a.stdout);assert out['status']=='ok'
    return {'status':'ok','mode':'reproduce','table_sha256':TABLE_SHA,'coverage':{'structural':1,'unconditional':1,'remaining':0},'valid_q':16}
if __name__=='__main__':print(json.dumps(reproduce(),sort_keys=True,separators=(',',':')))
