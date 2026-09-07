# C24: a parity-path certificate for a core with two triangular faces

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c24-parity-path
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: d40499d18353066b36376ad29069e820089b2851
Primary owner: math-proof.

## 1. Scope: two odd faces, with actual patch labels retained

Use C09's selected minimum-order triangulation T and C16's high core
R=T[H]. In this cycle assume that R has exactly two triangular faces
A and B and that all its other faces are quadrilaterals. R is simple
and 2-connected, so every face boundary is a simple cycle.

Each quadrilateral retains its actual label: a single-low wheel, or
a two-low strip with its unique majority pole from C17. A triangular
face may be unmarked or may represent a deleted low triangle. All
orientations on the edges of R and all patch data are fixed.

Sections 2-4 give a sufficient coloring certificate without claiming
that one always exists. Section 5 gives structural exclusions. Section 6
applies them to the residual profile of C23. No new admitted node is made.

## 2. Deleting the primal edges of a simple dual A-to-B path

Let
  A=F0, F1, ..., Fl=B
be a simple path in the geometric dual of R, where l>=1. Denote the
primal edges crossed by its successive dual edges by e1,...,el, and
let Gamma be this set of primal edges. No face occurs twice on the path.

Deleting Gamma keeps R connected. Delete e1 first: its incident faces
are distinct, so it is not a bridge and the two faces merge. Next e2
has the merged prefix face on one side and the as-yet-unvisited F2
on the other; these faces are distinct, so it is again not a bridge.
Continue. Extra retained edges between visited faces do not invalidate
this argument; they can become bridges but are not among the edges
being deleted at that step.

The merged face has boundary-walk length
  3+3+4*(l-1)-2*l = 2*l+2,
which is even. Every unvisited face is a quadrilateral. Consequently
R-Gamma is bipartite. To justify the latter implication without an
embedding shortcut, every simple cycle has even length: sum the lengths
of the faces in its disk; internal edges count twice. Bridges on facial
boundary walks also count twice. A graph with no odd cycle is bipartite.

Fix a proper two-coloring phi of the connected graph R-Gamma.
All edges outside Gamma are bichromatic.

## 3. Every deleted edge is monochromatic: the local transition table

Exactly one edge of Gamma lies on each terminal triangle. Its other
two edges are retained. The proper coloring along those two edges
makes the endpoints of the deleted edge equal.

At an intermediate quadrilateral exactly two distinct boundary edges
belong to Gamma. Starting from the first terminal, propagate equality
of the endpoints of the current deleted edge as follows.

If the two deleted edges are opposite, each retained edge joins an
endpoint of the first to one of the second. The endpoints of the second
are equal and have the opposite color to those of the first. Thus the
boundary has two adjacent vertices of each color.

If the two deleted edges are adjacent and meet at z, their two other
endpoints are joined by the retained two-edge boundary path. Those
endpoints have the same color. Equality across the first deleted edge
then makes z and both endpoints the majority color. The fourth vertex
has the opposite color. Thus the boundary is three-and-one, with the
singleton opposite z.

Induction proves that ALL edges of Gamma are monochromatic. Hence the
monochromatic edge-subdigraph of R under phi is exactly the orientation
of Gamma inherited from R. The coloring phi is acyclic on R if and only
if that oriented edge-subdigraph has no directed cycle. In particular
it is enough that the underlying edges of Gamma form a forest.
We do not infer that forest property merely from simplicity of the DUAL path.

The terminal triangles are nonmonochromatic. Every unvisited
quadrilateral is properly alternating around its boundary.

## 4. Exact patch conditions along this path

For a wheel quadrilateral, an adjacent-edge passage gives a three-and-one
boundary coloring and always passes C16's extension table.
An opposite-edge passage gives adjacent two-and-two colors. It passes
exactly when the two cone triangles over the crossed primal edges are
not BOTH directed.

For a strip quadrilateral, an opposite-edge passage gives a two-and-two
boundary coloring and always passes. For an adjacent-edge passage at z,
the singleton color is at the corner opposite z. By C17's unique
forbidden partition, this passage fails exactly when z is the strip's
distinguished majority pole. Turning at any other corner passes.

Every unvisited quadrilateral has alternating colors. This passes
both patch types: opposite poles of a strip then agree, and C16 covers
the wheel case. Every marked terminal triangle is nonconstant and
therefore passes the low-triangle table. Unmarked terminal triangles
are also nonconstant, so neither is a monochromatic directed cycle.

It follows that the following is a SUFFICIENT certificate to color T:
  (i) the oriented primal edge set Gamma is acyclic;
  (ii) each wheel opposite passage avoids two directed cone triangles;
  (iii) each strip adjacent passage avoids its majority pole.

Under (i), Section 3 supplies a valid coloring of the whole oriented
core, not just its faces. By the remaining conditions every marked
face passes its exact table. Reinsert all low patches successively
against the actual colored exterior, as in C16. This gives a coloring
of T. In a counterexample no such path certificate can exist.

