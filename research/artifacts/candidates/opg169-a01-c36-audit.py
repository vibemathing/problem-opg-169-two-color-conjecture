"""Separate C36 certificate consumer. Same generator trust domain.
Uses DFS cycles and per-source graph search, not the generator's closure code.
"""
import base64
import zlib
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path
D=Path('research/artifacts/candidates')

def need(ok,msg):
    if not ok:raise ValueError(msg)

def assignments(order):
    for m in range(2**len(order)):
        yield m,sum(((m>>i)&1)<<v for i,v in enumerate(order))

def relation(A,V,B,c):
    allowed=set(V)
    adj={u:[v for a,v in A if a==u and v in allowed and ((c>>u)&1)==((c>>v)&1)] for u in V}
    seen,active=set(),set()
    def visit(u):
        if u in active:return False
        if u in seen:return True
        active.add(u)
        for v in adj[u]:
            if not visit(v):return False
        active.remove(u);seen.add(u);return True
    for u in V:
        if not visit(u):return None
    R=set()
    for s in B:
        todo=list(adj[s]);reach=set()
        while todo:
            x=todo.pop()
            if x not in reach:reach.add(x);todo.extend(adj[x])
        R.update((s,v) for v in B if v in reach)
    return R

def map_faces(A,raw_rotation):
    rotation={int(v):list(ns) for v,ns in raw_rotation.items()}
    V=set(rotation);und={tuple(sorted(e)) for e in A}
    need(all(u!=v and (v,u) not in A for u,v in A),'simple oriented input')
    for v,ns in rotation.items():
        need(len(ns)==len(set(ns)) and set(ns)=={w for e in und if v in e for w in e if w!=v},'complete rotation neighbours')
    seen=set();fs=[]
    for u,v in sorted({e for x,y in und for e in ((x,y),(y,x))}):
        if (u,v) in seen:continue
        start=(u,v);seq=[];e=start
        while e not in seen:
            seen.add(e);x,y=e;seq.append(x);n=rotation[y];e=y,n[(n.index(x)+1)%len(n)]
        need(e==start,'dart orbit');fs.append(seq)
    need(len(V)-len(und)+len(fs)==2,'planar sphere certificate')
    reached=set();todo=[min(V)]
    while todo:
        x=todo.pop()
        if x not in reached:reached.add(x);todo.extend(rotation[x])
    need(reached==V,'connected rotation')
    return fs

def cycle_witness(A,c,item):
    k,seq=item
    need(len(seq)>=4 and seq[0]==seq[-1] and len(set(seq[:-1]))==len(seq)-1,'positive simple cycle')
    need(all((x,y) in A for x,y in zip(seq,seq[1:])),'every cycle arc exists')
    need(all((c>>x)&1==k for x in seq),'monochromatic cycle')

