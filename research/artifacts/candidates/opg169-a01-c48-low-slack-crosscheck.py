#!/usr/bin/env python3
"""Independent-formula cross-check for C48; candidate-only.

This file does not import the enumerator.  It checks the finite-cell count,
the sharp cyclic-gap bound by closed formulas and constructed witnesses, and
the critical two-sector quotient edge counts.
"""
from __future__ import annotations
import json
import platform


def qgraph(edges, vertices, mapping):
    v = {mapping.get(x, x) for x in vertices}
    e = set()
    for a, b in edges:
        a, b = mapping.get(a, a), mapping.get(b, b)
        assert a != b
        e.add(tuple(sorted((a, b))))
    return len(v), len(e)


def main():
    count_by_s = []
    cells = []
    for s in range(6):
        lo = max(0, 4 - s)
        ts = list(range(lo, 6))
        count_by_s.append(len(ts))
        cells.extend((s, t, 3*t+s) for t in ts)
    assert count_by_s == [2,3,4,5,6,6]
    assert len(cells) == 26

    sharp_rows = []
    for t in range(6, 101):
        for s in range(6):
            # s gaps of size 2 and the rest of size 1 is a sharp witness.
            gaps = tuple([2]*s + [1]*(t-s))
            assert len(gaps) == t
            assert sum(gaps) == t+s
            singletons = gaps.count(1)
            assert singletons == t-s >= 1
            sharp_rows.append((t,s,singletons))

    vertices={"p","H0","H","H2","u0","v0","u1","v1","q0","q1"}
    edges=set()
    def sector(q,L,R,u,v):
        for a,b in [
            ("p",L),("p",u),("p",v),("p",R),
            (L,u),(u,v),(v,R),(q,L),(q,u),(q,v),(q,R)
        ]:
            edges.add(tuple(sorted((a,b))))
    sector("q0","H0","H","u0","v0")
    sector("q1","H","H2","u1","v1")
    assert (len(vertices),len(edges))==(10,21)
    aliases={
        "distinct":{},
        "q0=H2":{"q0":"H2"},
        "q1=H0":{"q1":"H0"},
        "both":{"q0":"H2","q1":"H0"},
        "common_q":{"q0":"q","q1":"q"},
    }
    counts={name:qgraph(edges,vertices,m) for name,m in aliases.items()}
    assert counts=={
        "distinct":(10,21),
        "q0=H2":(9,21),
        "q1=H0":(9,21),
        "both":(8,20),
        "common_q":(9,20),
    }
    assert counts["both"][1] > 3*counts["both"][0]-6

    print(json.dumps({
        "format":"opg169-c48-low-slack-crosscheck-v1",
        "verdict":"candidate_only",
        "python":platform.python_version(),
        "finite_cell_count":26,
        "finite_cell_count_by_s":count_by_s,
        "sharp_formula_rows_checked":len(sharp_rows),
        "sharp_formula_range":{"t_min":6,"t_max":100,"s_min":0,"s_max":5},
        "alias_quotient_counts":counts,
        "normalized_singleton_parent_count":3*8*8,
        "independent_trust_domain":False,
        "root_closed":False,
    },sort_keys=True,separators=(",",":")))


if __name__=="__main__":
    main()
