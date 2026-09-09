"""Separate DFS/BFS consumer of the frozen incoming certificate; same trust domain."""
import hashlib
import itertools as it
import json
from collections import Counter, deque
from fractions import Fraction as F
from pathlib import Path
D = Path('research/artifacts/candidates')
B = (4,5,6,11,1,8)
I = (0,2,3,7)
K = (0,2,7)
BASE = {(0,2),(0,4),(2,3),(2,6),(2,11),(3,0),(3,4),(3,7),
        (4,5),(4,8),(5,0),(5,6),(6,0),(7,2),(7,8),(8,3),(11,6),(11,7)}


def demand(ok, message):
    if not ok:
        raise ValueError(message)


def assignment(order, word):
    return {v:(word>>j)&1 for j,v in enumerate(order)}


def analyse(A,V,c,ports=B):
    adj={v:[] for v in V}
    for x,y in A:
        if c[x]==c[y]:
            adj[x].append(y)
    done=set(); stack=set()
    def dfs(x):
        if x in stack:
            return False
        if x in done:
            return True
        stack.add(x)
        for y in adj[x]:
            if not dfs(y):
                return False
        stack.remove(x);done.add(x)
        return True
    if not all(dfs(x) for x in V):
        return None
    pairs=set()
    for start in ports:
        queue=deque(adj[start]);seen=set()
        while queue:
            x=queue.popleft()
            if x in seen:
                continue
            seen.add(x);queue.extend(adj[x])
        pairs.update((start,x) for x in ports if x in seen)
    return pairs


def check_map(A,rot):
    E={frozenset(e) for e in A}
    demand(all(len(e)==2 for e in E) and len(E)==len(A),'no loop or digon')
    demand(set(rot)==set().union(*E),'vertex set')
    for v,ns in rot.items():
        demand(len(ns)==len(set(ns)) and set(ns)=={next(iter(e-{v})) for e in E if v in e},'complete neighbour rotation')
    orbits=[];used=set()
    for a in sorted(rot):
        for b in rot[a]:
            if (a,b) in used:continue
            edge=(a,b);start=edge;face=[]
            while edge not in used:
                used.add(edge);x,y=edge;face.append(x)
                pos=rot[y].index(x);edge=(y,rot[y][(pos+1)%len(rot[y])])
            demand(edge==start,'dart permutation')
            orbits.append(face)
    reached={min(rot)}
    for _ in rot:reached|={y for x in reached for y in rot[x]}
    demand(reached==set(rot) and len(rot)-len(E)+len(orbits)==2,'connected sphere')
    return orbits


def canonical(f):
    return min(tuple(f[j:]+f[:j]) for j in range(len(f)))


