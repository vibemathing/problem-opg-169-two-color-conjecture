#!/usr/bin/env python3
"""
S02-B bounded adversarial checker for the C37 high-port edge-split family.

This is a same-principal dual-implementation research checker, not an
independent verifier receipt.

Source binding:
  repository: vibemathing/problem-opg-169-two-color-conjecture
  fresh main at analysis start: 2d9303e7ae9558d3904bb2fa0bade246ebe9bbde
  C37 input git blob: a452f67995e1b563e364382593b887bf0ec1f63d
  C37 exact scope: d(7)=6 only; the n>=1 graphs below are new S02-B constructions.

Family G_n:
  start from the frozen whole C37 D,w3 triangulation;
  delete 12->13;
  insert z_1,...,z_n with
       12 -> z_1 -> ... -> z_n -> 13,
  and for each z_i choose one of two spoke signs:
       bit 1: 7 -> z_i -> 5
       bit 0: 5 -> z_i -> 7.
  The embedding is the repeated edge split of the terminal edge in the two
  actual faces with third vertices 7 and 5.

For every spoke word, all z_i have degree 4 and semidegrees (2,2).
The full graph remains a simple plane triangulation, and old vertices retain
their previously valid semidegrees.

Profile boundary:
  B=(A,B,L,R)=(7,5,12,13).
The checker cross-checks acyclicity/reachability with:
  oracle A: Kahn topological deletion + DFS reachability;
  oracle B: Floyd-Warshall transitive closure.

It tests:
  * structural invariants for the all-1 family through --structural-max;
  * the all-1 profile family through --profile-max;
  * every 0/1 spoke word through --word-max;
  * whether a longer patch strongly lifts every valid coloring of some
    shorter prefix patch with R_long subseteq R_short.
"""

from __future__ import annotations
import argparse, hashlib, itertools, json, sys
from collections import defaultdict, deque

BASE_ARCS = [
    (0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),
    (4,5),(4,8),(5,0),(5,6),(5,12),(5,13),(6,0),(6,13),
    (7,2),(7,8),(7,12),(8,3),(8,5),(11,6),(11,7),
    (12,8),(12,13),(13,7),(13,11)
]
BASE_ROT = {
    0:[2,6,5,4,3],
    2:[0,3,7,11,6],
    3:[0,4,8,7,2],
    4:[0,5,8,3],
    5:[0,6,13,12,8,4],
    6:[0,2,11,13,5],
    7:[2,3,8,12,13,11],
    8:[3,4,5,12,7],
    11:[2,7,13,6],
    12:[5,13,7,8],
    13:[5,6,11,7,12],
}
BOUNDARY = (7,5,12,13)

def zname(i: int) -> int:
    return 1000 + i

def build_full(word):
    """Full source-valid triangulation for a spoke word (path always 12 -> ... -> 13)."""
    n = len(word)
    zs = [zname(i) for i in range(1,n+1)]
    arcs = [e for e in BASE_ARCS if e != (12,13)]
    if n == 0:
        arcs.append((12,13))
    else:
        chain = [12] + zs + [13]
        arcs.extend(zip(chain, chain[1:]))
        for z,bit in zip(zs,word):
            if bit:
                arcs += [(7,z),(z,5)]
            else:
                arcs += [(5,z),(z,7)]

    rot = {v:list(ns) for v,ns in BASE_ROT.items()}
    if n:
        rot[7] = [2,3,8,12] + zs + [13,11]
        rot[5] = [0,6,13] + list(reversed(zs)) + [12,8,4]
        rot[12] = [5,zs[0],7,8]
        rot[13] = [5,6,11,7,zs[-1]]
        for i,z in enumerate(zs):
            prev = 12 if i == 0 else zs[i-1]
            nxt = 13 if i == n-1 else zs[i+1]
            rot[z] = [7,prev,5,nxt]
    return zs, list(arcs), rot

