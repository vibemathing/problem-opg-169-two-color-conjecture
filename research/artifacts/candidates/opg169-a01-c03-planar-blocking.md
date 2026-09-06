# Candidate C03: articulation gluing and planar blocking rotations

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c03-planar-blocking
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: f4c980f287c1a1b6fcbd1ca41d7253e67662887b

## Scope

Retain exactly the finite simple planar orientation and vertex-minimality
hypotheses of the frozen target. C01 supplies a full proof draft of that
target. C02 strengthens its degree bound. The following are explicitly
additional necessary conditions, not changes to the admitted statement.
Their status is still candidate_only.

## C03.1: the underlying graph has no cut vertex

By C01 the hypothetical minimum counterexample G is strongly connected,
so U(G) is connected. Suppose a cut vertex t exists. Let W1,...,Wr,
r>=2, be the vertex sets of the connected components of U(G)-t.
Each G[Wj union {t}] is an orientation of a proper induced simple planar
graph, so vertex minimality provides an acyclic 2-coloring. In each piece
interchange color names when needed to make t color 1. The colorings then
agree on their sole common vertex and define a coloring of G.

There are no edges between distinct Wj. Every simple directed cycle
avoiding t lies in one Wj. If a simple directed cycle contains t, removing
t from the cycle leaves a connected path in U(G)-t, lying in a single Wj.
The entire cycle is therefore in that piece with t restored. Hence a
monochromatic cycle in the combined coloring would already be one in
a colored piece, a contradiction. Thus U(G) has no cut vertex.
The degree bound from C02 ensures at least three vertices, so U(G) is
2-connected. This does not assert 3-connectivity or the absence of
two-vertex separators.

## C03.2: nonalternation of disjoint blocking cycles

Fix a plane embedding of G, a vertex v of degree four, and any valid
coloring c of G-v for which both colors are blocked. By C02, each color
occurs on exactly one in-neighbor and one out-neighbor of v. By C01.3
there are directed simple blocking cycles C1 and C2, each through v,
whose remaining vertices have colors 1 and 2 respectively. They have
no common vertex other than v.

The four incident edges used by these two cycles cannot alternate
C1,C2,C1,C2 around v. Indeed, the image of the simple cycle C1 is a
Jordan curve. The connected curve C2-v is disjoint from C1 and so lies
on one side of it. Alternating incident edges would put its two ends
locally on opposite sides of C1 at v, a contradiction.
This explicitly uses the cycle-separation fact from planar-graph-basic;
a later formal encoding must supply that fact for its embedding model.

Thus the neighbor colors around v cannot be 1,2,1,2 cyclically.
Up to rotation and exchanging colors their blocked pattern is 1,1,2,2.
The conclusion is NECESSARY, not sufficient: same-colored in/out
neighbors also need the same-colored directed return paths.

## C03.3: complete four-edge rotation classification

Write I for an arc entering v and O for an arc leaving it. Because both
semidegrees equal 2, up to rotation and reversal the types are:

I1,I2,O3,O4:
the only possible two-color blocking pairs are {I1,O4} and {I2,O3}.
The other in/out matching {I1,O3},{I2,O4} alternates and is excluded
by C03.2. Pairing the two I edges together cannot create a blocking cycle.

I1,O2,I3,O4:
the possible pairings are {I1,O2},{I3,O4} or {I1,O4},{I3,O2}.
Both are nonalternating. The remaining pairing uses I-I and O-O
and is excluded by the directions alone.

These two small cases are a logical classification, not an executed
enumeration. No stronger claim that every degree-four vertex is
reducible follows: the oriented octahedron in C02 realizes an allowed
nonalternating blocking pattern and still has a different valid coloring.

## Audit, sources, and continuation

C03.1 depends on vertex-deletion heredity and the SCC conclusion in C01.
C03.2 depends on C01's exact blocking-path lemma, C02's four distinct
neighbors, and planar cycle separation. C03.3 is only the explicit
two-matching case split. No new admitted graph nodes or ledger entries
are introduced. The original target has no dependency on these
additional refinements, so its proof is not made circular.

Attack cases: two directed triangles sharing one vertex show that strong
connectivity alone does not exclude an underlying cut vertex; gluing
uses minimality in addition. C02 shows that nonalternation does not
imply extendibility. Dropping planarity invalidates the separation
argument, while the articulation argument itself does not need it
except for heredity of the class.

Source context and conventions are recorded in the C01 source note.
The local proof is given in full; no claim of novelty or formal-library
reuse is made. A bounded search for planar minimum-counterexample
degree-four/two-triangle statements did not supply an exact theorem
binding for these refinements; search absence is not a novelty result.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c03-planar-blocking
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: audit the planar shortcut-fan reduction at a semidegree-two
vertex, including every possible reverse-arc conflict; test whether
degree-four vertices must lie on two directed triangles.
No mathematical runtime, verifier receipt, or admission is claimed.
