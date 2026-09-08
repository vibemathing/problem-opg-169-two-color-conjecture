# C35: exact unpaid-triangle parameters and a fixed six-port degree-five deletion

Verdict: candidate_only. Status: proof-drafted with bounded generator controls.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: 4acd04bbb3e00edae107188e203eb37f6d7471e1
Primary owner: math-proof. No C27 dependency or repeated nine-donor enumeration.

## 1. Frozen scope and dependencies

An orientation has exactly one direction on every edge of a finite simple
planar graph. Both FULL induced binary colour classes must be acyclic; either
may be empty. Directed cycles and boundary returns have positive length.
The root asks for existence of a colouring, not extension of every prescribed
colouring. When minimality is invoked, it is over the ENTIRE contract class.

Reuse the distinct T3/T4, C32, C33, C34 and nine-donor proof candidates at the
base revision. Their mathematical statements are not trusted admission receipts.
In the selected edge-maximal least-order counterexample, d>=4; t counts exactly
C32 residual pairs assigned to their C33 donor, not arbitrary low-low edges.
The inherited constraints are t=0 at d=4,5; 3t<=d; t<=1 at d=6,7; t<=2 at d=9.
The nine-donor case is NOT enumerated or reopened here. The active ledger is
  gamma(d,t)=(d-4-2t)/d; mu(f)=length(f)-4+sum_corners gamma+h(f).
Every marked pair receives one unit on BOTH incident faces. The present
arithmetic target is all unpaid triangular parameter types, h=0 and sum gamma<1.

This paper distinguishes three domains: the complete integer parameter domain;
actual planar realizations; and genuine minimum counterexamples. Arithmetic
admissibility does not imply either of the latter. A finite graph below certifies
realization and a scoped extension obstruction, not a root counterexample.

## 2. Sharp integer normal forms, including the meaning of minimum

For a fixed integer t>=0 the least permitted degree is exactly
  D(t)=max(3t,2t+4).                                       (D)
Indeed t=0 gives4, t=1 gives6, t=2 gives8, t=3 gives10, t=4 gives12;
for t>=5 the packing bound3t dominates. These are equivalent to the inherited
integer restrictions, including the two-pair d6/7 and triple-pair d9 exclusions.
The word 'least' here means least INTEGER degree at fixed t, not minimum graph
order or an assertion that each pair can occur in a minimum counterexample.

An equivalent normal form is
  a=d-4-2t>=0, 0<=t<=a+4, d=a+2t+4, gamma=a/(a+2t+4).     (A)
Thus the zero-contribution corners are exactly
  (d,t)=(4,0),(6,1),(8,2),(10,3),(12,4).
At fixed t, increasing d strictly increases gamma. This gives exact cutoffs,
not a guessed finite list of degree triples.

For an especially short exhaustive classification put s=d-3t. Then
  s>=0, t>=max(0,4-s), d=3t+s,
  gamma=1/3+2(s-6)/(3d).                                  (S)
There are six low-slack subfamilies s=0,1,2,3,4,5; s=6 is neutral and s>=7
is high-slack. Denote these categories L,N,P. N means gamma=1/3, NOT zero charge.
For low corners put w=(6-s)/d>0, for high corners put v=(s-6)/d>0.
The COMPLETE disjoint unpaid negative-face classification, up to permuting
corners, is:

| Category | Exact additional condition |
|---|---|
| LLL | automatic |
| LLN | automatic |
| LNN | automatic |
| LLP | w1+w2>v3 |
| LNP | w1>v3 |
| LPP | w1>v2+v3 |

No other category is negative. Proof: summing (S) gives
  mu(f)=(2/3)*sum_i (s_i-6)/d_i.                           (SIGN)
There must be at least one L. Separating its positive deficit from P contributions
gives exactly the six rows. Equality in SIGN is the complete zero-face criterion;
reversing the inequality is the complete positive criterion. Strictness is not
lost by rounding. These are finite SYMBOLIC families with unbounded t,d.

