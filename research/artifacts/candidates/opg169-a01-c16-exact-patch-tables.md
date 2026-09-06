# C16: exact patch extension tables and the high-vertex core

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c16-exact-patch-tables
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: d90ba0a2be0dc58ae8fe2cd70c788f8290f7ab12
Primary owner: math-proof.

## 1. Precise extension quantifiers

A patch is drawn inside a disk whose boundary is a simple triangle or
quadrilateral. Its exterior F is any finite simple plane orientation drawn
in the complementary disk and containing every oriented boundary edge.
A valid coloring of F means that each induced color class has no directed
cycle. All exterior arcs, including possible boundary diagonals, are retained.

For each fixed patch orientation we determine exactly which boundary
colorings prevent extension of a valid coloring of F. The conclusions below
hold for EVERY compatible planar exterior F and EVERY valid coloring of F.
An extending internal coloring may depend on F, not just its boundary colors.
Thus this is an existence table, not an assertion that arbitrary independently
chosen internal colorings can be glued.

No minimum-counterexample assumption is used in Sections 2-4.

## 2. One interior vertex: the quadrilateral wheel

Let a,b,c,d occur cyclically on the boundary. The only interior vertex v
is joined to all four boundary vertices, and the four actual patch faces
are vab, vbc, vcd, vda. Write D(vab) when that oriented triangle is directed.
Colors A and B are distinct. Up to exchanging colors, the complete table is:

- Boundary multiplicities 4:0 or 3:1: always extendible.
- Alternating boundary A,B,A,B: always extendible.
- Boundary a=b=A and c=d=B: not extendible exactly when
  D(vab) AND D(vcd).
- Boundary b=c=A and d=a=B: not extendible exactly when
  D(vbc) AND D(vda).

These cases exhaust the sixteen labeled boundary assignments.

For the first case put v in a color occurring at most once on the boundary.
It has at most one same-colored neighbor, hence lies on no monochromatic cycle.

For an adjacent two-and-two assignment, consider color A and its adjacent
boundary pair a,b. A new monochromatic cycle must consist of the two incident
arcs at v and a return path between a and b in F. F already contains one arc
between a and b. A monochromatic path opposite that arc would contradict
acyclicity in F. Consequently color A is blocked precisely when vab is
directed. Apply the same argument to the B pair. This proves both directions.

For the alternating assignment, failure of both choices at v would give
an A-colored path between a,c and a B-colored path between b,d in F.
The two paths are vertex-disjoint because their colors differ. Their
underlying paths join alternating boundary pairs in a disk, which planarity
forbids. Their endpoints are distinct, and neither path can pass through
the other pair of boundary terminals. Therefore at least one color extends.

There are at most two forbidden two-and-two partitions, each representing
two complementary Boolean assignments. The table does not require the
spokes at v to be balanced: failure itself would force two incoming and
two outgoing spokes.

## 3. Two interior vertices: the short two-cone strip

The boundary is p,r,q,s in cyclic order. Interior vertices x,y form the
chain r,x,y,s, and each is adjacent to both poles p,q. There are no other
interior vertices or incident edges. The six patch triangles are the two
pole cones on each of rx, xy, ys.

The complete extension table is:

- If color(p)=color(q), every valid exterior coloring extends.
- If color(p)!=color(q) and color(r)!=color(s), it extends.
- If color(p)!=color(q) and color(r)=color(s), let h be the pole of that
  common color and t the other pole. It fails to extend exactly when
  all THREE triangles h r x, t x y, h y s are directed.

In particular only two possible three-and-one partitions can be forbidden:
the singleton color is at one of the poles. Each forbidden partition
represents two complementary assignments. This applies to arbitrary
orientations of the short-strip edges.

### 3a. Hole and parity proof

Assume for contradiction that a particular valid coloring of F does not
extend. First insert y, leaving x uncolored. Only p,q,s are colored
neighbors of y; a color absent from its incoming or outgoing side is safe.
Such a side has at most one colored neighbor. This yields a valid coloring
of F+y.

Both choices at the remaining hole x must fail. Each failure is a genuine
monochromatic cycle through x, so each color supplies an incoming and an
outgoing neighbor. The four neighbors are distinct and therefore each of
the two in/out pairs has one vertex of each color.

