# Nine-degree donors: exhaustive identifications, a seven-vertex deletion, and the full charge ledger

Verdict: candidate_only. Status: proof-drafted with finite certificate candidates.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: ad6f9d273cc158387961b5f9e0b0ad1b2b033ebe
Primary owner: math-proof. No C27, frozen-recolouring or exact-width search.
Current successor transaction: existing C34 / PR42; no second packet is needed.

## 1. Exact scope and dependencies

The contract is every orientation of a finite simple planar graph, with a
partition into two FULL induced acyclic colour classes. Empty classes are
allowed. A cycle and a boundary return have positive length. Selecting an
edge-maximal graph among counterexamples of minimum vertex order produces
the triangulated representative used below, as in C32. This selection does
not assert that every minimum counterexample is already triangulated.

C32 labels a residual adjacent-degree-four pair by boundary (0,1,2,3),
interiors 4,5, rim reversal word r and internal reversal word b on
[(0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5)]. The four residual codes are
(1,78),(1,100),(3,43),(5,77). Their unique distinguished common neighbour
has its two low spokes in the same direction; the other common neighbour
has one entering and one leaving spoke. Mark exactly these pair occurrences
and assign each to that distinguished donor. Write t(p) for the number
assigned to that donor. No additional arbitrary degree-four edges are marked.

Candidate dependencies, each retaining its own statement identity:
- T3/T4: minimum-counterexample strong connectivity and semidegrees >=2;
- C33: every marked pair's donor has degree >=6;
- C34 and the supplied post-C33 audit: both path endpoints have degree >=5,
  so separated pairs satisfy 3t(p)<=d(p);
- supplied post-C33 two-pair tables: d(p)=6 or7 implies t(p)<=1.
The latter tables have 64/128 complete local directions and 5088 valid
smaller-rim assignments. They are rechecked here, not silently promoted
to a trusted receipt. Their original source, input, records and proof are
preserved in the supplied-archive file without rewriting their old dates
or historical UNSENT metadata. The active packet is the C34 root packet,
not the archived earlier draft packet.

The NEW theorem is that d(p)=9,t(p)=3 is impossible in the selected minimum
counterexample. Its proof constructs a strictly smaller induced deletion
whose EVERY valid colouring lifts while every retained vertex keeps its
colour. It is not a recolouring-path assertion. No universal root solution
or full-domain root counterexample is supplied.

## 2. Complete nine-spoke geometry

By separated-pair packing, equality 3t=d at d=9 fixes the cyclic word to
H0,u0,v0,H1,u1,v1,H2,u2,v2, with each H of degree >=5 and all u,v of degree4.
The H spokes have the opposite direction to either adjoining low pair.
Thus all three low pairs have the same sign. Reverse ALL arcs if necessary:
p->u_i,p->v_i and H_i->p for every i. The reverse-sign case is restored by
reversing every arc and every positive relation, without changing any colour
assignment or the underlying plane embedding.

Let q_i be the other facial third vertex of the edge u_i v_i. Sector i has
poles p,q_i, endpoints H_i,H_(i+1), and low interiors u_i,v_i (indices mod3).
Its six actual triangular faces are, in a consistent oriented-face convention,
 (p,u_i,H_i), (p,v_i,u_i), (p,H_(i+1),v_i),
 (H_i,u_i,q_i), (q_i,v_i,H_(i+1)), (q_i,u_i,v_i).
The underlying edges are exactly these faces' edges. Adjacent sectors share
one p--H edge. The union has 18 stipulated internal triangular faces.

Fixed integer names in the checker:
 p=0; H0,H1,H2=1,2,3; (u0,v0)=(4,5), (u1,v1)=(6,7), (u2,v2)=(8,9);
 q0,q1,q2=10,11,12 before identifications.
The p rotation is (1,4,5,2,6,7,3,8,9), up to reversal/rotation.
All p and low incidences are accounted for by their full degrees; no extra
arc incident with these seven intended deleted vertices can be hidden outside.
Additional arcs between retained ports remain in the exterior, not dropped.

## 3. Exhaustive equality classification: 15 patterns, four survivors

