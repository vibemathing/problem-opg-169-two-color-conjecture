#!/usr/bin/env python3
"""Static Cycle-4 S09 GSRC occurrence audit.

This checker does not enumerate descendant configurations and does not recompute
strong-profile reductions. It checks the repository-bound 160-parent registry,
the direction of the occurrence claim, the pure-logic non-inversion countermodel,
and the conditional selected-J escape inference recorded in the Cycle-4
obligation manifest.

Candidate-only; not a trusted verifier receipt.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ATLAS = HERE / "opg169-a01-s09-cycle3-c37-lineage-atlas.json"
OBL = HERE / "opg169-a01-s09-cycle4-gsrc-occurrence-obligations.json"

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)

def main() -> None:
    atlas_bytes = ATLAS.read_bytes()
    atlas = json.loads(atlas_bytes)
    obl_bytes = OBL.read_bytes()
    obl = json.loads(obl_bytes)

    # Registry identity only; no profile search.
    require(atlas["counts"]["parents"] == 160, "registry parent count")
    require(atlas["counts"]["families"] == 5, "registry family count")
    require(atlas["counts"]["words_per_family"] == 32, "registry word count")
    require(atlas["counts"]["delete_0_2_total"] == 156, "delete 0,2 count")
    require(atlas["counts"]["bare_delete_3"] == 4, "bare delete-3 count")
    require(set(atlas["families"]) == {"D","X5","X6","Y4","Y5"}, "family set")

    ids = [f"{fam}/{w}" for fam in sorted(atlas["families"]) for w in range(32)]
    require(len(ids) == len(set(ids)) == 160, "unique source ids")
    ids_digest = sha256("\n".join(ids).encode())
    require(ids_digest == atlas["row_expansion"]["expanded_parent_ids_sha256"],
            "expanded parent id digest")

    # The target is intentionally open. A reduction registry has no existential
    # occurrence content by itself.
    target = obl["target_occurrence_claim"]
    require(target["status"] == "OPEN_NOT_DERIVED", "GSRC target status")
    require(obl["counts"]["gsrc_occurrence_edges_proved_to_R160"] == 0,
            "unexpected occurrence edge")

    # Pure logical countermodel: all 160 parents may be reducible while no parent
    # occurs as the source selected by a fixed face. This is not a graph model.
    cm = obl["non_inversion_countermodel"]
    require(cm["kind"] == "pure_logic_not_graph_counterexample", "countermodel type")
    require(cm["registry_parent_count"] == 160, "countermodel registry size")
    require(cm["reducible_for_every_registry_parent"] is True, "countermodel premise")
    require(cm["occurrence_pairs"] == 0, "countermodel occurrence pairs")
    require(cm["premise_registry_total_reduction"] is True, "countermodel premise truth")
    require(cm["conclusion_exists_registry_occurrence_for_f"] is False,
            "countermodel conclusion must fail")

    # Conditional selected-J escape. C36 gives lower bound 6 in its exact selected
    # J direction; the equality case d7=6 is exactly R160 and is reducible, hence
    # the surviving minimum-counterexample branch has d7>=7.
    esc = obl["conditional_escape"]
    require(esc["status"] == "PASS_CANDIDATE_DERIVATION", "escape status")
    require(obl["counts"]["conditional_selected_J_escape_lower_bound"] == 7,
            "escape lower bound")
    require("d(7)>=7" in esc["conclusion"], "escape conclusion")

    # This lane must never regress into descendant enumeration.
    require(obl["counts"]["descendant_census_runs"] == 0, "descendant census forbidden")
    require(any(m["name"] == "descendant_census" and m["expected"] == "REJECT"
                for m in obl["mutation_tests"]), "descendant mutation missing")

    established = {tuple(e) for e in obl["gsrc_occurrence_dag"]["established_edges"]}
    missing = {tuple(e) for e in obl["gsrc_occurrence_dag"]["missing_edges"]}
    require(("D0","A48") in established, "arithmetic edge")
    require(("A48","LSRC") in missing and ("LSRC","GSRC") in missing,
            "source bridge must remain open")
    require(("GSRC","C37J") in missing, "C37 specialization must remain open")

    result = {
        "status":"ok",
        "verdict":"candidate_only",
        "root_closed":False,
        "registry_parents":160,
        "registry_parent_ids_sha256":ids_digest,
        "obligations_sha256":sha256(obl_bytes),
        "registry_inverse":"INVALID_AS_LOGICAL_INFERENCE",
        "gsrc160_occurrence":"OPEN_NOT_DERIVED",
        "conditional_selected_J_escape":"d(7)>=7",
        "descendant_census_runs":0,
        "open_bridge":["A48->LSRC","LSRC->GSRC","GSRC->C37J","GSRC->JMAP"],
        "trust_boundary":"static source-lineage/logic audit only; no profile recomputation or trusted verification"
    }
    print(json.dumps(result, sort_keys=True, separators=(",",":")))

if __name__ == "__main__":
    main()
