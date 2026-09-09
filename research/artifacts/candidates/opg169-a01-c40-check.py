#!/usr/bin/env python3
"""Exact consumer for the compact C40 rule manifest; candidate-only."""
from __future__ import annotations
import collections, json, sys

BASE_ARCS={(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),(4,5),(4,8),
(5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7),
(11,12),(13,12),(13,8),(12,7),(7,13)}
BASE_TRIS=[(0,2,3),(0,6,2),(0,5,6),(0,4,5),(0,3,4),
(2,7,3),(2,11,7),(2,6,11),(3,8,4),(3,7,8),
(8,7,13),(13,7,12),(12,7,11)]
I={0,2,3,4,7}

def need(x,msg):
    if not x: raise AssertionError(msg)

def make_graph(qk,rk,w):
    q=14 if qk=='new' else int(qk); r=15 if rk=='new' else int(rk)
    A=set(BASE_ARCS)
    es=[(5,q),(q,4),(q,r) if w&1 else (r,q),(r,8) if w&2 else (8,r),(r,4) if w&4 else (4,r)]
    for e in es:
        need(e[0]!=e[1] and (e[1],e[0]) not in A,'orientation conflict')
        A.add(e)
    V={0,2,3,4,5,6,7,8,11,12,13,q,r}
    return V,A,q,r,BASE_TRIS+[(5,4,q),(q,4,r),(r,4,8)]

def closed_links(tris):
    succ={}
    for a,b,c in tris:
        for v,x,y in ((b,a,c),(c,b,a),(a,c,b)):
            row=succ.setdefault(v,{})
            need(x not in row or row[x]==y,'face successor conflict')
            row[x]=y
    ans={}
    for v,row in succ.items():
        ns=set(row)|set(row.values()); indeg=collections.Counter(row.values())
        if set(row)==ns and all(indeg[x]==1 for x in ns): ans[v]=len(ns)
    return ans

def relation(arcs,vertices,boundary,colour):
    vertices=set(vertices); adj={v:[] for v in vertices}
    for u,v in arcs:
        if u in vertices and v in vertices and colour[u]==colour[v]: adj[u].append(v)
    mark={v:0 for v in vertices}
    def dfs(v):
        mark[v]=1
        for z in adj[v]:
            if mark[z]==1:return False
            if mark[z]==0 and not dfs(z):return False
        mark[v]=2;return True
    for v in vertices:
        if mark[v]==0 and not dfs(v):return None
    R=set()
    for s in boundary:
        todo=list(adj[s]);seen=set()
        while todo:
            z=todo.pop()
            if z in seen:continue
            seen.add(z);todo.extend(adj[z])
        R|={(s,t) for t in boundary if t in seen}
    return frozenset(R)

def verify_rule(V,A,Iset,rule):
    B=rule['boundary']; qvs=rule['q_vertices']; ivs=rule['i_vertices']
    need(B==sorted(set(V)-set(Iset)),'boundary mismatch')
    dv=rule['delete']; adds={tuple(x) for x in rule['adds']}
    QV=set(V)-{dv}; QA={e for e in A if dv not in e}|adds
    need(qvs==sorted(QV),'Q order')
    P=collections.defaultdict(list)
    for bits in range(1<<len(ivs)):
        cp={v:0 for v in V}
        for i,v in enumerate(ivs):cp[v]=(bits>>i)&1
        for bword in range(1<<len(B)):
            for i,v in enumerate(B):cp[v]=(bword>>i)&1
            rp=relation(A,V,B,cp)
            if rp is not None:P[bword].append(rp)
    valid=equal=strict=fail=0
    for qbits in range(1<<len(qvs)):
        cq={v:(qbits>>i)&1 for i,v in enumerate(qvs)}
        rq=relation(QA,QV,B,cq)
        if rq is None:continue
        valid+=1; bword=sum(cq[v]<<i for i,v in enumerate(B))
        opts=[rp for rp in P[bword] if rp<=rq]
        if not opts: fail+=1
        elif rq in opts: equal+=1
        else: strict+=1
    need(fail==0,'valid Q input without profile lift')
    need((valid,equal,strict)==(rule['valid'],rule['equal'],rule['strict']),'rule count mismatch')

