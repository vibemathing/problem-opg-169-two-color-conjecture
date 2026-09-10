# R08 S01 Cycle 3 — source-cut repair and second-batch integration

Verdict: `candidate_only`. `root_closed=false`. `best_verified_result=none`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`
Problem: `problem:opg-169-two-color-conjecture`
Attempt: `attempt:web-20260906-opg169-a01`
Route: `route:minimal-counterexample-structure-v1`
Graph: `graph:opg169-initial-v1`
Target: `obligation:opg169-root`
Fresh protected main consumed: `160fa1085f274191bc09185f289d5ac2c4c6362e`.

Cycle 3 imports exactly two new completed candidate outputs beyond S01 Cycle 2:
S02-B high-port adversarial analysis and S10 clean-room finite consumer
corroboration. No S13 mapper, S12 B-criticality theorem, S11 lifting theorem,
S04 two-terminal decision, or S14 cap theorem is imported.

## 1. Source-cut type correction

The Cycle 1/2 label that called the C48 low-slack dichotomy the first
source cut is superseded. C48 is an arithmetic localization theorem, not a
source-faithful geometric generation theorem.

The corrected type chain is:

```text
D0  actual unpaid negative DC2 face
 |
 v
A48 arithmetic locator
    F26 arithmetic cell XOR SG singleton-gap arithmetic branch
 |
 |  no realizability inference
 v
LSRC local-source realization
    actual plane orientation / rotations / faces / holes / aliases /
    complete stars / edge ownership / local source constraints
 |
 |  no global-occurrence inference
 v
GSRC global source generation
    generated from D0 with exact payer/source identity and no double spending
 |
 v
JMAP unique L_join
    exactly one source selector / parent identity
 |
 v
SCUT source-faithful leaf cut
    exactly one of STRUCT / A / B
```

Thus:

- `A48` is the first root-wide **arithmetic** cut.
- `SCUT` is the first genuine **source-faithful** cut.
- `SCUT` remains `UNKNOWN`.
- No edge `A48 -> SCUT` is available without LSRC, GSRC, and JMAP.

The theorem content of C48 is not withdrawn. Only its DAG type is corrected.

## 2. Second-batch import: S02-B high-port family

Imported proof:
`research/artifacts/candidates/opg169-a01-s02b-high-port-chain-20260910.md`
SHA-256 `e003bbaeb1dfbe513d42fbf61e479c3173ed490e9c1072713b2373fff3e57900`.

Checker SHA-256:
`549239acee6ed91e57ab941c0d2c0635fc5f9ded2471b2b4cdf881ea9ff9033d`.

Checker output SHA-256:
`b3f74273204459ace40cbbde20021c314f8abe9e76f726d92d503717b3171835`.

### Imported candidate facts

For every `n>=1`, splitting the C37 witness edge `12->13` into

```text
12 -> z_1 -> ... -> z_n -> 13
```

and independently choosing either spoke sign

```text
7 -> z_i -> 5
```

or

```text
5 -> z_i -> 7
```

gives an exact locally source-valid simple plane triangulation with

```text
d(7)=6+n,
|V|=11+n,
|E|=27+3n,
|F|=18+2n,
d^-(z_i)=d^+(z_i)=2.
```

Therefore the following proposed termination coordinates fail as decreasing
ranks on the locally source-valid transition system:

- degree `d(7)`;
- number of fresh ports;
- number of fan sectors/faces;
- raw local vertex/edge/controlled-region size;
- any lexicographic rank whose earlier coordinates are constant on this family
  and whose decisive coordinate is one of those increasing quantities.

Status: `PASS(import/scope)` for the candidate counterfamily.
Trusted mathematical verification: absent.

### Fixed-interface compression is narrower than global termination

The same S02-B artifact proves that its explicit edge-split family cannot form
an infinite unresolved minimum-counterexample chain while the interface remains
the fixed four-port boundary `(7,5,12,13)`. The full strong boundary profile is
finite; repeated prefix profiles give a strict source-valid profile-preserving
replacement by a shorter prefix.

This is imported only for that family and interface. It is not generalized to
all bounded-interface sources.

The first surviving termination obligation is:

```text
ESCAPE
  interface release
  OR separator crossing
  OR absorption of a new complete star
  OR genuinely growing exterior contact set
