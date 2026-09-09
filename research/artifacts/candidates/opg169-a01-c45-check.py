#!/usr/bin/env python3
"""Generate C45's exact first-residual degree-four endpoint table.
Candidate-only research control; deterministic and network-free.
"""
from __future__ import annotations
import collections, itertools, json, platform

# Labels: 0=8, 1=12, 2=a, 3=b, 4=u, 5=z.
V=tuple(range(6))
B=(0,1,5,3)
U=4
A=2

BASE={
    (0,1),       # 8->12
    (0,4),(1,4), # 8,12 -> u
    (4,2),(4,3), # u -> a,b
    (2,1),       # a->12
    (3,2),(3,0), # b->a, b->8
    (2,5),       # a->z, forced by semidegree at degree-four a
}

def full_arcs(word:int, guard_failure:bool=False):
    arcs=set(BASE)
    arcs.add((1,5) if word&1 else (5,1))
    arcs.add((5,3) if word&2 else (3,5))
    if guard_failure:
        arcs.add((5,0))
    return arcs

def relation(vertices, arcs, boundary, color):
    vertices=set(vertices)
    adj={v:[] for v in vertices}
    indeg={v:0 for v in vertices}
    for x,y in arcs:
        if x in vertices and y in vertices and color[x]==color[y]:
            adj[x].append(y); indeg[y]+=1
    q=[v for v in vertices if indeg[v]==0]
    seen=0
    while q:
        x=q.pop(); seen+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    if seen!=len(vertices):
        return None
    out=set()
    for s in boundary:
        todo=list(adj[s]); reached=set()
        while todo:
            x=todo.pop()
            if x in reached:continue
            reached.add(x);todo.extend(adj[x])
        out.update((s,t) for t in boundary if t in reached)
    return tuple(sorted(out))

def test_rule(word, delete, adds, guard_failure=False):
    arcs=full_arcs(word,guard_failure)
    qv=tuple(v for v in V if v not in delete)
    qa={e for e in arcs if not (set(e)&set(delete))}
    for e in adds:
        if (e[1],e[0]) in qa:
            raise AssertionError("opposite arc in Q")
        qa.add(tuple(e))
    profiles=collections.defaultdict(list)
    for bits in range(1<<len(V)):
        col={v:(bits>>v)&1 for v in V}
        rp=relation(V,arcs,B,col)
        if rp is None:continue
        bw=sum(col[v]<<i for i,v in enumerate(B))
        profiles[bw].append((bits,rp))
    stats=collections.Counter(); lifts=[]; first=None
    for qb in range(1<<len(qv)):
        cq={v:(qb>>i)&1 for i,v in enumerate(qv)}
        rq=relation(qv,qa,B,cq)
        if rq is None:continue
        stats["valid"]+=1
        bw=sum(cq[v]<<i for i,v in enumerate(B))
        ordinary=profiles[bw]
        good=[x for x in ordinary if set(x[1])<=set(rq)]
        if not good:
            stats["fail"]+=1
            kind="ordinary_nonextension" if not ordinary else "relation_only"
            stats[kind]+=1
            if first is None:
                first={"q_bits":qb,"boundary_word":bw,"kind":kind,
                       "q_relation":[list(x) for x in rq]}
        else:
            chosen=next((x for x in good if x[1]==rq),good[0])
            stats["equal" if chosen[1]==rq else "strict"]+=1
            lifts.append({"q_bits":qb,"p_bits":chosen[0]})
    return {"delete":list(delete),"adds":[list(e) for e in adds],
            "valid_q":stats["valid"],"fail":stats["fail"],
            "ordinary_nonextension":stats["ordinary_nonextension"],
            "relation_only":stats["relation_only"],
            "equal":stats["equal"],"strict":stats["strict"],
            "first_failure":first,"lifts":lifts}

def main():
    rows=[]
    expected={
      0:([4],[(0,2)],None,(32,26,6)),
      1:([4],[(0,2)],None,(32,30,2)),
      2:([4,2],[(0,5)],[5,0],(12,10,2)),
      3:([4,2],[(0,5)],[5,0],(12,12,0)),
    }
    for word in range(4):
        delete,adds,guard,counts=expected[word]
        rule=test_rule(word,delete,adds)
        assert rule["fail"]==0
        assert (rule["valid_q"],rule["equal"],rule["strict"])==counts
        row={"word":word,
             "directions":{
               "12_z":"12->z" if word&1 else "z->12",
               "z_b":"z->b" if word&2 else "b->z"},
             "class":"unconditional" if guard is None else "conditional",
             "guard":guard,
             "rule":rule}
        if guard is not None:
            fallback=test_rule(word,[4],[(0,2)],guard_failure=True)
            assert fallback["fail"]==2 and fallback["ordinary_nonextension"]==2
            assert fallback["first_failure"]["boundary_word"]==2
            row["guard_failure_fallback"]=fallback
        rows.append(row)
    out={
      "format":"opg169-c45-first-residual-endpoint-d4-v1",
      "verdict":"candidate_only",
      "labels":{"0":8,"1":12,"2":"a","3":"b","4":"u","5":"z"},
      "boundary_order":[0,1,5,3],
      "fixed_arcs":[list(e) for e in sorted(BASE)],
      "faces":[[4,0,1],[4,1,2],[4,2,3],[4,3,0],[2,1,5],[2,5,3]],
      "coverage":{"unconditional":2,"conditional":2,"guard_failure_children":2},
      "selected_positive_lifts":sum(len(r["rule"]["lifts"]) for r in rows),
      "same_boundary_guard_failure_obstruction":{
        "boundary_word":2,
        "boundary_colors":{"8":0,"12":1,"z":0,"b":0},
        "actual_reverse_guard":[5,0],
        "argument":[
          "If a=0, a->z->b->a is a monochromatic directed triangle.",
          "If a=1 and u=1, 12->u->a->12 is monochromatic.",
          "If a=1 and u=0, u->b->8->u is monochromatic.",
          "Any same-boundary strict replacement has at most one internal vertex; color it 1. The color-0 boundary digraph z->b->8 plus z->8 is acyclic, and the color-1 class has at most {12,w}, hence is acyclic in a simple orientation. Thus the smaller coloring exists but P has no ordinary extension."
        ],
        "scope":"All simple oriented replacements inside the same four-vertex boundary that strictly reduce the two-internal-vertex patch; not replacements that release/identify a boundary vertex."
      },
      "rows":rows,
      "runtime":{"python":platform.python_version()},
      "scope":"The lexicographically first C44 residual wheel, with endpoint a of complete degree four and fourth neighbour z distinct from 8. Aliases of z to other exterior vertices are retained if all displayed arcs agree."
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
