# C30: representative-safe dynamic interfaces and their necessary size cost

Verdict: candidate_only. Status: proof-drafted with bounded generator controls.
Candidate: candidate:opg169-a01-c30-dynamic-proof
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Packet target: obligation:opg169-root
Base: ee72f3d08a26ac2991edc96c2d651641e0f69956
Primary owner: math-proof. No C27 dependency. PR #37 is not resubmitted.

## 1. Scope, exact claims, and the unchanged root gap

Keep finite simple planar orientations, all induced arcs, two indexed
colours 0/1, and possibly empty colour classes. A cycle has positive length;
reflexive reachability is not a cycle. A patch is a finite digraph embedded
in a closed disk with a fixed labelled boundary B and cyclic boundary order.
The interface results below also hold without planarity; an application
as a planar replacement must separately satisfy Section 7.

The remaining root configurations are degree four (2,2) with strongly
connected deletion, and degree five (2,3)/(3,2). T3 and T4 remain separately
identified proof candidates. Conditional on their elementary arguments,
Euler gives 2*n4+n5 >= 12+sum_(d>=7)(d-6)*n_d, and C28 reduces a degree-four
vertex whose neighbours are not in one deletion SCC. Neither argument
forces a reducible configuration among the remaining ones.

C29's nine-vertex example defeats single-vertex plus full-SCC repair from
an arbitrary deletion colouring. It is colourable and is not a root witness.
Its equal static states with different moves motivate the exact repair here.

C30 claims:
(D1) finite, cost-labelled dynamic states for each fixed finite patch;
(D2) every abstract move lifts from EVERY representative, not just one;
(D3) exact synchronized patch composition and quotient composition;
(D4) finite horizon types have boundary-only bounds, but exact all-horizon
     representative-safe types have no boundary-only size bound in general;
(D5) a four-vertex same-patch counterexample to only one refinement round,
     minimum order for a one-vertex boundary under single-vertex moves.
The exact meaning of the size lower bound is proved in Section 6. It is
not a lower bound for every conceivable weak or goal-specific abstraction.
No general repair, smaller root patch, or unavoidable discharging set is
claimed. These are tools and method obstructions toward the open root.

## 2. Static observation and the exact move alphabet

For a valid colouring c of P define L_P(c)=(sigma,R). Here sigma=c|B,
and R contains every POSITIVE monochromatic boundary-to-boundary path,
including paths through other boundary vertices. It is transitive,
irreflexive, and only relates equal colours. It has no empty-path diagonal.
For b=|B| there are at most L=2^(b+b*(b-1))=2^(b^2) labels. This loose
count deliberately includes many unrealizable colour/relation combinations.

Fix a radius r, here r=1 or r=2. A move changes a set D of at most r
vertices SIMULTANEOUSLY and requires both endpoint colourings to be valid.
For r=2 this includes single flips and all two-vertex flips, not only
opposite-colour pairs. Intermediate single flips need not be valid.
It does NOT include arbitrary large SCC palette flips. Such moves need
separate globally consistent labels; they are not smuggled into radius two.

Write S=D intersection B and j=|D minus B|. Label the local move by (S,j).
Keep exact j, not merely whether an interior move occurs. Include an
identity transition with label (empty,0). It is needed when only the other
piece moves. All other moves have 1<=|S|+j<=r.
The action alphabet has size
  A(b,r)=sum_(s=0..min(b,r)) binomial(b,s)*(r-s+1).
For r=2 the sizes are A(4,2)=17 and A(5,2)=23.
The identities are actual unchanged colourings, not arbitrary transitions
between representatives of a static label.

Let X_P be ALL valid colourings. There are N<=2^|V(P)| of them. The labelled
transition system is finite, including the N=0 case. It is defined using
actual induced acyclicity, not predicted neighbour-only blockers.

## 3. Refinement and the universal lifting property

Put c~0 d iff L_P(c)=L_P(d). Given a finite partition ~t, define
  T_(t+1)(c)=(T_t(c), {(S,j,T_t(e)): c --(S,j)--> e}).
Two states are equivalent at the next round precisely when these complete
signatures agree. Use a SET of successor types; multiplicity of equivalent
choices is irrelevant to existence of a matching move.

If N=0, the empty partition is already stable and no refinement is needed.
For N>=1, every round refines the preceding partition because the old type
is a signature component. If it changes, the number of nonempty blocks
strictly increases. It is at most N, so at most N-1 strict refinements
occur (and fewer if the initial partition has more blocks). A stable
partition ~* therefore exists for each finite P. This is an algorithmic termination
proof, not induction from finite experiments. The implementation stops
only when refinement causes no split, not after a preset number of rounds.