The H vertices and all low neighbours are distinct because they are distinct
entries in p's simple degree-nine rotation. q_i cannot equal p or its own low
vertices (distinct facial third vertices). It cannot equal its own endpoint:
that would leave one degree-four low star with at most three different
neighbours. It cannot be a low vertex from another pair: such a low vertex
already has the three different neighbours p, its mate and its own H endpoint,
and would additionally acquire both u_i and v_i, giving degree at least five.

Consequently q_i can only be its nonincident H_(i+2), or a genuinely new
vertex. The genuinely new q vertices may coincide with one another. This
leaves exactly 15 equality patterns, enumerated without direction assumptions:
8 patterns in which each q independently is new/distinct or its opposite H;
6 in which one fresh pair of q's is identified and the third is fresh or its
opposite H; and1 in which all three new q's coincide.

### 3.1 Fresh q coincidences

Any two sectors share one H endpoint. If their q vertices coincide at q,
four stipulated faces around that shared H close the link cycle
p, previous-low, q, next-low, p. These four neighbours are distinct and
these are ACTUAL facial sectors. No additional edge can be inserted at H:
all four wedges of its cyclic rotation have already been specified.

If the remaining q is not H itself, the H vertex is saturated at degree4,
contradicting its endpoint lower bound. This excludes the three pair-only
fresh identifications and the all-three-fresh identification (four patterns).

If the third q equals that H, its own sector forces four more neighbours
at H. The same closed four-face link then contradicts these extra incident
edges. This excludes the other three fresh-pair patterns. It is important
NOT to report degree4 for their entire abstract quotient graph: its degree
there is8; the contradiction is the impossible plane rotation containing
both the already closed link and the forced extra edges.

### 3.2 Two or three q-to-H identifications

Before identifications the core has13 vertices and30 edges. Two distinct
q_i=H_(i+2) identifications leave11 vertices and29 different underlying
edges (one pair of rim edges is identified). But a simple planar graph on
11 vertices has at most27 edges. Three such identifications leave10 vertices
and27 edges (three pairs of rim edges are identified), exceeding24. These
exclude three double-identification patterns and one triple pattern. This
is an actual finite edge count, not a claim that bounded degree tests prove
an unbounded embedding statement.

### 3.3 The surviving single q-to-H identifications MUST be retained

Four labelled equality types remain:
D: all six ports H0,q0,H1,q1,H2,q2 distinct;
A_i: exactly q_i=H_(i+2), for i=0,1,2, and the other two q's new/distinct.

D has a simple hexagonal complementary boundary. In A0 the old boundary
walk becomes H0,H2,H1,q1,H2,q2. It splits into the two complementary boundary
walks (H2,H1,q1) and (H2,q2,H0), sharing the port H2. These are NOT grounds
for declaring nonplanarity, and NOT a six-distinct-port disk. A1,A2 follow
by rotating the labels. The retained boundary subgraph is two triangles
meeting at one vertex. The core has12 vertices,30 edges,18 stipulated
triangular faces and two complementary regions, satisfying Euler exactly.

The face/rotation certificate caps each complementary walk only to record
the core embedding. It does NOT assert that the complementary triangular
regions in G are empty facial triangles. Arbitrary exterior graphs can
occupy them. This distinction is necessary for the all-exterior argument.

Classification counts: four endpoint-degree exclusions; three rotation-link
exclusions; four Euler exclusions; four surviving equality types. No other
identification or hidden assumption that q is new has been used.

## 4. All direction types and a complete seven-vertex deletion certificate

For each sector, relabel each of the four C32 codes by the possible endpoint
and low-pair interchanges and possible FULL arc reversal. Keep only maps
with the actual sector skeleton and the fixed donor-out sign. Remove literal
arc-set duplicates. This gives exactly eight possible complete sector arc sets.
The source records both these sets and their original C32 code/bijection.
Different sectors agree on their shared H_i->p arcs; hence the complete
normalized direction space is 8^3=512 for EACH surviving equality type.
No arbitrary exterior path length is part of that finite allocation.

Let P be the core and let B be its set of retained ports (six in D, five in
A_i). Let Q be P minus p,u0,v0,u1,v1,u2,v2. Thus Q retains EVERY P arc between
ports, not merely selected convenient arcs. There are no new arcs, no new
vertices, no boundary identifications, and no exterior reverse-arc guard.
Q is a hexagonal rim in D and the two joined triangular rims in A_i.

