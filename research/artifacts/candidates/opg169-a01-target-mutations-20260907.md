# R08: finite mutation audit, prior-proof comparison, and Lean status

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-target-mutations-20260907
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 2aaa043b59c90d7c50f456ce9c11bd85d978c8ce
Primary owner: math-proof.
Companion proof: research/artifacts/candidates/opg169-a01-target-closure-20260907.md

## 1. Method and coverage

This is a hand-derived finite audit. Each listed arc set is COMPLETE:
unlisted arcs are absent. Colors of H=G-v are fixed before trying the two
colors of v. The conclusions below follow from the displayed cycles,
orders, or direct arc inspection. No graph enumeration, Lean, SAT, SMT,
or other mathematical program was run, and no execution receipt is supplied.

Except for explicitly marked loop/digon controls, these graphs are
orientations of simple planar graphs. Every ordinary fixture has at most
four vertices, and every such underlying graph is a subgraph of a plane K4
(draw a triangle and put the fourth vertex inside). Removing the unused
edges gives a drawing. Each distinguished v has zero to three neighbors.

The companion contains the exhaustive symbolic degree-0/1/2 case table
and all eight labeled degree-three direction patterns. The examples
exercise its logical boundaries; the universal proof is NOT inferred
from the number of examples or from a claimed exhaustive machine search.
"Safe" means the FULL two-class induced coloring remains acyclic.

## 2. Explicit fixtures and their expected conclusions

### M00: empty graph, empty color classes

V=empty; A=empty. The unique empty coloring has both color classes empty.
Both induced graphs have no positive cycle. This excludes an empty
minimum counterexample. There is no distinguished vertex in this fixture.

### M01: singleton and length-zero reachability (zero neighbors)

V={v}; A=empty. H is empty. Both choices c(v)=0 and c(v)=1 are valid.
v reaches itself by the length-zero path; there is no positive closed walk.
Thus this graph is strongly connected under the stated nonempty/reflexive
convention and also acyclic. Requiring a positive self-return for "strong"
would change the convention; counting the empty walk as a cycle would
wrongly reject this fixture.

Mutating the coloring requirement to "both colors must occur" rejects
this singleton. That is a different problem, not our indexed-color
partition convention. The empty-class convention is therefore explicit.

### M02: the two one-edge orientations (one neighbor)

V={v,a}; first A={a->v}, then reverse it to A={v->a}; c(a)=0.
For the first graph, the all-zero order (a,v) witnesses acyclicity;
for the second, (v,a) does. With c(v)=1 the two classes are singletons.
Hence both colors are safe in both directions. Color exchange covers
c(a)=1. No two-arc return is available in an orientation on these vertices.

### M03: source and sink, including retained neighbor edges (two neighbors)

V={v,a,b}; c(a)=c(b)=0.
Source: A={v->a,v->b,a->b}. If c(v)=0, order (v,a,b) works.
Sink: A={a->v,b->v,a->b}. If c(v)=0, order (a,b,v) works.
For c(v)=1, the zero-class is the edge a->b and v is alone.
Both choices are safe. The arc a->b is retained, not silently discarded.
The no-entry/no-exit proof also covers unequal neighbor colors.

### M04: mixed directions without a return path (two neighbors)

V={v,a,b}; A={a->v,v->b}; c(a)=c(b)=0.
Both colors are safe. For c(v)=0 use order (a,v,b); for c(v)=1 the
zero-class {a,b} is edgeless and the one-class is a singleton.
Thus same-color in/out neighbors do NOT by themselves imply blockedness.

### M05: adding one returning arc, and reversing all directions

Add b->a to M04. A={a->v,v->b,b->a}; c(a)=c(b)=0.
Color 0 is blocked by a->v->b->a. Color 1 is safe: the full zero-class
has the single arc b->a and the one-class is {v}.

Reverse all three arcs and exchange both old colors to 1:
A={v->a,b->v,a->b}; c(a)=c(b)=1.
Color 1 is blocked by b->v->a->b; color 0 is safe. This tests the OTHER
labeled mixed pattern and the correct reversal of the required path.

For the first directed triangle in vertex order (v,a,b), all normalized
colorings with c(v)=0 are:
  000: invalid (the directed triangle);
  001: valid, zero-class {v,a} has only a->v;
  010: valid, zero-class {v,b} has only v->b;
  011: valid, one-class {a,b} has only b->a.
