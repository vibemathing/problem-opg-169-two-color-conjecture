# C33: exterior-face expansions, forced high donors, and a budgeted charge transfer

Verdict: candidate_only. Status: proof-drafted with bounded generator controls.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Packet target: obligation:opg169-root
Base: b782deb5f1dd369587a2492907c1e26305e6a6c6
Primary owner: math-proof.
C31/C32 are separately scoped candidate dependencies, not admitted Evidence.
No repeat of frozen-colouring or uniform dynamic-width searches; no C27 use.

## 1. Frozen domain and the exact new objective

Graphs are finite simple planar orientations. A binary colouring is valid
when BOTH full induced colour classes have no positive directed cycle.
Unused colours are allowed. R(c) records ALL positive monochromatic paths
between labelled boundary vertices, including paths via other boundary
vertices. It is not reflexive reachability and not just a selected path.

For minimum-counterexample conclusions SELECT an edge-maximal member of
minimum vertex order, as justified in C32. It is a plane triangulation;
this is a choice of representative, not a claim about every minimum graph.
T3/T4 give the separately drafted nonempty/strong/semidegree-two conditions.
Only true vertex-minimality allows applying colourability to a smaller graph
in the FULL contract class. The smaller graph need not satisfy T4.

The first target is C32's residual adjacent-degree-four pair (r,b)=(1,78).
The other three residues are treated next under the same frozen expansion
rule. The old four-port unchanged-rim obstruction is not re-searched.
We add actual OUTSIDE facial triangles. When two have a common third vertex,
a previous boundary vertex can become interior; that changes the interface
and is the decisive improvement over merely attaching a new boundary leaf.

This document proves a useful necessary condition and a new conserved
charge redistribution, not the root. It does not assert that every exterior
has one new vertex, or that negative charge already implies reducibility.

## 2. Residue and embedding conventions

The rim vertices 0,1,2,3 occur in this cyclic order. Interiors are u=4,v=5.
Rim edge i--(i+1 mod4) is forward unless bit i of r is one. The ordered
internal edges are
  [(0,4),(2,4),(1,4),(4,5),(0,5),(2,5),(3,5)];
bit i of b reverses edge i. Codes in this order are
  C0=(1,78), C1=(1,100), C2=(3,43), C3=(5,77).
The rotation is
  0:(1,4,5,3), 1:(0,2,4), 2:(3,5,4,1), 3:(0,5,2),
  4:(0,1,2,5), 5:(0,4,2,3).
The face permutation sends (a,b) to (b,next_b(a)). Its marked exterior
boundary is (0,1,2,3), and its other six faces are triangles.

A patch consists of the indicated closed disk. Extra arcs between its
boundary vertices drawn outside the disk belong to the exterior and remain
unchanged. There are no extra neighbours of an interior vertex. All four
initial ports are distinct by the adjacent-degree-four disk lemma of C32.
Every later construction supplies its own boundary and complete rotation.

## 3. All small exterior-face identifications and direction choices

Here 'complete' refers to the following precisely bounded stage, not an
arbitrarily large outside annulus. Each case retains all old arcs. Directions
are not inferred from planarity. A third vertex cannot be u or v: those
interior vertices already have their complete four incident edges/faces.

E (new third on one edge): for each edge (a,b)=(e,e+1), attach triangle
(a,b,6), with new vertex6. The new boundary inserts6 between a,b. Its two
new arcs are 6->a if bit0 is1 and a->6 otherwise, and 6->b if bit1 is1,
b->6 otherwise. There are4 edges x4 directions per residue. It is a seven-
vertex, five-port disk, with the original two interiors still inside.
All16 cases at C0 fail the requested containment replacement below. The
other residues have the same count, but no inference is based just on that
coincidence.

C (third was an old port): let j be the corner of an outside facial triangle
(a,j,b), a=j-1,b=j+1 modulo4. Add a->b for bit0 or b->a for bit1, remove j
from the marked boundary, and retain j as an interior vertex. This is a
six-vertex, three-port disk. Four corners x two directions give eight cases.
These cover every choice of an already-present third vertex for a single
rim-edge face, with duplicates described once by the enclosed corner.

