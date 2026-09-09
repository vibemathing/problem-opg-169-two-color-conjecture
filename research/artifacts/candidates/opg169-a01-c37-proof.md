# C37: the degree-six J sector, guarded hole replacements, and a whole-graph obstruction

Verdict: candidate_only. Status: proof-drafted with bounded generator controls.
Repository: vibemathing/problem-opg-169-two-color-conjecture
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: 1911f4608bed07c4840cf7e1fb38498869a50dcc
Owner: math-proof. No root closure or trusted verification is claimed.

## 1. Exact scope and quantifiers

An orientation gives one direction to each edge of a finite simple planar graph.
Both complete induced binary colour classes must be acyclic; unused colours are
allowed. R means ALL positive monochromatic paths between retained boundary
vertices, including paths through other boundary vertices. It is not reflexive
reachability. Root concerns existence, not extending an arbitrary fixed colouring.

The ONLY new degree is d(7)=6 in the frozen C35 J direction. Vertices 0,2,3 have
complete degree five. I=(0,2,3,7) is the controlled region: local surviving I
vertices MAY be recoloured simultaneously. Every vertex outside I is fixed in a
lift. We do not claim a sequence of legal single-point recolourings.

The selected triangulated least-order-counterexample setting, T3/T4 and C36's
previous d(7)<=5 exclusions remain separate candidate dependencies. No prior
nine-donor enumeration, closed d5 direction, universal J restoration, or uniform
width route is rerun. This document does not classify d(7)>=7.

## 2. Actual faces and complete equalities for the two extra neighbours

The old J neighbourhood has the eighteen arcs explicitly frozen in c37-input.
Its ten actual faces are
 (0,2,3),(0,6,2),(0,5,6),(0,4,5),(0,3,4),
 (2,7,3),(2,11,7),(2,6,11),(3,8,4),(3,7,8).
The old distinct ports are (4,5,6,11,7,8). At degree six the ordered additional
neighbours x,y of7 give actual faces (8,7,x),(x,7,y),(7,11,y) and the rotation
 of7 is (x,y,11,2,3,8), up to cyclic shift. There are exactly five extra edges
 (8,x),(x,7),(x,y),(y,7),(y,11).

The two extra neighbours are distinct entries of the simple star. They cannot
be 2,3,8,11,7, already present, and cannot be0 because its complete degree-five
star would acquire an extra neighbour. Thus each is old port4,5,6 or genuinely
new; two new names must be distinct. There are exactly13 labelled equality types:
one both-new, six one-old, and six ordered distinct-old pairs. New names12,13
are role labels, not assertions that the rest of the exterior is empty.

All x=4 cases close the actual degree-three link of8. All y=6 cases close that
of11. This excludes five equality types (the overlap is counted once). In (5,4),
two stipulated faces require different successors of the same dart at5; (6,5)
has the analogous conflict at6. These exclude two further types. The last
both-old case (6,4) has9 vertices and23 distinct edges, exceeding the simple
planar upper bound21. Its contradiction is geometric, not a search timeout.

Exactly five types survive:
 D=(12,13); X5=(5,13); X6=(6,13); Y4=(12,4); Y5=(12,5).
D has eleven vertices,23 edges,thirteen stipulated triangles and a seven-sided
complementary region. Each other type has ten vertices,23 edges,thirteen
stipulated triangles and TWO complementary regions, of lengths3 and4, sharing
the identified port. Complete rotations are supplied in the certificate.
These complementary regions may contain arbitrary exterior graphs; their caps
in an embedding record are not assumed to be actual empty faces of G.

The fully controlled stars are d0=d2=d3=5 and d7=6. The underlying degree of a
retained boundary vertex in this partial graph is not its degree in G. Extra
arcs among retained ports remain in the exterior. All13 equality types are
covered; no genuinely allowed two-region type is silently deleted.

## 3. Directions and allocated smaller replacements

A five-bit word w reverses the corresponding ordered edge in
 [(8,x),(x,7),(x,y),(y,7),(y,11)]. All32 words occur for every surviving equality