```

S02-A must prove a well-founded rank `rho` that strictly decreases on every
such escape transition, or S02-B must construct a source-valid growing-interface
pump defeating every proposed `rho`.

## 3. Termination is not a B-only child

Cycle 1/2 placed high-port termination only below the B leaf. S02-B makes that
placement unsound as a scheduling type: high-port source expansion already
exists at the local-source level, before any global STRUCT/A/B classification.

The repaired architecture treats termination as a well-foundedness gate on
recursive source resolution:

```text
LSRC / GSRC / JMAP recursive expansion
          |
          +-- TERM
              |
              +-- RAW-RANK family            FAIL(candidate route)
              |
              +-- explicit fixed-4-port C37
              |      profile compression     PASS(candidate, exact family)
              |
              `-- ESCAPE-RANK                 UNKNOWN
```

`TERM` is not a fourth leaf beside STRUCT/A/B. It is a side condition required
whenever source resolution recursively enlarges or changes the controlled
interface.

## 4. Second-batch import: S10 clean-room finite consumer

Imported execution manifest:
`research/artifacts/candidates/opg169-s10-cleanroom-execution-manifest.json`,
candidate artifact SHA-256
`2962b22e8d4be9101b3111510ac1debdc6ec84c16a6485c5c8634763a47e27c3`.

Frozen external execution identities recorded by that manifest:

- clean-room checker SHA-256
  `72300ee37f7f5df7ba28244577ab27c781876f9a2f642223065a30be8e2959a2`;
- results file SHA-256
  `e26ddb5b66afc1479e2f5f8634d666a81c5b783471271d054fbacf7e836c3f21`;
- semantic result digest
  `f3dc810615fd1ee01c779e2f5f763c7c62309eea61dbd7e42fe4390e9fd86a20`;
- row-status CSV SHA-256
  `935fa6f49cd26b9525c96c2fec5b117cf36e79626f0a7f2e4bb954fca8390a6c`.

The implementation imports no producer checker, producer lift vector, or
producer helper. It remains a candidate-generation trust domain, not a
registered trusted verifier.

### C37 exact d(7)=6

Clean-room result:

```text
160/160 PASS
156 merged delete {0,2}
4 bare delete-3 rows Y4/{0,4,16,20}
21,732 complete valid Q colourings
16,536 equal R+ lifts
5,196 strict R+ lifts
0 failures
```

All eight mutation canaries are killed when one of complete-Q, positive
reachability, embedding, reverse guards, complete stars, alias normalization,
nonvacuity, or strict order decrease is removed.

This upgrades the exact C37 `d(7)=6` library from producer-only support to
**clean-room candidate corroboration**. It still has no trusted EvidenceLink.

DAG effect: once GSRC/JMAP identifies an actual source state as one of these
exact 160 parents, the ordinary finite reduction library is no longer the
dominant research uncertainty. The missing bridge is global source generation
and mapping.

### S08 P10--P14

S10 reproduces `5/5 PASS` under the frozen anchored `ATC_any_old` contract.
The stronger `strict_zero_new` and `ATC_deleted_only` intersections remain
zero in their frozen scans.

DAG effect: anchored finite rows receive clean-room candidate corroboration.
They do not enter the ordinary root lane.

### S09 source blocker

S10 reports

```text
NOT_VERIFIABLE_MISSING_SOURCE
```

for the requested remaining guard-child difference.

Current repository truth has no exact remaining-child registry, row set, and
per-row source digests after ancestor subtraction. The C48 manifest contains
only unbound `S09_C5` corroboration of C37 `160/160`.

Cycle 3 status for S09:

`FAIL(source-admission gate)`, not mathematical falsity.

Required repair before S09 computation can matter:

1. freeze the canonical parent registry;
2. subtract exact ancestor-dominated descendants;
3. emit the remaining child identities with source digests;
4. only then run clean-room reduction verification.

## 5. Repaired live typed DAG

```text
R0  root conjecture
 |
 +-- D0 actual unpaid negative DC2 face                         [candidate]
      |
      +-- A48 arithmetic locator: F26 XOR SG                    [PASS candidate]
            |
            |  REQUIRED BRIDGE 1
            v
          LSRC actual local-source realizations                  [UNKNOWN]
            |
            |  TERM side gate on recursive source expansion
            |    RAW degree/port/size rank                       [FAIL candidate route]
            |    explicit C37 fixed-4-port tail compression      [PASS exact family]
            |    growing-interface / separator escape rank       [UNKNOWN]
            |
            |  REQUIRED BRIDGE 2
            v
          GSRC global generation from D0
               payer/source identity + ownership + no double spend
                                                                  [UNKNOWN]
            |
            |  REQUIRED BRIDGE 3
            v
          JMAP unique L_join                                     [UNKNOWN]
            |
            v
          SCUT exactly one source-faithful leaf
            |
            +-- STRUCT -> structural contradiction
            |
            +-- A -> strict ordinary reduction
            |       |
            |       +-- exact C37 d(7)=6 library:
            |              clean-room candidate corroborated 160/160
            |       |
            |       `-- LIFT-O
            |
            `-- B -> B-criticality                              [UNKNOWN]
                    -> strict ordinary reduction
                    -> LIFT-O

LIFT-O ordinary arbitrary-exterior theorem / verification       [UNKNOWN]
      -> contradiction
```