Color complements supply the other four assignments. Exactly the two
constant assignments fail. This is a full hand classification for this
three-vertex fixture, not a program output.

### M06: unequal endpoint colors

Use A={a->v,v->b,b->a} again but c(a)=0,c(b)=1.
If c(v)=0, its zero-class has only a->v; if c(v)=1, its one-class has
only v->b. The other class is a singleton. Both choices are safe.
An underlying directed cycle exists, but it is not monochromatic.

### M07: a longer path and a wrong-color internal vertex (two neighbors)

V={v,a,b,c}; A={a->v,v->b,b->c,c->a}.
First take c(a)=c(b)=c(c)=0. The zero-class in H is the directed path
b->c->a, so H is valid. Color 0 at v creates the directed four-cycle;
color 1 is safe. Looking only for a direct b->a arc would miss this block.

Now change only c(c) to 1. H is still valid and c(a)=c(b)=0 still holds,
but the sole b-to-a path uses c of color 1. Color 0 is safe with zero-class
order (a,v,b); color 1 is safe with one-class {v,c} edgeless.
Thus the path must be wholly in the specified INDUCED color class.

### M08: degree-three boundary

V={v,a,b,c}; A={v->a,a->b,b->v,v->c}.
Set c(a)=c(b)=0,c(c)=1. H has only the arc a->b.
Color 0 at v is blocked by v->a->b->v. Color 1 is safe: zero-class
order (a,b), one-class order (v,c). The unique in-neighbor b has color 0;
choosing its opposite color is exactly the degree-three table rule.
Reversing every arc gives the unique-out-neighbor version.
This does not supply a degree-four extension rule.

### M09: true SCCs versus arbitrary acyclic pieces

Take V={a,b,v}. Start with A={a->b,b->v}, all vertices color 0.
Its SCCs are the three singletons; their condensation is a path, and
their all-zero colorings glue to an acyclic graph.

Add v->a. The old singleton partition is no longer the SCC partition;
the new graph has ONE SCC. Arbitrary pieces {a,b} and {v} are individually
acyclic in color 0, but their union contains a->b->v->a. Therefore the
gluing argument requires actual SCCs (or a separately proved acyclic
quotient), not arbitrary acyclic pieces. This also exercises the t=1
branch without using minimality to color that whole SCC.

### M10: several actual SCCs, one of them cyclic

V={a,b,c,v}; A={a->b,b->c,c->a,c->v}.
The SCCs are {a,b,c} and {v}; the condensation has one arc toward {v}.
Color a,b with 0 and c with 1. The triangle component's full zero-class
has only a->b, and its one-class is a singleton.
Either color for v glues safely; if v has color 1, c->v is retained.
The SCC may contain directed cycles, and its singleton partner has an
empty local color class; neither fact invalidates the gluing proof.

### M11: an invalid deletion coloring (zero neighbors at v)

V={v,a,b,c}; A={a->b,b->c,c->a}; c(a)=c(b)=c(c)=0.
v is isolated. The proposed coloring of H is INVALID. Both extensions
still contain the old zero-colored triangle. This is a rejected input
to the extension lemma, not a failure of that lemma and not a counterexample
to the root: for example color a,b,v with 0 and c with 1 to color G.
The premise "H is validly colored" is essential for the new-cycle
localization argument.

### M12: retaining all induced arcs and distinguishing directed acyclicity

In M05, c(v)=c(a)=c(b)=0 fails because the induced graph includes b->a.
Reporting only the selected edges a->v,v->b would report a false DAG
certificate. It is not the induced digraph on that vertex class.

Instead genuinely reverse b->a to a->b. The resulting transitive triangle
has order (a,v,b), so its all-zero coloring is valid even though the
underlying zero-class graph is a triangle. Directed acyclicity must not
be replaced by undirected foresthood or by proper coloring.

### M13: loops are outside the contract (zero OTHER neighbors)

V={v}; A={v->v}. This control permits a directed 1-cycle, contrary to C.
Both c(v)=0 and c(v)=1 fail; deleting v gives the empty valid graph.
There is no neighbor distinct from v. The source/sink degree reasoning
must not be used after ignoring the loop. We do not assign ordinary
loop-degree zero: "zero other neighbors" is only this fixture's label.
This is not an orientation of a simple graph and is not a root witness.