model. The two original incoming and two original outgoing arcs at7 already
ensure both semidegrees>=2 for every such word. Both whole colours and complete
positive relations, not selected return paths, are tested.

First attempt Q=P-3. It has three controlled local survivors K=(0,2,7), whose
colours may change on lifting. If that fails the certificate criterion, try
Q=P-7 with K=(0,2,3), plus any set of noncrossing oriented diagonals in the actual
six-sided hole around7. All215 absent/directed diagonal sets are enumerated.
Candidates are ordered by the number of new boundary-boundary pairs, then edge
count and literal arcs. A positive result records the complete selected map;
it does not assert that every later candidate fails. Each of the nine negative
results visits the entire215-option second catalogue and retains a witness for
every option. The earlier bare P-3 gaps are retained separately.

Every selected added arc is drawn inside the deletion hole, so the net vertex
loss is exactly one. Arcs opposite to an existing P arc are rejected. If a new
arc a->b joins two boundary ports and did not already occur in P, require that
the actual exterior has no b->a. Consistent duplicate a->b arcs count once.
An arc with an endpoint in controlled I has no unknown exterior reverse arc:
its complete original star is specified. Guards are NOT inferred from planarity.

For every valid COMPLETE Q colouring d, the saved vector gives a complete P
colouring c with c|B=d|B and R_P(c) subseteq R_Q(d). Index8*b+k uses the sorted
retained-port order, then the three surviving controlled names in I order. A
hexadecimal digit gives the four-bit original I word; '-' means Q is invalid.
All valid assignments are covered, not merely one representative per boundary.

| Equality | No exterior guard | Guarded rules | No allocated rule | Full selected lifts |
|---|---:|---:|---:|---:|
|D|20|8|4|9478|
|X5|20|9|3|4916|
|X6|30|2|0|5000|
|Y4|28|4|0|5050|
|Y5|24|6|2|5302|
|Total|122|29|9|29746|

The nine remaining direction words are
 D:3,12,19,28; X5:3,12,19; Y5:12,28.
All these words make the central exterior triangle7-x-y directed cyclically.
This last observation is a property of the listed residuals, not a claim that
an arbitrary cyclic triangle is unavoidable or uncolourable. Guarded cases can
also survive when their actual forbidden exterior arc is present.

Example D,w2: the full extra arcs are 8->12,7->12,12->13,13->7,13->11.
Delete7 and add8->2,13->8,11->8 inside its hole. The exact exterior guards are
 absence of8->13 and8->11. No inverse condition is needed for8->2 because2 has
its full original degree-five star. Example D,w9 instead admits the guard-free
rule delete7, add12->2. The latter excludes this direction regardless of exterior
chords. All other selected arcs and full maps are available in the archive.

## 4. Quantified all-exterior lifting and class preservation

Let G contain one certified P in its recorded embedding, with no unlisted I
adjacencies. Replace P by its selected Q, retaining ALL external vertices/arcs
and satisfying every listed guard. Drawing the diagonals in the actual deletion
hole gives a planar graph. There are no loops or opposite arcs by the checked
conditions, and consistent repeated copies are kept once. Its order is |G|-1.
The resulting graph belongs to the full root class; it need not retain any
minimum-counterexample semidegree condition.

Take ANY valid colouring of this whole smaller graph. Its Q restriction is a
valid full table index. Choose that P lift and keep every vertex outside I
fixed. A monochromatic cycle wholly in P or F is impossible. A crossing cycle
can be split at successive boundary visits. Each positive P segment is replaced
by a same-coloured Q path with the same endpoints, using R_P subseteq R_Q.
Keeping F segments creates a positive closed walk in the original smaller
colouring. Such a walk contains a directed cycle, contradicting validity.
This argument also applies to the two complementary regions of the aliased
models; the interface need not be one simple cycle.

Thus the122 unguarded signed configurations cannot occur in a least-order
counterexample. A guarded configuration cannot occur when all of its guards
hold. Neither assertion comes from an unproved extrapolation over exterior
path lengths. There is no claim that all160 configurations are eliminated.

## 5. Complete eleven-vertex obstruction, including every smaller colouring

