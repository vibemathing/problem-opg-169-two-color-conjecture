"""Exact bounded candidate checker. No admission or trusted receipt authority.
Run from a frozen repository-shaped workspace under the recorded limits.
"""
import hashlib
import json
import platform
import sys
from collections import deque
from pathlib import Path


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def bitset(items):
    return sum(1 << x for x in items)


def dag_kahn(A, V):
    V = set(V)
    while V:
        zero = {x for x in V if not any((y, x) in A for y in V)}
        if not zero:
            return False
        V -= zero
    return True


def dag_dfs(A, V):
    V = set(V)
    mark = {x: 0 for x in V}
    def visit(x):
        mark[x] = 1
        for y in V:
            if (x, y) in A:
                if mark[y] == 1 or (mark[y] == 0 and not visit(y)):
                    return False
        mark[x] = 2
        return True
    return all(mark[x] != 0 or visit(x) for x in V)


def good(A, V, ones):
    for k in (0, 1):
        S = {x for x in V if ((ones >> x) & 1) == k}
        a, b = dag_kahn(A, S), dag_dfs(A, S)
        need(a == b, 'cycle-engine disagreement')
        if not a:
            return False
    return True


def reach(A, V, x, y, positive=False):
    V = set(V)
    if x not in V or y not in V:
        return False
    todo = [z for z in V if (x, z) in A] if positive else [x]
    seen = set()
    while todo:
        z = todo.pop()
        if z == y:
            return True
        if z not in seen:
            seen.add(z)
            todo += [w for w in V if (z, w) in A and w not in seen]
    return False


def scc(A, V):
    left = set(V)
    parts = []
    while left:
        x = min(left)
        S = {y for y in left if reach(A, V, x, y) and reach(A, V, y, x)}
        need(bool(S), 'empty SCC')
        parts.append(S)
        left -= S
    return parts


def state(A, V, B, ones):
    sigma = tuple((ones >> x) & 1 for x in B)
    R = set()
    for x in B:
        S = {z for z in V if ((ones >> z) & 1) == ((ones >> x) & 1)}
        for y in B:
            if reach(A, S, x, y, positive=True):
                R.add((x, y))
    return sigma, R


def faces(rotation, A):
    edges = {tuple(sorted(e)) for e in A}
    darts = {(x, y) for x, y in edges} | {(y, x) for x, y in edges}
    need(set(rotation) == {x for x, y in darts}, 'rotation vertex set')
    for x, ns in rotation.items():
        need(len(ns) == len(set(ns)), 'rotation duplicates')
        need(set(ns) == {y for a, y in darts if a == x}, 'rotation neighbours')
    seen, fs = set(), []
    for start in sorted(darts):
        if start in seen:
            continue
        d, f = start, []
        while d not in seen:
            seen.add(d)
            x, y = d
            f.append(x)
            ns = rotation[y]
            d = (y, ns[(ns.index(x) + 1) % len(ns)])
        need(d == start, 'face permutation collision')
        fs.append(f)
    need(seen == darts, 'dart coverage')
    # Edge-connectedness plus an oriented rotation system and Euler 2
    # gives a connected spherical map, not merely a drawing guess.
    todo, covered = [min(rotation)], set()
    while todo:
        x = todo.pop()
        if x not in covered:
            covered.add(x)
            todo += rotation[x]
    need(covered == set(rotation), 'map connectedness')
    need(len(rotation) - len(edges) + len(fs) == 2, 'sphere Euler')
    return fs


def topological(A, vertices, order):
    need(set(vertices) == set(order) and len(vertices) == len(order), 'order coverage')
    pos = {x: i for i, x in enumerate(order)}
    need(all(pos[x] < pos[y] for x, y in A if x in pos and y in pos), 'order arcs')


def cycle(A, V, ones, seq):
    need(len(seq) >= 4 and seq[0] == seq[-1], 'positive cycle')
    need(len(set(seq[:-1])) == len(seq) - 1, 'simple cycle')
    need(set(seq).issubset(V), 'cycle domain')
    need(all((x, y) in A for x, y in zip(seq, seq[1:])), 'cycle arcs')
    need(len({(ones >> x) & 1 for x in seq}) == 1, 'cycle monochromatic')