def make_z_graph(zk,bits):
    V,A,q,r,T=make_graph('12','new',2)
    z=14 if zk=='new' else int(zk);V.add(z)
    for e in [(z,15),(z,12) if bits&1 else (12,z),(z,8) if bits&2 else (8,z)]:
        need((e[1],e[0]) not in A,'z conflict');A.add(e)
    return V,A,z,T+[(12,15,z),(z,15,8)]

def make_guard_residual(bits):
    V,A,z,T=make_z_graph('new',bits);A.add((8,12));return V,A,z,T

def make_fan13(bits,fw):
    V,A,z,T=make_guard_residual(bits);a=16;V.add(a)
    for e in [(a,13),(a,8) if fw&1 else (8,a),(a,12) if fw&2 else (12,a)]:
        need((e[1],e[0]) not in A,'fan13 conflict');A.add(e)
    return V,A,z,a,T+[(8,13,a),(a,13,12)]

def make_fan14(bits,fw):
    V,A,z,T=make_guard_residual(bits);b=16;V.add(b)
    forced=(14,b) if bits==0 else (b,14)
    for e in [forced,(b,8) if fw&1 else (8,b),(b,12) if fw&2 else (12,b)]:
        need((e[1],e[0]) not in A,'fan14 conflict');A.add(e)
    return V,A,z,b,T+[(8,14,b),(b,14,12)]

def main(path):
    d=json.load(open(path,encoding='utf-8'))
    need(d['format']=='opg169-c40-d19-profile-catalog-v1','format')
    counts=collections.Counter(r['class'] for r in d['rows'])
    need(dict(counts)==d['coverage_counts'],'coverage')
    need(len(d['rows'])==70,'rows')
    for row in d['rows']:
        V,A,q,r,T=make_graph(str(row['q']),str(row['r']),row['word'])
        if row['class']=='structural_semidegree':
            cl=closed_links(T); sd={v:[0,0] for v in V}
            for u,v in A:sd[u][1]+=1;sd[v][0]+=1
            need({str(v):sd[v] for v in cl if min(sd[v])<2}==row['closed_star_bad'],'closed star')
        elif row['class'] in ('unguarded_reduction','guarded_reduction'):
            verify_rule(V,A,I,row['rule'])
            B=set(row['rule']['boundary'])
            guards=sorted([[v,u] for u,v in map(tuple,row['rule']['adds']) if u in B and v in B])
            need(guards==sorted(row['rule']['guards']),'guards')
            if row['class']=='unguarded_reduction':need(not guards,'unguarded')
        else:
            need(row['catalog_candidates_including_bare']>=421,'residual count')
    for row in d['degree4_outport_layer']['rows']:
        V,A,z,T=make_z_graph(row['z_identity'],row['direction_bits'])
        verify_rule(V,A,{0,2,3,4,7,15},row['rule'])
    for row in d['fan_end_layer']['endpoint_13_degree4']['rows']:
        if row.get('rule'):
            V,A,z,a,T=make_fan13(row['z_bits'],row['fan_word'])
            verify_rule(V,A,{0,2,3,4,7,13,15},row['rule'])
    for row in d['fan_end_layer']['endpoint_z14_degree4']['rows']:
        if row.get('rule'):
            V,A,z,b,T=make_fan14(row['z_bits'],row['fan_word'])
            verify_rule(V,A,{0,2,3,4,7,14,15},row['rule'])
    mult=collections.Counter(v for tri in make_z_graph('new',0)[3] for v in tri)
    need(mult==collections.Counter({4:6,7:6,0:5,2:5,3:5,8:5,12:5,15:4,5:3,6:3,11:3,13:2,14:2}),'ledger')
    print(json.dumps({'status':'ok','rows':70,'coverage':d['coverage_counts'],
      'selected_rules':sum(r['class'] in ('unguarded_reduction','guarded_reduction') for r in d['rows']),
      'outport_rows':len(d['degree4_outport_layer']['rows']),
      'fan13_rows':len(d['fan_end_layer']['endpoint_13_degree4']['rows']),
      'fan14_rows':len(d['fan_end_layer']['endpoint_z14_degree4']['rows'])},sort_keys=True,separators=(',',':')))

if __name__=='__main__':main(sys.argv[1])
