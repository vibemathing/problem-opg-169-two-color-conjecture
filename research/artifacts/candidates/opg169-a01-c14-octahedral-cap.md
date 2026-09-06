# C14: four directed faces force an octahedral cap

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c14-octahedral-cap
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 453fd401691fada49dbb117a557372f5e8b893c8
Primary owner: math-proof.

## 1. Scope

Let T be the selected triangulated minimum-order counterexample of C09.
This is an existential secondary choice if the root has any counterexample.
It does not assert that every minimum-order counterexample is 3-connected.

We use the already explicit same-side folding lemma: if a vertex has
exactly two in-neighbors, deleting it leaves a directed two-edge path
between those neighbors in one direction; the same holds for two
out-neighbors. The witnesses are in T-v. A direct neighbor-neighbor
arc is not a substitute for a two-edge path.

## 2. Four directed incident faces force a common external neighbor

Suppose a degree-four vertex v has all four incident triangular faces
directed. Its incident arcs must alternate in and out. Label its
cyclic neighbors a,b,c,d so that
a->v, v->b, c->v, v->d.
The four facial cycles then force
b->a, b->c, d->c, d->a.

Folding the pair of in-neighbors gives a directed two-edge path between
a and c in T-v. Its internal vertex is neither b nor d: neither a
nor c has an outgoing arc to b or d. Call its internal vertex w.

Folding the out-neighbor pair gives a directed two-edge path between
b and d. Its internal vertex is neither a nor c, because neither a
nor c has an outgoing arc to b or d. Call it z.

The star of v consists of its four actual triangular faces and is a
disk with boundary a-b-c-d-a. Both paths lie in the complementary
disk. They connect alternating pairs of distinct boundary vertices.
They therefore intersect. Their endpoints are all distinct, and each
path has just one internal vertex outside the four boundary vertices.
Their intersection forces w=z.

Consequently T contains an octahedral underlying subgraph B: its rim
is a-b-c-d-a, and its poles are v,w. The pole edge vw is absent because
v already has degree four. No rim diagonal can be present either:
B has twelve edges on six vertices and already attains the simple
planar edge bound.

This is a genuine consequence of planar intersection of the folding
witnesses. It does not infer an intersection merely from colored
neighbor existence or from a crossing in an arbitrary drawing.

## 3. The external cap must contain a separating triangle

The four faces of B incident with v are already faces of T. Any
additional vertices of T can occur only in the four triangles of B
incident with w. If there are no additional vertices, the planar
edge bound gives T=B, which is two-colorable for every orientation:
color v,w,a red and b,c,d blue. Each induced underlying graph is a path.

Therefore at least one triangle wxy, for consecutive rim vertices
x,y, contains an additional vertex on its w-side. Its other side
contains v and the rest of the octahedron, so wxy is a separating
triangle of T.

Moreover, that occupied triangle cannot have a low rim vertex.
Such a degree-four vertex already has all its neighbors in B.
A component inside the triangle could then attach to B through at
most its other two boundary vertices. Removing those two would
disconnect the component from the remaining low boundary vertex,
contrary to 3-connectivity of T.

Thus an occupied cap face has two high rim vertices. This condition
locates the separator more precisely; it does not remove all
separating triangles from the chosen triangulation.

## 4. Internal vertices of low paths have a non-directed incident face

Suppose v is internal to a path component of the degree-four induced
subgraph. Its two low neighbors are nonadjacent, so they occupy opposite
positions in the four-position link. Every consecutive pair of rim
vertices therefore contains a low vertex.

If all four faces at v were directed, Section 3 would require an
occupied cap face whose two rim vertices are high. No such pair exists.
This is impossible. Hence at least one of the four incident faces
is not directed.

C09 already supplies two directed incident facial triangles. Thus an
internal low-path vertex has either two or three directed incident
faces, never four. For a cyclic IIOO arc pattern only the two changes
between in and out can support a directed face. The extra restriction
is useful in the alternating IOIO pattern, where four directed faces
were locally possible before applying the folding and planar arguments.

We do not infer that the entire low path is reducible. Its exterior
still enters through the exact four-terminal profile in C13.

## 5. A global degree-five exclusion from a matched source theorem

Define M(D)=max_v min(d+(v),d-(v)). Picasarri-Arrieta's Corollary 8
(arXiv:2301.04881v2, 2023-05-25, printed p.3) gives
dichromatic_number(D)<=M(D) for an oriented graph with M(D)>=2.
This is a source-reuse claim, not a new proof or a verifier receipt.
https://arxiv.org/abs/2301.04881
https://arxiv.org/pdf/2301.04881v2

It covers every orientation with maximum underlying degree at most
five: M<=2, and if M<=1, repeated deletion and the missing-color
extension give two-colorability directly. Thus a minimum counterexample
must have a vertex with both semidegrees at least three.

The maximum over vertices is essential. Euler gives the existence of
a vertex of underlying degree at most five, not M<=2 for the whole
graph. The cited theorem also does not promise extension of a fixed
boundary coloring. Neither stronger assertion is used.

## 6. Attacks, attribution and verification scope

The input and output folding paths may have either direction; the
planar intersection argument uses only their underlying paths.
Each path's internal vertex is explicitly excluded from the other
pair of boundary terminals before intersection is invoked.
An unspecified longer path would not force a single common neighbor.

A nonfacial triangle cannot be substituted for the four actual faces
around v. Nor can one assume that an arbitrary minimum counterexample
has the triangulated embedding supplied by the secondary choice.

The cap proof is derived from C09 and C10/C12 and requires no additional
external classification theorem. The source statement in Section 5
was read in the primary abstract and parsed PDF. Screenshot requests
for its proof pages failed; no diagram reading or proof-assistant
replay of that paper is claimed. The source theorem's application is
kept separate from the direct cap argument.

The current forbidden local forms include the low transitive triangle,
the low diamond, low cycles of length at least four, and the four-
directed-face internal low-path star. They do not yet supply an
unavoidable-configuration or complete discharging contradiction.

## Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c14-octahedral-cap
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: reduce the selected graph to its high-vertex plane core
with triangular and quadrilateral patch faces, preserving exact
reachability profiles. Determine whether the resulting planar
boundary constraints must have a compatible coloring; do not assume
the all-equal exterior of C11 is impossible.
No SAT bound or mathematical execution is added by this packet.
