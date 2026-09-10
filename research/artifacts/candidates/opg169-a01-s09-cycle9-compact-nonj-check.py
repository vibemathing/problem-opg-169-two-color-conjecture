#!/usr/bin/env python3
import json, hashlib, itertools, sys
from pathlib import Path

D=Path(__file__).resolve().parent
C35=D/"opg169-a01-c35-input.json"
SIG=D/"opg169-a01-s09-cycle9-compact-nonj-signatures.json"

def need(x,msg):
    if not x: raise AssertionError(msg)

def faces(rot):
    seen=set(); out=[]
    for a in sorted(rot):
        for b in rot[a]:
            if (a,b) in seen: continue
            cur=(a,b); f=[]
            while cur not in seen:
                seen.add(cur); x,y=cur; f.append(x)
                cur=(y,rot[y][(rot[y].index(x)+1)%len(rot[y])])
            need(cur==(a,b),"face closes")
            out.append(f)
    return out

def hole(face,R):
    S=set(face)
    rr={v:[w for w in R[v] if w not in S] for v in R if v not in S}
    hs=[f for f in faces(rr) if len(f)>3]
    need(len(hs)==1 and len(hs[0])==6,"unique six-hole")
    return hs[0]

def closure(n,arcs,c):
    rr=[0]*n
    for u,v in arcs:
        if ((c>>u)&1)==((c>>v)&1): rr[u]|=1<<v
    for k in range(n):
        for i in range(n):
            if rr[i]>>k&1: rr[i]|=rr[k]
    if any(rr[i]>>i&1 for i in range(n)): return None
    return rr

def state(n,arcs,c):
    rr=closure(n,arcs,c)
    if rr is None: return None
    out=[0,0]
    for u in range(6):
        cu=(c>>u)&1
        for v in range(6):
            if u!=v and rr[u]>>v&1: out[cu]|=1<<(u*6+v)
    return tuple(out)

def profile(face,A,R):
    B=hole(face,R)
    loc={v:i for i,v in enumerate(B)}
    for i,v in enumerate(face): loc[v]=6+i
    V=set(B)|set(face)
    arcs=[(loc[u],loc[v]) for u,v in A if u in V and v in V]
    exact=[]
    for b in range(64):
        exact.append(sorted({s for im in range(8) if (s:=state(9,arcs,b|(im<<6))) is not None}))
    rim=[]
    for i in range(6):
        u,v=B[i],B[(i+1)%6]
        rim.append(0 if (u,v) in A else 1)
    return B,rim,exact

def cross(e,f):
    a,b=e;c,d=f
    return len({a,b,c,d})==4 and ((a<c<b)!=(a<d<b))

pairs=[e for e in itertools.combinations(range(6),2) if e[1]-e[0] not in (1,5)]
states=[]
for k in range(4):
    for es in itertools.combinations(pairs,k):
        if any(cross(e,f) for e,f in itertools.combinations(es,2)): continue
        for w in range(1<<k):
            dirs=tuple((b,a) if w>>i&1 else (a,b) for i,(a,b) in enumerate(es))
            states.append((k,tuple(es),w,dirs))
need(len(states)==215,"215 zero-internal directed states")

def rim_arcs(B,A):
    q=[]
    for i in range(6):
        u,v=B[i],B[(i+1)%6]
        q.append((i,(i+1)%6) if (u,v) in A else ((i+1)%6,i))
    return q

def accept(exact,B,A,dirs):
    q=rim_arcs(B,A)+list(dirs)
    valid=0
    for b in range(64):
        qs=state(6,q,b)
        if qs is None: continue
        valid+=1
        if not any(ps[0]&~qs[0]==0 and ps[1]&~qs[1]==0 for ps in exact[b]):
            return False,valid
    return valid>0,valid

def transform_dirs(dirs,perm):
    inv={old:new for new,old in enumerate(perm)}
    return tuple(sorted((inv[u],inv[v]) for u,v in dirs))

def transform_profile(rim,exact,perm,flip):
    inv={old:new for new,old in enumerate(perm)}
    nr=[]
    for j in range(6):
        ou,ov=perm[j],perm[(j+1)%6]
        nr.append(rim[ou] if ov==(ou+1)%6 else 1-rim[ov])
    ne=[]
    for nb in range(64):
        ob=0
        for j,old in enumerate(perm):
            z=(nb>>j)&1
            if flip: z^=1
            ob|=z<<old
        vals=[]
        for x,y in exact[ob]:
            rel=(y,x) if flip else (x,y)
            out=[]
            for mask in rel:
                nm=0
                for u in range(6):
                    for v in range(6):
                        if mask>>(u*6+v)&1: nm|=1<<(inv[u]*6+inv[v])
                out.append(nm)
            vals.append(tuple(out))
        ne.append(sorted(set(vals)))
    return nr,ne

