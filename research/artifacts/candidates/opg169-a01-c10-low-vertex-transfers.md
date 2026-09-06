# C10: color transfers classify the degree-four subgraph

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c10-low-vertex-transfers
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: c4904b472b580c6faa425fd83be96faaf9f7a51f
Primary owner: math-proof.

## 1. Frozen scope and the new conclusion

Assume a counterexample exists in the full frozen class of orientations
of finite simple planar graphs. Choose T of minimum vertex count, and
then maximum arc count on that vertex set as in C09. Thus U(T) is a
3-connected plane triangulation and every vertex has both semidegrees
at least two. Let L be the set of vertices of underlying degree four,
and let H=V(T)\L. A low vertex means a member of L, hence has indegree
two and outdegree two. All induced arcs are retained.

We prove directly that U(T)[L] is a disjoint union of paths (including
isolated vertices) and triangles. Every triangle component is directed
and facial in T. In particular each low vertex has at least two
neighbors in H. This is a necessary structural refinement, not a
contradiction or closure of the root conjecture.

The transfer and forbidden-triangle/diamond arguments use only global
vertex minimality and the semidegrees. The link and face arguments use
the chosen triangulation. We do not assume T is arc-critical.

## 2. Exact color incidence at an uncolored low vertex

Take any valid acyclic two-coloring of T-v with v low. If a color is
absent from N-(v), giving v that color creates no monochromatic cycle:
a new cycle would contain v and need a same-colored incoming arc.
The analogous statement holds for N+(v). Since T cannot be colored,
each of the two colors appears among each of its two in-neighbors and
among each of its two out-neighbors, necessarily once in each pair.

This condition is obtained from actual extension failure. Mere
presence of same-colored incoming and outgoing neighbors is not
asserted sufficient for failure; a directed return path is also needed.

A transfer from u to the uncolored v means: erase u's color and give
that color to v. It is safe whenever u is adjacent to low v. If u->v,
u was the unique in-neighbor of that color; after erasing u, no new
monochromatic cycle through v is possible. For v->u use the out-side.
All other colored vertices induce a subdigraph of the old acyclic
color classes. The result is a valid coloring of T-u.

To transfer again, the new uncolored vertex must be low. Every move
below meets that requirement. A transfer is a coloring operation,
not necessarily movement in the direction of the digraph arc.

## 3. Every all-low triangle is directed

Suppose instead that a triangle of low vertices is transitive, labelled
x->y, x->z, y->z. Start with a valid coloring of T-x. Let the colors
of y,z be A,B. They differ because they are the two out-neighbors of x.
Let w be the other out-neighbor of y besides z; w is outside {x,y,z}.

First transfer y to x. The uncolored vertex is now y, while x has A
and z has B. By Section 2 applied to y, w has A.

Independently return to the original coloring of T-x, transfer z to x,
and then y to z. The uncolored vertex is again y, but now z has A.
The vertex w has not changed and still has A. Thus both out-neighbors
of y have color A, contradicting Section 2. This excludes the
transitive orientation, so every all-low triangle is directed.

## 4. No two all-low triangles share an edge

Suppose triangles uvx and uvy have four distinct low vertices. Extra
edges among these vertices are allowed in this argument. By Section 3
both triangles are directed. Reverse all arcs and relabel if necessary
to have u->v, v->x, x->u and v->y, y->u.

Start with a valid coloring of T-u. Write color(x)=A, color(y)=B;
these differ because x,y are the two in-neighbors of u. Write color(v)=C.

Perform the three transfers x to u, v to x, and u to v. The uncolored
vertex is u again, x now has C, and y still has B. Section 2 implies
C!=B, so C=A.

From the original coloring instead perform y to u, v to y, and u to v.
Now u is uncolored, y has C and x still has A. Thus C!=A, so C=B.
The two conclusions contradict A!=B. This excludes every all-low
diamond (and also any larger graph containing those two triangles).

## 5. Each low vertex has at most two low neighbors

The four neighbors of a low vertex v form its cyclic link in the plane
triangulation. Any choice of three positions in a four-cycle contains
three consecutive positions. If at least three neighbors were low,
write such a consecutive triple as a,b,c. The facial triangles vab
and vbc would be two all-low triangles sharing vb, excluded by Section 4.

Consequently the maximum degree of U(T)[L] is at most two. Its finite
connected components are paths, cycles or isolated vertices. Triangle
components have the directed orientation from Section 3.

## 6. A low cycle of length at least four would force a colorable bipyramid

