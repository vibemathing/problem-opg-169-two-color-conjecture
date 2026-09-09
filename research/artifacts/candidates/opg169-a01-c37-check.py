"""C37 finite degree-six sector generator. Candidate controls, not a trusted verifier.
Run using c37-replay.py. It does not run any C35/C36 enumeration.
"""
import itertools as it,json,sys
from pathlib import Path
D=Path(__file__).parent
INPUT=json.loads((D/'opg169-a01-c37-input.json').read_text())
I=tuple(INPUT['controlled'])
def faces(rot):
 used=set();fs=[]
 for a in sorted(rot):
  for b in rot[a]:
   if (a,b) in used:continue
   e=(a,b);f=[]
   while e not in used:
    used.add(e);u,v=e;f.append(u)
    e=(v,rot[v][(rot[v].index(u)+1)%len(rot[v])])
   assert e==(a,b)
   fs.append(f)
 return fs
T0=INPUT['base_triangles']
A0={tuple(e) for e in INPUT['base_arcs']}

def geom(x,y):
 tris=T0+[[8,7,x],[x,7,y],[7,11,y]]
 succ={};adj={}
 for a,b,c in tris:
  if len({a,b,c})<3:return {'bad':'facial-repeat'}
  for v,l,r in ((b,a,c),(c,b,a),(a,c,b)):
   row=succ.setdefault(v,{})
   if l in row and row[l]!=r:return {'bad':'link-conflict','v':v,'left':l}
   row[l]=r;adj.setdefault(v,set()).update((l,r))
 options={};closed=[]
 for v,row in succ.items():
  if len(set(row.values()))!=len(row):return {'bad':'link-predecessor','v':v}
  ns=adj[v];heads=sorted(ns-set(row.values()));parts=[]
  if not heads:
   first=min(ns);seq=[first];q=row[first]
   while q!=first:
    if q in seq:return {'bad':'link-cycle','v':v}
    seq.append(q);q=row[q]
   if set(seq)!=ns:return {'bad':'link-extra','v':v}
   closed.append([v,len(ns)])
   if v not in I and len(ns)<4:return {'bad':'full-degree-less-four','v':v,'degree':len(ns)}
   options[v]=[seq]
  else:
   for h in heads:
    seq=[h]
    while seq[-1] in row:
     q=row[seq[-1]]
     if q in seq:return {'bad':'partial-cycle','v':v}
     seq.append(q)
    parts.append(seq)
   if sum(map(len,parts))!=len(ns):return {'bad':'link-extra','v':v}
   opts=[]
   for perm in it.permutations(parts[1:]):opts.append(sum([parts[0],*perm],[]))
   options[v]=opts
 vs=sorted(options);edges=sum(map(len,adj.values()))//2
 target={min(tuple(t[k:]+t[:k]) for k in range(3)) for t in tris}
 for choices in it.product(*(options[v] for v in vs)):
  rot=dict(zip(vs,choices));fs=faces(rot)
  canon=lambda f:min(tuple(f[k:]+f[:k]) for k in range(len(f)))
  if len(vs)-edges+len(fs)==2 and target<=set(map(canon,fs)):
   return {'rot':rot,'triangles':tris,'faces':fs,'closed':closed,'n':len(vs),'e':edges}
 return {'bad':'no-plane-completion','n':len(vs),'e':edges}

def make(x,y,w):
 pos=[(8,x),(x,7),(x,y),(y,7),(y,11)]
 extra={e if not (w>>i&1) else e[::-1] for i,e in enumerate(pos)}
 a=A0|extra
 if any(u==v or (v,u) in a for u,v in a):return None
 return a