def trace_faces(rot):
    darts = {(u,v) for u,ns in rot.items() for v in ns}
    faces = []
    while darts:
        start = next(iter(darts))
        d = start
        face = []
        while True:
            if d not in darts:
                raise AssertionError(("dart-repeat", start, d, face))
            darts.remove(d)
            u,v = d
            face.append(u)
            ns = rot[v]
            try:
                i = ns.index(u)
            except ValueError:
                raise AssertionError(("asymmetric-rotation",u,v))
            w = ns[(i+1) % len(ns)]
            d = (v,w)
            if d == start:
                break
        faces.append(tuple(face))
    return faces

def structural_check(word):
    n = len(word)
    zs, arcs, rot = build_full(word)
    V = set(rot)
    assert len(V) == 11+n
    assert len(arcs) == 27+3*n
    assert len(set(arcs)) == len(arcs)
    assert all(a != b for a,b in arcs)
    U = {tuple(sorted((a,b))) for a,b in arcs}
    assert len(U) == len(arcs), "opposite arcs/digons"
    RU = {tuple(sorted((u,v))) for u,ns in rot.items() for v in ns}
    assert U == RU
    assert all(u in rot[v] for v,ns in rot.items() for u in ns)

    indeg = {v:0 for v in V}
    outdeg = {v:0 for v in V}
    for a,b in arcs:
        outdeg[a] += 1
        indeg[b] += 1
    assert min(indeg.values()) >= 2
    assert min(outdeg.values()) >= 2
    assert len(rot[7]) == 6+n
    for z in zs:
        assert len(rot[z]) == 4
        assert (indeg[z],outdeg[z]) == (2,2)

    faces = trace_faces(rot)
    assert all(len(f) == 3 for f in faces)
    assert len(faces) == 18+2*n
    assert len(V) - len(U) + len(faces) == 2
    assert len(U) == 3*len(V)-6

    return {
        "n":n, "vertices":len(V), "edges":len(U), "faces":len(faces),
        "d7":len(rot[7]), "min_indegree":min(indeg.values()),
        "min_outdegree":min(outdeg.values())
    }

def transition_check(word):
    """Check exact edge-split delta from word to word+(bit,) for each bit."""
    n = len(word)
    if n == 0:
        terminal = 12
    else:
        terminal = zname(n)
    _, A, _ = build_full(word)
    old = set(A)
    for bit in (0,1):
        nw = word + (bit,)
        z = zname(n+1)
        _, B, _ = build_full(nw)
        new = set(B)
        removed = old - new
        added = new - old
        assert removed == {(terminal,13)}
        expect = {(terminal,z),(z,13)}
        expect |= {(7,z),(z,5)} if bit else {(5,z),(z,7)}
        assert added == expect
        structural_check(nw)
    return True

def patch(word):
    n = len(word)
    zs = [zname(i) for i in range(1,n+1)]
    V = list(BOUNDARY) + zs
    A = [(7,12),(5,12),(5,13),(13,7)]
    if n == 0:
        A.append((12,13))
    else:
        chain=[12]+zs+[13]
        A.extend(zip(chain,chain[1:]))
        for z,bit in zip(zs,word):
            if bit:
                A += [(7,z),(z,5)]
            else:
                A += [(5,z),(z,7)]
    return V,A

def kahn_acyclic(V,A,C,color):
    S = {v for v in V if C[v] == color}
    indeg = {v:0 for v in S}
    adj = {v:[] for v in S}
    for a,b in A:
        if a in S and b in S:
            adj[a].append(b)
            indeg[b] += 1
    q = [v for v in S if indeg[v] == 0]
    seen = 0
    while q:
        v = q.pop()
        seen += 1
        for w in adj[v]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    return seen == len(S)

def dfs_reach(V,A,C,color):
    S={v for v in V if C[v] == color}
    adj={v:[] for v in S}
    for a,b in A:
        if a in S and b in S:
            adj[a].append(b)
    rel=set()
    for s in BOUNDARY:
        if s not in S:
            continue
        stack=list(adj[s])
        seen=set()
        while stack:
            v=stack.pop()
            if v in seen:
                continue
            seen.add(v)
            if v in BOUNDARY:
                rel.add((s,v))
            stack.extend(adj.get(v,()))
    return frozenset(rel)

