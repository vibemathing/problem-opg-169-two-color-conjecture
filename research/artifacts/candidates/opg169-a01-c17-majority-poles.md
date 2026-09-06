# C17: rigid low-edge exteriors and majority-pole constraints

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c17-majority-poles
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 146f08c7f05380508c28dd2c64a8310075fe14a5
Primary owner: math-proof.

## 1. Scope and notation

Let T be C09's triangulated maximum-size representative of minimum
counterexample order. For a component {x,y} of the degree-four induced
subgraph, use C12's strip notation: boundary p,r,q,s in cyclic order,
chain r,x,y,s, with both low vertices joined to both poles p,q.
The six cone triangles are actual faces. The four boundary vertices
are distinct and high. Write F=T-{x,y}.

By minimum order F has a valid two-coloring. No such coloring extends
to T. C16 therefore says that each valid coloring gives r,s and one
pole h the same color, gives the other pole t the opposite color, and
has all three triangles h r x, t x y, h y s directed.

A pole is called heavy here when BOTH its indegree and outdegree in T
are at least three. This local definition is not a statement that
every vertex of degree at least six is heavy.

## 2. Both pole choices cannot be forbidden

Suppose both potential three-and-one boundary patterns are forbidden
by the patch orientation. Then all six cone triangles are directed.
Reverse every arc if necessary to arrange x->y.

The directed middle triangles force y->p->x and y->q->x.
The directed triangles on rx then force x->r->p and r->q.
The directed triangles on ys force p->s->y and q->s.
In particular both p and q point into x and into s.

Apply C14's four-directed-face argument at x, whose cyclic rim is
p,r,q,y. Its two incoming-neighbor folding path joins p,q; its
outgoing-neighbor folding path joins r,y. C14 proves that these
two directed two-edge paths have the SAME internal vertex w,
outside {x,p,r,q,y}.

Since w is adjacent to y and y has exactly the four neighbors
{x,p,q,s}, necessarily w=s. But s cannot be the internal vertex of
a directed path p->s->q or q->s->p: the displayed facial directions
are p->s and q->s. This contradiction excludes all six directed faces.

The argument uses directed two-edge folding witnesses, not merely
a common underlying neighbor. The orientation at the common vertex
is essential.

Since some valid coloring of F exists and none extends, at least
one of the two patterns is forbidden. Consequently EXACTLY one is
forbidden. There is one distinguished majority pole h and one
minority pole t, fixed by T, such that every valid coloring of F
satisfies
  color(h)=color(r)=color(s)!=color(t).
These equalities are up to the unavoidable global exchange of colors.

This strengthens C15's boundary rigidity to the remaining length-two
low component. It does not assert rigidity of an arbitrary planar
four-terminal graph.

## 3. The majority pole has both semidegrees at least three

Fix a valid coloring of F and denote its majority color by A and
minority color by B. The directed triangles h r x and h y s give h
one incoming and one outgoing edge in each of the disjoint pairs
{r,x} and {y,s}. Thus among {r,s,x,y}, h already has two incoming
and two outgoing neighbors.

Try recoloring h from A to B while leaving every other vertex of F
unchanged. If this were a valid coloring of F, it would give both
poles the same color and hence would extend across the strip by C16.
That would color T, a contradiction.

Hence recoloring h creates a real B-colored directed cycle in F,
necessarily through h. Take its predecessor i and successor o.
They are distinct in an orientation and both had color B before
recoloring. Neither is r or s, since those have color A. Neither
is x or y, which are absent from F.

These supply a third incoming and third outgoing neighbor of h,
outside the four already counted. Therefore
  d_T^-(h)>=3 and d_T^+(h)>=3.

In particular a degree-five vertex cannot be the majority pole of
a low-edge patch in a minimum counterexample. This is a local
necessary condition proved by a genuine recoloring failure; it does
not follow just by applying a global maximum-semidegree theorem.

## 4. Every boundary flip is blocked in the exterior

The unique boundary partition from Section 2 changes if exactly one
of h,r,s,t is recolored. Thus no single boundary-vertex flip is valid
in F. For each vertex z of that boundary and each valid coloring of F,
there must be a monochromatic directed cycle through z after its flip.
The predecessor and successor have the new color already in F.

This supplies real exterior return paths for later recoloring arguments.
It does not make the paths for different flips vertex-disjoint: they
may have the same color or intersect, and no disjointness is assumed.

