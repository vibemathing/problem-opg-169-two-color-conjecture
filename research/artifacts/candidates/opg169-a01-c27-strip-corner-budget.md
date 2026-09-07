# C27: strip-corner charging bounds the cycle blocks of a dual certificate

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c27-strip-corner-budget
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 9607922e375491f5464d655cb79356291edfab61
Primary owner: math-proof.

## 1. Exact setting and conclusion

Retain C25's connected simple 2-connected plane core R with exactly two
triangular faces A,B, both marked as low-triangle patches. Allow every
other face to be either a one-vertex wheel or a two-vertex strip.
For every strip assume the C17 UNIQUE forbidden three-and-one partition,
with its distinguished majority pole fixed by the patch orientation.
This assumption is valid for the low-edge patches of the selected
minimum-order counterexample; it is not asserted for every oriented strip.

Use C25's exact feasible primal edge sets Gamma: face parity, directed
acyclicity of the inherited primal edge-subgraph R[Gamma], and every
patch test must all hold. Let S=Gamma* be the selected geometric dual,
with isolated vertices omitted. A,B have selected degree one; all other
used vertices have selected degree two or four. Parallel edges are
allowed. There are no dual loops because the core has no bridges.

Assume a feasible certificate exists and choose one with minimum edge
count. Then S is connected and its bridge-component tree is an A-to-B
path, as in C26. For each nontrivial bridge-component Q, let:
  t(Q) = number of strip vertices in Q of degree FOUR IN S;
  w(Q) = number of wheel vertices in Q of degree FOUR IN S;
  b(Q) = number of distinct faces of Q occupied by the two attached
         bridge sides, so b(Q) is one or two;
  beta(Q) = |E(Q)|-|V(Q)|+1.

The new bounds are
  beta(Q) = t(Q)+w(Q),
  beta(Q)+1-b(Q) <= t(Q),
and hence
  w(Q) <= b(Q)-1 <= 1,       beta(Q) <= t(Q)+1.

Thus every cyclic bridge-component contains at most one selected
four-valent WHEEL, regardless of the number of strips. If its two bridge
sides occupy one face, it has no such wheel. These are conditional
certificate constraints, not an existence proof for Gamma or for a
coloring of the full counterexample.

## 2. The only obstruction to deleting a bridge-free selected face

Let f be a face of S whose boundary walk contains no bridge of S.
Every boundary edge occurs once, although a boundary vertex may occur
twice. Neither terminal occurs, since its sole edge is a bridge.
Delete all edges on this nonempty boundary.

The degree changes are exactly those audited in C26:
- selected degree two becomes zero;
- selected degree four, one boundary visit: the two deleted edges are
  consecutive in the full four-position rotation and leave an adjacent pair;
- selected degree four, two visits: all four edges are deleted.

Every affected vertex loses an even number of edges, so parity persists.
The resulting primal edge-subgraph is a subgraph of the old one and
therefore remains directed acyclic. Degree-zero states pass both wheel
and strip tests. An adjacent degree-two wheel pair always passes.

At a strip there is exactly one forbidden adjacent pair: its primal
boundary edges meet at the distinguished majority pole. Consequently
a failure after deletion is possible ONLY at a selected degree-four
strip vertex visited once, where the pair LEFT OVER is that forbidden
pair. The pair deleted by the facial walk is the complementary adjacent
pair. It occupies the unique corner opposite the forbidden corner.

Call this an obstructing corner for f. The deletion is feasible if and
only if f has no obstructing corner. This is an exact local criterion:
all parity and primal acyclicity conditions already survive deletion,
and the patch tests just listed exhaust the remaining conditions.

No statement about an arbitrary cycle follows. Its edge pair at a
four-valent vertex need not be consecutive in the ambient rotation.
C25's arbitrary-cycle deletion witness remains applicable to that
overstrong shortcut.

## 3. An injective charging argument

A selected degree-four strip has exactly one complementary corner
that can obstruct this deletion. Every corner of an embedded graph
belongs to exactly one face, even when a face has repeated vertices.
Therefore one such strip can obstruct at most ONE face of S.

By minimality, every bridge-free face of S has an obstructing corner.
Choose one for each face. No chosen strip can be used by two faces,
because its eligible corner belongs to only one face. We obtain an
injection
  {bridge-free faces of S} -> {selected degree-four strip vertices}.

The argument counts eligible corners, not merely incidences at a face.
A strip can occur twice on a facial walk; in that case all four of
its selected edges are deleted and it is not an obstruction there.
This prevents counting a degree-four vertex twice as two available charges.

## 4. Bridge parity and the two attachment faces

C25 permits deletion of a whole selected component without a terminal.
The minimum certificate is consequently connected. For a bridge e of S,
each side of S-e has an odd sum of original degrees: internal edges
contribute twice and e contributes once. Each side thus contains an
odd number of odd vertices, and the only odd vertices are A,B.
The bridge separates A from B.

