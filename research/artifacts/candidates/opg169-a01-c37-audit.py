"""Separate DFS/BFS consumer for C37. Same generator trust domain, not Evidence."""
import base64
from collections import deque
from fractions import Fraction
import hashlib
import itertools as it
import json
import lzma
from pathlib import Path
D=Path(__file__).parent

def require(p,msg):
    if not p:raise ValueError(msg)

def encode(order,m):return sum(((m>>i)&1)<<v for i,v in enumerate(order))

def relation(E,V,B,c):
    V=set(V);adj={v:[] for v in V}
    for u,v in E:
        if u in V and v in V and (c>>u&1)==(c>>v&1):adj[u].append(v)
    mark={v:0 for v in V}
    def dfs(u):
        mark[u]=1
        for v in adj[u]:
            if mark[v]==1:return False
            if mark[v]==0 and not dfs(v):return False
        mark[u]=2;return True
    if any(mark[v]==0 and not dfs(v) for v in V):return None
    R=0
    for i,u in enumerate(B):
        todo=deque(adj[u]);seen=set(adj[u])
        while todo:
            v=todo.popleft()
            for w in adj[v]:
                if w not in seen:seen.add(w);todo.append(w)
        for j,v in enumerate(B):
            if v in seen:R|=1<<(i*len(B)+j)
    return R

def canon(f):return min(tuple(f[i:]+f[:i]) for i in range(len(f)))

