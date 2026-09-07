# R08 C29: frozen planar deletion, pair moves, and recolouring-safe states

Verdict: candidate_only. Status: proof-drafted with bounded generator checks.
Candidate: candidate:opg169-a01-root-boundary-20260907-proof
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Current packet target: obligation:opg169-root (already admitted).
Base: 39ad97152d3d1f5a4eafbf5037be0181386ce84a
Initial computation source revision: 16b9fbcf379719f4fad59a364151ff36f1bbb772
Primary owner: math-proof. No C27 dependency or extension.

## 1. Frozen domain, dependencies and the remaining root quantifier

An orientation has exactly one directed arc per edge of a finite simple
planar underlying graph. A colouring c:V->{0,1} is valid when BOTH FULL
induced colour classes contain no positive directed cycle. Empty colour
classes are permitted; length-zero reachability is not a cycle. Fix a
plane embedding whenever a rotation or a disk boundary is used.

The root still asks: for EVERY such G, does SOME valid colouring exist?
Neither successful finite tests nor failure of one colouring to extend
answers that question. T3 is the admitted strong-connectivity/delta>=3
necessary condition. T4 is the separately identified semidegree>=2 and
delta>=4 proof candidate from the preceding packet. Neither has acquired
a trusted receipt or admission in this turn. This document reuses their
explicit arguments as proof-draft dependencies, not as EvidenceLinks.

For a vertex-number-minimum hypothetical counterexample, every proper
induced subdigraph remains simple, planar and oriented, with fewer
vertices, and is colourable. The empty graph and loopless singleton have
valid colourings. SCC condensation is a DAG; any directed cycle remains
in a single SCC. Consequently any palette swaps on whole SCCs preserve
an existing valid colouring, with all induced cross-SCC arcs retained.
The prior T3/T4 documents give the full nonempty and SCC proof.

## 2. What the planar charge inequality actually forces

For the nonempty minimum counterexample, n>=3 and m<=3n-6. Combining
this with T4 gives
  2*n4+n5 >= 12 + sum_{d>=7}(d-6)*n_d.                         (E)
Indeed sum_v(6-degree(v))=6n-2m>=12, and delta>=4 leaves exactly
the degree-four and degree-five terms on its positive side.
Thus a degree-four or degree-five vertex exists (in fact n4+n5>=6).
This is the C04 counting mechanism, not a new discharging contradiction.
A proof still needs a colouring-liftable configuration forced by (E).

Deletion preserves the frozen class. No unrestricted directed contraction
is used below: it could create a digon. The SCC reductions change only
colours after ordinary vertex deletion. The later abstract patch rule
requires its class-preservation hypotheses to be proved separately for
EACH actual replacement; it is not a licence to contract arbitrarily.

## 3. Exact degree-four blocking and its rotation constraint

For ANY valid c of H=G-v, colour k fails at v iff there are i->v and
v->o with c(i)=c(o)=k and an o-to-i directed path in H of colour k.
A new monochromatic cycle must use v; deleting v proves necessity.
Adding v to such a simple return path proves sufficiency. The paths
avoid v, all their vertices have the stated colour, and their endpoints
are distinct because loops and opposite arcs are forbidden.

If degree(v)=4 and both colours fail, each colour uses one incoming
and one outgoing neighbour. All four neighbours are different; the two
return paths are vertex-disjoint because their colours differ. Closing
them through v gives two simple curves meeting only at v. Their edge
pairs cannot alternate around v: one curve is a Jordan curve, and the
connected other path minus v lies entirely on one side. Alternating
ends would lie on different sides. This is the C03 nonalternation lemma.

In rotation I1,I2,O3,O4 the only possible pairing is I1-O4, I2-O3.
In rotation I1,O2,I3,O4 either adjacent in/out pairing is allowed.
These are necessary conditions, not existence of the return paths.

## 4. C28 SCC reduction reused; the semidegree-two rule also covers degree five

### S1: a separated semidegree-two side is reducible

