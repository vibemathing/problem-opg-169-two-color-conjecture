# C23: forest compression of low patches and a twelve-vertex high core

Verdict: candidate_only. Status: proof-drafted with named source dependencies.
Candidate: candidate:opg169-a01-c23-forest-compression
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 47e284ea38aa1fa0afb9deb721d1e542dffae850
Primary owner: math-proof.

## 1. Frozen setting and dependency levels

Let T be the selected maximum-size representative of minimum counterexample
order from C09, not an arbitrary minimum-order orientation. Use C16:
H is its set of vertices of degree at least five, h=|H|;
a,b,c count the components of the degree-four induced subgraph that are
respectively singletons, edges, and triangles. Then
  n=h+a+2b+3c,
  a+b=f4(T[H])<=h-2,
  c<=2h-4-2(a+b).

The local disk descriptions and extension-existence tables are those of
C11/C16; C17 fixes the unique majority pole of each low-edge patch.
We construct a new UNDIRECTED planar graph J. A two-forest partition of
J is sufficient, not necessary, for an acyclic two-coloring of T.

The numerical conclusions have explicit external premises:
HM36: every simple 3-connected cubic planar graph of order at most 36
is Hamiltonian (Holton--McKay).
KV26: every planar orientation of order at most 26 has an acyclic
two-coloring (Knauer--Valicov, Proposition 4).
The source note records their scope and what was actually read.
Neither computation nor either published proof is replayed here.

## 2. A Hamiltonian dual cycle gives induced forests

Let Q be a simple plane triangulation on k>=4 vertices and Q* its
geometric dual. Suppose Q* has a Hamiltonian cycle C*. Draw that cycle
as a Jordan curve, crossing each corresponding primal edge once,
no other primal edge, and no primal vertex. Color vertices of Q
according to the two components of the sphere minus the curve.

An edge of Q whose endpoints have the same color cannot be crossed by
C*: every crossed edge has exactly one transverse crossing, so its
endpoints lie on opposite sides. Thus a monochromatic simple primal
cycle C would be disjoint from C*. The connected curve C* lies in one
component of the sphere minus C. The other open disk contains a face
of Q: choose an interior point away from all primal edges; the
containing face cannot cross C. Its dual vertex lies in that disk.
But C* visits every dual vertex and lies on the other side of C.
This contradiction proves that both induced color classes are forests.

This uses the whole dual Hamiltonian cycle, not a spanning 2-factor,
a directed Hamiltonian cycle, or a Hamiltonian primal graph.
The primal orientation does not enter the argument.

## 3. HM36 implies two induced forests for every planar graph of order <=20

For k<=3 a partition into parts of size at most two suffices.
For 4<=k<=20, add planar edges without adding vertices to make the
given simple planar graph a maximal plane graph Q.

For completeness, edge maximality makes it connected. It has no cut
vertex: two consecutive neighbors at a cut vertex that belong to
different components after its deletion can be joined through that
face, and were not already adjacent. Facial boundaries are therefore
cycles. In a face of length at least four, take four consecutive
vertices. Its two alternating diagonals cannot both already lie in
the complementary disk. Add a missing diagonal in the face.
Consequently every face of Q is a triangle.

The dual Q* is simple and cubic. There is no dual loop since Q has no
bridge. Two distinct triangular faces cannot share two edges unless
Q is just a triangle, excluded by k>=4. Hence no dual parallel edges
occur. Elementary plane cycle--bond duality gives edge-connectivity
at least three: a dual bond of size one or two would give a primal
cycle of that size, impossible in a simple graph.

A simple cubic 3-edge-connected graph is 3-vertex-connected. A cut vertex
cannot attach three or more edges to each of two components. For a
two-vertex cut {u,v}, each component requires at least three edges to it.
If uv is an edge, only four attachment edges are available, impossible.
Otherwise there are exactly two components, each with three attachments.
Absence of a cut vertex forces distributions 2+1 and 1+2. The component
together with the terminal to which it has two attachments then has
an edge boundary of size two, also impossible.

Euler's identity gives |V(Q*)|=2k-4<=36. HM36 provides its Hamiltonian
cycle; Section 2 supplies induced forests in Q. Restricting to the
original graph preserves the forest property. This proves the stated
bounded-order consequence of HM36.

## 4. Compress every low edge and low triangle, keeping isolated lows

Start with the induced underlying graph
  P=U(T)[H union {all isolated degree-four vertices}].
Thus |V(P)|=h+a. The deleted low-edge and low-triangle disk interiors
leave distinct quadrilateral and triangular faces. The cyclic boundary
of an edge patch is p,r,q,s, with internal chain r,x,y,s and poles p,q.

