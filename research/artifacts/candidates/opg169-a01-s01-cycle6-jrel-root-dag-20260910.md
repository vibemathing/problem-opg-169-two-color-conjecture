# R08 S01 Cycle 6 — choice-free JREL root DAG and row-level cut matrix

Verdict: `candidate_only`. `best_verified_result=none`. `root_closed=false`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected `main` consumed: `61aa9f65e0be9b00205ed0e57c7c9a5c5917f96c`.

This S01 checkpoint rewrites the sole live root proof around actual-face join records rather than selectors or finite atlases. It consumes only repository-identity-bound outputs. It creates no EvidenceLink, Result, Solution, trusted-verifier receipt, or root closure.

## 1. Root theorem skeleton

The sole root route is now

```text
D0
 -> LowCorners relation
 -> JREL-SOUND + JREL-TOTAL
 -> JCLOSE-EC
 -> Sigma-mu contradiction.
```

`JUNIQ` and exact-one source-cut (`SCUT`) are optional normalization theorems, not logical root gates.

The point of this rewrite is to separate three statements which prior finite catalogues can easily conflate:

1. an arithmetic or local source **cover** exists;
2. an exact embedded source row has an exhaustive local certificate;
3. the same actual negative face in the assumed minimum counterexample is joined to that exact row.

Only (3), followed by closure, can discharge the root occurrence obligation.

## 2. D0 and the charge-side entrance

Use the current C34/C35 double-payment ledger:

```text
gamma(v) = (d(v)-4-2t(v))/d(v),
mu(f) = |f|-4 + sum_{v in f} gamma(v) + h(f).
```

Each donor pays the recorded pair units on both incident faces and pays its remaining `gamma` at every corner. The candidate bookkeeping keeps total final charge

```text
sum_f mu(f) = -8.
```

Length-at-least-four faces are nonnegative in the C48 source package. Hence the current candidate discharging route forces an unpaid negative triangular face. Define

```text
D0(f) :<=> f is an actual unpaid triangular face of the assumed
           vertex-minimum counterexample and mu(f)<0.
```

The final contradiction must never be described as a local reduction numerically adding charge to the original graph. The logic is instead:

```text
Sigma mu = -8
 -> some D0(f) exists
 -> every actual D0(f) is impossible by the join/closure theorem
 -> contradiction.
```

Thus the final charge step requires complete source-faithful elimination of actual `D0` faces, not another transfer rule.

## 3. LowCorners is a relation, not a selected branch

For a corner `p` of an actual `D0(f)`, retain C48 notation

```text
d(p)=3t(p)+s(p),
Low(f,p) :<=> p in V(f) and s(p)<=5.
```

C48 gives the candidate relation

```text
D0(f) -> exists p Low(f,p).
```

For a fixed low corner, exactly one arithmetic tag holds:

```text
F:  t(p)<=5,
SG: t(p)>=6.
```

On SG there can be several singleton gaps. None of this supplies a unique corner, a unique gap, a unique source state, or a source occurrence theorem.

Cycle 6 therefore keeps the full relation

```text
LowCorners(f) = {p : Low(f,p)}
```

and uses ordinary existential elimination. A root theorem may close uniformly for all low-corner descriptions, or close every actual join generated from them. No global choice function is needed.

## 4. JREL: actual same-face join records

`JREL` is S01 integration notation. It does not rename an unbound specialist theorem.

A join record `j` for `(f,p)` must contain at least:

```text
face_id             the same actual D0 face f,
corner_id           p in LowCorners(f),
optional_gap_id     if an SG construction uses a singleton gap,
actual_vertices/arcs,
actual rotations and faces,
alias quotient before geometry,
complete controlled stars,
all patch/exterior contacts,
edge and face ownership,
source/payer identity,
exact source-row locator,
source-row digest or immutable repository identity,
any reverse-arc guards,
class/source tags used downstream.
```

Write `JREL(f,p,j)` when this exact record is source-valid.

### JREL-SOUND

Every accepted join must be about the same root object:

```text
JREL(f,p,j)
 -> D0(f)
    and p in LowCorners(f)
    and face(j)=f
    and payer/source ownership in j is the ownership of f's actual graph.
```

