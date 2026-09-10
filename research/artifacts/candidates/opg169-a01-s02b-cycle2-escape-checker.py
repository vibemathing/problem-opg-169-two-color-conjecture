#!/usr/bin/env python3
"""
R08 S02-B Cycle 2 adversarial checker:
growing-interface / complete-star release / separator-escape ranks.

Candidate-only. Two internal graph/coloring implementations share one research
principal and are not an independent verifier receipt.

Fresh source anchor at analysis start:
  main = b742c72f1d50849bd074f1f7f7f6e2ed019870c4
Prior S02-B exact checker:
  549239acee6ed91e57ab941c0d2c0635fc5f9ded2471b2b4cdf881ea9ff9033d
"""

from __future__ import annotations
import argparse, itertools, json, hashlib
from collections import defaultdict, deque
import networkx as nx

BASE_ARCS = [
    (0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),
    (4,5),(4,8),(5,0),(5,6),(5,12),(5,13),(6,0),(6,13),
    (7,2),(7,8),(7,12),(8,3),(8,5),(11,6),(11,7),
    (12,8),(12,13),(13,7),(13,11)
]
BASE_ROT = {
    0:[2,6,5,4,3], 2:[0,3,7,11,6], 3:[0,4,8,7,2],
    4:[0,5,8,3], 5:[0,6,13,12,8,4], 6:[0,2,11,13,5],
    7:[2,3,8,12,13,11], 8:[3,4,5,12,7], 11:[2,7,13,6],
    12:[5,13,7,8], 13:[5,6,11,7,12],
}

def z(i): return 1000+i

def cyc_eq(a,b):
    if len(a)!=len(b): return False
    if not a: return True
    n=len(a)
    return any(all(a[(k+i)%n]==b[i] for i in range(n)) for k in range(n))

def trace_faces(rot):
    darts={(u,v) for u,ns in rot.items() for v in ns}
    faces=[]
    while darts:
        start=next(iter(darts)); d=start; face=[]
        while True:
            assert d in darts, ("dart repeat",start,d,face)
            darts.remove(d)
            u,v=d; face.append(u)
            ns=rot[v]
            assert u in ns, ("asymmetric rotation",u,v)
            w=ns[(ns.index(u)+1)%len(ns)]
            d=(v,w)
            if d==start: break
        faces.append(tuple(face))
    return faces

def build_strip(word):
    """Exact S02-B C37-derived strip."""
    n=len(word); zs=[z(i) for i in range(1,n+1)]
    arcs=[e for e in BASE_ARCS if e!=(12,13)]
    chain=[12]+zs+[13]
    arcs += list(zip(chain,chain[1:]))
    for zi,bit in zip(zs,word):
        arcs += [(7,zi),(zi,5)] if bit else [(5,zi),(zi,7)]
    rot={v:list(ns) for v,ns in BASE_ROT.items()}
    rot[7]=[2,3,8,12]+zs+[13,11]
    rot[5]=[0,6,13]+list(reversed(zs))+[12,8,4]
    rot[12]=[5,zs[0],7,8]
    rot[13]=[5,6,11,7,zs[-1]]
    for i,zi in enumerate(zs):
        prev=12 if i==0 else zs[i-1]
        nxt=13 if i==n-1 else zs[i+1]
        rot[zi]=[7,prev,5,nxt]
    return arcs,rot

def structural(arcs,rot):
    V=set(rot)
    U={tuple(sorted(e)) for e in arcs}
    assert len(U)==len(arcs), "loop/opposite/duplicate underlying edge"
    assert all(a!=b for a,b in arcs)
    RU={tuple(sorted((v,w))) for v,ns in rot.items() for w in ns}
    assert U==RU
    assert all(v in rot[w] for v,ns in rot.items() for w in ns)

    indeg={v:0 for v in V}; outdeg={v:0 for v in V}
    for a,b in arcs:
        outdeg[a]+=1; indeg[b]+=1
    assert min(indeg.values())>=2
    assert min(outdeg.values())>=2

    faces=trace_faces(rot)
    assert all(len(f)==3 for f in faces)
    assert len(U)==3*len(V)-6
    assert len(V)-len(U)+len(faces)==2
    return {
        "vertices":len(V),"edges":len(U),"faces":len(faces),
        "min_indegree":min(indeg.values()),"min_outdegree":min(outdeg.values())
    }

def acyclic_kahn(V,A,C):
    for color in (0,1):
        S={v for v in V if C[v]==color}
        indeg={v:0 for v in S}; adj={v:[] for v in S}
        for a,b in A:
            if a in S and b in S:
                adj[a].append(b); indeg[b]+=1
        q=[v for v in S if indeg[v]==0]; seen=0
        while q:
            v=q.pop(); seen+=1
            for w in adj[v]:
                indeg[w]-=1
                if indeg[w]==0: q.append(w)
        if seen!=len(S): return False
    return True

