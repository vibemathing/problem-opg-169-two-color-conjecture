# C32: corner discharging, guarded wheel reductions, and small-interface obstructions

Verdict: candidate_only. Status: proof-drafted with exact bounded generator controls.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: b6fe1706e05b2f488269d47f98c9ac723bec6611
Owner: math-proof. No C27 dependency; no repeated dynamic-width search.

## 1. Frozen quantifiers and what is actually disproved

The root concerns every orientation of a finite simple planar graph and
asks for some binary vertex colouring whose two FULL induced colour classes
are acyclic. Empty colour classes are allowed. Cycles/recorded return paths
are positive; reflexive reachability is used only for SCC membership.

Assume a vertex-number-minimum counterexample only in conclusions explicitly
labelled conditional. T3 and T4 provide separate proof-draft dependencies:
nonemptiness, strong connectivity, both semidegrees at least two, hence
underlying degree at least four. They are not trusted receipts. C28 further
forces strong deletion at degree four. C31 excludes its clean alternating
strips, using the stronger one-sided lifts: odd k>=5 to P3; even k>=6 to P4;
even k>=4 to P2 when the exterior reverse endpoint arc is absent.

A colourable graph cannot refute an implication whose hypotheses include
noncolourability and global minimum counterexample order. The counterexamples
below refute ONLY the proposed bridge from the AVAILABLE local degree,
embedding, strong-deletion and blocked-colouring conditions to occurrence
of a C31-reducible strip. No root or full-criticality counterexample is claimed.
The positive results replace that bridge by an exact charge ledger and
finite guarded direction families, not by another uniform dynamic-width claim.

## 2. A complete discharging rule, including every zero and negative case

Work with the connected simple plane underlying graph, degree >=4.
Faces are counted by their boundary walks, with corner multiplicities.
In a hypothetical minimum counterexample it is also 2-connected: if a cut
vertex separates pieces, colour the proper induced pieces, complement palettes
to agree there, and glue. A simple directed cycle cannot visit two different
pieces through their sole common vertex. This contradicts noncolourability.
Thus facial boundary walks are simple cycles; the corner formulas below
also count multiplicities correctly without this convenience.

Initial charges are mu(v)=d(v)-4 and mu(f)=length(f)-4. Euler gives
 sum mu = (2e-4n)+(2e-4f) = -8.
Rule R: a vertex of degree d gives (d-4)/d to EACH incident face corner.
Every transfer is nonnegative, appears once as a debit and once as a credit.
A vertex sends exactly d-4, receives nothing, and ends at ZERO. A face of
length l receives sum_(v corner f)(1-4/d(v)), sends nothing, and ends at
 mu*(f) = 2l-4 - 4*sum_(v corner f) 1/d(v).                 (CH)
For l>=4, mu*(f)>=l-4>=0. Equality requires l=4 and all four degrees=4.
Faces of length at least five are positive. Only triangles can be negative.

For a triangular face let 4<=a<=b<=c be its incident degrees. Its final
charge is negative iff 1/a+1/b+1/c>1/2. ALL possibilities are:

| Family | Allowed degrees | Final charge |
|---|---|---|
| F1 | (4,4,c), c>=4 | -4/c |
| F2 | (4,5,c), 5<=c<=19 | 1/5-4/c |
| F3 | (4,6,c), 6<=c<=11 | 1/3-4/c |
| F4 | (4,7,c), 7<=c<=9 | 3/7-4/c |
| F5 | (5,5,c), 5<=c<=9 | 2/5-4/c |
| F6 | (5,6,c), 6<=c<=7 | 8/15-4/c |

Proof of exhaustion: a>=6 gives sum<=1/2. If a=5, b>=7 gives
1/5+2/7<1/2, so b=5 or6, with the listed integer c bounds. If a=4,
b>=8 gives sum<=1/2; b=4,5,6,7 yields the four listed bounds.
This proves the all-degree classification, including the unbounded c in
F1; it is six SYMBOLIC families, not a bounded maximum degree assertion.
Zero triangles are exactly (4,5,20),(4,6,12),(4,8,8),(5,5,10),(6,6,6).
All other triangles are positive. Together with zero vertices and the
quadrilateral equality case, this accounts for every zero/negative object.

Since the total remains -8, at least one F1--F6 facial triangle exists.
This is an unavoidable configuration theorem stronger than just locating
an arbitrary degree4/5 vertex. It is NOT yet an unavoidable REDUCIBLE set:
we do not assert that each negative triangle is covered by C31. Sections
3 and 7 give exact obstructions to that missing assertion. Zero charge
itself causes no contradiction and is not claimed to certify reducibility.

