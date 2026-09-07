"""Bounded C28 patch tests. Candidate self-checks, not a trusted verifier.
All rotations, arcs and colorings are explicit. No third-party imports.
Print one JSON summary; emit the exact 276-state table to the requested file.
"""
import argparse
import hashlib
import itertools as it
import json
import platform
import time
from collections import deque
from pathlib import Path


def need(ok, label):
    if not ok:
        raise ValueError(label)


def vs(mask, n):
    return [x for x in range(n) if mask >> x & 1]


def reach(n, arcs, mask):
    r = [0] * n
    for a, b in arcs:
        if mask >> a & 1 and mask >> b & 1:
            r[a] |= 1 << b
    for k in vs(mask, n):
        for i in vs(mask, n):
            if r[i] >> k & 1:
                r[i] |= r[k]
    return r


def dag(n, arcs, mask):
    left = set(vs(mask, n))
    while left:
        remove = {b for b in left if not any((a, b) in arcs for a in left)}
        if not remove:
            return False
        left -= remove
    return True


def good(n, arcs, mask, ones):
    need(not ones & ~mask, 'color domain')
    return dag(n, arcs, ones) and dag(n, arcs, mask ^ ones)


def scc(n, arcs, mask):
    r = reach(n, arcs, mask)
    left = set(vs(mask, n)); parts = []
    while left:
        x = min(left)
        part = {y for y in left if x == y or (r[x] >> y & 1 and r[y] >> x & 1)}
        parts.append(sum(1 << y for y in part)); left -= part
    return parts


def extensions(n, arcs, v, ones):
    return [k for k in (0, 1) if good(n, arcs, (1 << n) - 1, ones | (k << v))]


def faces(rotation, arcs):
    n = len(rotation)
    edges = {tuple(sorted((a, b))) for a, b in arcs}
    need(all(a != b and (b, a) not in arcs for a, b in arcs), 'orientation')
    for x in range(n):
        neighbors = {b if a == x else a for a, b in edges if x in (a, b)}
        need(set(rotation[x]) == neighbors and len(rotation[x]) == len(neighbors), 'rotation')
    connected = {0}; pending = [0]
    while pending:
        for y in rotation[pending.pop()]:
            if y not in connected:
                connected.add(y); pending.append(y)
    need(len(connected) == n, 'connected map')
    unseen = {(a, b) for a, b in edges} | {(b, a) for a, b in edges}
    result = []
    while unseen:
        start = min(unseen); d = start; walk = []
        while True:
            need(d in unseen, 'dart permutation')
            unseen.remove(d); walk.append(d[0])
            a, b = d; rot = rotation[b]
            d = (b, rot[(rot.index(a) + 1) % len(rot)])
            if d == start:
                break
        result.append(walk)
    need(n - len(edges) + len(result) == 2, 'not a sphere rotation')
    return result


def signature(n, arcs, boundary, ones):
    r = []
    for k in (0, 1):
        mask = ones if k else ((1 << n) - 1) ^ ones
        q = reach(n, arcs, mask)
        r.append([[a, b] for a in boundary for b in boundary if q[a] >> b & 1])
    return {'ones': [x for x in boundary if ones >> x & 1], 'relations': r}


