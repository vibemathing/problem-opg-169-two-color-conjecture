# Candidate C05: exact two-terminal gluing interface

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c05-two-terminal
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 718cca5efdbe0047901b215607eda52afe0bf24c

## Scope and decomposition

Let G satisfy the hypothetical global vertex-minimum counterexample
assumptions of the frozen contract. For a two-vertex separator S={s,t},
s!=t, let W1,...,Wr, r>=2, be the components of U(G)-S, and put
Hi=G[Wi union S]. Each Hi is a proper induced planar orientation, so it
has a valid acyclic 2-coloring. There are no arcs between distinct Wi.
An arc between s and t, when present, belongs to every Hi.

The interface lemma below applies more generally to any such union of
colorable pieces, independently of planarity. Its minimality and size
consequences use the frozen class and C01-C03. These are additional
structural candidates, not a replacement or closure of the admitted target.

## C05.1: four coloring signatures and three compatible regimes

Normalize color names in each piece. A valid coloring has one of:
D: s and t have different colors.
E0: s and t have color 1 and neither is reachable from the other by a
    monochromatic directed path in Hi.
E+: s and t have color 1 and there is a monochromatic s-to-t path.
E-: s and t have color 1 and there is a monochromatic t-to-s path.

Paths have positive length; a direct terminal arc counts. For equal
terminal colors, both directions cannot occur in one valid piece:
concatenating the paths gives a nonempty directed closed walk and hence
a monochromatic directed cycle. Thus E+ and E- are mutually exclusive.

If every piece has a D-coloring, normalize s to 1 and t to 2 and glue.
A directed simple cycle using more than one piece must contain both
s and t. To see this, such a cycle can leave a component Wi only through
S; if it used only one terminal, deleting that terminal from the cycle
would leave a path in a single component of U(G)-S. A cross-piece cycle
therefore cannot be monochromatic when the terminals differ.

For equal terminal colors, normalize both to 1. A cross-piece simple
directed cycle gives an s-to-t monochromatic path in one piece and a
t-to-s monochromatic path in another. Conversely such paths in distinct
pieces have disjoint internal vertices and their union is a directed
cycle. If one path is a direct terminal arc, the opposing path would
already form a cycle in its own piece, since that arc belongs to all
pieces; validity rules this case out. Color 2 has no terminal vertices
and cannot create a cross-piece cycle.

Consequently equal-terminal colorings glue exactly when they do not
collectively contain both reachability directions.

For each piece define its nonempty availability set Ai subset of
{D,P,M} by:
D in Ai if a D-coloring exists;
P in Ai if an E0- or E+-coloring exists (no monochromatic t-to-s path);
M in Ai if an E0- or E--coloring exists (no monochromatic s-to-t path).

The E0 signature contributes to BOTH P and M; these regimes are not
exclusive signatures of an individual coloring.

The union G has a valid acyclic 2-coloring if and only if
the intersection of all Ai is nonempty.
For sufficiency, choose and normalize a coloring in a common regime
for each piece and apply the preceding gluing arguments.
For necessity, restrict any valid global coloring. Different terminal
colors give D in all Ai. If terminal colors agree, the global color
class cannot have paths in both directions, so one missing direction
gives P in all Ai or M in all Ai. This proves both directions.

## C05.2: at most three components behind a two-vertex separator

In a minimum counterexample the intersection of the Ai is empty.
For each of D,P,M choose a piece that excludes that regime. At most
three pieces have been selected, and their availability intersection
is already empty. Their induced union with S is not 2-colorable by
C05.1. If r>=4, this is a proper induced subdigraph of G in the frozen
class, contradicting vertex minimality. Hence r<=3.

If s->t is an arc, every equal-terminal coloring includes its
monochromatic s-to-t path, so M is absent from every Ai. There are
then only two possible regimes; the same argument gives r<=2.
For an arc t->s, exchange P and M. Thus an adjacent two-vertex
separator has exactly two components.

When r=3, deleting any one Wi leaves a colorable proper induced graph.
Thus every pairwise intersection of the Ai is nonempty, while the
triple intersection is empty. Choose a_i in the intersection of the
other two sets. It is not in Ai. These three a_i are distinct: if
a_i=a_j for i!=j, the first choice lies in Aj and the second does not.
They therefore exhaust {D,P,M}. Each Ai contains the other two
regimes and omits a_i. Up to indexing, the only family is
{P,M}, {D,M}, {D,P}.
This is a necessary interface pattern; no planar realization or
nonexistence of that pattern is asserted.

## C05.3: every component behind the separator has at least four vertices

By C02 every vertex of G has underlying degree at least 4. If
|Wi|<=2, its vertices have degree at most |Wi|-1+2<=3, impossible.

Suppose |Wi|=3. Each of its vertices must meet the other two and both
terminals, since these are its only four possible neighbors.
The induced underlying graph on Wi union S is K5 with at most the
terminal edge st missing. If st exists, this is nonplanar: a simple
planar graph on five vertices has at most nine edges, not ten.

If st is absent, choose any other component Wj. By C03, U(G) has no
cut vertex, so Wj has a neighbor at each of s and t; otherwise deleting
its sole neighboring terminal would disconnect Wj from the rest.
Since Wj is connected, there is an s-to-t path with all internal
vertices in Wj. Together with U(G)[Wi union S], this is a subdivision
of K5. Contract the external path to an st edge to obtain a K5 minor,
contrary to planarity and the same five-vertex edge bound.
Thus |Wi|>=4 for every i.

It follows that a minimum counterexample with a two-vertex separator
has at least 10 vertices, and one with three components behind that
separator has at least 14. These are conditional structural bounds,
not claims of optimal published order bounds for the whole conjecture.

## Source comparison and attacks

Primary source inspected: L. Gishboliner, R. Steiner and T. Szabo,
Dichromatic number and forced subdivisions, November 5, 2021,
printed page 16, Claim 2 and its proof (PDF page index 15).
https://people.math.ethz.ch/~lgishboli/dic_mader.pdf
The source studies a different 4-dicritical, forbidden-subdivision
counterexample and inserts a digon between separator vertices to force
different colors before gluing three-colorings. Relation: analogy,
not an applicable theorem. Inserting that digon is forbidden in our
orientation contract. C05 instead retains all three admissible
two-color/reachability regimes; it does not assert 3-connectivity.

A minimal gluing falsifier is the directed cycle
s->a->t->b->s, split into pieces on {s,a,t} and {s,b,t}.
Coloring all vertices with color 1 gives acyclic pieces with agreeing
terminal colors, but their union is cyclic. Their directions are E+
and E-, exactly the incompatible pair above. The graph itself has a
valid 2-coloring; the example tests the gluing rule only.

Further attacks: an E0 coloring must not be counted as incompatible
with E+ or E-; different terminal colors always prevent cross-piece
monochromatic cycles; a shared terminal arc cannot be forgotten.
No assertion about strong 2-connectivity follows from this analysis.

## Dependencies and checkpoint

C05.1 uses only the piece decomposition and valid colorings.
C05.2 adds global vertex minimality and induced-subgraph heredity.
C05.3 uses C02's degree bound, C03's no-cut-vertex lemma, and the basic
minor closure and edge bound for planar graphs. The original target
does not depend on these refinements; no new admitted nodes are created.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c05-two-terminal
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: produce an uncompiled core formalization of the
four-distinct-neighbor atom and a precise statement-faithfulness
handoff; do not treat the abstract atom as a full formal proof.
No mathematical program, verifier receipt or admission is claimed.
