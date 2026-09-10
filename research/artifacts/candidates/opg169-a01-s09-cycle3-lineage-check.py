#!/usr/bin/env python3
"""Static expander/checker for the S09 Cycle 3 C37 source-lineage atlas.

It expands the generative normal form to all 160 source rows, verifies the
cartesian source registry, direct-fan reverse conflicts, ancestor rule classes,
the four bare-delete exceptions, and the unique D/19 -> C40 core identity.

It does NOT recompute any strong-profile lift table and is not a trusted verifier.
"""
from __future__ import annotations
import collections, hashlib, json, sys
from pathlib import Path

C40_BASE = {
(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),(4,5),(4,8),
(5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7),
(11,12),(13,12),(13,8),(12,7),(7,13)
}

def need(x, msg):
    if not x:
        raise AssertionError(msg)

def sha256_text(s):
    return hashlib.sha256(s.encode()).hexdigest()

def expand(d):
    source=d["source"]
    base={tuple(e) for e in source["base_arcs"]}
    fan={tuple(e) for e in source["direct_fan_adds"]}
    out=[]
    for fam in ["D","X5","X6","Y4","Y5"]:
        f=d["families"][fam]
        x,y=f["x"],f["y"]
        direct=set(f["direct_fan_words"])
        catalogue=set(f["catalogue_delete_0_2_words"])
        bare=set(f["bare_delete_3_words"])
        need(direct.isdisjoint(catalogue|bare) and catalogue.isdisjoint(bare),"class overlap")
        need(direct|catalogue|bare==set(range(32)),"family word partition")
        for w in range(32):
            nominal=[(8,x),(x,7),(x,y),(y,7),(y,11)]
            extra=[(v,u) if ((w>>i)&1) else (u,v) for i,(u,v) in enumerate(nominal)]
            A=set(base)
            for e in extra:
                need(e[0]!=e[1] and (e[1],e[0]) not in A,"simple source orientation")
                A.add(e)
            conflicts=sorted((v,u) for u,v in fan if (v,u) in A)
            available=not conflicts
            need(available==(w in direct),"direct-fan classification")
            if w in bare:
                rule="bare_delete_3"
            elif available:
                rule="direct_fan_delete_0_2"
            else:
                rule="merged_delete_0_2_catalogue"
            named=(fam=="D" and w==19)
            need(named==(w in set(f["named_C38_C40_words"])),"named-chain classification")
            out.append({
                "parent_id":f"{fam}/{w}",
                "family":fam,"word":w,"x":x,"y":y,
                "extra_arcs":[list(e) for e in extra],
                "direct_fan_available":available,
                "fan_reverse_conflicts":[list(e) for e in conflicts],
                "ancestor_rule_class":rule,
                "named_chain":"C38->C39->C40" if named else None
            })
    return out

def swap(v):
    return 13 if v==12 else 12 if v==13 else v

def main(path):
    d=json.loads(Path(path).read_text(encoding="utf-8"))
    need(d["format"]=="opg169-s09-c37-source-lineage-atlas-v1","format")
    need(d["representation"]=="generative_normal_form_expands_to_160_rows","representation")
    need(d["verdict"]=="candidate_only" and d["root_closed"] is False,"status")
    rows=expand(d)
    need(len(rows)==160 and len({r["parent_id"] for r in rows})==160,"160 unique rows")

    ids="\n".join(r["parent_id"] for r in rows)
    canon=json.dumps(rows,sort_keys=True,separators=(",",":"))
    need(sha256_text(ids)==d["row_expansion"]["expanded_parent_ids_sha256"],"parent-id digest")
    need(sha256_text(canon)==d["row_expansion"]["expanded_rows_sha256"],"expanded-row digest")

    kinds=collections.Counter(r["ancestor_rule_class"] for r in rows)
    need(kinds==collections.Counter({
        "direct_fan_delete_0_2":96,
        "merged_delete_0_2_catalogue":60,
        "bare_delete_3":4
    }),"rule totals")
    need(sum(k!="bare_delete_3" for k in [r["ancestor_rule_class"] for r in rows])==156,"delete 0,2 total")

    base={tuple(e) for e in d["source"]["base_arcs"]}
    d19=next(r for r in rows if r["parent_id"]=="D/19")
    mapped={(swap(u),swap(v)) for u,v in base|{tuple(e) for e in d19["extra_arcs"]}}
    need(mapped==C40_BASE,"D/19 -> C40 exact core")

    print(json.dumps({
        "status":"ok",
        "parents":160,
        "direct_fan_delete_0_2":96,
        "merged_delete_0_2_catalogue":60,
        "bare_delete_3":4,
        "delete_0_2_total":156,
        "named_repository_lineage_rows":1,
        "d19_c40_core_identity":True,
        "profile_tables_recomputed":False,
        "verdict":"candidate_only",
        "root_closed":False
    },sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main(sys.argv[1])