W (two adjacent outside faces have the SAME NEW third): attach
(a,j,6) and (j,b,6) at corner j. For endpoints [a,j,b], bit k=1 chooses
6->endpoint, and bit k=0 its reverse. Replace j by6 in the cyclic boundary.
This gives a seven-vertex, four-port disk with three interiors. There are
four corners x eight direction assignments per residue. The full degree
and semidegrees of the newly enclosed j are now known. Cases with either
semidegree<2 are excluded in the minimum-counterexample application.

Z (two adjacent outside faces have the opposite OLD corner as their common
third): the two triangles triangulate the entire old complementary
quadrilateral. The resulting graph has six vertices and no exterior left.
Both choices of diagonal and both directions are explicitly checked. In
particular no unseen vertices may be inserted inside a face stipulated to
be an actual facial triangle. The two endpoints off the diagonal have
full degree3; the records additionally give valid full two-colourings.

If adjacent outside triangles have DIFFERENT third vertices, this stage
has not enclosed their common old corner. Continuing around its whole
star is a larger interface. Such cases are not omitted from the root;
they remain open, and are precisely possible once its degree is at least6.

## 4. Exhaustive smaller-disk search and what a negative means

For each applicable disk P with boundary B, candidate Q keeps all directions
on the CURRENT rim, has the same distinct boundary vertices in the same
cyclic order, and fewer interior vertices. Test
  for every valid Q-colouring d, some valid P-colouring c has
  c|B=d|B and R_P(c) subseteq R_Q(d).                         (L)
The selected map is saved for EVERY valid full Q assignment; null denotes
an invalid Q assignment, not an unchecked one. Its maps use boundary-first
vertex order, explicitly stored per case.

The checker enumerates every maximal simple disk skeleton with this rim
and up to two internal vertices. It enumerates possible edge sets AND
oriented triangular face covers of all remaining darts, checks each vertex
link is one cyclic order, connectedness, and Euler characteristic2. One
rotation per edge set suffices: colouring and R depend on the arcs and
boundary labels, and the saved rotation certifies an admissible disk.
It does not assume that one particular vertex-insertion recipe generates
all skeletons. Counts of skeletons with k internal vertices are
  B3: k=0,1,2 -> 1,1,6;
  B4: k=0,1,2 -> 2,5,40;
  B5: k=0,1 -> 5,21.
Every extra edge direction is visited. The bare rim is tested first.
The resulting complete maximum-size catalogues have393,5205,693 options
for three ports/two interiors, four ports/two interiors and five ports/one
interior, respectively (including the bare rim).

Any smaller same-rim simple plane graph can be augmented, on the SAME
vertices and fixed disk boundary, to a triangulated disk by adding missing
edges. Orient the added edges without changing existing directions. If (L)
held for the unaugmented Q, it would hold after augmentation: fewer colourings
remain and each remaining R_Q can only grow. Thus failure for every maximal
completion implies failure for every smaller same-rim graph for THIS
containment criterion. This argument does not say containment is necessary
for every conceivable exterior-dependent method of lifting.

For each added Q boundary chord x->y whose pair was not already an internal
chord of P, the guard requires that the exterior y->x is absent. A consistent
existing x->y counts once. An old chord in the interior of P has no separate
exterior copy in a simple graph. The embedding stays inside the original
disk; no vertex identification, loop, reverse arc, or extra cross adjacency
is permitted. All P interior vertices are removed and Q's internal labels
are fresh. The number of vertices strictly drops by the stated amount.

To prove the all-exterior lift, fix ANY valid colouring of Q union F.
Use its entry in (L), and leave EVERY vertex of F unchanged. A monochromatic
cycle crossing the interface cuts into positive boundary paths, forming a
cyclic chain in R_P union R_F. Those entries also lie in R_Q union R_F, so
expanding them would produce a positive closed walk in the smaller coloured
graph, hence a directed cycle. This is impossible. Cycles inside a piece
are excluded separately. No induced arc has been dropped from this argument.

Selected positive rules prefer no guard. After recording one guarded rule,
the search continues through guard-free maximal candidates, not all later
guarded candidates. A guarded result therefore certifies its selected rule,
NOT a theorem that every nonmaximal guard-free alternative fails. Negatives
visit the entire maximal catalogue. Every tested negative Q has a recorded
failing colouring mask; the source specifies regeneration order exactly.

