"""C34 exact finite controls for exterior-chord-conditioned facial expansions.
Candidate generator only. No trusted receipt or universal-root conclusion.
"""
from __future__ import annotations
import hashlib, itertools as it, json, platform, sys, time
from functools import lru_cache
from pathlib import Path

RESIDUES=((1,78),(1,100),(3,43),(5,77))
PE=((0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5))
BASE_ROT={0:[1,4,5,3],1:[0,2,4],2:[3,5,4,1],3:[0,5,2],4:[0,1,2,5],5:[0,4,2,3]}

def need(ok,label):
    if not ok: raise ValueError(label)

def pair(r,b):
    return {(i,(i+1)%4) if not (r>>i)&1 else ((i+1)%4,i) for i in range(4)} | {(y,x) if (b>>i)&1 else (x,y) for i,(x,y) in enumerate(PE)}

def faces(A,rot):
    darts=set(A)|{(y,x) for x,y in A}
    need(all(x!=y and (y,x) not in A for x,y in A),'orientation')
    need(set(rot)=={x for x,y in darts},'rotation vertices')
    for x,ns in rot.items():
        need(len(set(ns))==len(ns) and set(ns)=={y for a,y in darts if a==x},'rotation neighbours')
    seen=set(); out=[]
    for first in sorted(darts):
        if first in seen: continue
        d=first; f=[]
        while d not in seen:
            seen.add(d);x,y=d;f.append(x)
            d=(y,rot[y][(rot[y].index(x)+1)%len(rot[y])])
        need(d==first,'face permutation')
        out.append(f)
    todo=[min(rot)]; visited=set()
    while todo:
        x=todo.pop()
        if x not in visited: visited.add(x);todo.extend(rot[x])
    need(len(visited)==len(rot) and len(rot)-len(A)+len(out)==2,'sphere')
    return out

def ear(r,b,side,direction):
    A=pair(r,b);R={x:list(ns) for x,ns in BASE_ROT.items()}
    a,z=side,(side+1)%4;t=6
    for j,x in enumerate((a,z)): A.add((t,x) if (direction>>j)&1 else (x,t))
    R[a].insert(R[a].index(z),t);R[z].insert(R[z].index(a)+1,t);R[t]=[a,z]
    B=list(range(4));B.insert(side+1,t)
    return A,R,B

def cap(r,b,corner,direction):
    A=pair(r,b);R={x:list(ns) for x,ns in BASE_ROT.items()}
    a,z=(corner-1)%4,(corner+1)%4
    A.add((z,a) if direction else (a,z))
    R[a].insert(R[a].index(corner),z);R[z].insert(R[z].index(corner)+1,a)
    return A,R,[x for x in range(4) if x!=corner]

def fan(r,b,corner,direction):
    # Absorb both external triangles at a boundary corner with exactly one new neighbour.
    A,R,B=ear(r,b,(corner-1)%4,direction&3)
    # Ear's two bits correspond to (corner-1)->6 and corner->6.
    z=(corner+1)%4;t=6
    A.add((t,z) if (direction>>2)&1 else (z,t))
    # Attach across the consecutive exterior sides t,corner,z.
    R[t].insert(R[t].index(corner),z)
    R[z].insert(R[z].index(corner)+1,t)
    B=[t if x==corner else x for x in range(4)]
    return A,R,B

def rows(A,n):
    out=[0]*n
    for x,y in A: out[x]|=1<<y
    return tuple(out)

def close(R,n):
    R=list(R)
    for k in range(n):
        for x in range(n):
            if (R[x]>>k)&1: R[x]|=R[k]
    return R

def kahn(incoming,mask):
    while mask:
        removable=0
        for x in range(len(incoming)):
            if (mask>>x)&1 and not (incoming[x]&mask): removable|=1<<x
        if not removable: return False
        mask^=removable
    return True

def profile(A,n,b):
    R=rows(A,n); incoming=tuple(sum(1<<x for x in range(n) if (R[x]>>y)&1) for y in range(n)); full=(1<<n)-1; closure={}; good={}
    for S in range(1<<n):
        C=close([R[x]&S if (S>>x)&1 else 0 for x in range(n)],n)
        ok=not any((C[x]>>x)&1 for x in range(n))
        need(ok==kahn(incoming,S),'two cycle engines')
        closure[S]=C;good[S]=ok
    out=[]
    for c in range(1<<n):
        if not(good[c] and good[full^c]): out.append(None);continue
        rr=0
        for x in range(b): rr|=((closure[c][x]|closure[full^c][x])&((1<<b)-1))<<(b*x)
        out.append(rr)
    return tuple(out)

