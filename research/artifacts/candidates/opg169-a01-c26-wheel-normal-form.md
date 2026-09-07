# C26: a path-and-cycles normal form for wheel-only dual certificates

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c26-wheel-normal-form
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: b0106376e8b21ad248b36ea42197053ec231cc37
Primary owner: math-proof.

## 1. Scope, hypotheses, and theorem

Fix a connected simple 2-connected sphere-embedded core R with exactly
two triangular faces A,B, BOTH marked as low-triangle patches. Every
other face is a quadrilateral marked as a one-vertex WHEEL, not a
two-vertex strip. The orientation and every patch label are fixed.

A feasible certificate is an edge set Gamma as in C25: face parity
holds, the inherited oriented primal edge-subgraph R[Gamma] is acyclic,
and every marked face passes the exact C25 patch test. Let S=Gamma*
be its selected geometric dual, omitting isolated vertices.

A,B have selected degree one. Other used dual vertices have selected
degree two or four. At a wheel, selected degree zero or four is allowed;
a degree-two adjacent pair is always allowed; an opposite pair is
forbidden precisely when its two cone triangles are directed.
The dual can have parallel edges. It has no loops because R has no
bridges. A cycle of two parallel dual edges counts as a simple cycle.

THEOREM (conditional normal form). If any feasible Gamma exists, some
feasible Gamma has selected dual S consisting of a simple A-to-B path P
and a family of vertex-disjoint simple cycles. Each cycle meets P in
exactly one vertex w, different cycles use different such vertices, and
there are no other selected edges. At w the path and cycle half-edges
alternate in the ambient degree-four rotation, so the cycle separates
A from B. The two path edges at w form a forbidden opposite wheel pair.

The family may be empty. The cycles separating A,B are linearly nested
on the sphere, taking the side containing A for each. Their number is
the cycle rank of S and the number of its selected degree-four vertices.

This theorem does NOT assert feasibility. It gives a smaller complete
normal-form search target conditional on feasibility, while retaining
primal directed acyclicity. It does not assert that a path alone suffices.

## 2. Choose a minimal certificate and remove irrelevant components

Assume a feasible certificate exists and choose one with the fewest
selected edges. The choice exists because R is finite.

C25's handshaking argument places A,B in one selected component.
Any other selected component has no odd vertex and can be deleted
in its entirety by C25: local degrees there become zero and primal
acyclicity persists. Minimality therefore makes S connected.

It is enough below to contradict minimality by producing ANY feasible
strict subset, even one whose selected dual is disconnected. Subsequent
component removal is optional and not needed for the contradiction.

## 3. Safe deletion of a selected face with no bridge on its boundary

Faces in this section are faces of S, NOT faces of the full dual.
Suppose a face f of S has no bridge of S on its boundary walk.

In a connected plane graph an edge has the same face on both sides
exactly when it is a bridge. This follows directly from a cycle through
a nonbridge edge and Jordan separation; the converse follows by deleting
a bridge and following its two sides in the same face. Hence every edge
on this boundary walk occurs once, although a vertex can occur twice.

Delete all boundary edges of f. There is at least one such edge.
No terminal A or B lies on the walk: its sole selected edge is a bridge.

At a selected degree-two vertex met by the boundary, both incident
edges are deleted, leaving degree zero. At a degree-four vertex met once,
the face uses two consecutive half-edges in the selected rotation.
All four ambient dual edges were selected, so the deleted pair is
consecutive in the AMBIENT rotation too. The complementary pair is also
consecutive; its new degree-two wheel state is allowed.

If a degree-four vertex occurs twice on the facial walk, its two visits
use disjoint pairs of its four half-edges. All four edges are then
deleted, leaving degree zero. These exhaust the possible local changes.

Thus parity, terminal degrees, and all wheel tests are preserved.
The new primal selected-edge subgraph is a subgraph of the old one,
so it is still directed acyclic. C25 then gives a feasible strict subset,
contradicting minimality.

Consequently EVERY face of S is incident with at least one bridge of S.
This is why C25's arbitrary-cycle deletion counterexample does not apply:
a general cycle need not be the bridge-free boundary of a selected face
and can leave a forbidden OPPOSITE pair at a degree-four wheel.

## 4. The bridge-component tree is a terminal path

For any bridge e of S, deleting e yields two components. On either side,
the sum of degrees in S is twice the number of internal edges plus one.
It is odd, so that side contains an odd number of odd-degree vertices.
The only odd vertices are A,B. Each side therefore contains exactly one.
Every bridge separates A from B.

Delete all bridges and contract each remaining connected component
to a vertex. The quotient is a tree; parallel edges cannot arise here
because a pair of connecting edges would not be bridges. Every edge
of this tree separates the contracted vertices containing A,B.
A tree with that property is the simple path between those vertices:
an edge off that path would separate neither terminal pair.

The terminal bridge-components are the singleton vertices A and B,
because each has degree one in S. Every other bridge-component has
exactly two incident bridges. It may be a singleton or nontrivial.
A nontrivial component Q is bridgeless: each of its edges lies on a
cycle of S, and no such cycle can use a bridge of S.

## 5. Each nontrivial bridge-component is just one cycle

Let Q be a nontrivial bridge-component. Its two incident bridges are
its only connections to the rest of S. Each of the two attached
components, together with its attaching bridge, is drawn within one
face of Q. A connected piece disjoint from Q cannot cross an edge or
vertex of Q to reach another face. Thus at most TWO faces of Q contain
any edges of S outside Q.

