#!/usr/bin/env python3
"""Independent DFS/BFS consumer for C45 table. Candidate-only."""
from __future__ import annotations
import collections,json,sys

V=tuple(range(6)); B=(0,1,5,3)
BASE={(0,1),(0,4),(1,4),(4,2),(4,3),(2,1),(3,2),(3,0),(2,5)}

def arcs(word,guard=False):
    z=set(BASE)
    z.add((1,5) if word&1 else (5,1))
    z.add((5,3) if word&2 else (3,5))
    if guard:z.add((5,0))
    return z

def check(VV,AA,color):
    adj={v:[] for v in VV};state={v:0 for v in VV}
    for x,y in AA:
        if x in adj and y in adj and color[x]==color[y]:adj[x].append(y)
    def dfs(x):
        state[x]=1
        for y in adj[x]:
            if state[y]==1:return False
            if state[y]==0 and not dfs(y):return False
        state[x]=2;return True
    for x in VV:
        if state[x]==0 and not dfs(x):return None
    out=set()
    for s in B:
        q=collections.deque(adj[s]);seen=set()
        while q:
            x=q.popleft()
            if x in seen:continue
            seen.add(x);q.extend(adj[x])
        out.update((s,t) for t in B if t in seen)
    return out

def all_p(A,bw):
    vals=[]
    for cc in (0,1):
        for ca in (0,1):
            col={x:(bw>>B.index(x))&1 for x in B};col[4]=cc;col[2]=ca
            r=check(V,A,col)
            if r is not None:vals.append((cc,ca,r))
    return vals

def verify_rule(word,rule,guard=False):
    P=arcs(word,guard); delete=set(rule["delete"]); QV=tuple(v for v in V if v not in delete)
    Q={e for e in P if not(set(e)&delete)}
    for e in map(tuple,rule["adds"]):
        assert (e[1],e[0]) not in Q;Q.add(e)
    pp=collections.defaultdict(list)
    for bits in range(64):
        c={v:(bits>>v)&1 for v in V};r=check(V,P,c)
        if r is not None:
            bw=sum(c[v]<<i for i,v in enumerate(B));pp[bw].append((bits,r))
    st=collections.Counter();saved={x["q_bits"]:x["p_bits"] for x in rule["lifts"]}
    for qb in range(1<<len(QV)):
        cq={v:(qb>>i)&1 for i,v in enumerate(QV)};rq=check(QV,Q,cq)
        if rq is None:continue
        st["valid"]+=1;bw=sum(cq[v]<<i for i,v in enumerate(B))
        good=[x for x in pp[bw] if x[1]<=rq]
        if not good:
            st["fail"]+=1
            st["ordinary_nonextension" if not pp[bw] else "relation_only"]+=1
        else:
            assert qb in saved
            pb=saved[qb];cp={v:(pb>>v)&1 for v in V};rp=check(V,P,cp)
            assert rp is not None and rp<=rq
            st["equal" if rp==rq else "strict"]+=1
    for k in ("valid_q","fail","ordinary_nonextension","relation_only","equal","strict"):
        assert st[{"valid_q":"valid"}.get(k,k)]==rule[k],(k,st,rule)
    return st

def main(path):
    d=json.load(open(path,encoding="utf-8"))
    assert d["format"]=="opg169-c45-first-residual-endpoint-d4-v1"
    cov=collections.Counter();lifts=0;guard_fails=0
    for row in d["rows"]:
        w=row["word"];cov[row["class"]]+=1
        st=verify_rule(w,row["rule"]);assert st["fail"]==0
        lifts+=len(row["rule"]["lifts"])
        if row["guard"] is not None:
            fb=row["guard_failure_fallback"];st2=verify_rule(w,fb,True)
            assert st2["fail"]==2 and st2["ordinary_nonextension"]==2
            assert fb["first_failure"]["boundary_word"]==2
            guard_fails+=1
    assert dict(cov)=={"unconditional":2,"conditional":2}
    assert lifts==88 and d["selected_positive_lifts"]==88
    assert guard_fails==2
    for w in (2,3):
        P=arcs(w,True)
        bc={0:0,1:1,5:0,3:0}
        for ca in (0,1):
            for cu in (0,1):
                c=dict(bc);c[2]=ca;c[4]=cu
                assert check(V,P,c) is None
    print(json.dumps({"format":"opg169-c45-audit-v1","status":"ok",
      "coverage":{"unconditional":2,"conditional":2,"guard_failure_children":2},
      "selected_positive_lifts":88,"guard_failure_boundary_word":2,
      "same_boundary_strict_replacement_obstruction":"analytic certificate checked"},sort_keys=True,separators=(",",":")))
if __name__=="__main__":main(sys.argv[1])