For that edge patch C17 supplies its distinguished majority pole h0:
its only forbidden boundary partition has h0,r,s in one color and the
other pole in the opposite color. Add the undirected edge rs if absent.
Both existing edges h0r,h0s are boundary edges, so this makes a triangle
on {h0,r,s} in the auxiliary graph, whether or not it is a facial triangle.

Do this for every low-edge patch and call the resulting graph J.
The construction is simple and planar. Each absent edge can be drawn
inside its own empty quadrilateral. If it was already present outside,
leave it unchanged. If several faces request the same absent edge,
insert one copy through one requesting face. All other requested edges
use distinct face interiors. No edge is reversed, no duplicated edge
is kept, and no crossing is introduced.
There are no new vertices: |V(J)|=h+a.

Suppose J has a partition into two induced forests. Restrict its vertex
colors to P and to the original orientation. This is acyclic in each
color. Erase ALL artificially added edges before putting patches back.

Every removed low triangle has a nonmonochromatic boundary: its three
outer edges were already in P and would otherwise form a monochromatic
undirected cycle in J. Its C11/C16 table therefore allows extension.

For every removed low edge, the triangle {h0,r,s} in J is not
monochromatic. Its unique forbidden partition is consequently avoided,
regardless of the color of the other pole. This is a stronger auxiliary
restriction than its full exact table, and is used only for sufficiency.

Insert the deleted patches one by one, each time using its extension
table against the ACTUAL currently colored planar exterior. Previously
inserted patches may supply new paths, but the tables are universal
over those exteriors. All remaining boundary colors stay fixed.
Finite induction produces an acyclic two-coloring of T, a contradiction.

Thus J has no two-induced-forest partition. It follows from Section 3
and HM36 that
  h+a>=21.                                               (1)

The graph J is an auxiliary undirected graph, not an asserted smaller
counterexample to the root. Its orientation is irrelevant, and
forest colorability is not being identified with acyclic orientated
colorability. Isolated low vertices were retained, not silently deleted.

## 5. Improved core bound and an equality profile

Combining (1) with a+b<=h-2 yields
  21<=h+a<=2h-2-b,
  2h-b>=23,
  h>=12.                                                 (2)
The stronger inequality involving b is retained.

Now additionally use KV26, so n>=27, and suppose h=12.
Equation (1) implies a>=9; also a+b<=10.
If a+b=10, the bound on c gives c=0, and
  n=12+a+2b=22+b.
Since a>=9 implies b<=1, this gives n<=23, impossible.
If a+b<=9, necessarily a=9,b=0. Then c<=2 and
  n=21+3c>=27
forces c=2 and n=27.

Hence the only surviving h=12 profile under BOTH source premises is
  (h,a,b,c,n)=(12,9,0,2,27).                             (3)
The high core has exactly nine quadrilateral faces and two triangular
faces; both triangular faces carry low-triangle patches.
This is a necessary residual profile, not an existence or exclusion claim.

Deleting only the two low triangles in this residual case gives a
21-vertex plane triangulation P=J. It contains nine original isolated
degree-four vertices. By Section 4 it has no induced two-forest partition.
Its 38-vertex cubic dual is consequently non-Hamiltonian by Section 2.
This finite residual family is a sharper next target than an unrestricted
search over arbitrary small plane cores.

For comparison, deleting low triangles but NOT compressing low edges
would only give h+a+2b>=21 and h>=9. Section 4 explains the extra valid
compression responsible for (2); the stronger bound is not obtained
by pretending that the low-edge patches are always extendible.

## 6. Attack and scope audit

A feedback vertex set controls only its complement and is not a
two-induced-forest partition. Acyclicity of oriented color classes
does not imply their underlying graphs are forests. Neither
substitution is made here.

Existing exterior rs edges are never reversed or relocated. New
diagonals are erased before reinsertion, avoiding crossings with
the restored patch. Their nonmonochromatic triangle constraints
remain true because the vertex colors did not change.

The forest premise is a sufficient certificate deliberately stronger
than the root coloring property. Failure to find forests beyond
the proved order range is not a root counterexample.
No finite-order numerical result from KV26 was enlarged to order27
for all planar orientations. Its further 4-connectivity restrictions
were not imported into the present residual case.

Every use of HM36 and KV26 is exposed as a named source dependency.
The bound (1)-(2) uses HM36 but not KV26. Profile (3) also uses KV26.
No graph enumeration, Hamiltonian search, SAT run, published program
replay, or verifier receipt was produced.

## 7. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c23-forest-compression
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; no previously excluded route reused
next_obligation: obligation:opg169-strong-min-degree-three
next_action: characterize the 21-vertex residual triangulation and its
38-vertex non-Hamiltonian dual, auditing any source enumeration before
using it to exclude (3). Keep the orientation root separate from the
stronger induced-forest certificate problem.
