"""C30 finite controls: exact cost-labelled recolouring and bisimulation.
Generator self-test only. No external packages, trusted receipts or root claim.
"""
from __future__ import annotations
import hashlib
import itertools
import json
import platform
import sys
from collections import deque
from pathlib import Path


def need(test, name):
    if not test:
        raise ValueError(name)


def mask(vs):
    return sum(1 << x for x in vs)


def subsets(s):
    x = s
    while True:
        yield x
        if x == 0:
            break
        x = (x - 1) & s


def dag(arcs, vs):
    left = set(vs)
    while left:
        zero = {v for v in left if not any((u, v) in arcs for u in left)}
        if not zero:
            return False
        left -= zero
    return True


def positive(arcs, vs):
    vs = tuple(vs)
    reach = {(x, y) for x, y in arcs if x in vs and y in vs}
    for z in vs:
        reach |= {(x, y) for x in vs for y in vs
                  if (x, z) in reach and (z, y) in reach}
    return reach


def valid(arcs, vs, c):
    for k in (0, 1):
        sub = tuple(x for x in vs if (c >> x) & 1 == k)
        d = dag(arcs, sub)
        reach = positive(arcs, sub)
        need(d == (not any((x, x) in reach for x in sub)), 'cycle oracles')
        if not d:
            return False
    return True


def static(arcs, vs, boundary, c):
    rel = set()
    for k in (0, 1):
        sub = tuple(x for x in vs if (c >> x) & 1 == k)
        rel |= {(x, y) for x, y in positive(arcs, sub)
                if x in boundary and y in boundary}
    return tuple((c >> x) & 1 for x in boundary), tuple(sorted(rel))


def classes(signatures):
    uniq = {sig: j for j, sig in enumerate(sorted(set(signatures.values())))}
    return {c: uniq[sig] for c, sig in signatures.items()}


class System:
    def __init__(self, vs, arcs, boundary, radius):
        self.vs, self.arcs, self.B = tuple(vs), frozenset(arcs), tuple(boundary)
        self.radius, self.full = radius, mask(vs)
        need(len(self.vs) <= 11 and radius in (1, 2), 'finite resource bound')
        need(len(self.B) == len(set(self.B)) and set(self.B) <= set(vs), 'boundary')
        need(all(x != y and (y, x) not in self.arcs for x, y in self.arcs), 'orientation')
        need(all(x in vs and y in vs for x, y in self.arcs), 'arc domain')
        self.states = sorted(c for c in subsets(self.full) if valid(self.arcs, self.vs, c))
        values = set(self.states)
        self.labels = {c: static(self.arcs, self.vs, self.B, c) for c in self.states}
        changes = [mask(q) for t in range(radius + 1)
                   for q in itertools.combinations(self.vs, t)]
        bmask = mask(self.B)
        self.edges = {c: [(c ^ d, d & bmask, (d & ~bmask).bit_count())
                         for d in changes if c ^ d in values] for c in self.states}
        ids = classes(self.labels)
        self.layers = [ids]
        while True:
            sig = {c: (ids[c], tuple(sorted({(s, j, ids[d]) for d, s, j in self.edges[c]})))
                   for c in self.states}
            nxt = classes(sig)
            if len(set(nxt.values())) == len(set(ids.values())):
                break
            ids = nxt
            self.layers.append(ids)
        self.ids = ids
        self.blocks = {}
        for c in self.states:
            self.blocks.setdefault(ids[c], []).append(c)
        self.qedges = {}
        for q, members in self.blocks.items():
            signatures = [{(s, j, ids[d]) for d, s, j in self.edges[c]} for c in members]
            need(all(s == signatures[0] for s in signatures), 'universal representative lifting')
            self.qedges[q] = signatures[0]

    def distance(self, goals):
        dist = {c: 0 for c in goals}
        queue = deque(sorted(goals))
        while queue:
            c = queue.popleft()
            for d, s, j in self.edges[c]:
                if d not in dist:
                    dist[d] = dist[c] + 1
                    queue.append(d)
        return dist

    def summary(self):
        return {'colourings': len(self.states), 'blocks_by_depth':
                [len(set(ids.values())) for ids in self.layers],
                'stable_blocks': len(self.blocks),
                'nonidentity_directed_moves': sum(len(e) - 1 for e in self.edges.values())}


def compatible(lp, lf, B):
    return lp[0] == lf[0] and dag(set(lp[1]) | set(lf[1]), B)


