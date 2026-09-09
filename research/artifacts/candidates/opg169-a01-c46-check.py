#!/usr/bin/env python3
"""C46 exact octahedral guard-failure child. Candidate-only."""
from __future__ import annotations
import collections,json,platform

# 0=8,1=12,2=a,3=b,4=u,5=z
V=tuple(range(6)); B=(0,1,3)
BASE={(0,1),(0,4),(1,4),(4,2),(4,3),(2,1),(3,2),(3,0),(2,5),(5,3),(5,0)}

def arcs(word):
    A=set(BASE)
    A.add((1,5) if word==3 else (5,1))
    return A

def relation(VV,A,c):
    VV=set(VV);adj={v:[] for v in VV};ind={v:0 for v in VV}
    for x,y in A:
        if x in VV and y in VV and c[x]==c[y]:adj[x].append(y);ind[y]+=1
    q=[v for v in VV if ind[v]==0];n=0
    while q:
        x=q.pop();n+=1
        for y in adj[x]:
            ind[y]-=1
            if ind[y]==0:q.append(y)
    if n!=len(VV):return None
    R=set()
    for s in B:
        todo=list(adj[s]);seen=set()
        while todo:
            x=todo.pop()
            if x in seen:continue
            seen.add(x);todo.extend(adj[x])
        R.update((s,t) for t in B if t in seen)
    return tuple(sorted(R))

def main():
    A2=arcs(2)
    indeg=sum(1 for x,y in A2 if y==5);outdeg=sum(1 for x,y in A2 if x==5)
    assert (indeg,outdeg)==(1,3)
    A=arcs(3)
    und={frozenset(e) for e in A}
    assert len(und)==12
    assert all(frozenset(e) not in und for e in ({0,2},{1,3},{4,5}))
    QV=(0,1,3,4,5)
    QA={e for e in A if 2 not in e}|{(1,3)}
    profiles=collections.defaultdict(list)
    for bits in range(64):
        c={v:(bits>>v)&1 for v in V};rp=relation(V,A,c)
        if rp is None:continue
        bw=sum(c[v]<<i for i,v in enumerate(B));profiles[bw].append((bits,rp))
    valid=equal=strict=fail=0;lifts=[]
    for qb in range(32):
        cq={v:(qb>>i)&1 for i,v in enumerate(QV)};rq=relation(QV,QA,cq)
        if rq is None:continue
        valid+=1;bw=sum(cq[v]<<i for i,v in enumerate(B))
        good=[x for x in profiles[bw] if set(x[1])<=set(rq)]
        if not good:fail+=1;continue
        chosen=next((x for x in good if x[1]==rq),good[0])
        if chosen[1]==rq:equal+=1
        else:strict+=1
        lifts.append({"q_bits":qb,"p_bits":chosen[0]})
    assert (valid,fail,equal,strict)==(16,0,16,0)
    out={"format":"opg169-c46-octahedral-guard-child-v1","verdict":"candidate_only",
      "labels":{"0":8,"1":12,"2":"a","3":"b","4":"u","5":"z"},
      "word2":{"class":"structural_semidegree","z_indegree":1,"z_outdegree":3},
      "word3":{"class":"unconditional_reduction",
        "arcs":[list(e) for e in sorted(A)],
        "rotations":{"u":[0,1,2,3],"a":[1,4,3,5],"z":[1,2,3,0]},
        "faces":[[4,0,1],[4,1,2],[4,2,3],[4,3,0],[5,1,2],[5,2,3],[5,3,0],[5,0,1]],
        "underlying_edges":12,
        "missing_pairs":[[0,2],[1,3],[4,5]],
        "rule":{"delete":[2],"add":[1,3],"hole":[1,4,3,5],
          "boundary":[0,1,3],"q_vertices":list(QV),
          "valid_q":valid,"equal":equal,"strict":strict,"lifts":lifts}},
      "coverage":{"structural":1,"unconditional":1,"remaining":0},
      "runtime":{"python":platform.python_version()},
      "scope":"C45 guard-failure words 2/3 with z of complete degree four. Word 3 is the oriented octahedral patch; edge 12-b is absent by the planar six-vertex edge bound and is added in a's deletion hole."}
    print(json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
