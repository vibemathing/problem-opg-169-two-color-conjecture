"""C35 bounded generator controls. Run with the archived resource wrapper.
Finite arithmetic controls and one frozen graph; no trusted admission.
"""
import hashlib
import itertools as it
import json
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def need(ok, text):
    if not ok:
        raise ValueError(text)


def lower(t):
    return max(3*t, 2*t+4)


def parameters(cap):
    pairs = [(d,t) for d in range(4,cap+1) for t in range(d//3+1)
             if d >= lower(t)]
    need(all((d>=4 and (t==0 or d>=6) and 3*t<=d and
              (d not in (6,7) or t<=1) and (d!=9 or t<=2))
             == (d>=lower(t)) for d in range(4,cap+1)
             for t in range(d+1)), 'exact domain equivalence')
    pairs.sort(key=lambda x:(F(x[0]-4-2*x[1],x[0]),x))
    families=Counter(); signs=Counter(); boundary_checks=0
    for x,y,z in it.combinations_with_replacement(pairs,3):
        ds=[x[0],y[0],z[0]]; ts=[x[1],y[1],z[1]]
        rem=[d-4-2*t for d,t in zip(ds,ts)]
        n=sum(rem[i]*ds[(i+1)%3]*ds[(i+2)%3] for i in range(3))
        n-=ds[0]*ds[1]*ds[2]
        s=[d-3*t for d,t in zip(ds,ts)]
        weight=sum((s[i]-6)*ds[(i+1)%3]*ds[(i+2)%3] for i in range(3))
        need(3*n==2*weight,'slack identity')
        a,b=x[0],y[0]
        num=rem[0]*b+rem[1]*a; den=a*b
        interval=(num==0 or (num<den and
                  z[0]<=((4+2*z[1])*den-1)//num))
        need((n<0)==interval,'strict integer endpoint test')
        sign='negative' if n<0 else 'zero' if n==0 else 'positive'
        signs[sign]+=1
        if n<0:
            key=''.join(sorted('L' if q<6 else 'N' if q==6 else 'P' for q in s))
            need(key in ('LLL','LLN','LNN','LLP','LNP','LPP'),'exhaustive sign family')
            families[key]+=1
            boundary_checks+=1
    zeros=[p for p in pairs if p[0]-4-2*p[1]==0]
    need(zeros==[(4,0),(6,1),(8,2),(10,3),(12,4)],'five zero corners')
    # Selected controls distinguish strict inequality, banned old donors, and unbounded t.
    need(lower(3)==10 and lower(2)==8,'excluded nine/six donors')
    for m in range(4,100):
        need(3*F(3*m-4-2*m,3*m)-1==-F(4,m),'unbounded diagonal family')
    return {'degree_cap':cap,'admissible_pairs':len(pairs),'triple_sign_counts':dict(signs),
            'negative_family_counts':dict(families),'strict_endpoint_checks':boundary_checks,
            'zero_corners':zeros,'scope':'finite control; proof gives unbounded classification'}


def reach(A,V,c):
    R={x:0 for x in V}
    for x,y in A:
        if x in R and y in R and ((c>>x)^(c>>y))&1==0:
            R[x]|=1<<y
    for z in V:
        for x in V:
            if R[x]>>z&1: R[x]|=R[z]
    return R


def state(A,V,B,c):
    R=reach(A,V,c)
    if any(R[x]>>x&1 for x in V): return None
    return frozenset((x,y) for x in B for y in B if R[x]>>y&1)


def assignments(V):
    return (sum(((k>>i)&1)<<v for i,v in enumerate(V)) for k in range(1<<len(V)))


def faces(rotation):
    R={int(k):v for k,v in rotation.items()}; seen=set();fs=[]
    for a in sorted(R):
        for b in R[a]:
            if (a,b) in seen: continue
            cur=(a,b);f=[]
            while cur not in seen:
                seen.add(cur);x,y=cur;f.append(x)
                cur=(y,R[y][(R[y].index(x)+1)%len(R[y])])
            need(cur==(a,b),'face permutation')
            fs.append(f)
    need(len(R)-len(seen)//2+len(fs)==2,'sphere Euler')
    return fs


def topo(A,V,c,k):
    left={x for x in V if (c>>x)&1==k}; result=[]
    while left:
        zero=sorted(x for x in left if not any((y,x) in A for y in left))
        need(bool(zero),'topological certificate');result+=zero;left-=set(zero)
    return result


def cycle(A,V,c):
    for k in (0,1):
        vs=[x for x in V if (c>>x)&1==k]
        for n in range(3,len(vs)+1):
            for seq in it.permutations(vs,n):
                if seq[0]==min(seq) and all((seq[i],seq[(i+1)%n]) in A for i in range(n)):
                    return {'colour':k,'cycle':list(seq)+[seq[0]]}
    raise ValueError('no claimed failure cycle')


def patch(A,R,S, boundary=None):
    S=set(S);B=sorted({y for x,y in A if x in S and y not in S}|
                    {x for x,y in A if y in S and x not in S})
    if boundary is not None:
        need(set(boundary)==set(B),'complete separator');B=boundary
    V=B+sorted(S);P={e for e in A if set(e)<=set(V)};Q={e for e in P if not set(e)&S}
    maps=[];bad=[]
    for c in assignments(B):
        qr=state(Q,B,B,c)
        if qr is None:maps.append(None);continue
        good=next((c|s for s in assignments(sorted(S))
                   if (pr:=state(P,V,B,c|s)) is not None and pr<=qr),None)
        maps.append(good)
        if good is None:bad.append(c)
    rot={x:[y for y in R[x] if y in V] for x in V};fs=faces(rot)
    return {'deleted':sorted(S),'boundary':B,'order':V,'arcs':sorted(P),'retained_arcs':sorted(Q),
            'rotation':rot,'faces':fs,'lift_by_boundary_bits':maps,'bad_boundary_masks':bad}


def chord_sets(B):
    n=len(B);pairs=[(i,j) for i in range(n) for j in range(i+1,n) if j-i not in (1,n-1)]
    def cross(e,f):
        a,b=e;c,d=f
        return len({a,b,c,d})==4 and (a<c<b)!=(a<d<b)
    for k in range(n-2):
        for es in it.combinations(pairs,k):
            if any(cross(e,f) for e,f in it.combinations(es,2)):continue
            for word in range(1<<k):
                yield {(B[b],B[a]) if word>>i&1 else (B[a],B[b]) for i,(a,b) in enumerate(es)}


def graph_controls(data):
    g=data['graph'];V=g['vertices'];A={tuple(e) for e in g['arcs']};R={int(x):ns for x,ns in g['rotation'].items()}
    need(all(x!=y and (y,x) not in A for x,y in A),'simple orientation')
    for x in V:
        need(set(R[x])=={y for a,y in A if a==x}|{a for a,y in A if y==x},'rotation full neighbours')
        need(len(R[x])==5,'full degree five')
        need(min(sum(y==x for a,y in A),sum(a==x for a,y in A))>=2,'full semidegree')
    fs=faces(R);need(len(fs)==20 and all(len(f)==3 for f in fs),'all twenty triangles')
    need(state(A,V,[],g['full_valid_ones']) is not None,'full root is colourable')
    scan=[]
    for f in fs:
        p=patch(A,R,f)
        scan.append({'deleted':f,'boundary':p['boundary'],'bad_boundary_masks':p['bad_boundary_masks']})
    pos=patch(A,R,data['positive_delete'],data['positive_boundary_cycle']);B=pos['boundary'];P=set(map(tuple,pos['arcs']));Q=set(map(tuple,pos['retained_arcs']))
    need(not pos['bad_boundary_masks'] and all(c is not None for c in pos['lift_by_boundary_bits']),'64 complete lifts')
    need(sum(len(f)>3 for f in pos['faces'])==1 and any(f==B for f in pos['faces']),'hexagonal patch disk')
    options=cases=valid_cases=0
    for E in chord_sets(B):
        options+=1
        for bits,c in enumerate(assignments(B)):
            cases+=1;qr=state(Q|E,B,B,c)
            if qr is None:continue
            lift=pos['lift_by_boundary_bits'][bits]
            need(state(P|E,pos['order'],B,lift)==qr,'all direct exterior chord data')
            valid_cases+=1
    H=[v for v in V if v not in data['positive_delete']];ha={e for e in A if set(e)<=set(H)};full_lifts=[]
    for c in assignments(H):
        if state(ha,H,[],c) is None:continue
        bits=sum(((c>>v)&1)<<i for i,v in enumerate(B))
        lift=c|pos['lift_by_boundary_bits'][bits]
        need(state(A,V,[],lift) is not None,'entire exterior colouring fixed')
        full_lifts.append([c,lift])
    negS=data['negative_delete'];negH=[v for v in V if v not in negS];nh={e for e in A if set(e)<=set(negH)};c=data['negative_retained_ones']
    need(state(nh,negH,[],c) is not None,'actual negative full deletion colouring valid')
    failures=[]
    for ib in range(8):
        cc=c|sum(((ib>>i)&1)<<v for i,v in enumerate(negS))
        need(state(A,V,[],cc) is None,'all negative full extensions fail')
        failures.append({'internal_bits':ib,**cycle(A,V,cc)})
    vertex_ledger=[{'vertex':v,'d':5,'t':0,'initial':1,'unit_paid':0,'gamma':'1/5','corner_count':5,'final':0} for v in V]
    face_ledger=[{'walk':f,'h':0,'initial':-1,'received':'3/5','final':'-2/5'} for f in fs]
    need(sum(F(f['final']) for f in face_ledger)==-8,'complete global double-payment ledger')
    return {'positive':pos,'positive_full_retained_lifts':full_lifts,'exterior_chords':{'options':options,'assignments':cases,'valid':valid_cases},
            'face_scan':scan,'negative':{'deleted':negS,'retained_ones':c,'retained_orders':[topo(nh,negH,c,k) for k in (0,1)],'all_extensions':failures},
            'full_colouring_orders':[topo(A,V,g['full_valid_ones'],k) for k in (0,1)],'vertex_ledger':vertex_ledger,'face_ledger':face_ledger}


def main():
    raw=Path(sys.argv[1]).read_bytes();need(len(raw)<65536,'input cap');data=json.loads(raw)
    need(data['degree_cap']==32,'fixed finite arithmetic bound')
    out={'format':'c35-complete-candidate-certificate-v1','verdict':'candidate_only','trusted_verifier_receipt':False,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
         'parameters':parameters(32),'graph':graph_controls(data)}
    text=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';need(len(text.encode())<65536,'output cap')
    print(text,end='')


if __name__=='__main__':main()
