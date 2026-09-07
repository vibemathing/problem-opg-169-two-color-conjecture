# R08 degree-four audit and bounded checker handoff

Verdict: candidate_only. Status: proof-drafted; code execution pending/unverified.
Candidate: candidate:opg169-a01-degree4-audit-20260907
Base: 8f7fd4ffd8ef3c93fc1cac7bfa1f35456adf791e
Target: obligation:opg169-strong-min-degree-three
Primary owner: math-proof. Computation support is source design only.

## Direct-proof audit

C01/C02 and target-closure were reread. Their direct reductions have no
identified false implication. The new proof makes every-vertex
in/out-semidegree two its main statement. Directional witness existence
comes BEFORE forgetting directions and counting four neighbors.
Four distinct underlying neighbors alone do not imply either semidegree
bound. The new dependency chain does not infer that converse.

For each fixed deletion coloring, two blocked colors imply i0!=i1 and
o0!=o1 by different colors. Cross-side disjointness is used only to add
their cardinalities. With a unique incoming neighbor a, the only
potentially blocked color is c(a), and it blocks exactly when some
outgoing neighbor of that color has a monochromatic return path to a.
The outgoing-one version reverses the indicated path, not its colors.
This handles an arbitrarily large opposite side, not just total degree
at most three. T3 and T4 status and implication directions are separate.

## Self-contained checker design, NOT an execution report

Files:
opg169-a01-degree4-enumerator-20260907.py
opg169-a01-degree4-mutations-20260907.json

The checker does not import Lean, C01/C02, a graph library or this proof.
It constructs every labelled graph on n vertices by one ternary state
(absent, forward, reverse) for each unordered pair. Thus there are
3^(n(n-1)/2) graphs, not merely tournaments. It checks all 2^n full
colorings and all n*2^(n-1) deletion assignments, retaining both names of
the colors and including empty classes. Invalid deletion assignments
are counted and rejected as lemma inputs, not silently called extensions.

Acyclicity is decided twice: iterative indegree-zero vertex removal
and exhaustive enumeration of positive simple directed cycles. The
second oracle lists loops and digons for mutation controls, canonicalizes
only cyclic rotations, and never identifies reverse directions. The
blocker prediction uses separate BFS in the FULL induced color subset.
No prediction from the lemma is used as the direct extension oracle.

For each graph the program checks every induced subset using both
acyclicity engines; the SCC partition covers all vertices, its quotient
is a DAG, and for every full assignment global validity is equivalent
to componentwise validity. For every valid deletion assignment it
compares both color extensions with the path iff. If a semidegree is
at most one it requires some valid extension; if both fail it requires
both semidegrees at least two and four underlying neighbors.

Default requested range is n=0..4. Analytic expected graph counts are
1,1,3,27,729, total 761. Before invalid-color filtering the deletion
assignment count is 0+1+12+324+23328=23665. These are derived counting
identities, NOT observed results. The program checks such totals only
after finishing each order. Through order four all underlying graphs
are subgraphs of plane K4. Optional order five has 59049 labelled
orientations at that order, including nonplanar ones; it tests the
stronger local graph-theoretic lemma, not a planar-root enumeration.

The program hard-caps order at five and wall requests at 300 seconds,
streams one graph at a time and one bounded JSON summary, records
actual Python version and input/source SHA-256 at runtime, and saves
a last cursor on timeout. Timeout cannot return complete=true.
On a mismatch the small graph/assignment is a review candidate, not
an automatic theorem counterexample. External wall/memory/CPU/network
limits must also be enforced by the authorized runner.

No mathematical source was imported or executed in this turn. Python
text serialization, SHA-256/Git-blob hashing and ast.parse are structural
transport operations only. They do not test any graph or fixture.

## Mutation coverage and hand-derived witnesses

The JSON has 21 fixtures M00-M20. All arc lists are complete, and their
expected answers are assertions to be checked, not measured outputs.

| Fixtures | Mutation / boundary | Hand-derived result |
|---|---|---|
| M00-M01 | Empty graph, singleton, empty class, zero neighbors | Valid; no positive cycle |
| M02-M03 | One incoming / outgoing arc | Both colors safe |
| M04-M05 | Two incoming / outgoing arcs plus neighbor edge | Both colors safe by no exit / entry |
| M06 | Same-color in/out neighbors but no return | Both safe; kills neighbor-only test |
| M07-M09 | Add returning edge; reverse and complement; split colors | One block, reverse block, then no block |
| M10-M11 | Length-two return; recolor its internal vertex | First blocks 0; second permits both |
| M12-M13 | One-in-two-out and two-in-one-out | Triangle blocks 0; color 1 safe |
| M14 | Directed triangle SCC plus singleton | Component gluing valid with cross arc retained |
| M15 | Old monochromatic cycle and isolated v | Invalid deletion; checked_safe must reject |
| M16 | Loop | Outside orientation domain; both extensions fail |
| M17-M18 | One digon / two differently colored digon leaves | Domain rejection; respectively one / two blocked colors |
| M19 | Bidirected triangle | Domain rejection; all eight assignments fail |
| M20 | Two directed triangles sharing their center | Valid deletion with both colors blocked at degree four |