### M14: opposite arcs, first with one neighbor and then with two

One neighbor: V={v,a}; A={v->a,a->v}; c(a)=0.
Color 0 fails on the digon; color 1 works. Thus the "both choices safe at
degree one" assertion would fail without the orientation hypothesis.

Two neighbors: V={v,a,b}; A={v->a,a->v,v->b,b->v}.
H is edgeless. Fix c(a)=0,c(b)=1. Color 0 at v fails on v->a->v;
color 1 fails on v->b->v. Both colors really are blocked with only two
other neighbors when opposite arcs are allowed. Yet the WHOLE graph is
colorable: color v with 0 and a,b with 1. This is a failure of that fixed
extension outside C, not noncolorability of the graph.

A loopless graph on at most two vertices cannot block both colors at a
restored vertex with a valid fixed coloring: choose the color different
from its sole other vertex. Thus the latter three-vertex loopless
fixed-color obstruction has minimum order for that enlarged domain.

### M15: full noncolorability control outside the orientation domain

V={v,a,b}; both directions of all three unordered edges are present.
The underlying SIMPLE graph is K3 and planar, but this is not an
orientation of it. Every same-colored pair forms a digon.
All assignments up to color exchange, in order (v,a,b), are:
  000: digon v<->a;
  001: digon v<->a;
  010: digon v<->b;
  011: digon a<->b.
Their complements exhaust all eight assignments and also fail.
Any loopless digraph on at most two vertices is colorable with distinct
vertex colors, so this control is a minimum-order loopless counterexample
to the ENLARGED problem that permits digons. It is NOT an oriented planar
counterexample to the frozen problem or to the target theorem.

### M16: deleting noncolorability from the criticality implication

V={v,a}; A=empty. All proper induced subsets are colorable, but the
whole graph is also colorable and is not strongly connected. Its minimum
degree is zero. Consequently proper-induced colorability alone does not
imply the structure theorem. The noncolorability premise cannot be omitted.

## 3. Assumptions that cannot honestly be certified by these small tests

Planarity is needed here only to ensure the induced deletions remain in
the class on which (M) ranges. The local extension and SCC arguments
work for arbitrary orientations with the same proper-induced colorability
premise. We do not claim planarity is indispensable for those lemmas.
Parallel arcs in the same direction alone also do not invalidate the
cycle argument; the frozen simple-graph convention fixes the degree
notion and forbids loops/opposite directions.

Finiteness supplies strict cardinality decrease for proper subsets,
a minimum order in N, and finitely many SCC colorings to combine.
A finite example cannot be a mutation that violates finiteness.
Those uses are audited symbolically in the proof instead.

The minimum-counterexample assumption is not tested by pretending a small
colorable graph is a counterexample. Conditionally, from ANY hypothetical
counterexample D, adding an isolated vertex gives a larger counterexample
with degree zero and no strong connectivity. It is no longer minimum,
since D is smaller. This explains the necessity of the minimality
premise without claiming such a D has been exhibited.

The precise valid logical directions are: a valid coloring of G-v plus
degree<=2 implies an extension; contraposition is used with the SAME
domain and coloring premise. Neighbor colors without a return path are
not sufficient for blockedness, as M04 shows. The root's general coloring
assertion is nowhere assumed.

## 4. Audit of C01/C02: clarifications, not an invented mathematical repair

Fresh C01 sections C01.1-C01.4 already give the deletion, condensation,
return-path iff, and low-degree choices correctly. Fresh C02.1 correctly
derives both semidegrees>=2 and delta>=4. No false implication was found
in those direct reductions during this review.

The new standalone proof adds the details that previously relied on
conventions or brief standard facts:
- length-zero reachability versus positive cycles, nonempty strong
  connectivity, and explicit singleton/two-vertex colorings;
- why paths between vertices of an SCC stay inside its induced digraph;
- finite SCC selection, the positive-closed-walk argument, and the t=1
  case without applying minimality to G;
- the full labeled II/OO/IO/OI table and explicit two-way blockedness;
- concrete assumption mutations, with invalid-input and out-of-domain
  examples separated from genuine counterexamples.
It does not overwrite immutable C01/C02 or claim their theorem was false.
C02's degree-four octahedral fixed-color obstruction remains relevant:
nothing in the new theorem says every degree-four coloring extends.

