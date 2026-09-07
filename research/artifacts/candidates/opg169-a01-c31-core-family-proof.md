# C31: leaf-free core families, exact dynamic width, and a two-state safe policy

Verdict: candidate_only. Status: proof-drafted with bounded generator controls.
Candidate: candidate:opg169-a01-c31-core-family-proof
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Packet target: obligation:opg169-root
Base: bcffc6fe5ed24d412a3100ec75adb9178e770c9e
Primary owner: math-proof. C30 is a candidate dependency, not Evidence.
No C27 extension and no retransport of C28/C29/C30.

## 1. Scope and the new distinction

An orientation has exactly one direction per edge of a finite simple planar
underlying graph. A valid binary colouring makes BOTH full induced colour
classes acyclic; unused colours are allowed. Directed cycles and the
boundary relation have positive length, unlike reflexive reachability.

T3, T4, C28/C29, C30 and root keep their separate statement identities.
The root asks for SOME valid colouring of every graph in the contract.
Failure to repair one deletion colouring, or to bound a chosen exact
abstraction, is not failure of that existential assertion.

C30 proved a representative-safe dynamic interface by action-labelled
bisimulation and exact synchronization. Its general width obstruction used
leaves when the boundary had four or five terminals. That obstruction did
not meet the root-directed structural conditions. This candidate removes
that particular limitation by explicit LEAF-FREE families:
- every vertex of the completed graph has both semidegrees at least two;
- the underlying minimum degree is four and the plane graph triangulates;
- the selected vertex has degree four or five;
- deleting it leaves a strongly connected graph;
- arbitrarily many colourings have the same full static boundary state,
  block both restorations, but have distinct exact dynamic types.

These are the AVAILABLE local necessary conditions, not the full global
minimum-counterexample hypothesis. Every completed graph below has an
explicit valid colouring. No graph here is a root counterexample, and no
lower bound for a class additionally assuming noncolourability/minimality
is asserted. In particular earlier global low-strip bounds, if applicable
to an actual minimum counterexample, are not invalidated by colourable
examples of arbitrary size.

A second conclusion avoids a different overstrong requirement: for the
specific degree-five blocking states, a TWO-state one-sided safe policy
repairs them uniformly in the size of the family. Exact preservation of
ALL moves is not needed to certify a chosen successful move. The policy
has a proof of composition soundness with conservative reachability labels;
it is not a smaller graph replacement or a root discharging proof.

## 2. The degree-four family and its full oriented embedding

Let L>=4 be even, m=L-1, and use poles p,q and ring vertices r0,...,r_(L-1).
The graph G_L has precisely the ring arcs
  r_i -> r_(i+1 mod L),
and, for each even i, arcs p->r_i->q; for each odd i, arcs q->r_i->p.
There is no p-q edge and no further arc. Put v=r0 and H_L=G_L-v.

Embed the ring as an equator of a sphere with p and q on opposite sides.
A complete rotation system is
  p: (r0,r1,...,r_(L-1));
  q: (r0,r_(L-1),...,r1);
  r_i: (p,r_(i-1 mod L),q,r_(i+1 mod L)).
Thus the underlying graph is the planar bipyramid, not an abstract drawing
assumption. The directions are fixed by the preceding parity rule.
All ring vertices have in=out=2; each pole has in=out=L/2. There are
L+2 vertices, 3L edges and 2L triangular faces, so sum(6-degree)=12.
The minimum degree is four. At v the rotation is (p,r_m,q,r1), with
incoming neighbours p,r_m and outgoing neighbours q,r1.

H_L is strongly connected: an even ring vertex and an odd one give
p->even->q->odd->p. Both types remain when L>=4. Every remaining even
vertex lies on a p-to-q path and every odd vertex on a q-to-p path.
Consequently both poles and every ring vertex belong to the same SCC.
Adding v preserves strong connectivity. Deletion exposes the quadrilateral
boundary B4=(p,r_m,q,r1) up to reversal. No leaf or disconnected component
has been added to create a width obstruction.

## 3. Exact fixed-boundary colourings are a threshold chain

Fix c(p)=0, c(q)=1. For 1<=i<=m define
  t_i = c(r_i) XOR (i mod 2).