For every valid binary assignment d to ALL vertices of Q, the archived
vector gives a binary assignment c to ALL P vertices with
 c|B=d, c valid on both full induced colour classes, R_P(c) subseteq R_Q(d).
Because Q is a retained subgraph, the reverse containment holds automatically;
the selected maps actually have EQUAL positive boundary relations.
The vector index is the Q bitmask. Null means that Q assignment itself is
invalid, never that a valid Q assignment was omitted. The P bitmask uses
boundary-first order, followed by p and the six fixed low names. The four
orders and every original rotation are reproducible from the source.

Exact executed finite certificate scope:
 D: 512 direction types,32736 valid Q assignments;
 A0,A1,A2:512 direction types and14400 valid Q assignments EACH;
 total:2048 normalized types and75936 complete lifts.
Full reversal gives the other donor sign. The separate audit also checks
each reversed lifting relation directly; it does not merely inspect a count.
All2048 selected replacements delete exactly seven vertices.

Every direction word is included, including those that extra outside
semidegree information might later exclude. We do not reject a retained
boundary vertex just because its degree is small in this partial core.

## 5. Why every outside colouring lifts, including the two-region interfaces

Write G=P union F, where F contains all remaining vertices/arcs, including
any extra arcs between retained ports. P and F intersect only at B (shared
boundary arcs may be counted once) and there is no cross-interior arc because
all p/low stars are saturated. G'=G minus the seven vertices is an actual
induced subgraph, finite/simple/planar/oriented, with seven fewer vertices.
In particular this is NOT an arbitrary directed contraction.

Choose ANY valid colouring of G'. Its restriction to Q is a valid table
index. Choose the corresponding P colouring and keep EVERY F vertex colour
unchanged. Each colour class contains every induced original arc.

If a new monochromatic directed cycle crossed the interface, split it at
successive B visits. Its P portions are positive B paths recorded in R_P.
Each is replaced by a Q path with the same colour and endpoints because
R_P is contained in R_Q. Keeping the F portions yields a positive directed
closed walk in that colour of G'. Any finite positive closed walk contains
a directed cycle (choose equal positions of minimum positive separation).
This contradicts the given valid colouring of G'. Cycles wholly in P or F
were already excluded. This proves the desired all-exterior lift.

Nothing in this proof requires B to lie on one simple cycle. It applies to
the two complementary regions sharing a vertex in A_i without merging them
incorrectly or assuming either exterior empty. This is why keeping the
single q-to-H equality cases was essential.

For a minimum-order counterexample, G' is colourable by minimality in the
ENTIRE frozen contract class. The lift contradicts noncolourability. Hence
                         d(p)=9 implies t(p)<=2.
This is the new local necessary-condition candidate. It is not d(G)>=10,
not exclusion of all degree-nine vertices, and not a root colouring algorithm.

## 6. Full double-face funding, with every lost corner contribution recorded

Together with d>=6 at donors, 3t<=d, the six/seven-degree exclusions and the
new nine-degree exclusion, the all-degree budget is now
                            2t(p)<=d(p)-4.
For d>=12 use2floor(d/3)<=d-4. At d8,10,11 check the integer maximum;
at6,7 use t<=1; at9 use t<=2. Vertices of degrees4,5 have t=0.
There is no unproved exceptional payment left in this inequality.

Initial charges stay d(v)-4 and length(f)-4, total-8. For every marked pair
uv assigned to p, pay one unit from p to EACH of the faces p-u-v and q-u-v.
Then distribute d(p)-4-2t(p) equally over p's d(p) incident face corners.
Put gamma(p)=(d(p)-4-2t(p))/d(p), and let h(f) count every actual unit
payment received. Each debit has exactly one named credit; different
payments to the same face are counted separately. Every vertex finishes0.
EVERY face, not only a target, finishes at
                     length(f)-4 + sum_corners gamma + h(f).       (DC2)
Summing gives the unchanged total-8: sum d*gamma+sum h=sum(d-4).
Faces of length>=4 remain nonnegative, as do triangles with h>=1. Thus both
faces of every marked residual low-low edge are now nonnegative.