The three conditions concern one chosen simple dual path. This theorem
does not assert that every valid coloring arises from a simple path,
or that ordinary dual connectivity guarantees a permitted path.

## 5. Adjacent terminal triangles and a common-vertex obstruction

If A and B share an edge, take their one-edge dual path.
Gamma has one primal edge and is acyclic. There are no intermediate
quadrilaterals to test. Section 4 colors T, a contradiction.
Thus the two triangular faces cannot share an edge.

Suppose instead they meet at a vertex z. Because R is 2-connected,
each face appears only once in the cyclic face order at z.
The two arcs of that cyclic order from A to B give two simple dual
paths. Their crossed primal edges are all incident with z, hence
each Gamma is a star and satisfies condition (i).

Every intermediate passage is between consecutive edges at z.
Wheel passages cannot block either path. Thus each of the two
cyclic sectors must contain a strip whose distinguished majority
pole is z; otherwise its path satisfies all conditions in Section 4.
The strips in the two sectors are distinct.

There is a further semidegree consequence in T. Each of those two
strips gives the four-position link block r,x,y,s at z, with two
incoming and two outgoing spokes supplied by its directed end faces.
The two blocks are disjoint in this particular argument: they lie
in the two separated link sectors, and the two terminal triangles
do not share an edge. Their boundary spoke positions are distinct;
their deleted low interiors are distinct components.
Consequently
  d_T^-(z)>=4 and d_T^+(z)>=4.
This addition of contributions is justified only by these separated
sectors; it is not a general non-overlap claim about arbitrary contacts.

In particular, if there are no low-edge components, the two triangular
faces are vertex-disjoint. More generally, a common vertex must be
the majority pole of at least two distinct edge patches.

## 6. The h=12 residual profile becomes more rigid

Under the named source premises of C23, h=12 leaves exactly
  (h,a,b,c,n)=(12,9,0,2,27).
Thus R has nine quadrilateral wheel faces and two triangular faces,
both marked as low-triangle patches. There are no strip faces.
By Section 5 the two triangular faces are vertex-disjoint.

Let tau(z) be one if a high vertex z lies on either marked triangle
and zero otherwise. Exactly six high vertices have tau=1.
A high vertex is incident with d_R(z) faces, of which tau(z) are
triangular. Each incident quadrilateral restores one isolated low
neighbor; the one marked triangle, when present, restores two.
Therefore
  d_T(z)=d_R(z)+(d_R(z)-tau(z))+2*tau(z)
        =2*d_R(z)+tau(z).                                (1)

Vertices with tau=1 are qualified in the sense of C22: both semidegrees
in T are at least three. Since (1) is odd there, their degrees are
at least seven, so d_R(z)>=3.
Vertices with tau=0 are high and have even degree by (1); hence their
degrees in T are at least six, again giving d_R(z)>=3.

Accordingly the residual case has
  minimum degree of R at least three;
  no degree-five vertices in T;
  fifteen degree-four vertices in T;
  six high vertices of odd degree at least seven;
  six high vertices of even degree at least six.

R has twelve vertices and twenty-one edges. Hence
  sum_(z in H)(d_R(z)-3)=42-36=6.
At least six of its twelve vertices have core degree exactly three.
These are additional necessary restrictions, not a contradiction.

For the 21-vertex triangulation P obtained by deleting the two low
triangles, the core vertices have degrees 2*d_R(z)-tau(z), and its
nine isolated low vertices still have degree four. Its non-Hamiltonian
38-vertex dual from C23 is therefore subject to this specific degree
and face-incidence profile. No graph data have been decoded to claim
that the profile is absent from the published six-graph list.

## 7. Attacks, dependencies and checkpoint

The bipartite construction retains all edges not crossed by the path.
Faces after deletion may have repeated boundary vertices; the parity
argument uses boundary walks and does not require that merged face
to be a simple cycle. The original four-sided faces are simple.

A simple dual path is not automatically a forest in the primal.
The directed acyclicity of Gamma is a separate certificate requirement.
Matching local face patterns alone is insufficient without it.
The sufficient certificate must not be silently promoted to an
equivalence or to existence for every two-triangle core.

The table inputs are C16 and C17. C22 supplies low-triangle boundary
heaviness. C23 supplies only the conditional numerical residual profile.
Sections 2-5 are direct finite plane-graph arguments and require
neither HM36 nor KV26. Their source-backed premises enter only Section 6.
No mathematical program, graph enumeration, or Hamiltonian search was run.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c24-parity-path
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; no previously excluded route reused
next_obligation: obligation:opg169-strong-min-degree-three
next_action: replace the sufficient simple-path certificate by the exact
dual parity-subgraph encoding of all core colorings, keeping both local
patch constraints and global directed-cycle constraints. In particular,
test the unjustified shortcut of discarding closed dual components.