In particular JREL-SOUND forbids:

- replacing `f` by a different convenient negative face;
- borrowing a row from another root or another planar realization;
- turning arithmetic admissibility into occurrence;
- turning a finite atlas into occurrence;
- dropping an alias, star, rotation, ownership edge, or exterior contact;
- using an alternative root without creating a new explicit `D0` record and proving the new root connection.

This same-face rule is part of the S01 safety contract independently of whether a separately labelled S13-D or S15 artifact is repository-bound.

### JREL-TOTAL

Choice-free totality is

```text
forall f,p:
  D0(f) and Low(f,p)
  -> exists j JREL(f,p,j).
```

A weaker existential-on-one-corner theorem could also close the root if it explicitly proves that its construction applies to at least one low corner of every actual `D0`; no such weakening may be inferred from a finite atlas. The live root target is the uniform relation above because it avoids an unproved selector.

An empty JREL relation cannot satisfy the root by vacuity.

### JUNIQ is optional

`JUNIQ` would say that one normalized source identity represents each relevant join. It is useful for canonical IDs, payer injectivity if separately needed, and computation deduplication. It is not required when every actual join is sound and every generated join is closed.

Duplicate join records may coexist.

## 5. Three certificate levels

Cycle 6 records source status in three distinct levels.

```text
COVER-ONLY
  arithmetic/local atlas or finite class list;
  no occurrence implication.

ROW-CERTIFIED
  exact embedded source row with its own colouring/reduction certificate;
  still conditional on occurrence of that source row.

ACTUAL-JOIN-CERTIFIED
  a JREL record binding the same actual D0 face in the assumed
  minimum counterexample to a ROW-CERTIFIED source.
```

Current repository-bound finite libraries such as C48's 26 cells / selected-gap 192 atlas and C37 R160 do not by themselves reach `ACTUAL-JOIN-CERTIFIED`.

At the fresh Cycle-6 read, no repository-bound theorem provides a root-wide actual-join record for every `D0` low corner. This is the first root cut.

## 6. JCLOSE-EC: exhaustive-colouring closure of an actual join

`EC` means **exhaustive complete-colouring closure** in this S01 notation.

For an actual join record `j`, `JCLOSE-EC(j)` requires that every complete colouring obligation arising from the exact source row be covered by at least one source-valid closure lane, with all quantifiers and ownership attached to the same `j`.

The allowed lanes are:

```text
STRUCT(j)  source-bound structural contradiction;
L_A(j)     direct strict reduction / all-extend lane;
L_B(j)     blocker/critical lane closed to contradiction or reduction;
ESC(j)     explicit recursive/source escape with proven useful progress.
```

The classes need not be mutually exclusive. Exact-one SCUT is optional. What is mandatory is that every obligation that can actually arise is closed.

Formally, a sufficient choice-free root condition is

```text
forall f,p,j:
  D0(f) and Low(f,p) and JREL(f,p,j)
  -> JCLOSE-EC(j).
```

Together with JREL-TOTAL this contradicts the existence of `D0`.

## 7. What remains for L_A

`L_A(j)` is not merely "a smaller picture was found". For an actual join it still requires all of:

1. **actual source binding**: `j` identifies the exact source row for the same `D0(f)`;
2. **strict replacement**: a finite simple planar orientation in the frozen root class with strictly fewer vertices;
3. **alias/geometry fidelity**: aliases normalized before geometry; actual hole/boundary and rotations fixed;
4. **ownership completeness**: every interior-to-exterior contact and every shared boundary edge is assigned consistently;
5. **guard validity**: no reverse arc, duplicate edge, hidden controlled adjacency, or unrecorded contact invalidates the row;
6. **complete-Q quantifier**: every valid complete colouring of the smaller patch/whole graph in the stated row domain is included, with nonvacuity;
7. **lift**: a same-boundary valid original colouring exists for every valid Q colouring;
8. **positive reachability**: both colours satisfy `R_P^+ subseteq R_Q^+`, unless a source-bound complete-tournament specialization really applies;
9. **whole-exterior use**: the row is licensed by the generic LIFT-O theorem or an equivalent exact gluing theorem;
10. **admission**: trusted replay/statement faithfulness remains separate from candidate theorem content.

