#!/usr/bin/env python3
import collections, itertools, json, sys, time

BASE_ARCS={(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),(4,5),(4,8),
(5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7),
(11,12),(13,12),(13,8),(12,7),(7,13)}
I={0,2,3,4,7}

def make_graph(qk,rk,w):
    q=14 if qk=='new' else int(qk); r=15 if rk=='new' else int(rk)
    A=set(BASE_ARCS)
    for e in [(5,q),(q,4),(q,r) if w&1 else (r,q),(r,8) if w&2 else (8,r),(r,4) if w&4 else (4,r)]:
        if e[0]==e[1] or (e[1],e[0]) in A: return None
        A.add(e)
    return {0,2,3,4,5,6,7,8,11,12,13,q,r},A,q,r

def rel(A,V,B,c):
    adj={v:[] for v in V}
    for u,v in A:
        if u in V and v in V and c[u]==c[v]:adj[u].append(v)
    state={v:0 for v in V}
    def dfs(v):
        state[v]=1
        for z in adj[v]:
            if state[z]==1:return False
            if state[z]==0 and not dfs(z):return False
        state[v]=2;return True
    for v in V:
        if state[v]==0 and not dfs(v):return None
    out=set()
    for s in B:
        seen=set();todo=list(adj[s])
        while todo:
            z=todo.pop()
            if z in seen:continue
            seen.add(z);todo.extend(adj[z])
        out|={(s,t) for t in B if t in seen}
    return frozenset(out)

def colourings(V):
    vs=sorted(V)
    for bits in range(1<<len(vs)):
        yield {v:(bits>>i)&1 for i,v in enumerate(vs)},bits

def pprofiles(V,A,B):
    P=collections.defaultdict(set)
    for c,_ in colourings(V):
        r=rel(A,V,B,c)
        if r is not None:P[tuple(c[v] for v in B)].add(r)
    return P

def test(V,A,B,P,dv,adds):
    QV=V-{dv};QA={e for e in A if dv not in e}|set(adds)
    valid=fail=ordinary=relation=equal=strict=0;first=None
    for c,bits in colourings(QV):
        rq=rel(QA,QV,B,c)
        if rq is None:continue
        valid+=1;ps=P[tuple(c[v] for v in B)]
        got=[rp for rp in ps if rp<=rq]
        if got:
            if rq in got:equal+=1
            else:strict+=1
        else:
            fail+=1
            kind='relation' if ps else 'ordinary'
            if kind=='relation':relation+=1
            else:ordinary+=1
            if first is None:first=[bits,kind]
    return [valid,fail,equal,strict,ordinary,relation,first]

def hole(dv,q,r):
    return {0:[2,6,5,4,3],2:[0,3,7,11,6],3:[0,4,8,7,2],
            4:[0,5,q,r,8,3],7:[2,3,8,13,12,11]}[dv]

def candidates(poly,A):
    n=len(poly)
    pairs=[(i,j) for i in range(n) for j in range(i+1,n) if j-i not in (1,n-1)]
    def cross(e,f):
        a,b=e;c,d=f
        return len({a,b,c,d})==4 and ((a<c<b)!=(a<d<b))
    seen=set()
    for states in itertools.product(range(3),repeat=len(pairs)):
        chosen=[pairs[i] for i,s in enumerate(states) if s]
        if any(cross(e,f) for e,f in itertools.combinations(chosen,2)):continue
        new=set();ok=True
        for i,s in enumerate(states):
            if not s:continue
            u,v=poly[pairs[i][0]],poly[pairs[i][1]]
            e=(u,v) if s==1 else (v,u)
            if (e[1],e[0]) in A:ok=False;break
            if e not in A:new.add(e)
        if not ok:continue
        k=tuple(sorted(new))
        if k in seen:continue
        seen.add(k);yield k

def main():
    qk,rk,w=sys.argv[1],sys.argv[2],int(sys.argv[3])
    made=make_graph(qk,rk,w)
    if made is None:raise SystemExit('incompatible type')
    V,A,q,r=made;B=sorted(V-I);P=pprofiles(V,A,B);Bset=set(B)
    rows=[];solutions=[]
    for dv in sorted(I):
        base={e for e in A if dv not in e}
        for adds in candidates(hole(dv,q,r),base):
            st=test(V,A,B,P,dv,adds)
            guards=sorted((v,u) for u,v in adds if u in Bset and v in Bset)
            row=[dv,[list(e) for e in adds],[list(e) for e in guards],st]
            rows.append(row)
            if st[1]==0:solutions.append(row)
    solutions.sort(key=lambda x:(len(x[2]),len(x[1]),x[0],x[1]))
    print(json.dumps({'id':[qk,rk,w],'catalog':len(rows),'solution':solutions[0] if solutions else None,
      'no_solution_digest_input':rows if not solutions else None},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
