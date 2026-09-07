# R08 C29: frozen planar deletion, simultaneous pair moves, and dynamic state faithfulness

Verdict: candidate_only. Status: proof-drafted with actual bounded generator checks.
Candidate: candidate:opg169-a01-root-boundary-20260907-proof
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Current packet target: obligation:opg169-root (already admitted).
Base: 39ad97152d3d1f5a4eafbf5037be0181386ce84a
Primary owner: math-proof. No C27 dependency or extension.

## 1. Exact scope and the discharging gap

All graphs in the root contract are orientations of finite simple planar
underlying graphs. A valid colouring c:V->{0,1} makes BOTH FULL induced
colour classes acyclic. Empty classes are permitted. Directed cycles have
positive length; a length-zero self-path is used only for reachability.

T3 denotes the admitted necessary condition, strong connectivity and
underlying minimum degree at least three. T4 denotes the separately
identified proof candidate giving both semidegrees at least two and
underlying minimum degree at least four. These are supplied proof-draft
dependencies, not trusted EvidenceLinks. The root still quantifies over
EVERY graph and asks for SOME colouring. No result below closes it.

If a minimum-order counterexample exists, deleting a proper vertex set
preserves simplicity, planarity and the inherited orientation, and
strictly decreases the finite vertex count. Minimality therefore supplies
a valid colouring of each proper induced subdigraph. The empty graph and
loopless singleton are colourable. The T3/T4 proofs derive nonemptiness
and strong connectivity using the SCC condensation DAG, keeping every
induced cross-SCC arc. These proofs remain separately identified.

For n>=3, the simple planar edge bound m<=3n-6 and T4 give
  2*n4+n5 >= 12 + sum_{d>=7}(d-6)*n_d.                    (E)
This follows by writing sum_v(6-degree(v))=6n-2m>=12 and collecting terms.
Thus a degree-four or degree-five vertex exists, indeed n4+n5>=6.
C04 already supplied this counting argument. It does NOT imply that an
arbitrary deletion colouring extends at such a vertex. One must prove
an unavoidable configuration with a valid colouring lift.

## 2. Blocking paths, rotations, and the reduction already obtained in C28

Fix ANY valid colouring c of H=G-v. Giving v colour k fails iff there
are i->v and v->o, c(i)=c(o)=k, and a directed o-to-i path wholly in
H[c^{-1}(k)]. A new monochromatic cycle must contain v; removing v proves
necessity. Appending i->v->o to the simple return path proves sufficiency.
The endpoints are distinct because opposite arcs are forbidden and neither
is v because there are no loops. Merely present neighbours do not suffice.

At degree four, two failed colours use four distinct neighbours, one
incoming and one outgoing for each colour. Their return paths are
vertex-disjoint, since their colours differ. Closing them through v
produces simple curves meeting only at v. The pairs cannot alternate in
its rotation: one curve is a Jordan curve, and the other curve minus v
is connected, disjoint from it, and confined to one side. Alternating
ends would force a crossing. Thus I1,I2,O3,O4 has only the matching
I1-O4,I2-O3, while I1,O2,I3,O4 has the two adjacent in/out matchings.
These are necessary restrictions, not assertions that the paths exist.

A full SCC below means a strongly connected component of the UNCOLOURED
H. Complementing all colours on one such SCC preserves validity: every
directed cycle of H is wholly inside one SCC, whose colours are either
unchanged or all complemented. Cross-SCC arcs are retained. In contrast,
monochromatic SCCs are singletons when the colouring is valid.

C28 proved the following all-orders reduction. If v has degree four and
its neighbours are not all in one SCC of H, any valid colouring of H
can be made extendible by complementing at most one full SCC.
If the incoming pair is in different SCCs, complement one to make their
colours equal, and give v the missing incoming colour. The outgoing-pair
case is identical with directions reversed. Otherwise the incoming pair
is in a single SCC A and the outgoing pair in a single SCC B, A!=B.
Paths inside A and B joining their respective neighbour pairs are disjoint;
planar separation forces an IIOO, not an IOIO, rotation. A double block
uses its unique noncrossing in/out matching. Complement B only. This
switches the same-colour matching to the crossing one, which cannot
support two disjoint return paths. Some colour now extends at v.