Then c is valid on H_L IFF t_1>=t_2>=...>=t_m.

Proof: a monochromatic cycle avoiding the poles cannot occur in the
remaining directed ring PATH. A colour-0 cycle must pass through p, start
its ring segment at an even vertex, and finish at a later odd vertex.
A monochromatic such segment contains an adjacent even-to-odd pair of
colour 0; conversely such a pair and p form a directed triangle. Thus
colour-0 acyclicity is exactly the prohibition of 00 on every even-to-odd
edge. Colour-1 cycles through q are equivalently prohibited by excluding
11 on every odd-to-even edge. For either edge parity these prohibitions
say precisely that (t_i,t_(i+1)) cannot be (0,1). This proves both directions,
retaining every spoke and every ring-path arc.

There are exactly m+1=L such colourings for these opposite pole colours:
  t = 1^k 0^(m-k), 0<=k<=m.
Call the corresponding colouring c_k. Now also fix c(r1)=0 and c(r_m)=1.
As both indices are odd, this is exactly 1<=k<=m-1. Hence ALL valid
colourings with this boundary colouring are c_1,...,c_(m-1).

Each has exactly the same full static boundary observation:
  sigma on (p,r_m,q,r1) = (0,1,1,0),
  R = {(r1,p),(q,r_m)}.
The displayed pairs are direct arcs. Each same-coloured boundary group
has only two vertices; reverse reachability would create a monochromatic
cycle, and different-colour pairs are excluded by definition. Thus no
unrecorded extra boundary relation is possible.

Both colours at v fail for each c_k:
  colour 0: v->r1->p->v;
  colour 1: v->q->r_m->v.
The two return pairs are noncrossing in the frozen rotation. This realizes
the degree-four strongly-connected-deletion double-blocking configuration.

The graph G_L itself is colourable: set p and all even ring vertices to 0,
and q and all odd ring vertices to 1. The two induced graphs have only
p-to-even and q-to-odd arcs. They are DAGs. This is a full witness, not an
inference from an absence of counterexamples in enumeration.

## 4. Exact move distances and unbounded dynamic classes at four terminals

Use C30's action labels (S,j): changed boundary set S and exact number j
of simultaneously changed internal vertices. Radius one/two always includes
an internal single-flip action tau=(empty,1). Let e flip only r1.
Among the fixed-boundary states above, e is enabled IFF k=1: after that
flip t_1 becomes 0, and monotonicity requires all other t_i to be 0.
The tau graph on these states is exactly the path
  c_1 -- c_2 -- ... -- c_(m-1).
A single internal change moves the threshold by one; no other binary
monotone sequence can result. Thus the shortest tau-only distance from
c_k to a state enabling e is k-1.

Action-labelled bisimulation preserves e-enabledness and, by induction
on finite path length, the existence of a tau-path of each length to an
e-enabled state. It therefore preserves that minimum distance. The m-1
states with identical (sigma,R) require m-1 DISTINCT exact dynamic types.
As L grows, there is no bound depending only on b=4, even within the
semidegree-admissible, strongly-connected-deletion structural class above.
The same tau/e subalphabet proves this for radius two; including other
labelled actions cannot erase distinctions in this subalphabet.

There is a further exact all-orders repair-distance statement for this
family. Let d=min(k,m-k). Counting legal recolouring moves of H_L, with
restoration of v performed after those moves, the minimum distances are
  D1(k)=d,
  D2(k)=1+ceil(max(0,d-3)/2).                                (DIST)
D2 permits any simultaneous change of at most two vertices, not just
opposite-colour pairs. All these states are initially blocked, so distance
zero never occurs.

For D1: while B4 is fixed every valid state is a threshold state, and an
internal move changes k by one. The boundary vertices that can move are
r1 or p only at k=1, and r_m or q only at k=m-1. The endpoint assertion
follows from monotonicity. To flip p to colour 1 when k>=2, an even vertex
of colour 1 in the prefix and the odd r_m of colour 1 form the forbidden
cycle p->even->q->r_m->p. To flip q to 0 when k<=m-2 use the odd r1 of
colour 0 and an even suffix vertex of colour 0 in q->r1->p->even->q.
At k=1 flipping r1 gives c_0 and v can be 0; at k=m-1 flipping r_m gives
c_m and v can be 1. Every route to an extendible state must first change
the boundary, giving precisely min(k,m-k) moves.

