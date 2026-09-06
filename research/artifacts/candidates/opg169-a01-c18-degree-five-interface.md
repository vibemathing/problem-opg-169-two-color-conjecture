# C18: exact degree-five wheel extension with one return-path bit

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c18-degree-five-interface
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 8fb5a84a2bb54a5e37592e9eb4820ee80122f0b0
Primary owner: math-proof.

## 1. Frozen scope

Take five distinct boundary vertices a,b,c,d,e in this cyclic order
on a disk. Inside the disk place one vertex v and exactly its five
spokes; retain the oriented boundary cycle. The five triangles at v
are actual faces. The exterior F is any finite simple plane orientation
in the complementary disk containing all boundary edges. It may have
other vertices and boundary diagonals. Fix a valid acyclic two-coloring
phi of ALL of F. No vertex of F is recolored in this extension test.

The theorem determines existence of a color for v for this fixed phi.
It is universal over compatible F and phi, and does not assume that F
or the completed graph is a minimum counterexample. The later application
uses the selected triangulation T of C09. No new admitted node is created.

For neighboring rim vertices x,y, let D(vxy) mean that their oriented
triangle with v is directed. For any same-colored rim pair x,y, define
R_phi(x,y) as follows. If their spokes have the same direction at v,
R_phi(x,y)=0. Otherwise let o be the out-neighbor of v in the pair and
i its in-neighbor. Set R_phi(x,y)=1 exactly when F has a monochromatic
directed path o-to-i in their common color. This is an actual path,
not the mere presence of colored in/out neighbors.

The value of R depends on the entire exterior. Each table entry below
needs at most ONE such Boolean value in addition to local orientations
and the five boundary colors. We do not assert that one universal bit
serves all boundary assignments or all partially colored exteriors.

## 2. Exact obstruction and the adjacent-pair simplification

Putting v in color A fails exactly when two of its A-colored neighbors
o,i have spokes v->o and i->v and a directed A-colored path o-to-i in F.
Necessity follows by deleting v from a new monochromatic simple cycle:
every new cycle must contain v since phi was valid on F. Sufficiency
follows by adjoining the two spokes to a simple such path.

If the two neighbors x,y are adjacent on the rim, this obstruction
is exactly D(vxy). Indeed a directed triangle immediately blocks the
color. If the spokes have opposite directions but the triangle is
transitive, the boundary arc is i->o. A monochromatic o-to-i path would
then form a cycle already in F, impossible. Same-direction spokes cannot
be used by a cycle through v. Thus no nonlocal query is needed for an
adjacent same-color pair.

## 3. Complete five-rim table

If a color occurs at most once on the rim, assign it to v. No directed
cycle through v can use two distinct same-color neighbors. This covers
boundary multiplicities 5:0 and 4:1 and their color exchanges.

In all remaining cases one color B occurs twice and the other color A
occurs three times. Up to rotation, reflection, and exchanging color
names, there are precisely two cases.

Case I: consecutive minority pair.
  phi(a)=phi(b)=B; phi(c)=phi(d)=phi(e)=A.
There is NO extension if and only if
  D(vab) AND (D(vcd) OR D(vde) OR R_phi(c,e)).

The only possible B obstruction uses a,b and is D(vab) by Section 2.
The three possible unordered A obstruction pairs are cd,de,ce.
The first two are local triangle tests; the last is R_phi(c,e).
This proves both directions without any further topological assumption.

Case II: separated minority pair.
  phi(a)=phi(c)=B; phi(b)=phi(d)=phi(e)=A.
There is NO extension if and only if
  D(vde) AND R_phi(a,c).

The B obstruction is precisely R_phi(a,c). If it is absent B extends.
If it is present, choose one simple monochromatic B path joining a,c
in F. It separates the two boundary intervals: b is on one side and
d,e on the other. A monochromatic A path from b to d or to e would
join alternating boundary endpoints with that B path. Such paths must
meet in a disk, but different colors forbid a common vertex. Boundary
touches do not change this separation argument. Hence a simultaneous
A obstruction can only use d,e and is exactly D(vde) by Section 2.
Conversely the directed triangle vde and the indicated B path block
both choices. This proves the equivalence.

The table exhausts all 32 labeled boundary assignments: the automatic
cases cover 12, and the 3:2 cases cover 20. This count is a binomial
identity, not a report of an executed enumeration.

