"""Exact finite C32 controls. Generator-only, no mathematical admission.
Full induced arcs, two cycle engines, rational charges and explicit rotations.
Run with the separately archived bounded wrapper from a repository-shaped root.
"""
import hashlib
import itertools as it
import json
import platform
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def need(ok, text):
    if not ok:
        raise ValueError(text)


def closure(A, V):
    V = set(V)
    R = {(x, y) for x, y in A if x in V and y in V}
    for z in sorted(V):
        R |= {(x, y) for x in V for y in V if (x, z) in R and (z, y) in R}
    return R


def dag(A, V):
    left = set(V)
    while left:
        zero = {v for v in left if not any((u, v) in A for u in left)}
        if not zero:
            return False
        left -= zero
    return True


def state(A, V, B, ones):
    R = set()
    ok = True
    for k in (0, 1):
        S = {x for x in V if (ones >> x) & 1 == k}
        r = closure(A, S)
        a = dag(A, S)
        need(a == (not any(x == y for x, y in r)), 'cycle-oracle disagreement')
        ok &= a
        R |= {(x, y) for x, y in r if x in B and y in B}
    return frozenset(R) if ok else None


def strong(A, V):
    R = closure(A, V)
    return all(x == y or (x, y) in R for x in V for y in V)


def topo(A, V, c, k):
    left = {x for x in V if (c >> x) & 1 == k}
    order = []
    while left:
        z = sorted(x for x in left if not any((y, x) in A for y in left))
        need(bool(z), 'topological order')
        order += z
        left -= set(z)
    return order


def cycle(A, V, c, k):
    for length in range(3, len(V) + 1):
        S = [x for x in V if (c >> x) & 1 == k]
        for seq in it.permutations(S, length):
            if seq[0] == min(seq) and all((seq[i], seq[(i+1) % length]) in A for i in range(length)):
                return list(seq) + [seq[0]]
    raise ValueError('missing claimed monochromatic cycle')


def faces(A, rotation):
    R = {int(x): ns for x, ns in rotation.items()}
    E = {tuple(sorted(e)) for e in A}
    darts = set(A) | {(y, x) for x, y in A}
    need(all(x != y and (y, x) not in A for x, y in A), 'simple orientation')
    need(set(R) == {x for x, y in darts}, 'rotation vertices')
    for x, ns in R.items():
        need(len(ns) == len(set(ns)) and set(ns) == {y for a, y in darts if a == x}, 'rotation neighbours')
    todo, connected = [min(R)], set()
    while todo:
        x = todo.pop()
        if x not in connected:
            connected.add(x)
            todo += R[x]
    need(connected == set(R), 'map connected')
    used, result = set(), []
    for edge in sorted(darts):
        if edge in used:
            continue
        d, face = edge, []
        while d not in used:
            used.add(d)
            x, y = d
            face.append(x)
            d = (y, R[y][(R[y].index(x) + 1) % len(R[y])])
        need(d == edge, 'face permutation closure')
        result.append(face)
    need(used == darts and len(R) - len(E) + len(result) == 2, 'sphere Euler')
    return result


def negative_family(a, b, c):
    return (a == 4 and (b == 4 or b == 5 and c <= 19 or b == 6 and c <= 11 or b == 7 and c <= 9)
            or a == 5 and (b == 5 and c <= 9 or b == 6 and c <= 7))


def rational_controls():
    negative, zero = 0, []
    for a, b, c in it.combinations_with_replacement(range(4, 65), 3):
        q = 2 - 4*(F(1, a)+F(1, b)+F(1, c))
        need((q < 0) == negative_family(a, b, c), 'face family classification')
        negative += int(q < 0)
        if q == 0:
            zero.append([a, b, c])
    need(zero == [[4,5,20],[4,6,12],[4,8,8],[5,5,10],[6,6,6]], 'zero triangle list')
    return {'tested_sorted_triples': 39711, 'degree_cap': 64, 'negative_triples': negative,
            'zero_triangles': zero, 'scope': 'finite control only; all-degree proof is in the candidate'}


def wheel(d, s, r):
    rim = {(i, (i+1)%d) if not (r >> i)&1 else ((i+1)%d, i) for i in range(d)}
    A = rim | {(i, d) if (s >> i)&1 else (d, i) for i in range(d)}
    return A, rim


def crossing(e, f):
    a, b = sorted(e)
    c, d = sorted(f)
    return len({a,b,c,d}) == 4 and ((a<c<b) != (a<d<b))


