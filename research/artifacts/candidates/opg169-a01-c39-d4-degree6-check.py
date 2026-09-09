import itertools, collections, json, hashlib, sys

BASE_ARCS={(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),(4,5),(4,8),
(5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7),
(11,12),(13,12),(13,8),(12,7),(7,13)}
BASE_TRIS=[(0,2,3),(0,6,2),(0,5,6),(0,4,5),(0,3,4),
(2,7,3),(2,11,7),(2,6,11),(3,8,4),(3,7,8),
(8,7,13),(13,7,12),(12,7,11)]
OLD=[6,11,12,13]

def successors(tris):
    s={}
    for a,b,c in tris:
        for v,x,y in ((b,a,c),(c,b,a),(a,c,b)):
            row=s.setdefault(v,{})
            if x in row and row[x]!=y:return None
            row[x]=y
    return s

def closed_links(tris):
    s=successors(tris)
    if s is None:return None
    ans={}
    for v,row in s.items():
        ns=set(row)|set(row.values())
        indeg=collections.Counter(row.values())
        closed=set(row)==ns and all(indeg[n]==1 for n in ns)
        if closed:ans[v]=len(ns)
    return ans

def make_arcs(qk,rk,w):
    q=14 if qk=='new' else qk; r=15 if rk=='new' else rk
    A=set(BASE_ARCS)
    es=[(5,q),(q,4),
        (q,r) if w&1 else (r,q),
        (r,8) if w&2 else (8,r),
        (r,4) if w&4 else (4,r)]
    for e in es:
        if e[0]==e[1] or (e[1],e[0]) in A:return None
        A.add(e)
    return A

def compress(A,V,B):
    vs=sorted(V); p={v:i for i,v in enumerate(vs)}
    return vs,p,[(p[u],p[v]) for u,v in A if u in p and v in p],[p[b] for b in B]

def rel(edges,n,bpos,bits):
    R=[0]*n
    for u,v in edges:
        if ((bits>>u)&1)==((bits>>v)&1):R[u]|=1<<v
    for k in range(n):
        z=1<<k; rk=R[k]
        for i in range(n):
            if R[i]&z:R[i]|=rk
    if any(R[i]>>i&1 for i in range(n)):return None
    out=0; m=len(bpos)
    for i,u in enumerate(bpos):
        for j,v in enumerate(bpos):
            if R[u]>>v&1:out|=1<<(i*m+j)
    return out

def test_delete(A,V,I,dv):
    B=sorted(V-I)
    pvs,pp,ped,pbp=compress(A,V,B)
    P=collections.defaultdict(list)
    for z in range(1<<len(pvs)):
        rr=rel(ped,len(pvs),pbp,z)
        if rr is None:continue
        b=0
        for i,v in enumerate(B):
            if z>>pp[v]&1:b|=1<<i
        P[b].append(rr)
    QV=V-{dv}; QA={e for e in A if dv not in e}
    qvs,qp,qed,qbp=compress(QA,QV,B)
    valid=fail=equal=strict=ordinary=relation_only=0
    first_failure=None
    for z in range(1<<len(qvs)):
        rq=rel(qed,len(qvs),qbp,z)
        if rq is None:continue
        valid+=1;b=0
        for i,v in enumerate(B):
            if z>>qp[v]&1:b|=1<<i
        opts=[rp for rp in P[b] if rp & ~rq == 0]
        if not opts:
            fail+=1
            if not P[b]: ordinary+=1; kind='ordinary_nonextension'
            else: relation_only+=1; kind='relation_only'
            if first_failure is None:first_failure=[z,b,kind]
        elif rq in opts:equal+=1
        else:strict+=1
    return [valid,fail,equal,strict,ordinary,relation_only,first_failure]

def main():
    aliases=[]; excluded=[]
    kinds=OLD+['new']
    for qk in kinds:
        for rk in kinds:
            if qk!='new' and rk!='new' and qk==rk:continue
            q=14 if qk=='new' else qk; r=15 if rk=='new' else rk
            tris=BASE_TRIS+[(5,4,q),(q,4,r),(r,4,8)]
            links=closed_links(tris)
            if links is None:
                excluded.append([qk,rk,'rotation_conflict']);continue
            if any(d<4 for d in links.values()):
                excluded.append([qk,rk,'closed_link_degree_lt4',links]);continue
            V={0,2,3,4,5,6,7,8,11,12,13,q,r}
            E={frozenset(e) for e in BASE_ARCS}
            for e in [(5,q),(q,4),(q,r),(r,8),(r,4)]:E.add(frozenset(e))
            if len(E)>3*len(V)-6:
                excluded.append([qk,rk,'planar_edge_bound',len(V),len(E)]);continue
            aliases.append([qk,rk])
    assert len(aliases)==11 and len(excluded)==10
    rows=[]; positive=[]; matrix=collections.Counter()
    for qk,rk in aliases:
        q=14 if qk=='new' else qk; r=15 if rk=='new' else rk
        V={0,2,3,4,5,6,7,8,11,12,13,q,r}; I={0,2,3,4,7}
        for w in range(8):
            A=make_arcs(qk,rk,w)
            if A is None:continue
            ds={str(v):test_delete(A,V,I,v) for v in sorted(I)}
            goods=[int(v) for v,x in ds.items() if x[1]==0]
            if goods:cat='strong_profile'
            elif any(x[4]==0 for x in ds.values()):cat='ordinary_only'
            else:cat='ordinary_failure'
            matrix[cat]+=1
            row={'q':qk,'r':rk,'word':w,'delete':ds,'good_deletions':goods,'class':cat}
            rows.append(row)
            if goods:positive.append(row)
    assert len(rows)==70 and len(positive)==6
    assert dict(matrix)=={'strong_profile':6,'ordinary_only':48,'ordinary_failure':16}
    keys=[(x['q'],x['r'],x['word']) for x in positive]
    assert keys==[(11,12,1),(11,13,3),('new',6,4),('new',6,5),('new',6,6),('new',6,7)]
    first=next(x for x in rows if (x['q'],x['r'],x['word'])==(11,12,3))
    assert all(v[4]==0 and v[5]>0 for v in first['delete'].values())
    out={'format':'opg169-c39-d4-degree6-v1','verdict':'candidate_only',
         'alias_initial':21,'alias_excluded':excluded,'alias_surviving':aliases,
         'compatible_direction_types':len(rows),'coverage_matrix':dict(matrix),
         'positive_types':len(positive),'positive_rows':positive,
         'first_open_profile_type':first,
         'bit_semantics':['bit0:q->r else r->q','bit1:r->8 else 8->r','bit2:r->4 else 4->r'],
         'fixed_arcs':['5->q','q->4'],
         'scope':'D19 with d(4)=6 and fixed facial triangle 4->5->q->4; only single controlled-vertex induced deletions among {0,2,3,4,7}. No completeness beyond this replacement family.'}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
