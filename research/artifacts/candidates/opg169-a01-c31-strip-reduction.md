# C31: alternating-strip profiles and smaller all-exterior replacements

Verdict: candidate_only. Status: proof-drafted with bounded generator controls.
Candidate: candidate:opg169-a01-c31-strip-reduction
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: bcffc6fe5ed24d412a3100ec75adb9178e770c9e
Owner: math-proof. No C27 dependency. No trusted admission is claimed.

## 1. Exact patch, embedding and conclusions

For k>=2 use distinct poles p,q and distinct path vertices
z0=a,z1,...,z_(k-1)=b, disjoint from the poles. Put every forward path arc
z_i->z_(i+1). Types alternate A,B, beginning with either T. At type A
put p->z_i->q; at type B put q->z_i->p. These are ALL patch arcs.
There is no pq edge, and no ab edge except when k=2. Call this P(k,T).
Its labelled cyclic disk boundary is B=(p,a,q,b). The complete rotation is
 p:(z0,...,z_(k-1)); q:(z_(k-1),...,z0);
 a:(p,q,z1); b:(p,z_(k-2),q);
 z_i:(p,z_(i-1),q,z_(i+1)) for 0<i<k-1.
Draw the a-to-b path across the disk and put the two families of spokes
in its two half-disks. This realizes the rotation. There are k+2 vertices,
3k-1 edges, 2k-2 triangular interior faces and one quadrilateral outer face.

A valid binary colouring means both FULL induced colour classes are
acyclic; unused colours are allowed. Its boundary state (sigma,R) records
boundary colours and ALL positive monochromatic boundary reachability,
including paths through other boundary vertices. Empty paths do not count.
A profile S(P) consists of states of ALL valid colourings, not one witness.

The all-orders conclusions, for either T, are:
 E: S(P(k,T))=S(P(4,T)) for every even k>=4; there are 16 states.
 O: S(P(k,T))=S(P(5,T)) for every odd k>=5; there are 18 states.
 I3: S(P(3,T)) is a strict subset of the odd profile; it has 16 states.
 I2: S(P(2,T)) is a strict subset of the even profile; it has 12 states.

Consequently an isolated such disk strip in a minimum counterexample
cannot have odd k>=5 or even k>=6: replace it by P(3,T) or P(4,T).
Even k>=4 can be replaced further by P(2,T) when the exterior has no b->a
arc. All exterior colours lift unchanged; the graph loses at least two
vertices. This is a conditional reducible configuration, not an assertion
that every degree-four/five vertex lies in one. Sections 2-5 prove it.

## 2. Opposite pole colours: every colouring and every return

Normalize c(p)=0,c(q)=1 by global complement, encode A=0,B=1, and set
s_i=c(z_i) XOR type(z_i). A monochromatic cycle must use exactly one pole,
since the graph without poles is a directed path and the poles differ.
A colour-0 cycle through p uses a monochromatic forward path from an A
to a later B. It contains an adjacent AB pair coloured 00, which conversely
closes a triangle through p. Colour-1 acyclicity similarly forbids 11 at
BA edges through q. On either parity the forbidden transformed pair is
(s_i,s_(i+1))=(0,1). Thus validity is EXACTLY s=1^t0^(k-t), 0<=t<=k.

Without normalization let sa=c(a) XOR c(p) XOR type(a), and define sb
likewise. A boundary colouring is attainable iff sa>=sb. Cases 00,10,11
are realized by thresholds 0, any interior threshold, and k. There are
three states for each of two ordered pole colourings, hence six in total.

For k>=3, R is precisely the positive transitive closure of same-colour
boundary spokes. To see completeness, a monochromatic boundary path
using its colour's pole can be shortened at each boundary end to the
direct spoke: a detour going opposite that spoke would create a cycle.
A boundary path avoiding poles can only be a-to-b along the entire path.
All k vertices would be monochromatic, but the path includes both AB and
BA edges, violating one of the triangle conditions. No reverse path exists.
For k=2 treat this separately: a valid same-colour a->b arc is already
represented by the path through the pole of that colour, using the two
boundary spokes. The endpoint condition and R therefore have the same
form for k=2. This does not misuse the k>=3 full-path exclusion.

## 3. Equal pole colours: exact occupancy regimes

Let c(p)=c(q)=h. If there are both an A vertex x and a B vertex y coloured
h, then p->x->q->y->p is a monochromatic cycle. Conversely, when at most
one type is occupied in colour h, this class has the form p->A_h->q or
q->B_h->p, or consists of isolated poles. Adjacent types differ, so there
are no same-h path edges. The other colour induces a subpath, a DAG.
This proves the necessary and sufficient condition.

There are three regimes with exact boundary relations:
 E: neither type occupied; all path vertices are 1-h and R={(a,b)}.
 A: only A occupied, nonempty; close the same-colour boundary spokes
    together with p->q under positive transitivity.
 B: only B occupied, nonempty; do the same with q->p.
An occupied h vertex interrupts the only possible a-to-b path of colour
1-h, so no other-colour return has been omitted in regimes A/B.

An h-coloured endpoint forces its own type to be occupied. Endpoints of
different types both coloured h are impossible. If neither endpoint is h,
E is available, and A/B is available exactly when that internal type
exists. An endpoint already supplying the occupied type needs no extra
vertex. Each permitted regime is realized: keep the forced endpoints,
choose one extra vertex of that type if needed, and give every other path
vertex colour 1-h. These are explicit witnesses for every claimed state.