def embedding(rot,E,stipulated):
    rot={int(k):v for k,v in rot.items()};arcs={(u,v) for u in rot for v in rot[u]}
    require(all(u!=v and (v,u) in arcs for u,v in arcs),'symmetric simple darts')
    require(all(len(r)==len(set(r)) for r in rot.values()),'distinct neighbours')
    require({frozenset(e) for e in E}=={frozenset(e) for e in arcs},'all edges accounted')
    unseen=set(arcs);fs=[]
    while unseen:
        a=min(unseen);e=a;f=[]
        while e in unseen:
            unseen.remove(e);u,v=e;f.append(u);e=(v,rot[v][(rot[v].index(u)+1)%len(rot[v])])
        require(e==a,'face return');fs.append(f)
    require(len(rot)-len(arcs)//2+len(fs)==2,'sphere Euler')
    require(set(map(canon,stipulated))<=set(map(canon,fs)),'actual triangular sectors')
    reached={min(rot)};todo=list(reached)
    while todo:
        for v in rot[todo.pop()]:
            if v not in reached:reached.add(v);todo.append(v)
    require(len(reached)==len(rot),'connected embedding')
    return fs

def fills(C):
    n=len(C);pairs=[(i,j) for i in range(n) for j in range(i+1,n) if (j-i)%n not in (1,n-1)]
    def cross(e,f):
        a,b=e;c,d=f
        return (a<c<b<d) or (c<a<d<b)
    for k in range(n-2):
        for comb in it.combinations(pairs,k):
            if any(cross(a,b) for a,b in it.combinations(comb,2)):continue
            for bits in range(1<<k):yield tuple((C[v],C[u]) if bits>>i&1 else (C[u],C[v]) for i,(u,v) in enumerate(comb))

def edges(base,x,y,w):
    pos=[(8,x),(x,7),(x,y),(y,7),(y,11)]
    return set(base)|{e[::-1] if w>>i&1 else e for i,e in enumerate(pos)}

def main():
    raw=(D/'opg169-a01-c37-input.json').read_bytes();inp=json.loads(raw);I=tuple(inp['controlled']);base={tuple(e) for e in inp['base_arcs']}
    ab=(D/'opg169-a01-c37-certificate-archive.json').read_bytes();a=json.loads(ab)
    require(a['decoded_bytes']<=1048576,'decoded size cap')
    z=lzma.LZMADecompressor();body=z.decompress(base64.b64decode(a['data']),max_length=1048577)
    require(z.eof and len(body)==a['decoded_bytes'] and hashlib.sha256(body).hexdigest()==a['decoded_sha256'],'archive identity')
    C=json.loads(body);require(len(C['parts'])==5,'all geometric parts')
    aliases=C['parts'][0]['aliases'];expected={(12,13)}|{(v,13) for v in(4,5,6)}|{(12,v) for v in(4,5,6)}|set(it.permutations((4,5,6),2))
    require({tuple(q['pair']) for q in aliases}==expected,'complete initial equality allocation')
    for q in aliases:
        x,y=q['pair'];g=q['result'];ts=inp['base_triangles']+[[8,7,x],[x,7,y],[7,11,y]]
        if 'bad' not in g:
            embedding(g['rot'],edges(base,x,y,0),ts);continue
        if g['bad']=='full-degree-less-four':
            v=g['v'];suc={}
            for f in ts:
                if v in f:
                    i=f.index(v);suc[f[i-1]]=f[(i+1)%3]
            require(len(suc)==3 and set(suc)==set(suc.values()),'closed degree-three star')
        elif g['bad']=='link-conflict':
            v=g['v'];l=g['left'];rs=set()
            for f in ts:
                if v in f:
                    i=f.index(v)
                    if f[i-1]==l:rs.add(f[(i+1)%3])
            require(len(rs)>1,'incompatible actual facial sectors')
        else:
            E={frozenset(e) for e in edges(base,x,y,0)};V=set().union(*E)
            require(len(E)>3*len(V)-6,'explicit planar edge-bound obstruction')
    stats={'geometries':5,'direction_words':160,'unguarded_rules':0,'guarded_rules':0,'residuals':0,'positive_lifts':0,'strict_R_lifts':0,'reversed_lifts':0,'negative_option_witnesses':0,'whole_alternatives':0,'whole_Q_assignments':0,'whole_valid_Q':0,'whole_nonextendable_Q':0}
    residual=[]
    for part in C['parts']:
        require(part['input_sha256']==hashlib.sha256(raw).hexdigest(),'input binding')
        x,y=part['pair'];rot={int(k):v for k,v in part['geometry']['rot'].items()};V=sorted(rot);B=part['boundary']
        require(set(B)==set(V)-set(I),'fixed interface')
        tris=inp['base_triangles']+[[8,7,x],[x,7,y],[7,11,y]]
        fs=embedding(rot,edges(base,x,y,0),tris)
        require(len(tris)==13 and [len(rot[v]) for v in I]==[5,5,5,6],'saturated controlled stars')
        require({int(v):n for v,n in part['corner_counts'].items()}=={v:sum(f.count(v) for f in tris) for v in V},'all corner debits')
        require([r['word'] for r in part['rows']]==list(range(32)),'all directions')
        for row in part['rows']:
            w=row['word'];P=edges(base,x,y,w);rule=row['rule'];delete=rule['delete'];K=tuple(v for v in I if v!=delete);QV=set(V)-{delete}
            allp=[]
            for b in range(1<<len(B)):
                bc=encode(B,b);allp.append([relation(P,V,B,bc|encode(I,j)) for j in range(16)])
            if 'vec' in rule:
                added={tuple(e) for e in rule['added']};Q={e for e in P if delete not in e}|added
                require(all(u!=v and (v,u) not in Q for u,v in Q),'simple oriented replacement')
                require(frozenset(added) in {frozenset(o) for o in fills(rot[delete])},'same-hole planar infill')
                guard={e[::-1] for e in added if set(e)<=set(B) and e not in P}
                require(guard=={tuple(e) for e in rule['guards']},'all exterior reverse-arc guards')
                stats['guarded_rules' if guard else 'unguarded_rules']+=1
                require(len(rule['vec'])==8*(1<<len(B)),'all full Q assignments')
                for ix,ch in enumerate(rule['vec']):
                    b,k=divmod(ix,8);bc=encode(B,b);qc=bc|encode(K,k);rq=relation(Q,QV,B,qc)
                    if rq is None:require(ch=='-','explicit invalid assignment');continue
                    require(ch not in('-','!'),'a full lift exists');j=int(ch,16);rp=allp[b][j]
                    require(rp is not None and rp&~rq==0,'positive relation containment')
                    stats['positive_lifts']+=1;stats['strict_R_lifts']+=rp!=rq
                    p_rev={e[::-1] for e in P};q_rev={e[::-1] for e in Q}
                    rpr=relation(p_rev,V,B,bc|encode(I,j));rqr=relation(q_rev,QV,B,qc)
                    require(rpr is not None and rqr is not None and rpr&~rqr==0,'full reversal control');stats['reversed_lifts']+=1
            else:
                stats['residuals']+=1;residual.append([part['pair'],w]);records=rule['failed']
                require(len(records)==215 and {frozenset(map(tuple,r[0])) for r in records}=={frozenset(o) for o in fills(rot[7])},'complete remaining hole catalogue')
                for oo,bad in records:
                    added=set(map(tuple,oo));q0={e for e in P if 7 not in e}
                    if bad=='reverse':require(any(e[::-1] in q0 for e in added),'real reverse conflict');continue
                    b,k=bad;rq=relation(q0|added,set(V)-{7},B,encode(B,b)|encode((0,2,3),k))
                    require(rq is not None and not any(r is not None and r&~rq==0 for r in allp[b]),'real finite containment failure');stats['negative_option_witnesses']+=1
    W=C['obstruction'];wi=W['witness'];A=set(map(tuple,wi['arcs']));rot={int(k):v for k,v in wi['rotation'].items()};V=sorted(rot);B=wi['boundary']
    fs=embedding(rot,A,inp['base_triangles']+[[8,7,12],[12,7,13],[7,11,13]])
    require(len(V)==11 and min(map(len,rot.values()))>=4,'whole witness class')
    require(all(min(sum(a==v for a,b in A),sum(b==v for a,b in A))>=2 for v in V),'whole witness semidegrees')
    require(not any(len(rot[u])==4 and len(rot[v])==4 for u,v in A),'no low-low edge, so t=h=0')
    profiles=[];full=[]
    for b in range(1<<len(B)):
        bc=encode(B,b);poss=[]
        for j in range(16):
            c=bc|encode(I,j);r=relation(A,V,B,c)
            if r is not None:poss.append([j,r]);full.append(c)
        profiles.append(poss)
    require(profiles==W['full_profiles'] and sorted(full)==sorted(wi['all_full_colourings']),'complete full graph colouring domain')
    require([b for b,p in enumerate(profiles) if p]==W['attainable_boundary_words'],'all boundary colourings')
    for bs,cycles in W['nonextendable_boundary_cycles'].items():
        b=int(bs);require(not profiles[b] and len(cycles)==16,'every interior choice rejected')
        for j,(k,cy) in enumerate(cycles):
            c=encode(B,b)|encode(I,j)
            require(len(cy)>=4 and cy[0]==cy[-1] and len(set(cy[:-1]))==len(cy)-1,'positive simple cycle')
            require(all((u,v) in A for u,v in zip(cy,cy[1:])) and all(c>>v&1==k for v in cy),'actual monochromatic cycle')
    require(len(W['alternatives'])==308,'all allocated whole replacements')
    for v in I:
        records=[r for r in W['alternatives'] if r['delete']==v]
        require({frozenset(map(tuple,r['added'])) for r in records}=={frozenset(o) for o in fills(rot[v])},'complete hole catalogue')
        K=tuple(u for u in I if u!=v);qv=set(V)-{v}
        for row in records:
            Q={e for e in A if v not in e}|set(map(tuple,row['added']));text=row['all_Q_status'];require(len(text)==1024,'complete whole Q assignment table')
            require('B' in text,'at least one actual failure for each replacement')
            for ix,ch in enumerate(text):
                b,k=divmod(ix,8);r=relation(Q,qv,[],encode(B,b)|encode(K,k));expected='-' if r is None else 'E' if profiles[b] else 'B'
                require(ch==expected,'full exterior status not just boundary projection');stats['whole_Q_assignments']+=1
                stats['whole_valid_Q']+=ch!='-';stats['whole_nonextendable_Q']+=ch=='B'
            stats['whole_alternatives']+=1
    ledger=W['face_ledger'];require({canon(r['face']) for r in ledger}==set(map(canon,fs)),'every face accounted')
    total=Fraction(0)
    for row in ledger:
        f=row['face'];g=sum((Fraction(len(rot[v])-4,len(rot[v])) for v in f),Fraction(0));require(row['h']==0 and g==Fraction(row['gamma_sum']) and g-1==Fraction(row['charge']),'whole DC2 ledger');total+=g-1
    require(total==-8,'conserved total')
    # Minimality control: every ten-vertex completion has four possible directed diagonals.
    realized=[];allocated=0
    for part in C['parts'][1:]:
        x,y=part['pair'];gg=part['geometry'];actual=set(map(canon,gg['triangles']));regions=[f for f in gg['faces'] if canon(f) not in actual];quad=next(f for f in regions if len(f)==4);vv=sorted(map(int,gg['rot']));bb=sorted(set(vv)-set(I))
        for w in range(32):
            for oo in fills(quad):
                if len(oo)!=1:continue
                allocated+=1;aa=edges(base,x,y,w)|set(oo)
                if any(min(sum(u==v for u,z in aa),sum(z==v for u,z in aa))<2 for v in vv):continue
                realized.append((x,y,w,oo));row=next(r for r in W['ten_vertex_realizations'] if r['pair']==[x,y] and r['word']==w and set(map(tuple,r['added']))==set(oo))
                for ix,ch in enumerate(row['extension_vector']):
                    b,k=divmod(ix,8);bc=encode(bb,b);q=relation(aa,set(vv)-{3},[],bc|encode((0,2,7),k))
                    if q is None:require(ch=='-','ten-vertex invalid');continue
                    require(ch!='-' and relation(aa,vv,[],bc|encode(I,int(ch,16))) is not None,'ten-vertex full extension')
    require(allocated==512 and len(realized)==4,'all smallest complete realizations')
    require((stats['unguarded_rules'],stats['guarded_rules'],stats['residuals'])==(122,29,9),'allocated outcome count')
    stats.update({'format':'c37-consumer-output-v1','verdict':'candidate_only','archive_sha256':hashlib.sha256(ab).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),'residual_types':residual,'whole_graph_valid_colourings':len(full),'whole_graph_attainable_boundary_words':len(W['attainable_boundary_words']),'smallest_completion_controls':allocated,'trusted_receipt':False,'status':'all_declared_checks_passed'})
    print(json.dumps(stats,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