Suppose a component is the cycle v1,...,vk,v1, k>=4. At vi its two
cycle neighbors are not adjacent in U(T): such an edge would give
a cycle vertex a third low neighbor (also when k=4). Thus those two
neighbors are not consecutive in the four-position link of vi.
They alternate with vi's two high neighbors, say p_i and q_i.

The two facial triangles incident with edge vi vi+1 have third
vertices p_i,q_i. Viewed at vi+1, the same third vertices are its two
high neighbors. Hence {p_i,q_i} is a single constant pair {p,q}
all around the cycle.

The underlying subgraph B consists of the cycle and two distinct
nonadjacent poles p,q, each adjacent to every cycle vertex. The poles
cannot be adjacent: B already has 3k edges on k+2 vertices, meeting
the planar bound 3(k+2)-6. The inherited embedding of B has triangular
faces, each with two cycle vertices and one pole.

There are no additional vertices of T. Otherwise choose a component
of the vertices lying inside one face of B. Its only possible
neighbors in B are the three boundary vertices of that face. Both
cycle boundary vertices already have their four neighbors in B and
cannot have an edge to it. The component therefore attaches only to
the pole, or is disconnected. Both alternatives contradict the
connectivity and no-cut-vertex properties of T. There are also no
additional edges between vertices of B, by the planar edge bound.
Thus U(T)=B.

Every orientation of this bipyramid is two-colorable: color p,q,v1
red and v2,...,vk blue. The red induced underlying graph is a path of
length two and the blue induced underlying graph is a path. Any
orientation of a forest is acyclic. This colors T, a contradiction.
Therefore no component of U(T)[L] is a cycle of length at least four.

## 7. An all-low triangle cannot separate the embedding

Let abc be an all-low triangle. If it separates, both open sides
contain vertices. On each side each of a,b,c must have a neighbor
there: otherwise removing the other two triangle vertices separates
that side from the missing terminal, contrary to 3-connectivity.

Each terminal has only two neighbors outside abc. It therefore has
exactly one on each side. On a chosen side, the triangular faces
incident with ab,bc,ca force these three respective neighbors to be
one common vertex p. The other side similarly has a common vertex q.

We now have the triangular bipyramid on {a,b,c,p,q}. Each of a,b,c
already has all four neighbors there. Any further vertex in one of
its faces could attach to the rest only through the pole, as in
Section 6, which is impossible. Thus T would be this five-vertex
bipyramid. But its poles have degree three, contrary to the minimum
degree four of T. This excludes a separating all-low triangle.
A triangle in a triangulation with an empty side is facial; the
all-low triangle components are therefore directed facial triangles.

## 8. Exact counting consequence

Let l=|L| and let p be the number of path components of U(T)[L],
counting isolated vertices as one-vertex paths. Triangle components
have as many edges as vertices; each path has one fewer edge.
Thus e(L)=l-p and e(L,H)=4l-2e(L)=2l+2p.

This cross-edge identity is stronger than just minimum degree four,
but does not by itself contradict the planar Euler identity in C09.
In particular degree-five vertices and forced boundary colorings
are not eliminated by it.

## 9. Source comparison and an optional criticality bridge

Primary source: J. Bang-Jensen, T. Bellitto, T. Schweser and M. Stiebitz,
Hajos and Ore Constructions for Digraphs, arXiv:1908.04096v1 (2019-08-12),
Proposition 13 (printed p.13) and Theorem 11 (printed p.12).
https://arxiv.org/abs/1908.04096
https://arxiv.org/pdf/1908.04096
The color-transfer principle is prior art. The source's full low-block
classification assumes all proper subdigraphs are colorable.

For comparison, that hypothesis can be obtained without imposing it
on T: choose an arc-minimal non-two-colorable spanning subdigraph D.
Every smaller-order subdigraph is colorable by minimum order, and every
proper spanning subdigraph is colorable by arc minimality. Also D has
dichromatic number three, since D-v can use two colors and v a third.
Each low vertex of T retains all incident arcs in D, as D still has
both semidegrees at least two. Hence T[L]=D[L], with L contained in
the low vertices of D. The source's classification is consistent
with the direct forbidden-triangle and diamond arguments above.
It is not required as an unproved premise of Sections 2-8.

All displayed transfers and planar arguments are explicit proof-draft
steps, not an enumeration or solver run. No novelty claim is made.
The source's diagram is not used to determine any orientation here.

## Checkpoint and remaining obstacle

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c10-low-vertex-transfers
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: determine the exact three-terminal coloring interface of a
facial triangle of low vertices, rather than assuming it is reducible.
Then connect local interfaces to degree-five configurations.
No SAT bound, Lean execution, verifier receipt or root closure is claimed.