For wheel applications one may SELECT an edge-maximal representative among
the least-order counterexamples. Adding a planar edge in either direction
preserves noncolourability, because deleting that arc would preserve any
valid colouring. It leaves the vertex count minimal. A simple plane graph
maximal under such additions is a triangulation (a nontriangular face
admits a missing diagonal, or connectivity/cut separation admits an added
edge). This selection does not say every minimum counterexample is already
triangulated, and does not invoke minimality for same-order arc deletion.
In the selected graph the neighbours around any vertex bound its wheel disk.
Other edges between these neighbours belong to the exterior and stay fixed.

## 3. Minimum-order structural controls against the strip-only bridge

### O6: all degree four, strongly connected after every deletion

On 0,...,5 use poles0,1 and directed ring2->3->4->5->2. Add
  0->2,2->1,1->3,3->0,0->4,4->1,1->5,5->0.
These twelve arcs are complete. Rotation:
  0:(2,3,4,5); 1:(2,5,4,3);
  2:(0,5,1,3); 3:(0,2,1,4);
  4:(0,3,1,5); 5:(0,4,1,2).
This is the bipyramid over a four-cycle, a sphere map with eight triangular
faces. All semidegrees equal two. The four directed triangles
0-2-3-0,0-4-5-0,1-3-4-1,1-5-2-1 also show that deleting either pole or any
ring vertex leaves a strongly connected digraph: the surviving pole/ring
paths connect both parities; one can alternatively follow the displayed arcs.
The checker independently verifies every deletion.

Delete0 and colour1={2,3}, colour0={1,4,5}. The induced orders are
(2,3) and (4,1,5). Both restorations fail on 0-2-3-0 and 0-4-5-0,
with nonalternating pairs in the displayed rotation. In fact the finite
certificate lists blocked deletion colourings for all six choices of v.
Yet G is colourable: colour0={0,2,4}, colour1={1,3,5}; only outward stars
remain. This is not a minimum root counterexample.

A strip with k>=5 path vertices needs at least seven vertices, so cannot
occur. A k=4 strip uses all six vertices. Its nonadjacent poles must be one
of the three opposite pairs. Only pair{0,1} has a uniformly directed
four-vertex ring path with alternating spokes (allow reversed path/pole
labels); the unused closing ring arc is always b->a. For either other pole
pair the equatorial four-cycle has source/sink directions and no directed
Hamilton path. Equivalently the complete labelled audit finds eight P4
occurrences and every one fails the exterior reverse-endpoint guard. Thus
there is no applicable C31 smaller-strip reduction, including guarded P2.

Under simple planarity and all semidegrees>=2, 4n<=2e<=6n-12 implies n>=6.
O6 reaches this bound, so it is a minimum-order counterexample to the LOCAL
structural strip-only bridge. This is not a minimum-order claim for root
noncolourability. Its charge ledger is exact: every vertex starts/ends0;
each of its eight triangular faces starts/ends-1; no transfer occurs.

### I12: an all-degree-five control, covering both semidegree signs

The frozen input gives all30 arcs and a full20-face rotation on12 vertices.
For reconstructibility the arcs are
  0->2,0->4,1->8,1->9,1->11,2->3,2->6,2->11,
  3->0,3->4,3->7,4->5,4->8,5->0,5->6,6->0,6->10,
  7->1,7->2,7->8,8->3,8->9,9->4,9->5,9->10,
  10->1,10->5,10->11,11->6,11->7.
The underlying map is formed by two five-cycles 2..6 and7..11, joined as
an antiprism belt, with pole0 over the first and pole1 over the second.
All degrees are5, semidegrees are(2,3) or(3,2), and all vertex deletions
are strongly connected, checked from these exact arcs. At v=0 and v=1,
blocked deletion masks are242 and1564, with respective cycle pairs
  0-2-3-0 and0-4-5-0;
  1-11-7-1 and1-9-10-1.
Masks encode colour1 at the numbered bit; v is absent before restoration.
All twelve deletion witnesses and both induced orders are in the output.
A full valid colouring has mask211, with orders
  colour0: (2,8,3,9,10,5,11); colour1: (6,7,0,1,4).

No C31 strip with an internal vertex can occur: such a vertex must have
full degree4, whereas every degree here is5. Minimal order is claimed
ONLY for the all-minimum-degree-five structural class: 5n<=6n-12 forces
n>=12. The input is a fixed witness, not an enumeration of all12-vertex
planar orientations. Each vertex starts with1, sends1/5 to each of five
faces, and ends0. Each triangle receives3/5, ends at-2/5; twenty of them
total-8. Thus F5=(5,5,5) is an explicit residual deficit, not a proved reduction.

