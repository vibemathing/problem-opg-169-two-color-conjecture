"""Exact four-type incoming-neighbour controls; candidate_only, not admission."""
import hashlib
import itertools as it
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

D = Path('research/artifacts/candidates')
B = (4, 5, 6, 11, 1, 8)
I = (0, 2, 3, 7)
K = (0, 2, 7)
WORDS = (2, 3, 6, 7)
INPUT_HASH = '993932fcc1b8591a72869d0f474d4feb67ea31f994edb7ef2aa3bd70948a5f48'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def mask(order, word):
    return sum(((word >> j) & 1) << v for j, v in enumerate(order))


def profile(arcs, vertices, c):
    reach = {v: 0 for v in vertices}
    for u, v in arcs:
        if ((c >> u) ^ (c >> v)) & 1 == 0:
            reach[u] |= 1 << v
    for z in vertices:
        for u in vertices:
            if reach[u] >> z & 1:
                reach[u] |= reach[z]
    if any(reach[v] >> v & 1 for v in vertices):
        return None
    return sum(1 << (6*j+k) for j, u in enumerate(B) for k, v in enumerate(B)
               if reach[u] >> v & 1)


def valid(arcs, vertices, c):
    for colour in (0, 1):
        left = {v for v in vertices if c >> v & 1 == colour}
        while left:
            zero = {v for v in left if not any((u, v) in arcs for u in left)}
            if not zero:
                return False
            left -= zero
    return True


def embedding(arcs, rotation):
    E = {frozenset(e) for e in arcs}
    need(all(u != v and (v, u) not in arcs for u, v in arcs), 'simple orientation')
    for v, ns in rotation.items():
        need(len(ns) == len(set(ns)) and set(ns) == {next(iter(e-{v})) for e in E if v in e}, 'rotation incidence')
    seen = {min(rotation)}
    for _ in rotation:
        seen |= {w for v in seen for w in rotation[v]}
    need(seen == set(rotation), 'connected map')
    darts = {(u, v) for u in rotation for v in rotation[u]}
    faces = []
    while darts:
        first = e = min(darts)
        face = []
        while e in darts:
            darts.remove(e)
            u, v = e
            face.append(u)
            ns = rotation[v]
            e = (v, ns[(ns.index(u)+1) % len(ns)])
        need(e == first, 'face permutation')
        faces.append(face)
    need(len(rotation)-len(E)+len(faces) == 2, 'sphere Euler')
    return faces


def chords():
    pairs = [p for p in it.combinations(range(6), 2) if p[1]-p[0] not in (1, 5)]
    def cross(e, f):
        a, b = e
        c, d = f
        return len({a,b,c,d}) == 4 and ((a<c<b) != (a<d<b))
    result = []
    for n in range(4):
        for edges in it.combinations(pairs, n):
            if any(cross(e,f) for e,f in it.combinations(edges, 2)):
                continue
            for bits in range(1 << n):
                result.append({(B[v],B[u]) if bits>>j&1 else (B[u],B[v])
                               for j,(u,v) in enumerate(edges)})
    need(len(result) == 215, 'complete six-port direct-chord scope')
    return result