If c~*d and c --a--> e, stability says d has an a-successor f with e~*f.
The same holds with c,d exchanged. Their static labels also agree. Thus
~* is a strong action-labelled bisimulation, here proved directly.

Define an abstract edge C --a--> E whenever it has one concrete witness.
For EVERY d in C the preceding implication supplies a successor f in E.
An entire finite abstract path therefore lifts from any prescribed start
representative: length zero keeps that representative; for a path of
length t+1 lift the first edge and apply the induction hypothesis to the
remaining t edges. All actual intermediate colourings remain valid.
This is exactly the quantifier that C29's static interface lacked.

The quotient need not compress much. It can have N singleton states.
Its type IDs have meaning only with the frozen system and partition.
Equality of arbitrary numeric IDs in different patches is not equivalence.
To compare different patches use a common disjoint-union refinement or
supply an explicit label-preserving bisimulation relation.

For finite horizon h there is a uniform, though huge, bound. Set L0=2^(b^2)
and L_(h+1)=L_h*2^(A(b,r)*L_h). This bounds the signatures because each
of A actions selects a subset of at most L_h successor types. Equality
at depth h gives an h-step matching argument by induction, with one
remaining depth consumed at each move. It is not an all-horizon guarantee.

## 4. Exact composition, including a shared boundary flip counted ONCE

Let P,F meet exactly in the labelled vertex set B; their interiors are
disjoint, with no interior-to-interior cross arcs. Shared boundary arcs
must agree and occur once in the union. Fix compatible disk embeddings
when planarity is required. The static composition criterion is
  compatible(c_P,c_F) iff sigma_P=sigma_F and (R_P union R_F)^+ has no diagonal.
Cut any cross-piece monochromatic cycle at successive boundary visits
for necessity; expand any cyclic relation chain into a positive closed
monochromatic walk for sufficiency. Such a walk contains a cycle by
choosing a repeated pair of positions of least positive separation.
Cycles wholly in one piece are already excluded. All induced arcs remain.
Consequently restriction is a bijection between valid union colourings
and compatible pairs of valid piece colourings.

Suppose a move in P is labelled (S,jP) and one in F is labelled (S,jF).
Their synchronized candidate has total changed-vertex count
  |S|+jP+jF,                                                    (COST)
NOT 2*|S|+jP+jF. It is a legal global nonidentity move exactly when
1<=COST<=r and its target pair is statically compatible. The boundary
change sets must be identical. Local identity on one side is permitted.

Proof in both directions: a global changed set restricts to local changed
sets whose boundary part is S and whose disjoint interior parts have sizes
jP,jF. Restrictions of a valid global endpoint are valid. Conversely two
such local moves agree at the changed boundary as well as the unchanged
boundary; their endpoint union is a valid colouring by compatibility and
has exactly COST changes. No intermediate states are required for a
simultaneous move. This proves exact equality of transition systems, not
just absence of false-positive examples.

Now replace each piece by its stable quotient. Keep compatible block pairs;
compatibility is constant on a pair because static labels are constant.
Synchronize abstract edges with the same S and apply (COST) and target
compatibility. Any abstract product edge lifts from EVERY concrete pair:
independently use Section 3's universal lifting on the two pieces. Equal
boundary change sets make the lifted target agree on B; static target
labels give compatibility. Thus the two lifts combine into one actual
global move. Every concrete edge projects back. Induction lifts any finite
product path from any representative pair, without inserting an unsafe
boundary move or guessing favourable representatives.

This proof covers b=4 and b=5 without changing the move rule. It also
explains three dangerous shortcuts: failing to synchronize S, forgetting
interior costs, or counting a shared boundary flip twice. For example,
one internal flip in EACH edgeless piece sharing one boundary vertex is
a two-vertex global move, not a one-vertex move. Conversely changing their
shared boundary vertex is one global change, not two.

## 5. Application to the remaining degree-four and degree-five stars

Let P be the star at deleted v and F=G-v, with B=N(v) in its frozen
cyclic order. The star itself is acyclic for every colouring. A target
F-colouring is extendible iff some choice at v gives a compatible product
state. Equivalently, for at least one colour k, R_F contains no k-coloured
return from an outgoing neighbour to an incoming neighbour. For degree
four both blocked colours give the two disjoint return pairs and C28's
noncrossing restrictions. At degree five the (2,3)/(3,2) return condition
is the corresponding disjunction on the larger side. Direction, colour,
and all actual return paths are retained by L; future move possibilities
are retained by ~*, not guessed from L alone.

