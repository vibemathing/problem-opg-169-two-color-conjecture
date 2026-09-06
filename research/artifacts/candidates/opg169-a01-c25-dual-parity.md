# C25: exact dual parity encoding and safe component deletion

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c25-dual-parity
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 9ab818c43e4dafc29bf5cbefc71cf3295b9054d3
Primary owner: math-proof.

## 1. Fixed core and meaning of the new variables

Use the connected simple plane core R of C16, whose faces are triangles
or quadrilaterals. The oriented edges and the actual labels and
orientations of all deleted low patches are fixed. For the low-edge
patches use their unique majority poles proved in C17.

Choose a subset Gamma of the UNDIRECTED edges of R. The intended
meaning is exactly the set of edges with equal-colored endpoints,
not a set of deleted vertices, a feedback vertex set, or a matching.
Write Gamma* for the corresponding edge-subgraph of the geometric dual.
Ignore isolated dual vertices when discussing its connected components.

We prove an exact encoding, rather than assume that C24's sufficient
simple dual path represents every coloring. No new admitted node is added.

## 2. The face-parity equations characterize all two-colorings

Let g_e=1 when e is in Gamma and g_e=0 otherwise. For each facial
boundary require
  sum_(e on boundary f) g_e = length(f) modulo 2.          (P)

Necessity: for any two-coloring, the number of changes of color along
a closed boundary is even. Its changes occur exactly at the edges
outside Gamma, so (P) follows.

For sufficiency put q_e=1-g_e. Equation (P) says that the sum of q
on each facial boundary is zero modulo two. The same holds on every
simple cycle, by summing the facial boundary equations inside its
Jordan disk: every internal edge occurs twice. Every closed walk
decomposes into simple cycles and traversals that cancel modulo two,
so the sum is zero on every closed walk.

Fix one vertex r and give it color zero. Give any vertex z the sum of q
along a walk from r to z, modulo two. It is independent of the walk
by the preceding paragraph. Across an edge e the endpoint colors
differ exactly when q_e=1. Thus Gamma is EXACTLY the set of
monochromatic edges. Connectivity makes the coloring unique up to
exchanging the two colors.

Equivalently (P) prescribes the odd-degree vertices of Gamma*:
they are precisely the triangular faces of R. This parity statement
does not include the orientation or the patch conditions.

For a fixed h-vertex connected core, there are 2^(h-1) such parity
edge sets, one per coloring up to global exchange. In C23/C24's
twelve-vertex residual case this is 2048 sets for EACH FIXED core.
This is a counting identity, not an executed enumeration, a count
of possible plane cores, or a finite bound on the root problem.

## 3. Global acyclicity has an exact edge-set interpretation

Recover a coloring from (P) as in Section 2. Its monochromatic arcs
are precisely the arcs whose underlying edges belong to Gamma.
Therefore it is a valid acyclic two-coloring of R if and only if
the oriented edge-subdigraph R[Gamma] has no directed cycle.       (A)

The notation R[Gamma] here means the spanning EDGE-subdigraph,
not a vertex-induced graph. Every connected component of its
underlying graph is monochromatic. Thus (A) handles all global
monochromatic cycles, not just triangles or facial cycles.

In particular, (A) is preserved when Gamma is replaced by a subset.
That monotonicity does NOT automatically preserve the patch conditions.

## 4. Complete local patch table expressed in Gamma*

For a quadrilateral f, equation (P) allows degrees 0,2,4 in Gamma*.

Degree0: all four boundary edges change color, so the boundary
alternates. Both wheel and low-edge strip patches extend.

Degree4: the four boundary vertices all have one color.
Both patch types extend: C16 covers the wheel and the equally
colored poles of the strip.

Degree2, selected boundary edges adjacent at a corner z:
the boundary has three equal-colored vertices centered at z,
and its opposite vertex is the singleton color.
A wheel always extends. A strip fails exactly when z is its
distinguished majority pole.

Degree2, selected boundary edges opposite:
the boundary has two adjacent vertices of each color.
A strip always extends. A wheel fails exactly when both cone
triangles over the two selected edges are directed.

For a triangular face equation (P) allows selected degree1 or3.
Degree1 is the nonconstant boundary pattern. Degree3 is all equal.
A marked low-triangle patch requires degree1, by C11/C16.
An unmarked triangular face imposes no extra patch constraint.
If that unmarked triangle is directed, its degree3 case is already
excluded by the global acyclicity condition (A).

Consequently Gamma corresponds to an extendible core coloring exactly
when (P), (A), and all of these local tests hold. Necessity follows by
restricting a full coloring of T and C16's exact forbidden patterns.
Sufficiency follows by recovering the core coloring and inserting
all patches sequentially against the actual colored exterior.
This is an equivalence for the fixed decorated core, not merely a
screening rule or a face-only coloring assertion.