def main():
    raw = (D/'opg169-a01-c36-input.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest() == INPUT_HASH, 'frozen input bytes')
    g = json.loads(raw)['graph']
    A0 = set(map(tuple, g['arcs']))
    V = set(B+I)
    rot = {int(v): [u for u in ns if u in V] for v, ns in g['rotation'].items() if int(v) in V}
    Rfull = {int(v): ns for v, ns in g['rotation'].items()}
    base = {e for e in A0 if set(e) <= V and 1 not in e}
    rows = []
    total = Counter()
    for w in WORDS:
        A = base | {(1,x) if w>>j&1 else (x,1) for j,x in enumerate((11,7,8))}
        need(len(A) == 21 and all(len(rot[v]) == 5 for v in I), 'complete core stars')
        Pfaces = embedding(A, rot)
        need(sorted(map(len,Pfaces)) == [3]*12+[6], 'core disk')
        Q = {e for e in A if 3 not in e}
        QV = V-{3}
        qrot = {v: [u for u in ns if u != 3] for v, ns in rot.items() if v != 3}
        qfaces = embedding(Q, qrot)
        need(sorted(map(len,qfaces)) == [3]*7+[5,6], 'one deleted vertex, no added edge')
        choices = {}
        for b in range(64):
            c = mask(B,b)
            choices[b] = []
            for p in range(16):
                cc = c | mask(I,p)
                rp = profile(A,V,cc)
                need((rp is not None) == valid(A,V,cc), 'two cycle oracles')
                if rp is not None:
                    choices[b].append((p,rp))
        vector = []
        count = Counter()
        for b in range(64):
            c = mask(B,b)
            for k in range(8):
                cq = c | mask(K,k)
                rq = profile(Q,QV,cq)
                need((rq is not None) == valid(Q,QV,cq), 'replacement cycle oracles')
                if rq is None:
                    vector.append('-')
                    count['invalid'] += 1
                    continue
                possible = [(sum(((cq ^ (c|mask(I,p)))>>x)&1 for x in K),p,rp)
                            for p,rp in choices[b] if rp & ~rq == 0]
                need(bool(possible), 'every FULL valid replacement assignment lifts')
                changes,p,rp = min(possible)
                need(changes <= 2, 'at most two simultaneous interior changes')
                vector.append(format(p,'x'))
                count['valid'] += 1
                count['changed_'+str(changes)] += 1
                count['equal_R' if rp == rq else 'strict_R'] += 1
        chord_counts = []
        for F in chords():
            passed = 0
            for b in range(64):
                c = mask(B,b)
                for k in range(8):
                    cq = c | mask(K,k)
                    rq = profile(Q|F,QV,cq)
                    if rq is None:
                        continue
                    p = int(vector[8*b+k],16)
                    rp = profile(A|F,V,c|mask(I,p))
                    need(rp is not None and rp & ~rq == 0, 'same actual exterior chords retained')
                    passed += 1
            chord_counts.append([sorted(F),passed])
        # Find one complete twelve-vertex plane realization for each fixed core.
        outside_edges = sorted({tuple(sorted(e)) for e in A0 if not set(e) <= V})
        # Edges within V are exactly the core, and all remaining edges are outside.
        need(len(outside_edges) == 9, 'complete exterior edge allocation')
        wholeA = None
        for word in range(1 << len(outside_edges)):
            F = {(y,x) if word>>j&1 else (x,y) for j,(x,y) in enumerate(outside_edges)}
            full = A | F
            if all(sum(y==v for x,y in full)>=2 and sum(x==v for x,y in full)>=2 for v in Rfull):
                wholeA = full
                break
        need(wholeA is not None, 'realization with both semidegrees at least two')
        whole_faces = embedding(wholeA,Rfull)
        retained = tuple(v for v in sorted(Rfull) if v != 3)
        wholeQ = {e for e in wholeA if 3 not in e}
        full_lifts = []
        for k in range(1 << len(retained)):
            cq = mask(retained,k)
            if not valid(wholeQ,set(retained),cq):
                continue
            b = sum(((cq>>v)&1)<<j for j,v in enumerate(B))
            q = sum(((cq>>v)&1)<<j for j,v in enumerate(K))
            p = int(vector[8*b+q],16)
            cp = (cq & ~sum(1<<v for v in K)) | mask(I,p)
            need(valid(wholeA,set(Rfull),cp), 'full graph lift, all exterior colours fixed')
            full_lifts.append([cq,cp])
        need(bool(full_lifts), 'nonvacuous full graph test')
        ledger = [{'face':f,'gamma':[[v,'1/5'] for v in f],'h':0,'initial':-1,'final':'-2/5',
                   'affected':bool(set(f)&set(I)), 'single_to_double_change':'0'} for f in whole_faces]
        need(sum(Fraction(f['final']) for f in ledger) == -8, 'full original charge ledger')
        need(sum(f['affected'] for f in ledger) == 12, 'all recoloured/deleted-star faces')
        count['chord_valid'] = sum(n for _,n in chord_counts)
        count['full_lifts'] = len(full_lifts)
        total.update(count)
        rows.append({'w':w,'arcs':sorted(A),'rotation':rot,'faces':Pfaces,'Q_arcs':sorted(Q),
                     'Q_rotation':qrot,'Q_faces':qfaces,'lift_hex':''.join(vector),'counts':dict(count),
                     'direct_exterior_controls':chord_counts,'full_arcs':sorted(wholeA),
                     'full_lifts':full_lifts,'full_face_ledger':ledger})
    need([r['counts']['valid'] for r in rows] == [162,160,216,216], 'frozen four-type totals')
    sym = []
    for f in rows[0]['faces']:
        if len(f) != 3:
            continue
        k = sum(v in I for v in f)
        ports = [v for v in f if v in B]
        sym.append({'face':f,'constant':str(-1+Fraction(k,5)),'gamma_ports':ports,
                    'h_forced_zero':len(ports)<2,'old_to_double_deduction_ports':ports})
    report = {'format':'c36-incoming-certificate-v1','verdict':'candidate_only','trusted_verifier_receipt':False,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':INPUT_HASH,
              'boundary':B,'original_interior':I,'replacement_interior':K,'deleted_vertex':3,
              'vector_index':'8*boundary_word+replacement_interior_word; - invalid, hexadecimal original interior word',
              'rows':rows,'symbolic_faces':sym,'counts':dict(total),
              'scope':'only new distinct z=1, z->7, four directions; no old closed-direction replay'}
    text = json.dumps(report,sort_keys=True,separators=(',',':'))+'\n'
    need(len(text.encode()) < 1048576, 'bounded certificate')
    (D/'opg169-a01-c36-incoming-certificate.json').write_text(text)
    print(json.dumps({'verdict':'candidate_only','status':'four_types_passed','counts':dict(total),
          'source_sha256':report['source_sha256'],'certificate_sha256':hashlib.sha256(text.encode()).hexdigest(),
          'certificate_bytes':len(text.encode())},sort_keys=True))

if __name__ == '__main__':
    main()
