"""Exact nine-donor finite certificates; generator checks, not trusted admission.
Run from a repository-shaped root. All vertex labels and arc sets are explicit.
"""
import argparse, base64, hashlib, itertools as it, json, lzma, platform
from collections import Counter
from fractions import Fraction
from pathlib import Path

CORES=((1,78),(1,100),(3,43),(5,77))
EXTRA=((0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5))
H=(1,2,3); Q=(10,11,12)
LOWS=(4,5,6,7,8,9)
SECTORS=[(H[i],Q[i],H[(i+1)%3],4+2*i,5+2*i) for i in range(3)]
BOUNDARY=(1,10,2,11,3,12)
PREFIX=Path('research/artifacts/candidates/opg169-a01-nine-donor')

def need(ok,msg):
    if not ok: raise ValueError(msg)

def core(r,b):
    return {(i,(i+1)%4) if not (r>>i)&1 else ((i+1)%4,i) for i in range(4)} | {
        (y,x) if (b>>j)&1 else (x,y) for j,(x,y) in enumerate(EXTRA)}

def templates(a,q,b,u,v):
    sk={frozenset(e) for e in [(0,a),(a,q),(q,b),(b,0),(0,u),(a,u),(u,q),(u,v),(0,v),(v,q),(v,b)]}
    out={}
    for r,c in CORES:
        p=0 if (r,c) in CORES[:2] else 2
        for ends,lows,rev in it.product(it.permutations((a,b)),it.permutations((u,v)),(0,1)):
            lab={p:0,2-p:q,1:ends[0],3:ends[1],4:lows[0],5:lows[1]}
            A=tuple(sorted((lab[y],lab[x]) if rev else (lab[x],lab[y]) for x,y in core(r,c)))
            if {frozenset(e) for e in A}==sk and {(a,0),(b,0),(0,u),(0,v)}<=set(A):
                out[A]=[r,c,[lab[k] for k in range(6)],rev]
    need(len(out)==8,'eight local residual directions')
    return sorted(out.items())

T=[templates(*s) for s in SECTORS]

def inner_faces():
    fs=[]
    for a,q,b,u,v in SECTORS:
        fs += [[0,u,a],[0,v,u],[0,b,v],[a,u,q],[q,v,b],[q,u,v]]
    return fs

def permitted_partitions():
    # Restricted-growth fresh names plus the sole nonincident high allowed for each q.
    out=[]
    def visit(i,chosen,fresh):
        if i==3:
            out.append(tuple(chosen));return
        for target in [H[(i+2)%3]]+fresh+[10+len(fresh)]:
            visit(i+1,chosen+[target],fresh+[target] if target>=10 and target not in fresh else fresh)
    visit(0,[],[])
    need(len(set(out))==15,'fifteen equality patterns')
    return out

def split_closed_walk(w):
    # Splitting at a repeated port produces the actual complementary boundary components.
    for i,x in enumerate(w):
        for j in range(i+1,len(w)):
            if w[j]==x:
                return split_closed_walk(w[i:j])+split_closed_walk(w[j:]+w[:i])
    return [w]

def rotation_check(A,fs):
    darts=set(A)|{(y,x) for x,y in A}
    need(all(x!=y and (y,x) not in A for x,y in A),'simple orientation')
    succ={};used=set()
    for face in fs:
        need(len(face)>=3 and len(face)==len(set(face)),'simple capped face')
        for k,x in enumerate(face):
            y=face[(k+1)%len(face)];z=face[(k+2)%len(face)]
            need((x,y) in darts and (x,y) not in used,'dart coverage once')
            used.add((x,y));need((y,x) not in succ,'unique rotation successor')
            succ[y,x]=z
    need(used==darts,'all darts covered')
    R={}
    V={x for e in A for x in e}
    for x in sorted(V):
        ns={y for a,y in darts if a==x};start=min(ns);seq=[];y=start
        while y not in seq:
            seq.append(y);y=succ[x,y]
        need(y==start and set(seq)==ns,'one vertex link, not a split rotation')
        R[x]=seq
    seen=set();todo=[min(V)]
    while todo:
        x=todo.pop()
        if x not in seen:seen.add(x);todo.extend(R[x])
    need(seen==V and len(V)-len(A)+len(fs)==2,'connected sphere rotation')
    return R