Relative to C33's one-unit rule the additional credit at a donor-side face
is accompanied by the loss t(p)/d(p) at EVERY corner incident with p.
Specifically Delta(f)=h_extra(f)-sum_corners t(p)/d(p). There is no unpaid
hidden cost and no permission to retain C32's old F1--F6 positivity list
unchanged after reducing gamma. An unpaid triangle has charge
                         -1+gamma(x)+gamma(y)+gamma(z).
It is negative exactly when the displayed sum is less than1. These faces
are NOT all eliminated. The total-8 therefore still forces at least one
unpaid negative triangle; it does not give a contradiction.

For example the unexcluded decorated face type (d,t)=(8,2),(4,0),(5,0),
h=0 has charge-4/5. This is a precisely stated remaining charge type,
NOT an assertion that a globally minimum counterexample realizing it exists.
The old other-pole W(2,2), chord failures and degree-five reductions retain
their own open constraints; this turn does not claim to settle them.

One must not apply the new double rule to a hypothetical d9,t3 graph and
say its three old-7/9 faces have been paid: the resulting gamma=-1/9 would
be illegal. The deletion theorem EXCLUDES that configuration before the
budget is used. On the surviving minimum-counterexample domain, DC2 is the
previous double rule with its exceptional branch removed. This distinction
is checked as a negative arithmetic control.

## 7. Reproducibility and trust boundary

The new standalone generator uses induced-subset sink deletion for acyclicity
and bitset positive closure for relations. Every selected lift is crosschecked
with DFS/BFS. The separately executed certificate consumer imports neither
generator nor its predicate implementation; it reconstructs the eight sector
arc sets from C32 and audits all75936 lifts, their full reversals, all alias
rows, and the four core spherical embeddings. It also audits all5088 prior
six/seven-donor assignments from the exact supplied archive. No old runtime
record is relabelled as a new execution.

Selected CPython3.13.5 executions: generator exited0 in8.647023s; separate
audit exited0 in4.132772s; neither timed out or wrote stderr. Both applied
one CPU,512MiB address space,CPU80s/wall85s/parent90s,1MiB output-file caps,
and seccomp denial of socket/socketpair/connect. The files record exact
source, wrapper, interpreter and output hashes. These are candidate-generator
self-tests under the user's request, not registered-verifier receipts.
Lean/elan were not found by the recorded executable lookup; no elaboration
or axiom/escape report exists. No EvidenceLink/Result/Solution is self-signed.

The supplied old bundle is losslessly archived as a UTF-8 file map with
LZMA/base64, decoded byte count and SHA256. Extract it only into an isolated
local directory. Its draft packet and historical UNSENT/checkpoint text
remain history. The current active packet is the sole existing C34 packet
on the reused PR42 transaction. The readable old donor-audit proof retains
its exact bytes and is explicitly superseded on the open-nine-degree item
by this new proof. No previous merged PR is retransmitted.

## 8. Claim DAG and nonterminal checkpoint

Dependencies: actual saturated star + four C32 residuals + endpoint>=5
 -> fifteen equality patterns -> four surviving interfaces;
finite complete sector/certificate maps -> every-boundary lift;
these + arbitrary exterior composition + strict induced deletion
 -> nine-degree three-pair exclusion;
this + earlier packing/six/seven exclusions -> unconditional double budget
 -> conserved DC2 with explicit unpaid-triangle criterion.
Finite local certificate validity is not extrapolated to arbitrary exterior
colourings without the separate Section5 proof. Probability and asymptotic
estimates are inapplicable. Vertex count and finite paths supply the only
well-founded decreases used. All reversals and identifications are explicit.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
best_verified_candidate: none
nine_degree_configuration_remaining_cases: [] (proof/certificate candidate scope)
root_closed: false
first_open_configuration: an unpaid triangle h=0 with sum(gamma)<1, including
 decorated(8,2)-(4,0)-(5,0), and the already retained other-pole/chord/degree5 cases
next_action: restrict or reduce those unpaid directed face types and audit the
 entire new ledger; do not reopen the excluded nine-degree three-pair case
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