def options(d):
    diagonals = [e for e in it.combinations(range(d), 2) if e[1]-e[0] not in (1,d-1)]
    result = []
    for k in range(d-2):
        for es in it.combinations(diagonals, k):
            if any(crossing(e,f) for e,f in it.combinations(es,2)):
                continue
            for bits in range(1<<k):
                result.append(tuple((y,x) if (bits>>i)&1 else (x,y) for i,(x,y) in enumerate(es)))
    need(len(result) == (5 if d == 4 else 31), 'all noncrossing diagonal options')
    return result


def canonical(d, s, r):
    A, _ = wheel(d,s,r)
    orbit = set()
    for sign, offset, reverse in it.product((1,-1), range(d), (False,True)):
        f = lambda x: d if x == d else (sign*x+offset)%d
        B = {(f(y),f(x)) if reverse else (f(x),f(y)) for x,y in A}
        ss = sum(1<<i for i in range(d) if (i,d) in B)
        rr = sum(1<<i for i in range(d) if ((i+1)%d,i) in B)
        orbit.add((ss,rr))
    return min(orbit), len(orbit)


def wheel_controls(d):
    V, B = set(range(d+1)), set(range(d))
    opts = options(d)
    groups, hist, digest = {}, Counter(), hashlib.sha256()
    templates = direct_cases = 0
    for s in range(1<<d):
        if min(s.bit_count(), d-s.bit_count()) < 2:
            continue
        for r in range(1<<d):
            A, rim = wheel(d,s,r)
            rp = {c: [state(A,V,B,c),state(A,V,B,c|1<<d)] for c in range(1<<d)}
            rules = []
            for opt in opts:
                lift, failed = [], False
                for c in range(1<<d):
                    rq = state(rim|set(opt),B,B,c)
                    direct_cases += 1
                    if rq is None:
                        continue
                    ks = [k for k in (0,1) if rp[c][k] is not None and rp[c][k] <= rq]
                    if not ks:
                        failed = True
                    else:
                        lift.append([c,ks[0]])
                if not failed:
                    rules.append({'diagonals':list(opt),'lift':lift})
            key, orbit_size = canonical(d,s,r)
            row = {'s':s,'r':r,'orbit':key,'rules':rules}
            digest.update((json.dumps(row,sort_keys=True,separators=(',',':'))+'\n').encode())
            hist[len(rules)] += 1
            templates += 1
            if key != (s,r):
                continue
            rotation = {d:list(range(d)), **{i:[d,(i-1)%d,(i+1)%d] for i in range(d)}}
            fs = faces(A,rotation)
            need(sorted(map(len,fs)) == sorted([3]*d+[d]), 'wheel disk faces')
            witness = None
            if not rules:
                common = [c for c in range(1<<d) if all(x is None for x in rp[c])
                          and all(state(rim|set(o),B,B,c) is not None for o in opts)]
                need(bool(common), 'actual common failure witness for every option')
                c = common[0]
                witness = {'boundary_ones_mask':c,'blocking_cycles':[cycle(A,V,c,0),cycle(A,V,c|1<<d,1)],
                           'all_diagonal_options_valid':len(opts),'all_common_masks':common}
            groups[str(s)+','+str(r)] = {'s':s,'r':r,'orbit_size':orbit_size,'successful_options':len(rules),
                     'selected_rule':rules[0] if rules else None, 'failure':witness,
                     'arcs':sorted(A),'rotation':rotation,
                     'full_valid_ones_mask':next(c for c in range(1<<(d+1)) if state(A,V,B,c) is not None)}
    need(sum(x['orbit_size'] for x in groups.values()) == templates,'orbit partition')
    bad = [g for g in groups.values() if not g['successful_options']]
    totals = [templates, templates-hist[0],hist[0],len(groups),len(bad)]
    expected = [96,66,30,13,5] if d == 4 else [640,480,160,32,8]
    need(totals == expected, 'wheel complete totals')
    # Every member's success count must agree with its orbit representative.
    for s in range(1<<d):
        if min(s.bit_count(),d-s.bit_count()) >= 2:
            for r in range(1<<d):
                k,_ = canonical(d,s,r)
                need(str(k[0])+','+str(k[1]) in groups, 'canonical representative')
    return {'d':d,'totals_templates_positive_negative_orbits_negative_orbits':totals,
            'options_per_template':len(opts),'all_assignment_option_cases':direct_cases,
            'success_histogram':dict(hist),'table_sha256':digest.hexdigest(),
            'table_storage':'all labelled rows deterministically streamed; representative certificates saved',
            'representatives':list(groups.values())}


