#!/usr/bin/env python3
"""Audit or reproduce the split C42 candidate capsule."""
from __future__ import annotations
import argparse, base64, hashlib, json, pathlib, subprocess, tempfile, zlib
ROOT=pathlib.Path(__file__).resolve().parents[3]
C=ROOT/'research/artifacts/candidates'
M=C/'opg169-a01-c42-capsule-manifest.json'
def sha(b): return hashlib.sha256(b).hexdigest()
def decode():
    m=json.loads(M.read_text())
    chunks=[]
    for row in m['parts']:
        b=(C/row['name']).read_bytes(); assert len(b)==row['size']; assert sha(b)==row['sha256']; chunks.append(b)
    cap=b''.join(chunks); assert len(cap)==m['assembled_size']; assert sha(cap)==m['assembled_sha256']
    outer=json.loads(cap); raw=zlib.decompress(base64.b64decode(outer['zlib_b64']))
    assert len(raw)==outer['decoded_size']; assert sha(raw)==outer['decoded_sha256']
    inner=json.loads(raw); assert inner['format']=='opg169-c42-inner-file-map-v1'; assert len(inner['files'])==outer['inner_file_count']
    for name,text in inner['files'].items(): assert sha(text.encode())==outer['inner_sha256'][name]
    return m,outer,inner
def audit():
    m,o,i=decode(); return {'format':'opg169-c42-split-audit-v1','status':'ok','mode':'audit','parts':m['part_count'],'inner_files':len(i['files']),'decoded_size':o['decoded_size'],'decoded_sha256':o['decoded_sha256']}
def reproduce():
    m,o,i=decode()
    with tempfile.TemporaryDirectory(prefix='opg169-c42-') as td:
        root=pathlib.Path(td); d=root/'research/artifacts/candidates'; d.mkdir(parents=True)
        for n,t in i['files'].items(): (d/n).write_text(t)
        cmds=[['python3',str(d/'opg169-a01-c42-replay.py'),'reproduce'],['python3',str(d/'opg169-a01-c42-pinch-audit.py')],['python3',str(d/'opg169-a01-c42-guard-face-wheel.py')],['python3',str(d/'opg169-a01-c42-guard-face-wheel-audit.py')],['python3',str(d/'opg169-a01-c42-final-audit.py')]]
        outs=[]
        for cmd in cmds:
            p=subprocess.run(cmd,cwd=root,check=True,capture_output=True,text=True,timeout=90); outs.append(json.loads(p.stdout))
        assert outs[0]['status']=='ok' and outs[0]['successes']==0
        assert outs[1]['status']=='ok'; assert outs[2]['counts']=={'guarded':24,'residual':15,'unguarded':9}; assert outs[3]['status']=='ok'; assert outs[4]['status']=='ok'
    r=audit(); r.update(mode='reproduce',two_lobe_pairs=357048,two_lobe_successes=0,common_boundary_words=[22,54,73,105]); return r
def main():
    p=argparse.ArgumentParser(); p.add_argument('mode',choices=['audit','reproduce'],nargs='?',default='audit'); a=p.parse_args(); print(json.dumps(audit() if a.mode=='audit' else reproduce(),sort_keys=True,separators=(',',':')))
if __name__=='__main__': main()
