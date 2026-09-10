# R08 S01 Cycle 6 — final JREL refinement after S09 Cycle 5

`candidate_only`; `best_verified_result=none`; `root_closed=false`.

Fresh protected main imported by this refinement:
`f764f5b2b6acdf8b0ff965ec09dc1d224a36a08f`.

This file is the final Cycle-6 refinement of
`opg169-a01-s01-cycle6-jrel-root-dag-20260910.md`.
It does not replace the definitions or full row matrix there; it supersedes only
selected-J rows and freshness/source-gate statements affected by merged S09
Cycle 5 / PR #88.

## 1. Sole root shape is unchanged

```text
D0
 -> LowCorners relation
 -> JREL-SOUND/TOTAL
 -> JCLOSE-EC
 -> Sigma-mu contradiction.
```

`JUNIQ` and exact-one SCUT remain optional.

The first root missing record remains an **actual same-face JREL record** from
an actual `D0(f)` low corner to an exact source state.  S09 Cycle 5 starts
strictly *after* such a selected-J occurrence is already source-bound; it does
not prove `JREL-TOTAL`, `R-TOTAL`, `G-TOTAL`, or `D0 -> selected-J`.

## 2. New identity-bound bridge: selected-J cover after actual join

Merged S09 Cycle 5 candidate identities:

```text
merge main     f764f5b2b6acdf8b0ff965ec09dc1d224a36a08f
proof SHA256   96cb1b16c7e555709aec50fff49394f20d0fff85d798cf1150db52b8884a66bf
schema SHA256  39dbe5fd5157346d9e9a6b530f88dda36d15d383813a12be5b66f88b92e7f46d
D/3 SHA256     85402f19ce74a61231b432d2eb37cb821dfbef9e5d7e0561ba404358d3e87552
checker SHA256 0374baf1a904376acd0305cdcf855084b8e485719d72c2db7d6c1a256a52cf71
output SHA256  8dcbe0df2fe7a5368854ac68800935a8e6a3e9b9e52f3e5a697a4f149547f80a
```

Exact input contract:

```text
an already actual, source-bound selected C35/C36 J occurrence,
carrying the original (f,p[,g]) provenance,
exact embedding and rotation,
complete controlled stars,
alias roles,
source/payer keys,
and ownership.
```

Under the preserved C36 lower bound, `d(7)>=6`.  S09 then gives the disjoint
degree cover

```text
d(7)=6        -> exact C37 source identity,
d(7)>=7       -> exact-source class J_HIGHPORT.
```

This is a **post-JREL G-COVER / class-identification bridge** for the
selected-J lane.  It is not a generator from `D0`.

### Degree-six branch

For an already actual selected-J row with `d(7)=6`, the actual rotation gives
exactly two ordered wedge neighbours.  The exact 13-cell alias quotient leaves
only

```text
D, X5, X6, Y4, Y5,
```

and the five actual source-edge directions determine one exact five-bit word.
Thus the source receives one exact C37 parent identity `family/word` **before**
R160 is used.

Only after this occurrence identity may the exact C37 R160 reduction library be
invoked.  Therefore in a vertex-minimum counterexample the selected-J degree-six
branch is excluded.

This does not invert R160 into occurrence.

### High-port branch

For `d(7)>=7`, S09 records the disjoint exact-source class

```text
J_HIGHPORT.
```

Its source row retains the complete actual star of 7, ordered wedge neighbours,
actual wedge faces, alias and direction signatures, source/payer ownership and
an escape key.  No reducibility, finite classification or termination theorem
is claimed for this class.

The live continuation is therefore `J_HIGHPORT -> ESC/TPROG`, not a fake
higher-degree C37 table.

## 3. D/3 record: individually instantiated source, not root join

S09 supplies one fully instantiated source record for the repository C37
whole-graph control witness:

```text
source face      (0,2,3)
F48 witness      p=0
family/word      D/3
source-owned arcs 23
exterior-owned arcs 4
actual payer set empty
```

This is useful evidence of **candidate source-record schema fidelity** and an
individually instantiated actual source in a colourable control graph.

It is **not** an `ACTUAL-JOIN-CERTIFIED` root occurrence because the graph is
not the assumed minimum counterexample and the record is not generated from an
actual root `D0` face.  It cannot satisfy `JREL-TOTAL`.

## 4. Refined row-level cuts

The following rows supersede the corresponding selected-J rows in the full
Cycle-6 matrix.