A bound on degrees is impossible from these integer restrictions alone:
for every m>=4, the triple (d,t)=(3m,m) at all three corners has mu=-4/m<0.
This is an arithmetic family, NOT a constructed family of plane counterexamples.
Other geometry or previously proved configuration exclusions may cut it down.

An exact endpoint form can enumerate the integer types without approximation.
Fix two corners with gamma1+gamma2=A=p/q in lowest terms, p>=0,q>0, and fix t3.
If A>=1 there is no negative completion. If A=0 EVERY d3>=D(t3) is negative.
If 0<A<1, all and only the allowed negative completions are
  D(t3)<=d3<=floor(((4+2t3)*q-1)/p).                       (END)
This is just p*d3<(4+2t3)*q over integers. If one wants gamma-sorted triples,
also impose d3>=ceil((4+2t3)/(1-gamma2)). Empty intervals mean no completion.
Every negative triple is reached, and fixed t values have sharp integer bounds.
Sorting by ordinary degree alone would be wrong because t changes gamma.

For the donor-free slice t1=t2=t3=0, this reduces to the familiar reciprocal
inequality sum(1/d)>1/2, but that slice is NOT the whole new parameter space.
All old single-payment signs are superseded by SIGN/END for this task.

## 3. A realizable degree-five slice and its exact fixed separator

Select the donor-free slice (d,t)=(5,0) at three corners: mu=-2/5. The C32
complete twelve-vertex orientation in the frozen input realizes this slice
on all twenty faces, has all semidegrees at least two, and has no marked pair
anywhere (there is no degree-four vertex). Consequently h=t=0 actually, not
merely in a convenient projection. We do not call it a minimum counterexample.
It is the first degree-five slice treated here; lower-degree and donor-rich
arithmetic families have not thereby been classified geometrically.

Take internal vertices I={1,10,11} and the six DISTINCT boundary vertices in
cyclic order B=(2,7,8,9,5,6). The COMPLETE patch arcs are
  1->8,1->9,1->11,2->6,2->11,5->6,6->10,7->1,7->2,
  7->8,8->9,9->5,9->10,10->1,10->5,10->11,11->6,11->7.
All three I vertices have complete underlying degree five. Their triangle is
transitive, not a digirth assumption on the entire graph.
A full core rotation is
  2:(7,11,6); 7:(1,11,2,8); 8:(1,7,9); 9:(1,8,5,10);
  5:(6,10,9); 6:(2,11,10,5);
  1:(7,8,9,10,11); 10:(1,9,5,6,11); 11:(1,10,6,2,7).
The face permutation has the hexagonal outside B and ten triangular inside
faces; 9-18+11=2. This is the actual neighbourhood in the complete graph,
not an invented drawing. In a general application this same disk and all I
neighbours/directions must occur. Extra arcs BETWEEN B vertices may lie in the
exterior; they are retained. No extra neighbour of I is permitted.

Q=P-I is just the existing rim, with its actual directions
  7->2,7->8,8->9,9->5,5->6,2->6.
It is a DAG, so all64 boundary colourings are valid Q colourings. For an index
m=sum_i c(B_i)*2^i, choose the internal colour word listed below, with bit0 at1,
bit1 at10, bit2 at11. All other vertices retain their specified colours.

| first index | eight internal words for consecutive indices |
|---:|---|
|0|6,3,2,2,7,3,2,2|
|8|6,6,2,2,6,6,2,2|
|16|5,3,2,2,5,3,2,2|
|24|5,5,2,2,4,4,2,2|
|32|5,3,1,1,5,5,1,1|
|40|4,1,0,0,4,1,0,0|
|48|5,5,1,1,5,5,1,1|
|56|4,1,0,0,4,1,0,0|

Every row is checked from the full arcs: both P colour classes are DAGs, sigma
is unchanged and ALL positive boundary returns in P equal those in Q. The
finite vector is a complete certificate, not a probabilistic sample or merely
a list of good projections. Positive-closure generation and a different DFS/BFS
consumer both check it, with the latter importing no generator predicates.
The certificate retains the full colour vectors, original rotation and faces.