def pair_prediction(A, V, ones, x, y):
    need(((ones >> x) & 1) != ((ones >> y) & 1), 'opposite colours required')
    for z in (x, y):
        new_colour = 1 - ((ones >> z) & 1)
        S = {w for w in V - {x, y} if ((ones >> w) & 1) == new_colour}
        I = {i for i in S if (i, z) in A}
        O = {o for o in S if (z, o) in A}
        if any(reach(A, S, o, i) for i in I for o in O):
            return False
    return True


def verify(c):
    V = set(c['vertices'])
    v = c['deleted_vertex']
    H = V - {v}
    B = c['boundary']
    A = {tuple(e) for e in c['H_arcs']}
    Av = {tuple(e) for e in c['v_arcs']}
    G = A | Av
    need(len(A) == len(c['H_arcs']) and len(G) == 21, 'all arcs / duplicates')
    need(all(x != y and (y, x) not in G for x, y in G), 'simple orientation')
    need(all(x in H and y in H for x, y in A), 'H is induced deletion')
    need({x if y == v else y for x, y in Av} == set(B), 'all v neighbours')
    need(all(v in e for e in Av), 'v arcs')
    rot = {int(k): vs for k, vs in c['rotation'].items()}
    fg = faces(rot, G)
    rh = {x: [y for y in vs if y != v] for x, vs in rot.items() if x != v}
    fh = faces(rh, A)
    need(len(fg) == c['expected']['G_faces'] and all(len(f) == 3 for f in fg), 'G faces')
    need(len(fh) == c['expected']['H_faces'], 'H faces')
    need(any(len(f) == 4 and any(f == B[k:]+B[:k] or f == (B[k:]+B[:k])[::-1]
                               for k in range(4)) for f in fh), 'boundary face')
    degrees = {x: (sum(y == x for y, z in G), sum(z == x for y, z in G)) for x in V}
    need(all(min(d) >= 2 for d in degrees.values()), 'semidegrees')
    need(min(sum(d) for d in degrees.values()) == 4, 'minimum degree')
    need(len(scc(A, H)) == 1 and len(scc(G, V)) == 1, 'strong connectivity')
    initial = bitset(c['initial_ones'])
    need(good(A, H, initial), 'initial valid')
    for k in (0, 1):
        S = {x for x in H if ((initial >> x) & 1) == k}
        topological(A, S, c['H_topological_orders'][str(k)])
    for x in H:
        flipped = initial ^ (1 << x)
        need(not good(A, H, flipped), 'frozen vertex')
        cycle(A, H, flipped, c['single_flip_cycles'][str(x)])
    for k in (0, 1):
        extended = initial | (k << v)
        need(not good(G, V, extended), 'v blocked')
        cycle(G, V, extended, c['v_blocking_cycles'][str(k)])
    initial_state = state(A, H, B, initial)
    need(initial_state == (tuple(c['boundary_colours']),
                           {tuple(e) for e in c['boundary_positive_returns']}), 'boundary state')
    valid = {mask for mask in range(1 << v) if good(A, H, mask)}
    gvalid = [mask for mask in range(1 << len(V)) if good(G, V, mask)]
    extend = {mask for mask in valid if any(good(G, V, mask | (k << v)) for k in (0, 1))}
    need(len(valid) == c['expected']['H_valid_colourings'], 'H count')
    need(len(gvalid) == c['expected']['G_valid_colourings'], 'G count')
    need(len(extend) == c['expected']['H_extendible_colourings'], 'extendible count')
    todo = set(valid)
    sizes = []
    components = []
    while todo:
        q, comp = [min(todo)], set()
        while q:
            m = q.pop()
            if m in comp:
                continue
            comp.add(m)
            q += [m ^ (1 << x) for x in H if m ^ (1 << x) in valid and m ^ (1 << x) not in comp]
        todo -= comp
        sizes.append(len(comp))
        components.append(sorted(comp))
    need(sorted(sizes) == c['expected']['H_single_flip_component_sizes'], 'component counts')
    frozen = sorted(mask for mask in valid if all(mask ^ (1 << x) not in valid for x in H))
    need(frozen == c['expected']['H_frozen_masks'], 'frozen masks')
    orbit, q = set(), [initial]
    while q:
        m = q.pop()
        if m in orbit:
            continue
        orbit.add(m)
        q += [m ^ (1 << x) for x in H if m ^ (1 << x) in valid and m ^ (1 << x) not in orbit]
        q += [m ^ bitset(S) for S in scc(A, H) if m ^ bitset(S) not in orbit]
    need(sorted(orbit) == c['expected']['initial_orbit_single_plus_whole_SCC'], 'SCC augmented orbit')
    need(not orbit & extend, 'no reachable extension')
    distance = min((mask ^ initial).bit_count() for mask in extend)
    need(distance == c['expected']['minimum_flip_distance_to_extendible'], 'minimum batch distance')
    other = bitset(c['same_boundary_state_other_ones'])
    need(other in valid and state(A, H, B, other) == initial_state, 'same static state')
    moved = other ^ (1 << c['other_state_legal_flip'])
    need(moved in extend and moved in valid, 'other representative escapes')
    full = bitset(c['full_G_valid_ones'])
    need(full in gvalid, 'G NOT counterexample')
    for k in (0, 1):
        S = {x for x in V if ((full >> x) & 1) == k}
        topological(G, S, c['full_G_topological_orders'][str(k)])
    pair_tests = 0
    for mask in valid:
        for x in H:
            for y in H:
                if x < y and ((mask >> x) & 1) != ((mask >> y) & 1):
                    pred = pair_prediction(A, H, mask, x, y)
                    direct = mask ^ (1 << x) ^ (1 << y) in valid
                    need(pred == direct, 'pair criterion')
                    pair_tests += 1
    pair = c['simultaneous_escape_pair']
    swapped = initial ^ bitset(pair)
    need(swapped in extend and pair_prediction(A, H, initial, *pair), 'pair escape')
    composition_tests = 0
    accepted = 0
    # Piece P is only the embedded v-star; F is H. Interiors are disjoint.
    for mask in valid:
        _, rf = state(A, H, B, mask)
        for k in (0, 1):
            full_mask = mask | (k << v)
            need(good(Av, set(B) | {v}, full_mask), 'star acyclic')
            _, rp = state(Av, set(B) | {v}, B, full_mask)
            predicted = dag_kahn(rf | rp, B)
            actual = good(G, V, full_mask)
            need(predicted == actual, 'positive-boundary composition')
            composition_tests += 1
            accepted += int(predicted)
    return {'H_valid_colourings': len(valid), 'G_valid_colourings': len(gvalid),
            'H_extendible_colourings': len(extend), 'single_flip_components': components,
            'single_flip_component_sizes': sorted(sizes), 'frozen_masks': frozen,
            'single_plus_SCC_orbit': sorted(orbit), 'minimum_batch_distance': distance,
            'same_state_other_mask': other, 'other_after_one_flip': moved,
            'pair_escape_mask': swapped, 'pair_criterion_cases': pair_tests,
            'composition_cases': composition_tests, 'composition_accepted': accepted,
            'G_faces': fg, 'H_faces': fh,
            'G_semidegrees_out_in': {str(x): list(d) for x, d in degrees.items()},
            'same_boundary_state_masks': sorted(m for m in valid if state(A, H, B, m) == initial_state)}


def main():
    path = Path(sys.argv[1])
    raw = path.read_bytes()
    need(len(raw) <= 65536, 'input size')
    report = {'verdict':'candidate_only', 'record_kind':'generator_finite_check',
              'registered_verifier_receipt': False, 'complete':False,
              'runtime':platform.python_version(),
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256':hashlib.sha256(raw).hexdigest()}
    try:
        report['results'] = verify(json.loads(raw))
        report['complete'] = True
        report['status'] = 'finite_patch_checks_passed'
        code = 0
    except (AssertionError, ValueError, KeyError, TypeError) as exc:
        report['status'] = 'candidate_mismatch'
        report['error'] = str(exc)
        code = 1
    out = json.dumps(report, sort_keys=True)
    need(len(out.encode()) <= 65536, 'output bound')
    print(out)
    return code


if __name__ == '__main__':
    sys.exit(main())