## 4. Consequence for the selected minimum counterexample

For each degree-five vertex v of C09's T, choose any valid coloring of
T-v by minimum order. It cannot extend. By Section 3 there is a directed
facial triangle at v whose two rim vertices have the same color in that
coloring. In particular every degree-five vertex of T is incident with
at least one directed facial triangle.

The particular facial obstruction may depend on the coloring of T-v.
The table does not prove two directed incident faces, unconditionally
eliminate v, or color the whole high core. C09/C16's degree-four tables
must not be silently reused as a face-only degree-five table.

## 5. Six-vertex witnesses that the return bit is necessary

Both examples use the same underlying sphere triangulation: the wheel
with cyclic rim a,b,c,d,e and hub v, with exterior diagonals ac and ad.
The disk outside the wheel is triangulated by abc, acd, ade.
There are six vertices and twelve distinct underlying edges.

The common spokes and rim arcs are:
  a->v, v->b, v->c, d->v, v->e;
  a->b, b->c, d->c, e->d, a->e.
The common second diagonal is a->d.

In the bad-extension graph orient the first diagonal c->a.
In the good-extension graph orient it a->c.
These are alternative orientations, not simultaneous opposite arcs.

Fix phi(a)=phi(c)=B and phi(b)=phi(d)=phi(e)=A.
In F=G-v, the B class has just its one diagonal arc, and the A class
has just e->d and the isolated b. Thus phi is valid for both graphs.

All five faces at v have identical orientations in the two graphs.
Only vde is directed: d->v->e->d. It blocks color A in both graphs.
The other four faces at v are transitive.

In the bad-extension graph color B is blocked by a->v->c->a,
and R_phi(a,c)=1. Neither color extends.
In the good-extension graph the B class after adding v is the
transitive triangle a->v->c, a->c. Hence v=B extends, and R_phi(a,c)=0.

Both FULL graphs themselves are two-colorable. The partition
  {v,a,b} | {c,d,e}
works in either graph: the first class is the transitive triangle
a->v->b with a->b, and the second class is the path e->d->c.
Neither diagonal crosses the two color classes internally.

Thus identical local wheel faces and identical boundary colors can give
opposite extension-existence answers. This excludes the general face-only
shortcut, not the root conjecture. The witnesses are not asserted to
satisfy the minimum-counterexample semidegree or saturation consequences.
In particular the witness does not exclude a future face-only theorem
under ADDITIONAL, separately justified hypotheses.

## 6. Source and adversarial audit

Repository inputs fresh-read at the base: C09's alternating-path argument,
C16's universal small-patch tables, C17's current checkpoint, the frozen
contract, and the empty failed-route ledger.

A bounded web search for planar digraph degree-five precoloring extension
and wheel monochromatic paths returned, among other sources:
- Harutyunyan and Mohar, Planar Digraphs of Digirth Five Are 2-Colorable,
  J. Graph Theory 84 (2017), 408-427, DOI 10.1002/jgt.22032.
- Li and Mohar, Planar Digraphs of Digirth Four are 2-Colorable,
  DOI 10.1137/16M108080X.
The primary publisher abstracts were inspected on 2026-09-06.
https://onlinelibrary.wiley.com/doi/10.1002/jgt.22032
https://epubs.siam.org/doi/10.1137/16M108080X
They assert whole-graph coloring under digirth restrictions, not the
unrestricted fixed-boundary extension assertion here. Those hypotheses
exclude the directed facial triangles essential in this table.
No theorem from them is imported into this proof. The table is a direct
candidate derivation; no novelty or exhaustive literature claim is made.

Attack checks: never infer a return path from two colored neighbors;
retain the rim arc in the adjacent-pair argument; use planarity only
where two differently colored paths would cross; distinguish fixed
phi from existence of some coloring of F; do not merge the two alternative
diagonal orientations into a digon. The witnesses have explicit valid
full colorings. No mathematical program was run.

## 7. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c18-degree-five-interface
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; general face-only degree-five
extension shortcut excluded by Section 5, while the admitted route stays open.
next_obligation: obligation:opg169-strong-min-degree-three
next_action: use the exact table to analyze a degree-five vertex incident
with exactly one directed face. Test the resulting forced opposite
boundary pairs by safe single-diagonal insertion, not by reversing an
existing exterior arc.