def strip_test_six(A, n):
    need(n == 6, 'six-vertex scope')
    pattern_count, admissible = 0, []
    for p,q in it.permutations(range(n),2):
        zs = [x for x in range(n) if x not in (p,q)]
        for z in it.permutations(zs):
            for first in (0,1):
                P = {(z[i],z[i+1]) for i in range(3)}
                for i,x in enumerate(z):
                    P |= {(p,x),(x,q)} if (i+first)%2 == 0 else {(q,x),(x,p)}
                if not P <= A:
                    continue
                inside = set(z[1:-1])
                if any(x in inside or y in inside for x,y in A-P):
                    continue
                pattern_count += 1
                if (z[-1],z[0]) not in A-P:
                    admissible.append([p,q,list(z),first])
    need(not admissible, 'no admissible guarded P4-to-P2 reduction')
    return {'algebraic_P4_occurrences':pattern_count,'all_blocked_by_reverse_endpoint_arc':True,
            'longer_C31_strips_impossible_by_order':True,'admissible':admissible}


def structural_control(g):
    n = g['n']; V = set(range(n)); A = {tuple(e) for e in g['arcs']}
    fs = faces(A,g['rotation'])
    deg = {v:sum(v in e for e in A) for v in V}
    sem = {v:[sum(y==v for x,y in A),sum(x==v for x,y in A)] for v in V}
    need(all(min(ds)>=2 for ds in sem.values()),'structural semidegrees')
    need(all(strong(A,V-{v}) for v in V),'all deletions strongly connected')
    need(state(A,V,[],g['full']) is not None,'explicit full colouring')
    vertex_ledger = [{'v':v,'degree':deg[v],'initial':deg[v]-4,
                      'per_corner':str(F(deg[v]-4,deg[v])),'sent':deg[v]-4,'final':0} for v in sorted(V)]
    face_ledger = []
    for f in fs:
        received = sum((F(deg[v]-4,deg[v]) for v in f),F(0))
        final = len(f)-4+received
        face_ledger.append({'walk':f,'initial':len(f)-4,'received':str(received),'final':str(final)})
    need(sum((F(f['final']) for f in face_ledger),F(0)) == -8,'total charge conserved')
    blocked = []
    for v in V:
        H = V-{v}
        c = next((c for c in range(1<<n) if not(c>>v)&1 and state(A,H,[],c) is not None
                  and state(A,V,[],c) is None and state(A,V,[],c|1<<v) is None),None)
        need(c is not None,'blocked deletion at every vertex')
        blocked.append({'v':v,'ones':c,'cycles':[cycle(A,V,c,0),cycle(A,V,c|1<<v,1)],
                        'H_orders':[topo(A,H,c,k) for k in (0,1)]})
    absent = strip_test_six(A,n) if n == 6 else {'all_degrees_five':all(deg[v]==5 for v in V),
                                    'no_strip_with_internal_degree4_vertex':True}
    need(n != 12 or absent['all_degrees_five'],'icosahedron degree5')
    return {'name':g['name'],'n':n,'arcs':sorted(A),'rotation':g['rotation'],'faces':fs,
            'semidegrees_in_out':sem,'vertex_charges':vertex_ledger,'face_charges':face_ledger,
            'no_applicable_C31_strip':absent,'blocked_deletions':blocked,'full_ones':g['full'],
            'full_orders':[topo(A,V,g['full'],k) for k in (0,1)],
            'scope':'available structural conditions only, not noncolourable/minimum-counterexample premise'}


PAIR_EDGES = [(0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5)]


def pair_patch(r,b):
    _,rim = wheel(4,3,r)
    inside = {(y,x) if (b>>i)&1 else (x,y) for i,(x,y) in enumerate(PAIR_EDGES)}
    return rim|inside, rim


def pair_key(r,b):
    A,_ = pair_patch(r,b)
    orbit = set()
    for sign,offset,rev in it.product((1,-1),(0,2),(0,1)):
        f = {i:(sign*i+offset)%4 for i in range(4)}
        f[4] = 4 if f[1] == 1 else 5
        f[5] = 9-f[4]
        D = {(f[y],f[x]) if rev else (f[x],f[y]) for x,y in A}
        rr = sum(1<<i for i in range(4) if ((i+1)%4,i) in D)
        bb = sum(1<<i for i,(x,y) in enumerate(PAIR_EDGES) if (y,x) in D)
        orbit.add((rr,bb))
    return min(orbit),len(orbit)


def pair_options():
    out = [(4,opt) for opt in options(4)]
    for bits in range(16):
        out.append((5,tuple((i,4) if (bits>>i)&1 else (4,i) for i in range(4))))
    for diagonal,tris in [((0,2),[(0,1,2),(0,2,3)]),((1,3),[(0,1,3),(1,2,3)])]:
        for dr in (diagonal,diagonal[::-1]):
            for tri in tris:
                for bits in range(8):
                    out.append((5,tuple([dr]+[(i,4) if (bits>>j)&1 else (4,i) for j,i in enumerate(tri)])))
    need(len(out)==85,'all selected zero/one-interior replacement options')
    return out