After all bridges are deleted, contract their remaining connected
components. The quotient is a tree every edge of which separates the
terminal vertices, so it is a path. A nontrivial component Q in this
path has precisely two incident bridges and is bridgeless internally:
every internal edge lies on a cycle of S, which cannot contain a bridge.
Q contains neither terminal, since terminal components are singletons.

Removing Q leaves the two bridge sides. Each is connected and meets Q
only along its attaching bridge. In a plane embedding it stays within
one face of Q. Thus they occupy either one face or two distinct faces;
this defines b(Q) in {1,2}. No side can travel through a vertex or edge
of Q into another face without creating an additional attachment.

Every other face of Q is an actual face of S, with exactly its original
boundary and no bridge on that boundary. Its obstructing corner from
Section 3 lies at a degree-four strip IN Q. Applying the injection to
these unoccupied faces gives
  f(Q)-b(Q) <= t(Q).

The inequality remains true if some occupied face also has an obstruction;
only the unoccupied faces are counted.

## 5. Degree count and the cycle-rank budget

Each vertex of Q has degree two or four in S. There are exactly two
bridge half-edges incident with Q, including the case where both attach
to the same vertex. Hence
  2|E(Q)|+2 = sum_{x in Q} degree_S(x)
            = 2|V(Q)|+2(t(Q)+w(Q)).
It follows that
  beta(Q)=|E(Q)|-|V(Q)|+1=t(Q)+w(Q).

Euler's formula for the connected plane component Q gives
  f(Q)=beta(Q)+1.
Substituting into the face-charge inequality yields
  t(Q)+w(Q)+1-b(Q) <= t(Q),
which is exactly w(Q)<=b(Q)-1.

If w(Q)=1, then b(Q)=2 and the number of unoccupied faces is t(Q).
Every one must have an obstructing selected degree-four strip, and
there are exactly t(Q) available strips. Thus each unoccupied face has
exactly one eligible obstruction, and each of these strip vertices
obstructs one unoccupied face. This equality conclusion refers only
to eligible complementary corners, not to all strip-face incidences.

If t(Q)=0, nontrivial bridgelessness gives beta(Q)>=1; the bounds force
w(Q)=1, beta(Q)=1, b(Q)=2. The component is a cycle, and C26 recovers
the opposite-side common attachment and its forbidden wheel path pair.
So the wheel-only result is a precise specialization of this budget.

With t(Q)>0 we do NOT infer that Q is a single cycle, that all such
components are nested cycles, or that the bridge attachments coincide.
Vertices with one incident bridge can have degree three INSIDE Q while
retaining even degree four in S. Confusing these two degrees would give
an invalid stronger conclusion.

## 6. Scope of a resulting search reduction

Given any feasible certificate, repeatedly delete whole nonterminal
components and any bridge-free facial boundary having no obstructing
strip corner. Every step preserves feasibility by the proofs above and
strictly decreases the selected edge count. When no step applies, the
connected certificate has the bridge-path structure and the same
strip-corner budget for each nontrivial component.

This is finite monotone normalization of a GIVEN feasible certificate.
It neither generates a feasible input nor justifies dropping global
primal directed-cycle constraints. The number of deletion steps is
bounded by the initial selected edge count; no execution is reported.

For a fixed total number of strips, the budget restricts the extra
cycle rank of each bridge-component beyond its possible one-wheel
cycle. The number of components is not bounded by this local statement;
a global constant-size search does not follow.

## 7. Assumption and source audit

The unique forbidden strip pair is essential to the injection. If a
strip could forbid two distinct adjacent pairs, it could have two
eligible complementary corners, and the charge capacity would change.
No such two-forbidden-pair variant is smuggled into the stated theorem.

Marked triangular faces must both have selected degree one. Other
triangular faces or unmarked selected degree-three vertices are outside
this two-terminal statement. Face means face of S in Sections 2-3 and
face of Q in Sections 4-5; neither means an arbitrary region of the
full dual.

Direct proof-draft dependencies, at the base:
C16 exact wheel/strip tables; C17 unique majority pole for a low edge;
C25 parity characterization and whole-component deletion; C26 selected
face deletion and bridge-component analysis. The new corner injection
and inequalities are proved here. No external theorem or computation
is imported as a substitute for these implications.

This is a candidate refinement of the admitted structural route. The
original strong-connectivity/minimum-degree target remains distinct
from the conditional two-terminal decorated-core theorem above.

## 8. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c27-strip-corner-budget
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; arbitrary cycle deletion and
uniform-choice patch shortcuts remain excluded in earlier candidates
next_obligation: obligation:opg169-strong-min-degree-three
next_action: audit the published six 38-vertex nonhamiltonian cubic plane
graphs against the residual 21-vertex triangulation from C23. A source
classification can narrow the dual candidates, but face counts and
orientation-faithfulness require actual source inspection; do not infer
that a nonhamiltonian dual yields a dichromatic counterexample.
No mathematical program, solver, or verifier was executed.