The set of extendible states is a union of stable quotient blocks since
it depends only on L and the fixed star directions. Therefore if every
block of the deletion quotient can reach this set, every valid deletion
colouring can be repaired by radius-r moves and then extended. Conversely
a concrete failure to reach it is visible in the exact quotient. This is
a sufficient conditional reduction with a correctly lifted path, not a
proof that the condition holds in every planar minimal counterexample.

Actual controls use C29's nine-vertex graph deleting 8 (degree four), and
C28's seven-vertex graph deleting 0,1 (degree five with opposite semidegrees)
and 5 (degree four). Complete arcs/rotations are in the new input; no old
Candidate is replaced. For C29, the 54 deletion colourings have 18 static
labels, then 44 and 54 classes for r=1. For r=2 they refine directly to
54. Hence merely adding one-step data is not enough in the single-flip
case, and the stable exact quotient retains every colouring in this example.
Masks 170 and 146, C29's equal-static-state pair, separate at depth one.
For r=1 masks 85 and 170 cannot reach the extendible set; for r=2 every
valid colouring is already extendible or reaches it in one simultaneous
move. These statements concern this one graph, not all degree-four cores.

The two degree-five deletions each have 34 valid colourings: 30 static
labels refine to 34. Every one reaches an extendible colouring within one
single-vertex step in these fixtures. The two cases explicitly cover
(in,out)=(3,2) and (2,3). They do not establish a degree-five reduction for
all planar exteriors. The checker compares ALL concrete product edges
with the synchronized product and checks the quotient lifting condition
from EVERY concrete compatible pair, for r=1 and r=2.

## 6. An exact dynamic interface cannot generally have a boundary-only bound

For any n>=3 and b>=1 define P_(n,b) as the directed cycle
  x0->x1->...->x_(n-1)->x0
with b-1 new terminal leaves y_j and arcs x0->y_j. All arcs are listed.
B=(x0,y1,...,y_(b-1)). Draw the cycle in a disk meeting its boundary only
at x0, with the leaves on the remaining boundary and their arcs on the
other side of the two cycle arcs at x0. This is a simple planar orientation
with all boundary terminals cofacial and fixed cyclic order. A compatible
rotation at x0 is (x1,x_(n-1),y1,...); cycle vertices have their two cyclic
neighbours and each leaf its sole neighbour. This is a constructive plane
embedding, not a claimed property of every abstract rotation.

Fix boundary colour x0=0. For b=4 use boundary colours (0,0,1,1), and for
b=5 use (0,0,1,1,1). For each t=0,...,n-2 colour x1,...,x_t with 0 and
all other internal cycle vertices with 1. All these colourings are valid:
the only directed cycle contains x0 of colour 0 and at least one colour-1
vertex. They have exactly the same static observation: positive boundary
relations are just x0->y_j for the leaves coloured 0. For b=1 R is empty.

Let e=({x0},0) denote the single boundary-x0 flip, and tau=(empty,1) an
internal single flip. At the displayed colouring with t internal zeros,
e is disabled precisely when t=0: changing x0 would then make the whole
cycle colour 1. Changing leaves never creates any directed cycle.
The shortest tau-only path to a state disabling e has length exactly t.
Each tau move reduces the number of internal zeros by at most one, and
flipping those t zeros one at a time achieves t while keeping x0=0 and
some cycle vertex colour 1. Boundary colours cannot change on a tau path.

Any action-labelled bisimulation preserves whether e is enabled and,
by induction on path length, the existence of a tau-path of each length
to a state disabling e. Thus it preserves that minimum distance. The
n-1 displayed states must lie in different equivalence classes despite
identical static labels. Since n is unbounded, there is NO bound depending
only on b for such exact all-horizon interfaces, even with b=4 or b=5 and
these fixed colour splits. The same argument uses the e,tau subalphabet
when r=2, since exact internal costs keep tau distinct from a double move.

Scope: this is a lower bound for representative-safe, action-preserving
bisimulation or equivalent back-and-forth quotients. It does not rule out
weaker reachability-only summaries, forgetting move counts, or compression
under additional minimal-counterexample structure. The padded graphs have
leaves and need not be strongly connected. Therefore no corresponding
lower bound for the restricted strongly-connected, semidegree-two deletion
class is claimed. The one-boundary cycle itself IS strongly connected.
This is a methodological obstruction, not a conjecture counterexample.

A smallest SAME-PATCH counterexample to just depth-one information already
has four vertices: the directed cycle 0->1->2->3->0 with B={0}. Take colour-1
masks 12={2,3} and 8={3}. Both have boundary colour 0, no positive boundary
return, an enabled boundary flip, an enabled internal flip, and the same
sets of depth-zero successors for every action. Their depth-one types agree.
But from mask 12 an internal flip can reach mask 14, where the boundary
flip is disabled. From mask 8 no single internal flip can do so. Their
depth-two types differ. This explicitly defeats stopping refinement after
adding only one-step successor observations.

