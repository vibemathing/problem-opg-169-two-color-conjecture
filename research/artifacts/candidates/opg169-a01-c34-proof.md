# C34: conditioned exterior chords, high endpoints, and separated donor pairs

Verdict: candidate_only. Status: proof-drafted with actual bounded generator controls.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: ad6f9d273cc158387961b5f9e0b0ad1b2b033ebe
Owner: math-proof.

## 1. Fresh-state continuation and precise scope

The live main advanced to the merged C33/PR41 while the new independent
implementation was being tested. C33 is reused, not retransmitted. C32's
96/640 wheel and 288 pair types, C31's all-exterior strip lifts, and C33's
exterior-face/donor results remain separate candidate dependencies, not
trusted receipts. The nine-vertex frozen-colouring and exact-width dead
ends are not reopened. There is no C27 dependency.

An orientation assigns one direction to each edge of a finite simple planar
graph. A valid binary colouring makes BOTH FULL induced classes acyclic;
unused colours are allowed. Boundary reachability is positive, includes
paths through other boundary vertices, and has no diagonal in a valid class.
For conditional minimum-counterexample conclusions choose an edge-maximal
least-order counterexample, hence a triangulated plane representative as
in C32. This selection does not assert every least-order graph is triangulated.

The increment is to retain the ACTUAL outside boundary chords as part of
the lift test, derive a degree bound on both path endpoints of a residual
pair, and improve C33's donor packing. The allocated finite stage contains
one outside triangle, old-port closures, and two adjacent outside triangles
with one common new third. Different-third larger annuli are NOT classified.
No new assumption about their absence is made.

## 2. Interface and all direct outside-chord conditions

Use the unchanged C32 codes C0=(1,78), C1=(1,100), C2=(3,43), C3=(5,77).
Boundary order is (0,1,2,3), interiors u=4,v=5. Rim bit i reverses i->i+1.
Internal b bits reverse, in order,
 [(0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5)].
The base rotation is
 0:(1,4,5,3); 1:(0,2,4); 2:(3,5,4,1); 3:(0,5,2);
 4:(0,1,2,5); 5:(0,4,2,3).

The ear E(e,w) inserts a new vertex6 between e,e+1 in the boundary.
Bits0,1 choose 6->e and 6->e+1 when set, their reverses otherwise.
The cap C(j,w) fills the corner j by the actual outside face(j-1,j,j+1),
adds j-1->j+1 when w=0 (reverse when1), and makes j interior.
The wrap W(j,w) absorbs the two actual outside faces(j-1,j,6),(j,j+1,6).
For endpoints(j-1,j,j+1), bit i=1 chooses 6->endpoint. It replaces j by6
in the four-port boundary and retains j as a third interior vertex.
All original arcs remain. The full rotations, faces and boundary-first
relabellings are saved per case. Every newly internal vertex is tested
against both semidegrees>=2; boundary vertices may still have outside neighbours.

At a fixed new boundary B, let E_out be ALL direct exterior boundary chords.
Their unordered pairs are distinct from the chords already drawn inside P.
Chords on the complementary disk cannot have alternating endpoints. Every
noncrossing subset with every direction is enumerated. There are21 possible
E_out assignments for each five-port ear (one diagonal pair already inside),
five for each four-port wrap, and one for each three-port cap. This covers
all actual direct boundary-edge data of this stage, not all possible long
exterior paths; those are handled by the quantified composition argument.

For each actual E_out the test is
 for EVERY valid colouring d of Q union E_out, supply a valid colouring c
 of P union E_out with the SAME boundary colours and
 R_(P union E_out)(c) subseteq R_(Q union E_out)(d).           (L_E)
A Q with an arc opposite to E_out is rejected, not assigned a colouring.
Q must keep the entire current rim and embed in the same disk with fewer
interior vertices. Known inside boundary chords removed with P have no
separate exterior copies in a simple graph. No untested reverse-arc guard
is silently ignored.

Fix ANY valid colouring of Q union E_out union F, where the remaining exterior
F meets the patch only in B. Its restrictions are valid. A cross-piece
monochromatic cycle cuts into a cyclic chain of positive boundary paths.
By (L_E), every P-side chain entry is also a Q-side entry, so expanding
would create a positive monochromatic closed walk in the valid smaller
graph. Such a walk contains a cycle. This proves the full lift, keeping
EVERY exterior vertex colour fixed, even when F has arbitrary long paths.
The graph replacement keeps B and its cyclic order, removes all P interiors,
uses fresh Q interior labels, and changes no external arc. Same-rim directions,
noncrossing disks and tested reverse conflicts ensure simple/planar/oriented;
the vertex loss is |V(P)|-|V(Q)|>0. No directed contraction is assumed.