For the D2 lower bound suppose d>=4. A move changing p but not q, with
at most one additional ring change, cannot be legal: at least two prefix
even vertices and at least two suffix odd vertices have colour 1. Choose
two disjoint even/odd pairs; the two cycles p->even->q->odd->p cannot both
be destroyed by one ring change. The analogous argument forbids changing
q but not p, using two colour-0 prefix odd/suffix even pairs. Flipping
both poles changes no ring vertex; at the threshold edge it creates a
monochromatic triangle with the newly coloured p (k even) or q (k odd).
If neither pole changes, flipping r1 requires making all t_i zero and
therefore k ring changes; flipping r_m requires m-k changes. Both exceed
two. Thus NO boundary-changing radius-two move is possible when d>=4.
An internal radius-two move changes k by at most two. At least
ceil(max(0,d-3)/2) such moves must precede the first boundary change.

For the matching upper bound move the threshold toward its nearer end
in steps of at most two internal changes, until k<=3 or m-k<=3. If k<=3,
flip p and every even prefix vertex from 1 to 0. There is at most one
such even vertex, so this is one radius-two move. The colour-1 class now
consists of p,q and only odd ring vertices, ordered q->odd->p; the colour-0
class is a subpath of the ring. Both incoming neighbours of v now have
colour 1, so v can be 0. If m-k<=3, instead flip q and all even suffix
vertices from 0 to 1; there is at most one. The colour-0 class is ordered
q->odd->p, and v can be 1 because both outgoing neighbours have colour 0.
This proves (DIST) in both directions for every even L, not by extrapolation.

Since H_L is one uncoloured SCC, adding global palette complements cannot
shorten these distances: complementation commutes with every changed set,
preserves move validity, and preserves extendibility. Remove all such
complements from a mixed sequence; the remaining flip sequence is valid
up to global complementation and reaches an extendible state in no more
moves. This statement concerns this family's whole-SCC operation only.

The exact-state-width and distance statements are different. C29 already
has states with NO single-flip repair; this family instead gives arbitrarily
large FINITE repair distances and a particularly transparent observable
witness for unbounded exact dynamic width.

## 5. A leaf-free degree-five companion with both semidegree signs

For even L>=6 split pole p in G_L into a,b. Keep the same q and ring.
Pole a has spokes to r0,r1,r2. Pole b has spokes to r0,r2,r3,...,r_m.
Each spoke keeps the parity rule: pole->even and odd->pole. Add b->a.
Keep all q spokes and all directed ring edges. These are ALL arcs.
Call the graph J_L, still with v=r0, and K_L=J_L-v.

A complete plane rotation is
  a: (r0,r1,r2,b);
  b: (r0,a,r2,r3,...,r_m);
  q: (r0,r_m,...,r1);
  r0: (a,b,r_m,q,r1);
  r1: (a,r0,q,r2);
  r2: (b,a,r1,q,r3);
  r_i, i>=3: (b,r_(i-1),q,r_(i+1 mod L)).
Geometrically split a small disk around the old pole along the rays to
r0 and r2, retaining both endpoint spokes and joining the two new poles.
This adds two triangular faces, with no crossing. Endpoint spokes now have
different pole endpoints, so they are not duplicate edges; b->a has fresh
endpoints and has no reverse. There are L+3 vertices, 3L+3 edges, 2L+2
triangular faces. This is an explicit simple planar orientation.

Semidegrees (in,out) are:
  a: (2,2);
  b: (L/2-1,L/2+1);
  q: (L/2,L/2);
  r0 and r2: (3,2);
  all other ring vertices: (2,2).
Thus all semidegrees are at least two, minimum underlying degree is four,
and v has degree five. Again sum(6-degree)=12. In K_L the directed cycle
q->r1->a->r2->q lies in one SCC. The arcs b->a and q->r3->b include b in
it, and every further even/odd ring vertex is joined through b,q. Hence
K_L is strongly connected. Reversing ALL arcs preserves the underlying
embedding and colouring/move graph, and gives v semidegrees (2,3). It is
not an informal reversal of selected paths or a hidden orientation change.

