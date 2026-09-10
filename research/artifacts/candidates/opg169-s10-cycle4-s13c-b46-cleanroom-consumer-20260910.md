# S10 Cycle 4 — clean-room source gate for S13-C exact Bcrit rows

**Verdict:** `candidate_only`  
**Repository:** `vibemathing/problem-opg-169-two-color-conjecture`  
**Frozen protected main:** `61aa9f65e0be9b00205ed0e57c7c9a5c5917f96c`  
**Target:** `obligation:opg169-root`  
**Expected mission scope:** 46 exact S13-C Bcrit rows.

This is an S10 clean-room consumer audit. It does not use the S13 producer checker,
producer consumer, producer row classifier, producer lift vectors, or producer
helper functions. The source gate is evaluated before any mathematical row
verification.

## 1. Fresh source result

Fresh protected `main`, recent branches/PRs and the current S01 Cycle-6 source
audit contain no repository-bound S13-C `4300/B46` artifact or packet. S01
Cycle 6 explicitly records S13-C `4300/B46` as source-required/unconsumed.

The only repository object found that could plausibly carry the historical
Cycle-4 row material is open PR #54, the S13 Cycle-5 transport recovery at head

`e68936730ed8b28469b568d4958cf569cd1ac078`.

Its manifest identifies a 44,349-byte ZIP and, inside it, a 116,758-byte
`r08_s13_cycle4_registry.json` plus a 57,827-byte
`r08_s13_cycle4_source_states.json`. Those are suitable kinds of inputs for a
clean-room consumer only if the transport bytes first pass their own exact
manifest.

They do not.

## 2. Exact transport falsifier

The repository-bound unpacker reads each chunk as raw bytes, requires its raw
SHA-256 to match, decodes ASCII, applies `.strip()`, then requires the stripped
length to equal `chars_without_newline`.

The PR #54 manifest requires each of the four chunks to have

`chars_without_newline = 14783`.

For `opg169-a01-s13-c05-cycle4-capsule-part01.txt`, the Git blob is
`1ebfc1ba59f4ca7f099b23990d123e0cb642b8b5`. Direct blob slicing shows the
actual file has 14,783 raw bytes and its final byte is LF (`0x0a`).

Therefore the raw file ends in a newline. After the unpacker's `.strip()`, the
chunk has at most 14,782 characters, contradicting the manifest requirement
14,783. The recovery unpacker must fail before the four chunks can be accepted
as the advertised archive.

This is independent of the producer's mathematical checker. It is a
repository-byte / manifest contradiction.

PR #54 also has no successful final candidate gate at its current head:
`web-pr-diff-boundary` failed and `web-attempt-packet` failed (the harness
snapshot job passed). Those transport failures are not mathematical evidence,
but they remove any basis for treating #54 as a completed admitted source
transaction.

## 3. Consequence for the 46 requested rows

S10 cannot source-faithfully recover the exact S13-C row identities or their
full row payload from the current repository state. In particular S10 cannot
verify, for any alleged Bcrit row:

- exact row/source digest and parent identity;
- the actual B-criticality statement and its quantifiers;
- alias normalization and plane rotation before geometry;
- complete stars and complete exterior-contact ownership;
- simple-orientation / planarity / reverse-guard / strict-descent premises;
- nonvacuous complete valid-Q quantification, where a reduction row actually
  invokes minimality;
- same-boundary lifts and both-colour positive `R+` containment, where the row
  actually invokes LIFT-O;
- or any different B-criticality-specific certificate fields that the missing
  exact registry may require.

The phrase “46 exact Bcrit rows” supplied by the mission fixes only the expected
cardinality. It does not supply the source row IDs, geometry, theorem
statements, certificates, or ownership data.

Hence the exact consumer disposition is

```text
expected_row_slots = 46
source_row_ids_recovered = 0
mathematically_consumed_rows = 0
PASS = 0
FAIL = 0
NOT_VERIFIABLE_CORRUPT_TRANSPORT = 46
```

Ordinal audit slots `1..46` are all assigned this source-blocked disposition;
none of those ordinals is claimed to be an S13 source row identifier.

## 4. Why S10 does not repair the missing byte

Guessing whether the manifest count is wrong, a chunk newline was added, or a
base64 character was lost would create a new source not present in the
repository. Even if one guessed archive happened to unzip, its registry bytes
would not be identity-equivalent to the promised member digest unless the
entire chain were re-established.

Likewise, using `r08_s13_cycle4_checker.py`,
`r08_s13_cycle4_consumer.py`, `r08_s13_cycle4_check_report.json` or a producer
summary to reconstruct the 46 rows would violate this lane's clean-room
contract and could silently inherit the producer's row-selection or ownership
bugs.

## 5. Minimal source repair that reopens verification

Any one of the following is sufficient to reopen, but not automatically pass,
the 46-row audit:

1. publish the exact plain `r08_s13_cycle4_registry.json` and
   `r08_s13_cycle4_source_states.json` as repository files with SHA-256 equal
   to the frozen manifest values
   `44afadb72d1a8bb6d2b148e4acf6051c9a4bba355119f8d1ab8353741f6a0498`
   and
   `47d3e97f5d2810eb40cddf126570cb430a9aa145a528dcb0e91082cd1718c836`;
   or
2. repair the four text chunks and manifest in a new candidate transaction so
   the frozen unpacker reconstructs the advertised ZIP SHA-256
   `407358260e8b690af86c20b951543e9ce8dc6eaee55d545b6b6619577f19d9eb`,
   all 15 member hashes match, and the transaction passes the repository
   candidate gates.

After that, S10 should build a new checker from the registry/source-state
specification and evaluate the exact 46 rows without importing producer code
or saved lifts.

## 6. Trust boundary and nonclaims

The transport falsifier is source-admission information, not a mathematical
counterexample and not a failed route for B-criticality. No Bcrit row is
declared false. No B-criticality theorem, S13-C `4300/B46` theorem, GSRC/JREL
join, LIFT-BIND, trusted verifier receipt, EvidenceLink, Result, Solution, or
root closure is claimed.

```text
S13C_B46_SOURCE_BINDING: NOT_VERIFIABLE_CORRUPT_TRANSPORT
S13C_B46_EXPECTED_ROWS: 46
S13C_B46_CONSUMED_ROWS: 0
S13C_B46_PASS: 0
S13C_B46_FAIL: 0
S13C_B46_SOURCE_BLOCKED: 46
root_closed: false
```