def norm(A,rot,B):
    labels=B+sorted(set(rot)-set(B)); pos={x:i for i,x in enumerate(labels)}
    return {(pos[x],pos[y]) for x,y in A},labels

def edges_of(tris):
    return frozenset(tuple(sorted(e)) for t in tris for e in it.combinations(t,2))

@lru_cache(None)
def triangulations(poly):
    if len(poly)<3: return ((),)
    result=[]
    for k in range(1,len(poly)-1):
        for L in triangulations(poly[:k+1]):
            for R in triangulations(poly[k:]): result.append(((poly[0],poly[k],poly[-1]),)+L+R)
    return tuple(result)

@lru_cache(None)
def models(b,max_inner):
    """Complete maximal disk models at b=3,4 with <=2 interiors; b=5 <=1."""
    ans={}
    def add(n,tris):
        key=(n,tuple(sorted(edges_of(tris))))
        ans.setdefault(key,tuple(tris))
    for tris in triangulations(tuple(range(b))): add(b,tris)
    if max_inner:
        w=b
        for k in range(3,b+1):
            for ns in it.combinations(range(b),k):
                fan=[];gaps=[]
                for j,a in enumerate(ns):
                    z=ns[(j+1)%k];fan.append((w,a,z))
                    gap=[a];x=a
                    while x!=z: x=(x+1)%b;gap.append(x)
                    gaps.append(triangulations(tuple(gap)))
                for chosen in it.product(*gaps): add(b+1,tuple(fan)+sum(chosen,()))
    if max_inner==2:
        # Contracting the two interior vertices recovers a one-interior model.
        # Two facial third vertices are the only common boundary neighbours.
        for k in range(3,b+1):
            for ns in it.combinations(range(b),k):
                gaps=[]
                for j,x in enumerate(ns):
                    y=ns[(j+1)%k];gap=[x]
                    while x!=y: x=(x+1)%b;gap.append(x)
                    gaps.append(triangulations(tuple(gap)))
                for picked in it.product(*gaps):
                    outside=sum(picked,())
                    for i,j in it.combinations(range(k),2):
                        for u,w in ((b,b+1),(b+1,b)):
                            N=ns[i:j+1];M=ns[j:]+ns[:i+1]
                            ts=tuple((u,x,y) for x,y in zip(N,N[1:]))+tuple((w,x,y) for x,y in zip(M,M[1:]))
                            add(b+2,outside+ts+((u,w,ns[i]),(w,u,ns[j])))
        # Nonadjacent interiors: each in a different triangle of a boundary triangulation.
        for ts in triangulations(tuple(range(b))):
            for i,j in it.combinations(range(len(ts)),2):
                for u,w in ((b,b+1),(b+1,b)):
                    fs=tuple(t for h,t in enumerate(ts) if h not in (i,j))
                    for t,v in ((ts[i],u),(ts[j],w)):
                        x,y,z=t;fs+=((x,y,v),(y,z,v),(z,x,v))
                    add(b+2,fs)
    rim={tuple(sorted((i,(i+1)%b))) for i in range(b)}
    return tuple((n,tuple(e for e in es if e not in rim),ans[(n,es)]) for n,es in sorted(ans))

def rotation_from_faces(b,n,tris):
    links={v:{} for v in range(n)}
    for f in tuple(tris)+(tuple(reversed(range(b))),):
        for j,v in enumerate(f):
            prev=f[j-1];nxt=f[(j+1)%len(f)]
            need(prev not in links[v],'duplicate corner')
            links[v][prev]=nxt
    rot={}
    for v,L in links.items():
        start=min(L);x=start;ns=[]
        while x not in ns: ns.append(x);x=L[x]
        need(x==start and len(ns)==len(L),'one vertex rotation')
        rot[v]=ns
    return rot

def chord_options(b,forbidden=frozenset()):
    edges=[(x,y) for x,y in it.combinations(range(b),2) if y-x not in (1,b-1) and (x,y) not in forbidden]
    out=[]
    for word in it.product((0,1,2),repeat=len(edges)):
        active=[e for e,v in zip(edges,word) if v]
        if any(len(set(e+f))==4 and ((e[0]<f[0]<e[1])!=(e[0]<f[1]<e[1])) for e,f in it.combinations(active,2)): continue
        out.append(tuple((x,y) if v==1 else (y,x) for (x,y),v in zip(edges,word) if v))
    return tuple(sorted(out,key=lambda E:(len(E),E)))

