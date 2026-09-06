# C12: high-degree contacts and four-terminal low-path disks

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c12-low-patch-contacts
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: d39b0aa6fe0f55197dd93687c1b32024dae86d4b
Primary owner: math-proof.

## 1. Scope and notation

T is the chosen maximum-size, minimum-order counterexample from C09.
It is an orientation of a finite simple 3-connected plane triangulation.
L consists of its degree-four vertices. By C10, U(T)[L] consists of
paths and directed facial triangles. A high vertex is any vertex
outside L. These are conditional proof-draft premises; the admitted
target and root are not changed or declared closed.

## 2. Every outer vertex of a low triangular patch has both semidegrees at least three

Use C11's octahedral patch Q with inner triangle abc and outer triangle
xyz. Its corner triangles axz, bxy, cyz are directed, while xyz is
transitive. Let F=T-{a,b,c}. Every valid coloring of F makes xyz
monochromatic, and at least one such coloring exists.

At x the corner triangles bxy and axz use two disjoint pairs of
incident edges, namely (xy,xb) and (xz,xa). Each directed triangle
provides one incoming and one outgoing edge at x. Thus within Q,
d+(x)=d-(x)=2. The same holds at y and z.

Take a valid coloring of F with xyz red. Recolor only x blue.
This cannot be a valid coloring of F because its boundary would no
longer be monochromatic. Therefore a new monochromatic directed cycle
appears. It must contain x, and its color must be blue: the old red
class merely lost a vertex, while the old blue class was acyclic.
The predecessor and successor of x on this cycle are distinct blue
in- and out-neighbors. They belong to F and are not y or z, which are
red. They are consequently outside Q. Adding these two witnesses to
the two incoming and two outgoing edges already in Q gives
d_T^+(x)>=3 and d_T^-(x)>=3.

Apply the same argument separately to y and z, using the same starting
coloring if desired. Hence all three outer vertices have degree at
least six; no degree-five vertex is adjacent to a low triangle component.
The three recoloring failures need not be witnessed by disjoint paths.
No such disjointness is claimed or used.

## 3. A degree-six vertex cannot meet two low triangle components

Suppose a degree-six vertex w is an outer vertex of two distinct low
triangle patches. Each patch gives exactly two low neighbors of w,
consecutive in the cyclic link because they are adjacent in a face.
The two low pairs belong to different components of U(T)[L].
They cannot be consecutive to each other: the link edge between
consecutive low vertices would join those components.

There must therefore be at least one high neighbor in each of the two
gaps between the low pairs. The six positions at w leave exactly two
such high neighbors, say p and q. The two outer companions of w for
each octahedral patch are its high neighbors immediately before and
after that patch's low pair. Thus both patches have boundary wpq.

The two patches occupy the two complementary sectors between wp and wq
at w, so they fill opposite sides of the same triangle wpq. Each
patch's seven interior faces are actual faces of T by C11. Their union
therefore fills the sphere, and T consists of these two octahedra glued
on their common outer triangle.

Give wpq any nonmonochromatic two-coloring. C11 supplies an acyclic
extension to each octahedron by two underlying paths. Its tournament
gluing lemma then gives an acyclic two-coloring of T, a contradiction.

Thus a degree-six vertex is incident with at most one low triangle
component. Together with Section 2, degree five has no such incidence.
These incidence restrictions alone are not a discharging contradiction.

## 4. The constant pair of poles along a low path

Let v1,...,vk be a path component of U(T)[L], with k>=2.
For an internal vi, the two low neighbors vi-1 and vi+1 are not
adjacent in T, since they belong to the same induced path component.
They cannot be consecutive in the four-position link of vi.
They therefore alternate with vi's other two neighbors.

The faces on the two sides of each edge vi vi+1 have third vertices
equal to these two other neighbors. Across successive edges the pair
is unchanged. Thus every path vertex has the same two high neighbors
p and q. For k=2, simply define p and q as the two third vertices of
the faces incident with v1v2. They are distinct; neither is low,
otherwise the path would belong to a low triangle rather than a path.

Let r be the remaining neighbor of v1 and s that of vk. They are high,
distinct from p,q, and outside the low path. The endpoint links force
edges pr,qr,ps,qs. More precisely, with
u0=r, u1=v1, ..., uk=vk, uk+1=s,
each triple p ui ui+1 and q ui ui+1 is a face of T.

The poles are distinct, and neither endpoint terminal lies on the path.
It remains to exclude r=s; this is not assumed silently.

## 5. Coincident end terminals would give a colorable bipyramid

Suppose r=s=w. The cycle w,v1,...,vk,w and the poles p,q form a
bipyramid B. This is a simple maximal planar graph: on k+3 vertices
it has 3(k+3)-6 edges. In particular pq cannot also be an edge.

Every face of the inherited embedding of B contains at least one of
v1,...,vk. Those low vertices already have all four neighbors in B.
An additional vertex of T would lie in a face of B. A connected
component of the vertices inside that face could attach to B only at
the other two face vertices, or fewer. Deleting those at most two
vertices would disconnect it from the low boundary vertex still in B.
This contradicts 3-connectivity of T. Thus no extra vertices exist.
The planar edge bound also forbids extra edges, so T=B.

Every orientation of a bipyramid is acyclically two-colorable:
color both poles and one rim vertex red, and the remaining rim
vertices blue. Each color induces an underlying path. This contradicts
the counterexample premise. Therefore r and s are distinct.

## 6. The exact quadrilateral disk

We have four distinct high boundary vertices p,r,q,s, in cyclic order.
The union of the faces listed in Section 4 is a triangulated disk:
it is the union of two cones, from p and q, over the simple chain
r,v1,...,vk,s. The two cones are glued along that chain.
Its boundary is the cycle p-r-q-s-p, and its interior vertices are
exactly the low path component.

Every arc incident with an interior vertex is an arc of this disk.
Boundary diagonals, if present elsewhere in T, belong to the exterior
and are not invented as interior edges. In particular, no assumption
about the presence or orientation of pq or rs is used here.

This description exposes a four-terminal interface whose boundary size
is independent of k. Shortening the interior chain would preserve its
underlying disk embedding, but preservation of acyclic two-colorability
requires the actual monochromatic-reachability profile, not merely
the four boundary colors. That profile is the next proof obligation.

## 7. Attacks and dependencies

Section 2 needs the all-equal conclusion for EVERY valid exterior
coloring, not just one exhibited coloring. It obtains real cycles
from failed single-vertex recoloring, rather than treating neighbor
colors as sufficient. The in/out witnesses are distinct by the
orientation assumption and are outside the six-vertex patch.

Section 3 uses distinct low components, not two faces of one component.
The two complementary sectors at w are essential to the sphere-filling
argument. It does not exclude two patches at an arbitrarily high-degree
vertex, where more boundary positions are available.

Sections 4-6 use the induced low-path structure, exact degree four,
actual triangular faces, and 3-connectivity. They do not identify
vertices without checking orientation conflicts. The bipyramid
coloring is an orientation-independent forest partition.

Direct sources are the frozen contract and the C09-C11 proof drafts.
No new external theorem is required for these implications.
No theorem-prover, SAT solver or finite graph enumerator was executed.

## Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c12-low-patch-contacts
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: prove an exact finite boundary-state gluing and replacement
lemma for these four-terminal disks, then use repeated prefix profiles
to bound low-path lengths. Do not replace an unknown exterior by an
unproved universal precoloring extension assertion.