Erase y and give its former color to x. In the in/out pair of x containing
y, that color is now absent. Thus the transfer is safe and leaves a valid
coloring with hole y. Both choices at y must also fail.

Suppose p and q are both A. The first hole forces r and y to be B;
the transferred hole forces s to be B as well. In the original coloring
with hole x, the A obstruction gives an A path between p,q wholly in F.
The B obstruction gives a directed path between r,y. Since y has no other
B neighbor than s once x is deleted, this path contains a B path between
r,s wholly in F. These two differently colored paths join alternating
boundary pairs in the exterior disk, a contradiction.

Thus p and q differ. At either hole its two chain neighbors must differ:
if the poles form an in/out pair, this follows for the other pair;
if the poles are in different pairs, the chain neighbors are opposite
to differently colored poles. At the first hole r differs from the
original color of y. At the transferred hole the original color of y,
now on x, differs from s. Hence r and s have equal colors.

### 3b. Three decisive full colorings

Normalize r=s=h=A and t=B. The following assignments each have exactly
one monochromatic edge on the chain r,x,y,s:

j=0: x=A, y=B; the exceptional triangle is h r x.
j=1: x=B, y=B; the exceptional triangle is t x y.
j=2: x=B, y=A; the exceptional triangle is h y s.

All other same-colored internal vertices are leaves attached to their
matching pole. In j=1 the exceptional triangle meets F only at t.
In j=0 and j=2 it meets F exactly in its oriented boundary edge.
If the exceptional triangle is transitive, no monochromatic cycle can
be formed by adjoining it to F: any new path opposite the common arc
would already make the triangle cyclic, while a path following the
common arc cannot close a cycle absent from F. The remaining leaves
cannot be on a cycle. Therefore if any of these three triangles is
transitive, the corresponding assignment extends.

Conversely, if all three triangles are directed, h r x forces x=B
and h y s forces y=B. Then t x y is monochromatic and directed.
There is no extension. This proves necessity and sufficiency.

## 4. Three low vertices: the triangular octahedral patch

This paragraph concerns the particular low-triangle patch from C11-C12
in the selected minimum-order triangulation. Let its inner vertices
a,b,c form a directed triangle, with outer triangle x,y,z. The corner
triangles a x z, b x y, c y z are directed. These are the relevant
orientation properties of that structural patch, not assumptions about
arbitrary octahedral orientations.

Its exact forbidden boundary patterns are all-equal x,y,z.
Indeed all-equal outer color A forces a,b,c to color B using the three
corner cycles, after which their inner directed triangle is monochromatic.

Every nonconstant outer coloring extends. For example x=y=A,z=B admits
a=A,b=c=B; the two induced underlying subgraphs of the patch are paths.
The other cases follow by relabeling the outer and corresponding inner
vertices and exchanging colors. The patch shares the complete outer
triangle with F. In each color its shared vertices form a tournament.
In an acyclic digraph, paths between vertices of this tournament must
respect its unique order; otherwise the reverse tournament arc closes
a directed cycle. Therefore two acyclic colored pieces sharing exactly
this tournament cannot create a new monochromatic cycle when joined.
This verifies extension against the entire exterior, not just the boundary.

## 5. Simultaneous deletion and insertion

Now let T be C09's maximum-size representative among minimum-order
counterexamples. Write L for its degree-four vertices and H for the rest.
C15 says that the components of T[L] are single vertices, single edges,
or directed facial triangles. Put R=T[H].

C09-C12 give each low component a disk patch of Sections 2-4, with a simple
high-vertex boundary cycle and no other attachments. Patch interiors are
disjoint: if one original triangular face involved low vertices from two
components, those vertices would be adjacent and hence in the same component.
After deleting all low components, the patches become distinct faces of R.
Every other face was already an all-high triangular face of T.

The plane graph underlying R is connected and has no cut vertex. To prove
this directly, replace each segment of a T-path through a low component by
a path on that component's boundary cycle. This gives a walk in R between
any two high vertices. To treat R-z for a high vertex z, start with a path
in T-z, which exists by 3-connectivity of T. Each patch boundary with z
removed is still connected, so the same replacement avoids z. There are
at least three high vertices: every nonempty low patch has at least three
distinct high boundary vertices; if L is empty, R=T. Thus R is 2-connected.