Repository-bound C35/C36/C37 rows are valuable `ROW-CERTIFIED` examples/libraries. They do not establish JREL-TOTAL.

The exact C37 `d(7)=6` R160 library remains especially strong after source identity: 160 exact rows are candidate-reducible. S09 Cycle 4 proves that this library must not be inverted into a source-occurrence existential.

## 8. What remains for L_B

`L_B(j)` is the blocker/critical closure lane. It needs:

1. an identity-bound exact B-source row attached to `j`;
2. a source-bound exhaustive complete-colouring split for that row;
3. exact blocker witnesses, not a boundary-only proxy;
4. a proof that every blocker outcome produces a structural contradiction, a strict `L_A`-grade reduction, or an explicit source-bound recursive escape;
5. closure of every nonblocker/all-extend obligation with the same ownership and lifting quantifiers;
6. if a criticality lemma is used, its path-disjointness/topology/payer premises must be actual source facts, not abstract possibilities;
7. trusted lifting/admission remains separate.

No root-wide B-criticality theorem is identity-bound on fresh main.

A requested S12-A numerical package is described as 784 exact ALL-colouring obligations split into 578 blocker and 206 all-extend. Fresh repository/PR/branch/Issue searches found no identity-bound S12-A artifact, packet, source-row map, or digest for that package. Therefore Cycle 6 does **not** consume those counts as mathematics. They are recorded only as a requested-unbound input. If later source-bound, their correct insertion point is `L_B/JCLOSE-EC` **after** the package maps each obligation to an exact actual JREL source row; the counts cannot establish JREL occurrence or totality. The number `578` is not identified with C35's unrelated retained-colouring mask 578 without an explicit source record.

## 9. Requested S13-C / S13-D / S15 material: source gate

The user-requested S13-C package is described as a C35 4300 split with a B46 frontier. Fresh protected-main code search, PR search, branch search and Issue #3 search found no identity-bound artifact or packet for those numbers. The only visible S13 global-registry branch remains at old revision `13f35cd2a520babdec3e5052768b4b7ab5e63817`, before the Cycle-5 root rewrite.

Therefore:

```text
S13-C 4300 split          REQUESTED / NOT SOURCE-BOUND
S13-C B46 frontier        REQUESTED / NOT SOURCE-BOUND
```

They are not inserted into JREL, JCLOSE-EC, `L_A`, or `L_B` until an immutable source artifact identifies the exact C35 rows, actual face/source provenance and all-colouring semantics. In particular no occurrence is inferred from C35's finite parameter scans or its exact local examples.

The requested S13-D/S15 cautions about same-face provenance and alternative roots likewise have no identity-bound repository artifact at this read. They are not credited as imported specialist theorems. Their safety content is nevertheless enforced independently by S01's JREL-SOUND definition: the join must use the same actual face; an alternative root requires a new explicit root/source record.

## 10. S11 PR #83: transport only

PR #83 carries

```text
research/artifacts/candidates/opg169-a01-s11-cycle5-concrete-bridge.lean
SHA-256 103540b75a35c3de18e79d8cc45f4c54efba39c73ce9fc5601ac1dc8852fc2fe
```

but at this Cycle-6 read it is open and draft, not merged, and explicitly reports

```text
kernel_checked=false.
```

The source imports `Init` only and has a static scan with no `sorry`, `admit`, `axiom`, or `unsafe`, but no real Lean kernel replay or axiom report has occurred. Hence PR #83 is transport-only and contributes no verification or Evidence.

The generic LIFT-O mathematical content from the merged S10 consumer remains `PASS(candidate theorem content)`. It is not promoted by the presence of the Lean file.

### Lifting admission still missing

For root use we still need two separate layers:

```text
LIFT-BIND
  row-level exact alias/boundary/contact/ownership/guard/descent binding;

LIFT-VERIFY
  real pinned replay/axiom audit/statement-faithfulness/trusted admission.
```

