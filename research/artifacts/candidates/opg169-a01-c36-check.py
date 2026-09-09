"""C36 finite J-wedge certificate generator; not a trusted verifier.
No prior enumeration is imported. Run through the bounded replay wrapper.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction
from pathlib import Path

D = Path('research/artifacts/candidates')

def need(p, message):
    if not p:
        raise ValueError(message)


def masks(order):
    return [sum(((m >> i) & 1) << v for i, v in enumerate(order))
            for m in range(1 << len(order))]


def state(arcs, vertices, boundary, c):
    vs = sorted(vertices)
    idx = {v: i for i, v in enumerate(vs)}
    reach = [0] * len(vs)
    for u, v in arcs:
        if u in idx and v in idx and ((c >> u) & 1) == ((c >> v) & 1):
            reach[idx[u]] |= 1 << idx[v]
    for k in range(len(vs)):
        for i in range(len(vs)):
            if (reach[i] >> k) & 1:
                reach[i] |= reach[k]
    if any((reach[i] >> i) & 1 for i in range(len(vs))):
        return None
    return frozenset((u, v) for u in boundary for v in boundary
                     if (reach[idx[u]] >> idx[v]) & 1)


def faces(rotation):
    used, result = set(), []
    for u in sorted(rotation):
        for v in rotation[u]:
            if (u, v) in used:
                continue
            e, row = (u, v), []
            while e not in used:
                used.add(e)
                x, y = e
                row.append(x)
                ns = rotation[y]
                e = (y, ns[(ns.index(x) + 1) % len(ns)])
            need(e == (u, v), 'face closes at initial dart')
            result.append(row)
    edges = sum(len(x) for x in rotation.values()) // 2
    need(len(rotation) - edges + len(result) == 2, 'sphere Euler')
    return result


def rotation_from_triangles(triangles):
    successors = {}
    for a, b, c in triangles:
        need(len({a, b, c}) == 3, 'distinct facial vertices')
        for v, x, y in ((b, a, c), (c, b, a), (a, c, b)):
            row = successors.setdefault(v, {})
            need(x not in row or row[x] == y, 'consistent actual facial sectors')
            row[x] = y
    rotation = {}
    for v, row in successors.items():
        ns = set(row) | set(row.values())
        heads = sorted(ns - set(row.values()))
        if not heads:
            first = min(ns)
            chain, x = [first], row[first]
            while x != first:
                need(x not in chain, 'simple vertex link')
                chain.append(x)
                x = row[x]
            need(set(chain) == ns, 'closed full link')
        else:
            chain = []
            for h in heads:
                part = [h]
                while part[-1] in row:
                    x = row[part[-1]]
                    need(x not in part, 'partial link is a path')
                    part.append(x)
                chain += part
            need(len(chain) == len(ns) and set(chain) == ns, 'link chains cover neighbours')
        rotation[v] = chain
    fs = faces(rotation)
    canon = lambda f: min(tuple(f[i:] + f[:i]) for i in range(len(f)))
    need(set(map(canon, triangles)) <= set(map(canon, fs)), 'all stipulated faces retained')
    return rotation, fs, successors


def full_cycle(arcs, vs, c):
    for colour in (0, 1):
        allowed = {v for v in vs if (c >> v) & 1 == colour}
        adj = {u: sorted(v for a, v in arcs if a == u and v in allowed) for u in allowed}
        def visit(u, path):
            for v in adj[u]:
                if v in path:
                    return path[path.index(v):] + [v]
                got = visit(v, path + [v])
                if got:
                    return got
            return None
        for u in sorted(allowed):
            got = visit(u, [u])
            if got:
                return [colour, got]
    raise ValueError('claimed cyclic colouring has no cycle')


def topo(arcs, vs, c, colour):
    left = {v for v in vs if (c >> v) & 1 == colour}
    order = []
    while left:
        zero = sorted(v for v in left if not any((u, v) in arcs for u in left))
        need(bool(zero), 'topological order exists')
        order += zero
        left -= set(zero)
    return order


def chords(B):
    n = len(B)
    pairs = [e for e in it.combinations(range(n), 2) if e[1]-e[0] not in (1,n-1)]
    def cross(e, f):
        a,b=e; c,d=f
        return len({a,b,c,d})==4 and ((a<c<b)!=(a<d<b))
    for k in range(n-2):
        for es in it.combinations(pairs,k):
            if any(cross(e,f) for e,f in it.combinations(es,2)):
                continue
            for bits in range(1<<k):
                yield {(B[b],B[a]) if bits>>i&1 else (B[a],B[b]) for i,(a,b) in enumerate(es)}


def case(arcs, triangles, I, B, label):
    rot, fs, _ = rotation_from_triangles(triangles)
    vs = set(rot)
    need(all(u != v and (v,u) not in arcs for u,v in arcs), 'simple orientation')
    need({frozenset(e) for e in arcs} == {frozenset((u,v)) for u in rot for v in rot[u]}, 'all edges present')
    need(set(B) == vs-set(I), 'separator includes all retained vertices')
    rim = {(u,v) for u,v in arcs if u in B and v in B}
    lift, failures = [], []
    for m,c in enumerate(masks(B)):
        R = state(rim,B,B,c)
        if R is None:
            lift.append(None)
            continue
        selected, pressure = None, []
        for z,k in enumerate(masks(I)):
            rr=state(arcs,vs,B,c|k)
            if rr is not None and rr <= R:
                if selected is None:
                    selected=z
            elif rr is None:
                pressure.append([z,'cycle',full_cycle(arcs,vs,c|k)])
            else:
                pressure.append([z,'extra_relation',sorted(rr-R)])
        lift.append(selected)
        if selected is None:
            failures.append({'boundary_word':m,'all_interior_cases':pressure,
                             'no_valid_extension':all(x[1]=='cycle' for x in pressure)})
    return {'label':label,'boundary':B,'interior':I,'arcs':sorted(arcs),'rotation':rot,
            'faces':fs,'Q_arcs':sorted(rim),'internal_word_by_boundary_word':lift,'failures':failures}


def main():
    source = Path(__file__).read_bytes()
    raw = (D/'opg169-a01-c36-input.json').read_bytes()
    data=json.loads(raw)
    A={tuple(e) for e in data['graph']['arcs']};V=set(data['graph']['vertices'])
    rot={int(v):ns for v,ns in data['graph']['rotation'].items()}
    F=faces(rot);J=set(data['J']);I=data['interior_order']
    tris=[f for f in F if set(f)&J]
    baseE={frozenset((f[i],f[(i+1)%3])) for f in tris for i in range(3)}
    baseA={e for e in A if frozenset(e) in baseE}
    need(len(tris)==10 and len(baseA)==18,'frozen J core')
    rows=[]
    for bit in (0,1):
        arc=(11,8) if bit==0 else (8,11)
        rows.append(case(baseA|{arc},tris+[[8,7,11]],I,[4,5,6,11,8],['cap',bit]))
    for w in (1,5):
        B=data['new_boundary'] if w==1 else [4,5,6,11,8]
        for bit in range(8):
            extra={(w,v) if bit>>i&1 else (v,w) for i,v in enumerate(data['wedge_arc_order'])}
            rows.append(case(baseA|extra,tris+[[8,7,w],[7,11,w]],I,B,['new' if w==1 else 'alias5',bit]))
    alias=[]
    for w,low in ((4,8),(6,11)):
        rt,fs,succ=rotation_from_triangles(tris+[[8,7,w],[7,11,w]])
        need(len(rt[low])==3 and set(succ[low])==set(rt[low]),'alias closes a degree-three vertex')
        alias.append({'q':w,'forced_degree3':low,'closed_link':rt[low],'rotation':rt,'faces':fs})
    selected=next(r for r in rows if r['label']==['new',5])
    B=selected['boundary'];P={tuple(e) for e in selected['arcs']};Q={tuple(e) for e in selected['Q_arcs']}
    need(P=={e for e in A if e[0] in set(B+I) and e[1] in set(B+I)},'selected actual core')
    need(all(len(rot[v])==5 for v in I),'complete interior stars')
    extrows=[];validchord=0
    for E in chords(B):
        counts=0
        for m,c in enumerate(masks(B)):
            R=state(Q|E,B,B,c)
            if R is None:continue
            z=selected['internal_word_by_boundary_word'][m]
            rr=state(P|E,B+I,B,c|masks(I)[z])
            need(rr is not None and rr<=R,'same actual exterior chords retained')
            counts+=1
        extrows.append([sorted(E),counts]);validchord+=counts
    need(len(extrows)==215,'complete six-port chord allocation')
    H=V-set(I);whole=[]
    for c in masks(sorted(H)):
        if state(A,H,[],c) is None:continue
        m=sum(((c>>v)&1)<<i for i,v in enumerate(B));z=selected['internal_word_by_boundary_word'][m]
        cc=c|masks(I)[z]
        need(state(A,V,[],cc) is not None,'full retained assignment lifts')
        whole.append([c,cc])
    need(len(whole)==90,'complete full-exterior domain')
    specified=next(cc for c,cc in whole if c==data['specified_retained_ones'])
    vertex_rows=[]
    for v in sorted(V):
        d=len(rot[v]);t=0;gamma=Fraction(d-4-2*t,d)
        vertex_rows.append([v,d,t,str(gamma),d-4,0,str(d*gamma),0,len([w for w in rot[v] if w in H]) if v in H else None])
    face_rows=[]
    for f in F:
        gamma=sum((Fraction(len(rot[v])-4,len(rot[v])) for v in f),Fraction(0))
        face_rows.append([f,-1,str(gamma),0,str(gamma-1),bool(set(f)&set(I)),str(Fraction(0))])
    need(len(F)==20 and sum(Fraction(x[4]) for x in face_rows)==-8,'complete original charge ledger')
    need(sum(x[5] for x in face_rows)==12,'all affected faces, not selected projections')
    stats={'cases':len(rows),'successful_cases':sum(not r['failures'] for r in rows),
           'complete_positive_lifts':sum(len(r['internal_word_by_boundary_word']) for r in rows if not r['failures']),
           'negative_boundary_words':sum(len(r['failures']) for r in rows),
           'negative_no_extension':sum(f['no_valid_extension'] for r in rows for f in r['failures']),
           'direct_exterior_options':len(extrows),'direct_exterior_valid_assignments':validchord,
           'full_exterior_lifts':len(whole),'vertex_rows':len(vertex_rows),'face_rows':len(face_rows)}
    need(stats['successful_cases']==14 and stats['complete_positive_lifts']==576,'all selected family rules')
    need(stats['negative_boundary_words']==12 and stats['negative_no_extension']==4,'negative scope distinction')
    out={'format':'c36-j-wedge-certificate-v1','verdict':'candidate_only','trusted_verifier_receipt':False,
         'source_sha256':hashlib.sha256(source).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
         'rows':rows,'alias_exclusions':alias,'external_chord_counts':extrows,'full_exterior_lifts':whole,
         'specified_lift':{'old_ones':data['specified_retained_ones'],'new_ones':specified,'topological_orders':[topo(A,V,specified,k) for k in (0,1)]},
         'vertex_columns':['v','degree','t','gamma','initial','unit_debit','corner_debit','final','retained_degree_or_null'],
         'vertex_ledger':vertex_rows,'face_columns':['face','initial','corner_receipts','h','final','affected_by_deletion','change_from_single_payment'],
         'face_ledger':face_rows,'stats':stats}
    text=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
    need(len(text.encode())<1048576,'output cap')
    print(text,end='')
    return 0

if __name__=='__main__':
    sys.exit(main())
