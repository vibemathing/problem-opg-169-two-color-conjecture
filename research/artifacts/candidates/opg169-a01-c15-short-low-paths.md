# C15: every low path has at most two vertices

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c15-short-low-paths
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 35d22b4c0c8365114fbe29b867b35a7a92ed3b40
Primary owner: math-proof.

## 1. Frozen scope and strip notation

Let T be the maximum-size representative among minimum-order counterexamples
from C09. It is a simple plane triangulation and is 3-connected. A low vertex
has degree four and indegree and outdegree two. C10 shows that low components
are paths or directed facial triangles.

Suppose v1,...,vk is a low path component, k>=2. C12 gives distinct high
vertices p,r,q,s in this cyclic order on the boundary of a disk. Put
u0=r, ui=vi for 1<=i<=k, and u(k+1)=s. The disk consists of the chain
u0,...,u(k+1) and its two cones from p and q. For every 0<=j<=k,
p uj u(j+1) and q uj u(j+1) are actual faces of T.

Let F=T-{v1,...,vk}. It is a proper induced planar orientation and has a
valid acyclic two-coloring. It retains all arcs among p,r,q,s, including
any exterior diagonal. The strip disk is an empty quadrilateral face in F.
No other adjacency to a low path vertex exists.

All uses of minimality below concern the full frozen class. Replacement
graphs need not be induced subgraphs, triangulated, or degree-four graphs.

## 2. Two elementary operations, with real-cycle semantics

Starting from ANY valid coloring of F, color vk,v(k-1),...,v2 in that order.
At each insertion, at most three neighbors are colored. One of the incoming
or outgoing sides contains at most one colored neighbor. A color absent
from that side is safe: a newly created monochromatic directed cycle
would have to enter and leave the inserted vertex in its own color.
Thus this procedure gives a valid coloring of T-v1 extending the given
coloring of F.

In any valid coloring of T-vi, neither color can be assigned to vi, since
that would color T. Each failure therefore supplies an actual monochromatic
cycle through vi, or equivalently a return path in T-vi between an
out-neighbor and an in-neighbor of that color. Because vi has exactly two
incoming and two outgoing neighbors, each of these neighbor pairs contains
one vertex of each color.

A hole at vi may be moved to an adjacent low vertex vj: erase the color
of vj and give that old color to vi. In the incoming or outgoing pair
containing vj, that color is now absent. Hence the transfer is safe.
This produces a valid coloring of T-vj without changing F. No direction
of the low-low edge is required.

## 3. Every exterior coloring separates the two poles

Assume a valid coloring of F gives p and q the same color A. Extend it to
T-v1 as above and write B for the other color. At the hole v1, p and q
cannot belong to the same incoming or outgoing pair, since that pair
must contain both colors. Therefore r and v2 have color B.

Move the hole successively to v2,...,vk. At each hole the two chain
neighbors must be B for the same reason. Induction shows that, in the
original coloring of T-v1, all v2,...,vk and both r,s have color B.
The transfers do not change either pole or any other vertex of F.

Return to that original coloring. Blocking color A at v1 yields a positive
A-colored directed path between p and q in F: none of the remaining low
vertices is A. Blocking B yields a directed path between r and v2.
In the B-colored graph the vertices v2,...,vk have only their chain
neighbors available, since both poles are A. A simple path from v2 to r
or from r to v2 must therefore traverse s, and it contains a B-colored
directed path between r and s wholly in F.

The resulting p-to-q and r-to-s underlying paths join alternating boundary
pairs in the disk complementary to the deleted strip. They cannot be
vertex-disjoint in a planar embedding. Their colors differ, so they ARE
vertex-disjoint. The A path cannot use r or s and the B path cannot use p
or q; no boundary-terminal intersection is being overlooked. Contradiction.

Consequently every valid coloring of F has color(p)!=color(q).

## 4. Hole transfers impose endpoint parity

Fix any valid coloring of F. Normalize color(p)=0 and color(q)=1.
In a valid coloring with hole vi, the two chain neighbors of vi have
different colors. Indeed, if the poles belong to the same in/out pair,
the other pair consists of the two chain neighbors and has both colors.
If they belong to different pairs, each chain neighbor has the color
opposite its paired pole, and the two resulting colors differ.

Start with any extension to T-v1. At the first hole r and v2 differ.
After transferring v2 to v1, the neighbors of the new hole v2 are v1,
carrying the ORIGINAL color of v2, and v3. Hence the original colors of
v2 and v3 differ. Repeat along the path. The final hole at vk compares
the original color of vk with color(s).

Thus r,v2,...,vk,s, viewed as an ordered list, has alternating colors.
This list has k edges, so
color(s) = color(r) xor (k mod 2).
This conclusion holds for every valid exterior coloring; it does not
assume that any boundary precoloring can be extended.

## 5. A single monochromatic chain edge is a decisive test

For a fixed normalized exterior coloring let A=color(r). By Section 4
the endpoint parity permits a coloring of the FULL chain with precisely
one monochromatic edge, chosen arbitrarily as uj u(j+1), 0<=j<=k.
All other chain edges are bichromatic. The color of this unique
monochromatic edge is A xor (j mod 2). Let h_j be the unique pole of
that color.

If the triangular face h_j uj u(j+1) were transitive, this would extend
the exterior coloring to T. Here is the full crossing-cycle audit.

