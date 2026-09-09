#!/usr/bin/env python3
"""Independent DFS/BFS consumer for C44's frozen table.
Does not import generator code. Candidate-only.
"""
from __future__ import annotations
import collections,json,sys

B=(0,1,2,3); C=4

def graph(sm,rw):
    A={(0,1)}
    A.add((1,2) if rw&1 else (2,1))
    A.add((2,3) if rw&2 else (3,2))
    A.add((3,0) if rw&4 else (0,3))
    for x in B:A.add((x,C) if sm>>x&1 else (C,x))
    return A

def valid_and_relation(V,A,col):
    adj={v:[] for v in V}
    for x,y in A:
        if col[x]==col[y]:adj[x].append(y)
    state={v:0 for v in V}
    def dfs(x):
        state[x]=1
        for y in adj[x]:
            if state[y]==1:return False
            if state[y]==0 and not dfs(y):return False
        state[x]=2;return True
    for x in V:
        if state[x]==0 and not dfs(x):return None
    out=set()
    for s in B:
        q=collections.deque(adj[s]);seen=set()
        while q:
            x=q.popleft()
            if x in seen:continue
            seen.add(x);q.extend(adj[x])
        out.update((s,t) for t in B if t in seen)
    return out

def all_p(A,bw):
    vals=[]
    for cc in (0,1):
        col={x:(bw>>x)&1 for x in B};col[C]=cc
        r=valid_and_relation(set(B)|{C},A,col)
        if r is not None:vals.append((cc,r))
    return vals

def audit(path):
    d=json.load(open(path,encoding='utf-8'))
    assert d['format']=='opg169-c44-guard-face-degree4-catalog-v1'
    cc=collections.Counter(); tri=collections.Counter(); total_lifts=0
    seen=set()
    for row in d['rows']:
        sm=row['spoke_in_mask'];rw=row['rim_word'];key=(sm,rw)
        assert key not in seen;seen.add(key);assert sm.bit_count()==2 and 0<=rw<8
        A=graph(sm,rw); z=row['selected']; add=None if z['add'] is None else tuple(z['add'])
        QA={e for e in A if C not in e}
        if add is not None:
            assert (add[1],add[0]) not in QA
            QA.add(add)
            assert z['guard']==[add[1],add[0]]
        else:assert z['guard'] is None
        stats=collections.Counter(); expected_lifts={x['boundary_word']:x['center_color'] for x in z['lifts']}
        for bw in range(16):
            qcol={x:(bw>>x)&1 for x in B}
            rq=valid_and_relation(set(B),QA,qcol)
            if rq is None:continue
            stats['valid']+=1
            ps=all_p(A,bw);good=[(c,r) for c,r in ps if r<=rq]
            if not good:
                stats['fail']+=1
                stats['ordinary' if not ps else 'relation']+=1
            else:
                assert bw in expected_lifts
                cc0=expected_lifts[bw]
                match=[r for c,r in good if c==cc0]
                assert match
                stats['equal' if match[0]==rq else 'strict']+=1
        assert stats['valid']==z['valid_q'];assert stats['fail']==z['fail']
        assert stats['equal']==z['equal'];assert stats['strict']==z['strict']
        assert stats['ordinary']==z['ordinary_nonextension'];assert stats['relation']==z['relation_only']
        cls=row['class'];cc[cls]+=1
        if cls!='residual':assert z['fail']==0;total_lifts+=len(z['lifts'])
        else:assert z['fail']>0
        k=0
        for i in range(4):
            x,y=B[i],B[(i+1)%4]
            if ((C,x) in A and (x,y) in A and (y,C) in A) or ((x,C) in A and (C,y) in A and (y,x) in A):k+=1
        assert k==row['directed_incident_triangles']
        if cls=='residual':tri[k]+=1
    assert len(seen)==48
    assert dict(cc)=={'unconditional':9,'conditional':24,'residual':15}
    assert dict(tri)=={2:10,3:4,4:1}
    assert total_lifts==d['selected_positive_lift_entries']==496
    return {'format':'opg169-c44-guard-face-degree4-audit-v1','status':'ok','rows':48,
            'coverage':dict(cc),'residual_directed_triangle_distribution':{str(k):v for k,v in sorted(tri.items())},
            'selected_positive_lift_entries':total_lifts,
            'mirror_scope':'The generic wheel theorem applies to either incident side of edge 8->12 by boundary relabeling; no parent count is changed.'}
if __name__=='__main__':print(json.dumps(audit(sys.argv[1]),sort_keys=True,separators=(',',':')))
