#!/usr/bin/env python3
"""Independent combinatorial plane-embedding check for the P12 exterior witness."""
from collections import Counter
import hashlib, json
from pathlib import Path
import sys

BASE={(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),(4,5),(4,8),
      (5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7),(11,12),
      (13,12),(13,8),(12,7),(7,13)}
# P12 = q=14,r=15,w=2.
A=set(BASE)|{(5,14),(14,4),(15,14),(15,8),(4,15),(6,14),(13,6)}
inside=[(0,2,3),(0,6,2),(0,5,6),(0,4,5),(0,3,4),
        (2,7,3),(2,11,7),(2,6,11),(3,8,4),(3,7,8),
        (8,7,13),(13,7,12),(12,7,11),
        (5,4,14),(14,4,15),(15,4,8)]
outside=[(5,14,6),(14,15,8,13,6),(13,12,11,6)]
faces=inside+outside
V={x for e in A for x in e}
U={frozenset(e) for e in A}
assert all(u!=v for u,v in A)
assert all((v,u) not in A for u,v in A)
face_edges=Counter(); darts=Counter()
for f in faces:
    assert len(f)==len(set(f))
    for u,v in zip(f,f[1:]+f[:1]):
        assert frozenset((u,v)) in U, (f,u,v)
        face_edges[frozenset((u,v))]+=1
        darts[(u,v)]+=1
assert set(face_edges)==U
assert all(n==2 for n in face_edges.values())
assert all(darts[(u,v)]==1 and darts[(v,u)]==1 for e in U for u,v in [tuple(e)])
assert len(V)-len(U)+len(faces)==2
# The two exterior chords are explicitly on the same side of the old boundary
# and occur in opposite directions on their two incident face boundaries.
assert face_edges[frozenset((6,14))]==2
assert face_edges[frozenset((6,13))]==2
out={
 'status':'ok','format':'opg169-s08-cycle3-p12-plane-witness-v1',
 'vertices':len(V),'edges':len(U),'faces':len(faces),'euler':len(V)-len(U)+len(faces),
 'inside_faces':len(inside),'outside_faces':[list(f) for f in outside],
 'extra_actual_arcs':[[6,14],[13,6]],'root_closed':False,
}
raw=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
target=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("opg169-s08-cycle4-plane-output.json")
target.write_text(raw)
print(raw,end='')