## 4. Exact all-exterior lift condition and the finite direction encoding

For a valid patch colouring c record its positive monochromatic boundary
relation R(c). If P and F meet exactly in B, have disjoint interiors and
no other cross arcs, a compatible union colouring is valid iff
(R_P union R_F)^+ has no diagonal. Cut a cross-piece cycle at boundary
visits for one direction. Expand a cyclic chain into actual coloured paths
for the other; a positive closed walk contains a simple cycle. Shared
boundary arcs agree and every induced arc is retained.

Hence this sufficient test supports a true smaller replacement Q:
 for EVERY valid colouring d of Q, provide a valid c of P with the SAME
 boundary colours and R_P(c) subseteq R_Q(d).                (LIFT)
Any exterior colouring compatible with d stays fixed; the relation union
only loses entries, so cannot acquire a cycle. This is an existence lift,
not a path of legal single-vertex moves from a prescribed starting colouring.

For a wheel W(d,s,r), boundary labels are0,...,d-1 in cyclic order, centre=d.
Bit i of s is1 for i->centre,0 for centre->i. Bit i of r is1 for the rim
arc (i+1 mod d)->i,0 for i->(i+1 mod d). The complete sphere rotation is
 centre:(0,...,d-1); i:(centre,i-1 mod d,i+1 mod d).
There are d inner triangular faces and the outer d-cycle. Only s of weight2
for d4, and weight2 or3 for d5, are relevant to T4. Thus ALL labelled wheel
direction types number96 and640. This has not bounded any exterior path.

Try boundary-only Q keeping every rim arc and adding noncrossing diagonals.
For four terminals there are five options: empty or either diagonal in
either direction. For five terminals there are31: empty, ten one-diagonal
options, and twenty two-diagonal triangulations. Completeness follows from
noncrossing diagonals of a convex polygon; no polygon has more than d-3.
Every extra arc x->y requires exterior y->x ABSENT. An already present
x->y is kept once. The replacement embeds in the same disk with unchanged
boundary, no interior/exterior cross arcs or identified labels. Deleting
the centre decreases vertex count by one. The boundary-only graph is simple,
oriented and planar. Required reverse-arc guards are not inferred from
planarity or omitted from the claimed reduction.

All labelled types and all Q options were checked against (LIFT) using
full boundary colours and both centre colours. The finite output preserves
one lifting map for every positive orbit representative, not merely a yes/no.
The full labelled rule table is deterministically streamed into its recorded
SHA256; regeneration order is frozen in the code. These are finite certificate
candidates, not a registered verifier's approval. Counts:

| d | Labelled types | Types with a rule | Without a rule | Orbits | Residual orbits |
|---|---:|---:|---:|---:|---:|
|4|96|66|30|13|5|
|5|640|480|160|32|8|

Orbits use exactly boundary dihedral symmetries and reversal of ALL arcs.
Those bijections preserve acyclicity, containment of R, disk embeddings,
and transform guards/colour witnesses as well. No other symmetry is assumed.

An explicit rule with a direct proof, independent of the table, covers
W(4,3,0): replace by its rim plus0->2, provided exterior2->0 is absent.
If c(0)=c(1), give the centre the other colour; it has no same-coloured
incoming neighbour and contributes no new boundary path. If they differ,
give the centre c(2). Its unique incoming neighbour of that colour is either
0 or1. Q already has respectively0->2 or1->2. Any same-colour outgoing
neighbour is2 or3, and if it is3 it is reached via2->3. Thus each same-colour
segment through the centre is replaced by a Q path, proving both acyclicity
and R containment. W(5,3,0) has the analogous rule adding0->2 and2->4,
with reverse guards2->0 and4->2; the same c(2) choice uses2->3 or2->4.
This also gives the arc-reversed degree-five sign. The other finite rules
have their explicit all-assignment lifting maps, checked against actual arcs.

## 5. The complete residual wheel types, and real small-patch obstructions

Canonical residual codes (s,r), NOT unspecified rotation words, are:
 d4: (3,2),(3,3),(5,0),(5,1),(5,5);
 d5: (3,2),(3,3),(3,10),(5,4),(5,5),(5,7),(5,8),(5,9).