## 5. Whole even components without odd faces can be discarded safely

Suppose Gamma satisfies the exact conditions of Section 4.
Let K be a nonempty connected component of Gamma* that contains
no triangular face. Its selected degrees are all even.

Remove EVERY selected dual edge of K, or equivalently remove
the corresponding primal edges from Gamma, obtaining Gamma'.
Face parity remains valid. At each quadrilateral vertex of K
ALL its selected incident edges belonged to K, so its selected
degree becomes zero. Its new boundary is alternating and passes
either patch type. At any other face its selected boundary-edge
set is unchanged; the boundary coloring may exchange both color
names, but the local tests are invariant under that exchange.
Triangular faces are unaffected.

Also Gamma' is a subset of Gamma, so its oriented primal
edge-subdigraph stays acyclic. Section 4 gives another full coloring
certificate. Hence those entire components can indeed be removed.

This proves one of the deletion possibilities raised in C24, rather
than presuming every closed dual structure is essential or removable.

If R has exactly two triangular faces, every selected component has
an even number of odd-degree vertices by the handshaking identity.
Thus the two triangles lie in the same selected component.
After removing all other components, a feasible certificate may be
assumed connected between those two faces.

When BOTH triangular faces are marked, their selected degrees are one.
All other used dual vertices have degree two or four. If t of them
have degree four, and u have degree two, then
  |E(Gamma*)|=u+2t+1,   |V(Gamma*)|=u+t+2,
  |E|-|V|+1=t.                                           (B)
Thus t counts the cycle rank of that connected certificate.
For t=0 it is a simple path and reduces exactly to C24's certificate.
For t>0 it may contain cycles coupled through degree-four faces.
Nothing here justifies restricting the search to t=0.

If an unmarked terminal triangle has selected degree three, it is
not a degree-one terminal for formula (B); that case is not silently
included in the marked-terminal calculation.

## 6. Why deleting an arbitrary dual cycle is a different operation

Here is an explicit local attack on the stronger rule
"deleting any dual cycle from a feasible Gamma keeps the patch tests true."

Take a four-cycle rim a,b,c,d with arcs
  b->a, b->c, d->c, d->a.
Inside put a wheel center v with spokes
  a->v, v->b, c->v, v->d.
Optionally close the sphere with a second wheel center w outside,
all four of its spokes pointing away from w. This yields the
ordinary simple octahedral underlying graph.

Color all rim vertices zero and both centers one. The rim is acyclic:
b,d are sources and a,c are sinks in its orientation. The centers are
nonadjacent. Thus the FULL graph has a valid coloring, and Gamma
contains all four rim edges.

The dual of the rim has two vertices and four parallel edges.
The selected dual edges corresponding to bc and da form a simple
two-edge dual cycle. Remove just that cycle, leaving Gamma'={ab,cd}.
The recovered rim coloring is a=b=zero, c=d=one, up to color exchange.
Face parity holds and the oriented primal Gamma' is still acyclic:
it is only the two disjoint arcs b->a and d->c.

Nevertheless neither color can be given to v. Color zero is blocked
by a->v->b->a; color one is blocked by c->v->d->c.
Exactly the wheel degree2-opposite forbidden case has been created.
The removed cycle was not an entire selected connected component:
its two face vertices also had the other selected edges.

This finite example concerns the general local deletion rule.
It has no odd core face and is not a minimum counterexample, nor
is it an obstruction to the root, since its full coloring was displayed.
It does not exclude a future cycle-removal theorem with additional,
proved hypotheses in the two-marked-triangle setting.

## 7. Verification scope and checkpoint

The exact table dependencies are C11, C16, C17, and C24.
Parity-to-color recovery and component deletion are proved directly.
Only the stated h=12 numerical specialization inherits the external
source premises of C23. This is not a new SAT, Hamiltonian, or kernel
certificate, and no mathematical program or graph list was executed.

The encoding provides a finite audit target for each frozen core:
recover the two colors, check the actual directed edge-subdigraph,
and check every marked face using the recorded patch orientation.
A solver error would not be a counterexample, and agreement on a
sample of parity sets would not establish their universal properties.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c25-dual-parity
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; arbitrary cycle deletion is
excluded as a general shortcut by Section 6, not the admitted route
next_obligation: obligation:opg169-strong-min-degree-three
next_action: in the two-marked-triangle case with only wheel faces,
study an edge-minimal feasible parity certificate. Determine which
faces of its selected dual subgraph permit monotone deletion, and
whether its cyclic blocks have a forced chain structure. Do not
assume that acyclicity alone protects the local patch tests.
