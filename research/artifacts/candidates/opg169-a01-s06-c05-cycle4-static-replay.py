#!/usr/bin/env python3
"""Static consistency replay for the transported S06 Cycle 4 summary.

This checks only the frozen transport totals and declared identities.  It does
not regenerate the 24,928-row catalogue and is not an independent verifier.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUMMARY = HERE / "opg169-a01-s06-c05-cycle4-summary.json"


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    raw = SUMMARY.read_bytes()
    data = json.loads(raw)

    need(data["format"] == "opg169-s06-cycle5-transport-recovery-v1", "format")
    need(data["base_revision"] == "dc6ee891ed7614602e88d48a57314416082dd022", "base")
    need(data["trust"] == {
        "independent_verification": False,
        "kernel_checked": False,
        "result_admitted": False,
        "verdict": "candidate_only",
    }, "trust boundary")
    need(data["root_closed"] is False, "root must remain open")

    rule = data["replacement"]
    need(rule["delete"] == [0, 2], "deleted pair")
    need(rule["adds"] == [[5, 7], [6, 7], [7, 4]], "fan arcs")
    need(rule["hole_cycle"] == [3, 4, 5, 6, 11, 7], "merged hole")
    need(rule["interface_controlled"] == [0, 2, 3, 7], "interface")
    need(rule["relation_contract"] == "R_P_plus subseteq R_Q_plus", "relation")

    c39 = data["c39"]
    need(c39["parents"] == 70, "C39 parent count")
    need(c39["equal_lifts"] + c39["strict_lifts"] == c39["valid_q"], "C39 partition")
    need(c39["failures"] == 0, "C39 failure")

    c38 = data["c38"]
    for key in ("direct_d19", "whole_obstruction"):
        row = c38[key]
        need(row["equal_lifts"] + row["strict_lifts"] == row["valid_q"], f"C38 {key}")
        need(row["failures"] == 0, f"C38 {key} failure")

    c37 = data["c37"]
    need(sum(c37["families"].values()) == 160, "C37 family allocation")
    direct = c37["direct_universal"]
    need(direct["source_valid_success"] + direct["class_invalid"] == 160, "direct split")
    need(direct["equal_lifts"] + direct["strict_lifts"] == direct["valid_q"], "direct lifts")

    cat = c37["catalogue"]
    need(cat["equal_lifts"] + cat["strict_lifts"] + cat["failed_inputs"] == cat["valid_q"], "catalogue input partition")
    need(cat["ordinary_failures"] + cat["relation_failures"] == cat["failed_inputs"], "failure partition")
    need(cat["vacuous_q"] == 0, "vacuous Q")
    need(cat["candidate_rows"] == 24928 and cat["successful_rows"] == 11147, "catalogue rows")

    final = c37["final_selected"]
    need(final["merged_02"] + final["bare_delete3"] == final["parents"] == 160, "selected menu")
    need(final["equal_lifts"] + final["strict_lifts"] == final["valid_q"], "selected lifts")
    need(final["failures"] == final["guarded_only"] == final["residual"] == 0, "selected coverage")

    need(data["catalogue_stdout_sha256"] == "dd215e43d05e9cbe529d86afcf903f94b96eac879be85fdd7fd5ccf4da98fc8c", "catalogue digest")
    archive = data["archive"]
    need(archive["local_only"] is True, "archive must not be represented as transported")
    need(archive["sha256"] == "a2ea17f4794d5746f100bd0088e152f9909b4f4dcbf5047bb92366a47d62fca4", "archive digest")

    print(json.dumps({
        "status": "ok",
        "scope": "static_transport_consistency_only",
        "summary_bytes": len(raw),
        "summary_sha256": hashlib.sha256(raw).hexdigest(),
        "c37_parents": final["parents"],
        "c39_parents": c39["parents"],
        "root_closed": data["root_closed"],
        "verdict": data["trust"]["verdict"],
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
