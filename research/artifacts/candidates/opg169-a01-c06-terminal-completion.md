# Candidate C06: terminal completion tightens the separator interface

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c06-terminal-completion
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 1e52c77162c890587bb3e43eefa17fb75edc50ef

## Frozen scope and prior interface

Assume G is a vertex-count-minimum counterexample in the full frozen class
of orientations of finite simple planar graphs. Let S={s,t} be a
two-vertex separator, and W1,...,Wr the components of U(G)-S, r>=2.
Write Hi=G[Wi union S]. By C03 no vertex is a cut vertex, so every Wi
has neighbors at both terminals. An undirected s-to-t path with internal
vertices in any chosen Wi therefore exists.

Use C05's nonempty availability sets Ai subset of {D,P,M}:
D means there is a valid acyclic 2-coloring with different terminal colors;
P means there is one with equal terminal colors and no monochromatic
t-to-s path; M means equal colors and no monochromatic s-to-t path.
An equal-terminal coloring with neither path contributes to both P and M.
Color names may be swapped.

C05 proves that the coloring availability of any union of these pieces
is the intersection of their sets, and that G is colorable exactly when
the intersection is nonempty. It also proves r<=3, and r<=2 when s,t
are adjacent. C06 is an explicit stronger structural refinement; it
does not alter the admitted statement or claim to prove the root.

## C06.1: one terminal arc may be added to a proper retained union

Suppose s,t are nonadjacent. Choose any nonempty proper subset J of the
component indices. Let F=G[S union (union_{j in J} Wj)].
An omitted component Wk contains an undirected s-to-t path Q whose
internal vertices are disjoint from F.

Keep only U(F) and Q in U(G). Contract all but one edge of Q to obtain
U(F)+st; no retained vertex other than a terminal participates in these
contractions. Hence U(F)+st is planar by minor closure. Equivalently,
the missing part of the embedding supplies space for the new edge.
The terminal edge was absent, and its endpoints are distinct.
Either F+(s->t) or F+(t->s), considered SEPARATELY, is consequently an
orientation of a finite simple planar graph on |V(F)|<|V(G)| vertices.
Both are 2-colorable by global vertex minimality.

The path Q need not be directed in either direction: only its underlying
embedding is used, and the newly added edge is oriented afresh. We never
insert both directions at once. This use of minimality is over the full
contract class, not just over induced subdigraphs of G.

## C06.2: exact constraints imposed by one added arc

For any valid coloring of F, adding s->t preserves validity exactly when
the terminals differ, or they agree and there is no monochromatic
t-to-s path in F. Any new cycle must use the added arc, and deleting that
arc from the cycle gives precisely such a path. Conversely a path plus
the new arc is a cycle. Thus F+(s->t) is colorable exactly when
A_J intersects {D,P}, where A_J=intersection_{j in J} Ai.

Similarly F+(t->s) is colorable exactly when A_J intersects {D,M}.
C06.1 therefore gives BOTH constraints for every proper retained union.
Equivalently, A_J contains D, or it contains both P and M.
This is a statement about existence of colorings; the two augmented
graphs need not have the same coloring.

## C06.3: exactly two components behind every two-vertex separator

The adjacent case already follows from C05. In the nonadjacent case,
suppose r=3. C05's exact three-set classification gives, after indexing,
A1={P,M}, A2={D,M}, A3={D,P}.
Retaining pieces 1 and 2 gives A_{1,2}={M}. It has empty intersection
with {D,P}, contradicting C06.2 for the added arc s->t. Thus r!=3.
Together with r<=3 and r>=2, this proves r=2.

Only a single added arc is used to obtain this contradiction. No
forbidden digon or claim of 3-connectivity is hidden in the argument.
The previously unexcluded three-component regime family is now excluded
under the additional planar-completion/minimality argument.

## C06.4: rigid coloring types on the two remaining sides

Suppose s,t are nonadjacent and write the two sets as A and B.
Each contains D or contains both P and M, by C06.2 with a single piece.
Their intersection is empty because G is a counterexample.
They cannot both contain D. If A omits D, then A={P,M}; disjointness and
nonemptiness force B={D}. Thus, up to swapping the two sides, the only
possibility is {D} and {P,M}.

In concrete terms one piece forces different terminal colors in every
valid coloring. The other forces equal terminal colors and admits a
coloring with either forbidden reachability direction absent. These
two latter colorings need not coincide; an E0 coloring is permitted.

If s->t is already present, M is unavailable in every piece because
the direct arc is a monochromatic s-to-t path when terminals agree.
Two nonempty disjoint subsets of {D,P} must then be {D} and {P}.
For t->s they are {D} and {M}. This treats the shared terminal arc
without replacing it by a digon.

The terminal-color constraints can conflict even though each side is
colorable. This classification does not itself eliminate a two-cut.

## C06.5: a forced-different nonadjacent side has a directed two-edge path

In the nonadjacent case let F be the piece with availability {D}.
Suppose F contains no directed two-edge path s->x->t or t->x->s.
Identify s and t to one vertex q. Planarity of the underlying quotient
follows by contracting ALL of an omitted component's terminal path Q
after deleting its other edges, as in C06.1.

No loop is created because st was absent. A newly created digon q<->x
would require opposite arcs incident with the two old terminals; that
is exactly one of the two excluded directed two-edge paths. Duplicate
arcs in the same direction are retained just once. The quotient is
therefore a simple planar orientation with fewer vertices than G.

Color it by minimality and pull the coloring back to F, assigning
s and t the color of q. Every original arc maps to an arc, never to a
loop or to a vanished edge. A monochromatic directed cycle in F would
map to a nonempty directed closed walk in the quotient, which contains
a directed cycle. This contradicts validity there. The pullback is a
valid equal-terminal coloring of F, contrary to availability {D}.

Thus the forced-different side contains at least one directed two-edge
terminal path. This is a necessary condition only. A directed two-edge
path alone does not force its endpoints to have different colors.

## Source and counterexample audit

Direct proof dependencies are the frozen contract and C03-C05:
research/artifacts/candidates/opg169-a01-c03-planar-blocking.md
research/artifacts/candidates/opg169-a01-c05-two-terminal.md
No new external theorem beyond basic planar minor closure is imported.
The bounded source search did not supply an exact theorem to substitute
for this interface proof. No novelty claim or current whole-problem
status is inferred from search results.

The C05 directed 4-cycle example still blocks gluing equal-terminal
colorings with opposite reachability. It does not invalidate C06:
the availability conditions concern all valid colorings, not one choice.
Identifying the endpoints of s->x->t creates a digon; C06.5 explicitly
excludes that case before applying the orientation contract.
Adding both terminal directions would create a digon even if no
undirected drawing obstruction existed; this operation is never used.
An omitted component has attachments at both terminals because of C03,
not merely because it is nonempty. Vertex identification is used only
in C06.5 after a separate orientation audit.

## Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c06-terminal-completion
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: produce a bounded core formalization candidate for the
four-distinct-neighbor argument, with explicit missing graph-semantic
bridges and a verifier handoff. The original target's complete natural-
language proof remains C01; these refinements do not close its required
verification capabilities or the root.
No mathematical program was executed and no verifier receipt is claimed.