def warshall(V,A,C,color):
    S=[v for v in V if C[v] == color]
    idx={v:i for i,v in enumerate(S)}
    n=len(S)
    M=[[False]*n for _ in range(n)]
    for a,b in A:
        if a in idx and b in idx:
            M[idx[a]][idx[b]]=True
    for k in range(n):
        for i in range(n):
            if M[i][k]:
                rowi=M[i]
                rowk=M[k]
                for j in range(n):
                    if rowk[j]:
                        rowi[j]=True
    acyclic=all(not M[i][i] for i in range(n))
    rel=frozenset(
        (a,b) for a in BOUNDARY if a in idx
              for b in BOUNDARY if b in idx and a != b
              if M[idx[a]][idx[b]]
    )
    return acyclic, rel

def enumerate_states(word, oracle):
    V,A=patch(word)
    out=[]
    for bits in itertools.product((0,1), repeat=len(V)):
        C=dict(zip(V,bits))
        if oracle == "A":
            ac=[kahn_acyclic(V,A,C,c) for c in (0,1)]
            if not all(ac):
                continue
            rel=(dfs_reach(V,A,C,0),dfs_reach(V,A,C,1))
        elif oracle == "B":
            x0=warshall(V,A,C,0)
            x1=warshall(V,A,C,1)
            if not (x0[0] and x1[0]):
                continue
            rel=(x0[1],x1[1])
        else:
            raise ValueError(oracle)
        bc=tuple(C[b] for b in BOUNDARY)
        out.append((bc,rel,bits))
    return out

CACHE={}
def states(word):
    word=tuple(word)
    if word not in CACHE:
        A=enumerate_states(word,"A")
        B=enumerate_states(word,"B")
        sigA={(bc,r,bits) for bc,r,bits in A}
        sigB={(bc,r,bits) for bc,r,bits in B}
        assert sigA == sigB, ("oracle-disagreement",word)
        CACHE[word]=A
    return CACHE[word]

def strong_lift(Pword,Qword):
    """Every valid complete Q coloring has a P coloring with same boundary and R_P subseteq R_Q."""
    P=states(tuple(Pword))
    Q=states(tuple(Qword))
    by=defaultdict(list)
    for bc,r,bits in P:
        by[bc].append((r,bits))
    failures=[]
    for bc,rq,bitsq in Q:
        ok=False
        for rp,bitsp in by.get(bc,()):
            if rp[0].issubset(rq[0]) and rp[1].issubset(rq[1]):
                ok=True
                break
        if not ok:
            failures.append({
                "boundary":"".join(map(str,bc)),
                "q_bits":"".join(map(str,bitsq)),
            })
    return not failures, failures

