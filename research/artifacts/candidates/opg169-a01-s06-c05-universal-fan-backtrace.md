# S06 Cycle 5 transport recovery: universal merged-{0,2} fan backtrace

Verdict: `candidate_only`. Review status: pending.  
Candidate: `candidate:opg169-a01-s06-c05-universal-fan-backtrace`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Protected base: `dc6ee891ed7614602e88d48a57314416082dd022`  
Ongoing Issue: `#3`

## 1. Recovery scope and provenance

This packet transports the bounded S06 Cycle 4 candidate that was generated
against the protected base above but was not written to the repository in that
cycle. The supplied eighteen-file Cycle 4 archive was locally byte-audited; its
generated catalogue includes a 1.22 MiB file and is not copied as one repository
artifact. Instead, the accompanying `tar+xz+base64` multipart source capsule preserves the
exact seven replay sources. The replay regenerates the large outputs and checks
their frozen digests. The deterministic decoded source tar has SHA-256
`33c1547b9b3da243c8fcea097dcfc78f025bb4b7a9ceefbf4bfa037cb3c00dc4`,
contains seven regular files totalling 54,801 bytes before tar padding, and has
xz-stream SHA-256
`f4de48f85cb50403906bac483ce3c65fe2828eddb82bb633de63684070cf056e`.
The originally supplied full gzip archive had SHA-256
`a2ea17f4794d5746f100bd0088e152f9909b4f4dcbf5047bb92366a47d62fca4`.

The recovered material is not reclassified as Evidence. The two C++ catalogues,
the Python consumer, and this transport review all remain in the same generator
trust domain. Byte agreement and successful replay establish reproducibility of
the frozen computation only; they do not provide independent mathematical
verification, an EvidenceLink, a Result, or root closure.

## 2. Frozen local configuration and replacement contract

C37 fixes complete stars at vertices `0,2,3,7`, with degrees `5,5,5,6`, and
five surviving equality families

```text
D=(12,13), X5=(5,13), X6=(6,13), Y4=(12,4), Y5=(12,5),
```

each with 32 direction words. At the C37 interface use

```text
I={0,2,3,7},  B=V(P)-I.
rot(0)=(2,6,5,4,3),
rot(2)=(0,3,7,11,6).
```

Deleting the adjacent pair `{0,2}` merges their two closed star disks into the
actual hexagonal hole

```text
H=(3,4,5,6,11,7).
```

The main fan replacement is

```text
Q = P - {0,2} + {5->7,6->7,7->4}.
```

The three new edges are noncrossing diagonals of `H` and triangulate it as

```text
(7,3,4), (7,4,5), (7,5,6), (7,6,11).
```

For every complete valid colouring of `Q`, the required lift is a complete valid
colouring of `P` with the same colours on `B` and

```text
R_P^+(B) subseteq R_Q^+(B).
```

where `R+` contains every positive monochromatic directed path between boundary
vertices. This is the quantified condition used for arbitrary-exterior gluing;
ordinary extension alone is not substituted.

## 3. Backtrace through C39 and C38

C39 expands boundary vertex `4` to a complete degree-six star and obtains 70
compatible descendants. Moving `4` back to the boundary strengthens the lift
requirement because its colour must now be fixed. The recovered replay reports

| C39 parents | valid complete `Q` colourings | equal `R+` | strict `R+` decrease | failures |
|---:|---:|---:|---:|---:|
| 70 | 17,408 | 8,458 | 8,950 | 0 |

Hence the C39 `d(4)=6` expansion is not needed for this reduction.

C38's D/19 coordinates are obtained from C37 `D/19` by swapping labels
`12↔13`. The fan additions do not use those labels. On C37 `D/19`, with the
full C37 boundary fixed, the replay reports 168 valid `Q` colourings, 72 equal
relations, 96 strict decreases, and zero failures. The frozen twelve-vertex C38
whole-graph pressure test likewise has 90 valid `Q` colourings and zero failure
under this rule. These facts supersede only the stated local frontier; they do
not invalidate C38's negative result for its different one-point deletion and
contraction family.

## 4. Direct fan reach and the complete 160-parent merged catalogue

On the 160 signed C37 parents, the same fan is a source-valid orientation on 96
rows and succeeds on all of them. It is class-invalid on 64 rows because a desired
new arc is opposite to a parent arc; those rows are not counted as profile
failures.

The complete merged-hexagon catalogue enumerates all 215 noncrossing oriented
diagonal sets and then applies parent-specific duplicate and reverse-arc checks.
Its frozen totals are:

