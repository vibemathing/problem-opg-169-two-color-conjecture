#!/usr/bin/env python3
import json, sys
from collections import Counter, defaultdict

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
    T=BASE_TRIS+[(5,4,q),(q,4,r),(r,4,8)]
    return V,A,q,r,T

def closed_links(tris):
    succ={}
    for a,b,c in tris:
        for v,x,y in ((b,a,c),(c,b,a),(a,c,b)):
            row=succ.setdefault(v,{})
            need(x not in row or row[x]==y,'face successor conflict')
            row[x]=y
    ans={}
    for v,row in succ.items():
        ns=set(row)|set(row.values())
        indeg=Counter(row.values())
        if set(row)==ns and all(indeg[x]==1 for x in ns): ans[v]=len(ns)
    return ans

def colour_graph(arcs,vertices,colour):
    vertices=set(vertices)
    adj={v:[] for v in vertices}
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
    return adj

def relation(arcs,vertices,boundary,colour):
    adj=colour_graph(arcs,vertices,colour)
    if adj is None:return None
    R=set()
    for s in boundary:
        todo=list(adj[s]);seen=set()
        while todo:
            v=todo.pop()
            if v in seen:continue
            seen.add(v);todo.extend(adj[v])
        for t in boundary:
            if t in seen:R.add((s,t))
    return R

def verify_rule(V,A,Iset,rule):
    B=rule['boundary']; qvs=rule['q_vertices']; ivs=rule['i_vertices']
    need(B==sorted(set(V)-set(Iset)),'boundary mismatch')
    dv=rule['delete'];adds={tuple(x) for x in rule['adds']}
    QA={e for e in A if dv not in e}|adds; QV=set(V)-{dv}
    need(qvs==sorted(QV),'Q vertex order')
    vec=rule['lift_selection']; need(len(vec)==1<<len(qvs),'vector length')
    valid=equal=strict=0
    for bits,sel in enumerate(vec):
        cq={v:(bits>>i)&1 for i,v in enumerate(qvs)}
        rq=relation(QA,QV,B,cq)
        if rq is None:
            need(sel==-2,'invalid Q marker');continue
        valid+=1;need(sel>=0,'valid Q has lift')
        cp={v:0 for v in V}
        for v in B:cp[v]=cq[v]
        for i,v in enumerate(ivs):cp[v]=(sel>>i)&1
        rp=relation(A,V,B,cp)
        need(rp is not None,'P lift acyclic')
        need(rp<=rq,'positive relation containment')
        if rp==rq:equal+=1
        else:strict+=1
    need((valid,equal,strict)==(rule['valid'],rule['equal'],rule['strict']),'rule counts')

def make_z_graph(zk,bits):
    V,A,q,r,T=make_graph('12','new',2)
    z=14 if zk=='new' else int(zk)
    V.add(z)
    for e in [(z,15),(z,12) if bits&1 else (12,z),(z,8) if bits&2 else (8,z)]:
        need((e[1],e[0]) not in A,'z orientation conflict');A.add(e)
    T=T+[(12,15,z),(z,15,8)]
    return V,A,z,T

def make_guard_residual(bits):
    V,A,z,T=make_z_graph('new',bits)
    A.add((8,12))
    return V,A,z,T

def make_fan13(bits,fw):
    V,A,z,T=make_guard_residual(bits); a=16;V.add(a)
    for e in [(a,13),(a,8) if fw&1 else (8,a),(a,12) if fw&2 else (12,a)]:
        need((e[1],e[0]) not in A,'fan13 conflict');A.add(e)
    return V,A,z,a,T+[(8,13,a),(a,13,12)]

def make_fan14(bits,fw):
    V,A,z,T=make_guard_residual(bits); b=16;V.add(b)
    forced=(14,b) if bits==0 else (b,14)
    for e in [forced,(b,8) if fw&1 else (8,b),(b,12) if fw&2 else (12,b)]:
        need((e[1],e[0]) not in A,'fan14 conflict');A.add(e)
    return V,A,z,b,T+[(8,14,b),(b,14,12)]

def main(path):
    d=json.load(open(path))
    need(d['format']=='opg169-c40-d19-profile-catalog-v1','format')
    need(d['verdict']=='candidate_only','verdict')
    counts=Counter(row['class'] for row in d['rows'])
    need(dict(counts)==d['coverage_counts'],'coverage partition')
    need(len(d['rows'])==70,'70 rows')
    seen=set()
    for row in d['rows']:
        qk,rk,w=row['q'],row['r'],row['word']; key=(str(qk),str(rk),w)
        need(key not in seen,'duplicate type');seen.add(key)
        V,A,q,r,T=make_graph(str(qk),str(rk),w)
        if row['class']=='structural_semidegree':
            cl=closed_links(T);sd={v:[0,0] for v in V}
            for u,v in A:sd[u][1]+=1;sd[v][0]+=1
            bad={str(v):sd[v] for v in cl if min(sd[v])<2}
            need(bad==row['closed_star_bad'],'closed semidegree')
        elif row['class'] in ('unguarded_reduction','guarded_reduction'):
            verify_rule(V,A,I,row['rule'])
            B=set(row['rule']['boundary'])
            expected=sorted([[v,u] for u,v in map(tuple,row['rule']['adds']) if u in B and v in B])
            need(expected==sorted(row['rule']['guards']),'guard list')
            if row['class']=='unguarded_reduction':need(not expected,'unguarded has no unresolved boundary arc')
        else:
            need(row['catalog_candidates_including_bare']>=421,'residual catalog count')
    need(d['first_relation_only_closed']['id']=='11/12/3','first row')
    need(d['first_relation_only_closed']['rule']['delete']==0,'first deletion')
    need(d['first_relation_only_closed']['rule']['adds']==[[6,4]],'first shortcut')
    for row in d['degree4_outport_layer']['rows']:
        V,A,z,T=make_z_graph(row['z_identity'],row['direction_bits'])
        verify_rule(V,A,{0,2,3,4,7,15},row['rule'])
    for row in d['fan_end_layer']['endpoint_13_degree4']['rows']:
        if row['rule'] is not None:
            V,A,z,a,T=make_fan13(row['z_bits'],row['fan_word'])
            verify_rule(V,A,{0,2,3,4,7,13,15},row['rule'])
    for row in d['fan_end_layer']['endpoint_z14_degree4']['rows']:
        if row['rule'] is not None:
            V,A,z,b,T=make_fan14(row['z_bits'],row['fan_word'])
            verify_rule(V,A,{0,2,3,4,7,14,15},row['rule'])
    V,A,z,T=make_z_graph('new',0)
    mult=Counter(v for tri in T for v in tri)
    need(mult==Counter({4:6,7:6,0:5,2:5,3:5,8:5,12:5,15:4,5:3,6:3,11:3,13:2,14:2}),
         '18-face ledger multiplicity')
    print(json.dumps({'status':'ok','rows':70,'coverage':d['coverage_counts'],
      'selected_rules':sum(r['class'] in ('unguarded_reduction','guarded_reduction') for r in d['rows']),
      'degree4_outport_rows':len(d['degree4_outport_layer']['rows']),
      'fan13_rows':len(d['fan_end_layer']['endpoint_13_degree4']['rows']),
      'fan14_rows':len(d['fan_end_layer']['endpoint_z14_degree4']['rows'])},
      sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main(sys.argv[1])