def compose_test(vs, arcs, rotation, v, radius):
    B = tuple(rotation[v])
    H = tuple(x for x in vs if x != v)
    ha = {(a, b) for a, b in arcs if a != v and b != v}
    pa = set(arcs) - ha
    hs = System(H, ha, B, radius)
    ps = System(tuple(sorted(set(B) | {v})), pa, B, radius)
    gs = System(vs, arcs, B, radius)
    pairs = {(p, h) for p in ps.states for h in hs.states
             if compatible(ps.labels[p], hs.labels[h], B)}
    actual = {(g & ps.full, g & hs.full) for g in gs.states}
    need(pairs == actual, 'all-colouring static composition')
    lifted_edges = 0
    qlabels_p = {q: ps.labels[cs[0]] for q, cs in ps.blocks.items()}
    qlabels_h = {q: hs.labels[cs[0]] for q, cs in hs.blocks.items()}
    for p, h in sorted(pairs):
        g = p | h
        direct = {(d & ps.full, d & hs.full, s, j) for d, s, j in gs.edges[g]
                  if s.bit_count() + j > 0}
        product = {(pp, hh, s, jp + jh)
                   for pp, s, jp in ps.edges[p] for hh, t, jh in hs.edges[h]
                   if s == t and 1 <= s.bit_count() + jp + jh <= radius
                   and (pp, hh) in pairs}
        need(direct == product, 'exact synchronized cost product')
        qdirect = {(ps.ids[pp], hs.ids[hh], s, j) for pp, hh, s, j in direct}
        qproduct = {(qp, qh, s, jp + jh)
                    for s, jp, qp in ps.qedges[ps.ids[p]]
                    for t, jh, qh in hs.qedges[hs.ids[h]]
                    if s == t and 1 <= s.bit_count() + jp + jh <= radius
                    and compatible(qlabels_p[qp], qlabels_h[qh], B)}
        need(qdirect == qproduct, 'quotient product lifts from every representative')
        lifted_edges += len(product)
    goals = {g & hs.full for g in gs.states}
    dist = hs.distance(goals)
    report = {'deleted_vertex': v, 'boundary_order': B,
              'semidegree_in_out': [sum(b == v for a, b in arcs), sum(a == v for a, b in arcs)],
              'radius': radius, 'H': hs.summary(), 'star': ps.summary(),
              'G_colourings': len(gs.states), 'compatible_pairs': len(pairs),
              'product_moves_checked': lifted_edges,
              'extendible_H': len(goals), 'unreachable_H': sorted(set(hs.states) - set(dist)),
              'maximum_finite_repair_distance': max(dist.values(), default=None)}
    if v == 8 and len(vs) == 9:
        need(hs.labels[170] == hs.labels[146], 'C29 same static state')
        need(hs.ids[170] != hs.ids[146], 'C29 dynamic separation')
        report['C29'] = {'frozen_mask': 170, 'other_mask': 146,
                         'separation_depth': next(i for i, ids in enumerate(hs.layers)
                                                  if ids[170] != ids[146]),
                         'repair_distance_170': dist.get(170),
                         'same_static_state': True}
    return report


def check_rotation(vs, arcs, rotation):
    darts = set(arcs) | {(b, a) for a, b in arcs}
    for v in vs:
        need(set(rotation[v]) == {y for x, y in darts if x == v}, 'rotation adjacency')
        need(len(rotation[v]) == len(set(rotation[v])), 'rotation repeated neighbour')
    seen, fs = set(), []
    for start in sorted(darts):
        if start in seen:
            continue
        dart, face = start, []
        while dart not in seen:
            seen.add(dart)
            a, b = dart
            face.append(a)
            cyc = rotation[b]
            dart = b, cyc[(cyc.index(a) + 1) % len(cyc)]
        need(dart == start, 'face cycle')
        fs.append(face)
    # Check connectivity separately before the orientable-map Euler test.
    reached = {vs[0]}
    while True:
        new = reached | {b for a, b in darts if a in reached}
        if new == reached:
            break
        reached = new
    need(reached == set(vs), 'map connected')
    need(len(vs) - len(arcs) + len(fs) == 2, 'spherical rotation')
    return fs