## 5. Results for all four residues, and a genuine one-face obstruction

| Stage | Types | Excluded by small semidegree | Unguarded lifts | Guarded lifts | No (L) replacement |
|---|---:|---:|---:|---:|---:|
| E |64|0|0|0|64|
| C |32|20|10|0|2|
| W |128|40|70|13|5|

Sixteen Z controls additionally give closed six-vertex graphs. Every positive
C rule is the bare triangular rim. Every selected W rule strictly shrinks
the seven-vertex patch; 70 require no reverse-arc guard. Full per-type maps
and exact original/target rotations are in the lossless certificate.
At C0, W has18 unguarded rules,4 guarded rules,2 negatives and8 small cases;
C1 has the same totals. C2 has17,2,1,12; C3 has17,3,0,12.

Remaining W cases (corner,direction bits) are
 C0: (2,2),(2,5); C1: (2,2),(2,5); C2: (0,5); C3: none.
A listed guard can still fail in an actual exterior. In C0 the four selected
guarded cases have corner2 and bits0,1,3,7, with forbidden exterior arc3->1.
This is an actual condition on G, not an assumed absent edge.

The stronger negative E(C0,edge0,bits2) has all original C0 arcs plus
0->6,6->1. Its boundary is (0,6,1,2,3), and its full rotation is
 0:(1,4,5,3,6), 1:(0,6,2,4), 2:(1,3,5,4), 3:(0,5,2),
 4:(0,1,2,5), 5:(0,4,2,3), 6:(0,1).
This is a simple plane seven-vertex patch. In boundary-first order
(0,6,1,2,3,4,5), its unattainable boundary masks are
 0,7,8,10,15,16,21,23,24,31.
For EVERY one of693 maximal smaller same-rim candidates, at least one valid
Q-colouring restricts to an unattainable P boundary mask. The executed
checker separately tests this stronger domain condition for every Q. Its
witness can be regenerated by taking the first valid Q assignment whose
boundary mask is in the displayed list. The archived per-Q failure mask
certifies (L) failure and need not itself be that stronger domain witness.
An arbitrary nonmaximal Q has a maximal
completion; its witness is also valid in Q. Hence this particular patch
precludes ANY all-boundary-preserving lift from a same-rim Q with at most
one interior, even without requiring the stronger relation containment.
A rim-only exterior already witnesses the failure. The patch remains
colourable for other boundary assignments, so it is not a root counterexample.
Seven is the least order for this specified five-port/two-interior expansion
interface, not a global minimum for all planar obstruction definitions.

The two C negatives are C0/C1 at corner2 with added3->1. The three retained
boundary vertices have a transitive monochromatic rim; the original three
interiors cannot extend it. Any replacement with at most two interiors can
give them the opposite colour, which is acyclic in a simple orientation.
Thus these negatives too have a direct boundary-assignment interpretation.
No universal bad-boundary exclusion has been inferred from planarity.

## 6. New necessary condition: each residual pair has a degree-at-least-six donor

For the four canonical residues the distinguished common neighbour is
  p=0 for C0,C1; p=2 for C2,C3.
Intrinsically it is the common facial third vertex whose two spokes to u,v
point the SAME way. The other common neighbour q has one incoming and one
outgoing spoke. At p the known consecutive four spokes are IOOI or OIIO:
the pair u,v occupies the middle equal-direction run of length two, bracketed
by opposite directions at the two other old boundary neighbours a,b.
This description is preserved by the C32 disk symmetries and all-arc reversal.

Claim: in the SELECTED triangulated minimum counterexample, d(p)>=6.

If d(p)=4, the outside wedge at p is exactly the facial triangle(a,p,b).
This is a C case with corner p. Both directions of a--b have an unguarded
bare-rim lift. The six-vertex patch is replaced by its three boundary
vertices, deleting p,u,v. The readable donor table lists all eight boundary
assignments and their full lifts (or null when the rim is cyclic).

