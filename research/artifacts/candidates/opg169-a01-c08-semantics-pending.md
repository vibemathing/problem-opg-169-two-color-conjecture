# C08 semantic audit and pending transport checkpoint

Verdict: candidate_only. Status: proof-drafted. Execution: not_run.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Root kept open: obligation:opg169-root
Candidate: candidate:opg169-a01-c08-cycle-localization
Planned base: a10b85acb45c47dd8c380b5b126e4d26bfe1ec38
Planned branch: web/attempt-opg169-a01-c08-cycle-localization
Ongoing coordination Issue: #3

## Exact intended source and theorem

Source path: research/artifacts/candidates/opg169-a01-c08-cycle-localization.lean
Principal declaration: OPG169.C08.goodExtension_of_no_four.
Source digest: pending a readable fresh fetch and exact-byte comparison.
No packet digest is invented or supplied in this checkpoint.

For a vertex type V with decidable equality, an asymmetric arc relation R,
a vertex v, and Boolean coloring c, the intended theorem says:
if c is acyclic after deletion of v and v has no four pairwise distinct
underlying neighbors, some choice of color at v extends c acyclically.
This is a local extension result. The deletion coloring is an explicit
hypothesis, not an unproved use of the planar conjecture.

## Actual cycles, rather than neighbor presence

The draft defines positive walks by an edge constructor and a join of
two positive walks. There is no empty constructor. Acyclic R means that
no vertex has a positive R-walk back to itself. Delete R v retains
exactly R-arcs with both endpoints different from v. Mono R c b retains
exactly the R-arcs whose two endpoints have color b. Good R c requires
acyclicity of each of the two induced color relations. Colors may be unused.

The ambient type still contains an isolated v after Delete. This does
not encode a decreased vertex count, but its positive walks correspond
exactly to those of the ordinary induced deletion. Recolour changes c
only at v; its old value at v is irrelevant to the deletion hypothesis.

A positive directed closed walk contains a directed cycle: expand its
finite sequence of vertices and choose equal endpoint indices with the
smallest positive difference. The intervening segment has no internal
repeated vertex, since such a repeat would have a smaller difference.
Conversely a directed cycle is a positive closed walk. This is a
natural-language semantic bridge, not a reported Lean theorem or replay.

## Delete-or-visit and localization proof

Let x,y differ from v. Induct on a positive walk from x to y. An edge
avoids v. At a join through m, if m=v the two positive pieces visit v.
If the left piece visits v, append the right piece to its tail. Otherwise
it avoids v; apply the same dichotomy to the right piece, either retaining
both or prefixing its visit with the original left piece. Thus the walk
either survives Delete R v or supplies positive walks x to v and v to y.

If Delete R v is acyclic and R has a positive closed walk at x, then R
has a positive closed walk at v. The x=v case is immediate. Otherwise
the avoid alternative contradicts deletion acyclicity. In the visit
alternative concatenate v to x with x to v, in that order.

## Failed recoloring produces the required old-color witnesses

Assume Good (Delete R v) c. Recolor v with b and suppose some color k
now has a positive closed walk. Deleting v from the new monochromatic
relation maps edge by edge into the old deleted monochromatic relation,
because the old and new colors agree everywhere outside v. Hence the
new monochromatic relation becomes acyclic on deleting v.

Localization supplies a monochromatic closed walk at v. Its first edge
is v to o and its last edge is i to v. Since v has new color b, the
walk color k equals b. Asymmetry forbids i=v and o=v, which would be
loops. Both neighbors therefore keep their old color, so c(i)=c(o)=b.

Apply this argument separately when false and true both fail. The two
in/out witnesses of one color are distinct by asymmetry. Witnesses of
different colors are distinct because false and true differ. There are
therefore four pairwise distinct neighbors. Its contrapositive gives the
intended extension theorem.

The conversion from a negated Good predicate to an explicit Bad witness
uses Classical.byContradiction in the draft. Any future axiom audit must
report the actual dependencies. No axiom report is supplied here.

## Adversarial audit

An empty-walk constructor would incorrectly make every vertex cyclic;
it is absent. A loop at v would break outside-neighbor extraction;
asymmetry excludes it. Without asymmetry a digon could make the in- and
out-neighbor coincide; the four-neighbor argument explicitly uses the
missing assumption. The initially failed color k is not assumed to be b;
localization proves equality. No surviving induced arc is discarded.

BothNeighbourColours remains only a necessary local condition for two
failed extensions. The proof never turns mere neighbor presence into a
return path. The degree-four octahedral obstruction in C02 is compatible
with this result: that vertex does have four distinct neighbors.

## What remains open

The source has not been compiled. The fixed toolchain remains quarantined
and the Web profile does not authorize mathematical commands. An Init-only
file does not waive those restrictions. The repository v4.33.0 pin is
configuration, not an observed executable version.

Formal bridges still required: positive-walk/cycle equivalence in a chosen
graph library; finite neighbor cardinality; finite planar orientation
encoding; deletion-coloring existence from vertex minimality; SCC gluing;
and assembly of the full target. The root conjecture is separate.

After authorized runtime and consumer admission, a bounded replay plan
is lean --version followed by lean on the source path above, with a
60-second wall limit, 1024 MiB memory, one CPU/thread, no network and a
65536-byte output cap. Block replay if limits cannot be enforced. This
is a plan only. The source's #print axioms directives are audit requests,
not observed outputs.

## Transport recovery checkpoint

Later tool response contents were not readable to the agent. Creation
requests were issued for the branch and source, but their resulting
commit IDs must be confirmed by fresh GitHub reads. This file itself is
also being submitted through a create request; this text does not claim
that its write succeeded. No C08 PR or valid attempt packet is claimed.

Do not infer a completed transaction, CI result or merge from this prose.
Do not fabricate SHA-256 values, receipts, HTTP statuses or run IDs.
Fresh-read main, PR #10, Issue #3 and the planned C08 branch. Verify
whether the source and this file exist. Reuse existing owned paths;
do not create duplicate Issue/branch/PR objects or overwrite a later edit.
Compute candidate digests from the actual fetched bytes before producing
exactly one schema-valid C08 packet and opening/backfilling its PR.

best_verified_result: none
best_verified_candidate: none
best_complete_target_proof: C01, with the stronger semidegree argument in C02
best_new_draft: candidate:opg169-a01-c08-cycle-localization
route_status: open
blocker: tool_response_content_unreadable; nonterminal
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: reconcile C08 actual file/branch state and SHA-256 bindings,
then complete its packet/PR/checks transaction; only afterward start the
SCC/cut-gluing formal slice from a fresh main.

Sources: the frozen canonical ProblemContract and C01/C02/C07 candidate
files in this repository. Those candidates are draft dependencies, not
EvidenceLinks. No hidden reasoning transcript or full chat is retained.