def boundary_states(tick):
    rows = ['incoming_mask,one_mask,return_arcs,safe_colors']
    state_count = 0; blocked = []; incidence = {}
    for one in range(16):
        if one.bit_count() != 2:
            continue
        pairs = [tuple(vs(one, 4)), tuple(vs(15 ^ one, 4))]
        for choices in it.product(range(3), repeat=2):
            ret = set()
            for (a, b), t in zip(pairs, choices):
                if t:
                    ret.add((a, b) if t == 1 else (b, a))
            # Different-color disjoint terminal pairs interlace exactly here.
            if one in (5, 10) and len(ret) == 2:
                continue
            state_count += 1
            for incoming in range(16):
                if incoming.bit_count() != 2:
                    continue
                tick()
                star = {(x, 4) if incoming >> x & 1 else (4, x) for x in range(4)}
                arcs = ret | star
                rot = {4: [0, 1, 2, 3]}
                for x in range(4):
                    rot[x] = [4] + sorted({b if a == x else a for a, b in ret if x in (a, b)})
                faces(rot, arcs)
                safe = extensions(5, arcs, 4, one)
                predicted = []
                for k in (0, 1):
                    fail = any(not (incoming >> a & 1) and incoming >> b & 1
                               and (one >> a & 1) == k for a, b in ret)
                    if not fail:
                        predicted.append(k)
                need(safe == predicted, 'boundary introduction')
                rows.append(f'{incoming},{one},' + ';'.join(f'{a}>{b}' for a,b in sorted(ret))
                            + ',' + ''.join(map(str, safe)))
                if not safe:
                    item = {'incoming_mask': incoming, 'one_mask': one, 'return_arcs': sorted(ret)}
                    blocked.append(item); incidence[str(incoming)] = incidence.get(str(incoming), 0) + 1
    need(state_count == 46 and len(rows) == 277 and len(blocked) == 16, 'state totals')
    return '\n'.join(rows) + '\n', {'exterior_states': state_count, 'signed_states': len(rows)-1,
            'both_blocked': len(blocked), 'blocked_by_incoming_mask': incidence, 'blocked_states': blocked}


def orders_on(points):
    pairs = list(it.combinations(points, 2))
    result = []
    for choices in it.product(range(3), repeat=len(pairs)):
        r = set()
        for (x,y), k in zip(pairs, choices):
            if k:
                r.add((x,y) if k == 1 else (y,x))
        if all((x,z) in r for x,y in r for w,z in r if y == w):
            result.append(r)
    return result


def interlace(a,b,c,d,n):
    if len({a,b,c,d}) != 4:
        return False
    return (0 < (c-a)%n < (b-a)%n) != (0 < (d-a)%n < (b-a)%n)


def degree_five_states(tick):
    digest = hashlib.sha256(); profiles = 0; signed = 0; blocked = 0
    by_incoming = {}; first = None
    need(len(orders_on([0,1,2])) == 19, 'three-terminal partial orders')
    for one in range(32):
        if one.bit_count() not in (2,3):
            continue
        for r0 in orders_on(vs(31^one,5)):
            for r1 in orders_on(vs(one,5)):
                if any(interlace(a,b,c,d,5) for a,b in r0 for c,d in r1):
                    continue
                profiles += 1; relation = r0 | r1
                covers = {(a,b) for a,b in relation
                          if not any((a,c) in relation and (c,b) in relation for c in range(5))}
                for incoming in range(32):
                    if incoming.bit_count() not in (2,3):
                        continue
                    tick(); signed += 1
                    arcs = covers | {(x,5) if incoming>>x&1 else (5,x) for x in range(5)}
                    rot = {5:list(range(5))}
                    for x in range(5):
                        neighbors = {b if a==x else a for a,b in covers if x in (a,b)}
                        rot[x] = [5] + sorted(neighbors,key=lambda y:(x-y)%5)
                    faces(rot,arcs)
                    need(good(6,covers,31,one),'profile witness valid')
                    got = signature(6,covers,list(range(5)),one)['relations']
                    need({tuple(e) for color in got for e in color} == relation,'Hasse realization')
                    safe = extensions(6,arcs,5,one)
                    pred = [k for k in (0,1) if not any(not(incoming>>a&1) and incoming>>b&1
                                                       and (one>>a&1)==k for a,b in relation)]
                    need(safe==pred,'degree-five introduction')
                    row=f'{incoming},{one},'+ ';'.join(f'{a}>{b}' for a,b in sorted(relation))+','+''.join(map(str,safe))+'\n'
                    digest.update(row.encode())
                    if not safe:
                        blocked += 1; by_incoming[str(incoming)]=by_incoming.get(str(incoming),0)+1
                        if first is None:
                            first={'incoming_mask':incoming,'one_mask':one,'relations':sorted(relation),
                                   'exterior_cover_arcs':sorted(covers),'rotation':rot}
    return {'color_splits':[2,3],'abstract_profiles_before_planarity_filter':1140,
            'disk_realizable_profiles':profiles,'signed_states':signed,'both_blocked':blocked,
            'blocked_by_incoming_mask':by_incoming,'first_blocked_state':first,
            'streamed_table_sha256':digest.hexdigest(),
            'table_storage':'rows streamed into digest; regeneration defined in source, no separate table file claimed'}