## 3. Finite completeness and executed catalogue

The maximal smaller disks have the following skeleton counts by interior count:
 B3: 1,1,6; B4: 2,5,40; B5: 5,21 (at most one interior).
For one interior, its cyclic boundary-neighbour set determines a fan and
triangulated intervening polygon gaps. For two adjacent interiors, their
edge has exactly two common boundary neighbours; a third would force a
nonfacial triangle containing a boundary point inside the disk. Contracting
that edge gives a one-interior skeleton, and splitting its neighbour cycle
at the two common ports recovers exactly the enumerated adjacent cases.
For two nonadjacent interiors with at most four ports, both have degree3
and lie in distinct triangles of a boundary triangulation; an interior
adjacent to all four ports leaves only triangles incident with it, so the
other could not avoid it. These give the remaining models. Every generated
vertex link, face permutation, connectedness and Euler characteristic2 is
checked. All nonrim directions are visited. Sparse boundary-only options
are also included to avoid unnecessary guards; the source freezes ordering.

A nonmaximal smaller same-rim graph can be completed on the same vertices
to a triangulated disk. Missing directions may be chosen consistently with
any E_out edge on that pair. A valid (L_E) lift for the original Q remains
one after completion: fewer Q colourings remain and their relations grow.
Thus a negative over all compatible maximal models also excludes that
sufficient containment criterion for every smaller same-rim graph. It does
not by itself prove failure of every exterior-dependent lifting method.

The four real batches cover224 geometries:64 ears,32 caps,128 wraps.
Sixty are excluded by their newly internal small semidegree. The rest give
1796 geometries-with-E_out:1344 ears,12 caps,440 wraps. Of these,420 have
selected complete lifting maps (0,10,410 respectively). These are exact
finite scope counts, not an inference about all planar graphs.

| Residue | ear positive/total | cap positive/total | wrap positive/total |
|---|---:|---:|---:|
| (1,78) |0/336|3/4|108/120|
| (1,100)|0/336|3/4|108/120|
| (3,43) |0/336|2/2|95/100|
| (5,77) |0/336|2/2|99/100|

For C0/C1 wraps at the still-open other pole j=2, E_out in normalized
boundary (0,1,6,3) ranges over empty,0->6,1->3,6->0,3->1:
 bits0,1,3,7: all except 3->1 have a rule;
 bits2: none have a rule;
 bits4,6: all five have rules (some need two Q interiors);
 bits5: precisely 0->6 and1->3 have a rule.
For C2 at corner0,bits5, all five remain negative. For C3 at corner0,bits5,
only the normalized exterior2->0 remains negative. Other admissible wraps
are covered, sometimes by choosing different rules for different E_out.
The stored labels specify every conversion to original vertex names.

A concrete NEW positive case is C0,W(2,5). Its extra arcs are6->1,2->6,6->3.
If the actual exterior has0->6, delete interiors2,4,5 and add1->3 inside.
If it has1->3, instead add0->6 inside. In each case two exterior diagonals
cannot coexist on that side, so the other pair has no reverse exterior edge.
The current rim is1->0,6->1,6->3,3->0. The two diagonals are drawn on
opposite sides of that rim, so the construction stays planar.
In boundary-first order (0,1,6,3,2,4,5), BOTH choices use the sixteen-entry
full lift vector
 [null,17,null,19,100,21,102,null,null,25,26,27,44,null,46,null].
Null means the smaller colouring is invalid after retaining E_out. Every
other value encodes all seven original colours. The map verifies (L_E),
not just the existence of one good boundary assignment. Order falls by3.

## 4. Both path endpoints of every residual pair have degree at least five

In each C0--C3 pair call ports1,3 the path endpoints a,b. C33 separately
proved that the distinguished same-direction pole p (0 for C0/C1,2 for
C2/C3) has degree>=6 in the selected minimum counterexample.

Claim: d(a)>=5 and d(b)>=5 there.
Each endpoint has exactly three neighbours inside the base disk: the two
poles and its adjacent original interior. If it had degree4, its outside
wedge would have exactly one extra neighbour z. If z is new, the two actual
faces enclose W at that endpoint. Exactly four of the eight direction
choices satisfy its two semidegree lower bounds. ALL of those choices, for
both endpoints and every residue, have a rule adding NO new boundary chord.
The32 complete maps are exposed in endpoint-lifts.json and are separately
checked against every full smaller colouring. Hence they need no exterior
reverse-arc condition; they retain z with all its other external neighbours
and delete at least two of the old interiors. Minimum order gives a colouring
of the smaller graph, and its all-exterior lift contradicts noncolourability.