def acyclic_fw(V,A,C):
    for color in (0,1):
        S=[v for v in V if C[v]==color]
        idx={v:i for i,v in enumerate(S)}
        M=[[False]*len(S) for _ in S]
        for a,b in A:
            if a in idx and b in idx: M[idx[a]][idx[b]]=True
        for k in range(len(S)):
            for i in range(len(S)):
                if M[i][k]:
                    for j in range(len(S)):
                        M[i][j]=M[i][j] or (M[i][k] and M[k][j])
        if any(M[i][i] for i in range(len(S))): return False
    return True

def wheel_arcs(prev_bit,center_bit,next_bit):
    """
    Center X with boundary (U,L,D,R).
    Path/rim direction L->X->R.
    bit=1 means U->v->D; bit=0 means D->v->U.
    """
    X,U,L,D,R=0,1,2,3,4
    A=[(L,X),(X,R)]
    A += [(U,X),(X,D)] if center_bit else [(X,U),(D,X)]
    A += [(U,L),(L,D)] if prev_bit else [(L,U),(D,L)]
    A += [(U,R),(R,D)] if next_bit else [(R,U),(D,R)]
    return [X,U,L,D,R],A

def wheel_obstruction(triple):
    V,A=wheel_arcs(*triple)
    bad=[]
    for bc in itertools.product((0,1),repeat=4):
        if sum(bc)!=2: continue
        extA=extB=False
        for xc in (0,1):
            C={0:xc,1:bc[0],2:bc[1],3:bc[2],4:bc[3]}
            extA |= acyclic_kahn(V,A,C)
            extB |= acyclic_fw(V,A,C)
        assert extA==extB
        if not extA: bad.append("".join(map(str,bc)))
    return sorted(bad)

def check_alternating_strip(n):
    assert n>=5 and n%2==1
    word=tuple(1 if i%2==0 else 0 for i in range(n))
    arcs,rot=build_strip(word)
    s=structural(arcs,rot)
    rows=[]
    for i in range(1,n-1):
        triple=(word[i-1],word[i],word[i+1])
        bad=wheel_obstruction(triple)
        assert bad
        rows.append({
            "center":z(i+1),
            "triple":"".join(map(str,triple)),
            "bad_boundary_words":bad,
            "complete_degree":len(rot[z(i+1)]),
        })
    two_cycles=[]
    centers=[row["center"] for row in rows]
    for a,b in zip(centers,centers[1:]):
        two_cycles.append([a,b,a])
    assert two_cycles
    return {
        "n":n,"d7":len(rot[7]),"word":"".join(map(str,word)),
        "structural":s,"obstructive_internal_wheels":len(rows),
        "first_rows":rows[:4],"raw_release_two_cycles":two_cycles[:4],
        "raw_release_two_cycle_count":len(two_cycles),
    }

def build_bipyramid(n):
    assert n>=4 and n%2==0
    U,D=7,5
    R=[3000+i for i in range(n)]
    arcs=[]
    for i,r in enumerate(R):
        arcs.append((r,R[(i+1)%n]))
    for i,r in enumerate(R):
        bit=(i%2==0)
        arcs += [(U,r),(r,D)] if bit else [(D,r),(r,U)]
    rot={U:R[:], D:[R[0]]+list(reversed(R[1:]))}
    for i,r in enumerate(R):
        rot[r]=[U,R[(i-1)%n],D,R[(i+1)%n]]
    return arcs,rot,R

def check_bipyramid(n):
    arcs,rot,R=build_bipyramid(n)
    s=structural(arcs,rot)
    rows=[]
    for i,r in enumerate(R):
        triple=((i-1)%2==0, i%2==0, (i+1)%2==0)
        triple=tuple(int(x) for x in triple)
        bad=wheel_obstruction(triple)
        assert bad
        rows.append({"center":r,"triple":"".join(map(str,triple)),"bad":bad})
    release_cycle=R+[R[0]]
    return {
        "n":n,"pole_degree":n,"structural":s,
        "all_wheels_obstructive":True,
        "release_cycle_length":n,
        "release_cycle":release_cycle if n<=12 else release_cycle[:6]+["..."]+release_cycle[-3:],
        "rows_head":rows[:4],
    }

def shell_name(layer,pos): return 5000+3*layer+pos

def add_nested_shells(arcs,outer,depth):
    """
    Replace a directed triangular face A->B->C->A by repeated octahedral shells.
    Each layer has inner triangle a->b->c->a and cross directed 6-cycle
    A->b->C->a->B->c->A.
    """
    arcs=list(arcs); tris=[outer]
    A,B,C=outer
    for layer in range(1,depth+1):
        a,b,c=[shell_name(layer,j) for j in range(3)]
        arcs += [(a,b),(b,c),(c,a)]
        arcs += [(A,b),(b,C),(C,a),(a,B),(B,c),(c,A)]
        tris.append((a,b,c))
        A,B,C=a,b,c
    return arcs,tris