def recoloring_distances(n, arcs, v):
    h = ((1 << n) - 1) ^ (1 << v)
    valid = {s for s in range(1 << n) if not s & ~h and good(n, arcs, h, s)}
    dist = {s: 0 for s in valid if extensions(n, arcs, v, s)}
    queue = deque(dist)
    while queue:
        s = queue.popleft()
        for x in vs(h, n):
            t = s ^ (1 << x)
            if t in valid and t not in dist:
                dist[t] = dist[s] + 1; queue.append(t)
    return valid, dist


def orbit_test(n, arcs, v, old):
    h = ((1 << n) - 1) ^ (1 << v); parts = scc(n, arcs, h)
    orbit = {old}
    for part in parts:
        orbit |= {c ^ part for c in list(orbit)}
    need(all(good(n, arcs, h, c) for c in orbit), 'SCC palette swap')
    valid, distances = recoloring_distances(n, arcs, v)
    return {'scc_masks': parts, 'orbit': [{'ones_mask': c, 'safe': extensions(n, arcs, v, c)}
            for c in sorted(orbit)], 'single_vertex_escape_distance': distances.get(old),
            'safe_neighbor_flips': [x for x in vs(h, n) if old ^ (1 << x) in valid
                                    and extensions(n, arcs, v, old ^ (1 << x))]}


def test_fixtures(tick):
    # C02 oriented octahedron: 0=v, 1=w, 2=a, 3=b, 4=c, 5=d.
    octa = {(0,2),(2,3),(3,0),(0,4),(4,5),(5,0),(3,4),(5,2),(2,1),(4,1),(1,3),(1,5)}
    rot = {0:[2,3,4,5],1:[2,5,4,3],2:[0,5,1,3],3:[0,2,1,4],4:[0,3,1,5],5:[0,4,1,2]}
    fs = faces(rot, octa); old = 48; h = 62
    for mask in range(64):
        q = reach(6, octa, mask)
        need(dag(6, octa, mask) == all(not (q[x] >> x & 1) for x in range(6)), 'two cycle oracles')
    need(all(sum(b==x for a,b in octa)==2 and sum(a==x for a,b in octa)==2 for x in range(6)), 'semidegrees')
    need(not extensions(6, octa, 0, old), 'double block')
    orbit = orbit_test(6, octa, 0, old)
    need(len(orbit['orbit']) == 2 and all(not x['safe'] for x in orbit['orbit']), 'orbit obstruction')
    need(orbit['single_vertex_escape_distance'] == 1, 'do not overclaim recoloring failure')
    fixed = [{'w_color': k, 'ones_mask': old | (k << 1), 'safe': extensions(6,octa,0,old | (k << 1))}
             for k in (0,1)]
    need(all(not x['safe'] and good(6,octa,h,x['ones_mask']) for x in fixed), 'fixed rim fiber')
    oct_report = {'arcs':sorted(octa),'rotation':rot,'faces':fs,'old_ones_mask':old,
                  'orbit_certificate':orbit,'fixed_rim_cases':fixed,
                  'boundary_signature':signature(6,octa-set(e for e in octa if 0 in e),[2,3,4,5],old),
                  'full_coloring_ones_mask':40}
    need(good(6,octa,63,40), 'full octa coloring')
    # A genuinely two-SCC deleted graph with a blocked initial coloring.
    two = {(1,2),(2,3),(3,1),(4,5),(5,6),(6,4),(1,0),(2,0),(0,4),(0,5),(4,1),(5,2)}
    rt = {1:[2,4,0,3],2:[1,3,0,5],3:[2,1],4:[0,1,5,6],5:[4,2,0,6],6:[5,4],0:[2,1,4,5]}
    ff = faces(rt,two); old2=36
    need(good(7,two,126,old2) and not extensions(7,two,0,old2), 'two SCC witness')
    o2=orbit_test(7,two,0,old2)
    need(any(x['safe'] for x in o2['orbit']), 'two SCC resolution')
    parts=scc(7,two,126); count=0
    for c in range(128):
        if c & 1 or not good(7,two,126,c):
            continue
        tick(); count += 1
        need(bool(extensions(7,two,0,c)) or any(extensions(7,two,0,c^p) for p in parts), 'one swap lemma fixture')
    return {'octahedron':oct_report,'two_scc_fixture':{'arcs':sorted(two),'rotation':rt,'faces':ff,
            'old_ones_mask':old2,'orbit_certificate':o2,'valid_deletion_colorings_tested':count}}


