#!/usr/bin/env python3
"""Generate the exact degree-four guard-face wheel profile catalogue.
Candidate-only research control; no external network or randomness.
"""
from __future__ import annotations
import collections, hashlib, itertools, json, platform

B=(0,1,2,3)  # source labels: 0=8, 1=12, 2=a, 3=b
C=4
RIM_PAIRS=((0,1),(1,2),(2,3),(3,0))
DIAGONALS=(None,(0,2),(2,0),(1,3),(3,1))

def acyclic_relation(vertices, arcs, boundary, color):
    V=set(vertices); adj={v:[] for v in V}; indeg={v:0 for v in V}
    for u,v in arcs:
        if color[u]==color[v]: adj[u].append(v); indeg[v]+=1
    q=[v for v in V if indeg[v]==0]; seen=0
    while q:
        x=q.pop(); seen+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    if seen!=len(V): return None
    rel=[]
    for s in boundary:
        todo=list(adj[s]); reached=set()
        while todo:
            z=todo.pop()
            if z in reached: continue
            reached.add(z); todo.extend(adj[z])
        rel.extend((s,t) for t in boundary if t in reached)
    return tuple(sorted(rel))

def p_arcs(spoke_in, rim_word):
    arcs={(0,1)}
    arcs.add((1,2) if rim_word&1 else (2,1))
    arcs.add((2,3) if rim_word&2 else (3,2))
    arcs.add((3,0) if rim_word&4 else (0,3))
    arcs.update((x,C) if x in spoke_in else (C,x) for x in B)
    return arcs

def triangle_directed(arcs, x, y):
    return int(((C,x) in arcs and (x,y) in arcs and (y,C) in arcs) or
               ((x,C) in arcs and (C,y) in arcs and (y,x) in arcs))

def test_candidate(arcs, add):
    q_arcs={e for e in arcs if C not in e}
    if add is not None:
        if (add[1],add[0]) in q_arcs: return None
        q_arcs.add(add)
    p_by_boundary=collections.defaultdict(list)
    for bw in range(16):
        bc={v:(bw>>v)&1 for v in B}
        for cc in (0,1):
            col=dict(bc); col[C]=cc
            rp=acyclic_relation(B+(C,),arcs,B,col)
            if rp is not None: p_by_boundary[bw].append((cc,rp))
    valid=fail=equal=strict=ordinary=relation_only=0; lifts=[]; first=None
    for bw in range(16):
        col={v:(bw>>v)&1 for v in B}
        rq=acyclic_relation(B,q_arcs,B,col)
        if rq is None: continue
        valid+=1
        ordinary_opts=p_by_boundary[bw]
        good=[(cc,rp) for cc,rp in ordinary_opts if set(rp)<=set(rq)]
        if not good:
            fail+=1
            kind='ordinary_nonextension' if not ordinary_opts else 'relation_only'
            if kind=='ordinary_nonextension': ordinary+=1
            else: relation_only+=1
            if first is None: first={'boundary_word':bw,'kind':kind,
              'q_relation':[list(x) for x in rq],
              'p_relations':[{'center_color':cc,'relation':[list(x) for x in rp]} for cc,rp in ordinary_opts]}
        else:
            chosen=next((z for z in good if z[1]==rq),good[0])
            lifts.append({'boundary_word':bw,'center_color':chosen[0]})
            if chosen[1]==rq: equal+=1
            else: strict+=1
    return {'add':None if add is None else list(add),'guard':None if add is None else [add[1],add[0]],
            'valid_q':valid,'fail':fail,'equal':equal,'strict':strict,
            'ordinary_nonextension':ordinary,'relation_only':relation_only,
            'first_failure':first,'lifts':lifts}

def main():
    rows=[]; counts=collections.Counter(); selected_lifts=0; residual_triangles=collections.Counter()
    for spoke_in in itertools.combinations(B,2):
        sm=sum(1<<x for x in spoke_in)
        for rw in range(8):
            arcs=p_arcs(set(spoke_in),rw)
            candidates=[]
            for add in DIAGONALS:
                z=test_candidate(arcs,add)
                if z is not None: candidates.append(z)
            successes=[z for z in candidates if z['fail']==0]
            if any(z['add'] is None for z in successes):
                cls='unconditional'; selected=next(z for z in successes if z['add'] is None)
            elif successes:
                cls='conditional'; selected=successes[0]
            else:
                cls='residual'; selected=min(candidates,key=lambda z:(z['fail'],z['ordinary_nonextension'],z['relation_only'],str(z['add'])))
            counts[cls]+=1
            tri_count=sum(triangle_directed(arcs,B[i],B[(i+1)%4]) for i in range(4))
            if cls=='residual': residual_triangles[tri_count]+=1
            if cls!='residual': selected_lifts+=len(selected['lifts'])
            rows.append({'spoke_in_mask':sm,'rim_word':rw,'class':cls,
                         'directed_incident_triangles':tri_count,
                         'selected':selected,
                         'candidate_summaries':[{k:v for k,v in z.items() if k not in ('lifts','first_failure')} for z in candidates]})
    assert len(rows)==48
    assert dict(counts)=={'unconditional':9,'conditional':24,'residual':15}
    assert dict(residual_triangles)=={2:10,3:4,4:1}
    out={'format':'opg169-c44-guard-face-degree4-catalog-v1','verdict':'candidate_only',
         'source_labels':{'0':8,'1':12,'2':'a','3':'b','4':'u'},
         'fixed_edge':[0,1],
         'spoke_semantics':'spoke_in_mask bit i means boundary i -> center u; exactly two bits are set',
         'rim_semantics':['8->12 fixed','rim bit0:12->a else a->12','rim bit1:a->b else b->a','rim bit2:b->8 else 8->b'],
         'replacement_catalog':['delete u','optionally add exactly one oriented diagonal 8-a or 12-b in the actual quadrilateral hole'],
         'coverage':dict(counts),'residual_directed_triangle_distribution':{str(k):v for k,v in sorted(residual_triangles.items())},
         'selected_positive_lift_entries':selected_lifts,'rows':rows,
         'runtime':{'python':platform.python_version()},
         'scope':'One saturated degree-four third vertex on a triangular face of the fixed oriented edge 8->12. Boundary neighbours are distinct; arbitrary exterior arcs are retained. Conditional rules require absence of the recorded reverse guard.'}
    text=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    print(text,end='')
if __name__=='__main__':main()