Any other face of Q is also a face of S, and its entire boundary consists
of nonbridge edges. Section 3 excludes such a face. Hence Q has at most
two faces. Since it is nontrivial and bridgeless, it has a cycle, and
Euler's formula gives at least two faces. It has exactly two, so
  |E(Q)| - |V(Q)| + 1 = 1.

A connected bridgeless graph of cycle rank one is a cycle. One direct
proof takes its unique cycle after adding one edge to a spanning tree;
any remaining edge would lie in a tree attached to it and be a bridge.
This proof also covers a two-edge parallel cycle. Loops are absent.

If the two incident bridges met this cycle at different vertices, each
attachment would have degree three in S (two cycle edges and one bridge).
That contradicts the even selected degree at every nonterminal.
Both bridges meet a single vertex w, where S has degree four.
Every other vertex on the cycle has selected degree two.

The two bridges must be drawn in DIFFERENT faces of this cycle;
otherwise its other face would contradict Section 3. Therefore the
cyclic order at w alternates between a path bridge and a cycle edge.
In particular each pair is opposite in the ambient quadrilateral.

The bridge-component tree is a path, so replacing each cyclic component
by its attachment vertex produces a simple A-to-B path P consisting
of the bridges and the intermediate singleton components. The omitted
cyclic components are vertex-disjoint and meet P exactly as stated.

## 6. Why a cycle cannot simply be erased in this minimal form

Consider one cycle C and its attachment w. If the two path edges at w
were an allowed wheel pair, deleting all edges of C would be safe:
the other cycle vertices go from selected degree two to zero, w goes
from four to an allowed two, and every other state is unchanged.
Parity and primal directed acyclicity would persist.

Minimality therefore implies that this opposite path pair is FORBIDDEN:
the two cone triangles over its primal boundary edges are directed.
The full degree-four state at w is allowed, but the path by itself
would not be. This gives a precise role for a potentially essential cycle.

The two bridges leave opposite sides of C. The A and B portions of the
bridge-component path have no other intersection with C, so they remain
on different sides. Thus C separates A and B. For two disjoint cycles
that both separate the same two points of the sphere, the disks
containing A are nested: disjoint Jordan curves bound disjoint or nested
regions, and the common point A rules out disjoint A-regions.
This proves the asserted linear nesting.

Each cycle has one distinct selected degree-four attachment, with no
other selected degree-four vertices. Hence the number of cycles equals
the number of such attachments. Euler or C25's degree count gives the
same cycle rank. This provides a consistency check, not an enumeration.

## 7. Exact converse and finite normalization procedure

Conversely, take any selected dual subgraph with the stated path and
vertex-disjoint attached cycles. Suppose its path/cycle rotations are
as stated, every degree-two wheel pair is allowed, and the corresponding
primal oriented edge-subgraph is acyclic. It has terminal degree one
and every other selected degree even. It therefore passes all C25
parity and patch conditions and gives an extendible core coloring.

The forbidden condition on the two path edges at each attachment is
needed for minimality, not for this sufficiency direction. Retaining
it only reduces the canonical search family and loses no feasible core.

Starting with ANY feasible certificate, a finite monotone normalization
can repeatedly remove a whole nonterminal component or a selected
face whose boundary contains no bridge. Every operation deletes an edge,
never adds one, and has the preservation proof above. A stopped
certificate is connected, every face has a bridge, and Sections 4-5
already give its path-and-cycles form. Remove any attached cycle whose
remaining path pair is allowed, and repeat normalization if necessary.
There are at most |Gamma_initial| nonempty deletion steps.

This is a proof of a finite reduction procedure given a feasible input,
not an execution report and not a procedure that finds a feasible input.

## 8. Assumption and source audit

The wheel-only hypothesis is essential in the face-deletion proof.
For a strip, an adjacent degree-two pair can be forbidden at its
distinguished majority pole. No claim for strips is obtained by silently
using the wheel argument. The two triangles must be marked so that
their selected degrees are one, not three. No other triangular faces
are allowed in this normal-form statement.

A face of S may have a repeated vertex; Section 3 explicitly treats it.
Parallel dual edges are retained. The proof never assumes a simple dual,
drops the global primal acyclicity test, or claims all cycles removable.
The full selected-face boundary, not an arbitrary closed walk modulo two,
is used for the monotone deletion.

Direct dependencies: C25's exact parity/patch equivalence and component
deletion, C16's universal wheel table, finite graph parity, planar
bridge/face facts, and Jordan separation. All new implications are
proved above. A bounded search for plane-graph forbidden transitions
and minimal planar T-joins did not identify a source theorem matching
this decorated orientation-sensitive normal form. No theorem from the
unrelated search hits is imported, and no novelty claim is made.

## 9. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c26-wheel-normal-form
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; arbitrary cycle deletion remains
excluded as a general shortcut; the admitted route is open
next_obligation: obligation:opg169-strong-min-degree-three
next_action: allow strip quadrilaterals and charge each bridge-free
undeletable selected face to its unique forbidden strip corner.
Test whether each cyclic bridge-component then has at most one
selected degree-four wheel, with all extra cycle rank paid for by strips.
No mathematical program, solver, or verifier was executed.