A real kernel replay of the exact PR #83 source may contribute to `LIFT-VERIFY`; transport, static scanning and GitHub CI cannot.

## 11. S04 remains repository-bound STANDBY

S04 has repository specialist identity artifact

```text
research/artifacts/candidates/opg169-a01-s04-cycle6-artifact-identity.json
SHA-256 89a2a4e26b9108907e8fe88a7918330e4c8dcca4ba4b4da27d831152d6a93e53.
```

Its disposition is `STANDBY`, with `mathematical_content_promotion=none`.

The substantive two-hole ownership content remains C43/C47/S10:

```text
H13=(7,8,16,12),
H14=(8,15,12,17),
vertex intersection {8,12},
edge intersection empty,
8->12 exterior in the unabsorbed decomposition.
```

The lobes form a vertex-only two-terminal interface, not a common `K2` tournament. Full positive two-terminal reachability and exact ownership remain required. C47's 8,136 failures stay restricted to delete `{13,14}` plus at most one new nonisolated internal vertex total. S04 adds no new theorem in Cycle 6.

## 12. New identity-bound substantive delta: S02-B Cycle 3

Fresh main contains merged PR #86, S02-B Cycle 3 terminal-usefulness lower bound.

Frozen candidate identities include:

```text
proof SHA-256
9d586e7ae6abb04a823b9165462d0799c68bc931e49ee2dff7bc71030f1d2bbd

checker SHA-256
ccfaf917f11df1d146ca28f99d314601a5bc76643d9faddc2d178514b0a88fcc

output SHA-256
f66a8f3c51a6b9571d6ca51eda0a57a883ca57af056566808650a48103f6d504.
```

For every even `N>=6`, the explicit root-class family `T_N` is a simple plane triangulation with minimum semidegree at least two, unbounded pole degree, no separating triangles, and a monotone complete-star exposure with growing interface. Every consecutive exposed A-star block of size 1, 2 or 3 has no strict same-boundary ordinary-extension replacement; the exhaustive finite candidate total across both parities is 9,558,600.

Exact scope:

- `T_N` is root-class stress only;
- it is not an exact C37 higher-degree source;
- it is not LSRC, GSRC or a JREL actual join;
- it is not a root counterexample.

Effect on Cycle 6: an escape/recursive branch cannot prove `JCLOSE-EC` merely from well-founded discovery plus separating-triangle decomposition plus local same-boundary reductions on at most three consecutive exposed stars. Any universal bounded-cluster usefulness theorem of that form must use block size at least four, or genuinely nonlocal/source-specific information.

Thus `TPROG` remains open and is strictly stronger than source-discovery termination.

## 13. Row-level dependency / cut matrix

Status vocabulary:

```text
PASS-CANDIDATE  repository-bound candidate statement in exact stated scope;
ROW-CERTIFIED   exact source row/library with local closure certificate;
ACTUAL-JOIN     same actual D0 face is source-bound to that row;
COVER-ONLY      finite/arithmetic/local cover, no occurrence implication;
SOURCE-REQUIRED requested result has no repository identity at fresh read;
OPEN            mathematical bridge still missing.
```

