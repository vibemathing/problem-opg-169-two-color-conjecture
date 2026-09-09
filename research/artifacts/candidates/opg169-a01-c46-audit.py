#!/usr/bin/env python3
"""Independent DFS/BFS consumer for C46. Candidate-only."""
from __future__ import annotations
import collections,json,sys
V=tuple(range(6));B=(0,1,3)

def vr(VV,A,c):
    adj={v:[] for v in VV};state={v:0 for v in VV}
    for x,y in A:
        if x in adj and y in adj and c[x]==c[y]:adj[x].append(y)
    def dfs(x):
        state[x]=1
        for y in adj[x]:
            if state[y]==1:return False
            if state[y]==0 and not dfs(y):return False
        state[x]=2;return True
    for x in VV:
        if state[x]==0 and not dfs(x):return None
    R=set()
    for s in B:
        q=collections.deque(adj[s]);seen=set()
        while q:
            x=q.popleft()
            if x in seen:continue
            seen.add(x);q.extend(adj[x])
        R.update((s,t) for t in B if t in seen)
    return R

def main(path):
    d=json.load(open(path,encoding="utf-8"));assert d["format"]=="opg169-c46-octahedral-guard-child-v1"
    assert d["word2"]["z_indegree"]==1 and d["word2"]["z_outdegree"]==3
    w=d["word3"];A={tuple(e) for e in w["arcs"]}
    assert len({frozenset(e) for e in A})==12
    assert all(frozenset(e) not in {frozenset(x) for x in A} for e in ((0,2),(1,3),(4,5)))
    rule=w["rule"];QV=tuple(rule["q_vertices"]);QA={e for e in A if 2 not in e}|{tuple(rule["add"])}
    saved={x["q_bits"]:x["p_bits"] for x in rule["lifts"]}
    valid=equal=fail=0
    for qb in range(1<<len(QV)):
        cq={v:(qb>>i)&1 for i,v in enumerate(QV)};rq=vr(QV,QA,cq)
        if rq is None:continue
        valid+=1;assert qb in saved
        pb=saved[qb];cp={v:(pb>>v)&1 for v in V};rp=vr(V,A,cp)
        if rp is None or not rp<=rq:fail+=1
        elif rp==rq:equal+=1
    assert (valid,fail,equal)==(16,0,16)
    print(json.dumps({"format":"opg169-c46-audit-v1","status":"ok",
      "coverage":{"structural":1,"unconditional":1,"remaining":0},
      "valid_q":16,"equal_relations":16,"octahedron_edges":12},sort_keys=True,separators=(",",":")))
if __name__=="__main__":main(sys.argv[1])