If d(p)=5, there is exactly one additional neighbour z in that wedge.
The two exterior faces are (a,p,z),(p,b,z). When z is new, this is W at p.
ALL eight directions of the three new arcs have an unguarded bare-rim lift.
The seven-vertex patch is replaced by its four boundary vertices, again
deleting p,u,v. All sixteen boundary assignments and lifts are listed.
The new boundary retains z: we never assume its other exterior neighbours
are absent. No new diagonal or its guard is needed in these donor cases.

The possible identification z=q must be handled rather than called new.
Those two outside triangles fill the old complementary quadrilateral;
the two endpoints a,b have degree3 in the resulting closed six-vertex
triangulation. No further vertices can occupy its actual facial triangles.
This violates T4. All other old vertices are already neighbours of p or
are the saturated interiors, so there is no other identification.

Each valid smaller-graph colouring therefore lifts by Section4, contradicting
vertex minimality. Degrees below4 are already excluded. This proves the
claim using forty explicit donor tables (two C and eight W cases per residue),
not by extrapolating the unsuccessful arbitrary-ear searches.

The accompanying readable table is an exact extraction of the executed
certificate. For example, C0, degree4, added3->1 uses boundary-first order
(1,2,3,0,4,5); the eight lift entries are
  [null,41,10,11,20,21,14,null].
C0, degree5, all new arcs a->6,p->6,b->6, uses order(6,1,2,3,0,4,5), with
  [48,49,82,83,20,21,22,23,40,41,42,43,28,29,14,15].
Each integer gives ALL original vertex colours, not merely u,v. Checking
the actual arcs and boundary relation verifies every entry. The other
thirty-eight rows cover all remaining directions and residues.

## 7. A refined charge rule with an actual nonnegative donor budget

Mark every adjacent-degree-four edge uv having one of these residual codes.
Assign it to the unique donor p just identified; write q for the other
facial third vertex. Distinct marked edges at p are distinct consecutive
pairs in its rotation. Each occupies a maximal cyclic run of exactly two
equal-direction spokes, bracketed by the opposite direction. Their two-
spoke runs do not overlap. Write t(p) for the number assigned to p.

The all-order bound is
  t(p)<=d(p)-4.                                             (BUDGET)
For d>=8, t<=floor(d/2)<=d-4. For d=7, t<=3=d-4. At d=6 three runs of
length two would exhaust all six spokes and form three cyclic alternating
binary runs. A cyclic binary word has an even number of direction changes,
so this is impossible. Thus t<=2=d-4. Section6 ensures d>=6 for any donor.
Vertices receiving no assignments have t=0, and d>=4 handles them too.
No orientation word on just a sampled range is used in this proof.

Start again from C32's initial charges d(v)-4 and length(f)-4, total -8.
NEW RULE:
 (i) for each marked uv assigned to p, p sends ONE unit to the opposite
     face q-u-v (across the edge uv from its incident face p-u-v);
 (ii) p distributes its remaining d(p)-4-t(p) equally to each of its
      d(p) incident face corners.
A transfer across an adjacent face is explicitly allowed here; it is still
one named debit and one named credit, not charge manufactured on a face.
Rule(ii) at t=0 is C32's original rule. (BUDGET) makes every transfer
nonnegative, and every vertex sends exactly its initial charge and ends0.

For every face f, including faces with no marked edge, the COMPLETE final
ledger is
 mu_new(f)=length(f)-4
          +sum_(corners p of f) (d(p)-4-t(p))/d(p)
          +h(f),                                           (NEW)
where h(f) counts all opposite-face unit transfers received. Multiple
transfers are counted separately, each backed by a different marked edge.
Relative to the old C32 ledger the change is
  h(f)-sum_(corners p of f)t(p)/d(p).
Thus all losses elsewhere are stated, not hidden behind a gain at one face.

A triangular opposite face q-u-v of any marked pair has h>=1; its other
receipts are nonnegative, so it ends nonnegative. Every face of length>=4
also remains nonnegative. Vertices remain zero and the total remains -8.
The donor-side triangles, failed-guard configurations, and other triangular
faces can still be negative. We have NOT reached an all-nonnegative ledger.
This removes the opposite-face deficit of each marked residual pair while
exposing the precise new liabilities at the high donors. It does not claim
all F1 faces or all F2--F6 types are eliminated.

