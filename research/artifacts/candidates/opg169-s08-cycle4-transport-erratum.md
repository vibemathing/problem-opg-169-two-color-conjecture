# S08 Cycle 4 — transport metadata erratum

`verdict=candidate_only`; `root_closed=false`.

PR #56 used C40 commit `dc6ee891ed7614602e88d48a57314416082dd022` as the
mathematical source snapshot. Its final pre-merge base was C47 commit
`bb148946d74532ef350edd7cc8322a8dfdc26bfb`, and it squash-merged as
`13f35cd2a520babdec3e5052768b4b7ab5e63817`.

Three merged non-packet files still name the earlier C46 base
`a0b2908f88ef017d6bd58e7fb006a2c7135589ec`:

- `opg169-s08-cycle4-proof.md`;
- `opg169-s08-cycle4-executions.json`;
- `opg169-s08-cycle4-review-request.json`.

Those bytes are retained because the merged root packet binds the proof and
execution digests. Rewriting them in place would invalidate that packet.
This erratum supplies the corrected historical interpretation instead.

The stale base string does not alter any mathematical object or computation:
the five owned parents, deletion hole, replacement arcs, complete colouring
counts, reachability profiles, arbitrary-`d(8)` quantifier, nineteen facial
anchors, P12 plane witness, capsule members, and replay output are unchanged.
C47 explicitly left the C40 parent count unchanged.

The first attempted in-place correction was rejected by CI precisely because
it changed the two packet-bound digests. No mathematical failure occurred.

```text
best_verified_result: none
best_candidate_result: unchanged from the merged S08 Cycle 4 recovery
root_closed: false
```