| Row | Dependency / intended edge | Identity-bound source | Certificate level | First missing actual source record / cut | Cycle-6 disposition |
|---|---|---|---|---|---|
| R0 | `Sigma mu=-8 -> exists D0` | C34/C35/C48 | PASS-CANDIDATE ledger | trusted/admitted ledger still absent; candidate route has D0 localization | candidate entrance |
| R1 | `D0(f) -> LowCorners(f) nonempty` | C48 + S01 C4/C5 semantics | COVER-ONLY arithmetic relation | none for arithmetic statement; geometry not implied | PASS-CANDIDATE arithmetic |
| R2-F | low F corner -> actual source join | C48 26-cell list only | COVER-ONLY | **actual same-face F join record with rotations, stars, aliases, ownership and source locator** | OPEN; first root cut |
| R2-SG | low SG corner/gap -> actual source join | C48 selected-gap 3-interface/192 atlas | COVER-ONLY | **actual same-face `(f,p,g)` join record**; 192 cannot imply occurrence | OPEN; first root cut |
| R3 | `JREL-SOUND` | S01 integration contract + source-owned rows | logical contract | each producer must emit immutable actual face/source/payer record | OPEN globally |
| R4 | `JREL-TOTAL` | none root-wide | none | at least one actual join for every required low-corner description; no atlas inversion | OPEN, highest priority |
| C35-d5 | exact saturated six-port degree-five core | C35 proof/input | ROW-CERTIFIED: 64 complete boundary lifts + arbitrary-exterior deletion for exact core | **same actual D0 face -> exact C35 core JREL record** | row certified, root occurrence OPEN |
| C36-J5 | selected C35/C36 J, `d(7)=5` exact rows | C36 source chain | ROW-CERTIFIED candidate reductions | **actual selected-J occurrence record for same D0** | conditional closure only |
| C37-R160 | selected J, exact `d(7)=6` | C37/S06/S09/S10 | ROW-CERTIFIED 160-row library | **actual selected-J JREL record**; R160 cannot provide it | equality kill after join |
| J-high | selected J in minimum counterexample -> `d(7)>=7` | S09 Cycle 4 | conditional source consequence | actual selected-J occurrence, then source-specific high-port closure | OPEN escape |
| S02B-C3 | generic terminal usefulness stress | S02-B Cycle 3 / PR #86 | ROW-CERTIFIED root-class counterpressure, not join | a source-specific theorem excluding stress family or a usefulness mechanism with block>=4/nonlocal | TPROG OPEN |
| 2TERM | corrected two-hole ownership `{8,12}` | C43/C47/S10; S04 identity bound | ROW-CERTIFIED ownership contract; C47 bounded negative catalogue | actual JREL/source row reaching this interface and any positive closure theorem | S04 STANDBY; no root join |
| S12-A | requested 784 = 578 blocker + 206 all-extend | **no identity-bound repository artifact found** | SOURCE-REQUIRED | S12-A artifact + packet + exact source-row/obligation map + digest | unconsumed; may later feed `L_B/JCLOSE-EC` only |
| S13-C | requested C35 4300 split | **no identity-bound repository artifact found** | SOURCE-REQUIRED | repository artifact/packet plus exact C35 actual source mapping | unconsumed; no atlas occurrence inference |
| S13-C-B46 | requested B46 frontier | **no identity-bound repository artifact found** | SOURCE-REQUIRED | exact B46 source identity, actual face/source provenance, closure semantics | unconsumed |
| S13-D/S15 | requested same-face / alternative-root cautions | no identity-bound specialist artifact found | SOURCE-REQUIRED as specialist output | source artifact if specialist credit is desired | safety already enforced independently by JREL-SOUND |
| S11-83 | Lean bridge source | PR #83 identity known, draft/unmerged | TRANSPORT-ONLY, kernel unchecked | real pinned kernel replay + axiom report + statement-faithfulness + trusted receipt | not verification |
| L_A | direct reduction closure | generic LIFT-O content + row sources | partial ROW-CERTIFIED examples | actual JREL row + exact replacement + LIFT-BIND + trusted LIFT-VERIFY | OPEN globally |
| L_B | blocker/critical closure | no root-wide identity-bound B theorem | none globally | actual B row + exhaustive blocker split + blocker elimination/reduction + lifting | OPEN |
| JCLOSE | all actual joins close exhaustively | no root-wide theorem | partial row libraries only | complete `L_A/L_B/STRUCT/ESC` coverage for every actual JREL row | OPEN |
| CHARGE | `no D0` contradicts `Sigma mu=-8` | C34/C35/C48 candidate ledger | PASS-CANDIDATE bookkeeping | JREL-TOTAL + JCLOSE-EC for every actual D0; no payer/source mismatch | final root cut OPEN |

### Individually-certified rows versus actual joins

Current main has several individually certified exact source rows/libraries, including the C35 six-port deletion, selected C36 J reductions and exact C37 R160. They are `ROW-CERTIFIED` in their stated candidate scopes.