def pair_controls():
    B,V = set(range(4)),set(range(6))
    opts=pair_options();groups={};hist=Counter();digest=hashlib.sha256();cases=0
    for r in range(16):
        _,rim=pair_patch(r,0)
        qt=[]
        for n,opt in opts:
            rows=[(c,state(rim|set(opt),set(range(n)),B,c)) for c in range(1<<n)]
            qt.append((n,opt,[(c,R) for c,R in rows if R is not None]))
        for b in range(128):
            A,_=pair_patch(r,b)
            if not all(sum(y==v for x,y in A)==2 for v in (4,5)):
                continue
            ps={c:[] for c in range(16)}
            for c in range(64):
                R=state(A,V,B,c)
                if R is not None:
                    ps[c&15].append((c,R))
            rules=[]
            for n,opt,rows in qt:
                lift=[];failed=False
                for c,R in rows:
                    choices=[cc for cc,rr in ps[c&15] if rr<=R]
                    cases+=1
                    if not choices:
                        failed=True
                    else:
                        lift.append([c,choices[0]])
                if not failed:
                    rules.append({'vertices':n,'added_arcs':list(opt),'lift':lift})
            digest.update((json.dumps([r,b,rules],sort_keys=True,separators=(',',':'))+'\n').encode())
            hist[len(rules)]+=1
            key,size=pair_key(r,b)
            if key!=(r,b):
                continue
            failure=None
            if not rules:
                bad=[c for c in range(16) if not ps[c]]
                common=[c for c in bad if all(any((cc&15)==c for cc,_ in rows) for _,_,rows in qt)]
                need(bool(common),'common obstruction across all small replacements')
                c=common[0]
                need(c.bit_count() in (1,3),'one minority boundary vertex')
                majority=0 if c.bit_count()==1 else 1
                S={x for x in B if (c>>x)&1==majority}
                same={(x,y) for x,y in rim if x in S and y in S}
                need(len(same)==2 and (len({x for x,y in same})==1 or len({y for x,y in same})==1),
                     'majority boundary source/sink certificate')
                cycles=[]
                for inside in range(4):
                    cc=c|(inside<<4)
                    k=next(k for k in (0,1) if not dag(A,{x for x in V if (cc>>x)&1==k}))
                    cycles.append({'interior_bits':inside,'colour':k,'cycle':cycle(A,V,cc,k)})
                failure={'boundary_ones_mask':c,'all_four_interior_assignments_fail':cycles,
                         'majority_rim_arcs':sorted(same),'valid_small_replacement_options':85,
                         'scope':'all replacements with at most one interior vertex and unchanged boundary rim; see general minority-colour proof'}
            groups[str(r)+','+str(b)]={'r':r,'b':b,'orbit_size':size,'successful_options':len(rules),
                      'selected_rule':rules[0] if rules else None,'failure':failure}
    need(sum(hist.values())==288 and hist[0]==32 and len(groups)==43,'pair totals')
    need(sum(g['orbit_size'] for g in groups.values())==288,'pair orbit partition')
    need(sum(g['failure'] is not None for g in groups.values())==4,'four pair residual orbits')
    return {'templates':288,'successful_templates':256,'remaining_templates':32,'orbits':43,
            'remaining_orbits':4,'options_per_template':85,'valid_small_assignment_cases':cases,
            'success_histogram':dict(hist),'table_sha256':digest.hexdigest(),
            'table_storage':'all rows streamed; representative lifting maps and obstruction cycles retained',
            'representatives':list(groups.values())}


def main():
    raw = Path(sys.argv[1]).read_bytes()
    need(len(raw)<65536,'input bound')
    data = json.loads(raw)
    report = {'verdict':'candidate_only','trusted_verifier_receipt':False,'complete':False,
              'runtime':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256':hashlib.sha256(raw).hexdigest()}
    try:
        need(data['wheel_orders']==[4,5],'frozen range')
        report['charge_controls'] = rational_controls()
        report['structural_controls'] = [structural_control(g) for g in data['structural_controls']]
        report['wheel_controls'] = [wheel_controls(d) for d in (4,5)]
        report['adjacent_degree4_controls'] = pair_controls()
        report['complete'],report['status'] = True,'bounded_controls_passed'
        code = 0
    except (ValueError,KeyError,TypeError,StopIteration) as e:
        report['status'],report['error'] = 'candidate_mismatch',str(e)
        code = 1
    out = json.dumps(report,sort_keys=True,separators=(',',':'))+'\n'
    need(len(out.encode())<65536,'output bound')
    print(out,end='')
    return code


if __name__ == '__main__':
    sys.exit(main())