Consequently in a minimum counterexample all neighbours of a degree-four
vertex lie in a single SCC S of G-v. Strong connectivity of G then makes
S all of H: simple v-to-x and x-to-v paths yield inside H a path from
an outgoing neighbour to x and from x to an incoming neighbour. Thus
G-v must be strongly connected for EVERY degree-four vertex.
This is a reused C28 theorem; it does not show such a vertex is reducible.
The small-side argument alone also handles degree five when its unique
semidegree-two side is split across deletion SCCs. No contraction is used;
only class-preserving deletion and colour changes occur.

## 3. A nine-vertex planar obstruction to arbitrary-length single/SCC repair

Let H have vertices 0,...,7 and EXACTLY the following 17 arcs:
  2->0, 0->3, 4->0, 0->5, 0->6, 7->0,
  1->2, 3->1, 4->1, 1->5, 6->1, 1->7,
  2->3, 3->4, 5->4, 5->6, 6->7.
Add v=8 and EXACTLY the four arcs
  0->8, 8->2, 8->1, 7->8
 to obtain G. The input JSON lists every arc, with no omitted additions.

The underlying G is the bipyramid over cycle 2,3,4,5,6,7,8,2, with poles
0 and 1 in opposite hemispheres. This gives a crossing-free sphere
embedding and hence a plane embedding after removing a point of a face.
A complete rotation system is:
  0: 2,3,4,5,6,7,8       1: 8,7,6,5,4,3,2
  2: 0,8,1,3             3: 0,2,1,4
  4: 0,3,1,5             5: 0,4,1,6
  6: 0,5,1,7             7: 0,6,1,8
  8: 0,7,1,2.
The face permutation (a,b)->(b,next_b(a)) has 14 triangular orbits,
9-21+14=2, with every dart accounted for. Deleting 8 leaves 11 faces,
one bounded by B=(0,2,1,7); 8-17+11=2. The checker verifies the rotations
against the full undirected edge set. No opposite arcs or loops occur.
At 8 the I/O word is I,I,O,O, in the displayed rotation.

Colour even vertices of H with 0 and odd vertices with 1; denote this c.
The full induced colour-0 arcs are 2->0,4->0,0->6, with topological order
(2,4,0,6). Colour 1 has 3->1,1->5,1->7, with order (3,1,5,7).
Thus c is valid, not just a colouring of a selected acyclic subgraph.
Changing ANY SINGLE vertex creates the following monochromatic cycle:

| Vertex changed | Cycle after that change |
|---|---|
| 0 | 0->3->1->7->0 |
| 1 | 1->2->0->6->1 |
| 2 | 2->3->1->2 |
| 3 | 3->4->0->3 |
| 4 | 4->1->5->4 |
| 5 | 5->4->0->5 |
| 6 | 6->1->5->6 |
| 7 | 7->0->6->7 |

These eight explicit cycles certify the absence of a first legal
single-vertex move, hence of any positive-length sequence of such moves.
H is strongly connected: 0->3->4->1->2->0 is a cycle, and the other
vertices join it by 0->5->4, 0->6->1 and 1->7->0. Thus its only full-SCC
palette change is global complementation. The complement of c is also
frozen. With single-vertex changes and whole uncoloured-SCC complements
allowed together, the reachable set is EXACTLY {c,complement(c)}.

Neither colouring in this orbit extends at 8. For c, colour 0 creates
8->2->0->8 and colour 1 creates 8->1->7->8. Complementation interchanges
the roles of the two colours. This is a finite complete certificate
against the proposed UNIVERSAL repair tactic for an arbitrary deletion
colouring. It does not rule out other simultaneous recolouring moves.

G itself is strongly connected, all seven equatorial vertices have
in=out=2, and poles 0,1 have (in,out)=(3,4),(4,3). Its degrees are seven
4s and two 7s, so average degree=42/9<6 and (E) holds with equality:
14=12+2. It is therefore a genuine oriented planar obstruction to the
tactic even in the presence of these necessary degree conditions.
It is NOT claimed to be a minimum counterexample to the root.

Indeed G has the explicit valid colouring
  colour 1: {0,1,3,5}, with topological order (0,3,1,5);
  colour 0: {2,4,6,7,8}, with topological order (4,6,7,8,2).
All induced arcs respect these orders. Thus the frozen witness is NOT
a root counterexample, and it does not disprove all discharging methods.