Anchored reduction/lifting remains a disjoint type. S08 `ATC_any_old` cannot
close any `LIFT-O` edge without a separate lane-conversion theorem.

## 6. Mutually exclusive status ledger

| Node / lane | Cycle 3 status | Meaning |
|---|---|---|
| A48 arithmetic locator | PASS(import/scope) | arithmetic only |
| LSRC geometry realization from A48 | UNKNOWN | S13-B missing |
| GSRC negative-face generation | UNKNOWN | source/payer bridge missing |
| JMAP unique L_join | UNKNOWN | S13-C/D missing |
| SCUT STRUCT/A/B partition | UNKNOWN | depends on GSRC+JMAP |
| exact C37 d(7)=6 finite library | PASS(clean-room candidate) | 160/160; conditional on exact source identification |
| raw degree/port/sector/size termination | FAIL(candidate route) | S02-B parametric local-source counterfamily |
| fixed four-port C37 tail | PASS(candidate, family-scoped) | finite-profile compression |
| escape/growing-interface termination | UNKNOWN | S02-A/B live target |
| B-criticality | UNKNOWN | S12-A/B/C |
| S09 remaining guard difference | FAIL(source gate) | exact source registry missing |
| S08 ATC_any_old | PASS(clean-room candidate, anchored) | no ordinary-lane promotion |
| LIFT-O theorem and independent verification | UNKNOWN | S11 + S10 theorem-level interface still missing |
| S04 corrected two-terminal scope | UNKNOWN | C47 cannot be extrapolated |
| S14 singleton caps | UNKNOWN | no repository-bound completed successor |
| root | UNKNOWN/open | no EvidenceLink / Result |

## 7. Ancestor precedence after S10

Exact-parent precedence remains unchanged in logical scope, but its finite
support is stronger:

- exact C37 `d(7)=6`, five families x 32 directions = 160 parents;
- S06 producer catalogue: 160/160;
- S10 clean-room consumer: 160/160 with matching complete-Q and R+ totals;
- therefore same-exact-parent C38/C39/C40/C43--C47/S08-D19 ordinary descendants
  remain inactive for live scheduling when they only restrict the exterior.

No dominance extends to:

- `d(7)>=7`;
- S02-B's split-edge family;
- another J orientation;
- a changed complete star, arc set, rotation, or interface;
- all F26 or SG states;
- GSRC/JMAP;
- the global root.

## 8. Current frontier

Priority order after the source-cut repair:

1. **GSRC + JMAP** — source-faithful generation and unique `L_join`.
   Arithmetic coverage and local source geometry are now explicitly upstream
   types, not substitutes.
2. **ESCAPE-RANK** — the only high-port termination mechanism still exposed by
   S02-B: growing interface / separator / complete-star release.
3. **B-criticality** — still requires blocking-path, topology, and falsifier
   agreement.
4. **S09 source registry** — source-data repair first; no further checker run is
   meaningful before the exact difference set exists.
5. **LIFT-O theorem** — S10 corroborates finite instances and mutations but does
   not replace S11 arbitrary-exterior theoremization.
6. **S04 / S14 finite structural lanes** — only after source identity survives
   ancestor precedence.

## 9. Truth and trust boundary

The authoritative failed-route ledger remains empty. S02-B's finite-degree/raw
complexity failure is a candidate failed-route proposal only.

The EvidenceLink ledger is empty. The Result ledger is empty.

`best_verified_result=none`
`root_closed=false`

## 10. Non-claims

This checkpoint does not claim:

- that C48 arithmetic cells are geometrically realizable;
- that S02-B local source states occur as GSRC children;
- a global source generator;
- a unique `L_join`;
- a completed STRUCT/A/B source cut;
- a global high-port termination theorem;
- a growing-interface no-pump theorem;
- B-criticality;
- an exact remaining S09 child set;
- ordinary use of anchored S08 rules;
- trusted independent verification;
- a full arbitrary-exterior lifting theorem;
- a two-terminal theorem;
- a singleton-cap theorem;
- an EvidenceLink, Result, Solution, or root closure.