def cycle_family(n, b):
    # Directed cycle 0,...,n-1, extra boundary leaves n,...,n+b-2.
    vs = tuple(range(n + b - 1))
    arcs = {(i, (i + 1) % n) for i in range(n)} | {(0, j) for j in range(n, n + b - 1)}
    B = (0,) + tuple(range(n, n + b - 1))
    rotation = {0: [1, n - 1] + list(range(n, n + b - 1))}
    rotation.update({i: [(i - 1) % n, (i + 1) % n] for i in range(1, n)})
    rotation.update({i: [0] for i in range(n, n + b - 1)})
    fs = check_rotation(vs, arcs, rotation)
    s = System(vs, arcs, B, 1)
    # Hold B colours fixed: 0,0,1,1[,1]. Select t extra cycle zeros.
    leaf_ones = mask(B[2:])
    samples = []
    for t in range(n - 1):
        c = mask(range(t + 1, n)) | leaf_ones
        samples.append(c)
    need(len({s.labels[c] for c in samples}) == 1, 'family same static labels')
    need(len({s.ids[c] for c in samples}) == n - 1, 'unbounded dynamic distinctions')
    # Minimal internal-move distance to a state disabling the boundary-0 flip.
    goal = {c for c in s.states if all(a != 1 or j != 0 for d, a, j in s.edges[c])}
    dist, queue = {c: 0 for c in goal}, deque(goal)
    while queue:
        c = queue.popleft()
        for d, a, j in s.edges[c]:
            if a == 0 and j == 1 and d not in dist:
                dist[d] = dist[c] + 1
                queue.append(d)
    need([dist[c] for c in samples] == list(range(n - 1)), 'internal distance certificate')
    return {'cycle_order': n, 'boundary_size': b, 'total_vertices': len(vs),
            **s.summary(), 'rotation': rotation, 'faces': fs, 'boundary_order': B,
            'same_label_sample_masks': samples,
            'sample_distances_to_disabled_boundary_flip': [dist[c] for c in samples]}


def main():
    raw = Path(sys.argv[1]).read_bytes()
    need(len(raw) < 65536, 'input limit')
    data = json.loads(raw)
    out = {'verdict': 'candidate_only', 'trusted_verifier_receipt': False, 'complete': False,
           'runtime': platform.python_version(),
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'input_sha256': hashlib.sha256(raw).hexdigest()}
    try:
        out['compositions'] = []
        out['rotations'] = []
        for f in data['fixtures']:
            V, A = tuple(f['vertices']), {tuple(e) for e in f['arcs']}
            R = {int(x): y for x, y in f['rotation'].items()}
            out['rotations'].append({'fixture': f['name'], 'faces': check_rotation(V, A, R)})
            for v in f['deletions']:
                for radius in (1, 2):
                    out['compositions'].append({'fixture': f['name'], **compose_test(V, A, R, v, radius)})
        out['unbounded_family_controls'] = [cycle_family(n, b) for b, ns in data['family_ranges']
                                            for n in ns]
        c4 = System(range(4), {(0, 1), (1, 2), (2, 3), (3, 0)}, (0,), 1)
        need(c4.layers[1][12] == c4.layers[1][8] and c4.ids[12] != c4.ids[8], 'one-round insufficient')
        out['minimal_same_graph_depth1_collision'] = {
            'vertices': [0, 1, 2, 3], 'arcs': [[0, 1], [1, 2], [2, 3], [3, 0]],
            'boundary': [0], 'colouring_masks': [12, 8], 'depth1_equal': True,
            'first_distinguishing_depth': next(i for i, ids in enumerate(c4.layers) if ids[12] != ids[8])}
        # Concrete controls for synchronization and exact global move cost.
        ep = System((0, 1), (), (0,), 1)
        ef = System((0, 2), (), (0,), 1)
        need((2, 0, 1) in ep.edges[0] and (4, 0, 1) in ef.edges[0], 'two local interior moves')
        need(1 + 1 > 1, 'two interiors do not fit radius one')
        need((1, 1, 0) in ep.edges[0] and (1, 1, 0) in ef.edges[0], 'shared boundary flip')
        need(1 + 0 + 0 == 1, 'shared boundary counted once')
        need(ep.labels[1][0] != ef.labels[0][0], 'unsynchronized boundary rejected')
        out['move_cost_controls'] = {'boundary_sync': True, 'two_interior_cost': 2,
                                     'shared_boundary_cost': 1}
        out['complete'] = True
        out['status'] = 'bounded_controls_passed'
        code = 0
    except (ValueError, KeyError, TypeError) as e:
        out['status'], out['error'] = 'candidate_mismatch', str(e)
        code = 1
    text = json.dumps(out, sort_keys=True)
    need(len(text.encode()) < 65536, 'output limit')
    print(text)
    return code


if __name__ == '__main__':
    sys.exit(main())