Every low vertex not on the exceptional monochromatic edge has exactly
one same-colored neighbor, namely its matching pole. It cannot lie on
a monochromatic cycle. If 1<=j<=k-1, the two exceptional low vertices
form a triangle with h_j; this triangle attaches to the rest of their
color class only at h_j. The only possible new cycle is that triangle.

If j=0 or j=k, the exceptional triangle consists of one low vertex,
one endpoint terminal, and its matching pole. It meets F in the actual
boundary edge between the terminal and pole. Acyclic digraphs sharing
an arc glue acyclically when the colorings agree: a new directed
two-edge path opposite that arc would already be a directed triangle,
and a path following the arc cannot create a cycle absent from F.
Equivalently, this is the tournament-gluing lemma for a two-vertex
tournament. All other same-colored low vertices remain leaves.

These arguments retain every exterior arc and path. They do not replace
the exterior by a face-color condition or ignore a boundary diagonal.

Since T is not colorable, for EACH j the face h_j uj u(j+1) is directed.

## 6. A long strip has a unique normalized boundary coloring

Suppose k>=3. If two valid normalized colorings of F gave r different
colors, Section 5 would force BOTH faces p uj u(j+1) and q uj u(j+1)
to be directed for every j. In particular all four incident faces at
the internal low vertex v2 would be directed.

C14 excludes precisely this configuration at an internal low-path vertex.
Therefore color(r) is fixed once p=0,q=1 is fixed. Endpoint parity then
fixes color(s) as well. Every valid coloring of F has the SAME four-terminal
pattern up to exchanging the two colors. At least one exists by minimality.

This is rigidity of the actual exterior of a hypothetical counterexample.
It is not a claim that arbitrary planar four-terminal pieces are rigid.

## 7. Odd lengths at least three can be replaced by one interior vertex

Let k>=3 be odd. The fixed boundary pattern has p and q different and
r and s different. Its two same-colored pairs are disjoint boundary
edges of the quadrilateral p-r-q-s-p: either pr and qs, or ps and rq.

Delete the strip and add a single new interior vertex w adjacent to
all four boundary vertices. Keep all orientations in F unchanged.
Orient the four new spokes so that the triangles on those two
same-colored boundary edges are directed. This is consistent because
the two triangles use disjoint pairs of spokes; each pre-existing
boundary edge can be completed to a directed triangle in exactly one way.

Any valid coloring of the resulting graph would restrict to the fixed
boundary pattern in F. Either color for w would then complete its
corresponding monochromatic directed triangle. Thus the replacement
graph is not two-colorable. It is a finite simple planar orientation
on |V(T)|-k+1 < |V(T)| vertices, contrary to minimality.

The new vertex is distinct from every old vertex. No terminal
identification or reverse parallel arc is used.

## 8. Even lengths at least four can be replaced by two interior vertices

Let k>=4 be even. Then r and s have the same color as exactly one pole h.
Call the other pole t. The boundary consists of three vertices h,r,s
of one color and the single vertex t of the other.

Insert two new vertices w1,w2 in the empty quadrilateral disk as a
shorter two-cone strip with chain r,w1,w2,s and poles h,t. Orient its
new edges so that these three triangles are directed:
h r w1,   t w1 w2,   h w2 s.
The first and third triangles each use one fixed boundary edge, hr or hs,
and two new edges. The middle triangle uses three different new edges.
Their new edge sets are disjoint, so the orientations can be chosen
simultaneously, without changing any arc of F.

In any valid coloring, the first and third triangles force w1 and w2
to take the minority color of t. The middle triangle then becomes
monochromatic and directed. Hence the new simple planar orientation
is not colorable, although it has |V(T)|-k+2 < |V(T)| vertices.
This again contradicts vertex minimality.

## 9. Conclusion and scope

Every path component of the degree-four induced subgraph of the selected
triangulated representative has at most two vertices. Combining with C10:
its low components are single vertices, single edges, and directed
facial triangles.

This replaces C13's bound k<=2^1728 by k<=2 for this particular structural
class. It does not invalidate C13's general finite boundary-profile
semantics. The new replacements do NOT preserve all profiles for every
possible exterior. They need only remain uncolorable against the actual,
proved-rigid exterior F; that is sufficient for the minimum-order
contradiction.

If a,b,c count isolated low vertices, low edges, and low triangles,
then the low vertex count is a+2b+3c and the low-to-high edge count is
4a+6b+6c, by summing degree four and removing twice the low-low edges.
These counts alone give no discharging contradiction.

## 10. Attacks, dependencies, and checkpoint

The pole-equality contradiction uses real return paths and the planar
complementary disk, not neighbor colors alone. The single-edge test uses
a specific full coloring whose other low vertices are monochromatic
leaves. The endpoint cases retain and use the actual shared boundary arc.
The two replacements preserve the full exterior and its arcs; no
unconditional precoloring theorem is imported.

Dependencies: C09 minimal-order triangulated representative; C10 safe
hole transfers and low-component classification; C12 distinct four-terminal
strip disk; C14 internal-low-vertex face restriction; C11 edge tournament
gluing, which is reproved in the needed case above. The stronger degree
bound is a structural refinement, not a new admitted Obligation ID.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c15-short-low-paths
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: derive exact exterior-independent extension tables for the
remaining one- and two-vertex quadrilateral patches, then audit simultaneous
patch insertion into the high-vertex plane core. Keep degree-five vertices
and global monochromatic cycles in that core as open issues.
No mathematical program, graph enumeration, or verifier was executed.