Fix boundary B5=(a,b,r_m,q,r1) to colours (0,0,1,1,0). As before let
c_k(r_i)=1_(i<=k) XOR (i mod 2), for 1<=k<=m-1, and a=b=0,q=1.
These are exactly ALL valid colourings with the fixed boundary colours.
Colour-1 cycles use q and are excluded exactly by the old odd-to-even
11 prohibition. Colour-0 cycles using b, or using a via its only remaining
outgoing spoke a->r2 and b->a, require an even-to-odd monochromatic ring
segment. Its adjacent 00 edge already gives a triangle with b. Therefore
exactly the same monotonicity t_1>=...>=t_m characterizes validity.
No cycle avoiding poles exists in the ring path.

Every c_k has the same full boundary relation
  R={(r1,a),(b,a),(q,r_m)}.
For the colour-0 triple, the listed two incoming paths to a are immediate.
An a-to-b or a-to-r1 path would make a cycle with an existing incoming arc.
A b-to-r1 path cannot occur since r1 is the path's first vertex and its
other in-neighbour is q of colour 1. An r1-to-b path cannot occur: if it
starts via a, append b->a to make a cycle; if it starts via r2, prepend
a->r2 and append b->a to make a cycle. These exhaust r1's outgoing arcs
in K_L. This audits the entire positive relation, not just two convenient
blocking entries. The colour-1 pair has only q->r_m, as before.

The two restoration cycles are v->r1->a->v and v->q->r_m->v.
Flipping r1 alone is enabled only at k=1; internal single flips, with ALL
five boundary vertices fixed, move k along the same path. Thus the shortest
internal distance to enabling that boundary action is k-1. Consequently
m-1 different exact action-preserving types are required even with b=5,
strong deletion, all graph semidegrees at least two and degree-five v.
Arc reversal gives the same result for the opposite semidegree sign.

Again J_L is colourable: a,b and every even ring vertex have colour 0,
q and every odd ring vertex have colour 1. The colour-0 arcs go
b->a->even or b->even; the colour-1 arcs are q->odd. These are DAGs.
The construction does not assume or exhibit minimum-counterexample
noncolourability. It rules out deriving a uniform EXACT dynamic width
bound just from these structural prerequisites.

## 6. A uniform two-state policy for the degree-five blocking states

Despite the preceding lower bound, every c_k in K_L is repaired by the
SAME single boundary action: flip a from 0 to 1, then give v colour 0.
This is an all-orders statement for the specified family and boundary
state, not a numerical observation about selected L.

In K_L, a has precisely the two incoming neighbours b,r1, both of colour 0.
After the flip a has no same-coloured incoming neighbour, so no new
colour-1 cycle can pass through a; the colour-0 class only lost a. Thus
the move is valid. For restoring v in colour 0, its only same-coloured
incoming neighbour is now b and its only same-coloured outgoing neighbour
is r1. The old static state has no colour-0 path r1-to-b. Removing a from
that class cannot create one. The exact blocking lemma therefore permits
v=0. In the reversed orientation the analogous missing return is b-to-r1,
and the same colour choices work.

An abstract controller has just two states. Its pre-state represents all
c_k; its post-state all c_k with a flipped. The sole action has S={a},j=0.
The pre-label (sigma,R) is exact. After the action the boundary colours
are (1,0,1,1,0), and every actual positive relation is contained in
  R_upper={(a,q),(q,r_m),(a,r_m)}.                           (UPPER)
Indeed a has no same-coloured incoming neighbour, and no colour-0 boundary
relation remains. If k=1 then a's sole outgoing neighbour r2 has colour 0,
so the only positive boundary relation is q->r_m. For k>=2, a->r2->q
adds a->q and hence a->r_m. Thus (UPPER) is the exact union of these
possible relations and is itself transitive and acyclic. Reverse the
relation entries in the reversed graph.