def main():
    cp=D/'opg169-a01-c36-incoming-certificate.json'
    raw=cp.read_bytes(); data=json.loads(raw)
    ip=D/'opg169-a01-c36-input.json'; inp=json.loads(ip.read_text())
    demand(hashlib.sha256(ip.read_bytes()).hexdigest()==data['input_sha256'],'input identity')
    demand([r['w'] for r in data['rows']]==[2,3,6,7],'complete four-type scope')
    total=Counter(); vectors=[]
    for row in data['rows']:
        w=row['w'];A=BASE|{(1,x) if w>>j&1 else (x,1) for j,x in enumerate((11,7,8))}
        V=set(B+I);QV=V-{3};Q={e for e in A if 3 not in e}
        demand(A==set(map(tuple,row['arcs'])) and Q==set(map(tuple,row['Q_arcs'])),'all original and replacement arcs')
        rot={int(v):ns for v,ns in row['rotation'].items()}
        faces=check_map(A,rot)
        demand({canonical(f) for f in faces}=={canonical(f) for f in row['faces']},'all original faces')
        qrot={v:[u for u in ns if u!=3] for v,ns in rot.items() if v!=3}
        demand(sorted(map(len,check_map(Q,qrot)))==[3]*7+[5,6],'deletion embedding')
        demand(all(set(rot[v])==set(inp['graph']['rotation'][str(v)]) for v in I),'no hidden exterior neighbour of internally recoloured vertices')
        vector=row['lift_hex'];demand(len(vector)==512 and set(vector)<=set('-0123456789abcdef'),'total vector grammar')
        records=[];count=Counter()
        for b,k in it.product(range(64),range(8)):
            c=assignment(B,b)|assignment(K,k);rq=analyse(Q,QV,c)
            token=vector[8*b+k]
            if rq is None:
                demand(token=='-','invalid replacement assignment distinguished')
                count['invalid']+=1;continue
            demand(token!='-','no valid replacement assignment omitted')
            p=int(token,16);lift=assignment(B,b)|assignment(I,p);rp=analyse(A,V,lift)
            demand(rp is not None and rp<=rq,'FULL containment lift')
            demand(all(lift[v]==c[v] for v in B),'same boundary colours')
            changed=sum(c[x]!=lift[x] for x in K)
            demand(changed<=2,'two simultaneous changes bound')
            count['valid']+=1;count['changed_'+str(changed)]+=1
            count['equal_R' if rp==rq else 'strict_R']+=1
            revA={(y,x) for x,y in A};revQ={(y,x) for x,y in Q}
            aa=analyse(revA,V,lift);qq=analyse(revQ,QV,c)
            demand(aa is not None and qq is not None and aa<=qq,'full arc-reversal control')
            records.append((c,lift))
        # Independent ternary enumeration of all noncrossing exterior diagonals.
        diagonals=[(i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5)]
        actual={tuple(map(tuple,r[0])):r[1] for r in row['direct_exterior_controls']}; used=0;valid_chords=0
        for digits in it.product((0,1,2),repeat=len(diagonals)):
            es=[e for e,d in zip(diagonals,digits) if d]
            if any(len(set(e+f))==4 and ((e[0]<f[0]<e[1])!=(e[0]<f[1]<e[1])) for e,f in it.combinations(es,2)):continue
            E={(B[i],B[j]) if d==1 else (B[j],B[i]) for (i,j),d in zip(diagonals,digits) if d}
            got=0
            for c,lift in records:
                rq=analyse(Q|E,QV,c)
                if rq is None:continue
                rp=analyse(A|E,V,lift)
                demand(rp is not None and rp<=rq,'actual same exterior chord graph')
                got+=1
            demand(actual[tuple(sorted(E))]==got,'complete chord counts')
            valid_chords+=got;used+=1
        demand(used==len(actual)==215,'exact direct exterior catalogue')
        count['chord_valid']=valid_chords
        full=set(map(tuple,row['full_arcs'])); fv=set(inp['graph']['vertices']);fq={e for e in full if 3 not in e}
        demand({e for e in full if set(e)<=V}==A,'full realization restricts to the frozen core')
        fr={int(v):ns for v,ns in inp['graph']['rotation'].items()}
        ff=check_map(full,fr)
        demand(all(len(fr[v])==5 and sum(y==v for x,y in full)>=2 and sum(x==v for x,y in full)>=2 for v in fv),'realized degree/semidegree bounds')
        stored={a:b for a,b in row['full_lifts']}; reached=0
        order=sorted(fv-{3})
        for bits in range(1<<len(order)):
            c=assignment(order,bits)
            if analyse(fq,set(order),c,()) is None:continue
            mask=sum(1<<x for x,k in c.items() if k);demand(mask in stored,'complete full exterior domain')
            lift={x:(stored[mask]>>x)&1 for x in fv}
            demand(analyse(full,fv,lift,()) is not None,'full union acyclic')
            demand(all(c[x]==lift[x] for x in fv-set(I)),'ENTIRE exterior colour fixed')
            reached+=1
        demand(reached==len(stored),'no duplicate or nonexistent full cases')
        count['full_lifts']=reached
        ledger=row['full_face_ledger'];demand({canonical(f) for f in ff}=={canonical(r['face']) for r in ledger},'every original face accounted once')
        for r in ledger:
            demand(r['h']==0 and F(r['final'])==-F(2,5) and r['single_to_double_change']=='0','donor-free full ledger')
        demand(sum(F(r['final']) for r in ledger)==-8 and sum(r['affected'] for r in ledger)==12,'global and affected charge counts')
        demand(dict(count)==row['counts'],'all row totals independently recomputed')
        total.update(count);vectors.append([w,count['valid'],count['invalid'],count['full_lifts']])
    ports=Counter()
    for r in data['symbolic_faces']:
        f=r['face'];i=sum(v in I for v in f);bs=[v for v in f if v in B]
        demand(F(r['constant'])==-1+F(i,5) and r['gamma_ports']==bs and r['old_to_double_deduction_ports']==bs,'symbolic gamma and every t/d loss')
        demand(r['h_forced_zero']==(len(bs)<2),'payment possibility is not assumed absent')
        ports.update(bs)
    demand(dict(ports)=={1:2,4:3,5:2,6:3,8:3,11:3},'all sixteen boundary face corners')
    # Exact identity over controls, with the algebraic proof kept separate.
    for d in range(4,101):
        for t in range(d+1):
            if d<max(3*t,2*t+4):continue
            gamma=F(d-4-2*t,d)
            demand(gamma>=0 and d*gamma+2*t==d-4,'matched vertex debits')
            demand(gamma-F(d-4-t,d)==-F(t,d),'every corner loss retained')
    demand(dict(total)==data['counts'],'global totals')
    out={'verdict':'candidate_only','trusted_verifier_receipt':False,'status':'separate_consumer_passed',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'certificate_sha256':hashlib.sha256(raw).hexdigest(),'rows_w_valid_invalid_full':vectors,
         'counts':dict(total),'boundary_corner_multiplicities':dict(ports),
         'no_prior_positive_direction_replay':True,'lean_elaboration':'not_run','axiom_report':None}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))

if __name__ == '__main__':main()