## 4. All-exterior three-vertex deletion, with no reverse-arc exception

For ANY graph G in the contract containing the saturated core above, delete I.
G'=G-I is an actual induced subgraph, so is finite/simple/planar/oriented and
has exactly three fewer vertices. No edge is added, reversed or contracted;
no boundary vertices are identified. Thus there is no new reverse-arc guard.
The three-degree-five condition here is local to I; G' need not preserve it.

Fix ANY valid colouring of G'. Restrict it to Q and use the unique table entry.
Leave every retained vertex, not just B, unchanged. Write F for all exterior
vertices and arcs, including every additional boundary chord. All arcs of G
are in P or F; there are no I-to-exterior arcs outside P.
If a new monochromatic cycle existed, cycles inside P or F are excluded. Cut
a crossing cycle at its boundary visits. Replace each positive P segment by
its same-colour Q path, using R_P subseteq R_Q. Together with all F segments,
this yields a positive monochromatic closed walk in the valid G' colouring.
Taking repeated positions of least positive separation gives a directed cycle,
a contradiction. This proves the lift with the entire exterior fixed.

In a minimum-order counterexample, minimality supplies a colouring of G'; the
lift excludes this specific signed configuration. It does NOT exclude every
transitive triangular face of degree-five vertices, every (5,5,5) rotation, or
every external inverse-arc configuration left by C32/C34.

The checker also retains all actual noncrossing direct exterior chords of B.
There are215 absent/directed chord sets, with13760 full boundary assignments;
11018 are valid on the rim plus actual exterior chords and their chosen lifts
are checked with those SAME chords still present. These are finite controls of
the proof above, not a replacement for quantification over arbitrarily long
external paths. In the complete twelve-vertex graph, all100 valid full G-I
colourings are extended and checked directly, leaving all nine retained colours
fixed. This specifically audits more than local boundary projections.

## 5. Complete-graph failure of the universal facial-triple extension shortcut

The SAME frozen twelve-vertex graph refutes the stronger claim that an arbitrary
facial triple of degree-five vertices can always be deleted and restored from
EVERY valid retained colouring. Its entire arc set and full rotation are in
c35-input.json, copied as the selected witness from the cited C32 source.
This is not a new root counterexample or a repeated four-port shrinking search.

Delete J={0,2,3}. On ALL remaining vertices take colour1={1,6,9}, colour0 all
others (integer mask578). The retained induced colour-class orders are
  colour0:(4,10,5,11,7,8), colour1:(1,6,9).
Thus this is a valid FULL exterior colouring, not just an attainable boundary
projection. The separator for J is {4,5,6,7,8,11}; its colour1 set is {6}.
The eight possible assignments to J, in bit order(0,2,3), fail as follows:

| bits | colour | directed cycle |
|---:|---:|---|
|0|0|0->2->3->0|
|1|0|2->3->7->2|
|2|0|0->4->5->0|
|3|0|3->4->8->3|
|4|0|0->4->5->0|
|5|0|2->11->7->2|
|6|0|0->4->5->0|
|7|1|0->2->3->0|

All arcs occur in the full graph and all indicated vertices have that colour.
The complete graph remains colourable: colour1 mask211, with orders
  colour0:(2,8,3,9,10,5,11), colour1:(6,7,0,1,4).
Minimal order is asserted only for this failure within the full minimum-degree-
five structural class: simple planarity gives5n<=2e<=6n-12, hence n>=12, and
this witness has12 vertices. No minimality among all minimum-degree-four graphs
or among root counterexamples is asserted.

The twenty face deletions of this one graph are scanned and their entire bad
boundary lists retained. Only the stated positive core is used as a universal
local deletion rule. A failed reachability-containment attempt does not by itself
mean no full lift exists; the eight full-graph cycles above supply the stronger
negative claim for J. The failed-route proposal is ONLY the universal prescribed-
colouring facial-triple extension shortcut. The admitted parent route and root
remain open. No impossibility of all other smaller replacements is inferred.