This is a SOUND CHOSEN-PATH certificate, not an exact quotient of all
possible moves. More generally, let an abstract state Q represent a set
Gamma(Q) of valid patch colourings with common boundary colours and
R(c) subseteq U(Q) for every c in Gamma(Q). An abstract action to Q'
with label (S,j) is certified only if EVERY representative has an actual
move with that label into Gamma(Q'). For a compatible exterior move,
synchronize the same S, add interior costs as in C30, and require
U(Q') union R_exterior' to be acyclic. The lifted actual relation union
is a subrelation and is therefore also acyclic. This proves composition
soundness for every representative and every exterior satisfying that
guard. Induction certifies chosen finite controller paths. Completeness
or preservation of unselected actions is NOT required or claimed.

For our post-state, restoration of the star with v=0 satisfies this guard
uniformly: the colour-0 star contributes only b->r1, while (UPPER) contains
only colour-1 pairs. The colour-1 portion of the star has no v and no arc.
Thus no positive cyclic chain is formed. The initial blocked colouring
is a colouring of K_L, not a valid colouring of the full J_L: the controller
first moves in the deletion and only then INTRODUCES v. It does not pretend
there was a valid full-graph start state to be recoloured.

This two-state controller intentionally covers the displayed pre-colourings,
not every colouring of every degree-five deletion. The width lower bound
for exact all-action quotients is consequently no obstruction to a finite
SOUND goal-directed controller. A root argument must still force an
applicable configuration or obtain the needed starting invariant.

## 7. Replacement, finiteness and quantifier boundaries

No underlying graph is replaced in the controller argument. A colouring
state compression is not vertex deletion or contraction. In particular
it does not itself invoke the minimum-counterexample hypothesis.

For a genuine smaller replacement P' one still needs: a same-disk embedding
and distinct identical boundary ports in the same cyclic order; no extra
cross arcs; same directions on shared boundary edges; no loop or digon;
consistent duplicates suppressed; and strictly fewer internal vertices.
For EVERY valid P'-colouring, a valid P-colouring with the same boundary
colours and no larger positive boundary relation must be provided. Then
EVERY compatible exterior colouring lifts by monotonicity of the positive
composition criterion. The guarded one-sided controller above must not be
substituted for this all-smaller-colourings requirement without a bridge.

Per finite patch the exact C30 refinement terminates because there are
at most 2^n colourings and each strict refinement increases the block
count. C31's family proof shows this count cannot be bounded using only
four/five terminals plus the available degree/strong-deletion conditions.
The TWO-state controller is a separate fixed finite object whose invariant
sets are defined uniformly by the explicit threshold family. Its chosen
action is certified from every member of each relevant invariant set.
It does not claim that all root instances share those invariant sets.

The root is existential. A universal repair claim for every initial
colouring is sufficient but stronger than necessary. These method
obstructions must not be taken as evidence against the root.

## 8. Exact finite controls and their limited role

The new checker uses the frozen C30 code only for primitive cycle tests,
static labels, exact flips/refinement and rotations; its SHA-256 is enforced
before import. The new oriented family generator, threshold classification,
repair-distance formulas and two-state controller tests are separate code.
All induced colourings are decided by the actual arcs, not by the predicted
threshold formula. Both Kahn deletion and positive transitive closure check
acyclicity. Rotations, face cyclic order, strong connectivity, semidegrees,
Euler charge and full colouring witnesses are verified explicitly.

Nine frozen cases are selected: unsplit L=4,6,8,10; reversed unsplit L=8;
split L=6,8 in both directions. These are controls, not all planar graphs.
For every case all deletion and completed-graph binary assignments are
checked, not merely the displayed threshold states. The fixed-boundary
valid assignments are compared with the predicted complete threshold list;
all exact quotient classes and repair distances are then computed.

For the unsplit family the complete counts also have elementary proofs.
For opposite pole colours there are L valid H colourings per pole assignment
by the threshold characterization. For equal pole colour s, no s-coloured
even and s-coloured odd vertex can coexist, because with p,q they form a
4-cycle. Conversely their absence excludes every s-cycle, and the other
class is a subpath. Thus per equal-pole assignment there are
2^(L/2)+2^(L/2-1)-1 valid H colourings. Combining both pole choices gives
  |Good(H_L)| = 3*2^(L/2)-2+2L.
In G_L with opposite poles the cyclic monotonicity forces all transformed
bits equal, giving four assignments in total. With equal poles the all-ring
opposite assignment is also invalid on the ring cycle, so the combined
count is
  |Good(G_L)| = 2^(L/2+2).
These identities are derived here, not guessed from the control table.

Selected actual counts:
| Case | H vertices | Valid H | Valid G | Same-label distinct types |
|---|---:|---:|---:|---:|
| unsplit L4 | 5 | 18 | 16 | 2 |
| unsplit L6 | 7 | 34 | 32 | 4 |
| unsplit L8 | 9 | 62 | 64 | 6 |
| unsplit L10 | 11 | 114 | 128 | 8 |
| split L6, either direction | 8 | 72 | 70 | 4 |
| split L8, either direction | 10 | 136 | 134 | 6 |

For unsplit L10 the actual threshold-state single-flip repair distances
are 1,2,3,4,4,3,2,1, and the radius-two distances are 1,1,1,2,2,1,1,1.
For every tested split state, flipping a gives a repair in one move.
The split controller also checks all 57 strict positive monochromatic
boundary relations for its post-colour split; every upper-compatible
relation is compatible with every concrete target representative.
These are abstract exterior STATE controls, not an enumeration of all
outside graphs or all outside recolouring sequences. Section 6 supplies
that general soundness argument.

The selected final source was actually replayed under CPython 3.13.5, one
CPU, 512 MiB address space, CPU35s/wall40s, 65536 bytes per output file,
and seccomp denial of socket/socketpair/connect. Exit code is zero,
no timeout and no stderr. The archived wrapper, input, source and compact
output/record fix the run identity. Earlier development versions are not
used as inputs to the selected final execution. No Lean/elan was found;
no elaboration, axiom report, trusted verifier acknowledgement or receipt
is claimed. Actual generator execution remains candidate_only.

## 9. Claim dependencies, failed shortcut and next root action

Local claim DAG, not new admitted obligation records:
- F4-embedding: explicit ring/spokes -> plane rotation, degrees, strong H;
- F4-threshold: actual mono cycles -> adjacent prohibitions -> monotone bits;
- F4-width: threshold path + observable boundary action -> dynamic distinctions;
- F4-distance: first-boundary-move obstruction + matching explicit moves;
- F5-embedding: audited pole split -> leaf-free planar degree-five family;
- F5-threshold/width: exact cycles and boundary paths -> same threshold invariant;
- F5-controller: certified a-flip + missing return -> restoration; upper-relation
  guard -> one-sided composition soundness for every representative;
- root remains separate: no unavoidable configuration or all-exterior
  smaller graph replacement has yet been established by these candidates.

Proposed failed shortcut: the available semidegree, strong-deletion,
noncrossing-return and Euler conditions impose a boundary-only bound on
exact all-action dynamic types. The explicit colourable families disprove
that inference. This is not a failed root route, a change of T4, or a claim
that global minimality supplies no further useful conditions. C30's exact
composition theorem is unaffected; its per-patch state count may grow.

The analysis freezes all directions, labels and quantifiers. Invariants
are full induced colour classes, fixed boundary colours during tau moves,
and monotone threshold bits. Distances use strict finite path lengths;
finite refinements use their block-count monovariant. The formulas use
ordinary induction only for path lifting, never finite-sample extrapolation.
Colour reversal/global complementation preserve exactly the stated objects.
No asymptotic numerical estimate or probabilistic premise enters the proof.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
best_verified_result: none
first_open_configuration: genuine minimum-counterexample degree-four (2,2)
  strongly connected deletion with double returns; degree-five (2,3)/(3,2)
  not forced into an invariant covered by a uniform safe policy
next_obligation: obligation:opg169-root
next_action: seek goal-directed one-sided certificates for additional
  oriented configurations and prove applicability/unavoidability or an
  all-exterior smaller-patch lift; do not require complete preservation of
  every move or reassert a boundary-only exact-width bound from local degrees
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
root_closed: false