The executable also contains five explicitly wrong-semantics controls:
length-zero reachability mistaken for a cycle; omitting an induced arc;
replacing actual SCCs by arbitrary singleton pieces; neighbor presence
mistaken for a return path; adding in/out cardinalities despite overlap.
These use concrete minimal graphs and must distinguish correct from
wrong answers, not merely pass an empty test set.

M07's three-vertex directed cycle has six valid binary assignments:
only the two constant assignments fail. M19 has no valid assignment
because every repeated-color pair is a digon; order at most two is
colorable by distinct colors. M20 has the valid full coloring with only
the center in color 0, so it is not a root counterexample. Its four
neighbors are necessary for two blocked colors in an orientation.
Invalid deletion inputs and out-of-domain controls are never mixed into
the ordinary enumeration as counterexamples.

No finite fixture can violate finiteness. Its uses are audited in the
proof by well-ordering, strict cardinality decrease and finite SCC
selection. Planarity is used for class heredity, not to exclude a
return path. Simplicity's no-loop/no-digon parts have explicit controls;
same-direction multiplicities alone do not invalidate these local
arguments, although they change degree conventions outside the contract.

## Lean, statement-faithfulness and admission separation

Fresh sources:
C07 core blob e4f176bcf027c3c66dd57f64721aa2388472ee93;
C08 localization blob 8736e3182558fe404a6e73c463d590dcd0ab778f;
C08 cut companion blob 86a08dbbda38243c16d307ae4bf6a45b098ceb34.
All label themselves unexecuted. The fixed repository pin is
leanprover/lean4:v4.33.0, not an observed installed executable.

C07.twoInTwoOut_of_bothColours records appropriate directional witnesses,
but its predicate is not an actual cycle. C08 supplies proposed genuine
failed-extension localization. Its critical_structure theorem retains
ProperColorings and concludes strong reachability and four neighbors.
It does not by itself present the finite cardinality semidegree result.
The bridge must explicitly extract two in/out witnesses from actual
blocking cycles, apply finite cardinality, and connect ProperColorings
to finite planar vertex minimality. The ambient isolated deleted vertex
in the relation encoding must not count as a smaller vertex type.

No new or revised unelaborated Lean source is offered as a repair.
The separate request pins existing inputs, proposed commands, budgets,
expected statements, actual registered verifier IDs and required
axiom/escape and semantic checks. Their current fixture-scoped registry
entries alone do not demonstrate a target-specific execution receipt.
The current web profile has command_execution=false; user approval to
start trusted admission does not let the web generator sign receipts.

The native Lean request schema has a restricted module-name pattern,
whereas these existing source filenames use quoted hyphenated modules.
The request is honestly a staged preparation/replay request, not a
pretended runnable schema-valid full-target Lean capsule. Any staging
wrapper, concrete full-target encoding and changed import must be
frozen and reviewed by the trusted runner before native adapter use.

T3 remains the admitted statement, with the old target-closure candidate.
T4 has its own new candidate identity and implies T3, but no new
obligation record is written. A stronger-result admission requires a
trusted explicit statement binding; T3 evidence cannot silently be
relabelled T4. Root admission is excluded from this necessary-condition
request. No graph enumeration verifier of matching scope is registered
here; request scope admission instead of borrowing a fixture verifier ID.

Attribution: the repository C01 source note identifies Mohar's preprint
as prior art. The author's bibliography was checked for the publication
metadata (Eigenvalues and colorings of digraphs, LAA 432 (2010), 2273-2277):
https://www.sfu.ca/~mohar/Bibsci4.html
No PDF or its theorem proof was reread this turn; no external lemma is
an unproved dependency of the direct argument and no novelty is claimed.

readiness: RESULT_CANDIDATE_READY / min-degree-four-necessary-condition
natural_language_remaining_cases: []
enumerator_run: pending/unverified
Lean_run: not_run
admission_request: pending trusted scope and execution
best_verified_candidate: none
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