def state(arcs,vs,B,c):
 vs=tuple(vs);ind={v:i for i,v in enumerate(vs)};r=[0]*len(vs)
 for u,v in arcs:
  if u in ind and v in ind and ((c>>u)^(c>>v))&1==0:r[ind[u]]|=1<<ind[v]
 for k in range(len(vs)):
  bit=1<<k
  for i in range(len(vs)):
   if r[i]&bit:r[i]|=r[k]
 if any(r[i]>>i&1 for i in range(len(vs))):return None
 out=0
 for i,u in enumerate(B):
  for j,v in enumerate(B):
   if r[ind[u]]>>ind[v]&1:out|=1<<(i*len(B)+j)
 return out

def mask(order,k):return sum(((k>>i)&1)<<v for i,v in enumerate(order))


def options(cycle):
 n=len(cycle);pairs=[(i,j) for i in range(n) for j in range(i+1,n) if j-i not in(1,n-1)]
 cross=lambda a,b:len(set(a+b))==4 and ((a[0]<b[0]<a[1])!=(a[0]<b[1]<a[1]))
 for k in range(n-2):
  for es in it.combinations(pairs,k):
   if any(cross(e,f) for e,f in it.combinations(es,2)):continue
   for bits in range(1<<k):yield tuple((cycle[b],cycle[a]) if bits>>l&1 else (cycle[a],cycle[b]) for l,(a,b) in enumerate(es))


def try_vertex(pair,w,v):
 a=make(*pair,w);g=geom(*pair);V=sorted(g['rot']);B=sorted(set(V)-set(I));K=tuple(x for x in I if x!=v);q0={e for e in a if v not in e};qv=sorted(set(V)-{v})
 ps=[]
 for b in range(1<<len(B)):
  bc=mask(B,b);rs=[]
  for j in range(16):
   r=state(a,V,B,bc|mask(I,j))
   if r is not None:rs.append((j,r))
  ps.append(rs)
 bad=[]
 for opt in sorted(options(g['rot'][v]),key=lambda oo:(sum(set(e)<=set(B) and e not in a for e in oo),len(oo),oo)):
  if any(e[::-1] in q0 for e in opt):bad.append([opt,'reverse']);continue
  q=q0|set(opt);vec=[];fail=None
  for b in range(1<<len(B)):
   bc=mask(B,b)
   for k in range(1<<len(K)):
    r=state(q,qv,B,bc|mask(K,k))
    if r is None:vec.append('-');continue
    f=next((j for j,pr in ps[b] if pr&~r==0),None)
    if f is None:fail=(b,k);break
    vec.append(format(f,'x'))
   if fail:break
  if fail is None:return {'delete':v,'added':opt,'vec':''.join(vec),'guards':[e[::-1] for e in opt if set(e)<=set(B) and e not in a],'failed_previous':bad}
  bad.append([opt,fail])
 return {'delete':v,'failed':bad}

def tri_cells(poly,es):
 if len(poly)==3:return [poly]
 for i in range(len(poly)):
  a,b,c=poly[i-1],poly[i],poly[(i+1)%len(poly)]
  if frozenset((a,c)) in es:
   return [[a,b,c]]+tri_cells(poly[:i]+poly[i+1:],es-{frozenset((a,c))})
 raise ValueError('no ear')

def fullrot(tris):
 su={}
 for a,b,c in tris:
  for v,x,y in ((a,c,b),(b,a,c),(c,b,a)):
   row=su.setdefault(v,{})
   assert x not in row or row[x]==y
   row[x]=y
 rt={}
 for v,row in su.items():
  first=min(row);r=[first];z=row[first]
  while z!=first:
   assert z not in r;r.append(z);z=row[z]
  assert len(r)==len(row);rt[v]=r
 assert len(rt)-sum(map(len,rt.values()))//2+len(faces(rt))==2
 return rt