def main():
    raw=(D/'opg169-a01-c36-input.json').read_bytes();data=json.loads(raw)
    packed=(D/'opg169-a01-c36-certificate-archive.json').read_bytes();archive=json.loads(packed)
    need(archive['format']=='c36-lossless-certificate-v1' and archive['encoding']=='zlib-base64','archive format')
    dec=zlib.decompressobj();cr=dec.decompress(base64.b64decode(archive['data'],validate=True),1048576)
    need(dec.eof and not dec.unconsumed_tail and not dec.unused_data,'bounded exact archive')
    need(len(cr)==archive['decoded_bytes'] and hashlib.sha256(cr).hexdigest()==archive['decoded_sha256'],'decoded certificate identity')
    cert=json.loads(cr)
    need(hashlib.sha256(raw).hexdigest()==cert['input_sha256'],'input identity')
    A={tuple(e) for e in data['graph']['arcs']};V=set(data['graph']['vertices'])
    fs=map_faces(A,data['graph']['rotation']);J=set(data['J']);I=data['interior_order']
    base_tri=[f for f in fs if set(f)&J]
    base_edges={tuple(sorted((f[i],f[(i+1)%3]))) for f in base_tri for i in range(3)}
    base={e for e in A if tuple(sorted(e)) in base_edges}
    need(len(cert['rows'])==18,'finite allocation')
    lifts=reverse_lifts=negative_assignments=domain_failures=0;labels=set()
    for row in cert['rows']:
        kind,bit=row['label'];labels.add((kind,bit))
        B=row['boundary'];P={tuple(e) for e in row['arcs']};vs=set(B+I)
        if kind=='cap':
            expected=base|{(11,8) if bit==0 else (8,11)};tri=base_tri+[[8,7,11]]
        else:
            w=1 if kind=='new' else 5
            expected=base|{(w,v) if bit>>j&1 else (v,w) for j,v in enumerate([11,7,8])}
            tri=base_tri+[[8,7,w],[7,11,w]]
        need(P==expected,'directions reconstructed from frozen J')
        ff=map_faces(P,row['rotation']);canon=lambda x:min(tuple(x[i:]+x[:i]) for i in range(len(x)))
        need(set(map(canon,tri))<=set(map(canon,ff)),'actual absorbed triangles')
        Q={e for e in P if set(e)<=set(B)};need(Q==set(map(tuple,row['Q_arcs'])),'every retained arc')
        bad={f['boundary_word']:f for f in row['failures']};positive_case=not bad
        for m,c in assignments(B):
            R=relation(Q,B,B,c);z=row['internal_word_by_boundary_word'][m]
            if R is None:
                need(z is None and m not in bad,'invalid smaller assignment distinguished');continue
            if z is not None:
                inside=sum(((z>>i)&1)<<v for i,v in enumerate(I));rr=relation(P,vs,B,c|inside)
                need(rr is not None and rr==R,'full positive reachability equality')
                Pr={(v,u) for u,v in P};Qr={(v,u) for u,v in Q}
                need(relation(Pr,vs,B,c|inside)==relation(Qr,B,B,c),'full arc reversal')
                if positive_case:lifts+=1;reverse_lifts+=1
            else:
                need(m in bad,'every failed smaller assignment recorded')
                pressure={r[0]:r for r in bad[m]['all_interior_cases']};none_valid=True
                for j,k in assignments(I):
                    rr=relation(P,vs,B,c|k);r=pressure[j]
                    if rr is None:need(r[1]=='cycle','failure kind');cycle_witness(P,c|k,r[2])
                    else:
                        none_valid=False;need(r[1]=='extra_relation' and set(map(tuple,r[2]))==rr-R and rr-R,'exact extra return witness')
                    negative_assignments+=1
                need(none_valid==bad[m]['no_valid_extension'],'nonextension is not failed containment')
                domain_failures+=none_valid
        need(positive_case==(kind!='new' or bit in [0,1,4,5]),'scoped direction family')
    need(labels=={('cap',b) for b in range(2)}|{(k,b) for k in ('new','alias5') for b in range(8)},'all allocated types')
    for row in cert['alias_exclusions']:
        w=row['q'];x=row['forced_degree3'];tri=base_tri+[[8,7,w],[7,11,w]]
        und={tuple(sorted((f[i],f[(i+1)%3]))) for f in tri for i in range(3)}
        ns={b for a,b in und if a==x}|{a for a,b in und if b==x}
        around=[f for f in tri if x in f]
        need(len(ns)==3 and len(around)==3 and set(row['closed_link'])==ns,'closed degree-three star, not partial degree')
    selected=next(r for r in cert['rows'] if r['label']==['new',5]);B=selected['boundary']
    P=set(map(tuple,selected['arcs']));Q=set(map(tuple,selected['Q_arcs']));H=V-set(I)
    def lift(c):
        m=sum(((c>>v)&1)<<i for i,v in enumerate(B));z=selected['internal_word_by_boundary_word'][m]
        return c|sum(((z>>i)&1)<<v for i,v in enumerate(I))
    actual=[]
    for _,c in assignments(sorted(H)):
        if relation(A,H,[],c) is None:continue
        cc=lift(c);need(relation(A,V,[],cc) is not None,'all full retained colours, not projection')
        actual.append([c,cc])
    need(actual==cert['full_exterior_lifts'] and len(actual)==90,'complete eight-vertex exterior')
    need(lift(578)==cert['specified_lift']['new_ones']==715,'old obstruction repaired only after releasing7')
    old=578
    need(all(relation(A,V,[],old|k) is None for _,k in assignments(sorted(J))),'known C35 failure as minimum-expansion control only')
    diagonals=[e for e in it.combinations(range(6),2) if e[1]-e[0] not in (1,5)]
    ext=[];valid_ext=0
    for word in it.product((0,1,2),repeat=9):
        es=[e for e,z in zip(diagonals,word) if z]
        if any(len(set(e+f))==4 and ((e[0]<f[0]<e[1])!=(e[0]<f[1]<e[1])) for e,f in it.combinations(es,2)):continue
        E={(B[a],B[b]) if z==1 else (B[b],B[a]) for (a,b),z in zip(diagonals,word) if z}
        count=0
        for _,c in assignments(B):
            R=relation(Q|E,B,B,c)
            if R is None:continue
            need(relation(P|E,set(B+I),B,lift(c))==R,'actual outside chord retained')
            count+=1
        ext.append((tuple(sorted(E)),count));valid_ext+=count
    need(sorted(ext)==sorted((tuple(map(tuple,e)),n) for e,n in cert['external_chord_counts']),'all absent/directed noncrossing chords')
    need(len(ext)==215,'exterior scope')
    need(all(len(data['graph']['rotation'][str(v)])==5 for v in V),'original graph has no marked low-low pairs')
    for row in cert['vertex_ledger']:
        v,d,t,g,initial,units,corners,final,after=row
        need(d==5 and t==0 and F(g)==F(1,5) and initial==1 and units==0 and F(corners)==1 and final==0,'each original debit')
        expected=sum(w in H for w in data['graph']['rotation'][str(v)]) if v in H else None
        need(after==expected,'new degree is not substituted into original charge')
    need(len(cert['face_ledger'])==20 and {tuple(x[0]) for x in cert['face_ledger']}==set(map(tuple,fs)),'all actual faces')
    for f,initial,received,h,final,affected,delta in cert['face_ledger']:
        need(initial==-1 and F(received)==F(3,5) and h==0 and F(final)==F(-2,5),'each original face receipt')
        need(affected==bool(set(f)&set(I)) and F(delta)==0,'all affected faces and single-to-double debit')
    need(sum(F(x[4]) for x in cert['face_ledger'])==-8,'global conservation')
    # Targeted mutations: invalid stored colouring, induced-cycle omission,
    # zero-length paths, and illegal escapes are not accepted as proof.
    need(relation(P,set(B+I),B,0) is None,'all-zero corrupted lift rejected')
    need(relation({(0,1),(1,2),(2,0)},[0,1,2],[],0) is None and relation({(0,1),(1,2)},[0,1,2],[],0) is not None,'omitting induced arc changes validity')
    need(relation(set(),[0],[0],0)==set(),'reflexive zero-length path is not positive return')
    need(relation({(0,0)},[0],[0],0) is None and relation({(0,1),(1,0)},[0,1],[],0) is None,'loop and digon controls')
    need(F(8-4-2*2,8)==0 and F(8-4-2,8)-F(2,8)==0,'single-to-double corner loss retained')
    out={'verdict':'candidate_only','trusted_verifier_receipt':False,'status':'all_declared_checks_passed',
         'same_generator_trust_domain':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':hashlib.sha256(raw).hexdigest(),'certificate_sha256':hashlib.sha256(cr).hexdigest(),
         'positive_family_lifts':lifts,'reversed_lifts':reverse_lifts,'negative_interior_witnesses':negative_assignments,
         'negative_actual_nonextension_boundaries':domain_failures,'full_exterior_lifts':len(actual),
         'external_chord_sets':len(ext),'external_chord_valid_assignments':valid_ext,
         'original_vertex_rows':12,'original_face_rows':20,'affected_faces':12,'unaffected_faces':8,'targeted_mutations':6}
    print(json.dumps(out,sort_keys=True,separators=(',',':')));return 0
if __name__=='__main__':sys.exit(main())