A stronger failure than a missing relation test occurs for D,w3. Freeze the
following WHOLE simple plane triangulation on
 V=(0,2,3,4,5,6,7,8,11,12,13).
Its core is D,w3; its four additional exterior arcs are
 8->5,5->12,6->13,5->13.
The complete27 arcs are in c37-input, with full rotation
 0:(2,6,5,4,3); 2:(0,3,7,11,6); 3:(0,4,8,7,2);
 4:(0,5,8,3); 5:(0,6,13,12,8,4); 6:(0,2,11,13,5);
 7:(2,3,8,12,13,11); 8:(3,4,5,12,7);
 11:(2,7,13,6); 12:(5,13,7,8); 13:(5,6,11,7,12).
All semidegrees are at least two and all underlying degrees at least four.
Its only degree-four vertices are4,11,12, with NO edge between them. Hence
there is no marked residual degree-four pair anywhere: actual t=h=0 globally.

On G-3 take colour1={4,5,6,7,8,11} (mask2544). This is a valid complete smaller
colouring. Its fixed seven-port boundary word is31 in B=(4,5,6,8,11,12,13).
No colouring of I can extend that boundary, even if all three local surviving
colours are allowed to change. A direct forcing proof is:
 - cycles0->4->5->0 and3->4->8->3 force0=3=0;
 - cycle0->2->3->0 then forces2=1;
 - cycle2->11->7->2 forces7=0;
 - cycle7->12->13->7 is then monochromatic0, contradiction.
Every arc belongs to the frozen whole graph.

This ONE graph has124 valid full colourings, attaining66 of128 boundary words.
For each of the62 unattainable words all16 complete internal assignments have
an explicit monochromatic-cycle witness. Thus it is not a root counterexample.
For example the colour1 mask232={3,5,6,7} is valid.

The allocated alternative family is: choose any v in I, delete v, and add any
noncrossing directed chord subset in its actual hole, retaining everything else.
There are31 options for each of0,2,3 and215 for7:308 in total. For EVERY option
there is a valid WHOLE smaller-graph colouring with an unattainable original
boundary word. All315392 complete smaller assignments are recorded by status:
 '-' invalid; 'E' valid and extendable; 'B' valid but no extension.
47116 are valid, of which2136 are B. This never says all valid colourings fail.
Each of308 alternatives has a selected B witness, and all its original I
restorations are covered by the stored16-cycle list for that boundary word.
These are actual full-exterior failures, not merely boundary projections.

Minimality has an exact restricted meaning. Within complete simple plane
triangulations with this frozen J direction, d7=6, minimum degree>=4 and both
semidegrees>=2, no prescribed-boundary failure of G-3 can have fewer than11
vertices. The equality classification forces at least ten vertices. At exactly
ten, only the four aliased models are possible; their exterior is a triangle
and a quadrilateral, with no additional vertex available. Completing the latter
has four directed diagonal choices. All4*32*4=512 completions are included.
Exactly four satisfy both semidegrees>=2: X5, words0,2,12,14, with6->13.
All110,112,82,116 valid G-3 assignments respectively extend with their boundary
fixed. This last minimality test concerns ordinary extension, NOT relation
containment (some of those ten-vertex lifts add relations). The eleven-vertex
witness above attains the stated ordinary-extension lower bound. No minimum
claim over arbitrary planar graphs, other separators or all gadgets is made.

The failed-route proposal is ONLY the universal repair by one controlled-point
deletion plus diagonals in that point's hole. It does not forbid replacing by
a graph with different internal structure, changing the interface, or exploiting
additional global constraints of a genuine minimum counterexample.

## 6. All thirteen controlled faces and unchanged double-payment costs

Retain exactly DC2 on the ORIGINAL graph:
 gamma(v)=(d(v)-4-2t(v))/d(v), mu(f)=length(f)-4+sum_corners gamma+h(f).
Each marked pair has one actual donor debit and one unit credit on EACH side.
A vertex sends2t+d*gamma=d-4 and ends0. C37 introduces no payment, no duplicate
subsidy, and no recomputation of the original t from the smaller graph.