Suppose N-(v)={a,b} and a,b belong to different SCCs of H. Start with
any valid colouring of H. If c(a)!=c(b), interchange the two colour
names on the entire SCC containing b. This preserves validity: every
directed cycle of H is confined to one original SCC, whose restriction
is either unchanged or globally complemented. Now a and b have the
same colour. Give v the other colour. A new cycle of that colour would
need a same-coloured incoming neighbour, and none exists. This lifts
the deletion colouring to G. No bound on outdegree(v) is required.

The reversed-arc argument proves the corresponding statement for two
outgoing neighbours in different SCCs. Therefore in a hypothetical
minimum counterexample, the two vertices on EVERY semidegree-two side
belong to one SCC of G-v. This includes the small side at degree five.
It is a conditional reducibility lemma, not a claim Euler forces its
hypothesis. A whole SCC here is not a monochromatic SCC; the latter
is a singleton in an acyclic colour class.

### S2: a nonalternating degree-four vertex needs all neighbours in one SCC

Suppose degree(v)=4 with rotation I1,I2,O3,O4. If the two incoming
neighbours, or the two outgoing neighbours, are in different SCCs,
S1 supplies an extension. Otherwise write A for the SCC containing
both incoming neighbours and B for the SCC containing both outgoing
neighbours. Assume A!=B and take a valid colouring c of H.

If c already extends, there is nothing to change. If both colours are
blocked, Section 3 forces c(I1)=c(O4) and c(I2)=c(O3), with these two
colours different. Complement all of SCC B, leaving A unchanged. The
new colouring of H is valid by the SCC argument. Its neighbour colours
are now alternating around v. Section 3 then rules out simultaneous
blocking, so some colour for v gives a full extension.

Thus in a minimum counterexample EVERY degree-four IIOO vertex has all
four neighbours in a SINGLE SCC of G-v. The fresh C28 proof supplies the missing extra step for the general
rotation: if A and B are different, paths within A between the incoming
pair and within B between the outgoing pair are disjoint. Their incident
edges at v cannot alternate, by the same Jordan argument. Thus that case
is necessarily IIOO. C28 therefore reduces EVERY degree-four vertex
whose neighbours are not all in one deletion SCC, not just one rotation.

Moreover strong connectivity of G makes this neighbour SCC all of H:
simple v-to-x and x-to-v paths give, inside H, a path from an outgoing
neighbour to x and from x to an incoming neighbour. Thus every x belongs
to the same SCC. In a minimum counterexample every degree-four deletion
must be strongly connected. These are reused C28 results, not fresh
claims of novelty or completed discharging. The small-side proof S1
also applies to degree five, where the opposite side has size three.

## 5. Minimal fixed-boundary obstruction and a stronger frozen obstruction

With four distinct boundary neighbours and one restored vertex, the
six arcs v->a,a->b,b->v,v->c,c->d,d->v block both extensions for the
fixed boundary colours a=b=0, c=d=1. A plane rotation is v:(a,b,c,d),
a:(v,b), b:(v,a), c:(v,d), d:(v,c). Its two bounded triangular faces
and one repeated-v exterior face certify the two-triangle drawing.
Four neighbours are necessary by Section 3, so five vertices are
minimum for this fixed-colouring extension failure. This reuses the
preceding M20 example with an explicit rotation, not a new root witness.
It does NOT block recolouring of those boundary vertices.

The new stronger example below blocks every legal single-vertex move,
even without fixing the boundary, and also every combination with whole
uncoloured-SCC palette swaps. It is not claimed minimum in total order.

Let H have vertices 0,...,7 and exactly the following 17 arcs:
  2->0, 0->3, 4->0, 0->5, 0->6, 7->0,
  1->2, 3->1, 4->1, 1->5, 6->1, 1->7,
  2->3, 3->4, 5->4, 5->6, 6->7.
Let G add v=8 and exactly
  0->8, 8->2, 8->1, 7->8.