| quantity | count |
|---|---:|
| parent-specific candidates | 24,928 |
| successful candidates | 11,147 |
| valid complete `Q` colourings | 3,549,510 |
| equal relation lifts | 2,008,336 |
| strict relation lifts | 1,422,566 |
| failed valid inputs in rejected candidates | 118,608 |
| ordinary failures in rejected candidates | 36,272 |
| relation-only failures in rejected candidates | 82,336 |
| vacuous-`Q` candidates | 0 |

Candidate-level failures remain negative catalogue rows. Raw parent coverage is
`146 unguarded + 14 guarded-only + 0 residual`.

## 5. Geometry discharge and final selected menu

The frozen family rotations determine these complementary regions:

| family | complementary face boundaries |
|---|---|
| D | `(4,8,12,13,11,6,5)` |
| X5 | `(4,8,5)` and `(5,13,11,6)` |
| X6 | `(4,8,6,5)` and `(6,13,11)` |
| Y4 | `(4,8,12)` and `(4,11,6,5)` |
| Y5 | `(4,8,12,5)` and `(5,11,6)` |

Ten rows use `delete {0,2}; add {4→6,4→11,7→4}`. Their nominal reverse
edges `6→4` and `11→4` cannot be exterior edges in the X5/Y5 embeddings because
the endpoint pairs are not cofacial in any complementary region. This changes
the merged-disk parent coverage to `156 unguarded + 4 guarded-only`.

The four remaining rows `Y4/0`, `Y4/4`, `Y4/16`, `Y4/20` reuse C37's bare
`delete 3` rules. Their complete valid-`Q` counts are respectively
`124,150,134,162`, with zero failures. The final selected menu is therefore

```text
156 merged-{0,2} rules
  4 bare delete-3 rules
-----------------------
160 unconditional rules
  0 guarded-only
  0 residual
```

Across the selected menu the frozen totals are 21,732 valid complete `Q`
colourings, 16,536 equal lifts, 5,196 strict lifts, and zero failures.

## 6. Arbitrary exterior gluing

Let the original graph be `P∪F`, with intersection exactly `B`; completeness of
the controlled stars excludes unrecorded internal-to-exterior arcs. Take any
valid colouring of the strictly smaller `Q∪F`. The profile certificate supplies
a `P` colouring with the same boundary colours and
`R_P^+⊆R_Q^+`, while every exterior colour is left unchanged.

A newly created monochromatic directed cycle crossing the interface can be cut
at consecutive boundary visits. Replace each positive `P` segment by the
certified same-colour `Q` path. Together with the unchanged `F` segments this
creates a positive monochromatic closed walk in the already valid smaller graph;
a finite directed closed walk contains a directed cycle. Cycles wholly inside
one side were excluded separately. The replacement therefore glues against an
arbitrary exterior within the stated saturated-interface hypotheses.

## 7. Dependency and claim boundary

The candidate conclusion is limited to the exact frozen C37 `d(7)=6` J-sector,
including its C38 D/19 and C39 70-parent descendants. It depends on C37's eight
structural exclusions among the thirteen initial equality identities and on the
recorded rotations and complete stars. It does not classify `d(7)≥7`, another J
orientation, another C35 arithmetic family, the global negative-face join, or
the discharging ledger. It does not prove that every negative configuration
contains this sector.

The older C37 whole-graph obstruction remains valid for its exact family of 308
one-controlled-vertex hole replacements. The merged pair deletion is outside
that family. No failed-route record is altered by this transport.

## 8. Reproduction

Repository recovery files:

```text
opg169-a01-s06-c05-cycle4-source-capsule.json
opg169-a01-s06-c05-cycle4-source-part-00.txt ... source-part-07.txt
opg169-a01-s06-c05-cycle4-replay.py
```

Run from their directory:

```bash
python3 opg169-a01-s06-c05-cycle4-replay.py
```

The outer replay verifies the multipart capsule manifest and every numbered part, then safely reconstructs all seven replay sources in a
temporary directory, and invokes the contained bounded Cycle 4 replay. The
recorded environment was CPython 3.13.5, NetworkX 3.6.1, and g++ 14.2.0. Tool
availability and a successful rerun remain candidate-level execution facts.

```text
best_verified_result=none
best_verified_candidate=none
checkpoint_state=NONTERMINAL_CHECKPOINT
verdict=candidate_only
root_closed=false
```