def all_balanced_octahedra(tick):
    edges=[(a,b) for a in range(6) for b in range(a+1,6) if {a,b} not in ({0,1},{2,4},{3,5})]
    totals={'underlying_orientations':0,'semidegree_two_orientations':0,'valid_deletion_colorings':0,
            'both_blocked_colorings':0,'scc_noncore_cases':0,'max_single_flip_distance':0,'unreachable':0}
    for dirs in it.product((0,1),repeat=12):
        tick();totals['underlying_orientations']+=1
        arcs={e if d else (e[1],e[0]) for e,d in zip(edges,dirs)}
        if not all(sum(a==v for a,b in arcs)==2 for v in range(6)):
            continue
        totals['semidegree_two_orientations']+=1
        need(any(good(6,arcs,63,c) for c in range(64)), 'octa colorability')
        for v in range(6):
            valid,dist=recoloring_distances(6,arcs,v)
            h=63^(1<<v); parts=scc(6,arcs,h)
            neighbors={x for e in arcs if v in e for x in e if x!=v}
            core=any(all(p>>x&1 for x in neighbors) for p in parts)
            for c in valid:
                totals['valid_deletion_colorings']+=1
                if not extensions(6,arcs,v,c):
                    totals['both_blocked_colorings']+=1
                if not core:
                    totals['scc_noncore_cases']+=1
                    need(bool(extensions(6,arcs,v,c)) or any(extensions(6,arcs,v,c^p) for p in parts),'one swap lemma')
                if c not in dist:
                    totals['unreachable']+=1
                else:
                    totals['max_single_flip_distance']=max(totals['max_single_flip_distance'],dist[c])
    return totals


def cycle_witness(n, arcs, mask):
    points=vs(mask,n)
    for length in range(1,len(points)+1):
        for seq in it.permutations(points,length):
            if seq[0]==min(seq) and all((seq[j],seq[(j+1)%length]) in arcs for j in range(length)):
                return list(seq)+(list(seq[:1]))
    return None


