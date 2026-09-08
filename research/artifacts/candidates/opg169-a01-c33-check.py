"""C33 exact finite exterior-face controls; generator-only, candidate_only.
Run with the archived resource-limited wrapper. No third-party dependencies.
The proof of applicability and the charge transfer are separate from this test.
"""
import base64
import hashlib
import itertools as it
import json
import platform
import sys
import zlib
from collections import Counter
from functools import lru_cache
from pathlib import Path

CODES = ((1, 78), (1, 100), (3, 43), (5, 77))
PAIR_EDGES = ((0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5))
BASE_ROT = {0:[1,4,5,3],1:[0,2,4],2:[3,5,4,1],3:[0,5,2],4:[0,1,2,5],5:[0,4,2,3]}
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
D = Path('research/artifacts/candidates')


def need(ok, message):
    if not ok:
        raise ValueError(message)


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()


def pair(code):
    r, b = code
    return {(j,i) if (r>>i)&1 else (i,j) for i in range(4) for j in [(i+1)%4]} | {
        (y,x) if (b>>i)&1 else (x,y) for i,(x,y) in enumerate(PAIR_EDGES)}


def faces(rotation):
    used, out = set(), []
    for x in sorted(rotation):
        for y in rotation[x]:
            if (x,y) in used:
                continue
            a,b = x,y
            f = []
            while (a,b) not in used:
                used.add((a,b)); f.append(a)
                a,b = b,rotation[b][(rotation[b].index(a)+1)%len(rotation[b])]
            need((a,b)==(x,y), 'face closure')
            out.append(f)
    return out


BASE_FACES = [f for f in faces(BASE_ROT) if len(f)==3]