For even k>=4 the internal path contains both types and endpoint types
differ. The four endpoint patterns (neither, first, last, both h) give
3,1,1,0 regimes per h. Thus equal poles give ten states, plus the previous
six:16. For odd k>=5 the endpoint types agree; regime counts 3,1,1,1 give
twelve plus six:18. Relations and availability depend only on endpoint
types and internal-type existence. This proves E/O for all k.
For k=3 only the type opposite to the endpoints exists internally; counts
2,1,1,1 give16 states, all in the odd profile. For k=2 no internal type
exists; counts1,1,1,0 give12 states, all in the even profile. This proves
I3/I2 including their direction. The finite checker is not the proof.

## 4. Unequal profiles do not invalidate the one-sided lift

Take T=A and boundary colours (p,a,q,b)=(0,1,0,1). In P(5,A), colouring
its internal A vertex 0 and all other path vertices 1 gives R={(p,q)}.
In P(3,A) its sole internal B vertex instead gives R={(q,p)} when 0,
or R={(a,b)} when 1. The two profiles are therefore not equal.
Nevertheless EVERY P3 state occurs in P5. This is the direction needed
to lift colourings of the SMALLER graph. The missing LONG-patch state
need not lift backwards. An early unmerged draft incorrectly treated
non-equality as a reason to reject P3; that inference is corrected here
before the first packet. No failed-route claim is made from that error.

## 5. Replacement for every exterior; class preservation

Assume G=P(k,T) union F, with intersection exactly the four distinct
boundary vertices, disjoint interiors, no additional cross arcs, and
consistent directions on shared boundary edges. Every arc of G is
accounted for; internal strip vertices have exactly the listed neighbours.
The same-disk embedding and fixed cyclic order are hypotheses. F may
have additional edges between boundary vertices.

For odd k>=5 choose k0=3; for even k>=6 choose k0=4. Embed P(k0,T) in the
same disk. Since k-k0 is even, the endpoint types and all four boundary
spoke directions match. Use fresh internal vertices. No pq or ab edge
is added. No loop, reverse pair, repeated endpoint pair or new exterior
adjacency is introduced. Consistent shared boundary edges are kept once.
The outside drawing is unchanged and the inside drawing is planar.
Thus G' is a finite simple planar orientation with k-k0>=2 fewer vertices.
No unrestricted directed contraction or boundary identification is used.

Take ANY valid colouring of G'. By E or I3 its short-patch restriction
has a state realized by a valid original-patch colouring. Use that witness
and keep every exterior colour fixed. If the union contained a cross-piece
monochromatic cycle, splitting it at boundary visits would give a cyclic
chain in R_patch union R_F. Those relations are unchanged from G', so the
chain expands there to a positive monochromatic closed walk. Such a walk
contains a cycle: choose equal positions with least positive separation.
This contradicts validity of G'. Cycles wholly in either piece were
already excluded. This proves the lift for ALL exterior colourings.

For even k>=4 one may instead use k0=2 and I2. This adds a->b inside the
disk. Require the exterior b->a arc to be absent, or a digon would leave
the contract class. If F has a->b already, keep its one consistent
direction and remove a duplicate in the planar multiedge drawing; directed
reachability is unchanged. No pq edge is added. Under that guard G' is
again in the class, loses k-2>=2 vertices, and every colouring lifts as
above. The guard is not silently inferred from planarity.

For a minimum-order counterexample, the applicable G' must be colourable
by minimality over the FULL frozen class. Its lift contradicts the assumed
counterexample. Hence no isolated alternating strip of odd k>=5 or even
k>=6 can occur. An even k=4 strip can survive this reduction only if the
exterior contains b->a. No unavoidability theorem is inferred from Euler.
Nonuniform orientations and other degree-four/five cores remain open.

## 6. Scope, finite controls, dependency chain and checkpoint

These profiles are bounded static interfaces. C31's separate core-family
proof shows exact all-action dynamic types can still grow. A root existence
proof needs a lifted colouring, not necessarily legal moves from every
preselected original colouring. The profile replacement and the separate
two-state guarded dynamic policy are distinct sufficient tools. Neither
has been shown to cover an unavoidable family of all remaining cores.

The selected checker enumerates all8160 complete assignments for k=2..9,
both starting types:16 cases,8 equal-profile comparisons,12 one-sided
inclusion comparisons. It checks Kahn acyclicity against positive closure,
exact profiles, full rotations, every face and the quadrilateral boundary.
The P3/P5 non-equality AND inclusion and the P2 reverse-arc digon mutation
are retained. Complete profiles for k=2,3,4,5 are in the saved actual output.
These are controls, not induction or a universal root enumeration.

The frozen source and replay wrapper ran on CPython3.13.5. Source-enforced
bounds: oneCPU,512MiB address space,CPU20s/wall alarm25s,65536-byte output
files,seccomp denial of socket/socketpair/connect; parent timeout30s.
Actual exit code, versions, hashes and output summary are recorded.
No Lean/elan was found in the bounded PATH probe; no elaboration or axiom
report exists. Generator checks and transport CI are not trusted receipts.

The dependency chain is explicit patch -> all-colouring cycle classification
-> profile inclusion -> same-disk smaller graph -> every-exterior lift ->
minimal-counterexample exclusion. Minimality strictly decreases vertex
count; finite path length and finite colouring spaces bound subsidiary
arguments. No hidden converse, probabilistic step or asymptotic inference
is used. C13/C30 provide prior composition context; the needed proof is
included here. T3,T4,C30,C31 and root keep separate admission scopes.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
first_open_configuration: degree4 (2,2) strongly connected deletion outside
 isolated alternating strips; degree5 (2,3)/(3,2) not forced into a safe-policy
 invariant or smaller-patch lift; unavoidability remains open
next_obligation: obligation:opg169-root
next_action: treat nonuniform strip orientation defects, prove every proposed
 all-exterior lift and class-preservation guard, and construct an unavoidable
 family rather than extrapolating finite controls
root_closed: false