If z is the OTHER old endpoint, the two actual outside triangles fill the
complementary quadrilateral. No unlisted exterior remains. In particular
the distinguished pole p still has degree4, contradicting C33's degree>=6.
Equivalently its donor-cap lift applies. It is NOT correct to say every
old-endpoint identification has a degree3 vertex: which vertices have degree3
depends on the chosen diagonal. The degree>=6 contradiction handles the
needed identification without that shortcut. z cannot be an already adjacent
pole or the saturated original interior vertices; there is no further case.
Degrees<4 were already excluded. This proves the claim for all four residues.

The finite maps are proof-candidate certificates for a fixed finite list;
the embedding wedge and minimality argument above apply at every graph order.
They are not a new admitted obligation or trusted verifier conclusion.

## 5. Improved donor packing, with the whole debit/credit ledger retained

Use EXACTLY C33's marked residual pairs and distinguished donors. Let t(p)
count assigned pairs at p. Each pair is a maximal length-two equal-direction
run in p's cyclic spoke word. Different such pairs have disjoint two-vertex
sets. Section4 shows that each pair's preceding and following neighbours
in this rotation have degree>=5, whereas both paired neighbours have degree4.
Assign to each pair its immediately following endpoint in a fixed rotation
sense. These t endpoints are distinct, and none belongs to ANY marked pair.
Thus there are at least3t distinct neighbours, proving the ALL-DEGREE bound
  t(p)<=floor(d(p)/3).                                      (PACK)
This does not follow merely from finite word tests. C33 already supplies
d(p)>=6 at donors. In particular (PACK)<=d-4 for d>=6, so its existing
one-unit opposite-face payments remain funded.

Initial charges are d(v)-4 and length(f)-4, total-8. Retain C33's rule:
for each assigned pair uv, donor p sends1 to the opposite face q-u-v;
it then distributes d(p)-4-t(p) equally over its own incident corners.
A vertex sends exactly its initial amount, every transfer is nonnegative,
and every vertex ends0. With h(f) counting received unit payments,
 mu_new(f)=length(f)-4 + sum_corners (d-4-t)/d + h(f).        (LEDGER)
The improved guaranteed corner remainder at a donor is
 (d-4-t)/d >= (d-4-floor(d/3))/d.
For d=6,7,8,9,10,11,12 this lower bound is respectively
 0,1/7,1/4,2/9,3/10,4/11,1/3.
It is an improved BOUND on a funded remainder, not charge added to the system.
No payment is counted once per overlapping patch: every corner and every
marked edge has its own single debit and credit in (LEDGER).

Targeted opposite triangles and all faces of length>=4 remain nonnegative.
The donor-side triangle p-u-v has no unit payment from its other edges,
since p>=6 and those edges do not join two degree4 vertices. Its exact
charge is -(4+t(p))/d(p), still NEGATIVE. This identifies rather than hides
the surviving deficit. F1--F6 have not been eliminated and total remains-8.

For comparison only, under the OLD C32 uniform-corner rule the six inner
faces of a residual pair sum to 4-12/d0-12/d2-8/d1-8/d3. The new endpoint
bounds and C33's donor bound make this at least-21/5 for C0/C1; for C2/C3
the other pole also needs degree>=5 from its small local semidegree, giving
at least-18/5. These are alternative OLD-ledger bounds, not extra credits
added to (LEDGER). The distinction prevents charging the same money twice.

## 6. An analytic seven-vertex obstruction after a wrap expansion

For C0,W(2,2), add1->6,6->2,3->6 to the old C0 arcs. The boundary is
(0,1,6,3) and interiors are(2,4,5). The complete rotation is
 0:(1,4,5,3); 1:(0,6,2,4); 2:(3,5,4,1,6);
 3:(0,5,2,6); 4:(0,1,2,5); 5:(0,4,2,3); 6:(1,3,2).
Give ALL four boundary vertices colour0. Avoiding cycles0->4->1->0,
0->5->3->0 and2->3->6->2 forces4,5,2 all to colour1. Then2->5->4->2
is monochromatic. This rejects all eight interior assignments; the audit
output lists an actual cycle for each, not a timeout or a missing search hit.