@lru_cache(None)
def union_relation(rr,b,extra):
    R=[(rr>>(x*b))&((1<<b)-1) for x in range(b)]
    for x,y in extra: R[x]|=1<<y
    R=close(R,b)
    return None if any((R[x]>>x)&1 for x in range(b)) else sum(R[x]<<(b*x) for x in range(b))

def with_exterior(rr,c,b,E):
    if rr is None: return None
    return union_relation(rr,b,tuple((x,y) for x,y in E if ((c>>x)&1)==((c>>y)&1)))

def conditioned(P,n,b,qs,ps,baseline_rules):
    rim_pairs={tuple(sorted((i,(i+1)%b))) for i in range(b)}
    forbidden=frozenset(tuple(sorted(e)) for e in P if e[0]<b and e[1]<b and tuple(sorted(e)) not in rim_pairs)
    result=[]
    for E in chord_options(b,forbidden):
        ep=[[] for _ in range(1<<b)]
        for c in range(1<<b):
            for cc,rr in ps[c]:
                re=with_exterior(rr,c,b,E)
                if re is not None: ep[c].append((cc,re))
        selected=None;bad_vector=[];visited=0
        for qi,(nn,aa,pp,tris) in enumerate(qs):
            if any((y,x) in aa for x,y in E): bad_vector.append(255);continue
            visited+=1;lift=[];fail=None
            for c,rr in enumerate(pp):
                re=with_exterior(rr,c,b,E)
                if re is None: lift.append(None);continue
                choices=ep[c&((1<<b)-1)]
                match=next((cc for cc,rp in choices if not rp&~re),None)
                lift.append(match)
                if match is None: fail=c;break
            if fail is None:
                selected={'q_index':qi,'vertices':nn,'arcs':aa,'triangles':tris,'lift':lift};break
            bad_vector.append(fail)
        result.append({'exterior_arcs':E,'selected':selected,'tested_before_success_or_exhaustion':visited,
                       'failure_masks_hex':bytes(bad_vector).hex() if selected is None else None})
    return result

@lru_cache(None)
def candidates(b,rim_code,max_inner):
    rim={(i,(i+1)%b) if not(rim_code>>i)&1 else ((i+1)%b,i) for i in range(b)}
    result=[];seen=set()
    for opt in chord_options(b):
        A=rim|set(opt);key=(b,tuple(sorted(A)));seen.add(key)
        result.append((b,key[1],profile(A,b,b),None))
    for n,extras,tris in models(b,max_inner):
        for word in range(1<<len(extras)):
            A=rim|{(y,x) if (word>>j)&1 else (x,y) for j,(x,y) in enumerate(extras)}
            key=(n,tuple(sorted(A)))
            if key in seen: continue
            seen.add(key)
            rot=rotation_from_faces(b,n,tris)
            faces(A,rot)
            p=profile(A,n,b)
            need(any(x is not None for x in p),'candidate not vacuous')
            result.append((n,tuple(sorted(A)),p,tris))
    return tuple(result)

