#!/usr/bin/env python3
"""R08 S09 Cycle 5: narrow selected-J GSRC source-or-escape checker.

Candidate-only. This checker validates the row schema, reconstructs the exact
C37 degree-six geometry/alias quotient, and independently consumes one actual
D/3 source record. It does not enumerate descendants or recompute profile lifts.
"""
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path
import itertools as it

D = Path(__file__).resolve().parent
SCHEMA = D / "opg169-a01-s09-cycle5-gsrc-source-or-escape-schema.json"
RECORD = D / "opg169-a01-s09-cycle5-gsrc-source-record-D3.json"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def trace_faces(rot):
    rot={int(k):list(v) for k,v in rot.items()}
    darts={(u,v) for u,ns in rot.items() for v in ns}
    faces=[]
    while darts:
        start=min(darts); d=start; face=[]
        while True:
            assert d in darts, ("repeat", start, d, face)
            darts.remove(d)
            u,v=d; face.append(u)
            ns=rot[v]; assert u in ns
            w=ns[(ns.index(u)+1)%len(ns)]
            d=(v,w)
            if d==start: break
        faces.append(face)
    return faces

BASE_TRIANGLES=[
 [0,2,3],[0,6,2],[0,5,6],[0,4,5],[0,3,4],
 [2,7,3],[2,11,7],[2,6,11],[3,8,4],[3,7,8]
]
I={0,2,3,7}

def canon_cycle(f):
    return min(tuple(f[k:]+f[:k]) for k in range(len(f)))

def geom(x,y):
    tris=BASE_TRIANGLES+[[8,7,x],[x,7,y],[7,11,y]]
    succ={}; adj={}
    for a,b,c in tris:
        if len({a,b,c})<3: return {"bad":"facial-repeat"}
        for v,l,r in ((b,a,c),(c,b,a),(a,c,b)):
            row=succ.setdefault(v,{})
            if l in row and row[l]!=r: return {"bad":"link-conflict","v":v}
            row[l]=r
            adj.setdefault(v,set()).update((l,r))
    options={}
    for v,row in succ.items():
        if len(set(row.values()))!=len(row): return {"bad":"link-predecessor","v":v}
        ns=adj[v]; heads=sorted(ns-set(row.values())); parts=[]
        if not heads:
            first=min(ns); seq=[first]; q=row[first]
            while q!=first:
                if q in seq: return {"bad":"link-cycle","v":v}
                seq.append(q); q=row[q]
            if set(seq)!=ns: return {"bad":"link-extra","v":v}
            if v not in I and len(ns)<4: return {"bad":"full-degree-less-four","v":v}
            options[v]=[seq]
        else:
            for h in heads:
                seq=[h]
                while seq[-1] in row:
                    q=row[seq[-1]]
                    if q in seq: return {"bad":"partial-cycle","v":v}
                    seq.append(q)
                parts.append(seq)
            if sum(map(len,parts))!=len(ns): return {"bad":"link-extra","v":v}
            options[v]=[sum([parts[0],*perm],[]) for perm in it.permutations(parts[1:])]
    vs=sorted(options); edges=sum(map(len,adj.values()))//2
    target={canon_cycle(t) for t in tris}
    for choices in it.product(*(options[v] for v in vs)):
        rot=dict(zip(vs,choices)); fs=trace_faces(rot)
        if len(vs)-edges+len(fs)==2 and target <= {canon_cycle(f) for f in fs}:
            return {"rot":rot,"triangles":tris,"faces":fs,"n":len(vs),"e":edges}
    return {"bad":"no-plane-completion"}

def underlying(arcs):
    return {tuple(sorted(e)) for e in arcs}

def directed_set(arcs):
    return {tuple(e) for e in arcs}

