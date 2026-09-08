"""Separate C35 certificate consumer: imports no generator predicates.
DFS tests full colour classes; BFS computes every positive boundary return.
"""
import hashlib
import itertools as it
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def need(ok,msg):
    if not ok:raise ValueError(msg)


def inspect(A,V,B,c):
    V=set(V);adj={x:[] for x in V}
    for x,y in A:
        if x in V and y in V and (c>>x)&1==(c>>y)&1:adj[x].append(y)
    marks={}
    def visit(x):
        if marks.get(x)==1:return False
        if marks.get(x)==2:return True
        marks[x]=1
        for y in adj[x]:
            if not visit(y):return False
        marks[x]=2;return True
    if not all(visit(x) for x in sorted(V)):return None
    rel=set()
    for x in B:
        todo=list(adj[x]);seen=set()
        while todo:
            y=todo.pop()
            if y not in seen:seen.add(y);todo+=adj[y]
        rel|={(x,y) for y in seen if y in B}
    return rel


def masks(V):
    for bits in it.product((0,1),repeat=len(V)):
        yield sum(c<<v for v,c in zip(V,bits))


def run(data,cert):
    pairs=[(d,t) for d in range(4,33) for t in range(d//3+1)
           if (t==0 or d>=6) and (d not in (6,7) or t<=1) and (d!=9 or t<=2)]
    gs=[F(d-4-2*t,d) for d,t in pairs];counts=Counter()
    for i,j,k in it.combinations_with_replacement(range(len(pairs)),3):
        val=gs[i]+gs[j]+gs[k]-1
        counts['negative' if val<0 else 'positive' if val>0 else 'zero']+=1
    need(dict(counts)==cert['parameters']['triple_sign_counts'],'separate rational classification')
    g=data['graph'];A=set(map(tuple,g['arcs']));V=g['vertices'];rot={int(x):y for x,y in g['rotation'].items()}
    need(len(A)==30 and len(V)==12,'complete graph identity')
    for x,ns in rot.items():
        need(len(ns)==5 and len(set(ns))==5 and set(ns)=={y for a,y in A if a==x}|{a for a,y in A if y==x},'full rotations')
    face_sets=[];seen=set()
    for x in V:
        for y in rot[x]:
            if (x,y) in seen:continue
            start=(x,y);dart=start;face=[]
            while dart not in seen:
                seen.add(dart);a,b=dart;face.append(a);dart=b,rot[b][rot[b].index(a)-1]
            need(dart==start and len(face)==3,'reverse face permutation');face_sets.append(frozenset(face))
    need(len(face_sets)==20,'twenty face incidence sets')
    pos=cert['graph']['positive'];B=pos['boundary'];S=pos['deleted'];PV=B+S
    P={e for e in A if set(e)<=set(PV)};Q={e for e in A if set(e)<=set(B)}
    need(P==set(map(tuple,pos['arcs'])) and Q==set(map(tuple,pos['retained_arcs'])),'full induced patch arcs')
    for v in S:need(all(w in PV for w in rot[v]),'no hidden exterior neighbour')
    lifts=pos['lift_by_boundary_bits'];need(len(lifts)==64,'complete vector')
    for c in masks(B):
        i=sum(((c>>v)&1)<<j for j,v in enumerate(B));d=lifts[i]
        need(d is not None and all(((d>>v)&1)==((c>>v)&1) for v in B),'sigma equality')
        need(inspect(P,PV,B,d)==inspect(Q,B,B,c),'full relation equality')
    options=[];diags=[(i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5)]
    # Alternative ternary generator includes absent and both directions on every diagonal.
    for choice in it.product((0,1,2),repeat=len(diags)):
        chosen=[e for e,v in zip(diags,choice) if v]
        if any(a<c<b<d or c<a<d<b for (a,b),(c,d) in it.combinations(chosen,2)):continue
        E={(B[a],B[b]) if v==1 else (B[b],B[a]) for (a,b),v in zip(diags,choice) if v}
        options.append(E)
    need(len(options)==cert['graph']['exterior_chords']['options'],'all exterior chords')
    external_ok=0
    for E in options:
        for c in masks(B):
            qr=inspect(Q|E,B,B,c)
            if qr is None:continue
            i=sum(((c>>v)&1)<<j for j,v in enumerate(B))
            need(inspect(P|E,PV,B,lifts[i])==qr,'exterior actual arcs retained');external_ok+=1
    need(external_ok==cert['graph']['exterior_chords']['valid'],'exterior count')
    H=[x for x in V if x not in S];table={a:b for a,b in cert['graph']['positive_full_retained_lifts']}
    for c in masks(H):
        if inspect(A,H,[],c) is None:need(c not in table,'invalid H is not a lift index');continue
        d=table[c];need(all((c>>x)&1==(d>>x)&1 for x in H),'ALL retained colours')
        need(inspect(A,V,[],d) is not None,'global lift, not boundary projection')
    neg=cert['graph']['negative'];S=neg['deleted'];H=[x for x in V if x not in S];c=neg['retained_ones']
    need(inspect(A,H,[],c) is not None,'full bad-interface start is valid')
    for rec in neg['all_extensions']:
        d=c|sum(((rec['internal_bits']>>i)&1)<<x for i,x in enumerate(S));seq=rec['cycle'];k=rec['colour']
        need(seq[0]==seq[-1] and len(set(seq[:-1]))==len(seq)-1,'simple cycle')
        need(all((a,b) in A for a,b in zip(seq,seq[1:])) and all((d>>x)&1==k for x in seq),'full obstruction')
        need(inspect(A,V,[],d) is None,'second engine obstruction')
    need(inspect(A,V,[],g['full_valid_ones']) is not None,'NOT a root counterexample')
    for row in cert['graph']['vertex_ledger']:
        need(row['d']==5 and row['t']==0 and F(row['gamma'])*5==row['initial']==1 and row['final']==0,'every vertex debit')
    for row in cert['graph']['face_ledger']:
        need(frozenset(row['walk']) in face_sets and row['h']==0 and F(row['final'])==-F(2,5),'every face receipt')
    need(sum(F(r['final']) for r in cert['graph']['face_ledger'])==-8,'no missing face deficit')
    # Every old-to-new debit uses all corners; this is an identity control, not graph realization.
    budgets=0
    for d in range(4,201):
        for t in range(d//3+1):
            if t and d<6 or d in (6,7) and t>1 or d==9 and t>2:continue
            old=F(d-4-t,d);new=F(d-4-2*t,d)
            need(new>=0 and old-new==F(t,d) and 2*t+d*new==d-4,'full donor accounting');budgets+=1
    return {'status':'all_declared_checks_passed','parameter_triples':sum(counts.values()),'positive_local_lifts':64,
            'direct_exterior_options':len(options),'direct_exterior_valid_assignments':external_ok,
            'actual_full_exterior_lifts':len(table),'bad_full_extensions':8,'vertex_debits':12,'face_receipts':20,
            'finite_budget_controls':budgets,'scope':'same generator trust domain, separate implementation; no trusted receipt'}


def main():
    a=Path(sys.argv[1]).read_bytes();b=Path(sys.argv[2]).read_bytes();need(len(a)<65536 and len(b)<65536,'bounded inputs')
    out={'verdict':'candidate_only','trusted_verifier_receipt':False,'input_sha256':hashlib.sha256(a).hexdigest(),
         'certificate_sha256':hashlib.sha256(b).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         **run(json.loads(a),json.loads(b))}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
