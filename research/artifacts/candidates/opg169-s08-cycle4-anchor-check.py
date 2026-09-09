#!/usr/bin/env python3
"""Check that every ATC-any-old anchor used in Cycle 3 is an actual directed face of P."""
from __future__ import annotations
import hashlib,json,sys
from pathlib import Path

BASE={(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),(4,5),(4,8),
      (5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7),(11,12),
      (13,12),(13,8),(12,7),(7,13)}
BASE_FACES=[(0,2,3),(0,6,2),(0,5,6),(0,4,5),(0,3,4),
            (2,7,3),(2,11,7),(2,6,11),(3,8,4),(3,7,8),
            (8,7,13),(13,7,12),(12,7,11)]
SPECS={'P10':(14,12,4),'P11':(14,12,5),'P12':(14,15,2),'P13':(14,15,4),'P14':(14,15,5)}
RESULT=Path(__file__).with_name("opg169-s08-cycle4-anchored-results.json")

def graph(name):
    q,r,w=SPECS[name];A=set(BASE)
    A.update({(5,q),(q,4),(q,r) if w&1 else (r,q),(r,8) if w&2 else (8,r),(r,4) if w&4 else (4,r)})
    F=BASE_FACES+[(5,4,q),(q,4,r),(r,4,8)]
    return A,{frozenset(f) for f in F}

def directed_on(A,t):
    a,b,c=t
    return (((a,b) in A and (b,c) in A and (c,a) in A) or
            ((a,c) in A and (c,b) in A and (b,a) in A))

if len(sys.argv)>1:
    RESULT=Path(sys.argv[1])
d=json.loads(RESULT.read_text())
out={}
for row in d['cycle2_selected_rules']:
    name=row['id'];A,faces=graph(name);checks=[]
    for tri in row['symbolic_possible_new_directed_triangles']:
        ok=[]
        for edge,wits in tri['anchor_witnesses'].items():
            for w in wits:
                if frozenset(w) in faces and directed_on(A,w):
                    ok.append({'edge':edge,'face':w})
        assert ok,(name,tri)
        checks.append({'new_cycle':tri['cycle'],'facial_anchors':ok})
    out[name]=checks
payload={'format':'opg169-s08-cycle3-facial-anchor-check-v1','status':'ok',
         'result_sha256':hashlib.sha256(RESULT.read_bytes()).hexdigest(),
         'parents':out,'root_closed':False}
raw=json.dumps(payload,sort_keys=True,separators=(',',':'))+'\n'
target=Path(sys.argv[2]) if len(sys.argv)>2 else Path(__file__).with_name("opg169-s08-cycle4-anchor-output.json")
target.write_text(raw)
print(raw,end='')
