# C08 companion: proper-induced criticality to the structural target

Verdict: candidate_only. Status: proof-drafted; execution: not_run.
Candidate: candidate:opg169-a01-c08-critical-semantics
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Root kept open: obligation:opg169-root
Planned base: a10b85acb45c47dd8c380b5b126e4d26bfe1ec38
Primary content owner: math-proof.

## Selected source pair, unexecuted

1. research/artifacts/candidates/opg169-a01-c08-cycle-localization.lean
2. research/artifacts/candidates/opg169-a01-c08-scc-bridge-v2.lean

Principal companion declaration: OPG169.C08Cut.critical_structure.
It proposes strong reachability and four distinct neighbors at every vertex
from arc asymmetry, failure of acyclic 2-colorability, and acyclic colorings
of all proper induced vertex subsets.

The earlier proposed opg169-a01-c08-scc-bridge.lean is NOT selected for
replay. Static review found an extra closing parenthesis in the Good
hypothesis of good_of_cut. Revision 2 corrects that binder in a new
artifact. This is a source syntax repair, not a mathematical counterexample
or failure of the admitted route. Neither version has been compiled.
The source and companion SHA-256 values require readable fresh GitHub
content and exact-byte comparison before packet construction.

## Forward-closed cut lemma

For a relation R and a vertex predicate S, suppose every R-edge starting
in S ends in S. Then any positive R-walk starting in S stays in S.
Induct on edge/join construction: the edge case is closure; at a join,
use the left induction conclusion to establish membership at the join
vertex, then apply the right induction hypothesis.

Dually, for a positive walk ending outside S, every vertex lies outside S.
The edge-level implication is contraposition of forward closure. At a
join, first propagate nonmembership backward through the right part,
then through the left. The source isolates both induction directions.

Every positive closed walk is therefore wholly inside S or wholly in
its complement, according to its initial vertex. Acyclicity of the two
induced restrictions implies acyclicity of R. No cross-edge is deleted
from the ambient relation in this conclusion.

## Gluing two acyclic colorings

Suppose a colors the induced relation on S and b colors its complement.
Define c(x)=a(x) on S and c(x)=b(x) outside S. For each color k, the new
monochromatic relation is still forward-closed on S. Its restriction to
S maps edge by edge into the old a-monochromatic relation, and its other
restriction maps into the old b-monochromatic relation. The cut lemma
rules out every new monochromatic closed walk.

This uses only TWO supplied colorings. It does not select a coloring
simultaneously for every SCC. The companion file proves strong
connectivity by this alternative cut argument; it does not purport to
implement the SCC quotient or its condensation graph. The original C01
SCC-condensation proof remains a separate natural-language derivation.

## Strong connectivity from proper-induced criticality

Define Reach R u x to allow either x=u or a positive walk u to x.
This reflexive reachability is deliberately different from the positive
walk relation used to define acyclicity.

Suppose v is not reachable from u, and set S to all vertices reachable
from u. It contains u, excludes v, and is forward-closed: append an edge
to a positive reaching walk, or use that edge when the old endpoint is u.
Both S and its complement are proper subsets. By the proper-induced
colorability premise they have acyclic 2-colorings. The preceding gluing
lemma gives an acyclic coloring of the whole graph, contradicting the
non-colorability premise. Thus every vertex reaches every other.

No asymmetry, planarity or finite cardinality is needed for this conditional
cut lemma. Those conditions enter the application of its premises to the
frozen problem, not as silently assumed properties of arbitrary relations.

## Four neighbors from the same criticality premise

For any v, the subset of vertices different from v is proper. Its supplied
coloring is exactly a Good coloring of Delete R v in the first source.
Neither recoloring at v can be Good, since either would color the whole
relation. The first source then produces the two pairs of same-color
in/out witnesses and four pairwise distinct neighbors.

The companion's final declaration conjoins strong reachability with
this four-neighbor conclusion. It does not introduce either as an axiom.
It imports the earlier source explicitly and uses its proposed proof
terms. Compilation and an axiom/escape audit remain outstanding.

## Faithfulness to the frozen finite planar statement

Let G be a counterexample of minimum vertex count in the contract class.
For every proper vertex subset S, finiteness gives |S|<|V(G)|. The induced
underlying graph is finite, simple and planar, and its inherited arcs
form an orientation. Minimality therefore supplies its acyclic coloring.
Lift that coloring arbitrarily outside S to a function on the ambient
vertex type. Outside values do not affect the restricted induced arcs.
This supplies ProperColorings for the relation encoding of G.

Arc asymmetry follows from one direction per edge of a simple graph.
The failure-of-coloring premise is exactly the counterexample assumption.
The positive-walk/cycle semantic bridge is documented in the companion
C08 semantics note. Thus the conditional structural theorem applies.

In a finite simple underlying graph, four pairwise distinct neighbors
are four distinct members of the neighbor set, giving degree at least 4,
and hence the admitted target's weaker degree-at-least-3 conclusion.
Asymmetry excludes the center itself from that neighbor set. This is an
explicit strengthening; the frozen obligation and its digest are unchanged.
The finite-cardinality and planar-encoding translations are still prose
bridges rather than declarations against an imported graph library.

The strengthened conditional structure does not exhibit a counterexample,
prove that counterexamples exist, or exclude all possible counterexamples.
The root conjecture remains open in the repository state.

## Replay staging and remaining gates

Only after authorized runtime, toolchain and consumer admission, copy the
TWO selected frozen source files into a verifier-owned capsule, preserving
bytes and their exact filenames. Do not load the earlier non-v2 companion.
The quoted import in revision 2 names the first artifact's module; it is
not an installed formal package.

Proposed commands inside that capsule:
- lean --version
- lean -o opg169-a01-c08-cycle-localization.olean opg169-a01-c08-cycle-localization.lean
- LEAN_PATH=. lean opg169-a01-c08-scc-bridge-v2.lean

The module object must be built from the frozen first source by the same
observed executable, not supplied by an unknown cache. Do not commit the
module object to the candidate branch. Enforce a total 120-second wall
limit, 1024 MiB memory, one CPU/thread, no network and 65536 output bytes.
These are proposed limits, not observed runtime measurements.

The Web profile currently does not authorize mathematical command
execution and the T18 status is quarantined. Nothing here bypasses those
gates. Compiler success, imports, axiom dependencies, classical reasoning
and statement-faithfulness must be separately audited. No outputs, run
versions, receipt digests or verification status are invented.

## Pending transport checkpoint

Tool response bodies were not readable to the agent during these creation
requests. Source, revision and note writes remain to be confirmed. No C08
packet, PR, check run or merge is asserted. This note is not a receipt.

best_verified_result: none
best_verified_candidate: none
best_new_draft: C08 source pair and structural semantic bridge
best_complete_target_proof: C01, strengthened by C02
route_status: open
blocker: tool_response_content_unreadable; nonterminal
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_action: fresh-read Issue #3, main and the C08 branch; confirm the four
selected source/note artifacts, record the earlier companion as superseded,
compute actual content digests, and complete one C08 packet/PR transaction
without modifying any protected record or gate.
