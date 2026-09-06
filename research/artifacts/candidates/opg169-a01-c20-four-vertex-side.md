# C20: four-interior-vertex sides of a directed triangle are excluded

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c20-four-vertex-side
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 7580d436b6fec2ab0926897a8abba40cab8209f4
Primary owner: math-proof.

## 1. Scope and exact count

Let T be C09's selected maximum-size minimum-order counterexample.
Let S be a directed separating triangle, and suppose one of its sides
has exactly four interior vertices I. Let J=T[I] be their underlying
induced graph and write e=|E(J)|. The closed disk on S union I is a
triangulation with seven vertices and fifteen edges. An interior vertex
has no neighbors outside this disk. Consequently
  sum_{x in I} degree_T(x) = 12+e.
All four degrees are at least four, so e>=4; simplicity gives e<=6.

C15 is used as an explicit proof-draft dependency: in this selected T,
the induced degree-four subgraph has components only isolated vertices,
single edges, or directed facial triangles. In particular it cannot
contain an induced three-vertex path or a connected set of four vertices.

This lemma does not claim a universal extension theorem for every
seven-vertex disk orientation regardless of its criticality constraints.

## 2. Four interior edges

If e=4, the degree sum is sixteen and all four interior vertices are
degree four in T. A simple graph on four vertices with four edges is
connected: a disconnected one has at most three edges, attained by a
triangle and an isolated vertex. The four vertices would therefore lie
in a single degree-four component of order at least four, contradicting
C15. Edges to additional low boundary vertices could only enlarge that
component and cannot repair the contradiction.

## 3. Five interior edges

If e=5, J is K4 with one edge removed. The full interior degree sum is
seventeen. Exactly one interior vertex h has degree five in T and the
other three have degree four.

If h has degree three inside J, removing it leaves a three-vertex
path on the three low vertices. This is forbidden by C15. Thus h is
one endpoint of J's missing edge and has internal degree two. The
other three vertices form a low triangle.

Those three vertices are an entire low component by C15. C11 supplies
its octahedral disk patch with three distinct outside boundary vertices.
Since h is adjacent to two of the low vertices, it is one of these
boundary vertices. The other two, x,y, belong to S: there is no other
vertex in the closed disk to choose. Denote the remaining vertex of S
by z.

Delete the three low vertices from the seven-vertex disk. They have
degree sum twelve and three mutual edges, so exactly nine edges are
removed. Six edges remain on {h,x,y,z}, which must be the complete
graph K4. Geometrically, the removed low patch has become the triangular
face hxy of this core. All other edges and orientations are unchanged.

Take any valid coloring of the actual exterior of S, which exists by
global minimum order. Its restriction to S is nonconstant because
S is directed. Color h opposite to the majority color of S.
The four vertices of the K4 core are now colored two and two.

Each induced color class of the core has two vertices and is acyclic
in an orientation. Every triangular subset of the four core vertices
is nonconstant, including the marked face hxy. By C11's explicit
octahedral construction this coloring extends across the three deleted
low vertices. The resulting disk coloring is acyclic by gluing along
the complete tournament hxy.

Finally glue this disk to the actual exterior along the complete
tournament S. Tournament gluing rules out any cross-piece monochromatic
cycle. The result colors T, contradicting its definition. Thus e=5
is impossible.

The 2+2 core coloring works for every nonconstant coloring of S and
for every orientation of the core. It is not an assumed coloring
extension theorem for unrestricted larger planar pieces.

## 4. Six interior edges

If e=6, J=K4. The connected outer triangle S lies in one face of this
embedded K4, since it is disjoint from J. Every face of a plane K4 is
triangular. The fourth vertex of J lies on the other side of that
face's bounding triangle from S.

No edge from that fourth vertex to S can cross this separating
triangle. There are no other interior vertices to serve as neighbors,
and vertices on the other side of S cannot be reached without
crossing S. Its only neighbors in T are therefore the other three
vertices of J. This contradicts minimum degree four.

This is a Jordan-separation argument in the existing embedding,
not an assertion that a four-clique can never occur in a triangulation.

## 5. Consequences

All three possibilities e=4,5,6 are impossible. Hence no directed
separating triangle in the selected T has exactly four interior
vertices on a side.

Together with C19's exclusions for one, two and three interior vertices,
each side of any directed separating triangle has at least FIVE
vertices. Therefore a T with such a separator has
  |V(T)| >= 3+5+5 = 13.

C19 consequently forces a degree-five vertex with exactly one directed
incident face to lie on a directed separating triangle whose two sides
each have at least five vertices. This remains a necessary structural
condition. It is not an absolute order bound for the root, a sharp
published bound, or proof that the separator cannot exist.

## 6. Dependencies and attack pass

Frozen inputs: canonical contract; C09 selected triangulation and minimum
degree; C11 exact low-triangle geometry and nonconstant-boundary extension;
C15 classification of low components; C19 small-side count.

All low degrees above are degrees in the FULL T. The interior edge
count is not substituted for the full degree. The e=5 case distinguishes
the two orbits of vertices in K4 minus an edge before applying C15.
The leftover K4 is established by its exact edge count, not by a
drawing guess. Color agreement and all boundary arcs are retained in
both uses of tournament gluing. No solver, enumeration, formal compiler
or new external theorem was used.

## 7. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c20-four-vertex-side
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; prior local exclusions remain
recorded in their immutable candidates.
next_obligation: obligation:opg169-strong-min-degree-three
next_action: analyze the unique interior-side neighbor of a one-face
degree-five vertex. Test safe contraction of their common edge, then
derive a bounded support capacity using their cyclic links.
No mathematical verification receipt or admission is asserted.
