#!/usr/bin/env python3
"""Static S09 Cycle-4 GSRC occurrence-direction audit.

No descendant configurations are generated and no strong-profile table is
recomputed.  The checker validates the exact Cycle-3 R160 identity, corrected
A48 witness semantics as frozen in the Cycle-4 obligations, the pure-logic
non-inversion countermodel, the conditional selected-J escape status, and the
zero-descendant-census invariant.

Candidate-only; not a trusted verifier receipt.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ATLAS = HERE / "opg169-a01-s09-cycle3-c37-lineage-atlas.json"
OBL = HERE / "opg169-a01-s09-cycle4-gsrc-occurrence-obligations.json"

def need(x, msg):
    if not x:
        raise SystemExit(msg)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main():
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    obl_bytes = OBL.read_bytes()
    obl = json.loads(obl_bytes)

    # Exact conditional registry identity; no reduction/profile recomputation.
    need(atlas["counts"]["parents"] == 160, "registry parent count")
    need(atlas["counts"]["families"] == 5, "registry family count")
    need(atlas["counts"]["words_per_family"] == 32, "registry word count")
    need(atlas["counts"]["delete_0_2_total"] == 156, "delete-{0,2} count")
    need(atlas["counts"]["bare_delete_3"] == 4, "bare-delete-3 count")
    family_order = ["D","X5","X6","Y4","Y5"]
    need(set(atlas["families"]) == set(family_order), "family set")
    ids = [f"{fam}/{w}" for fam in family_order for w in range(32)]
    need(len(ids) == len(set(ids)) == 160, "unique R160 ids")
    ids_digest = sha256("\n".join(ids).encode())
    need(ids_digest == atlas["row_expansion"]["expanded_parent_ids_sha256"],
         "R160 id digest")

    need(obl["format"] == "opg169-s09-cycle4-gsrc-occurrence-obligations-v2",
         "obligation format")
    need(obl["verdict"] == "candidate_only" and obl["root_closed"] is False,
         "candidate status")

    # Corrected A48: existence of a witness p, then XOR only for fixed (f,p).
    a48 = obl["a48_witness_semantics"]
    q = set(a48["established_quantifiers"])
    need("forall f, D0(f) -> exists p W48(f,p)" in q,
         "missing W48 witness existence")
    need("forall f,p, W48(f,p) -> exactly_one(F48(f,p),SG48(f,p))" in q,
         "missing fixed-witness F/SG XOR")
    notq = set(a48["not_established"])
    need("unique p with W48(f,p)" in notq, "unique witness must remain unproved")
    need("face-level exactly_one(exists p F48(f,p), exists p SG48(f,p))" in notq,
         "face-level XOR must remain unproved")
    need("unique singleton gap g on an SG witness" in notq,
         "unique SG gap must remain unproved")
    need("(f,p,g)" in a48["sg_provenance"],
         "SG gap provenance must be carried")

    # Registry non-inversion countermodel: a logic countermodel, never graph data.
    target = obl["target_occurrence_claim"]
    need(target["status"] == "OPEN_NOT_DERIVED", "GSRC160 target status")
    cm = obl["non_inversion_countermodel"]
    need(cm["kind"] == "pure_logic_not_graph_counterexample",
         "countermodel type")
    need(cm["registry_parent_count"] == 160, "countermodel size")
    need(cm["reducible_for_every_registry_parent"] is True,
         "countermodel registry premise")
    need(cm["occurrence_pairs"] == 0, "countermodel occurrence relation")
    need(cm["premise_registry_total_reduction"] is True,
         "countermodel premise truth")
    need(cm["conclusion_exists_registry_occurrence_for_f"] is False,
         "countermodel must falsify occurrence conclusion")

    # Positive conditional escape: C36 >=6 plus R160 killing equality -> >=7.
    esc = obl["conditional_escape"]
    need(esc["status"] == "PASS_CANDIDATE_DERIVATION", "escape status")
    need("d(7)>=7" in esc["conclusion"], "escape conclusion")
    need(obl["counts"]["conditional_selected_J_escape_lower_bound"] == 7,
         "escape lower bound")

    dag = obl["gsrc_occurrence_dag"]
    established = set(dag["established_relations"])
    missing = set(dag["missing_relations"])
    need("forall f, D0(f) -> exists p W48(f,p)" in established,
         "D0/W48 relation")
    need("forall f,p, W48(f,p) -> exactly_one(F48(f,p),SG48(f,p))" in established,
         "fixed-witness tag relation")
    need(any(x.startswith("F48(f,p) -> LSRC_F") for x in missing),
         "F->LSRC open")
    need(any(x.startswith("SG48(f,p)") for x in missing),
         "SG->LSRC open")
    need(any(x.startswith("LSRC_F/LSRC_SG -> GSRC") for x in missing),
         "LSRC->GSRC open")
    need(any(x.startswith("GSRC -> C37J") for x in missing),
         "GSRC specialization open")
    need("GSRC -> JMAP" in missing, "JMAP open")

    # Mutation gate: explicitly reject witness-erasing and descendant-census moves.
    muts = {m["name"]:m["expected"] for m in obl["mutation_tests"]}
    for name in [
        "invert_registry","face_level_xor","drop_witness_p","drop_gap_g",
        "arithmetic_is_occurrence","local_is_global","force_degree6",
        "drop_payer_identity","pretend_branch_name_is_evidence",
        "descendant_census"
    ]:
        need(muts.get(name) == "REJECT", f"mutation not rejected: {name}")

    need(obl["counts"]["gsrc_occurrence_edges_proved_to_R160"] == 0,
         "unexpected R160 occurrence edge")
    need(obl["counts"]["descendant_census_runs"] == 0,
         "descendant census forbidden")

    result = {
        "status":"ok",
        "verdict":"candidate_only",
        "root_closed":False,
        "registry_parents":160,
        "registry_parent_ids_sha256":ids_digest,
        "obligations_sha256":sha256(obl_bytes),
        "registry_inverse":"INVALID_AS_LOGICAL_INFERENCE",
        "a48_face_level_xor":"INVALID_READING",
        "a48_fixed_witness_xor":"PASS_CANDIDATE_ARITHMETIC",
        "gsrc160_occurrence":"OPEN_NOT_DERIVED",
        "conditional_selected_J_escape":"d(7)>=7",
        "descendant_census_runs":0,
        "open_bridge":[
            "F48(f,p)->LSRC_F",
            "SG48(f,p,g)->LSRC_SG",
            "LSRC_F/LSRC_SG->GSRC",
            "GSRC->C37J_or_disjoint_source",
            "GSRC->JMAP"
        ],
        "trust_boundary":"static source-lineage/witness-logic audit only; no descendant or profile recomputation; not trusted verification"
    }
    print(json.dumps(result, sort_keys=True, separators=(",",":")))

if __name__ == "__main__":
    main()