The arc lists are complete. The underlying G is the bipyramid with
poles 0,1 and equatorial cycle 2,3,4,5,6,7,8,2. Embed the poles on
opposite sides of that cycle. No crossing or repeated edge is needed.
One complete clockwise rotation system is
  0: 2,3,4,5,6,7,8       1: 8,7,6,5,4,3,2
  2: 0,8,1,3             3: 0,2,1,4
  4: 0,3,1,5             5: 0,4,1,6
  6: 0,5,1,7             7: 0,6,1,8
  8: 0,7,1,2.
Its face permutation has 14 triangular faces and 9-21+14=2. Deleting
8 exposes the boundary B=(0,2,1,7). All arcs and rotations are frozen
in the accompanying patch JSON and checked by the finite program.

Give even vertices of H colour 0 and odd vertices colour 1; call this c.
The full colour-0 induced arcs are 2->0,4->0,0->6, with topological
order (2,4,0,6). Colour 1 has 3->1,1->5,1->7, with order (3,1,5,7).
Thus c is valid. For each attempted SINGLE vertex change, the following
new monochromatic cycle forbids the move:

| Changed vertex | Cycle after the change |
|---|---|
| 0 | 0->3->1->7->0 |
| 1 | 1->2->0->6->1 |
| 2 | 2->3->1->2 |
| 3 | 3->4->0->3 |
| 4 | 4->1->5->4 |
| 5 | 5->4->0->5 |
| 6 | 6->1->5->6 |
| 7 | 7->0->6->7 |

Consequently there is no first legal single-vertex move, hence no
sequence of such moves starting at c. H is strongly connected: the
cycle 0->3->4->1->2->0 contains the first five listed vertices, and
5,6,7 each have a path in and out of that cycle. The only entire-SCC
palette swap of H is global complementation. The complement of c is
also frozen. These allowed moves reach exactly {c,complement(c)}.
Neither extends to v: colour 0 at v creates 8->2->0->8; colour 1
creates 8->1->7->8, with complementary statements after a global swap.
This is a complete no-recolouring certificate for the SPECIFIED move set.

G is itself strongly connected, every equatorial vertex has in=out=2,
and the poles have semidegrees (3,4) and (4,3). Its underlying degrees
are seven 4s and two 7s. Thus it meets delta>=4 and (E) with equality:
14=12+2. These facts do not make it a minimum counterexample.

Indeed G IS colourable. Give colour 1 to {0,1,3,5} and colour 0 to
{2,4,6,7,8}. The respective topological orders are (0,3,1,5) and
(4,6,7,8,2). Therefore this witness is an obstruction only to the
universal single-vertex/SCC-repair shortcut, NOT to the root and NOT
to all discharging or all possible multi-vertex reductions.

## 6. Exact simultaneous opposite-colour pair-swap criterion

Let c be any valid colouring of a loopless orientation H. Take x of
colour 0 and y of colour 1. Change both colours simultaneously.
The new colour-1 class is (old colour-1 class minus y) plus x, and the
new colour-0 class is (old colour-0 class minus x) plus y. Each retained
old class is a DAG. Thus the swap is valid IFF BOTH of these fail to exist:
  a colour-1 return path for x avoiding {x,y};
  a colour-0 return path for y avoiding {x,y}.
More explicitly the first path goes from a colour-1 out-neighbour of x
to a colour-1 in-neighbour of x inside H-{x,y}; the second reverses
colours and uses y. This follows in both directions from the exact
single-restoration blocking lemma applied to the two new colour classes.
Equivalently, all old opposite-colour blocking cycles for x must hit y,
and all those for y must hit x. There is no promise that such a pair
exists in every relevant graph, nor that a valid swap makes v extendible.

In the frozen example, simultaneously changing 0 and 7 gives the
colour-1 set {0,1,3,5}, already used in the full valid colouring above.
This pair move escapes although neither individual move is legal.
The finite checker tested the iff on all 832 opposite-colour pairs
across all 54 valid H colourings. This finite test supports the checker;
the general iff follows from the argument above, not from those cases.