def marks(A,rt):
 ts=faces(rt);E={frozenset(e) for e in A};tags=[]
 for uv in sorted(E,key=lambda e:tuple(sorted(e))):
  u,v=sorted(uv)
  if len(rt[u])!=4 or len(rt[v])!=4:continue
  pp=[next(w for w in f if w not in uv) for f in ts if uv<=set(f)]
  if len(pp)!=2:raise ValueError('not triangulation')
  found=False
  for uu,vv in ((u,v),(v,u)):
   for p,q in (pp,pp[::-1]):
    aa=next(x for x in rt[uu] if x not in (vv,p,q));bb=next(x for x in rt[vv] if x not in (uu,p,q))
    if aa==bb:continue
    labels=[p,aa,q,bb,uu,vv]
    r=sum((1<<i) for i in range(4) if (labels[(i+1)%4],labels[i]) in A)
    positions=[(0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5)]
    b=sum((1<<i) for i,(x,y) in enumerate(positions) if (labels[y],labels[x]) in A)
    if (r,b) in ((1,78),(1,100),(3,43),(5,77)) or (15-r,127-b) in ((1,78),(1,100),(3,43),(5,77)):
     donor=next(x for x in (p,q) if ((x,uu) in A)==((x,vv) in A))
     tags.append([u,v,donor]);found=True;break
   if found:break
 return tags



def cyclic(f):
    return min(tuple(f[k:]+f[:k]) for k in range(len(f)))


def family(index):
    pair=tuple(INPUT['surviving_pairs'][index]);g=geom(*pair)
    assert 'bad' not in g
    B=sorted(set(g['rot'])-set(I));rows=[]
    for w in range(32):
        # First try literal deletion of 3, with all remaining I colours movable.
        a=make(*pair,w);vs=sorted(g['rot']);K=(0,2,7)
        q={e for e in a if 3 not in e};qv=sorted(set(vs)-{3});vec=[];gaps=[]
        for b in range(1<<len(B)):
            bc=mask(B,b)
            ps=[(j,state(a,vs,B,bc|mask(I,j))) for j in range(16)]
            ps=[(j,r) for j,r in ps if r is not None]
            for k in range(8):
                rq=state(q,qv,B,bc|mask(K,k))
                if rq is None:vec.append('-');continue
                j=next((j for j,r in ps if r&~rq==0),None)
                vec.append('!' if j is None else format(j,'x'))
                if j is None:gaps.append([b,k])
        if not gaps:
            rule={'delete':3,'added':[],'guards':[],'vec':''.join(vec)}
        else:
            rule=try_vertex(pair,w,7)
            rule['bare3_gaps']=gaps
        rows.append({'word':w,'rule':rule})
    initial=[(12,13)]+[(v,13) for v in (4,5,6)]+[(12,v) for v in (4,5,6)]+list(it.permutations((4,5,6),2))
    aliases=[{'pair':p,'result':geom(*p)} for p in initial] if index==0 else []
    counts={v:sum(f.count(v) for f in g['triangles']) for v in g['rot']}
    return {'part':index,'pair':pair,'geometry':g,'boundary':B,'corner_counts':counts,'rows':rows,'aliases':aliases}


def cycle(A,vs,c):
    for k in (0,1):
        colour={v for v in vs if c>>v&1==k};adj={v:sorted(b for a,b in A if a==v and b in colour) for v in colour}
        done=set();active=[]
        def visit(v):
            active.append(v)
            for w in adj[v]:
                if w in active:return active[active.index(w):]+[w]
                if w not in done:
                    got=visit(w)
                    if got:return got
            active.pop();done.add(v)
        for v in sorted(colour):
            if v not in done:
                got=visit(v)
                if got:return [k,got]
    raise ValueError('no claimed cycle')


