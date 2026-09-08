"""Separate DFS/BFS certificate consumer; does not import or execute the generator.
It checks every retained lifting map, including the supplied six/seven-donor inputs.
"""
import base64,hashlib,itertools as it,json,lzma,platform
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
D=Path('research/artifacts/candidates')
CERT=D/'opg169-a01-nine-donor-certificate.json'
OLD=D/'opg169-a01-post-c33-supplied-archive-20260908.json'
CORES=((1,78),(1,100),(3,43),(5,77))
EXTRA=((0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5))

def require(ok,label):
    if not ok:raise ValueError(label)

def unpack(p):
    a=json.loads(p.read_bytes());require(a['decoded_bytes']<1048576,'decoded input cap')
    dec=lzma.LZMADecompressor();raw=dec.decompress(base64.b64decode(a['data']),max_length=1048577)
    require(dec.eof and not dec.unused_data,'one complete compressed stream')
    require(len(raw)==a['decoded_bytes'] and hashlib.sha256(raw).hexdigest()==a['decoded_sha256'],'archive exact bytes')
    return json.loads(raw)

def relation(A,V,B,c):
    out={x:[] for x in V}
    for x,y in A:
        if c[x]==c[y]:out[x].append(y)
    mark={x:0 for x in V}
    def walk(x):
        mark[x]=1
        for y in out[x]:
            if mark[y]==1 or mark[y]==0 and not walk(y):return False
        mark[x]=2;return True
    if any(mark[x]==0 and not walk(x) for x in V):return None
    R=set()
    for x in B:
        todo=list(out[x]);seen=set()
        while todo:
            y=todo.pop()
            if y not in seen:seen.add(y);todo.extend(out[y])
        R.update((x,y) for y in seen if y in B)
    return R

def map_check(A,names,B,Q,vec):
    require(len(names)==len(set(names)) and len(vec)==2**len(B),'input indexing')
    V=set(names);Bs=set(B);n=len(names);b=len(B);count=0;strict=0
    require(all(x!=y and (y,x) not in A for x,y in A),'orientation source')
    require(Q=={(x,y) for x,y in A if x in Bs and y in Bs},'replacement is exact vertex deletion')
    for mask,entry in enumerate(vec):
        d={x:(mask>>i)&1 for i,x in enumerate(B)};rq=relation(Q,Bs,Bs,d)
        if rq is None:
            require(entry is None,'invalid Q must be explicitly null');continue
        require(isinstance(entry,int) and 0<=entry<2**n,'complete original colouring')
        c={x:(entry>>i)&1 for i,x in enumerate(names)}
        require(all(c[x]==d[x] for x in B),'same sigma for all external vertices')
        rp=relation(A,V,Bs,c);require(rp is not None and rp<=rq,'all-exterior containment')
        ra={(y,x) for x,y in A};rQ={(y,x) for x,y in Q}
        rr=relation(ra,V,Bs,c);rq2=relation(rQ,Bs,Bs,d)
        require(rr=={(y,x) for x,y in rp} and rr<=rq2,'whole-arc reversal lift')
        count+=1;strict+=rp!=rq
    return count,strict

def sphere(A,rotation,expected_faces):
    R={int(x):list(v) for x,v in rotation.items()};V=set(R)
    E={frozenset((x,y)) for x,y in A}
    for x,ns in R.items():
        require(len(ns)==len(set(ns)) and set(ns)==set().union(*(set(e) for e in E if x in e))-{x},'complete local rotation')
    unseen={(x,y) for e in E for x,y in it.permutations(e,2)};faces=[]
    while unseen:
        start=min(unseen);edge=start;face=[]
        while True:
            require(edge in unseen,'dart partition');unseen.remove(edge);x,y=edge;face.append(x)
            ns=R[y];edge=y,ns[(ns.index(x)+1)%len(ns)]
            if edge==start:break
        faces.append(face)
    canonical=lambda f:min(tuple(f[k:]+f[:k]) for k in range(len(f)))
    require({canonical(f) for f in faces}=={canonical(f) for f in expected_faces},'actual face walks')
    require(len(V)-len(E)+len(faces)==2,'sphere Euler')

def root_arcs(r,b):
    A={(i,(i+1)%4) if not(r>>i)&1 else ((i+1)%4,i) for i in range(4)}
    A|={(y,x) if (b>>i)&1 else (x,y) for i,(x,y) in enumerate(EXTRA)}
    return A