## 7. Boundary composition: exact for colourability, not for move lifting

Reuse C13's state (sigma,R): sigma colours labelled boundary B, and R
records POSITIVE monochromatic boundary reachability, including paths
through intermediate boundary vertices. For valid colourings of pieces
P,F with disjoint interiors meeting exactly in B, and no other cross
arcs, their union is valid iff (R_P union R_F)^+ has no diagonal.
Shared boundary arcs, when present, must agree in direction.

Proof: cut a cross-piece monochromatic cycle at boundary visits to
obtain a positive cyclic chain of relation entries. Conversely expand
such a chain into the witnessing paths; it is a positive monochromatic
closed walk and contains a cycle. Pieces themselves were already valid.
This proves both directions and does not discard any induced arc.

For G, P is the four-spoke v-star and F=H. The boundary state of the
frozen colouring is sigma=(0,0,1,1), R={(2,0),(1,7)} in B order.
Four boundary vertices are necessary for this double-blocked degree-four
interface. The checker verifies all 108 combinations of a valid H
colouring and a choice at v; exactly 62 unions are valid.

There is a separate, essential failure of STATIC states as recolouring
states. On the SAME H take d with colour-1 set {1,4,7}. Direct inspection
(or the certificate checker) gives EXACTLY the same sigma and R as c. Their uncoloured boundary reachability is also
identical, since the entire uncoloured graph H is the same.
But changing vertex 0 in d is legal and makes v colourable with 0:
after that change the incoming neighbours 0,7 of v are both colour 1.
Before that change, d has colour-0 order (2,0,3,5,6) and colour-1
order (4,1,7). After it, the orders are (2,3,5,6) and (4,1,7,0).
These orders retain every same-colour arc and directly certify the move.
By contrast c has no legal single-vertex first move. Thus a transition
observed for one representative of (sigma,R) cannot be lifted from
every other representative. C13 never claimed this dynamic property;
its colourability composition theorem is not being contradicted.

The finite graph of all 256 H assignments has 54 valid vertices and
single-vertex component sizes 1,1,52. The two isolated vertices are c
and its complement. Only 44 of the 54 H colourings extend at v. These
are exhaustive results for this H, not a universal reconfiguration bound.
For a fixed finite patch one can retain witness colourings and their
reconfiguration components; no uniform boundary-only connectivity
compression is asserted here.

### A sufficient one-sided replacement rule, with the correct direction

Suppose a smaller P' fits the same labelled disk boundary and orientations,
and for EVERY valid colouring of P' there is a valid colouring of P
with the SAME sigma and R_P subseteq R_P'. For any compatible exterior F,
a valid colouring of P' union F lifts to P union F: the relation union
only loses entries, so cannot acquire a cyclic chain. This is an
existence lift, not necessarily a sequence of legal local recolourings.

To use vertex minimality one must also prove P' union F is finite,
simple, oriented and planar, and has strictly fewer total vertices.
Gluing disk embeddings with the prescribed cyclic boundary order,
compatible shared edges and no additional interior/exterior adjacencies
is sufficient for the planarity part. Suppression of a duplicate edge
is allowed only with its one consistent direction; reverse arcs or
identified distinct boundary vertices cannot be ignored. No universal
P' satisfying these tests for the remaining common-SCC configuration
has been constructed. Deleting the star without strengthening the
boundary constraints fails on the displayed blocked state.

## 8. Execution, provenance and exact limits

The unchanged preceding enumerator and its unchanged 21 fixtures were
actually executed on CPython 3.13.5, under one-CPU affinity, 512 MiB,
20 CPU seconds, 25 wall seconds, 65536-byte per-output-file caps, and
seccomp denial of socket/socketpair/connect. It exited 0. Orders 0..4
covered 761 labelled orientations, 11895 full assignments, 23665 deletion
assignments (23233 valid, 432 rejected), and 46466 extensions. All 21
fixtures and five wrong-semantics controls passed. Output and execution
metadata preserve exact source/input/output hashes. This is generator
execution explicitly requested this turn, not a registered-verifier run.
The actual Python differs from the old request's proposed 3.12.10;
that old request and the Web profile were NOT silently modified.