## 5. C07/C08 Lean source status and the separation from C27

Fresh-read source identities at the base:
  C07 core: Git blob e4f176bcf027c3c66dd57f64721aa2388472ee93.
  C08 cycle-localization: Git blob 8736e3182558fe404a6e73c463d590dcd0ab778f.
  C08 scc-bridge-v2: Git blob 86a08dbbda38243c16d307ae4bf6a45b098ceb34.

C07's intended theorem is a conditional local atom from both-color
in/out neighbor witnesses, not actual cycle obstruction or full minimality.
C08 adds positive-walk localization and proposed extension proof terms.
Its selected companion uses forward-closed-cut gluing, not an SCC
condensation implementation. The companion retains a proper-induced
colorability premise; concrete finite graph/cardinality/planarity
application is still separate from that relational theorem.

Each source labels itself unexecuted. This turn supplies no fixed-version
elaboration, compiler result, axiom report, or full statement-faithfulness
receipt, and adds no new Lean source. Presence of #print axioms directives
is NOT an axiom report. The current evidence-links ledger was read empty.
The current Web profile has command_execution=false; no executable probe
or Lean run has been performed. No claim about installed binaries is made.

C27 was read: it assumes a feasible decorated dual certificate and proves
conditional normalization constraints. It is not a dependency of the
standalone target proof. This cycle neither extends that machinery nor
promotes its feasibility premise into a coloring theorem.

## 6. Source and discipline record

Repository dependencies: the canonical contract, C01/C02 direct proofs,
C01 source note, the three Lean sources above, C27 solely for scope audit,
the admitted graph, failed-route ledger, verifier registry, and current
Harness 1.2.4. All repository reads refer to the frozen base above.

Bounded external discovery on 2026-09-07:
https://www.openproblemgarden.org/category/neumann_lara_victor
https://www.sfu.ca/~mohar/Bibsci4.html
The former reproduces the orientation/simple-planar/induced-acyclic
problem statement. The author's bibliography lists Eigenvalues and
colorings of digraphs, Linear Algebra Appl. 432 (2010), 2273-2277.
C01's repository source note identifies the 2009 preprint and its
Lemmas 2.1/2.2 as prior art. This turn did not reread that PDF or reuse
either lemma as an unproved step. The standalone proof supplies the
elementary arguments directly. No novelty claim or current root-status
claim is derived from the web search.

Applicability record:
- Definitions/quantifiers: frozen; (N),(M) kept distinct.
- Witnesses: explicit color extensions; local acyclicity/cycle witnesses
  above. Minimal counterexample existence is conditional and uses
  well-ordering, not an enumeration or general coloring algorithm.
- Counterexample pressure: M00-M16 supplied; out-of-domain controls labeled.
- Invariants: full induced arcs and all old colors away from v.
- Monovariant: vertex order decreases at every use of (M); walk shortening
  decreases finite length. No unbounded process is claimed.
- Induction: no induction from sample cases; only the elementary finite
  walk-shortening/concatenation argument is needed.
- Symmetry: color complement and vertex-label exchange preserve validity;
  empty graphs and equal-color cases are treated explicitly.
- Probability/asymptotics: not applicable to this finite direct proof.
- Scale: the path iff handles arbitrary exterior size; examples alone
  make no all-orders conclusion.
- Evidence: proof-drafted and hand-derived only; trusted gates still open.

## 7. Checkpoint

readiness: RESULT_CANDIDATE_READY
verdict: candidate_only
best_verified_candidate: none
best_verified_result: none
best_candidate: candidate:opg169-a01-target-closure-20260907
natural_language_remaining_cases: []
formal_execution: not_run
formal_and_admission_remaining:
  fixed-version elaboration for a faithful full-target encoding;
  actual axiom/escape report; statement-faithfulness review;
  trusted EvidenceLink/admission under the existing acceptance policy.
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: [] in the freshly read authoritative ledger.
route_status: open
next_obligation: obligation:opg169-strong-min-degree-three
next_action: submit/review the direct proof and this audit through one
candidate-only packet/PR; record actual final-head checks and merge in
Issue #3. After transport, hand off this same target for the specified
review gates, not for another conditional C27 extension.

RESULT_CANDIDATE_READY is the user's local proof-readiness label; it is
not an admission state and does not assert that either ledger obligation
has been closed. The root conjecture is not concluded.
