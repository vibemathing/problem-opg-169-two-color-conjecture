"""R08 bounded exhaustive checker candidate. Execution: pending/unverified.
No third-party dependencies. This program does not sign mathematical receipts.
Default exhaustive range: all labelled orientations on 0..4 vertices.
An explicit --max-order 5 also includes nonplanar graphs; only local lemmas
and SCC gluing are tested, never a claimed planar-root classification.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Graph:
    n: int
    arcs: frozenset[tuple[int, int]]

    def basic_check(self) -> None:
        if not 0 <= self.n <= 5:
            raise ValueError("order outside bounded checker")
        if any(not (0 <= a < self.n and 0 <= b < self.n)
               for a, b in self.arcs):
            raise ValueError("arc endpoint outside vertex set")

    def oriented(self) -> bool:
        return all(a != b and (b, a) not in self.arcs for a, b in self.arcs)

    @property
    def full(self) -> int:
        return (1 << self.n) - 1


class Mismatch(Exception):
    def __init__(self, test: str, detail: dict):
        self.test, self.detail = test, detail


def need(condition: bool, test: str, **detail) -> None:
    if not condition:
        raise Mismatch(test, detail)


def vertices(mask: int, n: int) -> list[int]:
    return [v for v in range(n) if mask & (1 << v)]


def submasks(mask: int) -> Iterable[int]:
    x = mask
    while True:
        yield x
        if x == 0:
            return
        x = (x - 1) & mask


def acyclic_kahn(g: Graph, mask: int) -> bool:
    """Full induced arcs only; loops and digons are correctly cyclic."""
    left = set(vertices(mask, g.n))
    while left:
        removable = [v for v in left
                     if not any((u, v) in g.arcs for u in left)]
        if not removable:
            return False
        left.difference_update(removable)
    return True


def simple_cycle(g: Graph, mask: int) -> tuple[int, ...] | None:
    """Separate oracle: enumerate positive simple cycles, including 1 and 2."""
    vs = vertices(mask, g.n)
    for length in range(1, len(vs) + 1):
        for seq in itertools.permutations(vs, length):
            # Only rotation duplicates are removed, never direction reversals.
            if seq[0] != min(seq):
                continue
            if all((seq[j], seq[(j + 1) % length]) in g.arcs
                   for j in range(length)):
                return seq + (seq[0],)
    return None


def reachable(g: Graph, mask: int, start: int, end: int) -> bool:
    if not (mask & (1 << start) and mask & (1 << end)):
        return False
    # This reflexive relation is for paths, not the cycle oracle.
    seen, frontier = {start}, [start]
    while frontier:
        x = frontier.pop()
        if x == end:
            return True
        for y in vertices(mask, g.n):
            if (x, y) in g.arcs and y not in seen:
                seen.add(y)
                frontier.append(y)
    return False


def scc_masks(g: Graph) -> list[int]:
    left = set(range(g.n))
    parts = []
    while left:
        root = min(left)
        comp = {v for v in left
                if reachable(g, g.full, root, v)
                and reachable(g, g.full, v, root)}
        parts.append(sum(1 << v for v in comp))
        left.difference_update(comp)
    return parts


def two_good(g: Graph, mask: int, ones: int) -> bool:
    if ones & ~mask:
        raise ValueError("color class outside its vertex domain")
    return acyclic_kahn(g, ones) and acyclic_kahn(g, mask ^ ones)


def predicted_blocked(g: Graph, v: int, ones: int, k: int) -> bool:
    """Return-path side, distinct from both direct cycle decision engines."""
    h = g.full ^ (1 << v)
    color = ones if k == 1 else h ^ ones
    incoming = [i for i in vertices(color, g.n) if (i, v) in g.arcs]
    outgoing = [o for o in vertices(color, g.n) if (v, o) in g.arcs]
    return any(reachable(g, color, o, i)
               for i in incoming for o in outgoing)


def checked_safe(g: Graph, v: int, ones: int) -> list[int]:
    """Reject out-of-domain graphs and invalid deletion colorings explicitly."""
    g.basic_check()
    if not g.oriented():
        raise ValueError("not a simple orientation")
    if not 0 <= v < g.n:
        raise ValueError("missing deleted vertex")
    h = g.full ^ (1 << v)
    if not two_good(g, h, ones):
        raise ValueError("invalid deletion coloring")
    return [k for k in (0, 1)
            if two_good(g, g.full, ones | ((1 << v) if k else 0))]


def graph_stream(n: int) -> Iterable[Graph]:
    pairs = list(itertools.combinations(range(n), 2))
    for states in itertools.product((0, 1, 2), repeat=len(pairs)):
        arcs = []
        for (a, b), state in zip(pairs, states):
            if state == 1:
                arcs.append((a, b))
            elif state == 2:
                arcs.append((b, a))
        yield Graph(n, frozenset(arcs))


def run_fixtures(data: dict, tick) -> dict:
    need(data["execution_status"] == "pending/unverified", "fixture status")
    covered = []
    for f in data["fixtures"]:
        tick()
        raw = [tuple(e) for e in f["arcs"]]
        need(len(raw) == len(set(raw)), "duplicate fixture arcs", fixture=f["id"])
        g = Graph(f["n"], frozenset(raw))
        g.basic_check()
        need(g.oriented() == f["expected_orientation"], "fixture domain",
             fixture=f["id"])
        for s in submasks(g.full):
            need(acyclic_kahn(g, s) == (simple_cycle(g, s) is None),
                 "fixture cycle engines", fixture=f["id"], subset=s)
        parts = scc_masks(g)
        need(len(parts) == f["expected_sccs"], "fixture SCCs", fixture=f["id"])
        if f["deleted_vertex"] is None:
            ones = sum(1 << x for x in f["ones"])
            need(two_good(g, g.full, ones) == f["expected_full_valid"],
                 "fixture full coloring", fixture=f["id"])
        else:
            v = f["deleted_vertex"]
            h = g.full ^ (1 << v)
            ones = sum(1 << x for x in f["ones"])
            valid = two_good(g, h, ones)
            need(valid == f["expected_deleted_valid"], "fixture deletion",
                 fixture=f["id"])
            direct = [k for k in (0, 1)
                      if two_good(g, g.full, ones | ((1 << v) if k else 0))]
            need(direct == f["expected_safe"], "fixture extensions",
                 fixture=f["id"], actual=direct)
            rejected = False
            try:
                accepted = checked_safe(g, v, ones)
            except ValueError:
                rejected = True
            should_reject = not g.oriented() or not valid
            need(rejected == should_reject, "fixture input rejection",
                 fixture=f["id"])
            if not rejected:
                need(accepted == direct, "fixture checked answers", fixture=f["id"])
                for k in (0, 1):
                    need(predicted_blocked(g, v, ones, k) == (k not in direct),
                         "fixture path iff", fixture=f["id"], color=k)
        if "full_coloring_ones" in f:
            full_ones = sum(1 << x for x in f["full_coloring_ones"])
            need(two_good(g, g.full, full_ones), "fixture full witness",
                 fixture=f["id"])
        if "expected_valid_assignments" in f:
            count = sum(two_good(g, g.full, s) for s in submasks(g.full))
            need(count == f["expected_valid_assignments"], "fixture partitions",
                 fixture=f["id"], actual=count)
        covered.append(f["id"])

    # Deliberately wrong semantics are killed by explicit minimal controls.
    singleton = Graph(1, frozenset())
    need(reachable(singleton, 1, 0, 0) and simple_cycle(singleton, 1) is None,
         "kill length-zero-is-cycle mutant")
    triangle = Graph(3, frozenset({(1, 0), (0, 2), (2, 1)}))
    selected = Graph(3, frozenset({(1, 0), (0, 2)}))
    need(two_good(selected, 7, 0) and not two_good(triangle, 7, 0),
         "kill noninduced-arc mutant")
    need(all(two_good(triangle, 1 << x, 0) for x in range(3))
         and not two_good(triangle, 7, 0) and len(scc_masks(triangle)) == 1,
         "kill omitted-SCC mutant")
    need(not predicted_blocked(selected, 0, 0, 0)
         and (1, 0) in selected.arcs and (0, 2) in selected.arcs,
         "kill neighbor-only blocker mutant")
    bidir = Graph(3, frozenset((a, b) for a in range(3)
                             for b in range(3) if a != b))
    need(all(sum((x, v) in bidir.arcs for x in range(3)) == 2
             and sum((v, x) in bidir.arcs for x in range(3)) == 2
             and sum(((x, v) in bidir.arcs or (v, x) in bidir.arcs)
                     for x in range(3)) == 2 for v in range(3)),
         "kill overlapping-neighbors-addition mutant")
    return {"fixture_ids": covered, "semantic_mutants_killed": 5}


def exhaustive(max_order: int, report: dict, tick) -> None:
    for n in range(max_order + 1):
        row = {"n": n, "graphs": 0, "full_colorings": 0,
               "deletion_colorings": 0, "valid_deletion_colorings": 0,
               "invalid_deletion_colorings": 0, "extensions_tested": 0,
               "small_semidegree_cases": 0, "both_blocked_cases": 0}
        report["orders"].append(row)
        for index, g in enumerate(graph_stream(n)):
            tick()
            report["cursor"] = {"n": n, "graph_index": index}
            g.basic_check()
            need(g.oriented(), "generator domain", **report["cursor"])
            dag = {}
            for mask in submasks(g.full):
                left = acyclic_kahn(g, mask)
                right = simple_cycle(g, mask) is None
                need(left == right, "cycle engines", **report["cursor"], subset=mask)
                dag[mask] = left
            parts = scc_masks(g)
            union = 0
            for comp in parts:
                need(comp != 0 and union & comp == 0, "SCC partition",
                     **report["cursor"])
                union |= comp
            need(union == g.full, "SCC coverage", **report["cursor"])
            owner = {v: j for j, comp in enumerate(parts)
                     for v in vertices(comp, n)}
            quotient = Graph(len(parts), frozenset(
                (owner[a], owner[b]) for a, b in g.arcs if owner[a] != owner[b]))
            need(acyclic_kahn(quotient, quotient.full), "condensation DAG",
                 **report["cursor"])
            for ones in submasks(g.full):
                full_valid = dag[ones] and dag[g.full ^ ones]
                local_valid = all(dag[ones & s] and dag[s ^ (ones & s)]
                                  for s in parts)
                need(full_valid == local_valid, "SCC gluing all assignments",
                     **report["cursor"], ones=ones)
                row["full_colorings"] += 1
            for v in range(n):
                h = g.full ^ (1 << v)
                incoming = {x for x in range(n) if (x, v) in g.arcs}
                outgoing = {x for x in range(n) if (v, x) in g.arcs}
                need(not incoming & outgoing, "disjoint sides", **report["cursor"])
                for ones in submasks(h):
                    tick()
                    report["cursor"] = {"n": n, "graph_index": index,
                                        "v": v, "ones": ones}
                    row["deletion_colorings"] += 1
                    if not (dag[ones] and dag[h ^ ones]):
                        row["invalid_deletion_colorings"] += 1
                        continue
                    row["valid_deletion_colorings"] += 1
                    safe = []
                    for k in (0, 1):
                        one = ones | ((1 << v) if k else 0)
                        direct = dag[one] and dag[g.full ^ one]
                        need(predicted_blocked(g, v, ones, k) == (not direct),
                             "return-path iff", **report["cursor"], color=k,
                             arcs=sorted(g.arcs))
                        if direct:
                            safe.append(k)
                        row["extensions_tested"] += 1
                    small = len(incoming) <= 1 or len(outgoing) <= 1
                    if small:
                        row["small_semidegree_cases"] += 1
                        need(bool(safe), "small-semidegree extension",
                             **report["cursor"], arcs=sorted(g.arcs))
                    if not safe:
                        row["both_blocked_cases"] += 1
                        need(len(incoming) >= 2 and len(outgoing) >= 2
                             and len(incoming | outgoing) >= 4,
                             "two-color witnesses", **report["cursor"],
                             arcs=sorted(g.arcs))
            row["graphs"] += 1
        expected = 3 ** (n * (n - 1) // 2)
        need(row["graphs"] == expected, "complete graph count", n=n)
        need(row["full_colorings"] == expected * (2 ** n),
             "complete full-color count", n=n)
        deletion_total = expected * n * (2 ** (n - 1)) if n else 0
        need(row["deletion_colorings"] == deletion_total,
             "complete deletion-color count", n=n)
        need(row["valid_deletion_colorings"] + row["invalid_deletion_colorings"]
             == row["deletion_colorings"], "deletion partition", n=n)
    report["cursor"] = None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-order", type=int, choices=range(0, 6), default=4)
    parser.add_argument("--seconds", type=int, choices=range(1, 301), default=100)
    parser.add_argument("--fixtures", type=Path, default=Path(__file__).with_name(
        "opg169-a01-degree4-mutations-20260907.json"))
    args = parser.parse_args()
    start = time.monotonic()
    report = {"verdict": "candidate_only", "complete": False, "status": "running",
              "max_order": args.max_order, "orders": [], "cursor": None,
              "runtime": {"implementation": platform.python_implementation(),
                          "version": platform.python_version()},
              "scope": "all labelled orientations; local extension and SCC only"}
    def tick():
        if time.monotonic() - start > args.seconds:
            raise TimeoutError
    try:
        raw = args.fixtures.read_bytes()
        if len(raw) > 65536:
            raise ValueError("fixture file exceeds bound")
        report["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        report["fixtures_sha256"] = hashlib.sha256(raw).hexdigest()
        report["mutations"] = run_fixtures(json.loads(raw), tick)
        exhaustive(args.max_order, report, tick)
        report["complete"], report["status"] = True, "bounded_checks_passed"
        code = 0
    except TimeoutError:
        report["status"] = "incomplete_timeout"
        code = 2
    except Mismatch as error:
        report["status"] = "mismatch_candidate_requires_review"
        report["failure"] = {"test": error.test, "detail": error.detail}
        code = 1
    except (ValueError, KeyError, TypeError, OSError) as error:
        report["status"] = "input_or_runtime_error"
        report["error_type"] = type(error).__name__
        code = 3
    report["elapsed_seconds"] = round(time.monotonic() - start, 6)
    output = json.dumps(report, ensure_ascii=True, sort_keys=True)
    if len(output.encode()) > 65536:
        output = '{"complete":false,"status":"output_limit","verdict":"candidate_only"}'
        code = 3
    print(output)
    return code


if __name__ == "__main__":
    sys.exit(main())