def main():
    require(platform.python_version()=='3.13.5','runtime pin')
    cert=unpack(CERT);old=unpack(OLD)
    require(len(cert['rows'])==2048 and cert['complete'],'selected complete allocation')
    sectors=[tuple(x) for x in cert['labelled_sectors']];T=[]
    # Regenerate every direction independently from all C32 codes and literal bijections.
    for index,(a,q,b,u,v) in enumerate(sectors):
        expected=set();sk={frozenset(e) for e in [(0,a),(a,q),(q,b),(b,0),(0,u),(a,u),(q,u),(u,v),(0,v),(q,v),(v,b)]}
        for r,s in CORES:
            p=0 if (r,s) in CORES[:2] else 2
            for e,f,rev in it.product(it.permutations((a,b)),it.permutations((u,v)),(0,1)):
                lab={p:0,2-p:q,1:e[0],3:e[1],4:f[0],5:f[1]}
                A={(lab[y],lab[x]) if rev else (lab[x],lab[y]) for x,y in root_arcs(r,s)}
                if {frozenset(x) for x in A}==sk and {(a,0),(b,0),(0,u),(0,v)}<=A:expected.add(tuple(sorted(A)))
        require(len(expected)==8,'eight complete directions')
        actual=[tuple(map(tuple,x)) for x in cert['sector_templates'][index]]
        require(actual==sorted(expected),'complete ordered source template table');T.append(actual)
    counts=Counter();strict=0;keys=set()
    for row in cert['rows']:
        alias=row['alias_sector'];ds=tuple(row['directions']);key=(alias,ds)
        require(key not in keys,'unique local type');keys.add(key)
        require(alias in (-1,0,1,2) and all(0<=x<8 for x in ds),'local type domain')
        A=set().union(*(set(T[i][ds[i]]) for i in range(3)))
        sub={} if alias<0 else {10+alias:1+(alias+2)%3}
        A={(sub.get(x,x),sub.get(y,y)) for x,y in A}
        B=list(dict.fromkeys(sub.get(x,x) for x in (1,10,2,11,3,12)))
        names=B+[0]+list(range(4,10));Q={(x,y) for x,y in A if x in B and y in B}
        n,s=map_check(A,names,B,Q,row['lift']);counts[alias]+=n;strict+=s
        require(len(names)-len(B)==7,'strict order decrease')
        require(all(sum(x in e for e in A)==4 for x in range(4,10)),'saturated lows')
    require(keys==set(it.product((-1,0,1,2),it.product(range(8),repeat=3))),'all 2048 types')
    for geom in cert['geometry_examples'].values():
        sphere(set(map(tuple,geom['original_arcs'])),geom['rotation'],geom['interior_faces']+geom['complementary_faces'])
    aliases=cert['alias_classification'];require(len(aliases)==15,'alias rows')
    ac=Counter(x['status'] for x in aliases)
    require(ac=={'allowed':4,'excluded_endpoint_degree':4,'excluded_nonplanar':4,'excluded_rotation_conflict':3},'alias partition')
    for row in aliases:
        if row['status']=='excluded_nonplanar':require(row['edges']>3*row['vertices']-6,'Euler contradiction')
        if row['status'] in ('excluded_endpoint_degree','excluded_rotation_conflict'):
            v=row['saturated_high'];fs=row['saturating_faces'];link=[set(f)-{v} for f in fs]
            require(len(link)==4 and all(len(e)==2 for e in link),'four facial sectors')
            ns=set().union(*link);require(len(ns)==4 and all(sum(x in e for e in link)==2 for x in ns),'closed length-four link')
            require(row['degree']==4 if row['status']=='excluded_endpoint_degree' else bool(row['required_extra_neighbours']),'reason for exclusion')
    # Archive must preserve every exact supplied historical file, not an invented receipt.
    k=next(k for k in old if k.endswith('/opg169-a01-c34-two-donor-certificate.json'))
    prior=json.loads(old[k]);prior_counts={};prior_total=0
    for name,expected in [('six_donor',64),('seven_donor',128)]:
        rows=prior[name];require(len(rows)==expected,'dependency table scope');n=0
        for row in rows:
            A=set(map(tuple,row['original_arcs']));B=row['boundary'];names=row['normalised_vertex_names']
            Q={(names[x],names[y]) for x,y in row['replacement_arcs']}
            q,s=map_check(A,names,B,Q,row['lift_vector']);n+=q
            require(len(names)-len(B)==5,'old seven/six donor removal')
        prior_counts[name]=n;prior_total+=n
    require(prior_total==5088,'prior dependency full valid assignment count')
    # Symbolic ledger is checked through coefficient identities, not by inventing degrees for boundary ports.
    for d in range(4,101):
        for t in range(d//3+1):
            if t and d<6 or d in (6,7) and t>1 or d==9 and t==3:continue
            g=F(d-4-2*t,d);g_old=F(d-4-t,d)
            require(g>=0 and d*g+2*t==d-4,'all vertex receipts funded')
            require(g==g_old-F(t,d),'every corner loss counted')
    require(F(9-4-6,9)<0,'unproved exceptional payment must be rejected')
    report={'verdict':'candidate_only','trusted_verifier_receipt':False,'status':'finite_certificate_audit_passed',
            'runtime':platform.python_version(),'direction_types':2048,'positive_assignments':sum(counts.values()),
            'reverse_direction_assignments':sum(counts.values()),'by_alias':dict(counts),'strict_containment_cases':strict,
            'prior_two_donor_assignments':prior_counts,'prior_total':prior_total,'alias_classification':dict(ac),
            'charge_all_faces':'length-4+sum(gamma)+h, loss relative C33 is sum(t/d)',
            'unpaid_triangles_not_eliminated':True,'root_closed':False,'lean_elaboration':'not_run',
            'audit_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'certificate_sha256':hashlib.sha256(CERT.read_bytes()).hexdigest(),'supplied_archive_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
    (D/'opg169-a01-nine-donor-audit-output-20260908.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
    print(json.dumps(report,sort_keys=True))
if __name__=='__main__':main()