ANY smaller same-rim replacement has at most two interiors. Give all of them
colour1. That class has at most two vertices and is acyclic in a simple
orientation without digons. The boundary majority has the four source-to-sink
arcs {1,3}->{0,6}. Its only possible extra edges join the two sources or the
two sinks; orienting either cannot create a directed cycle. Thus the boundary
colouring is valid in EVERY such smaller patch, while it has no extension
in the original. A rim-only exterior suffices to defeat an all-boundary lift.
This proves impossibility beyond the finite maximum-model criterion.

The patch itself has the valid colouring ones={0,2}; the other class has
order(5,4,1,3,6), and0,2 have no same-colour arc. It is not a root counterexample.
Seven is the size forced by this specified four-port/three-interior wrap
interface, NOT a global minimum among all planar lifting obstructions.
Boundary vertices may acquire outside neighbours in a full graph; the new
endpoint and donor degree conditions are not presumed to hold inside this
small disk by itself. Its possible occurrence in a true minimum counterexample
with those outside neighbours has not been excluded.

## 7. Replays, audit scope and exact limitations

Four allocated batches were actually executed with the SAME frozen source
and input on CPython3.13.5, each exiting0 with empty stderr and no timeout.
Each uses one CPU,768MiB address space,CPU55s,wall alarm60s,parent65s and4MiB
output-file caps; socket/socketpair/connect are denied by seccomp. Exact
commands, source/input/wrapper/executable hashes and raw-output hashes are
in executions.json. The previous all-residue development invocation was
interrupted by the tool deadline without a complete result/exit receipt;
it is not counted as a completed check. Partitioning was the recovery.

A separate implementation uses recursive DFS for cycles and explicit path
search for positive relations, without importing the catalogue generator.
Its actual run checked all224 original geometries, all420 selected conditional
maps and5962 valid smaller assignments,97 retained plain maps,32 endpoint maps,
and the explicit eight-cycle obstruction. It additionally checked8128 binary
words and24156 permitted markings through degree12 as controls for (PACK).
It exited0 under one CPU,512MiB,CPU30s/wall35s,parent40s,65536-byte outputs
and the same socket denial. It does NOT claim to have repeated every negative
maximum-model search; those are reproducible from the primary frozen checker.

The compact certificate losslessly retains every allocated case, all selected
positive full lifting maps, original profiles, arcs, rotations, model library
and exterior chords. Per-option negative mask vectors are NOT committed:
they regenerate in the primary batch raw outputs, whose four exact SHA256
values are bound in the archive/records. The archive has an explicit omission
field, not a false full-raw-output claim. Endpoint maps are additionally readable.
No hidden reasoning, full chats, credentials, host paths or external full texts
are saved. No new Lean source or elaboration/axiom report is supplied; recorded
PATH probes found neither lean nor elan. All checks are generator controls,
not registered verifier receipts or mathematical admission.

## 8. Dependency DAG and next root work

C32 geometry/encoding -> exact expanded stage and external chords -> finite
(L_E) maps -> all-exterior strict-size lifts. C33 donor>=6 + endpoint maps
+ exhaustive endpoint wedge identifications -> endpoint>=5. That endpoint
bound + disjoint marked runs -> (PACK) -> funded remainder bound in (LEDGER).
The explicit cycles and boundary sources/sinks separately prove the wrap
impossibility. None of these arrows uses a finite sample as induction.

All definitions, directions and changed boundaries are frozen. Strict finite
vertex decrease is the minimality measure; finite colouring and edge catalogues
bound the controls. Full induced classes and fixed exterior colours are lift
invariants. Probability/asymptotic approximations are inapplicable. Cyclic
rotation and all-arc reversal transport the stated local claims, not an
unproved global representative selection.

first_open_configuration: C0,W(2,2), with high donor d0>=6, endpoints d1,d3>=5,
 and actual further exterior neighbours; C0,W(2,5) when neither successful
 directed exterior chord is available; high-donor distinct-third wedges.
next_action: absorb the second DISTINCT outside neighbour of the high donor
 or a high endpoint; prove a new strictly smaller all-exterior lift or a
 genuine global restriction on the bad boundary colouring. Then account for
 the remaining donor-side negative charge and the degree5 F2--F6 types.
failed_shortcuts: retain C33's single-ear and C32 same-four-port obstructions;
 the explicit W(2,2) now also forbids repeating the same-rim <=2-interior search.
T3,T4,C31,C32,C33,C34 and root have separate statement-faithfulness scopes.
checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
best_verified_result: none
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
root_closed: false