def profile_signature(word):
    # Full realized relation sets, not minimized.
    by=defaultdict(set)
    for bc,r,bits in states(tuple(word)):
        by[bc].add((tuple(sorted(r[0])),tuple(sorted(r[1]))))
    return tuple(
        (bc,tuple(sorted(rs)))
        for bc,rs in sorted(by.items())
    )

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--structural-max",type=int,default=64)
    ap.add_argument("--profile-max",type=int,default=12)
    ap.add_argument("--word-max",type=int,default=8)
    args=ap.parse_args()

    # Exact structural family, all-1 spokes.
    structural=[]
    for n in range(1,args.structural_max+1):
        word=(1,)*n
        structural.append(structural_check(word))
        transition_check(word)

    # Natural all-1 profile pump.
    natural=[]
    q0=()
    for n in range(1,args.profile_max+1):
        word=(1,)*n
        ok,fail=strong_lift(word,q0)
        natural.append({
            "n":n,
            "d7":6+n,
            "valid_colourings":len(states(word)),
            "lifts_P0":ok,
            "fail_boundary_words":sorted({x["boundary"] for x in fail}),
            "full_profile_sha256":hashlib.sha256(repr(profile_signature(word)).encode()).hexdigest(),
        })

    assert natural[0]["lifts_P0"] is False
    assert natural[0]["fail_boundary_words"] == ["0110","1001"]
    assert all(r["lifts_P0"] for r in natural[1:])

    # Exhaust all source-valid forward-path spoke words.
    word_rows=[]
    irreducible_by_n={}
    p0_fail_by_n={}
    for n in range(1,args.word_max+1):
        irreduc=[]
        p0fail=[]
        for word in itertools.product((0,1),repeat=n):
            structural_check(word)
            ok0,_=strong_lift(word,())
            if not ok0:
                p0fail.append("".join(map(str,word)))
            reduced=None
            for m in range(0,n):
                if strong_lift(word,word[:m])[0]:
                    reduced=m
                    break
            if reduced is None:
                irreduc.append("".join(map(str,word)))
            word_rows.append({
                "word":"".join(map(str,word)),
                "n":n,
                "lifts_P0":ok0,
                "shortest_prefix_replacement":reduced,
                "valid_colourings":len(states(word)),
                "profile_sha256":hashlib.sha256(repr(profile_signature(word)).encode()).hexdigest(),
            })
        irreducible_by_n[str(n)]=irreduc
        p0_fail_by_n[str(n)]=p0fail

    assert irreducible_by_n["1"] == ["1"]
    for n in range(2,args.word_max+1):
        assert irreducible_by_n[str(n)] == []

    # Exact repeat -> compression sanity: if two prefix profiles are equal,
    # later strongly lifts earlier.
    repeat_checks=0
    for n in range(1,args.word_max+1):
        for word in itertools.product((0,1),repeat=n):
            sigs={}
            for m in range(n+1):
                sig=profile_signature(word[:m])
                if sig in sigs:
                    i=sigs[sig]
                    assert strong_lift(word[:m],word[:i])[0]
                    repeat_checks += 1
                else:
                    sigs[sig]=m

    out={
        "format":"opg169-s02b-high-port-pump-check-v1",
        "verdict":"candidate_only",
        "root_closed":False,
        "trust_boundary":"same-principal dual-implementation bounded checker; not an independent verifier receipt",
        "source":{
            "repository":"vibemathing/problem-opg-169-two-color-conjecture",
            "fresh_main_at_analysis_start":"2d9303e7ae9558d3904bb2fa0bade246ebe9bbde",
            "c37_input_git_blob":"a452f67995e1b563e364382593b887bf0ec1f63d",
        },
        "scope":{
            "structural_all1_n":"1..%d"%args.structural_max,
            "natural_profile_all1_n":"1..%d"%args.profile_max,
            "all_spoke_words_n":"1..%d"%args.word_max,
            "path_orientation":"12 -> z1 -> ... -> zn -> 13",
            "spoke_bit_1":"7 -> zi -> 5",
            "spoke_bit_0":"5 -> zi -> 7",
            "boundary":[7,5,12,13],
        },
        "structural_last":structural[-1],
        "natural_profile":natural,
        "all_words":{
            "rows":len(word_rows),
            "irreducible_by_n":irreducible_by_n,
            "p0_fail_by_n":p0_fail_by_n,
            "repeat_profile_compression_checks":repeat_checks,
        },
        "key_findings":{
            "unbounded_source_family":True,
            "degree_formula":"d(7)=6+n",
            "size_formula":"|V|=11+n, |E|=27+3n, |F|=18+2n",
            "all_new_vertices":"degree 4; indegree=outdegree=2",
            "natural_n1_P0_failure_boundary_words":["0110","1001"],
            "natural_n_ge_2_P0_lift_checked":True,
            "all_spoke_words_n_ge_2_have_shorter_prefix_replacement_through_bound":True,
        },
        "nonclaims":[
            "No finite word bound proves global high-port termination.",
            "No C37 d(7)>=7 classification is imported from the d(7)=6 table.",
            "No C45 high-degree or AE/M12 shell/cap claim is used.",
            "The checker does not handle growing interfaces, arbitrary exterior contacts at every fan port, or all separator geometries.",
            "Dual implementations share one generator trust domain."
        ],
        "python":sys.version.split()[0],
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__ == "__main__":
    main()
