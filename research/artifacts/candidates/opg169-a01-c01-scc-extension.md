# Candidate C01: SCC gluing and low-degree extension

Status: proof-drafted. Verdict: candidate_only.
Candidate ID: candidate:opg169-a01-c01-scc-extension
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Target statement SHA-256: e5d7b7d2903018956d3e5c66f61cd5d33ef699e068931d2e97a13a1fbaeda4da
Base: 9ab3be6a25a9694cbe99eb9517363213dfd36acb

## Frozen claim and conventions

If G is an orientation of a finite simple planar graph, is not acyclically
2-colorable, and has the least number of vertices among all such
counterexamples, then G is strongly connected and delta(U(G)) >= 3.
Here U(G) is the underlying undirected graph.

A 2-coloring is a function c: V(G) -> {1,2}; an unused color is allowed.
It is valid exactly when each induced digraph G[c^{-1}(i)] has no directed
cycle. This is not proper coloring of U(G). An orientation assigns exactly
one direction to each edge: no loop, digon, or repeated arc is present.
A directed cycle has distinct vertices except for its repeated endpoint.
Allowed axioms: finite-digraph-basic, planar-graph-basic, finite-combinatorics.
No assertion that a counterexample exists is made.

## C01.1: deletion and minimality

For every S subset of V(G), G[S] is the inherited orientation of the simple
planar induced graph U(G)[S]. Delete vertices and incident edges in a planar
drawing; no edge, crossing, loop or reverse arc is introduced. Thus every
proper induced subdigraph is validly 2-colorable by vertex minimality.
The empty digraph has the empty coloring, so G is nonempty. This argument
does not assume that deleting an arc reduces the number of vertices.

## C01.2: SCC gluing

Let S_1,...,S_t be the equivalence classes of mutual directed reachability.
They are the strongly connected components. The condensation has a vertex
for each S_j and an arc S_j -> S_k, j != k, whenever G has such an arc.
If the condensation contained a directed cycle, internal directed paths
in its components together with the inter-component arcs would make all
components on that cycle mutually reachable. They would therefore be one
component, a contradiction. The condensation is acyclic.

Every directed cycle of G lies in a single component: any two of its
vertices reach each other along the cycle. Equivalently, a cycle crossing
components would project to a nonempty directed closed walk in the
condensation, and every such finite walk contains a directed cycle.

Suppose t >= 2. Every S_j is then a proper vertex subset. By C01.1 choose
a valid coloring c_j of G[S_j]. Define c(v)=c_j(v) for v in S_j. This is a
function on all of V(G); its two color classes are disjoint and cover V(G).
Keep ALL original arcs when forming each induced color-class digraph.
A monochromatic directed cycle would lie in one S_j, contradicting the
validity of c_j. Thus c is valid on G, a contradiction. Consequently t=1
and G is strongly connected.

## C01.3: exact obstruction to restoring one vertex

Fix v and any valid coloring c of H=G-v. Call color i blocked at v if
assigning i to v produces a monochromatic directed cycle.
Color i is blocked if and only if H has a directed path
w -> ... -> u entirely of color i, where v -> w and u -> v are arcs.

For necessity, any new monochromatic cycle must contain v: otherwise it
already existed in the unchanged induced color-class digraph of H.
On that cycle let w follow v and u precede v. Removing v gives the stated
path. For sufficiency, append u -> v -> w to such a simple path.
The endpoints u and w are distinct since G is an orientation. In
particular, a blocked color must appear on BOTH an in-neighbor and an
out-neighbor of v. Merely having both kinds of neighbor is not sufficient;
the monochromatic return path is also required.

## C01.4: every degree-0/1/2 vertex is extendible

Use degree in U(G), not just in-degree or out-degree. Minimality supplies
a valid coloring of G-v by C01.1.

Degree 0: v has neither an in-neighbor nor an out-neighbor, so either color
is safe by C01.3.

Degree 1: the sole incident arc enters v or leaves v. One of the two
neighbor sets is empty, so neither color is blocked.

Degree 2: the two distinct neighbors give exactly three cases for
(d^-(v),d^+(v)).
- (2,0) or (0,2): a required kind of neighbor is absent, so both colors
  are safe.
- (1,1): write u -> v -> w. If c(u) != c(w), neither color occurs on
  both endpoints, so both are safe. If c(u)=c(w)=i, assign 3-i to v.
  Color i may be blocked precisely by an i-colored w-to-u path; color
  3-i cannot be blocked because it is absent from both neighbors.

Thus the two colors cannot both be blocked at a degree-2 vertex. Restoring
v changes only its color-class vertex set and the arcs incident with v;
the other induced color-class digraph is unchanged. Each case constructs
a valid coloring of G, contradicting that G is a counterexample.
Therefore no degree-0/1/2 vertex exists and delta(U(G)) >= 3.

## Dependency and attack audit

C01.1 uses only the frozen class and vertex minimality.
C01.2 depends on C01.1 and finite directed reachability.
C01.3 uses only the valid coloring of G-v and the orientation convention.
C01.4 depends on C01.1 and C01.3.
The target follows from C01.2 and C01.4; there is no circular dependency.

Hand-audited falsifiers: empty G; singleton SCCs; several SCCs with arcs
between them; a source or sink of degree 2; differently colored neighbors;
and u -> v -> w -> u with u,w of the same color. The last example really
blocks that color but leaves the other color available. A pre-existing
cycle avoiding v is excluded by validity on G-v, not by planarity.
A bidirected triangle is outside the orientation domain and warns against
dropping the no-digon hypothesis. No enumeration or solver was run.

The degree bound in the target is not asserted to be strongest possible.
This proof uses planarity only for closure under vertex deletion, so its
mechanism also applies to a vertex-hereditary class of orientations.
That observation is not a claim about all orientations being 2-colorable.

## Sources, limitations, and checkpoint

Source comparison: research/artifacts/source-notes/opg169-a01-c01-sources.md.
Mohar's 2009 paper, Section 2, Lemmas 2.1 and 2.2, provides directly relevant
prior art. The elementary arguments above expose the required SCC and
degree-2 details; no novelty claim is made.

No verifier receipt, formal compilation, or admission has been produced.
Both admitted obligations remain open in repository truth.
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c01-scc-extension
route_status: open
next_obligation: obligation:opg169-strong-min-degree-three
next_action: audit the stronger semidegree-two consequence, vertex
criticality versus arc criticality, and the exact degree-four boundary.
The root conjecture is not a consequence of this structural lemma.