Current main does **not** contain a root-wide repository-bound theorem turning every actual `D0` low corner into one of those exact source rows. Therefore those rows are not counted as `ACTUAL-JOIN-CERTIFIED` root occurrences.

This is the central Cycle-6 distinction.

## 14. JUNIQ and exact-one SCUT remain optional

Suppose one actual join belongs to two source classes. Root closure remains sound if every class that may arise is covered and at least one source-valid closure applies, or if each generated row is itself exhaustively closed. A proof that exactly one STRUCT/A/B class holds can simplify bookkeeping but is not needed by the existential-elimination logic.

Likewise several low corners or gaps may map to the same source row. No uniqueness theorem is required unless a separate charge/payer injectivity argument explicitly uses it.

Hence the sole root DAG contains neither mandatory `JUNIQ` nor mandatory exact-one SCUT.

## 15. Sole live Cycle-6 DAG

```text
Assume a vertex-minimum counterexample G
 |
 +-- DC2/C35 charge ledger: Sigma mu = -8
 |      -> some actual unpaid negative triangle D0(f)
 |
 +-- LowCorners(f) nonempty                             [C48 candidate]
 |      |
 |      `-- for low corner p
 |             |
 |             +-- JREL-SOUND                           [contract; row-bound]
 |             +-- JREL-TOTAL                           [OPEN]
 |             |      actual same-face source record j
 |             |
 |             `-- JCLOSE-EC(j)                         [OPEN globally]
 |                    |
 |                    +-- STRUCT(j)
 |                    |
 |                    +-- L_A(j)
 |                    |      strict reduction
 |                    |      -> LIFT-BIND
 |                    |      -> LIFT-O theorem content [PASS candidate]
 |                    |      -> LIFT-VERIFY            [OPEN]
 |                    |
 |                    +-- L_B(j)
 |                    |      exhaustive blocker split [OPEN source-wide]
 |                    |      -> STRUCT or L_A or source-bound escape
 |                    |
 |                    `-- ESC(j)
 |                           -> normalized/source-specific discovery
 |                           -> TPROG useful terminal   [OPEN]
 |                           S02-B C3 excludes generic radius<=3 story
 |
 `-- every actual D0 closed
        -> no negative final face can occur in G
        -> contradict Sigma mu = -8.
```

Optional side tools:

```text
JUNIQ      normalize duplicate joins if useful;
SCUT-1     prove exact-one STRUCT/A/B if useful;
```

Neither is a root gate.

## 16. Exact live frontier

Priority after the fresh Cycle-6 source audit:

1. **JREL actual-source production.** Emit immutable same-face join records for low corners with rotations, aliases, complete stars, ownership and source/payer identity. This is the first missing root source record.
2. **JREL-TOTAL.** Prove the join relation covers every required actual low-corner description, without using C37 R160 or C35 finite atlases as occurrence theorems.
3. **JCLOSE-EC.** For every actual join, provide exhaustive complete-colouring closure through STRUCT / `L_A` / `L_B` / explicit escape.
4. **L_B.** Source-bind the blocker obligations and prove every blocker makes mathematical progress. The requested S12-A numbers cannot be used before identity binding.
5. **High-port escape / TPROG.** S02-B Cycle 3 shows generic separator + radius<=3 local usefulness is insufficient; prove source-specific/nonlocal usefulness or a stronger bounded radius.
6. **LIFT-BIND + LIFT-VERIFY.** Generic theorem content is candidate-PASS; per-row ownership/admission and real kernel/trusted replay are missing. PR #83 is transport-only.
7. **Final charge closure.** Once every actual `D0` is impossible under the unchanged ledger, use `Sigma mu=-8` to finish the contradiction. No new charge payment is presently justified.

## 17. Evidence ceiling

Everything in this checkpoint remains `candidate_only`.

Fresh authoritative ledgers at the consumed main are empty:

```text
research/records/evidence-links.jsonl
result-library/records/results.jsonl
research/records/failed-routes.jsonl.
```

No candidate here is promoted to Evidence. No EvidenceLink, Result, Solution, trusted verification or root closure is written.

```text
best_verified_result=none
root_closed=false.
```