## 6. No new charge is invented; every corner and face stays accounted for

C35 adds a graph deletion rule, not a new payment rule. Retain exactly DC2:
  gamma=(d-4-2t)/d>=0;
  each marked pair pays one unit from its donor to each incident face;
  every donor pays gamma at EACH of its d corners.
Every vertex sends2t+d*gamma=d-4 and finishes zero. Every face, regardless
of whether the new deletion rule applies, has length-4+sum gamma+h. Relative
to the older one-face rule the difference on every face is precisely
  additional donor-side unit receipts - sum_corners(t/d).
Thus reduced contributions on all other adjacent triangles are included.
There are no extra C35 credits, no duplicate payments, and no modification of
t after a hypothetical replacement used to reason about the ORIGINAL graph.

For the full twelve-vertex witness, every vertex has d5,t0: initial1, pays1/5
at each of five corners, final0. Every one of its20 triangles has h0, receives
3/5, and ends-2/5. The certificate records all12 vertex rows and20 face rows,
whose sum is-8. Finding one of its signed faces reducible does not magically
make these numerical charges nonnegative. Rather, a TRUE minimum counterexample
cannot contain that signed configuration. Other realized or hypothetical negative
parameter types remain to be eliminated by genuine local/global arguments.

## 7. Actual controls, provenance and review units

Selected CPython3.13.5 generator and separate consumer ran under one CPU,512MiB,
CPU35s/wall40s/parent43s,1MiB output caps and denied socket syscalls. Both exit0,
no timeout/stderr. The records bind their exact sources, wrapper, inputs,
outputs and interpreter hashes. No existing execution is relabelled as new.
Finite degree cap32 gives188 allowed pairs,1125180 unordered triples:
164078 negative,2034 zero,959068 positive. The six negative family counts are
LLL26235,LLN12879,LNN2385,LLP92085,LNP14355,LPP16139.
The first implementation checks integer strict endpoints; the consumer instead
sums exact rational gammas. Neither finite range is used to prove unbounded SIGN.
Lean/elan are absent from the actual wrapper lookup; no elaboration/axiom report
exists. Both implementations remain the same generator trust domain, not trusted
verifiers. A matching scoped faithfulness/closure review is still requested.

Source comparison: Li--Mohar, arXiv:1606.06114v1, proves the digirth-at-least-four
subclass, as stated in its abstract. Our contract and negative witness permit
directed triangles; that theorem is not used as a missing general-case proof.
Barat--Czett, arXiv:2201.13161v1, uses arc-dicriticality, whereas our minimality
parameter is vertex count. No arc-minimality consequence is imported. These
are attribution/scope notes, not proofs of C35 or evidence of its novelty.

Dependency DAG: inherited degree/packing exclusions -> exact integer domain ->
SIGN/END; explicit saturated plane core + complete lifting vector -> all-exterior
deletion -> conditional local exclusion; full graph + valid retained colouring +
eight cycles -> scoped failure. These chains do not use one another circularly.
Fixed vertex count strictly decreases in the reduction; finite paths and bounded
colour spaces terminate the subsidiary arguments. Probability/asymptotics do not
enter; full-arc reversal and relabelling must transform arcs and relations together.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
best_verified_result: none
root_closed: false
arithmetic_classification_remaining_cases: [] for EXACTLY the stated integer domain
first_open_configuration: unpaid L-containing triangles whose signed actual
 neighbourhood is not the specified six-port degree-five core; lower-degree
 guarded configurations and donor-rich unbounded families remain geometrically open
next_obligation: obligation:opg169-root
next_action: expand one remaining realized signed negative triangle with a fixed
 separator, preserve all external paths/colours, and prove an all-exterior lift
 or a budgeted transfer; do not infer geometric completeness from the six sign rows