A related cofacial identification consequence is also available:
for each u in {h,r,s}, F contains a directed two-edge path between u
and t in at least one direction. Suppose no such path existed.
The pair is cofacial in the empty strip quadrilateral of F. Identify
u and t across this face (contract their existing edge if adjacent,
or insert and contract an undirected diagonal if nonadjacent).
Remove a resulting loop, if any, and merge same-direction duplicates.

No digon can appear, because an opposite pair at the new vertex would
be exactly an excluded directed u-to-t or t-to-u two-edge path.
The quotient is a smaller simple planar orientation and hence has a
valid coloring by global minimum order. Pull it back to F. Any simple
directed cycle of F would map to a positive closed walk in the quotient:
only u,t were identified and at most their one edge could disappear.
Since an original directed cycle has length at least three, some arc
remains. Thus a monochromatic cycle would contradict the quotient
coloring. The pullback gives u,t the same color, contrary to rigidity.

The three two-edge paths need not use different internal vertices.
This conclusion refines the former two-cut witness principle but
does not by itself eliminate all frozen boundary patterns.

## 5. The other diagonal obstructs a directed chain through the majority pole

Suppose r->h->s. If rs is absent from F, draw the new arc s->r
inside its empty quadrilateral face. The new graph is a simple planar
orientation with |V(T)|-2 vertices. Every valid coloring would restrict
to a valid coloring of F, in which r,h,s have one color by Section 2.
The new triangle r->h->s->r is then monochromatic. Thus the new graph
is not colorable, contradicting minimum order.

Consequently rs must already exist. Its orientation cannot be s->r,
since F itself has a valid coloring with r,h,s monochromatic.
It must be r->s. The reversed directed chain s->h->r analogously
forces the existing arc s->r.

Equivalently, if the endpoints r,s are nonadjacent, h must be a source
or a sink with respect to its two boundary edges hr,hs.

We do not reverse an existing exterior arc. Reversing one might create
new exterior colorings, so the previously proved rigidity could not
be assumed after that operation. The absent-edge hypothesis is not
dispensable in the insertion contradiction.

## 6. A direct small-core exclusion without enumeration

Let R=T[H] be C16's high-vertex plane core. It is simple, 2-connected,
has at least three vertices, and every face has length three or four.
The marked-face tables of C16 apply. We prove |H|>=5 by hand.

If |H|=3, R is a triangle. Give two vertices color A and one color B.
Both classes are acyclic and every marked triangular face is nonconstant.
There are no quadrilateral faces. C16 then colors all of T, impossible.

Suppose |H|=4. A simple 2-connected graph on four vertices has between
four and six edges. With four edges it is C4. Give its vertices
alternating colors. On both faces every one-vertex patch is extendible,
and every two-vertex strip has equally colored opposite poles and is
extendible; either choice of opposite pole pair works.

With five edges the graph is K4 minus one edge. Its plane embedding
has two triangular faces and one quadrilateral face. Color the four
vertices alternately around the quadrilateral. Every color class
has at most two vertices and hence no directed cycle in an orientation.
Both triangular faces are nonconstant, and the quadrilateral passes
both possible patch tables.

With six edges R=K4 and all faces are triangles. Any two-and-two
vertex coloring is acyclic and makes every face nonconstant.

Thus in all four-vertex cases the constrained core coloring exists.
C16 extends it to T, a contradiction. We conclude |H|>=5.
No solver call, generated list of graphs, or empirical absence result
was used in this classification.

C16 bounds total order by 7|H|-12, but this is not an absolute bound.
The separately cited published finite-order result, if imported with
its full statement and certificate scope, would give further numerical
consequences; no such replay is asserted here.

## 7. Limitations and checkpoint

The local constraints now distinguish the majority pole of a low-edge
face from its other high boundary vertices. They do not exclude every
low edge, force every degree-five vertex to be reducible, or ensure a
global compatible coloring of the high core.

The original two-cut issue remains separate: C09 uses a maximum-size
minimum-order representative to obtain 3-connectivity. None of C15-C17
claims that every vertex-minimum counterexample has no two-cut.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c17-majority-poles
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: combine majority-pole and low-triangle heavy-vertex contacts
into a simultaneous charge/constraint argument. Account for isolated
low vertices and degree-five vertices; do not presume the exterior
return paths for different flips are disjoint.
No mathematical program, SAT certificate, kernel replay, or admission
was produced in this proof cycle.
