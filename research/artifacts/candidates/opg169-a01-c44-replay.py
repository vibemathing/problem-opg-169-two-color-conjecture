#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,hashlib,json,pathlib,subprocess,tempfile,zlib
ROOT=pathlib.Path(__file__).resolve().parent
ARC=ROOT/'opg169-a01-c44-guard-face-d4-table-archive.json'

def decode():
    d=json.loads(ARC.read_text())
    raw=zlib.decompress(base64.b64decode(d['zlib_b64']))
    assert len(raw)==d['decoded_size']
    assert hashlib.sha256(raw).hexdigest()==d['decoded_sha256']
    return d,raw

def audit():
    d,raw=decode(); table=json.loads(raw)
    assert table['coverage']=={'conditional':24,'residual':15,'unconditional':9}
    assert table['residual_directed_triangle_distribution']=={'2':10,'3':4,'4':1}
    return {'status':'ok','mode':'audit','decoded_size':len(raw),'decoded_sha256':d['decoded_sha256'],'rows':48}

def reproduce():
    d,raw=decode()
    with tempfile.TemporaryDirectory() as td:
        p=pathlib.Path(td)/'table.json'
        r=subprocess.run(['python3',str(ROOT/'opg169-a01-c44-guard-face-d4-check.py')],capture_output=True,timeout=30)
        assert r.returncode==0 and not r.stderr
        assert r.stdout==raw
        p.write_bytes(raw)
        r2=subprocess.run(['python3',str(ROOT/'opg169-a01-c44-guard-face-d4-audit.py'),str(p)],capture_output=True,text=True,timeout=30)
        assert r2.returncode==0 and not r2.stderr
        a=json.loads(r2.stdout);assert a['status']=='ok'
    return {'status':'ok','mode':'reproduce','decoded_sha256':d['decoded_sha256'],'rows':48,'selected_positive_lift_entries':496}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',nargs='?',choices=['audit','reproduce'],default='audit');x=ap.parse_args()
    print(json.dumps(audit() if x.mode=='audit' else reproduce(),sort_keys=True,separators=(',',':')))
