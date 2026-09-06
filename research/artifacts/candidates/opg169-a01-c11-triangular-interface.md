# C11: exact boundary behavior of an all-low triangular patch

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c11-triangular-interface
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 8689bd5701f791cb2e3bada7e85c23e49bf4a8d9
Primary owner: math-proof.

## 1. Scope and forced geometry

Use the selected triangulated minimum-order counterexample T of C09
and the degree-four classification of C10. Suppose abc is a component
of its low-vertex subgraph. It is a directed facial triangle, and
each of a,b,c has exactly two additional neighbors.

Let the faces on the other sides of ab,bc,ca have third vertices
x,y,z respectively. These are outside abc and pairwise distinct.
For example, if x=y, the cyclic four-neighbor link of b would contain
the three-cycle a,c,x: its edges correspond to faces bac, bax, bcx.
A four-cycle link cannot contain that three-cycle. The other two
possible coincidences are excluded in the same way.

Thus the external neighbors of a are x,z, those of b are x,y, and
those of c are y,z. Their four-position links force the additional
faces axz, bxy, cyz. In particular xyz is a triangle.

Let Q be the subdigraph on these six vertices. Its underlying graph
is the octahedron, with nonadjacent pairs (a,y),(b,z),(c,x).
All edges involving a,b,c belong to Q. Put F=T-{a,b,c}. Then
T=F union Q, and the intersection is precisely the tournament on xyz.
The seven faces involving a,b,c form a triangular disk with boundary
xyz. This boundary is a face in F. Each of x,y,z has degree at least
five in T, since a fourth low vertex would create an all-low diamond.

No direction of an outer or corner edge has been inferred solely from
the existence of a known directed inner face.

## 2. Tournament gluing, with all crossing cycles audited

If two acyclic colored digraphs intersect in a tournament K and agree
on its vertex colors, their union is acyclic in each color.
Here is a proof for the needed case.

Fix a color. The same-colored vertices of K form an acyclic tournament,
so its arcs give a strict linear order. Any positive monochromatic
path in either piece between distinct such boundary vertices must
follow this order: a backward path together with the forward direct
arc would form a monochromatic closed walk and hence a cycle in that
piece. A positive path returning to the same boundary vertex is
already forbidden by the piece's validity.

A monochromatic cycle crossing pieces splits at boundary visits into
positive paths. Every segment between different boundary vertices
strictly advances in the same linear order. The segments cannot return
to their starting vertex. A cycle using no boundary vertex belongs to
one piece. This proves the gluing assertion.

The actual terminal arcs are retained in both pieces. This argument
does not invoke any precoloring extension conjecture.

## 3. Every nonmonochromatic outer precoloring extends

This statement holds for EVERY orientation of the octahedral graph Q,
not just the orientations forced in a hypothetical counterexample.
By exchanging the color names and cyclically relabelling, a prescribed
nonmonochromatic outer coloring may be written
color(x)=color(y)=red and color(z)=blue.

Set color(a)=red and color(b)=color(c)=blue. The red induced underlying
subgraph on {x,y,a} has just edges xy and xa. The blue induced
underlying subgraph on {z,b,c} has just edges zc and bc. Both are paths.
Therefore their orientations are acyclic, regardless of arc directions.

If F had any valid coloring with xyz nonmonochromatic, this explicit
extension in Q and Section 2 would give a valid coloring of T.
Consequently EVERY valid coloring of F makes x,y,z the same color.
At least one such coloring exists because F has fewer vertices than T.

It follows that xyz is transitive: a directed outer triangle would
forbid the monochromatic coloring just deduced.

## 4. The three corner triangles must also be directed

Fix a valid coloring of F and call its common boundary color red.
Suppose, for example, axz is transitive. Color a red and b,c blue.
The red part of Q is the union of the transitive tournament xyz and
the transitive tournament axz, agreeing on their common edge xz.
It is acyclic by Section 2. The blue part has only the single edge bc.
Another application of Section 2 then glues this coloring to F,
contradicting T's noncolorability.

Thus axz is directed. The same proof applies to bxy and cyz.
Together with the directed inner triangle abc, this gives all four
directed triangles needed for the precise boundary obstruction below.
This direction conclusion was proved by extension, not by choosing
a particular pair from the earlier facial-triangle existence lemma.

## 5. Complete boundary table of the forced patch

For a Q with directed triangles abc, axz, bxy, cyz and transitive xyz:

- The six labeled boundary colorings using both colors all extend,
  by the two induced paths in Section 3.
- The two monochromatic boundary colorings do not extend. If xyz
  is red, the three directed corners force a,b,c all blue, and then
  the directed triangle abc is monochromatic. Interchanging the
  colors gives the other obstruction.

Thus the exact extendible boundary relation of Q is
not-all-equal(x,y,z). By contrast the actual exterior F has only the
all-equal boundary relation. Its two complementary all-equal colorings
both occur, because color names may be swapped.

For any valid coloring of T-a, the vertices x,y,z are consequently
monochromatic and b,c have the opposite color. The analogous statements
hold for deletion of b or c. These are genuine constraints on all
such deletion colorings, not just on a conveniently selected one.

This describes a three-terminal incompatibility. It does not prove
that a planar exterior with the all-equal property cannot occur.
In particular the patch is not declared unconditionally reducible.

## 6. Rejected shortcut and its explicit local witness

An incorrect shortcut would infer that a known directed facial
triangle through a degree-four vertex belongs to the disjoint pair
of directed facial triangles provided by C09.

Consider a wheel with hub v and cyclic rim b,c,z,x. Its arcs are
v->b, c->v, v->z, x->v,
b->c, z->c, x->z, b->x.
The hub has indegree two and outdegree two. The triangles vcz and
vxb are directed and meet only at v. The triangle vbc is also
directed, but the opposite triangle vxz is transitive.
This is a finite planar local witness against the shortcut.
It is not a counterexample to the root and does not satisfy the
global minimum-counterexample hypothesis. Section 4 avoids the
shortcut by its separate global extension argument.

## 7. Prior art and remaining scope

Raphael Steiner, A Note on Graphs of Dichromatic Number 2,
DMTCS 22:4 (2021), paper 11, DOI 10.23638/DMTCS-22-4-11.
https://dmtcs.episciences.org/7040/pdf
Lemma 1 on printed page 2 is tournament gluing. Proposition 1 and
Figure 1 on printed pages 2-3 use an oriented octahedron to prevent
a monochromatic outer triangle. The screenshot of Figure 1 and the
statement on page 2 were read. The not-all-equal gadget principle
is prior art; no novelty claim is made here.

The contribution of this candidate is the explicit deduction of the
six-vertex patch and its forced direction/boundary properties from
C09-C10, including the sufficiency proof by two underlying paths.
Steiner's general precoloring extension is equivalent to the root
conjecture, so it is not used as an unconditional theorem.

## Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c11-triangular-interface
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: derive the four-terminal disk structure of a low path
component and a reachability-state gluing rule that detects real
cycles, including cycles using the exterior. The all-equal exterior
obstruction is retained, not presumed impossible.
No mathematical program, finite-instance search, or verifier was run.