The boundary requires four vertices for two blocked colours, by Section 2.
The earlier five-vertex pair of directed triangles achieves the minimum
order for fixed-colouring extension failure. The present stronger
nine-vertex recolouring obstruction is NOT claimed globally minimum.
Neither unrecorded exploration nor a search over one embedding per graph
is used for a minimality claim here.

## 4. Exact opposite-colour pair-swap criterion

Let c be ANY valid colouring of a loopless orientation H, with x colour 0
and y colour 1. Change both simultaneously. The new colour-1 class is
(old colour 1 minus y) plus x; the new colour-0 class is (old colour 0
minus x) plus y. The retained old classes are induced DAGs.

The swap is valid IFF both of the following are absent:
(a) a path, all of old colour 1 in H-{x,y}, from a remaining out-neighbour
    of x to a remaining in-neighbour of x;
(b) a path, all of old colour 0 in H-{x,y}, from a remaining out-neighbour
    of y to a remaining in-neighbour of y.
Necessity and sufficiency follow by deleting the newly added vertex from
any new cycle in its class, or by completing such a path through that
vertex. The edge xy, if present, remains bichromatic. No arc is omitted.
Equivalently every blocking cycle from flipping x alone must meet y,
and every one from flipping y alone must meet x.

For the frozen example change vertices 0 and 7 together. This yields the
colour-1 set {0,1,3,5} and permits 8 to receive colour 0, as displayed above.
Neither individual change is legal, so this is NOT a two-step path in
the single-vertex recolouring graph. A valid pair swap still needs a
separate extension check at v; no universal successful pair is asserted.

## 5. Exact static composition and a dynamic counterexample on the SAME graph

Reuse C13/C28's static state (sigma,R): sigma gives the colours of labelled
boundary B, and R contains positive monochromatic boundary-to-boundary
reachability, including paths via other boundary vertices. For valid
coloured pieces P,F meeting exactly at B, with disjoint interiors and no
other cross-arcs, their union is valid IFF (R_P union R_F)^+ has no diagonal.
Shared boundary arcs must agree in direction. Cut a cross-piece cycle
at successive boundary visits for one implication. Expand a positive
cyclic chain of relation entries into the actual paths for the other:
the result is a positive monochromatic closed walk, which contains a
cycle. This proof handles shared path vertices and keeps all induced arcs.

In the example P is the four-spoke star at 8 and F=H. For c its boundary
state is sigma=(0,0,1,1), R={(2,0),(1,7)} on B=(0,2,1,7).
On the SAME H, let d have colour-1 set {1,4,7}. It has exactly that same
sigma and R; the uncoloured boundary reachability is necessarily also
identical. Its full colour-0 order is (2,0,3,5,6), and colour-1 order
(4,1,7). Yet changing vertex 0 in d is legal: the new orders are
(2,3,5,6) and (4,1,7,0). Now both incoming neighbours 0,7 of 8 have
colour 1, so 8 can be coloured 0. Thus d has a one-step escape while
c has no first step, even though their complete static states coincide.

Therefore an existential transition witnessed by one representative
of a static state cannot be assumed liftable from another representative.
C13's static colourability composition theorem is not contradicted.
For a finite patch, retaining actual colouring witnesses and their move
components is one exact option; no uniformly bounded boundary-only
reconfiguration compression is established here.

A valid one-sided replacement rule is: for EVERY state of a smaller
patch P', supply a P-colouring with the same sigma and R_P subseteq R_P'.
If P' glued to exterior F is valid, its reachability union has no cycle;
the smaller union using R_P also has no cycle. This gives an EXISTENCE
lift, not necessarily a legal move sequence from a prescribed colouring.
For minimality one must separately prove the replacement stays in the
same disk with the same cyclic boundary labels, compatible shared arcs,
no loop/digon or boundary identification, no extra interior/exterior
adjacencies, and strictly fewer interior vertices. These hypotheses
ensure class preservation. No such universal dominating smaller patch
has been supplied for the remaining strongly connected deletion.

## 6. Executed finite checks and provenance correction

The original 0..4 enumerator and its 21-mutation input have actual saved
runs, including the already merged C28 execution bundle. Coverage is
761 labelled orientations, 11895 full assignments, 23665 deletion
assignments (23233 valid, 432 rejected), and 46466 extensions, with all
21 fixtures and five wrong-semantics controls passing. These are bounded
generator self-tests, not trusted verifier receipts or a universal proof.
The historical replay files preserved on this branch record their own
actual timing and output hashes; old source files are not resubmitted.