def rotation_from_faces(n, face_list):
    nxt = [{} for _ in range(n)]
    for f in face_list:
        need(len(f)==len(set(f)), 'simple facial walk')
        for j,b in enumerate(f):
            a,c = f[j-1],f[(j+1)%len(f)]
            need(a not in nxt[b], 'duplicate facial dart')
            nxt[b][a] = c
    rotation = {}
    for b, mp in enumerate(nxt):
        need(bool(mp), 'isolated vertex in completed map')
        a = min(mp); seq = [a]; c = mp[a]
        while c != a:
            seq.append(c)
            need(len(seq)<=len(mp), 'split rotation')
            c = mp[c]
        need(len(seq)==len(mp), 'multiple link circles')
        rotation[b] = seq
    need(n-sum(map(len,rotation.values()))//2+len(face_list)==2, 'sphere Euler')
    todo, seen = [0], set()
    while todo:
        x=todo.pop()
        if x not in seen:
            seen.add(x); todo.extend(rotation[x])
    need(len(seen)==n, 'map connectedness')
    return rotation


def check_map(n, arcs, rotation, boundary):
    need(all(x!=y and (y,x) not in arcs for x,y in arcs), 'orientation domain')
    darts = arcs | {(y,x) for x,y in arcs}
    need(darts=={(x,y) for x,ys in rotation.items() for y in ys}, 'all rotation neighbours')
    fs=faces(rotation)
    need(n-len(arcs)+len(fs)==2, 'planar map')
    cyclic={tuple(boundary[j:]+boundary[:j]) for j in range(len(boundary))}
    need(sum(tuple(f) in cyclic for f in fs)==1, 'exact marked boundary face')
    return fs


def rows(n, arcs, d):
    """All binary assignments; bitset closure checked against Kahn removal."""
    result = {}
    full=(1<<n)-1; boundary=(1<<d)-1
    for c in range(1<<n):
        adjacency=[0]*n
        for x,y in arcs:
            if ((c>>x)&1)==((c>>y)&1):
                adjacency[x] |= 1<<y
        reach=adjacency[:]
        for k in range(n):
            bit=1<<k; rk=reach[k]
            for x in range(n):
                if reach[x]&bit:
                    reach[x] |= rk
        positive_acyclic=not any((reach[x]>>x)&1 for x in range(n))
        left=full
        while left:
            targets=0
            for x in range(n):
                if (left>>x)&1:
                    targets |= adjacency[x]&left
            zero=left & ~targets
            if not zero:
                break
            left ^= zero
        need(positive_acyclic==(left==0), 'two cycle engines disagree')
        if positive_acyclic:
            result[c]=sum((reach[x]&boundary)<<(d*x) for x in range(d))
    return result


@lru_cache(None)
def skeletons(d, k):
    """All maximal simple disk skeletons for k<=2, with prescribed rim.
    Enumerate edge sets AND oriented triangular face covers, not just a library
    embedding or one insertion construction. Retain one map per edge set.
    """
    need(3<=d<=5 and 0<=k<=2, 'skeleton allocation')
    n=d+k
    rim={tuple(sorted((i,(i+1)%d))) for i in range(d)}
    extra=[p for p in it.combinations(range(n),2) if p not in rim]
    edge_count=3*n-3-d
    result=[]
    for selected in it.combinations(extra,edge_count-d):
        edges=rim|set(selected)
        if any(sum(x in e for e in edges)<3 for x in range(d,n)):
            continue
        darts=edges|{(y,x) for x,y in edges}
        left=darts-{(i,(i+1)%d) for i in range(d)}
        answer=None
        def visit(unused, triangles):
            nonlocal answer
            if answer is not None:
                return
            if not unused:
                try:
                    rot=rotation_from_faces(n,triangles+[list(range(d))])
                except (ValueError,KeyError):
                    return
                answer=rot
                return
            a,b=min(unused)
            for c in range(n):
                if (b,c) in unused and (c,a) in unused:
                    visit(unused-{(a,b),(b,c),(c,a)},triangles+[[a,b,c]])
        visit(left,[])
        if answer is not None:
            result.append((tuple(sorted(edges)),answer))
    return tuple(result)


def replacements(d, rim, max_internal):
    """The bare rim followed by every maximal completion, without duplicates."""
    yield d, rim, {i:[(i-1)%d,(i+1)%d] for i in range(d)}
    rim_edges={tuple(sorted(e)) for e in rim}
    for k in range(max_internal+1):
        for edges,rot in skeletons(d,k):
            extras=sorted(set(edges)-rim_edges)
            if not extras:
                continue
            for bits in range(1<<len(extras)):
                arcs=rim|{(y,x) if (bits>>j)&1 else (x,y) for j,(x,y) in enumerate(extras)}
                yield d+k,arcs,rot


def canon(n, arcs, boundary):
    order=boundary+[x for x in range(n) if x not in boundary]
    mp={x:i for i,x in enumerate(order)}
    return {(mp[x],mp[y]) for x,y in arcs},order


def profile_search(n, arcs, boundary, mode):
    arcs,order=canon(n,arcs,boundary)
    d=len(boundary); mask=(1<<d)-1
    original=rows(n,arcs,d)
    p=[[] for _ in range(1<<d)]
    for c,r in original.items():
        p[c&mask].append((c,r))
    rim={e for e in arcs if max(e)<d and (e[0]-e[1])%d in (1,d-1)}
    need(len(rim)==d, 'full directed rim')
    present={tuple(sorted(e)) for e in arcs}
    failed=[]; candidates=0; examined=0; first_guarded=None; domain_only=True
    for nn,q,rot in replacements(d,rim,n-d-1):
        candidates += 1
        added=sorted(e for e in q if e not in rim)
        guards=sorted((y,x) for x,y in added if x<d and y<d and tuple(sorted((x,y))) not in present)
        if first_guarded is not None and guards:
            continue
        examined += 1
        qr=rows(nn,q,d)
        lift=[None]*(1<<nn); failure=None
        for c,r in qr.items():
            choices=[cc for cc,rp in p[c&mask] if rp & ~r == 0]
            if not choices:
                failure=c; break
            lift[c]=min(choices)
        if failure is not None:
            failed.append(ALPHABET[failure])
            if not any(not p[c&mask] for c in qr):
                domain_only=False
            continue
        added=sorted(e for e in q if e not in rim)
        guards=sorted((y,x) for x,y in added if x<d and y<d and tuple(sorted((x,y))) not in present)
        rule={'vertices':nn,'arcs':sorted(q),'rotation':rot,'forbidden_exterior_arcs':guards,
              'lift_by_full_mask':lift,'vertices_saved':n-nn}
        check_map(nn,q,rot,list(range(d)))
        # Do not count a Q-colouring not visited after early rejection as verified.
        need(all(lift[c] is not None and lift[c]&mask==c&mask and
                 original[lift[c]] & ~r == 0 for c,r in qr.items()), 'complete selected lift')
        if mode=='rim_only' or not guards:
            return {'order':order,'status':'rule','rule':rule,'tested':examined,'visited_candidates':candidates}
        if first_guarded is None:
            first_guarded=rule
    if first_guarded is not None:
        return {'order':order,'status':'guarded_rule','rule':first_guarded,'tested':examined,'visited_candidates':candidates,
                'guard_free_maximal_search_only':True}
    return {'order':order,'status':'no_containment_replacement','candidates':candidates,
            'failure_masks_alphabet64':''.join(failed),'every_maximal_has_unattainable_boundary':domain_only,
            'bad_boundary_masks':[c for c in range(1<<d) if not p[c]]}


def local_cases():
    certificate=[]; summaries=[]
    for index,code in enumerate(CODES):
        a0=pair(code); per=Counter(); residual=[]
        # One exterior triangle on EACH boundary edge, new third vertex.
        for edge in range(4):
            a,b=edge,(edge+1)%4
            boundary=list(range(edge+1))+[6]+list(range(edge+1,4))
            for bits in range(4):
                arcs=a0|{(6,a) if bits&1 else (a,6),(6,b) if bits&2 else (b,6)}
                rot=rotation_from_faces(7,BASE_FACES+[[a,b,6],boundary])
                check_map(7,arcs,rot,boundary)
                s=profile_search(7,arcs,boundary,'all')
                need(s['status']=='no_containment_replacement', 'fresh-ear outcome changed')
                need(s['candidates']==693, 'complete five-port replacements')
                certificate.append({'id':[index,'ear',edge,bits],'arcs':sorted(arcs),'boundary':boundary,
                                    'rotation':rot,**s})
                per['ear_negative']+=1
        # Facial closure whose third vertex was already on the old boundary.
        for corner in range(4):
            a,b=(corner-1)%4,(corner+1)%4
            boundary=[x for x in range(4) if x!=corner]
            for bit in range(2):
                arcs=a0|{(b,a) if bit else (a,b)}
                rot=rotation_from_faces(6,BASE_FACES+[[a,corner,b],boundary])
                check_map(6,arcs,rot,boundary)
                small=min(sum(x==corner for x,y in arcs),sum(y==corner for x,y in arcs))<2
                if small:
                    s={'status':'excluded_small_semidegree'}
                else:
                    s=profile_search(6,arcs,boundary,'all')
                per['closure_'+s['status']]+=1
                certificate.append({'id':[index,'closure',corner,bit],'boundary':boundary,'arcs':sorted(arcs),
                                    'rotation':rot,**s})
        # Adjacent exterior faces have the SAME NEW third vertex. The corner
        # becomes interior, so its full degree/semidegrees are now known.
        for corner in range(4):
            a,b=(corner-1)%4,(corner+1)%4
            boundary=list(range(4)); boundary[corner]=6
            for bits in range(8):
                arcs=a0|{(6,x) if (bits>>j)&1 else (x,6) for j,x in enumerate([a,corner,b])}
                rot=rotation_from_faces(7,BASE_FACES+[[a,corner,6],[corner,b,6],boundary])
                check_map(7,arcs,rot,boundary)
                small=min(sum(x==corner for x,y in arcs),sum(y==corner for x,y in arcs))<2
                if small:
                    s={'status':'excluded_small_semidegree'}
                else:
                    s=profile_search(7,arcs,boundary,'all')
                    if s['status']=='no_containment_replacement':
                        need(s['candidates']==5205, 'complete four-port two-interior replacements')
                        residual.append([corner,bits])
                per['wrap_'+s['status']]+=1
                certificate.append({'id':[index,'wrap',corner,bits],'boundary':boundary,'arcs':sorted(arcs),
                                    'rotation':rot,**s})
        # The shared third vertex may be the opposite old corner. Two triangles
        # then close the whole complementary quadrilateral: no exterior remains.
        for diagonal in ((0,2),(1,3)):
            for bit in range(2):
                x,y=diagonal; arcs=a0|{(y,x) if bit else (x,y)}
                other=[z for z in range(4) if z not in diagonal]
                triangles=([[0,1,2],[0,2,3]] if diagonal==(0,2) else [[0,1,3],[1,2,3]])
                rot=rotation_from_faces(6,BASE_FACES+triangles)
                low=[z for z in range(6) if min(sum(a==z for a,b in arcs),sum(b==z for a,b in arcs))<2]
                valid=rows(6,arcs,0)
                need(bool(valid), 'six-vertex closed control colourable')
                certificate.append({'id':[index,'closed',x,bit],'arcs':sorted(arcs),'rotation':rot,
                                    'small_semidegree_vertices':low,'full_colouring_mask':min(valid),
                                    'status':'whole_graph_colourable_or_small_semidegree'})
                per['closed_controls']+=1
        expected=([(2,2),(2,5)] if index<2 else [(0,5)] if index==2 else [])
        need(residual==[list(z) for z in expected], 'wrap residual list')
        donor=0 if index<2 else 2
        for row in certificate:
            if row['id'][0]!=index or row['id'][1] not in ('closure','wrap') or row['id'][2]!=donor:
                continue
            need(row['status']=='rule' and row['rule']['vertices']==len(row['boundary']) and
                 not row['rule']['forbidden_exterior_arcs'], 'degree-six donor: every small case has bare-rim lift')
        summaries.append({'code':code,'counts':dict(per),'wrap_residuals':residual,'forced_donor':donor})
    return certificate,summaries


def donor_controls():
    counts=[]
    for d in range(6,13):
        maximum=0
        for mask in range(1<<d):
            word=[(mask>>j)&1 for j in range(d)]
            # Each marked residual pair is a maximal cyclic run of length two.
            runs=sum(word[(j-1)%d]!=word[j]==word[(j+1)%d]!=word[(j+2)%d] for j in range(d))
            need(runs<=d-4, 'donor budget')
            need(d-4-runs>=0, 'nonnegative remaining budget')
            maximum=max(maximum,runs)
        counts.append([d,1<<d,maximum])
    return {'words':sum(z[1] for z in counts),'by_degree':counts,
            'scope':'finite control; unrestricted run-count and charge proof are separate'}


def main():
    raw=Path(sys.argv[1]).read_bytes()
    need(len(raw)<65536, 'input cap')
    data=json.loads(raw)
    need(data['codes']==[list(c) for c in CODES], 'frozen residue allocation')
    out={'verdict':'candidate_only','trusted_verifier_receipt':False,'complete':False,
         'runtime':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':hashlib.sha256(raw).hexdigest()}
    try:
        expected={(3,0):1,(3,1):1,(3,2):6,(4,0):2,(4,1):5,(4,2):40,(5,0):5,(5,1):21}
        for key,value in expected.items():
            need(len(skeletons(*key))==value, 'disk skeleton count')
        cert,summary=local_cases()
        out['residues']=summary
        out['donor_controls']=donor_controls()
        payload=canonical_json({'format':'c33-full-local-certificate-v1','failure_alphabet':ALPHABET,
                                'failure_order':'bare rim; then k, sorted skeleton edge sets, binary orientations',
                                'rows':cert})
        need(len(payload)<1048576, 'decompressed certificate cap')
        packed={'format':'c33-lossless-zlib-base64-v1','verdict':'candidate_only','uncompressed_bytes':len(payload),
                'uncompressed_sha256':hashlib.sha256(payload).hexdigest(),
                'data':base64.b64encode(zlib.compress(payload,9)).decode()}
        need(zlib.decompress(base64.b64decode(packed['data']))==payload, 'certificate roundtrip')
        (D/'opg169-a01-c33-certificate.json').write_bytes(canonical_json(packed)+b'\n')
        out['certificate_sha256']=hashlib.sha256((D/'opg169-a01-c33-certificate.json').read_bytes()).hexdigest()
        out['certificate_rows']=len(cert)
        out['certificate_decoded_sha256']=packed['uncompressed_sha256']
        out['skeleton_counts']={str(k):v for k,v in expected.items()}
        out['complete']=True;out['status']='bounded_controls_passed';code=0
    except (ValueError,KeyError,TypeError) as error:
        out['status']='candidate_mismatch';out['error']=str(error);code=1
    text=canonical_json(out)+b'\n'
    need(len(text)<65536, 'summary cap')
    sys.stdout.buffer.write(text)
    return code


if __name__=='__main__':
    sys.exit(main())