def alias_audit():
    A=set().union(*(set(ts[0][0]) for ts in T));ans=[]
    for pat in permitted_partitions():
        sub=dict(zip(Q,pat));E={frozenset((sub.get(x,x),sub.get(y,y))) for x,y in A}
        need(all(len(e)==2 for e in E),'no underlying loop in allocation')
        verts=set().union(*E);rec={'q_targets':list(pat),'vertices':len(verts),'edges':len(E)}
        pairs=[(i,j) for i,j in it.combinations(range(3),2) if pat[i]==pat[j]]
        if pairs:
            i,j=pairs[0];common=next(x for x in (H[i],H[(i+1)%3]) if x in (H[j],H[(j+1)%3]))
            rec.update(status='excluded_endpoint_degree',saturated_high=common,degree=sum(common in e for e in E))
            f=[list(map(lambda x:sub.get(x,x),face)) for face in inner_faces() if common in face]
            neighbours=set().union(*(set(face) for face in f))-{common}
            edges={frozenset(set(face)-{common}) for face in f}
            need(len(f)==4 and len(neighbours)==4 and len(edges)==4,'four distinct facial sectors')
            need(all(sum(y in e for e in edges)==2 for y in neighbours),'closed four-face link')
            rec['saturating_faces']=f
            if rec['degree']>4:
                rec['status']='excluded_rotation_conflict'
                rec['required_extra_neighbours']=sorted(set().union(*(set(e) for e in E if common in e))-{common}-neighbours)
                need(bool(rec['required_extra_neighbours']),'extra neighbours conflict with closed link')
            else:
                need(rec['degree']==4,'saturated high degree four')
        else:
            hits=[i for i in range(3) if pat[i] in H]
            if len(hits)>=2:
                need(len(E)>3*len(verts)-6,'Euler excludes two or three crossed identifications')
                rec.update(status='excluded_nonplanar',planar_edge_max=3*len(verts)-6)
            else:
                rec.update(status='allowed',alias_sector=hits[0] if hits else -1)
                AA={(sub.get(x,x),sub.get(y,y)) for x,y in A}
                fs=[[sub.get(x,x) for x in face] for face in inner_faces()]
                outside=split_closed_walk([sub.get(x,x) for x in BOUNDARY])
                rec['rotation']=rotation_check(AA,fs+outside);rec['complementary_faces']=outside
        ans.append(rec)
    need(Counter(r['status'] for r in ans)=={'allowed':4,'excluded_endpoint_degree':4,'excluded_rotation_conflict':3,'excluded_nonplanar':4},'complete alias partition')
    return ans

def adjacency(A,n):
    out=[0]*n
    for x,y in A:out[x]|=1<<y
    return out

def dag_table(A,n):
    out=adjacency(A,n);good=bytearray(1<<n);good[0]=1
    for S in range(1,1<<n):
        left=S
        while left:
            bit=left&-left;v=bit.bit_length()-1
            if not out[v]&S:
                good[S]=good[S^bit];break
            left^=bit
    return good

def relation(A,n,b,c):
    rows=[0]*n
    for x,y in A:
        if ((c>>x)^(c>>y))&1==0:rows[x]|=1<<y
    for k in range(n):
        bit=1<<k
        for x in range(n):
            if rows[x]&bit:rows[x]|=rows[k]
    return tuple(rows[x]&((1<<b)-1) for x in range(b))

def dfs_bfs(A,n,b,c):
    # Deliberately different checker from subset/sink DP and bitset closure.
    out=[[] for _ in range(n)]
    for x,y in A:
        if ((c>>x)^(c>>y))&1==0:out[x].append(y)
    mark=[0]*n
    def dfs(x):
        mark[x]=1
        for y in out[x]:
            if mark[y]==1 or mark[y]==0 and not dfs(y):return False
        mark[x]=2;return True
    if any(mark[x]==0 and not dfs(x) for x in range(n)):return None
    rel=[]
    for x in range(b):
        todo=list(out[x]);seen=set()
        while todo:
            y=todo.pop()
            if y not in seen:seen.add(y);todo.extend(out[y])
        rel.append(sum(1<<y for y in seen if y<b))
    return tuple(rel)

def case(choices,alias):
    A=set().union(*(set(T[j][k][0]) for j,k in enumerate(choices)))
    sub={} if alias<0 else {Q[alias]:H[(alias+2)%3]}
    A={(sub.get(x,x),sub.get(y,y)) for x,y in A}
    B=list(dict.fromkeys(sub.get(x,x) for x in BOUNDARY))
    fs=[[sub.get(x,x) for x in f] for f in inner_faces()]
    outside=split_closed_walk([sub.get(x,x) for x in BOUNDARY]);rot=rotation_check(A,fs+outside)
    need(len(rot[0])==9 and all(len(rot[x])==4 for x in LOWS),'complete interior degrees')
    need([sum(y==0 for x,y in A),sum(x==0 for x,y in A)]==[3,6],'donor directions')
    need(all(sum(y==x for z,y in A)==2 and sum(z==x for z,y in A)==2 for x in LOWS),'low semidegrees')
    names=B+[0]+list(LOWS);n=len(names);b=len(B);lab={x:i for i,x in enumerate(names)}
    AA=tuple(sorted((lab[x],lab[y]) for x,y in A));BB=tuple((x,y) for x,y in AA if x<b and y<b)
    need(n-b==7,'seven actual deletions')
    good=dag_table(AA,n);gq=dag_table(BB,b);full=(1<<n)-1;mask=(1<<b)-1
    vec=[];verified=0;sum_valid_original=sum(bool(good[c] and good[full^c]) for c in range(1<<n))
    for c in range(1<<b):
        if not(gq[c] and gq[mask^c]):
            need(dfs_bfs(BB,b,b,c) is None,'invalid Q crosscheck');vec.append(None);continue
        rq=relation(BB,b,b,c);need(rq==dfs_bfs(BB,b,b,c),'Q relation engines')
        chosen=None
        for internal in range(1<<7):
            cc=c|(internal<<b)
            if not(good[cc] and good[full^cc]):continue
            rp=relation(AA,n,b,cc)
            if all(x&~y==0 for x,y in zip(rp,rq)):
                chosen=cc;need(rp==dfs_bfs(AA,n,b,cc),'original witness independent algorithm');break
        need(chosen is not None,'no all-exterior bare-interface lift for '+str((choices,alias,c)))
        vec.append(chosen);verified+=1
    # First geometry per alias is stored separately; all other instances use the same construction.
    geom={'names':names,'rotation':rot,'original_arcs':sorted(A),'retained_arcs':[e for e in sorted(A) if e[0] in B and e[1] in B],
          'interior_faces':fs,'complementary_faces':outside}
    return {'alias_sector':alias,'directions':list(choices),'lift':vec,'valid_original_assignments':sum_valid_original},verified,geom

