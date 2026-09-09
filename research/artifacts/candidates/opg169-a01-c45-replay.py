#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,hashlib,json,pathlib,subprocess,tempfile,zlib
ROOT=pathlib.Path(__file__).resolve().parent
ARC=ROOT/'opg169-a01-c45-table-archive.json'

def decode():
    d=json.loads(ARC.read_text())
    raw=zlib.decompress(base64.b64decode(d['zlib_b64']))
    assert len(raw)==d['decoded_size']
    assert hashlib.sha256(raw).hexdigest()==d['decoded_sha256']
    return d,raw

def audit():
    d,raw=decode();t=json.loads(raw)
    assert t['coverage']=={'conditional':2,'guard_failure_children':2,'unconditional':2}
    assert t['selected_positive_lifts']==88
    return {'status':'ok','mode':'audit','decoded_size':len(raw),'decoded_sha256':d['decoded_sha256'],'rows':4}

def reproduce():
    d,raw=decode()
    with tempfile.TemporaryDirectory() as td:
        p=pathlib.Path(td)/'table.json'
        r=subprocess.run(['python3',str(ROOT/'opg169-a01-c45-check.py')],capture_output=True,timeout=30)
        assert r.returncode==0 and not r.stderr and r.stdout==raw
        p.write_bytes(raw)
        a=subprocess.run(['python3',str(ROOT/'opg169-a01-c45-audit.py'),str(p)],capture_output=True,text=True,timeout=30)
        assert a.returncode==0 and not a.stderr
        out=json.loads(a.stdout);assert out['status']=='ok'
    return {'status':'ok','mode':'reproduce','decoded_sha256':d['decoded_sha256'],'rows':4,'selected_positive_lifts':88}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',nargs='?',choices=['audit','reproduce'],default='audit');x=ap.parse_args()
    print(json.dumps(audit() if x.mode=='audit' else reproduce(),sort_keys=True,separators=(',',':')))