The exact patch checker and JSON input on this branch have been recovered
from connector text and matched to their Git blob AND SHA-256 identities.
A further replay using the newly archived c29-replay.py pins CPython
3.13.5 and enforces one-CPU affinity, 512 MiB address space, 20 CPU seconds,
25 wall seconds, 65536 bytes per output file, and seccomp denial of
socket/socketpair/connect. Its actual record is c29-replay.json.
It exits 0 with no stderr. This replay matches the historical patch
output byte-for-byte, not merely its expected totals.

The checker uses indegree-zero deletion and DFS cycle detection, checks
all specified cycles and orders, both sphere rotations, strong connectivity,
all 256 H assignments and all 512 G assignments. It finds:
- H has 54 valid colourings and single-flip component sizes 1,1,52;
- its only frozen colourings are masks 85 and 170;
- the single-plus-whole-SCC orbit of 170 is {85,170}, with no extension;
- G has 62 valid colourings and 44 H colourings are extendible;
- minimum simultaneous change distance from 170 to an extendible state is 2;
- all 832 opposite-colour pair cases agree with the pair-swap criterion;
- all 108 star/exterior compositions agree with the static criterion;
- masks 146,154,170,210,218 share the initial boundary state.
Masks encode colour 1 at bit x. These counts concern THIS explicit graph.

The earlier unsubmitted proof revision claimed a replay archive containing
three exploratory searches and their outputs. That archive is not present
in this branch and is not used or asserted delivered. That sentence and
its exploratory count claims are withdrawn in this revision. The archived
checker, input, actual outputs and c29-replay wrapper suffice to reproduce
all finite claims made here. No global smallest-order assertion relies
on exploratory searches. This correction changes no arc or theorem.

The bounded PATH lookup found neither lean nor elan in this runtime.
No Lean elaboration or axiom/escape report exists for these candidates.
The old proposed CPython 3.12.10 pin is not falsely reported as used;
actual replays are labelled 3.13.5. Profile, registry and workflows have
not been edited to turn generator execution into trusted admission.

## 7. Dependency and review units; nonterminal checkpoint

Definitions and valid deletion -> exact blocking iff -> pair criterion.
Plane rotations plus blocking iff -> nonalternation -> C28 SCC reduction.
The explicit arc list, orders, eight cycles and strong H -> frozen orbit.
Two explicit colourings and their boundary paths -> static state does not
preserve move availability. Positive-path composition -> one-sided state
domination and the conditional replacement lift. No circular dependency
or inference from a finite enumeration to an all-orders theorem is used.

The rejected shortcut is narrowly: EVERY valid colouring of a degree-four
vertex deletion can be rescued using legal single-vertex changes and
whole uncoloured-SCC palette complements. Its complete finite obstruction
is this G,H,c. The parent admitted route, T3, T4 and root are not rejected.
Only a failed-route PROPOSAL is submitted; no truth ledger is edited.

All applicable discipline checks are explicit: full induced arcs and old
colours are invariants; finite vertex count decreases for minimality;
path shortening and finite state searches terminate. Symmetry is exact
colour complementation, not an assumed orbit quotient. Probability and
asymptotics are inapplicable. Planarity is supported by both a direct
bipyramid embedding and the full oriented rotation certificate.

Review/admission units stay distinct: existing T3, separately stated T4,
C28 reducibility, C29 frozen-move obstruction/pair criterion/state example,
and the universal root. No evidence for one is relabelled as another.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none (registered-verifier meaning)
best_bounded_result: executed finite checks and explicit frozen-orbit
  certificate, plus proof drafts of pair-swap and replacement criteria.
first_open_configuration: degree-four (2,2) with strongly connected deletion
  and noncrossing blocked return paths; degree-five (2,3)/(3,2) remains open.
next_action: construct a boundary-dominating smaller replacement or prove
  an attainable simultaneous repair for that configuration, AND show an
  unavoidable reducible configuration by a valid discharging argument.
  Do not reuse the false single/SCC repair claim or a static-state move lift.
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
root_closed: false
No planar contradiction or full-domain counterexample is obtained here.
