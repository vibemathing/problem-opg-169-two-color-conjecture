"""C31 exact finite controls for semidegree-admissible planar core families.
Generator self-test, not a registered verifier. Reuses frozen C30 primitives.
"""
import hashlib
import importlib.util
import json
import itertools
import platform
import sys
from collections import deque
from pathlib import Path

D = Path('research/artifacts/candidates')
DEPENDENCY = D / 'opg169-a01-c30-dynamic-check.py'
DEPENDENCY_SHA = '0f3cd926f1e21939d4807c5a6a2310f5ab820023dc14a2d31bd7c7927e5db13b'
if hashlib.sha256(DEPENDENCY.read_bytes()).hexdigest() != DEPENDENCY_SHA:
    raise ValueError('frozen C30 dependency mismatch')
spec = importlib.util.spec_from_file_location('c30_frozen', DEPENDENCY)
c30 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c30)
need = c30.need


def family(L, split, reverse=False):
    need(L >= 4 and L % 2 == 0, 'even cycle order')
    need(not split or L >= 6, 'split hub semidegrees')
    ring = list(range(2, L + 2))
    b = L + 2
    A = set()
    for i, x in enumerate(ring):
        A.add((x, ring[(i + 1) % L]))
        A.add((x, 1) if i % 2 == 0 else (1, x))
        hubs = [0] if not split else ([0, b] if i in (0, 2) else [0] if i == 1 else [b])
        for p in hubs:
            A.add((p, x) if i % 2 == 0 else (x, p))
    R = {0: ring[:], 1: [ring[0]] + ring[:0:-1]}
    for i, x in enumerate(ring):
        R[x] = [0, ring[(i - 1) % L], 1, ring[(i + 1) % L]]
    if split:
        A.add((b, 0))
        R[0] = ring[:3] + [b]
        R[b] = [ring[0], 0] + ring[2:]
        R[ring[0]] = [0, b, ring[-1], 1, ring[1]]
        R[ring[2]] = [b, 0, ring[1], 1, ring[3]]
        for i in range(3, L):
            R[ring[i]][0] = b
    if reverse:
        A = {(y, x) for x, y in A}
    return tuple(sorted(R)), A, R, ring


def colouring(ring, k):
    # Poles 0[,b] have 0, pole 1 has 1; v=ring[0] is deleted.
    return (1 << 1) | sum(1 << x for i, x in enumerate(ring) if i > 0 and
                          ((int(i <= k) ^ (i % 2)) == 1))


def topo(A, V, c, k):
    left = {x for x in V if (c >> x) & 1 == k}
    result = []
    while left:
        zero = sorted(x for x in left if not any((y, x) in A for y in left))
        need(bool(zero), 'topological witness')
        result += zero
        left -= set(zero)
    return result