Here g0=g2=g3=1/5, but g7=(1-t7)/3 with t7=0 or1. It is WRONG to keep C36's
old g7=1/5. Writing gv for the actual remaining corner contribution, the13
original controlled faces are:
 (0,2,3): -2/5;
 (0,6,2): -3/5+g6; (0,3,4): -3/5+g4;
 (0,5,6): -4/5+g5+g6+h; (0,4,5): -4/5+g4+g5+h;
 (2,7,3): -3/5+g7;
 (2,11,7): -4/5+g11+g7; (3,7,8): -4/5+g8+g7;
 (2,6,11): -4/5+g6+g11+h; (3,8,4): -4/5+g8+g4+h;
 (8,7,x): -1+g8+g7+gx+h;
 (x,7,y): -1+gx+g7+gy+h;
 (7,11,y): -1+g7+g11+gy+h.
Omitted h is zero: that face has no possible degree-four/degree-four edge.
Every displayed h is its ACTUAL number of unit payments; it is not set to zero
in arbitrary exteriors. If x or y equals an old port, aggregate that vertex's
repeated corner coefficients, without identifying distinct face payments.

Their complete total is
 -10+6g7+3g4+2g5+3g6+3g11+3g8+2gx+2gy+sum(h).
There are21 controlled corners and18 retained-port corners, all39 counted.
Relative to the OLD single-face rule the difference is extra actual unit
receipts MINUS
 t7+3t4/d4+2t5/d5+3t6/d6+3t11/d11+3t8/d8+2tx/dx+2ty/dy.
In particular ALL SIX t7/6 losses are included, not merely the three new faces.
Every other face keeps its own DC2 entries. No previously positive face is
silently presumed positive after decreasing gamma.

For the frozen whole eleven-vertex witness, all t=h=0. Its18 exact face rows
and11 vertex rows are independently recomputed from the full rotation. The13
controlled faces sum to -86/15; the other5 sum to -34/15; total remains -8.
Its unpaid degree triples and counts are (5,5,5):2, (5,5,6):4, (4,5,6):8,
(4,5,5):4, with charges respectively -2/5,-4/15,-7/15,-3/5. These numeric
negative faces are not made nonnegative by finding some local reductions.
The C35 L/N/P parameter classification is retained, not replaced by old
single-payment signs or a finite bound on all graph degrees.

## 7. Reproducibility, scope and next obligation

The standalone generator has five family batches plus one whole-obstruction
batch. The lossless archive contains all six outputs, every selected lift,
every residual option witness, all full colouring domains, full rotations and
charge rows. The consumer imports no generator implementation: it uses DFS for
cycles and BFS for positive paths, checks complete Q vectors and all reversals,
all1935 final negative option witnesses and all315392 whole-Q statuses.
Both programs remain in ONE generator trust domain. Their successful exits
are not registered verifier receipts. Replay uses CPython3.13.5, one CPU,
512MiB, CPU35s/wall40s/parent43s,1MiB output caps and denied socket syscalls.
Exact source, input, output and execution identities are recorded separately.
No Lean elaboration, axiom report or matching trusted acknowledgement occurred.

Dependency DAG: saturated J faces -> ordered six-degree sector ->13 equalities
-> five embeddings ->32 directions each -> complete lift/guard table -> same-class
strict decrease and arbitrary-exterior composition -> scoped local exclusion.
The whole-graph obstruction/minimality and DC2 ledger are separate branches.
The only well-founded changes are fewer graph vertices, finite colour domains
and finite path simplification. No statistical or asymptotic extrapolation enters.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
best_verified_candidate: none
first_open_configuration: D,w3 or another of the nine d6 residuals; a guarded
rule whose actual exterior inverse arc occurs; all d7>=7 sectors remain open
next_action: use a different internal gadget or a genuinely larger controlled
interface for D,w3, retaining complete exterior quantifiers and DC2 costs.
Do not repeat the exhausted one-point-deletion/hole-diagonal shortcut there.
next_obligation: obligation:opg169-root
root_closed: false
