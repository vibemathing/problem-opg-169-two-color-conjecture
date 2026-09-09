# S06 Cycle 5 source and transport trace

Verdict: `candidate_only`. Scope: repository-source provenance and recovery
integrity; no external literature claim and no mathematical admission.

## Frozen repository sources at `dc6ee891ed7614602e88d48a57314416082dd022`

| layer | repository path | Git blob | relation |
|---|---|---|---|
| C39 | `research/artifacts/candidates/opg169-a01-c39-d4-degree6-proof.md` | `c07673e27896a87edd848c201fd154472e5bd523` | prior candidate expanded from C38 D/19 |
| C38 | `research/artifacts/candidates/opg169-a01-c38-proof.md` | `d26135ddb4be1efb3d3b5fe8a869f49bc225c6d6` | prior candidate identifying its coordinates with C37 after `12↔13` |
| C37 | `research/artifacts/candidates/opg169-a01-c37-proof.md` | `4aae213b6ad489880eca79f0f9b59cd81d8ea26f` | exact local sector and earlier 122+29+9 allocation |
| C37 input | `research/artifacts/candidates/opg169-a01-c37-input.json` | `a452f67995e1b563e364382593b887bf0ec1f63d` | exact arcs, rotations, family identities, and whole-graph witness |
| C37 audit output | `research/artifacts/candidates/opg169-a01-c37-audit-output.json` | `c91a3913803083a88982fb20545437d718c3d8e8` | prior candidate computation summary |
| C40 checker | `research/artifacts/candidates/opg169-a01-c40-check.py` | `ec5d3ffd99297c2a7d4693414466ac2fbeaefd12` | prior profile semantics and 70-parent reconstruction context |

The canonical ProblemContract digest remains
`719230edd088c52a5468eed8090579e5eef1bf85d8a56e633350063108f345ec`.
The active attempt is `attempt:web-20260906-opg169-a01`, route
`route:minimal-counterexample-structure-v1`, graph
`graph:opg169-initial-v1`, target `obligation:opg169-root`.
The authoritative failed-route ledger is empty at the recovery base.

## Recovered local object

The original supplied archive was
`s06-r08-cycle4-backtrace-c39-c38-c37.tar.gz`, SHA-256
`a2ea17f4794d5746f100bd0088e152f9909b4f4dcbf5047bb92366a47d62fca4`.
It expanded to 18 regular files and was locally byte-audited. The repository
multipart source capsule reconstructs the exact seven replay-source files; generated
outputs are regenerated and compared with frozen digests. Its deterministic
source tar has SHA-256
`33c1547b9b3da243c8fcea097dcfc78f025bb4b7a9ceefbf4bfa037cb3c00dc4`,
and its xz stream has SHA-256
`f4de48f85cb50403906bac483ce3c65fe2828eddb82bb633de63684070cf056e`.

The multipart capsule manifest checks each numbered part and each reconstructed source file separately; the replay script rejects
absolute paths, nested paths, `..`, non-regular members, duplicates, unexpected
members, size mismatches, and digest mismatches before executing anything.

## Trust ceiling

The original computations, the separate producer/consumer implementations, the
source recovery capsule, and this source comparison were all produced or reviewed in
the same ChatGPT/GitHub candidate lane. They are reproducibility and
statement-trace artifacts, not independent verification. No kernel result,
axiom audit, statement-faithfulness receipt, EvidenceLink, or Result is present.
CI, PR review, merge, and command exit status remain transport facts only.