Their orbit sizes are8,8,4,8,2 for d4 and20 each for d5. All arcs and rotations
reconstruct from Section4. Each representative has a COMMON boundary colouring
that is valid in EVERY listed Q but has NO colour for the original centre.
The output gives that colouring, both explicit blocking cycles, and all
common masks. This is stronger than simply failing the sufficient test:
it proves these unchanged-rim boundary-only replacements really cannot
lift all boundary colourings, even with an otherwise empty exterior.

For the first d4 type, s3,r2, the arcs are
  0->1,2->1,2->3,3->0,0->4,1->4,4->2,4->3.
Set boundary1={1,2}, boundary0={0,3}. Centre0 fails on4->3->0->4;
centre1 fails on4->2->1->4. Both possible diagonals join DIFFERENT colours,
so every orientation of every noncrossing diagonal subset preserves the
valid boundary colouring. Thus NO boundary-only same-rim replacement can
lift it. Five total vertices are minimum for a degree-four restored centre
with four distinct boundary neighbours; this minimality has that exact scope.
This graph is itself colourable (for example a different boundary colouring);
it is not a root counterexample or a globally minimum critical graph.

A low vertex in the selected triangulated minimum counterexample must
therefore either have one of these residual orbit types, or have a positive
type whose selected rule is blocked by an exterior reverse-arc guard. The
latter is additional finite data: two possible diagonal pairs at d4, five
at d5, each absent/forward/reverse. Not all such ternary assignments are
planar-realizable; this finite overdescription does not invent realizability.
In particular absence of a successful admissible rule is not root closure.

## 6. Attack the unbounded-degree F1 family using adjacent degree-four vertices

In a simple plane triangulation with minimum degree4, two adjacent degree4
vertices u,v form a clean double-fan disk with four distinct boundary ports,
possibly with extra boundary chords in its exterior. Let the two facial
third vertices at uv be p,q; let the remaining neighbour of u be a and that
of v be b. Their facial rims give boundary p-a-q-b-p and internal path a-u-v-b.
No internal extra adjacency exists because both internal degrees are exactly4.

The only possible boundary coincidence is a=b. It would create the five-
vertex triangular bipyramid, already a sphere triangulation, all of whose
faces touch u or v. Adding anything in one of its faces while retaining a
triangulation would require a new neighbour of u or v: a triangular disk
whose boundary vertex has no interior neighbour keeps that boundary triangle
as its incident face. This violates degree4. Thus the whole graph would be
that five-vertex bipyramid, whose two poles have degree3, contrary to minimum
4. Hence a!=b. The disk and labels used below are legitimate. This argument
applies to the selected triangulated representative, not all plane graphs.

Label the boundary (p,a,q,b)=(0,1,2,3), and the two interiors u=4,v=5.
Keep the rim directions encoded by r as above. The seven other edge positions
in order are
 E=[(0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5)].
Bit i of b reverses E[i] when1. The fixed rotation is
 0:(1,4,5,3); 2:(3,5,4,1); 1:(0,2,4); 3:(0,5,2);
 4:(0,1,2,5); 5:(0,4,2,3).
Of128 internal direction words,18 give both interior semidegrees(2,2), so
there are288 types after all16 rim words. This parameter b is a bitmask,
not the earlier boundary vertex name.

The checker tries85 candidate replacements with at most one interior:
five boundary-only choices; sixteen four-spoke wheel orientations; and
sixty-four choices obtained by a quadrilateral diagonal and an interior
vertex in either resulting triangle. Any smaller disk patch can be extended
to one of the maximal one-interior triangulations without changing its rim;
adding arcs only strengthens the Q side of (LIFT). This completeness is useful
context, but the residual obstruction below does not depend on a completion
argument or a finite test alone.

All288 types give256 positive and32 negative types under (LIFT). The symmetry
group preserves the pole pair{0,2}, allows its four disk symmetries and all-arc
reversal. There are43 orbits,39 positive and FOUR residual orbits, each size8:
 (r,b)=(1,78),(1,100),(3,43),(5,77).
Every selected positive rule in the actual certificate is BOUNDARY-ONLY,
not merely one-interior: both original interiors are deleted, decreasing
order by two. The unchanged-rim/noncrossing/reverse-arc conditions and all-
exterior proof of Section4 apply. These are nonuniform direction reductions,
not a repeated claim that all low vertices belong to an alternating long strip.

## 7. Four residual pair types defeat ALL smaller same-rim patches

For the first two residual codes use boundary mask4 (only vertex2 colour1);
for the last two use mask1 (only vertex0 colour1). In each case the original
patch has no valid extension. The four assignments to interiors4,5 are
explicitly rejected by cycles in the output. For (r,b)=(1,78) they are:
 interiors00: 0->4->1->0;
 interiors10 (4=1,5=0): 0->5->3->0;
 interiors01 (4=0,5=1): 0->4->1->0;
 interiors11: 2->5->4->2.
