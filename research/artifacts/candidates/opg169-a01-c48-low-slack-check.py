#!/usr/bin/env python3
"""Bounded exact checks for the C48 live-frontier cut.

Candidate-only.  The universal arguments are in the accompanying proof:
this program pressure-tests the integer normal form, the 26-cell finite
branch, and the cyclic-gap singleton bound.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import platform
import sys
from fractions import Fraction
from typing import Iterator, Tuple


def compositions(total: int, parts: int) -> Iterator[Tuple[int, ...]]:
    """All positive ordered compositions of total into `parts` parts."""
    if parts <= 0:
        return
    for cuts in itertools.combinations(range(1, total), parts - 1):
        points = (0,) + cuts + (total,)
        yield tuple(points[i + 1] - points[i] for i in range(parts))


def gamma(t: int, s: int) -> Fraction:
    d = 3 * t + s
    assert d > 0
    return Fraction(t + s - 4, d)


def allowed(t: int, s: int) -> bool:
    if t < 0 or s < 0:
        return False
    d = 3 * t + s
    return d >= max(3 * t, 2 * t + 4)



def quotient_graph(edges, vertices, mapping):
    qverts = {mapping.get(v, v) for v in vertices}
    qedges = set()
    loops = []
    for a, b in edges:
        x, y = mapping.get(a, a), mapping.get(b, b)
        if x == y:
            loops.append((x, y))
        else:
            qedges.add(frozenset((x, y)))
    return qverts, qedges, loops


def singleton_sector_geometry():
    """Critical alias audit for two marked sectors separated by one high port."""
    vertices = {"p", "H0", "H", "H2", "u0", "v0", "u1", "v1", "q0", "q1"}
    edges = set()

    def add_sector(p, q, left, right, u, v):
        for a, b in [
            (p, left), (p, u), (p, v), (p, right),
            (left, u), (u, v), (v, right),
            (q, left), (q, u), (q, v), (q, right),
        ]:
            edges.add(tuple(sorted((a, b))))

    add_sector("p", "q0", "H0", "H", "u0", "v0")
    add_sector("p", "q1", "H", "H2", "u1", "v1")
    assert len(vertices) == 10 and len(edges) == 21
    assert 21 == 3 * 10 - 9  # triangulated disk with outer length six

    low_degrees = {
        v: sum(v in e for e in edges)
        for v in ("u0", "v0", "u1", "v1")
    }
    assert set(low_degrees.values()) == {4}

    # q0=q1 closes all four actual wedges at H:
    # p-v0-q-u1-p.  The endpoint would have degree four, contradicting
    # the inherited endpoint lower bound d(H)>=5.
    common_map = {"q0": "q", "q1": "q"}
    qv, qe, loops = quotient_graph(edges, vertices, common_map)
    assert not loops and len(qv) == 9 and len(qe) == 20
    h_neighbours = {
        next(iter(e - {"H"})) for e in qe if "H" in e
    }
    assert h_neighbours == {"p", "v0", "q", "u1"}

    rows = []
    for name, mapping, expected in [
        ("distinct", {}, "survives"),
        ("q0_equals_H2", {"q0": "H2"}, "survives"),
        ("q1_equals_H0", {"q1": "H0"}, "survives"),
        (
            "both_opposite_endpoint_aliases",
            {"q0": "H2", "q1": "H0"},
            "planar_edge_bound",
        ),
        ("q0_equals_q1", common_map, "closed_high_link"),
    ]:
        qv, qe, loops = quotient_graph(edges, vertices, mapping)
        if name == "both_opposite_endpoint_aliases":
            assert len(qv) == 8 and len(qe) == 20 and len(qe) > 3 * len(qv) - 6
        if name == "q0_equals_q1":
            assert len(h_neighbours) == 4
        rows.append(
            {
                "case": name,
                "vertices": len(qv),
                "edges": len(qe),
                "simple_planar_upper_bound": 3 * len(qv) - 6,
                "status": expected,
            }
        )

    return {
        "base_vertices": 10,
        "base_edges": 21,
        "outer_boundary_length": 6,
        "saturated_low_degrees": low_degrees,
        "critical_alias_rows": rows,
        "surviving_local_interfaces": [
            "six_distinct_outer_ports",
            "q0=H2: two triangular exterior regions sharing H2",
            "q1=H0: two triangular exterior regions sharing H0",
        ],
        "direction_count_from_frozen_sector_dependency": {
            "sector_types_at_fixed_donor_sign": 8,
            "two_sector_types_per_surviving_interface": 64,
            "surviving_interfaces": 3,
            "normalized_total": 192,
            "scope": (
                "The factor 8 is imported from the frozen C32/C34 residual-sector "
                "candidate.  This checker audits the geometry and multiplication, "
                "not that upstream direction catalogue independently."
            ),
        },
    }

def main() -> None:
    finite_cells = []
    for s in range(6):
        for t in range(6):
            if not allowed(t, s):
                continue
            d = 3 * t + s
            g = gamma(t, s)
            g_alt = Fraction(1, 3) + Fraction(2 * (s - 6), 3 * d)
            assert g == g_alt
            finite_cells.append(
                {
                    "s": s,
                    "t": t,
                    "d": d,
                    "gamma": f"{g.numerator}/{g.denominator}",
                    "singleton_lower_bound_if_t_positive": max(0, t - s),
                }
            )

    assert len(finite_cells) == 26
    assert [sum(1 for c in finite_cells if c["s"] == s) for s in range(6)] == [
        2, 3, 4, 5, 6, 6
    ]

    gap_checks = []
    total_compositions = 0
    for t in range(1, 13):
        for s in range(6):
            if not allowed(t, s):
                continue
            total = t + s
            seen = 0
            min_singletons = t
            sharp_witness = None
            for gaps in compositions(total, t):
                seen += 1
                singleton_count = sum(g == 1 for g in gaps)
                excess = sum(g - 1 for g in gaps)
                assert excess == s
                assert singleton_count >= max(0, t - s)
                if sharp_witness is None or singleton_count < min_singletons:
                    min_singletons = singleton_count
                    sharp_witness = gaps
            total_compositions += seen
            assert seen > 0
            expected = max(0, t - s)
            assert min_singletons == expected
            gap_checks.append(
                {
                    "t": t,
                    "s": s,
                    "compositions": seen,
                    "minimum_singleton_gaps": min_singletons,
                    "sharp_witness": list(sharp_witness),
                }
            )

    # Pressure-test the universal implication:
    # an unpaid negative triangle must have a low-slack corner s <= 5.
    corners = []
    for t in range(13):
        for s in range(13):
            if allowed(t, s):
                corners.append((t, s, gamma(t, s)))
    negative_triples = 0
    checked_triples = 0
    for i, a in enumerate(corners):
        for j in range(i, len(corners)):
            b = corners[j]
            for k in range(j, len(corners)):
                c = corners[k]
                checked_triples += 1
                if a[2] + b[2] + c[2] < 1:
                    negative_triples += 1
                    assert min(a[1], b[1], c[1]) <= 5

    # Boundary attacks: the singleton conclusion cannot be strengthened
    # from "at least one" to "at least two".
    sharp_high_branch = next(
        row for row in gap_checks if row["t"] == 6 and row["s"] == 5
    )
    assert sharp_high_branch["minimum_singleton_gaps"] == 1

    geometry = singleton_sector_geometry()

    output = {
        "format": "opg169-c48-low-slack-cut-v1",
        "verdict": "candidate_only",
        "python": platform.python_version(),
        "finite_low_t_cells": finite_cells,
        "finite_cell_count": len(finite_cells),
        "finite_cell_count_by_s": [2, 3, 4, 5, 6, 6],
        "gap_parameter_range": {"t_min": 1, "t_max": 12, "s_min": 0, "s_max": 5},
        "gap_rows": len(gap_checks),
        "gap_compositions_checked": total_compositions,
        "bounded_face_triples_checked": checked_triples,
        "bounded_negative_face_triples": negative_triples,
        "sharp_high_branch_witness": sharp_high_branch,
        "singleton_two_sector_geometry": geometry,
        "universal_claims_checked_symbolically_in_proof": [
            "d=3t+s and d>=max(3t,2t+4) iff s>=0 and t+s>=4",
            "gamma=(t+s-4)/(3t+s)=1/3+2(s-6)/(3d)",
            "negative unpaid triangle implies at least one corner has s<=5",
            "cyclic pair blocks with positive gaps have sum(g_i-1)=s",
            "singleton-gap count is at least t-s",
        ],
        "scope_limit": (
            "The enumeration is a bounded pressure test.  It does not prove "
            "that a singleton gap has an octahedral-shell/cap geometry, that "
            "the 26 cells are reducible, or that every negative face maps to "
            "a previously verified local parent."
        ),
        "root_closed": False,
    }
    raw = json.dumps(output, sort_keys=True, separators=(",", ":")) + "\n"
    sys.stdout.write(raw)


if __name__ == "__main__":
    main()