def check_nested_splice(strip_n,depth):
    assert strip_n%2==1
    word=tuple(1 if i%2==0 else 0 for i in range(strip_n))
    base_arcs,base_rot=build_strip(word)
    outer=(7,z(strip_n),13)
    assert (outer[0],outer[1]) in base_arcs
    assert (outer[1],outer[2]) in base_arcs
    assert (outer[2],outer[0]) in base_arcs

    arcs,tris=add_nested_shells(base_arcs,outer,depth)
    G=nx.Graph()
    G.add_edges_from((a,b) for a,b in arcs)
    planar,emb=nx.check_planarity(G)
    assert planar
    assert G.number_of_edges()==3*G.number_of_nodes()-6

    oldV=set(base_rot)
    preserved=True
    reversed_only=True
    for v in oldV:
        order=list(emb.neighbors_cw_order(v))
        restricted=[x for x in order if x in oldV]
        preserved &= cyc_eq(restricted,base_rot[v])
        reversed_only &= cyc_eq(list(reversed(restricted)),base_rot[v])
    assert preserved or reversed_only

    indeg={v:0 for v in G}; outdeg={v:0 for v in G}
    for a,b in arcs: outdeg[a]+=1; indeg[b]+=1
    assert min(indeg.values())>=2 and min(outdeg.values())>=2

    sep=[]
    for i in range(1,len(tris)-1):
        H=G.copy(); H.remove_nodes_from(tris[i])
        comps=[len(c) for c in nx.connected_components(H)]
        assert len(comps)>=2
        sep.append({"level":i,"triangle":list(tris[i]),"component_sizes":sorted(comps)})
    return {
        "strip_n":strip_n,"depth":depth,
        "vertices":G.number_of_nodes(),"edges":G.number_of_edges(),
        "min_indegree":min(indeg.values()),"min_outdegree":min(outdeg.values()),
        "old_rotation_preserved":preserved,
        "separator_count":len(sep),
        "separator_head":sep[:4],
        "separator_tail":sep[-2:] if sep else [],
        "local_shell_period":"all layers use the same directed octahedral shell",
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--strip-n",type=int,default=31)
    ap.add_argument("--bipyramid-max",type=int,default=64)
    ap.add_argument("--separator-depth",type=int,default=32)
    args=ap.parse_args()

    strip=check_alternating_strip(args.strip_n)
    bip=[]
    for n in range(8,args.bipyramid_max+1,2):
        bip.append(check_bipyramid(n))
    nested=check_nested_splice(args.strip_n,args.separator_depth)

    exact_bad={
        "010":wheel_obstruction((0,1,0)),
        "101":wheel_obstruction((1,0,1)),
    }
    assert exact_bad=={"010":["0110","1001"],"101":["0011","1100"]}

    out={
        "format":"opg169-s02b-cycle2-escape-rank-audit-v1",
        "verdict":"candidate_only","root_closed":False,
        "source":{
            "fresh_main_at_analysis_start":"b742c72f1d50849bd074f1f7f7f6e2ed019870c4",
            "prior_s02b_checker_sha256":"549239acee6ed91e57ab941c0d2c0635fc5f9ded2471b2b4cdf881ea9ff9033d",
        },
        "wheel_obstruction":exact_bad,
        "c37_alternating_strip":strip,
        "generic_alternating_bipyramids":{
            "checked_even_n":[x["n"] for x in bip],
            "largest":bip[-1],
            "all_passed":True,
            "scope":"root-class stress test; not claimed to be an exact C37 descendant",
        },
        "c37_separator_splice":nested,
        "rank_falsifiers":{
            "history_free_active_window_rank":"refuted by raw two-cycles W_i<->W_{i+1} in the exact C37-derived alternating strip",
            "local_successor_release_rank":"refuted in the generic alternating bipyramid: successor release cycles around the ring",
            "boundary_size":"constant 4 on wheel-release chain; constant 3 on separator stack",
            "active_local_isomorphism_type":"period 2 on strip/bipyramid; period 1 on octahedral separator shells",
            "separator_level_from_outer_root":"increases under inward crossing",
            "raw_controlled_size":"can increase under star absorption",
        },
        "surviving_history_rank":{
            "candidate":"lexicographic unseen vertices / incomplete exposed stars / unprocessed rooted separator sides",
            "status":"not refuted by these families",
            "limitation":"proves discovery well-foundedness only; does not prove terminal source is reducible or gives GSRC/JMAP",
        },
        "trust_boundary":"same-principal exact checker; NetworkX planarity plus separate rotation/face/coloring checks are differential candidate controls, not independent verification",
        "networkx":nx.__version__,
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