def pentagonal_bipyramid(tick):
    ring=list(range(2,7))
    edges=[(a,x) for a in (0,1) for x in ring]+[(ring[j],ring[(j+1)%5]) for j in range(5)]
    totals={'underlying_orientations':0,'semidegree_admissible':0,'degree4_blocked':0,
            'degree4_one_step_failures':0,'degree4_max_recolor_distance':0,
            'degree5_blocked':0,'degree5_max_recolor_distance':0,'unreachable':0}
    for bits in it.product((0,1),repeat=15):
        tick();totals['underlying_orientations']+=1
        arcs={e if b else e[::-1] for e,b in zip(edges,bits)}
        if not all(sum(a==x for a,b in arcs)>=2 and sum(b==x for a,b in arcs)>=2 for x in range(7)):
            continue
        totals['semidegree_admissible']+=1
        for v in range(7):
            valid,dist=recoloring_distances(7,arcs,v)
            key='degree4' if v in ring else 'degree5'
            for c in valid:
                if c not in dist:
                    totals['unreachable']+=1
                else:
                    totals[key+'_max_recolor_distance']=max(totals[key+'_max_recolor_distance'],dist[c])
                if not extensions(7,arcs,v,c):
                    totals[key+'_blocked']+=1
                    if v in ring and (c not in dist or dist[c]>1):
                        totals['degree4_one_step_failures']+=1
    arcs={(0,4),(0,6),(1,2),(1,3),(1,5),(2,0),(2,6),(3,0),(3,2),(4,1),(4,3),(5,0),(5,4),(6,1),(6,5)}
    rot={0:ring,1:[2,6,5,4,3]}
    for j,x in enumerate(ring):
        rot[x]=[0,ring[(j-1)%5],1,ring[(j+1)%5]]
    fs=faces(rot,arcs);v=5;old=22;h=95
    need(good(7,arcs,h,old) and not extensions(7,arcs,v,old),'selected blocked coloring')
    moves=[]
    for x in vs(h,7):
        c=old^(1<<x);valid=good(7,arcs,h,c)
        row={'flipped_vertex':x,'ones_mask':c,'valid_deletion':valid,'safe':extensions(7,arcs,v,c)}
        if not valid:
            row['old_graph_monochromatic_cycle']=next(cyc for mask in (c,h^c)
                        if (cyc:=cycle_witness(7,arcs,mask)) is not None)
        else:
            row['restoration_cycles']=[cycle_witness(7,arcs,(127^(c|(k<<v))) if k==0 else (c|(1<<v))) for k in (0,1)]
        need(not row['safe'],'one-step obstruction')
        moves.append(row)
    sequence=[22,18,19]
    need(all(good(7,arcs,h,c) for c in sequence),'valid two-step sequence')
    need(extensions(7,arcs,v,19)==[0],'two-step escape')
    totals['selected_witness']={'arcs':sorted(arcs),'rotation':rot,'faces':fs,'v':v,
        'old_ones_mask':old,'scc_masks':scc(7,arcs,h),'all_six_single_flip_cases':moves,
        'escape_flip_vertices':[2,0],'escape_ones_masks':sequence,'safe_after_escape':[0]}
    return totals


def gluing_test(tick):
    cases=bad=0
    for one in range(16):
        if one.bit_count()!=2:
            continue
        states=[]
        for r0 in orders_on(vs(15^one,4)):
            for r1 in orders_on(vs(one,4)):
                if not any(interlace(a,b,c,d,4) for a,b in r0 for c,d in r1):
                    states.append(r0|r1)
        for left in states:
            for right in states:
                tick();n=4;arcs=set();colors=one
                for relation in (left,right):
                    for a,b in sorted(relation):
                        arcs|={(a,n),(n,b)}
                        if one>>a&1:
                            colors|=1<<n
                        n+=1
                direct=good(n,arcs,(1<<n)-1,colors)
                predicted=dag(4,left|right,15)
                need(direct==predicted,'gluing subdivided paths')
                cases+=1;bad+=not direct
    need(cases==374,'gluing coverage')
    return {'compatible_boundary_color_state_pairs':cases,'cyclic_unions':bad,
            'witness':'each piece arc subdivided by its own fresh vertex; no boundary digons introduced'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--table-out',type=Path,required=True);a=p.parse_args()
    start=time.monotonic()
    def tick():
        if time.monotonic()-start>60:
            raise TimeoutError('bounded patch checks')
    table,states=boundary_states(tick)
    need(len(table.encode())<65536,'table cap')
    a.table_out.write_text(table,encoding='utf-8')
    report={'verdict':'candidate_only','trusted_verifier_receipt':False,'complete':False,
            'runtime':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'degree_five_states':degree_five_states(tick),'boundary_states':states,'table_sha256':hashlib.sha256(table.encode()).hexdigest(),
            'gluing':gluing_test(tick),'pentagonal_bipyramid':pentagonal_bipyramid(tick),'fixtures':test_fixtures(tick),'balanced_octahedra':all_balanced_octahedra(tick)}
    report['complete']=True;report['elapsed_seconds']=round(time.monotonic()-start,6)
    text=json.dumps(report,sort_keys=True)
    need(len(text.encode())<65536,'summary cap');print(text)


if __name__=='__main__':
    main()