All faces of R are triangles or quadrilaterals. Some triangular faces are
marked as low-triangle patches, and every quadrilateral is marked as a
one-vertex wheel or a two-vertex strip, including its orientation data.

There is a valid two-coloring of T if and only if R has a valid two-coloring
that avoids the corresponding forbidden boundary patterns in Sections 2-4.

Necessity follows by restricting a coloring of T: each forbidden pattern
already forces an internal monochromatic triangle, regardless of other patches.
For sufficiency, insert the patches one at a time. At each step the colored
exterior consists of R and the patches already inserted. It is a compatible
plane exterior and has a valid coloring by induction. The boundary colors
of every uninserted patch remain unchanged. Its table guarantees an extension
against this ACTUAL exterior, which may include new monochromatic paths.
Therefore the enlarged graph stays acyclic in each color. Finite induction
inserts all patches. Cross-patch cycles have not been silently discarded.

The tables eliminate reachability variables for these small patches'
EXTENSION-EXISTENCE test. C13's finer profile is still needed when prescribing
particular internal colorings or handling larger unrestricted pieces.

## 6. Exact Boolean encoding, not an executed SAT certificate

Assign one Boolean variable z_v to each v in H. For every directed simple
cycle C in R include the two clauses
  (OR_{v in C} z_v),   (OR_{v in C} NOT z_v).
These exclude its two monochromatic assignments.

For each marked low-triangle face include its two three-variable NAE clauses.
For each forbidden quadrilateral assignment sigma include
  OR_{v on the face} literal(v,sigma),
where literal is z_v if sigma(v)=0 and NOT z_v if sigma(v)=1.
Include also the clause for the complementary assignment. A quadrilateral
has at most two forbidden partitions, hence at most four such clauses.

By Section 5, this finite formula is satisfiable exactly when T is colorable.
All directed simple cycles of the CORE are required, not just its facial
triangles. These global cycle clauses need not form a planar SAT instance.
No formula instance, solver call, enumeration range, or UNSAT proof has
been produced by this conceptual encoding.

## 7. A size identity for the plane core

Let h=|H| and let a,b,c count respectively the isolated-low, low-edge,
and low-triangle components. Then
  |V(T)|=h+a+2b+3c,
  f4(R)=a+b.
Because R is a connected plane graph with only faces of length three or four,
Euler's identity and the edge-face incidence count give
  f3(R)=2h-4-2f4(R).
Every low-triangle component marks a distinct triangular face, so c<=f3(R).
Consequently
  |V(T)| <= 7h-12-5a-4b <= 7h-12.

This bounds total order in terms of core order, not core order itself.
It does not make the root a finite bounded search or yield a discharging
contradiction.

## 8. Explicit attack on an overstrong gluing interpretation

Take the wheel of Section 2, with cyclic boundary p,r,q,s colored A,B,A,B
and spokes p->v->q and r->v->s. Orient the boundary edges arbitrarily;
each is bichromatic.

One exterior adds only the diagonal q->p. Its A class is acyclic, but v=A
is blocked by a directed triangle, while v=B extends.
A second exterior instead adds only the diagonal s->r. It forces v=A,
while v=B is blocked. Each is planar and acyclicly colored, and has the
same colored boundary and the same wheel orientation.

Thus there is no internal color for v that works uniformly for both
exteriors. The two diagonals are NOT put together: they would cross in
the exterior disk. The quantified existence table holds in both examples.
This excludes only a uniform-choice shortcut, not the root or the admitted route.

## 9. Checkpoint and remaining proof obligation

Dependencies: C09-C12 structural patch geometry, C15 low-component bound,
and elementary directed-cycle and planar alternating-path arguments.
The new universal tables were proved here rather than imported as an
unconditional precoloring theorem.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c16-exact-patch-tables
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: attack the constrained high-core coloring problem, beginning
with minority/majority terminal restrictions on low-edge faces and the
degree-five vertices. Do not drop global core cycle clauses or assert that
a coloring of the smaller core automatically satisfies every marked face.
No mathematical runtime, graph enumeration, or verifier was executed.
