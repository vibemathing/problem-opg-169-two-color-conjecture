#!/usr/bin/env python3
"""Independent finite ledger for S16 Cycle 4's exact D/19 row language.

This replays the C39 alias/rotation/orientation filters, then checks that the
C40 named structural, unguarded, residual and guarded-complement predicates
form a disjoint 10+24+22+14 partition of all 70 compatible labelled rows.
It does not certify any graph replacement or global unavoidability theorem.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path
from typing import Any

BASE_ARCS = {
    (0, 2), (0, 4), (2, 3), (2, 6), (2, 11), (3, 0), (3, 4),
    (3, 7), (4, 5), (4, 8), (5, 0), (5, 6), (6, 0), (7, 2),
    (7, 8), (8, 3), (11, 6), (11, 7), (11, 12), (13, 12),
    (13, 8), (12, 7), (7, 13),
}
BASE_TRIS = [
    (0, 2, 3), (0, 6, 2), (0, 5, 6), (0, 4, 5), (0, 3, 4),
    (2, 7, 3), (2, 11, 7), (2, 6, 11), (3, 8, 4), (3, 7, 8),
    (8, 7, 13), (13, 7, 12), (12, 7, 11),
]
OLD = [6, 11, 12, 13]
NEW = "new"

EXPECTED_FAMILIES = [
    (11, 12), (11, 13), (11, NEW), (12, 13), (12, NEW),
    (13, NEW), (NEW, 6), (NEW, 11), (NEW, 12), (NEW, 13),
    (NEW, NEW),
]

STRUCTURAL = {
    (11, 13): {2, 3, 6, 7},
    (12, 13): {2, 6},
    (NEW, 13): {2, 3, 6, 7},
}
UNGUARDED = {
    (11, 12): {1, 3, 5, 7},
    (11, NEW): set(range(8)),
    (13, NEW): {1, 3, 4, 6, 7},
    (NEW, 6): {3, 4, 5, 6, 7},
    (NEW, 12): {3, 7},
}
RESIDUAL = {
    (12, NEW): {2, 5},
    (13, NEW): {2, 5},
    (NEW, 6): {2},
    (NEW, 11): {2, 4, 5},
    (NEW, 12): {2, 4, 5},
    (NEW, NEW): {2, 4, 5},
}


def concrete(kind: int | str, fresh: int) -> int:
    return fresh if kind == NEW else int(kind)


def successors(tris: list[tuple[int, int, int]]) -> dict[int, dict[int, int]] | None:
    succ: dict[int, dict[int, int]] = {}
    for a, b, c in tris:
        for v, x, y in ((b, a, c), (c, b, a), (a, c, b)):
            row = succ.setdefault(v, {})
            if x in row and row[x] != y:
                return None
            row[x] = y
    return succ


def closed_links(tris: list[tuple[int, int, int]]) -> dict[int, int] | None:
    succ = successors(tris)
    if succ is None:
        return None
    answer: dict[int, int] = {}
    for v, row in succ.items():
        neighbours = set(row) | set(row.values())
        indegree = collections.Counter(row.values())
        closed = set(row) == neighbours and all(indegree[n] == 1 for n in neighbours)
        if closed:
            answer[v] = len(neighbours)
    return answer


def alias_catalogue() -> tuple[list[tuple[int | str, int | str]], list[dict[str, Any]]]:
    surviving: list[tuple[int | str, int | str]] = []
    excluded: list[dict[str, Any]] = []
    kinds: list[int | str] = OLD + [NEW]
    for q_kind in kinds:
        for r_kind in kinds:
            if q_kind != NEW and r_kind != NEW and q_kind == r_kind:
                continue
            q = concrete(q_kind, 14)
            r = concrete(r_kind, 15)
            tris = BASE_TRIS + [(5, 4, q), (q, 4, r), (r, 4, 8)]
            links = closed_links(tris)
            if links is None:
                excluded.append({"q": q_kind, "r": r_kind, "reason": "rotation_conflict"})
                continue
            if any(degree < 4 for degree in links.values()):
                excluded.append({
                    "q": q_kind,
                    "r": r_kind,
                    "reason": "closed_link_degree_lt4",
                    "closed_links": links,
                })
                continue
            vertices = {0, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, q, r}
            edges = {frozenset(edge) for edge in BASE_ARCS}
            for edge in [(5, q), (q, 4), (q, r), (r, 8), (r, 4)]:
                edges.add(frozenset(edge))
            if len(edges) > 3 * len(vertices) - 6:
                excluded.append({
                    "q": q_kind,
                    "r": r_kind,
                    "reason": "planar_edge_bound",
                    "vertices": len(vertices),
                    "edges": len(edges),
                })
                continue
            surviving.append((q_kind, r_kind))
    return surviving, excluded


def orientation_is_compatible(q_kind: int | str, r_kind: int | str, word: int) -> bool:
    q = concrete(q_kind, 14)
    r = concrete(r_kind, 15)
    arcs = set(BASE_ARCS)
    new_arcs = [
        (5, q),
        (q, 4),
        (q, r) if word & 1 else (r, q),
        (r, 8) if word & 2 else (8, r),
        (r, 4) if word & 4 else (4, r),
    ]
    for u, v in new_arcs:
        if u == v or (v, u) in arcs:
            return False
        arcs.add((u, v))
    return True


def named(row: tuple[int | str, int | str, int], table: dict[tuple[int | str, int | str], set[int]]) -> bool:
    q, r, word = row
    return word in table.get((q, r), set())


def classify(row: tuple[int | str, int | str, int]) -> str:
    flags = {
        "structural": named(row, STRUCTURAL),
        "unguarded": named(row, UNGUARDED),
        "residual": named(row, RESIDUAL),
    }
    named_hits = [key for key, value in flags.items() if value]
    if len(named_hits) > 1:
        raise AssertionError(f"overlapping named classes for {row}: {named_hits}")
    if named_hits:
        return named_hits[0]
    return "guarded"


def row_key(q: int | str, r: int | str, word: int) -> str:
    return f"{q}/{r}/{word}"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def build_ledger(lean_path: Path | None) -> dict[str, Any]:
    aliases, excluded = alias_catalogue()
    assert aliases == EXPECTED_FAMILIES, (aliases, EXPECTED_FAMILIES)
    assert len(aliases) == 11
    assert len(excluded) == 10

    rows: list[tuple[int | str, int | str, int]] = []
    for q, r in aliases:
        for word in range(8):
            if orientation_is_compatible(q, r, word):
                rows.append((q, r, word))
    assert len(rows) == 70

    records = []
    counts: collections.Counter[str] = collections.Counter()
    for q, r, word in rows:
        cls = classify((q, r, word))
        counts[cls] += 1
        records.append({"id": row_key(q, r, word), "q": q, "r": r, "word": word, "class": cls})

    expected_counts = {"structural": 10, "unguarded": 24, "guarded": 22, "residual": 14}
    assert dict(counts) == expected_counts, (dict(counts), expected_counts)

    expected_guarded = {
        (12, NEW): {0, 1, 3, 4, 6, 7},
        (13, NEW): {0},
        (NEW, 6): {0, 1},
        (NEW, 11): {0, 1, 3, 6, 7},
        (NEW, 12): {0, 1, 6},
        (NEW, NEW): {0, 1, 3, 6, 7},
    }
    actual_guarded: dict[tuple[int | str, int | str], set[int]] = collections.defaultdict(set)
    for q, r, word in rows:
        if classify((q, r, word)) == "guarded":
            actual_guarded[(q, r)].add(word)
    assert dict(actual_guarded) == expected_guarded, (dict(actual_guarded), expected_guarded)

    compatible_words: dict[str, list[int]] = collections.defaultdict(list)
    for q, r, word in rows:
        compatible_words[f"{q}/{r}"].append(word)

    result: dict[str, Any] = {
        "format": "opg169-s16-cycle4-d19-ledger-v1",
        "verdict": "candidate_only",
        "frozen_main": "dc6ee891ed7614602e88d48a57314416082dd022",
        "source_blobs": {
            "c39_check": "43245a07727452f92fbec9c3d4a999ef7a797414",
            "c40_check": "ec5d3ffd99297c2a7d4693414466ac2fbeaefd12",
        },
        "bit_semantics": [
            "bit0: q->r else r->q",
            "bit1: r->8 else 8->r",
            "bit2: r->4 else 4->r",
        ],
        "fixed_arcs": ["5->q", "q->4"],
        "alias_initial": 21,
        "alias_excluded_count": len(excluded),
        "alias_excluded": excluded,
        "alias_surviving": [{"q": q, "r": r} for q, r in aliases],
        "compatible_direction_types": len(rows),
        "compatible_words": dict(compatible_words),
        "partition_counts": dict(counts),
        "partition_identity": "70 = 10 structural + 24 unguarded + 22 guarded + 14 residual",
        "rows": records,
        "guarded_rows": [rec["id"] for rec in records if rec["class"] == "guarded"],
        "residual_rows": [rec["id"] for rec in records if rec["class"] == "residual"],
        "unclosed_frontier": {
            "residual_rows": 14,
            "guard_failure_children": "all realizable failures of the concrete reverse-arc guards on the 22 guarded rows",
        },
        "claim_established": "finite D/19 row partition only",
        "claim_not_established": [
            "embedding-faithful StrictProfileReduction objects for every named selected rule",
            "closure of all residual rows",
            "closure of all failed-guard children",
            "global D/19 unavoidability in every minimal bad graph",
            "root theorem for the concrete plane-orientation contract",
        ],
    }
    if lean_path is not None:
        result["cycle4_lean"] = {
            "path": lean_path.name,
            "sha256": sha256(lean_path),
            "bytes": lean_path.stat().st_size,
            "lines": sum(1 for _ in lean_path.open("r", encoding="utf-8")),
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lean", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    ledger = build_ledger(args.lean)
    text = json.dumps(ledger, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "compatible": ledger["compatible_direction_types"],
        "partition": ledger["partition_counts"],
        "guarded": len(ledger["guarded_rows"]),
        "residual": len(ledger["residual_rows"]),
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
