# Candidate C04: shortcut fans and forced directed triangles

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c04-shortcut-fan
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 360814c61e86d5d4b0c74003e3567730510bc67d

## Scope and exact claim

Keep global vertex-number minimality in the FULL frozen class of finite
simple planar orientations. In such a hypothetical counterexample:

(a) if d-(v)=2, every incoming arc of v lies on a directed triangle;
(b) if d+(v)=2, every outgoing arc of v lies on a directed triangle;
(c) every underlying degree-four vertex lies on two directed triangles
    whose only common vertex is v;
(d) there are at least four distinct directed triangles in total.

These are additional necessary conditions, not a replacement of the
admitted target and not a proof of the root. The elementary axioms used
are finite-digraph-basic, planar-graph-basic and finite-combinatorics.
Planar edge contraction and the simple-planar edge bound are used
explicitly, not a closure assumption about a digirth-restricted subclass.

## C04.1: safe incoming shortcut-fan reduction

Let N-(v)={u,u'}, with u!=u', and suppose w->u is absent for every
w in N+(v). Define H by deleting v and, for each w in N+(v), adding
u->w if it is not already present.

H is a finite simple orientation. There is no new loop because u is
not an out-neighbor of v: otherwise u->v and v->u would form a digon
in G. No new arc is opposite to an existing arc, precisely by the
assumption that w->u is absent. Existing u->w arcs are kept just once,
and the distinct out-neighbors give distinct new endpoint pairs.

For planarity, contract the undirected edge uv in U(G), label its merged
vertex u, and suppress loops and duplicate undirected edges. Every
edge of U(H) is in this planar contraction: old edges of U(G-v) survive,
and each needed uw comes from vw. Some other contraction edges, such as
uu' when it was not already in G-v, are simply not selected for H.
Thus U(H) is a subgraph of a planar graph and is planar. This argument
does NOT claim that an unrestricted directed contraction preserves
orientations; orientation conflicts were audited separately above.

H has one fewer vertex than G, so global vertex minimality supplies
a valid acyclic 2-coloring c of H. Its restriction to G-v is valid since
deleting added arcs cannot create a directed cycle.

If c(u)=c(u'), give v the other color. It has no same-colored in-neighbor
and cannot lie on a new monochromatic directed cycle.

If c(u)!=c(u'), give v color c(u). A new monochromatic directed cycle
would enter v from u, the UNIQUE in-neighbor of that color. Let its
out-neighbor be w. Removing v from this simple cycle gives a c(u)-colored
path w->...->u in G-v. H contains u->w and therefore contains a
monochromatic directed cycle, contradicting the choice of c.

In both cases c extends, contrary to G being a counterexample. Therefore
the assumed absence of all w->u arcs is impossible. For each incoming
arc u->v some w satisfies v->w->u, giving the required directed triangle.

## C04.2: outgoing version and degree-four matching

Reverse every arc. This operation preserves the frozen class, directed
acyclic colorability, and global minimum vertex count. Applying C04.1
to the reversed orientation proves (b).

At degree four, C02 implies d-=d+=2. Let I={u1,u2} and O={w1,w2}.
Form an auxiliary bipartite graph with edge ui-wj exactly when wj->ui
is an arc of G. Statements (a) and (b) say no vertex of this bipartite
graph is isolated. It has a perfect matching, as follows without any
unmentioned matching theorem. If u1 has only neighbor w1, then w2 must
be adjacent to u2, so choose those two edges. If u1 has both neighbors,
choose any neighbor for u2 and give u1 the other one.

The two matched edges complete u1->v->w_j->u1 and
u2->v->w_k->u2 with j!=k. All four neighbors are distinct by the
orientation assumption, so these triangles meet only at v.
They need not be facial triangles. In an IIOO plane rotation C03
forces the nonalternating matching; in an IOIO rotation either listed
nonalternating matching is possible.

For degree five, only one semidegree equals 2. The corresponding two
arcs lie on distinct triangles, but these triangles may share another
vertex. A row-nonempty 2-by-3 incidence matrix need not have a matching
covering its two rows: both rows may have the same sole neighbor.
No vertex-disjoint-triangle claim at degree five is made.

## C04.3: a global counting consequence and its exact limitation

Let n4 and n5 count the vertices of underlying degree 4 and 5.
By C02 all other vertices have degree at least 6. As G is simple planar
with at least three vertices, m<=3n-6, whence
sum_v (6-deg_U(v)) = 6n-2m >= 12.
Terms at degree at least 6 are nonpositive, so
2*n4+n5 >= 12 and n4+n5 >= 6.

Every vertex of degree 4 or 5 has one semidegree exactly 2. The two arcs
on that side lie on two distinct directed triangles by (a) or (b).
If T is the number of distinct directed triangles, their incidences
with these low-degree vertices therefore satisfy
3*T >= 2*(n4+n5) >= 12.
Consequently T>=4.

This counting bound and the local conditions are jointly realizable
in a colorable graph. In the C02 oriented octahedron, the four directed
triangles are v-a-b-v, v-c-d-v, w-b-c-w and w-d-a-w.
To audit completeness, every underlying triangle chooses one vertex
from each of {v,w}, {a,c}, {b,d}. The other four possibilities are
v-b-c, v-d-a, w-a-b and w-c-d, and their orientations are transitive
by the twelve-arc list in C02. Thus exactly four are directed.
All six vertices have degree 4 and each lies on exactly two of these
directed triangles; the displayed C02 coloring still colors the graph.
Thus these local conditions and inequalities alone cannot supply a
contradiction. Global minimality or further structure must do more work.

## Assumption attacks and scope separation

The shortcut graph H may have new directed triangles. It is admissible
because minimality is over ALL planar orientations. This proof must not
be reused by asserting that H stays in a digirth-at-least-four class:
that claim is false even for a small planar input. Take the directed
4-cycle u->v->w->z->u and add the single arc u'->v from a fifth vertex.
There is no directed triangle and d-(v)=2, but the shortcut through u
creates u->w->z->u in H. This input is only a class-preservation test,
not a counterexample to the coloring conjecture. Accordingly T>=4 here
is a statement about a globally vertex-minimum counterexample, not
a theorem that every planar orientation with fewer triangles is
2-colorable.

If an existing reverse arc w->u is ignored, adding u->w creates a
digon and leaves the frozen orientation class. Keeping parallel arcs
instead of suppressing duplicates also changes the declared simple
model. Neither operation is used. The coloring of H must be restricted
before restoring v; no added arc is silently treated as an arc of G.

The reduction needs more than closure under vertex deletion. C01's
extension to arbitrary vertex-hereditary classes is not imported into
C04. Planarity is justified separately through an explicit minor.

## Dependency, attribution, and checkpoint

C04.1 is a direct construction under the frozen assumptions. C04.2 uses
C04.1, arc reversal and C02. C04.3 uses C04.2 and the planar edge bound.
C03 only refines the cyclic order after existence of the two triangles;
C04.1 and the counting argument do not depend on that topological lemma.
The original target is already covered by C01, without these refinements.

The C01 source note supplies dichromatic terminology and prior-art
context. A bounded source search did not identify an exact locked
reference for this shortcut formulation; no novelty claim follows.
All constructions and case arguments needed here are supplied above.
No mathematical program or prover was run.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c04-shortcut-fan
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: derive a complete two-terminal color/reachability gluing
interface for two-vertex separators and audit its minimality consequences.
No verifier receipt, EvidenceLink or Result is created by this draft.