| Row | Exact dependency | Certificate level | First missing actual source record / cut | Disposition |
|---|---|---|---|---|
| JSEL-IN | actual `D0(f)` low corner -> actual selected C35/C36 J row | none root-wide | **same-face JREL record with `(f,p[,g])`, complete stars, aliases, payer/source ownership** | OPEN; still first selected-J cut |
| JSEL-COVER | already actual selected-J row -> `d6 C37` OR `J_HIGHPORT` | PASS-CANDIDATE source-bound classification | none after JSEL-IN; depends on preserved C36 lower bound | CLOSED conditionally after actual join |
| JSEL-d6-ID | actual selected-J + `d(7)=6` -> exact C37 family/word | ROW-CERTIFIED identity bridge | actual selected-J occurrence is prerequisite | PASS candidate |
| JSEL-d6-CLOSE | exact C37 family/word -> R160 strict reduction -> lifting | ROW-CERTIFIED finite library | row-level LIFT-BIND / trusted LIFT-VERIFY for admission; no occurrence inference | candidate equality kill |
| JSEL-HIGH | actual selected-J + `d(7)>=7` -> `J_HIGHPORT` exact-source escape | source class identified | **source-specific useful terminal/closure theorem** | TPROG OPEN |
| D3-CONTROL | repository D/3 whole-graph source record | individually instantiated actual control source | **root D0 same-face occurrence absent** | not a root actual join |

The root-wide matrix remains unchanged elsewhere.

## 5. S13-C/B46 source gate remains closed

Concurrent S10 PR #89 is not consumed by this Cycle-6 refinement because it is
not on protected main and its latest observed candidate gate is not successful.
Its current candidate message is itself a source-admission result, not B46
mathematics: 46 expected slots, zero recovered source row IDs, zero consumed
rows, and no PASS/FAIL mathematical classification.  It reports historical
transport corruption rather than recovering the requested S13-C rows.

Hence the user-requested C35 `4300` split remains unconsumed, and the B46
frontier remains source-gated.  No C35 finite atlas implies occurrence.

## 6. S12-A and S13-D/S15 remain source-gated

Fresh protected-main search still contains no identity-bound S12-A package for

```text
784 exact ALL-colouring obligations = 578 blocker + 206 all-extend,
```

so those counts remain requested but unconsumed.  Their valid future insertion
point is `L_B/JCLOSE-EC` only after exact source-row and actual JREL mapping.

Likewise no protected-main identity-bound S13-D/S15 specialist artifact supplies
the requested same-face/alternative-root result.  The safety condition is
already enforced independently by `JREL-SOUND`: an actual join must retain the
same root `D0` face and its payer/source ownership; an alternative root requires
a new explicit source record.

## 7. L_A, L_B, lifting and charge remain exactly scoped

`L_A` still needs an actual same-face JREL source row, strict source-valid
replacement, complete-Q nonvacuous all-colouring lift, both-colour positive
reachability containment, exact aliases/ownership/guards/descent and lifting
admission.

`L_B` still needs an actual B-source JREL row, identity-bound exhaustive
ALL-colouring blocker split, exact blocker witnesses, complete closure of both
blocker and all-extend outcomes, source-valid B-criticality premises, and
lifting admission.  No root-wide B-criticality theorem is added here.

Generic LIFT-O theorem content remains candidate-PASS.  `LIFT-BIND` and real
`LIFT-VERIFY` remain separate.  S11 PR #83 is still transport-only until a real
pinned kernel replay/axiom/statement-faithfulness process is performed.

The final charge contradiction is unchanged:

```text
Sigma_f mu(f) = -8
 -> an actual D0 exists
 -> JREL-TOTAL + JCLOSE-EC makes every actual D0 impossible
 -> contradiction.
```

No local reduction is represented as numerically adding charge to the original
graph.

## 8. Final Cycle-6 live DAG

```text
minimum counterexample G
 |
 +-- Sigma mu=-8 -> actual D0(f)
 |
 +-- LowCorners(f) nonempty
 |      |
 |      `-- actual low corner p
 |             |
 |             +-- JREL-SOUND
 |             +-- JREL-TOTAL                         [OPEN ROOT CUT]
 |             |      -> actual source row j
 |             |
 |             `-- JCLOSE-EC(j)                       [OPEN GLOBALLY]
 |                    |
 |                    +-- selected-J
 |                    |      -> S09 C5 narrow cover   [PASS after join]
 |                    |           +-- d6 -> exact C37 -> R160 -> L_A/lifting
 |                    |           `-- d>=7 -> J_HIGHPORT -> ESC/TPROG [OPEN]
 |                    |
 |                    +-- STRUCT
 |                    +-- L_A -> LIFT-BIND -> LIFT-O -> LIFT-VERIFY
 |                    `-- L_B -> blocker closure / B-criticality -> lifting
 |
 `-- all actual D0 impossible -> contradict Sigma mu=-8.
```

No mandatory `JUNIQ` or exact-one SCUT is introduced.

No EvidenceLink, Result, Solution, trusted verification, or root closure is
created by this refinement.