## 8. Actual finite execution, separate scope checks and reproducibility

The standalone checker does not import C32 or use a conjectured lift as its
cycle oracle. For every tested binary assignment it compares positive
bitset transitive closure against iterative indegree-zero deletion. Rotations
are checked by their darts, face walks, connectivity and Euler identity.
It enumerates64 E,32 C,128 W and16 Z cases:240 certificate rows. All selected
Q maps cover every valid full Q assignment, with equality of sigma and
inclusion of the entire boundary relation explicitly checked.

The full lossless certificate contains all positive lifting maps and all
negative maximal-option failing masks. It is compressed solely for bounded
transport: base64 decode its data field, LZMA-decompress, check the stated
byte count and SHA256, and parse JSON. Decoded size177992 bytes; SHA256
02c6b6477e2804d64666df268b9970cddf1484d7354a43ac9226b456ce940e85.
Failure masks index the alphabet in the decoded header, in the source's
bare-rim / internal-count / skeleton-edge-set / binary-direction order.
The archive was losslessly re-encoded from the actual zlib-packed checker
output; it binds that original output hash separately. Replaying the checker
regenerates the original zlib file named in the summary, not the later archive.
The archive decoded bytes are identical, as checked during transport packaging.
The separate donor-lifts file exposes the forty crucial maps uncompressed.
It was derived from this certificate without changing a tested map.

Selected execution: CPython3.13.5, exit0, no timeout or stderr. The wrapper
applied one CPU affinity,512MiB address space,CPU85s,wall alarm90s,parent95s,
524288-byte output-file limit and65536-byte stdout summary cap. It denied
socket/socketpair/connect syscalls. Actual elapsed27.444805s; summary1959
bytes; source/input/wrapper/executable/output hashes are in execution.json.
The 8128 binary direction words through degree12 are controls for (BUDGET),
not its all-order proof. No real graph is assumed to realize every word.

These are explicitly generator checks under the direct user request, not
registered verifier receipts, CI mathematical validation, or signed admission.
Lean and elan were absent from the recorded PATH probe. No elaboration or
axiom/escape report occurred. A trusted scope/faithfulness review is requested
for the finite certificates, triangulation wedge applications and charge
rule separately. T3,T4,C31,C32,C33 and root must keep their statement identities.

## 9. Dependency DAG, failed shortcut and first remaining configuration

New proof units, not new admitted obligation records:
 A: exact facial attachment and identification -> enumerated finite maps;
 B: all-assignment sigma/R certificate -> strict-size all-exterior lifting;
 C: triangulation degree4/5 wedge + donor maps + B -> donor degree>=6;
 D: four-spoke run pattern + C -> unrestricted donor budget;
 E: D + explicit debit/credit bookkeeping -> (NEW) and targeted nonnegative faces.
No arrow goes from a finite untested exterior or an unexplained average-degree
claim to root. The completion argument is scoped to the required containment
criterion; exceptional stronger negative certificates are labelled separately.

Rejected auxiliary shortcut: attaching a single new-third exterior triangle
to C0 always permits a same-five-port smaller containment replacement. All
sixteen first-stage directions fail that shortcut; E(0,2) gives the stronger
actual no-all-boundary-lift witness. The parent route and root are not negated.
No new failed-route ledger is written by the generator. The previously rejected
same-four-port search and dynamic-width shortcut are not retried.

first_open_configuration: residual C0 at its OTHER pole2, wrap bits2 or5;
 a guarded positive wrap blocked by exterior3->1; or a high donor (degree>=6)
 with at least two distinct outside neighbours requiring a larger interface.
The analogous C1/C2 wrap residues and guard failures remain listed above;
C3's one-shared-third wrappers have rules but their guards still matter.
The negative charge after (NEW) may be on donor-side triangles or other
F2--F6 direction/guard types. A new global counting argument is still needed.

next_action: include the second distinct exterior neighbour of the high donor,
 or use a forced reverse boundary chord in the remaining wrap; prove a new
 all-exterior smaller-patch lift or a quantified global restriction, then
 audit the remaining donor-side charge. Do not simply assume (NEW)>=0 everywhere.
checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
best_verified_result: none
next_obligation: obligation:opg169-root
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
root_closed: false