def analyze(L, split, reverse):
    V, A, R, ring = family(L, split, reverse)
    v, m = ring[0], L - 1
    B = tuple(R[v])
    H = tuple(x for x in V if x != v)
    ha = {(x, y) for x, y in A if x != v and y != v}
    faces = c30.check_rotation(V, A, R)
    hr = {x: [y for y in R[x] if y != v] for x in H}
    hfaces = c30.check_rotation(H, ha, hr)
    orders = {tuple(B[k:] + B[:k]) for k in range(len(B))}
    orders |= {x[::-1] for x in tuple(orders)}
    need(any(tuple(f) in orders for f in hfaces), 'boundary face cyclic order')
    need(all(len(f) == 3 for f in faces), 'full graph triangular faces')
    need(all(x != y and (y, x) not in A for x, y in A), 'simple orientation')
    degrees = {x: (sum(y == x for z, y in A), sum(z == x for z, y in A)) for x in V}
    need(all(min(p) >= 2 for p in degrees.values()), 'all graph semidegrees >=2')
    need(min(sum(p) for p in degrees.values()) == 4, 'graph minimum degree4')
    need(sum(degrees[v]) == (5 if split else 4), 'chosen degree')
    reach = c30.positive(ha, H)
    need(all(x == y or (x, y) in reach for x in H for y in H), 'strong deletion')
    ng = c30.positive(A, V)
    need(all(x == y or (x, y) in ng for x in V for y in V), 'strong graph')
    chi = sum(6 - sum(p) for p in degrees.values())
    need(chi == 12, 'Euler charge equality')
    samples = [colouring(ring, k) for k in range(1, m)]
    hs1 = c30.System(H, ha, B, 1)
    hs2 = c30.System(H, ha, B, 2)
    valid = set(hs1.states)
    need(all(c in valid for c in samples), 'monotone sample valid')
    sigma = samples[0] & c30.mask(B)
    same_boundary = {c for c in valid if c & c30.mask(B) == sigma}
    need(same_boundary == set(samples), 'exact fixed-boundary classification')
    labels = {hs1.labels[c] for c in samples}
    need(len(labels) == 1, 'full static state equality')
    need(len({hs1.ids[c] for c in samples}) == m - 1, 'radius1 distinctions')
    need(len({hs2.ids[c] for c in samples}) == m - 1, 'radius2 distinctions')
    goals_e = {c for c in samples if c ^ (1 << ring[1]) in valid}
    need(goals_e == {samples[0]}, 'first-port action enabled only at k1')
    dist_e, q = {c: 0 for c in goals_e}, deque(goals_e)
    while q:
        c = q.popleft()
        for d, s, j in hs1.edges[c]:
            if s == 0 and j == 1 and d not in dist_e:
                dist_e[d] = dist_e[c] + 1
                q.append(d)
    need([dist_e[c] for c in samples] == list(range(m - 1)), 'observable internal distances')
    gvalid = {c for c in c30.subsets(c30.mask(V)) if c30.valid(A, V, c)}
    goals = {c & hs1.full for c in gvalid}
    need(not set(samples) & goals, 'all fixed-boundary samples double blocked')
    full_witness = (1 << 1) | c30.mask(ring[1::2])
    need(full_witness in gvalid, 'full graph is colourable')
    if not split:
        need(len(valid) == 3 * 2 ** (L // 2) - 2 + 2 * L, 'base H total count')
        need(len(gvalid) == 2 ** (L // 2 + 2), 'base G total count')
    repair1, repair2 = hs1.distance(goals), hs2.distance(goals)
    need(all(c in repair1 and c in repair2 for c in samples), 'samples have a repair')
    if not split:
        expected1 = [min(k, m - k) for k in range(1, m)]
        expected2 = [1 + (max(0, d - 3) + 1) // 2 for d in expected1]
        need([repair1[c] for c in samples] == expected1, 'exact single-flip distances')
        need([repair2[c] for c in samples] == expected2, 'exact radius2 distances')
    else:
        need(all((c ^ 1) in goals for c in samples), 'split degree5 one-step repair at pole0')
        need([repair1[c] for c in samples] == [1] * (m - 1), 'degree5 sample distance1')
    controller = None
    if split:
        upper = {(0, 1), (1, ring[-1]), (0, ring[-1])}
        if reverse:
            upper = {(y, x) for x, y in upper}
        sigma_after = hs1.labels[samples[0] ^ 1][0]
        actual_returns = [set(hs1.labels[c ^ 1][1]) for c in samples]
        need(all(hs1.labels[c ^ 1][0] == sigma_after for c in samples), 'controller common target colours')
        need(all(r <= upper for r in actual_returns), 'controller upper relation')
        need(set().union(*actual_returns) == upper, 'controller exact relation envelope')
        pa = A - ha
        upper_label = (sigma_after, tuple(sorted(upper)))
        star_label = c30.static(pa, tuple(B) + (v,), B, samples[0] ^ 1)
        need(c30.compatible(upper_label, star_label, B), 'uniform restore with colour zero')
        same_pairs = [(x, y) for x, y in itertools.combinations(B, 2)
                      if ((samples[0] ^ 1) >> x) & 1 == ((samples[0] ^ 1) >> y) & 1]
        relation_count, accepted_count = 0, 0
        for options in itertools.product((0, 1, 2), repeat=len(same_pairs)):
            rel = set()
            for (x, y), opt in zip(same_pairs, options):
                if opt:
                    rel.add((x, y) if opt == 1 else (y, x))
            if not c30.dag(rel, B) or c30.positive(rel, B) != rel:
                continue
            relation_count += 1
            if c30.dag(upper | rel, B):
                accepted_count += 1
                need(all(c30.dag(r | rel, B) for r in actual_returns), 'one-sided exterior soundness')
        need(relation_count == 57, 'all post-colour strict boundary relations')
        controller = {'abstract_states': 2, 'boundary_action_vertex': 0, 'interior_cost': 0,
                      'target_boundary_colours': sigma_after, 'target_upper_relation': sorted(upper),
                      'root_star_colour': 0, 'abstract_exterior_relations_tested': relation_count,
                      'upper_compatible_relations': accepted_count, 'universal_sample_lift': True}
    sample_rows = []
    for k, c in enumerate(samples, 1):
        out_return, in_return = (ring[1], 0), (1, ring[-1])
        cyc0 = [v, ring[1], 0, v]
        cyc1 = [v, 1, ring[-1], v]
        if reverse:
            cyc0, cyc1 = cyc0[::-1], cyc1[::-1]
        for colour, cyc in ((0, cyc0), (1, cyc1)):
            cm = c | ((1 << v) if colour else 0)
            need(all((a, b) in A for a, b in zip(cyc, cyc[1:])), 'cycle directions')
            need(all((cm >> x) & 1 == colour for x in cyc), 'cycle colours')
        sample_rows.append({'k': k, 'ones_mask': c, 'internal_distance_to_first_port': dist_e[c],
                            'single_repair_distance': repair1[c], 'radius2_repair_distance': repair2[c]})
    return {'cycle_order': L, 'split': split, 'reversed': reverse, 'vertices': V,
            'arcs': sorted(A), 'rotation': R, 'faces': faces, 'deletion_faces': hfaces,
            'deleted_vertex': v, 'boundary_order': B, 'semidegrees_in_out': degrees,
            'strong_deletion': True, 'charge_sum': chi,
            'full_colouring_ones_mask': full_witness,
            'full_topological_orders': {str(k): topo(A, V, full_witness, k) for k in (0, 1)},
            'H_valid_colourings': len(valid), 'G_valid_colourings': len(gvalid),
            'extendible_H': len(goals), 'H_radius1': hs1.summary(), 'H_radius2': hs2.summary(),
            'fixed_boundary_static_state': next(iter(labels)), 'fixed_boundary_samples': sample_rows,
            'number_same_label_distinct_dynamic_classes': len(samples),
            'uniform_two_state_controller': controller,
            'blocking_cycles': [cyc0, cyc1]}


def main():
    raw = Path(sys.argv[1]).read_bytes()
    need(len(raw) < 65536, 'input size')
    data = json.loads(raw)
    need(data['cases'] == [[4, False, False], [6, False, False], [8, False, False],
                           [10, False, False], [8, False, True], [6, True, False],
                           [6, True, True], [8, True, False], [8, True, True]], 'frozen case allocation')
    out = {'verdict': 'candidate_only', 'trusted_verifier_receipt': False,
           'complete': False, 'runtime': platform.python_version(),
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': hashlib.sha256(raw).hexdigest(), 'dependency_sha256': DEPENDENCY_SHA}
    try:
        out['cases'] = [analyze(*args) for args in data['cases']]
        out['complete'] = True
        out['status'] = 'bounded_family_controls_passed'
        code = 0
    except (ValueError, KeyError, TypeError) as e:
        out['status'], out['error'] = 'candidate_mismatch', str(e)
        code = 1
    text = json.dumps(out, sort_keys=True)
    need(len(text.encode()) < 65536, 'output cap')
    print(text)
    return code


if __name__ == '__main__':
    sys.exit(main())