def analysis_one(r,b,kind,position,direction):
    A,R,B={'ear':ear,'cap':cap,'fan':fan}[kind](r,b,position,direction)
    fs=faces(A,R)
    need(any(tuple(f) in {tuple(B[k:]+B[:k]) for k in range(len(B))} for f in fs),'outer face')
    interior=set(R)-set(B)
    semi={x:(sum(y==x for z,y in A),sum(z==x for z,y in A)) for x in interior}
    meta={'residue':[r,b],'kind':kind,'position':position,'direction':direction,'boundary':B,'arcs':sorted(A),'rotation':R,'faces':fs,'internal_semidegrees':semi}
    if any(min(s)<2 for s in semi.values()):
        meta['status']='excluded_small_semidegree';return meta
    P,labels=norm(A,R,B);d=len(B);n=len(labels);full=profile(P,n,d)
    ps=[[] for _ in range(1<<d)]
    for c,rr in enumerate(full):
        if rr is not None: ps[c&((1<<d)-1)].append((c,rr))
    rim_code=sum(1<<i for i in range(d) if ((i+1)%d,i) in P)
    qs=candidates(d,rim_code,n-d-1)
    rules=[]; fails=[]; support=(1<<(1<<d))-1
    impossible={c for c in range(1<<d) if not ps[c]}
    for qi,(nn,aa,pp,tris) in enumerate(qs):
        lift=[];bad=None;possible=set()
        for c,rr in enumerate(pp):
            if rr is None: lift.append(None);continue
            sigma=c&((1<<d)-1);possible.add(sigma)
            match=next((cc for cc,rp in ps[sigma] if rp&~rr==0),None)
            lift.append(match)
            if match is None: bad=c;break
        if bad is None:
            extra={e for e in aa if e[0]<d and e[1]<d and tuple(sorted(e)) not in {tuple(sorted((i,(i+1)%d))) for i in range(d)}}
            old_inside_pairs={tuple(sorted(e)) for e in P if e[0]<d and e[1]<d}- {tuple(sorted((i,(i+1)%d))) for i in range(d)}
            guards=sorted((y,x) for x,y in extra if tuple(sorted((x,y))) not in old_inside_pairs)
            rules.append({'q_index':qi,'vertices':nn,'arcs':aa,'triangles':tris,'guards':guards,'lift':lift})
        else: fails.append(bad)
        support&=sum(1<<x for x in {c&((1<<d)-1) for c,rr in enumerate(pp) if rr is not None})
    common=sorted(c for c in impossible if (support>>c)&1)
    # Keep guard-minimal rules; any omitted rule has a guard superset.
    minimal=[]
    for rule in sorted(rules,key=lambda x:(len(x['guards']),x['vertices'],x['q_index'])):
        g=set(map(tuple,rule['guards']))
        if not any(set(map(tuple,z['guards']))<=g for z in minimal): minimal.append(rule)
    outside=conditioned(P,n,d,qs,ps,rules)
    meta.update({'exterior_cases':outside,'normalized_labels':labels,'rim_code':rim_code,'original_profile':full,'candidate_count':len(qs),'rule_count':len(rules),'common_bad_boundary':common,'status':'has_guarded_rules' if rules else 'no_rule_in_complete_maximal_search','rules':minimal,'failure_masks_hex':None if rules else bytes(fails).hex()})
    return meta

def main():
    report={'verdict':'candidate_only','trusted_verifier_receipt':False,'complete':False,'runtime':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':[]}
    start=time.monotonic()
    try:
        raw=Path(sys.argv[1]).read_bytes()
        need(len(raw)<65536,'input cap')
        data=json.loads(raw)
        need(data['residues']==[list(x) for x in RESIDUES] and data['stages']==['ear','cap','fan'],'frozen allocation')
        report['input_sha256']=hashlib.sha256(raw).hexdigest()
        report['base_revision']=data['base_revision']
        index=int(sys.argv[2]); need(0<=index<4,'batch index')
        report['selected_residue']=list(RESIDUES[index])
        report['batch_index']=index
        for r,b in (RESIDUES[index],):
            for kind,positions,dirs in (('ear',range(4),range(4)),('cap',range(4),range(2)),('fan',range(4),range(8))):
                for pos,direction in it.product(positions,dirs): report['cases'].append(analysis_one(r,b,kind,pos,direction))
        report['complete']=True
        report['summary']={str(res):{status:sum(c['residue']==list(res) and c['status']==status for c in report['cases']) for status in sorted({c['status'] for c in report['cases']})} for res in RESIDUES}
        report['model_counts']={str(b):[sum(n==b+k for n,e,t in models(b,1 if b==5 else 2)) for k in range(3)] for b in (3,4,5)}
        code=0
    except (ValueError,KeyError,TypeError,IndexError) as ex: report['error']=str(ex);code=1
    report['model_library']={str(b):[[n,list(e),t] for n,e,t in models(b,1 if b==5 else 2)] for b in (3,4,5)}
    report['statistics']={kind:{'templates':sum(c['kind']==kind for c in report['cases']),
        'excluded':sum(c['kind']==kind and c['status']=='excluded_small_semidegree' for c in report['cases']),
        'plain_positive':sum(c['kind']==kind and bool(c.get('rules')) for c in report['cases']),
        'exterior_types':sum(len(c.get('exterior_cases',[])) for c in report['cases'] if c['kind']==kind),
        'exterior_positive':sum(e['selected'] is not None for c in report['cases'] if c['kind']==kind for e in c.get('exterior_cases',[]))}
        for kind in ('ear','cap','fan')}
    report['raw_table_semantics']='All vertices/arcs and full profiles retained; negative vectors regenerate every failed maximum-model test. These are finite generator controls.' 
    raw=json.dumps(report,separators=(',',':'),sort_keys=True)+'\n'
    need(len(raw.encode())<4000000,'output cap')
    print(raw,end='');return code
if __name__=='__main__': sys.exit(main())