Minimality is for r=1, one boundary vertex, and two states of the SAME
simple oriented graph. On at most three vertices an orientation is either
a DAG or a directed triangle. In a DAG all colourings are valid, so within
one fixed graph the boundary colour alone is already a bisimulation label.
In a directed triangle, for a fixed boundary colour the only internal
same-colour counts are 0 and 1; boundary-flip availability distinguishes
them at depth one. The count-1 states have identical labelled successor
patterns because exactly the two constant triangle colourings are forbidden. Thus no smaller
same-patch collision exists. Padding gives four/five-boundary examples but
no minimum total-order claim for those padded examples is made.

## 7. Replacement and admission remain separate gates

For a candidate smaller patch P' one sufficient EXISTENCE-lifting condition
is: for every valid P'-colouring c' there exists a valid P-colouring c with
the same sigma and R_P(c) subseteq R_P'(c'). Every valid exterior colouring
compatible with c' is then compatible with c; the union only loses
reachability entries. This is the all-exterior quantifier needed for a
minimal-counterexample replacement, rederived from static composition.

For a prescribed dynamic lift, additionally supply a relation between
P' and P colourings satisfying that domination and a forward matching
condition for every labelled move with the same boundary S and the same
interior cost j. The synchronization proof then lifts global paths without
changing their allowed costs. A bisimulation with equal labels is an even
stronger sufficient certificate. A numeric state ID or an existential
edge between static states is not such a relation.

Before invoking vertex minimality require a same-disk embedding with the
same distinct boundary vertices and cyclic order; compatible shared arcs,
no unlisted cross arcs, no new loop or opposite pair, duplicates retained
only once with consistent direction, and strictly fewer interior vertices.
Gluing then preserves finiteness, simplicity, planarity and orientation,
and reduces total vertex count. We have not constructed such a P' for all
remaining degree-four or degree-five cores. Quotienting a COLOURING state
graph does not contract the underlying graph or reduce its vertex count.

## 8. Controls, attribution, and next obligation

The new self-contained checker does not import a proof result as an oracle.
It directly checks both induced classes, using Kahn deletion and positive
transitive closure as different cycle tests, enumerates actual flips,
refines partitions, and checks universal block successors and product edges.
Its fixed fixtures include all source rotations and both degree-five signs.
Cycle-family controls use n=3..8 for b=1 and n=4,6 for b=4,5. These support
the implementation only; the unbounded claim is the all-n proof above.
The actual replay uses CPython 3.13.5, a frozen wrapper, one CPU, bounded
wall/CPU/memory/output and denied socket syscalls. Exact execution and
output files record source/input hashes and exit status. No Lean or elan
was found in the runtime probe; no elaboration or axiom report is claimed.
No trusted verifier acknowledgement or EvidenceLink is generated here.

The general method has prior art in labelled transition-system bisimulation
and contracted solution graphs. The source note records primary locators
and exact scope: proper graph-colouring reconfiguration is not our acyclic
digraph problem. All acyclic-path observations, action costs, gluing and
counterexamples needed here are proved explicitly. No novelty is claimed
for partition refinement as a general method.

Dependency DAG: contract -> actual induced colourings -> static composition;
actual flips -> cost-labelled system -> stable refinement -> all-representative
lifting -> synchronized composition. Cycle family + disabled-action distance
-> unbounded exact width. C4 -> one-round shortcut failure. T4/Euler/C28
only locate the remaining root configurations; the interface proofs do not
assume the root or infer it from a control. Invariants are label agreement,
induced arcs and exact changed sets; monovariants are the number of partition
blocks and finite path length in the respective termination/induction proofs.
Symmetry is explicit cycle internal-count comparison or colour complement.
No probability, asymptotic approximation or unchecked limiting step is used.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
new_all_order_candidates: representative-safe finite-patch dynamics;
  exact cost-synchronized composition; no general boundary-only exact width
first_open_configuration: degree-four (2,2), strongly connected deletion,
  noncrossing double return pairs; degree-five (2,3)/(3,2) likewise open
next_action: exploit additional minimal-counterexample structure to bound
  relevant dynamic classes or construct a boundary-dominating smaller patch;
  prove an attainable simultaneous repair and an unavoidable configuration,
  not merely finite per-patch reachability
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
T3, T4, C28/C29, C30 and root retain distinct verification scopes.
root_closed: false
