# C23 source recovery and transport-faithfulness audit

Verdict: candidate_only. Review status: pending.
Candidate: candidate:opg169-a01-c23-source-recovery-audit
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 4666100c5996b03da8b9fe71397594215084a288
Ongoing Issue: #3
Scope: transport and existing-source comparison only; no new mathematical research.

## 1. Recovered source, not a duplicate of the merged C23 proof

The existing branch web/attempt-opg169-a01-c23-source-core-bound had
one commit beyond its merge base and no PR. Its sole extra file was:
research/artifacts/source-notes/opg169-a01-c23-finite-bounds.md
Original commit: 21c9b0bde2cfa023eb11f7767a0ad2b6ace3b6c1
Original Git blob: c1f918498ddbec2d0dd7eda0474958ac83ab71a1
UTF-8 bytes: 2981
SHA-256: d19e5472a675795142e32f366defae17087249d29275977ffdbd9a213ece5782

The file was absent from main at the base above. Its original bytes are
preserved. The existing main file used for comparison is:
research/artifacts/source-notes/opg169-a01-c23-order-bounds.md
Git blob: dd8b90cca9633622d174664be51b0336e5b8e19e
UTF-8 bytes: 2760
SHA-256: dbc19567eb64f3999085006a68ef78efa158791c44cce1f3bfaf4d9974893c04

The two texts are not byte-identical and their access statements differ.
The already merged C23 forest-compression proof is not resubmitted.
No new branch or research Issue is needed. The existing source branch
was synchronized using a two-parent commit, followed by a non-forced
fast-forward of that branch only:
d19d0f85e462a584633f8f994d24b0a3508db4c6
Parents are its old head and the current main base shown above.
No default-branch write, ref deletion, or history rewrite was performed.

## 2. Source-faithfulness comparison and unresolved provenance

Both saved notes distinguish two inputs: a bounded planar-orientation
coloring statement labelled KV26 and a bounded undirected Hamiltonicity
statement labelled HM36. Both distinguish those finite inputs from the
unbounded root and state that no source computation was replayed.
This paragraph compares saved statements; it does not reverify either
published theorem, any graph catalog, or the planar-dual bridge.

There is a material access-record discrepancy. The recovered earlier
note says that the Holton--McKay erratum's parsed text was read and
describes an added classification case. The later merged note says
the erratum entry was located but its text was not obtained.
The later note also supplies additional version and access details.

Neither saved sentence is an execution receipt. This transport turn
did not retrieve or render the external papers, replay their code,
inspect their data, or resolve which earlier access assertion was
accurate. Treat the recovered note as an archival, unverified source
candidate, read together with this caveat. Do not use its stronger
access claim as evidence of a completed erratum audit.
The discrepancy is preserved rather than silently rewriting either note.
A future source-faithfulness review must resolve it before relying on
that access history; it is not a reason to discard an undelivered file
or to claim that the root or a published theorem has been contradicted.

## 3. Earlier uncertain C08 writes already delivered

Fresh main reads confirm the selected cycle-localization source,
scc-bridge-v2 source, semantics-pending note and critical-semantics note.
Their exact UTF-8 bytes matched the returned Git blob identities, and
the source hashes match the C08 packet. They are already in merged
PR #11, merge 869d6a64d909993ab853a16a1b4ca1f98fec68b5, checked head
a705e291fa2f1b334bec9545c89d6c1f99894b75.
No C08 artifact or packet is duplicated in this recovery transaction.

The pending-write paragraphs in those frozen notes describe their old
checkpoint, not the present delivery state. The non-v2 companion is
recorded there as superseded for an extra-parenthesis error. The selected
v2 and the retained correction explanation cover that obsolete draft;
it is not reinstated as a new candidate.
Neither selected source has acquired a mathematical replay receipt by
being fetched or hashed. All unexecuted Lean and semantic bridges retain
their existing pending status.

## 4. C27 transport discrepancy corrected by actual objects

An older Issue comment claimed C27 had already merged. At the start of
this audit, actual main was 9607922e375491f5464d655cb79356291edfab61,
PR #30 was open, and its packet still had null PR fields.
The existing branch and PR were reused. Commit
60a12a49fbf38ecc985dd67bc0dbfd8072ab50f5 backfilled PR #30 and its URL.
Run 34070064759 passed all three required transport jobs; the exact
two-file diff was rechecked and PR #30 was actually squash-merged as
4666100c5996b03da8b9fe71397594215084a288. Fresh main confirmed that SHA.
Issue checkpoint 5563404037 records the correction and content hashes.
The old claimed merge SHA is not substituted for this actual receipt.

## 5. Inventory boundary and a previously recorded research lead

At the recovery base the artifact trees contain 31 candidate files,
5 source notes, and 27 packets. C01-C27 branch heads match their merged
PR heads; the extra C23 source branch is the one undelivered research
file addressed here. PR #2 is an already closed, unmerged transport
smoke, not an additional mathematical candidate needing admission.

The earlier C27 Issue checkpoint also records a proposed next step about
the h=12 residual, a 38-vertex cubic dual, facial four-cycle packing,
and short turning paths. Preserve it as an unverified research lead:
audit the claimed packing and terminal-path exclusions against actual
source data and a complete proof before using them. No completed C28
proof, enumeration, input dataset, decoded graph list, or certificate
was present in the inspected current candidate refs. This turn does not
invent such an artifact or turn the lead into a proved claim.

The accompanying transport inventory records the exact byte hashes
computed in this audit and the observed branch/PR mapping. It is an
audit snapshot, not a verifier receipt. It does not claim that every
older file's SHA-256 was independently recomputed during this turn.

## 6. Checkpoint at creation

best_verified_result: none
best_verified_candidate: none
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger read as empty
mathematical_execution: not_run
source_access_discrepancy: pending source-faithfulness review
transport_at_creation: recovered note and this audit await the sole new packet PR
next_action: bind the actual PR, require all three final-head checks,
merge under protection, then fresh-read main, refs and the unique Issue.
A final transport checkpoint must distinguish delivery completion from
the still-open mathematical obligations. No root closure is claimed.
