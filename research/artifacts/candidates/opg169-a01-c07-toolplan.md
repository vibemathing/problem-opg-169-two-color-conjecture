# C07 ToolPlan: a local four-neighbor formalization slice

Verdict: candidate_only. Output: ToolPlan with unexecuted source input.
Plan ID: candidate:opg169-a01-c07-toolplan
Source ID: candidate:opg169-a01-c07-core-source
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Target statement SHA-256: e5d7b7d2903018956d3e5c66f61cd5d33ef699e068931d2e97a13a1fbaeda4da
Base: ae1f4a5e910a048ece0a310538b947795eed88ac
Primary owner for this planning step: math-toolchain.
Proof-content owner for the admitted route: math-proof.
Formalization constraints: math-formalization.

## Frozen input and exact scope

Source: research/artifacts/candidates/opg169-a01-c07-core.lean
Source SHA-256: 13792336186770f7d3847a8d62d5d03c6d1b7f97b6e4e6b38e757514042a3624
The input is a draft, not the output of a Lean execution.

The principal intended declaration is
OPG169.C07.fourDistinct_of_bothColours.
Its hypothesis says that each Boolean color has an in-neighbor and an
out-neighbor at v, and that the arc relation is asymmetric.
Its conclusion exhibits four pairwise distinct underlying neighbors of v.

The source also isolates:
- distinct colors imply distinct vertices;
- an in-neighbor differs from an out-neighbor in an orientation;
- a neighbor differs from its center;
- the two same-side neighbor pairs are distinct even without asymmetry;
- absence of four distinct neighbors rules out the local witness pattern.

The mathematical witness order is i0,o0,i1,o1. The two within-color
inequalities use asymmetry; the four between-color inequalities use
false != true. This is the logical core of C02's stronger minimum-degree
bound. It is NOT an encoding of a complete counterexample-minimality
argument, SCC theorem, planarity theorem, or numerical degree function.

## Semantic bridge obligations, kept open

B1. Specify finite simple planar graph orientations and connect their
arc relation with the source's asymmetric relation. An arc is not an
undirected edge, and the two directions of one edge cannot both occur.

B2. Specify vertex deletion and valid acyclic vertex 2-coloring with all
induced arcs retained. Booleans represent the two colors and do not
require both colors to be used.

B3. Prove that failure of both extensions of a valid coloring of G-v
produces the source's local neighbor witnesses. This requires actual
monochromatic cycles or return paths. BothNeighbourColours is only a
NECESSARY local obstruction: it is not a definition of blocked colors.
Having both types of neighbor in a color does not assert a return path.

B4. Connect FourDistinctNeighbours with the finite neighbor-set cardinality
and with degree(U(G),v)>=4, then derive the weaker target bound >=3.

B5. Encode SCC gluing and vertex-count minimality, and combine them with
the local degree argument. The root statement is still a separate open
claim, not a consequence of checking this source file.

These labels are local bridge labels, not invented admitted Obligation IDs.
All B1-B5 remain open for the formal theorem. Their natural-language
counterparts are developed in C01/C02; that does not constitute a kernel
translation or a semantic-verifier receipt.

## Selected tool and environment gate

Chosen tool: T18, Lean 4 + mathlib.
Registry: governance/control-plane/math-tool-maturity.v1.json.
The entry has maturity verifier_admitted but operational_status quarantined.
Source pin read from fixtures/lean-proof/lean-toolchain:
leanprover/lean4:v4.33.0.

The draft imports only Init. This reduces proposed dependencies but does
not waive the registry quarantine, executable identity check, or the
Web profile's command_execution=false. No Lean executable was probed or run.
The named pin is repository configuration, not an observed runtime version.

Consumer candidate: lean-obligation-v1, subject to a matching admitted
runner and statement-binding policy. The registry's fixture policies
must not be silently generalized to this new graph proof.

Execution preconditions: an authorized runner, cleared toolchain status,
exact binary identity/version, frozen source digest, explicit consumer
admission, and a verifier identity in a different trust domain from the
generator. Until these hold the output remains this unexecuted ToolPlan.

## Planned bounded replay, not an execution record

Commands after all preconditions hold:
1. lean --version
2. lean research/artifacts/candidates/opg169-a01-c07-core.lean

Run through the admitted bounded runner: wall timeout 60 seconds, memory
limit 1024 MiB, one CPU and one worker thread, output cap 65536 bytes,
no network access, at most one informative syntax-repair retry.
Block execution if those limits cannot be enforced. Record the exact
runner-enforced limits and tool options actually used.
No .olean cache from an unknown origin may be substituted for replay.

The source includes #print axioms for each of its six theorems.
The verifier must capture actual exit status, diagnostics, imports,
declaration types, axiom dependencies and escape-audit output.
A successful run would concern ONLY the conditional local slice.
It would not close B1-B5 or supply statement faithfulness for the full target.

Failure handling: preserve diagnostics under the trusted receipt policy;
revise only a new candidate version and digest. Do not change a frozen
old packet, toolchain pin, registry, workflow, or acceptance gate.
No stdout, stderr, exit code, binary version, elapsed time or receipt
digest is supplied here because the commands have not been run.

## Required receipt separation

Kernel replay of the named declarations, axiom/escape audit, and a
statement-faithfulness review are separate requests with different scopes.
An audit must reject hidden admissions or custom axioms not authorized by
the frozen problem. Inspect declarations and imports, not just a textual
absence of suspicious tokens.

Candidate transport checks only validate files, packet bindings, digests
and write boundaries. They do not invoke the commands above.
The source's #print commands are proposed audit requests, not observed
axiom reports. No artifact in this cycle is a verifier receipt.

## Source review and limits

The fixed owner Skills, T18 registry entry, fixture pin, verifier registry,
and C01/C02 are the repository sources for this plan.

Official Lean reference, retrieved 2026-09-06:
https://lean-lang.org/doc/reference/latest/Axioms/
https://lean-lang.org/doc/reference/latest/Tactic-Proofs/Tactic-Reference/
The references describe axiom tracking and tactic behavior. They are
documentation aids, not a version lock or an execution receipt.
Requests for version-specific 4.33.0 reference pages did not resolve in
this environment. The plan does not pretend that a latest-reference URL
identifies the exact pinned binary. No external source code is copied.

## Checkpoint

execution_status: not_run
best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c07-toolplan
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: formalize a genuine cycle-extraction bridge or SCC-local
acyclicity bridge as a separate bounded source candidate; meanwhile keep
the unexecuted toolchain gate distinct from the mathematical assertions.