The new patch checker ran under the same external limits, exited 0,
and checked rotations, all listed cycles, both topological orders,
SCCs, 256/512 assignments, the augmented move orbit, the pair-swap iff,
and exact boundary composition. Its output is separately frozen.
No Lean executable was found by the bounded PATH lookup in this runtime;
no elaboration or axiom report occurred. The existing fixed-version
Lean request remains pending, with no self-signed EvidenceLink.

A separate run already saved by C28 has the same old-enumerator coverage
but different observed timing/output bytes. This turn preserves its own
actual replay rather than re-uploading the old source or the C28 bundle.
The replay archive preserves the two exact executed Python wrappers,
three bounded exploratory searches, their exact input tables and compact
actual outputs. The two-cone-over-path search stopped at its first
8-vertex frozen deletion witness. The atlas searches are discovery only:
one stopped at a 6-vertex frozen graph; the hole search checked 55552
orientations on selected embeddings and found none. One embedding per
skeleton is not an all-embeddings/global-minimality proof. Nine vertices
are deliberately NOT labelled globally minimal. No exploratory search
is interpreted as evidence against the root.

## 9. Claim DAG, failed shortcut and nonterminal checkpoint

Local claims (not newly admitted obligation records; the SCC and
dominance arguments are rederived with C28 attribution):
- claim:opg169-root-scc-side-reduction: valid H colouring -> whole-SCC
  complement -> small-side agreement -> extension (S1).
- claim:opg169-root-iioo-scc-reduction: S1 + planar nonalternation ->
  reduction when incoming and outgoing SCCs differ (S2).
- claim:opg169-root-frozen-patch: explicit oriented spherical map +
  eight cycle witnesses + strong H -> no single/SCC-move escape.
- claim:opg169-root-pair-swap: blocking iff -> exact paired-cycle hitting.
- claim:opg169-root-profile-not-reconfiguration: two explicit colourings
  with one static state but different move availability.
- claim:opg169-root-boundary-dominance: positive-relation composition ->
  one-sided colourability lifting under stated replacement conditions.

Proposed failed shortcut ONLY: every valid deletion colouring at a
low-degree vertex can be rescued by legal single-vertex changes and
whole uncoloured-SCC palette swaps. The frozen witness contradicts this
shortcut. The admitted parent route, T3, T4 and root are not negated.
The authoritative failed-route ledger was read empty; its update is
requested through this candidate packet, not written by the generator.

Definition freeze, explicit witnesses, mutation pressure and invariant
checks are supplied above. SCC palette changes preserve each component's
validity; pair changes use the two exact induced classes; replacement
monotonicity concerns reachability entries. Minimality uses a strict
finite vertex-count decrease. Finite searches have explicit bounds.
No probabilistic, asymptotic or infinite iterative argument is used.

Separate pending review/admission units: existing T3; stronger T4 with
its own exact statement; new SCC/pair/profile claims; and root. Do not
rename T3 receipts as T4, and do not use finite patch success to close root.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none (registered-verifier meaning)
best_bounded_result: executed old finite checks; checked frozen patch;
  proof drafts of S1/S2, pair-swap and boundary-dominance lemmas.
first_open_configuration: degree-four (2,2), strongly connected deletion with
  forced noncrossing return pairs; degree-five (2,3)/(3,2) also unresolved.
next_action: prove a boundary-dominating smaller replacement or an
  attainable simultaneous recolouring for the common-SCC configuration;
  require its exact exterior-state lifting proof and an unavoidable
  discharging bridge, rather than repeating the false single/SCC rescue.
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
root_closed: false
No universal colouring, planar contradiction, or root counterexample
has been obtained in this step. Mathematical research remains nonterminal.