def main():
    g=json.loads(C35.read_text())["graph"]
    A={tuple(e) for e in g["arcs"]}
    R={int(v):ns for v,ns in g["rotation"].items()}
    sig=json.loads(SIG.read_text())
    need(sig["verdict"]=="candidate_only" and not sig["root_closed"],"trust boundary")
    raw=C35.read_bytes()
    git_blob=hashlib.sha1((f"blob {len(raw)}\0").encode()+raw).hexdigest()
    need(git_blob==sig["sources"]["c35_input_git_blob"],"exact C35 git blob")
    FS=faces(R)
    need(len(FS)==20 and all(len(f)==3 for f in FS),"20 triangles")
    need(all(len(R[v])==5 for v in R),"degree five frozen control")

    derived=[]
    base=[]
    for f in FS:
        B,rim,exact=profile(f,A,R)
        passers=[x for x in states if accept(exact,B,A,x[3])[0]]
        mk=min(x[0] for x in passers)
        k,es,w,dirs=sorted([x for x in passers if x[0]==mk],key=lambda x:(x[1],x[2]))[0]
        pobj=[[[f"{x:09x}",f"{y:09x}"] for x,y in row] for row in exact]
        ph=hashlib.sha256(json.dumps(pobj,separators=(",",":")).encode()).hexdigest()
        derived.append((f,B,rim,exact,ph,passers,(k,es,w,dirs)))
        base.append(dirs)

    need(len(set(x[4] for x in derived))==20,"20 raw exact P profiles distinct")
    need(len(set(base))==19,"19 distinct canonical systems")
    dih={tuple((s+j)%6 for j in range(6)) for s in range(6)}|{tuple((s-j)%6 for j in range(6)) for s in range(6)}
    orb={transform_dirs(t,p) for t in set(base) for p in dih}
    need(len(orb)==85,"85 D6-closed systems")

    ch=[]
    for f,B,rim,exact,ph,passers,can in derived:
        texts=[]
        for p in dih:
            for flip in (False,True):
                nr,ne=transform_profile(rim,exact,p,flip)
                texts.append(json.dumps({"rim":nr,"p":ne},sort_keys=True,separators=(",",":")))
        ch.append(hashlib.sha256(min(texts).encode()).hexdigest())
    need(len(set(ch))==20,"20 profiles remain distinct mod D6+colour swap")

    # The compact signature artifact must bind every reconstructed control exactly.
    need(len(sig["controls"])==20,"20 signature rows")
    byface={tuple(c["face_walk"]):c for c in sig["controls"]}
    need(len(byface)==20,"unique physical face keys")
    for n,(f,B,rim,exact,ph,passers,can) in enumerate(derived):
        c=byface[tuple(f)]
        need(c["boundary_walk"]==B,"boundary walk bind")
        need(c["rim_direction_word"]=="".join(map(str,rim)),"rim direction bind")
        need(c["exact_P_profile_sha256"]==ph,"exact P profile hash bind")
        need(c["D6_colour_swap_canonical_profile_sha256"]==ch[n],"canonical profile hash bind")
        need(c["all_215_profile_valid_count"]==len(passers),"215 pass-count bind")
        k,es,w,dirs=can
        t=c["canonical_minimum_template"]
        need(t["added_chord_count"]==k,"minimum chord count bind")
        need(t["underlying_pairs"]==[list(e) for e in es],"template pairs bind")
        need(t["orientation_word"]==w,"template word bind")
        need(t["directed_chords"]==[list(e) for e in dirs],"template directions bind")
        need(t["valid_Q_count"]==accept(exact,B,A,dirs)[1],"template Q count bind")
        need(c["forbidden_nonrim_boundary_pairs"]==[],"raw C35 forbidden set empty")

    # Verify compact counterrow: physical face (0,3,4).
    row=next(x for x in derived if x[0]==[0,3,4])
    f,B,rim,exact,ph,passers,can=row
    need(B==[2,7,8,9,5,6],"counterrow boundary")
    need(len(passers)==1,"unique profile-valid state among all 215")
    only=passers[0]
    need(only[1]==((0,2),(0,3),(0,4)) and only[2]==2,"unique chord state")
    need(only[3]==((0,2),(3,0),(0,4)),"unique directions")
    need((2,8) not in A and (8,2) not in A,"C35 control has free blocker pair")
    # In the counterrow, exterior adds 8->2: reverse of required 2->8.
    required_actual=(B[0],B[2]); reverse=(B[2],B[0])
    need(required_actual==(2,8) and reverse==(8,2),"mapped guard")
    # Zero blockers => one source-safe profile state; one blocker hits its required underlying pair.
    need((0,2) in only[1],"one blocker hits unique state")
    cr=sig["counterrow"]
    need(cr["source_geometry_control_face"]==[0,3,4],"counterrow source face bind")
    need(cr["boundary_walk"]==B,"counterrow boundary bind")
    need(cr["exact_P_profile_sha256"]==ph,"counterrow exact profile bind")
    need(cr["exterior_owned_arcs"]==[[8,2]],"counterrow exterior reverse bind")
    need(cr["guard_failure"]["required_actual_arc"]==[2,8],"counterrow required arc bind")
    need(cr["guard_failure"]["actual_reverse_arc"]==[8,2],"counterrow reverse guard bind")

    out={
      "format":"opg169-s09-cycle9-compact-nonj-check-output-v1",
      "verdict":"candidate_only",
      "root_closed":False,
      "physical_controls":20,
      "raw_exact_profile_count":20,
      "signature_rows_exactly_bound":20,
      "c35_git_blob_exact":True,
      "D6_colour_swap_profile_count":20,
      "canonical_template_count":19,
      "D6_closed_template_count":85,
      "all_zero_internal_state_count":215,
      "counterrow_profile_valid_before_guard":1,
      "counterrow_profile_valid_after_reverse_guard":0,
      "counterrow_minimum_blocker_count":1,
      "conditional_COMPACT_NONJ_CLOSE":"PASS_candidate_statement_shape",
      "controls_exhaust_arbitrary_COMPACT_NONJ":False,
      "registry_inversion":"FORBIDDEN",
      "mince_occurrence_created":False
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