def obstruction():
    from fractions import Fraction
    W=INPUT['witness'];A={tuple(e) for e in W['arcs']};rt={int(v):r for v,r in W['rotation'].items()}
    vs=sorted(rt);B=W['boundary'];g=geom(12,13);assert len(vs)==11
    assert min(map(len,rt.values()))>=4
    assert all(min(sum(a==v for a,b in A),sum(b==v for a,b in A))>=2 for v in vs)
    assert marks(A,rt)==[]
    domain=[];bad_cycles={};profiles=[]
    for b in range(1<<len(B)):
        bc=mask(B,b);poss=[]
        for j in range(16):
            c=bc|mask(I,j);r=state(A,vs,B,c)
            if r is not None:poss.append([j,r])
        profiles.append(poss)
        if poss:domain.append(b)
        else:bad_cycles[b]=[cycle(A,vs,bc|mask(I,j)) for j in range(16)]
    rows=[]
    for v in I:
        qv=sorted(set(vs)-{v});K=tuple(x for x in I if x!=v)
        for opt in options(rt[v]):
            q={e for e in A if v not in e}|set(opt)
            assert not any(e[::-1] in q for e in q)
            statuses=[];first=None
            for b in range(1<<len(B)):
                bc=mask(B,b)
                for k in range(8):
                    rq=state(q,qv,B,bc|mask(K,k))
                    status='-' if rq is None else 'B' if not profiles[b] else 'E'
                    statuses.append(status)
                    if status=='B' and first is None:first=[b,k]
            assert first is not None
            rows.append({'delete':v,'added':opt,'all_Q_status':''.join(statuses),'failure':first})
    assert len(rows)==308
    fs=faces(rt);actual=set(map(cyclic,g['triangles']));ledger=[]
    for f in fs:
        gamma=sum((Fraction(len(rt[v])-4,len(rt[v])) for v in f),Fraction(0))
        ledger.append({'face':f,'h':0,'gamma_sum':str(gamma),'charge':str(gamma-1),'controlled':cyclic(f) in actual})
    assert sum(Fraction(r['charge']) for r in ledger)==-8
    # Exhaust all smallest-order (ten-vertex) completions of the four aliased cores.
    ten=[];allocated=0
    for pair in INPUT['surviving_pairs'][1:]:
        gg=geom(*pair);actual=set(map(cyclic,gg['triangles']));regions=[f for f in gg['faces'] if cyclic(f) not in actual]
        quad=next(f for f in regions if len(f)==4);tr=next(f for f in regions if len(f)==3)
        for w in range(32):
            for opt in options(quad):
                if len(opt)!=1:continue
                allocated+=1;aa=make(*pair,w)|set(opt);vv=sorted(gg['rot'])
                if any(min(sum(u==v for u,z in aa),sum(z==v for u,z in aa))<2 for v in vv):continue
                rot=fullrot(gg['triangles']+[tr]+tri_cells(quad,{frozenset(e) for e in opt}))
                assert min(map(len,rot.values()))>=4
                bb=sorted(set(vv)-set(I));kk=(0,2,7);vec=[]
                for b in range(1<<len(bb)):
                    bc=mask(bb,b);poss=[j for j in range(16) if state(aa,vv,[],bc|mask(I,j)) is not None]
                    for k in range(8):
                        if state(aa,set(vv)-{3},[],bc|mask(kk,k)) is None:vec.append('-');continue
                        assert poss;vec.append(format(poss[0],'x'))
                ten.append({'pair':pair,'word':w,'added':opt,'extension_vector':''.join(vec)})
    assert allocated==512 and len(ten)==4
    return {'part':'obstruction','witness':W,'attainable_boundary_words':domain,'full_profiles':profiles,'nonextendable_boundary_cycles':bad_cycles,'alternatives':rows,'face_ledger':ledger,'ten_vertex_allocation':allocated,'ten_vertex_realizations':ten}


def main():
    import hashlib
    arg=sys.argv[1]
    obj=obstruction() if arg=='obstruction' else family(int(arg))
    obj['verdict']='candidate_only';obj['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    obj['input_sha256']=hashlib.sha256((D/'opg169-a01-c37-input.json').read_bytes()).hexdigest()
    text=json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n'
    assert len(text.encode())<=1048576
    print(text,end='')
if __name__=='__main__':main()