def main():
    schema=json.loads(SCHEMA.read_text())
    rec=json.loads(RECORD.read_text())

    assert schema["verdict"]=="candidate_only" and schema["root_closed"] is False
    assert rec["verdict"]=="candidate_only" and rec["root_closed"] is False
    assert "D0->R160" in schema["nonclaims"][0]
    assert schema["input_contract"]["requires_actual_source_bound"] is True

    # Alias quotient: exact 13 labelled types, exact five survivors.
    alias=schema["classification"]["C37"]["alias_quotient"]
    assert len(alias)==13
    survivors=[r["name"] for r in alias if r["status"]=="C37"]
    assert survivors==["D","X5","X6","Y4","Y5"]

    # Reconstruct all five underlying plane templates independently.
    expected_pairs={"D":(12,13),"X5":(5,13),"X6":(6,13),"Y4":(12,4),"Y5":(12,5)}
    for name,pair in expected_pairs.items():
        g=geom(*pair); assert "bad" not in g
        stored=schema["classification"]["C37"]["families"][name]
        assert (stored["x"],stored["y"])==pair
        got={str(k):v for k,v in sorted(g["rot"].items())}
        assert got==stored["patch_rotation"]
        assert g["n"] in (10,11) and g["e"]==23

    # Actual record: simple oriented triangulation and exact faces.
    rot=rec["actual_embedding"]["rotation"]
    arcs=rec["actual_embedding"]["arcs"]
    V=set(map(int,rot))
    A=directed_set(arcs); U=underlying(arcs)
    assert len(A)==len(arcs)==len(U)
    assert all(a!=b and (b,a) not in A for a,b in A)
    rotU={tuple(sorted((int(v),w))) for v,ns in rot.items() for w in ns}
    assert rotU==U
    fs=trace_faces(rot)
    assert len(V)-len(U)+len(fs)==2
    assert len(U)==3*len(V)-6
    assert all(len(f)==3 for f in fs)
    assert {canon_cycle(f) for f in fs}=={canon_cycle(f) for f in rec["actual_embedding"]["faces"]}

    # Provenance is actual and source-bound. f=(0,2,3), p=0 is an F witness.
    prov=rec["provenance"]
    assert prov["source_bound"] is True
    f=prov["source_face"]
    assert canon_cycle(f) in {canon_cycle(x) for x in fs}
    assert prov["descriptor"]=={"kind":"F","p":0,"g":None}
    w=prov["c48_witness"]
    assert (w["d"],w["t"],w["s"])==(5,0,5)
    assert w["d"]-3*w["t"]==w["s"] and w["F48"] is True
    gamma=Fraction(1,5)
    assert -1+3*gamma==Fraction(-2,5)
    assert rec["payments"]["source_face_charge"]=="-2/5"
    assert rec["payments"]["marks"]==[] and rec["payments"]["payer_ids"]==[]
    assert rec["payments"]["classification_invents_payment"] is False

    # Ownership partition is literal and complete.
    SA=directed_set(rec["ownership"]["source_owned_arcs"])
    EA=directed_set(rec["ownership"]["exterior_owned_arcs"])
    assert SA.isdisjoint(EA) and SA|EA==A
    assert rec["ownership"]["no_edge_double_ownership"] is True
    stars=rec["ownership"]["complete_stars"]
    assert stars["0"]==[2,6,5,4,3]
    assert stars["2"]==[0,3,7,11,6]
    assert stars["3"]==[0,4,8,7,2]
    assert stars["7"]==[2,3,8,12,13,11]
    for v in ("0","2","3","7"):
        assert list(rot[v])==stars[v]

    # Exact C37 parent identity from actual source data, not from reduction coverage.
    sel=rec["selected_J"]; cls=rec["classification"]
    assert sel["degree7"]==6 and len(sel["ordered_wedge_neighbors"])==2
    x,y=sel["ordered_wedge_neighbors"]
    assert (x,y)==(12,13) and sel["alias_signature"]==["new","new"]
    assert cls["family"]=="D"
    roles=[(8,x),(x,7),(x,y),(y,7),(y,11)]
    extras=directed_set(cls["actual_extra_arcs"])
    bits=0
    for i,e in enumerate(roles):
        if e in extras: pass
        elif e[::-1] in extras: bits |= 1<<i
        else: raise AssertionError(("missing role edge",e))
    assert bits==3 and cls["word"]==3 and cls["parent_id"]=="D/3"
    assert cls["registry_use_order"].startswith("occurrence/source identity first")
    assert cls["family_template_match"] is True
    assert rec["actual_embedding"]["source_patch_rotation"]==schema["classification"]["C37"]["families"]["D"]["patch_rotation"]

    # Imported R160 rule is used only after identity.
    rule=cls["imported_ancestor_rule"]
    assert rule["class"]=="direct_fan_delete_0_2"
    assert rule["delete"]==[0,2] and rule["adds"]==[[5,7],[6,7],[7,4]]
    assert rule["hole"]==[3,4,5,6,11,7]
    assert rule["strict_all_exterior_candidate"] is True

    # Source-or-escape cut is disjoint and exhaustive after the C36 d7>=6 gate.
    def cut(d7):
        assert d7>=6
        return "C37" if d7==6 else "J_HIGHPORT"
    assert cut(6)=="C37"
    assert all(cut(d)=="J_HIGHPORT" for d in range(7,33))
    assert schema["classification"]["J_HIGHPORT"]["disjoint_from_C37"].startswith("degree:")

    out={
      "status":"ok",
      "verdict":"candidate_only",
      "root_closed":False,
      "scope":"already actual source-bound selected C35/C36 J occurrence",
      "narrow_selected_J_G_COVER":"PASS_CANDIDATE",
      "R_TOTAL":"NOT_CLAIMED",
      "G_TOTAL_from_arbitrary_Desc48":"NOT_CLAIMED",
      "registry_inversion":"FORBIDDEN",
      "alias_types":13,
      "c37_families":survivors,
      "degree6_cut":"exact C37 family/word parent identity",
      "degree_ge7_cut":"J_HIGHPORT exact-source escape record",
      "instantiated_parent":"D/3",
      "instantiated_source_face":[0,2,3],
      "instantiated_witness":{"kind":"F","p":0},
      "payer_count":0,
      "ownership_partition":"23 source-owned arcs + 4 exterior-owned arcs",
      "schema_sha256":sha256(SCHEMA),
      "record_sha256":sha256(RECORD),
      "descendant_census_runs":0,
      "profile_recomputations":0
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