This is a complete finite proof for the displayed interface, with no
unstated return path. The other three code representatives have analogous
four displayed cycle witnesses, not just search timeouts.

Why NO smaller same-rim patch can work, even outside our85-option search:
its boundary has one minority-colour vertex and three majority vertices.
The majority rim arcs form a two-edge source or sink: respectively
 {1->0,3->0}, {1->0,3->0}, {2->1,2->3}, {1->2,3->2}.
The only possible additional majority boundary edge cannot make a directed
triangle, since the shared source/sink stays such. With zero internal vertices
the colouring is therefore valid. With ONE internal vertex give it the
minority colour; that colour class has only two vertices, which cannot form
a cycle in a loopless orientation without opposite arcs. The majority class
is unchanged. Thus every such smaller patch has a colouring with this
boundary assignment, whereas the original has none. An empty exterior
already disproves an all-exterior lift that leaves boundary colours fixed.

Six vertices are minimum for an obstruction with four fixed boundary ports
and two removed internal vertices, and the displayed patch attains that
size. This is scoped interface minimality, not minimum order of a root
counterexample. The obstruction does not exclude enlarging the boundary,
including exterior return paths, or a nonlocal reduction that changes which
vertices are retained. It DOES exclude repeatedly searching a same-rim
five-vertex replacement for these four residual codes.

## 8. Execution, provenance, and the precise unresolved charge deficit

The archived self-contained checker uses Kahn deletion and positive
transitive closure as separate acyclicity oracles; no conjectured reduction
is used as the direct colouring oracle. It checks rotations and all face
walks, explicit orders/cycles, all deletions of O6/I12, exact rational charges,
and all finite wheel/pair types, not a sample of those type spaces.
It checks39711 degree triples up to64 only as an implementation control;
Section2, not that bound, proves the unrestricted charge classification.

Actual final generator replay: CPython3.13.5, one CPU affinity,512MiB address
space,95 CPU seconds,100-second wall alarm,parent105s,65536 bytes per output
file, seccomp denied socket/socketpair/connect. Exit0, no timeout/stderr.
Final recorded elapsed23.130760s. Wheel checks cover7680 and634880 complete
boundary-assignment/option cases. Pair checks cover578880 valid small-patch
assignments. The output contains all orbit representatives, selected lifting
maps, common failure assignments, and explicit rotation/charge/cycle ledgers.
All labelled rule streams have reproducible hashes and source-defined order.
The broad structural graph search is not used as a minimum-order certificate;
O6/I12 minimality follows from their stated degree bounds and Euler.

No Lean/elan was found by the recorded executable lookup, no elaboration or
axiom/escape report exists, and no registered verifier receipt is produced.
Generator controls do not become mathematical admission via CI or merge.
New claims use claim IDs only, not invented admitted obligation records.
The pending review must bind T3,T4,C31,C32 and root separately.

The remaining negative charges are now localized: an F1 face supplies an
adjacent-degree4 pair, which must be one of four residual pair types or fail
a guard for a positive rule. Every other F2--F6 face supplies a degree4/5
wheel, which must be a residual wheel type or fail a selected reverse-arc
guard. This is a FINITE directed-interface-and-guard reduction of the problem,
not an assertion that the remaining types have been eliminated. F1's third
vertex degree is unbounded; its pair interface does not need that degree.
The exact -8 charge has not been redistributed to an all-nonnegative final
ledger. Claiming each residual zero/negative type already reducible would
contradict the explicit small-interface witnesses, not prove the root.

Next move: enlarge the first residual pair (1,78) by its actual exterior
arcs/returns, or exploit the compulsory reverse arc obstructing a selected
positive rule. A same-rim at-most-one-interior replacement for that pair is
now a certified dead end. Any enlarged replacement needs its own profile
lift for every exterior and strict vertex decrease, then a valid argument
that the -8 charge cannot be supported only on surviving directed types.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
best_verified_result: none
first_open_configuration: F1 residual adjacent4 pair (r,b)=(1,78) or a failed
 exterior reverse-arc guard; degree5 residual wheel (s,r)=(3,2) is also open
next_obligation: obligation:opg169-root
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_shortcuts: local-structure-implies-C31-strip; same-rim smaller replacements
 for the explicit residual interfaces; prior singleton/SCC and exact-width failures
root_closed: false