def charges():
    tested=0
    for d in range(4,101):
        for t in range(d//3+1):
            if t and d<6 or d in (6,7) and t>=2 or d==9 and t==3:continue
            need(2*t<=d-4,'all surviving double budgets')
            gamma=Fraction(d-4-2*t,d)
            need(gamma>=0 and d*gamma+2*t==d-4,'exact every-vertex debit')
            tested+=1
    need(Fraction(9-4-2*3,9)==Fraction(-1,9),'mutation: do not double-pay the exception without excluding it')
    return {'bounded_parameter_checks':tested,'degree_cap_control_only':100,
            'all_degree_proof':'t<=floor(d/3); d6,7:t<=1; exclude d9,t3; remaining integer cases proved separately',
            'vertex_balance':'d-4-2t-d*gamma=0',
            'all_face_formula':'length-4+sum_corners gamma+h',
            'comparison_with_C33':'extra donor-side credits minus sum_corners t/d',
            'unpaid_triangle_negative_iff':'sum_corners gamma<1',
            'root_charge_total':-8,'all_nonnegative_claim':False}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output-prefix',default=str(PREFIX));a=p.parse_args()
    output=Path(a.output_prefix);need(platform.python_version()=='3.13.5','fixed Python version')
    cert={'format':'nine-donor-all-boundary-lifts-v1','verdict':'candidate_only','trusted_verifier_receipt':False,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'labelled_sectors':SECTORS,'sector_templates':[[[list(e) for e in A] for A,src in ts] for ts in T],
          'sector_template_sources':[[src for A,src in ts] for ts in T],
          'alias_classification':alias_audit(),'rows':[],'geometry_examples':{},'complete':False}
    byalias=[]
    for alias in (-1,0,1,2):
        count=0;hist=Counter()
        for ch in it.product(range(8),repeat=3):
            row,num,geom=case(ch,alias);cert['rows'].append(row);count+=num;hist[row['valid_original_assignments']]+=1
            if ch==(0,0,0):cert['geometry_examples'][str(alias)]=geom
        byalias.append({'alias_sector':alias,'direction_types':512,'verified_lifts':count,
                        'original_valid_count_histogram':dict(sorted(hist.items()))})
    cert['complete']=True;cert['charge_controls']=charges()
    raw=(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n').encode()
    arc={'format':'lzma-base64-json-v1','decoded_bytes':len(raw),'decoded_sha256':hashlib.sha256(raw).hexdigest(),
         'data':base64.b64encode(lzma.compress(raw,preset=6)).decode()}
    encoded=(json.dumps(arc,sort_keys=True,separators=(',',':'))+'\n').encode()
    need(lzma.decompress(base64.b64decode(arc['data']))==raw,'lossless archive check')
    output.with_name(output.name+'-certificate.json').write_bytes(encoded)
    summary={'verdict':'candidate_only','trusted_verifier_receipt':False,'complete':True,'runtime':platform.python_version(),
             'source_sha256':cert['source_sha256'],'alias_counts':dict(Counter(x['status'] for x in cert['alias_classification'])),
             'by_alias':byalias,'total_direction_types':len(cert['rows']),
             'total_verified_lifts':sum(x['verified_lifts'] for x in byalias),'seven_vertices_deleted_each':True,
             'all_rules_have_no_new_arcs_or_reverse_arc_guards':True,'certificate_bytes':len(encoded),
             'certificate_sha256':hashlib.sha256(encoded).hexdigest(),'decoded_bytes':len(raw),
             'decoded_sha256':arc['decoded_sha256'],'charges':cert['charge_controls']}
    output.with_name(output.name+'-summary.json').write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__': main()
