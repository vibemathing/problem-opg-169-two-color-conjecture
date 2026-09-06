# Candidate C02: semidegree strengthening and the degree-four boundary

Status: proof-drafted. Verdict: candidate_only.
Candidate ID: candidate:opg169-a01-c02-semidegree-boundary
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 3c26454908e7d3ce8322159d5abdfdcf4f3415ca

## Scope and frozen conventions

The admitted target is strong connectivity and underlying minimum degree
at least 3 for a vertex-number-minimum counterexample. This candidate
explicitly STRENGTHENS its degree conclusion to at least 4; it does not
replace the target or claim that such a counterexample exists.

Use the same finite simple planar orientations, induced acyclic color
classes, and optional unused color as C01. In-neighbors and out-neighbors
are disjoint because an edge is oriented exactly once. Only the frozen
basic finite-digraph, planar-graph and finite-combinatorics axioms are used.

## C02.1: one missing neighbor color is sufficient

Let c be any valid acyclic 2-coloring of G-v. If color i is absent from
the out-neighbors of v, then assigning i to v is safe: a newly created
monochromatic directed cycle must pass through v and leave it on an
i-colored outgoing arc, which is impossible. Absence from the in-neighbors
works in the same way, by considering the arc entering v.

Consequently any such coloring extends whenever d+(v) <= 1 or d-(v) <= 1.
If v has no such neighbors, either color is absent; if there is exactly
one, select the other color. The argument does not bound the degree on
the opposite side.

In a vertex-minimum counterexample G, the induced orientation G-v remains
in the frozen class and is validly 2-colorable. Therefore, for EVERY v,
d+(v) >= 2 and d-(v) >= 2. Since G has no digons,
deg_U(v)=d+(v)+d-(v) >= 4. Together with C01's SCC argument, this implies
the admitted target and gives the explicitly stronger degree bound.

Equivalently, suppose both colors were blocked for a fixed coloring.
For each color choose an in-neighbor and an out-neighbor on its blocking
cycle. The two choices on the same side differ because their colors
differ; the two sides are disjoint by the orientation assumption. Hence
there are four distinct neighbors. This also proves that EVERY valid
coloring of G-v extends when deg_U(v) <= 3.

## C02.2: exact criticality bridge for literature comparison

Define the dichromatic number as the least number of acyclic vertex
color classes. A vertex-minimum counterexample has dichromatic number
greater than 2. Coloring G-v with two colors and assigning a fresh third
color to v gives a valid 3-coloring, so its number is exactly 3.

For any v the number of G-v is at most 2. It cannot be at most 1:
giving v a fresh second color would then color G with two colors.
Thus every G-v has number exactly 2. In particular G is vertex-critical
in the convention used in Mohar (2009), Section 2. Vertex minimality does
NOT imply that every same-order proper arc-deleted subdigraph is
2-colorable. No such stronger minimality premise is used here.

## C02.3: a six-vertex exact obstruction to fixed-color extension

This is a counterexample to the auxiliary assertion
"every valid coloring of G-v extends without recoloring when deg_U(v)=4",
NOT to the Two Color Conjecture.

Define D on the six distinct vertices v,w,a,b,c,d with exactly these arcs:
v->a, a->b, b->v, v->c, c->d, d->v,
b->c, d->a, a->w, c->w, w->b, w->d.

The underlying graph consists of the 4-cycle a-b-c-d-a, with v adjacent
to all four cycle vertices and w also adjacent to all four, and with no
v-w, a-c, or b-d edge. It is simple. For a crossing-free embedding, draw
the 4-cycle as an equator on the sphere, v in the northern hemisphere,
w in the southern hemisphere, and their incident edges as disjoint
meridian-like arcs within their respective hemispheres. Removing a point
in any face gives a plane drawing. Thus D is in the frozen graph class.

Every vertex has two in-neighbors and two out-neighbors:
v: in {b,d}, out {a,c};
w: in {a,c}, out {b,d};
a: in {v,d}, out {b,w};
b: in {a,w}, out {v,c};
c: in {v,b}, out {d,w};
d: in {c,w}, out {v,a}.
The directed 4-cycle a->b->c->d->a is strongly connected, and both v
and w have an arc into it and an arc from it. Hence D is strongly
connected. The obstruction therefore survives these necessary
conditions; it is not just an isolated source, sink, or low-degree gadget.

In D-v, take X1={a,w,b}, X2={c,d}. The full induced arc set on X1 is
{a->w,w->b,a->b}, with topological order (a,w,b). The full induced arc
set on X2 is {c->d}, with topological order (c,d). This is a valid coloring.
Assigning color 1 to v creates v->a->b->v. Assigning color 2 creates
v->c->d->v. Both colors are blocked, so this fixed coloring does not extend.

Nevertheless D itself has the valid coloring Y1={v,a,c,w}, Y2={b,d}.
The induced arcs on Y1 are v->a,v->c,a->w,c->w, consistent with order
(v,a,c,w), and Y2 has no arcs. Thus D is explicitly 2-colorable.
This distinction prevents the auxiliary failure from being mistaken
for a witness against the root conjecture.

## Verification recipe and dependency audit

Reconstruct D directly from the twelve listed arcs; compare unordered
endpoint pairs with the given embedding description; check the six
neighbor rows; check the two topological orders for D-v; check the two
directed triangles through v; then check the displayed coloring of D.
These are finite hand-auditable certificates. No program, enumeration,
SAT solver, or theorem prover was executed for this candidate.

C02.1 is a direct new-cycle argument and the deletion-heredity premise
from the frozen contract. C02.2 is only a literature bridge and is not
needed by C02.1. C02.3 uses an explicitly defined separate graph D; it
does not assume D is a minimal counterexample. The target follows from
C02.1 and C01.2, not from treating this example as non-2-colorable.

The only failure recorded here is the fixed-color degree-four extension
hypothesis. The admitted route remains viable; no failed-route ledger
entry is requested for the entire route.

## Attribution and checkpoint

Prior art: Mohar, Eigenvalues and colorings of digraphs (2009), Section 2,
Lemmas 2.1 and 2.2. The exact source comparison is in
research/artifacts/source-notes/opg169-a01-c01-sources.md at the base commit.
No novelty claim is made for semidegree-criticality observations.
The six-vertex construction and explicit colorings are fully specified
here and require no external classification theorem.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c02-semidegree-boundary
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: audit articulation gluing and the planar nonalternation
constraint for the two blocking cycles at a degree-four vertex.
No verifier receipt or Result is supplied by this proof draft.
