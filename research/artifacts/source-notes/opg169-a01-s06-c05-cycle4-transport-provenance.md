# S06 Cycle 5 transport-provenance note

Verdict: `candidate_only`. This is a provenance and scope record, not mathematical Evidence.

## Recovered object

The recovered local object was named

```text
s06-r08-cycle4-backtrace-c39-c38-c37.tar.gz
```

with recorded SHA-256

```text
a2ea17f4794d5746f100bd0088e152f9909b4f4dcbf5047bb92366a47d62fca4
```

The prior foreground computation reported an 18-file manifest check and a successful replay of the frozen C37/C38/C39 summaries. The execution belonged to the same generator domain as the candidate. It is not an independent verifier receipt and is not entered under `research/artifacts/receipts/`.

## Why the complete archive is not copied into this PR

The local package contains a catalogue TSV larger than the Web channel's 1 MiB per-file limit. An interrupted recovery attempt prepared multipart blobs, but those blobs were never bound to repository paths or a commit. Reusing unnamed, unreferenced blob SHAs would make path-to-content provenance ambiguous. This recovery therefore does not attach them and does not claim that the complete archive is present in GitHub.

The PR instead preserves:

- a readable statement of the exact replacement, interfaces, counts, scope and non-claims;
- a compact machine-readable summary of the frozen totals;
- a static consistency replay that checks the summary but expressly does not regenerate the catalogue;
- this provenance note;
- a Web packet whose registered artifact is only a transport marker with a known exact digest.

The full local archive remains identifiable by name and digest. Independent review should obtain the archive through an explicit file-transfer channel, verify its manifest, rerun the actual enumerators, and compare the regenerated row stream with the recorded catalogue-output digest

```text
dd215e43d05e9cbe529d86afcf903f94b96eac879be85fdd7fd5ccf4da98fc8c.
```

## Repository dependencies traced

The candidate is a refinement of repository candidate material at protected base `dc6ee891ed7614602e88d48a57314416082dd022`:

- `research/artifacts/candidates/opg169-a01-c37-proof.md` and its frozen input/checker;
- `research/artifacts/candidates/opg169-a01-c38-proof.md` and replay capsule;
- `research/artifacts/candidates/opg169-a01-c39-d4-degree6-proof.md` and checker;
- `research/artifacts/candidates/opg169-a01-c40-proof.md` and compact rule manifest.

The recovered report does not overwrite or retroactively change those files. It states that a larger two-adjacent-star replacement lies outside the old one-point-hole search families.

## Verification request

A suitable independent verifier should check, from frozen explicit arcs and rotations:

1. the merged `{0,2}` hole and every added diagonal are geometrically valid;
2. aliases and existing/reverse arcs are handled before any profile test;
3. every complete valid smaller colouring is quantified;
4. ordinary extension and full positive-reachability containment are separated;
5. ten claimed guard eliminations follow from actual complementary-face incidence;
6. the four reused `Y4` bare deletions match the committed C37 inputs;
7. the selected 160-parent menu has no vacuous-Q or non-strict-order case.

Until such a receipt exists, all statements remain `candidate_only`; `root_closed=false`.
