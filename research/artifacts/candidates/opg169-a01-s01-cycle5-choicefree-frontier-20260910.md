# R08 S01 Cycle 5 — choice-free root semantics and latest substantive delta

Verdict: `candidate_only`. `root_closed=false`. `best_verified_result=none`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected `main` consumed: `6b34ce7f7ce83b238bebd85babd7aaff6f40a3d0`.

Cycle 5 replaces selector-dependent root wording by a choice-free relational
contract and imports the latest completed deltas: S09 Cycle 4 GSRC occurrence
audit, S10 Cycle 3 corrected two-hole ownership, and S04 Cycle 6 identity-only
binding. No new S12, S13, S14, S15, or S02-A theorem is imported. S11 PR #83
is draft transport and is not consumed as a completed/kernel-checked bridge.

## 1. Choice-free root contract

For an actual unpaid negative face `f`, define

```text
W48(f,p)   p is a corner of f and s(p)<=5
F48(f,p)   W48(f,p) and t(p)<=5
SG48(f,p)  W48(f,p) and t(p)>=6
```

and let `G48(p)` be the set of singleton gaps for an SG witness. Define

```text
Desc48(f) =
  { (F,p)    : F48(f,p) }
  union
  { (SG,p,g) : SG48(f,p) and g in G48(p) }.
```

C48/S01 Cycle 4 gives

```text
D0(f) -> Desc48(f) != empty.
```

No unique corner or gap is supplied.

### Choice-free closure lemma

If every admissible description closes uniformly,

```text
forall f,a:
  D0(f) and a in Desc48(f) -> Close(f,a),
```

then no `D0(f)` exists.

Proof: assume `D0(f)`. Nonemptiness gives an arbitrary
`a in Desc48(f)` by existential elimination; the uniform theorem gives
`Close(f,a)`. No canonical selector or global choice function is used.

Hence the root architecture requires uniform coverage of all admissible
descriptions, not construction of a preferred witness.

## 2. Nonvacuous source relations

For `a in Desc48(f)` define

```text
Real(f,a,r)   actual alias-normalized local embedded realization
Gen(f,a,r,s)  globally source-faithful generated state
Class(s,c)    explicit source class of s.
```

The mandatory choice-free gates are:

```text
R-TOTAL:
  D0(f) and a in Desc48(f)
  -> exists r Real(f,a,r)

G-TOTAL:
  D0(f) and a in Desc48(f) and Real(f,a,r)
  -> exists s Gen(f,a,r,s)

G-COVER:
  D0(f) and a in Desc48(f) and Real(f,a,r) and Gen(f,a,r,s)
  -> exists c Class(s,c).
```

`Real` must carry actual rotations/faces, aliases before geometry, complete
stars, all contacts and ownership, and the source/payer key. `Gen` may not be
empty. Every generated state must be classified and handled; otherwise
universal statements could close by vacuity.

Duplicate descriptions are allowed.

## 3. Unique JMAP is optional, coverage is mandatory

Cycle 4 still placed a unique `JMAP/L_join` after GSRC. Choice-free root logic
does not require uniqueness if `G-TOTAL` and `G-COVER` hold and every generated
state is handled.

`JMAP-UNIQUE` is therefore demoted from a root gate to an optional
normalization theorem. It can still be useful for registry compression,
canonical IDs, avoiding duplicate computation, or a separately proved
payer-injectivity requirement. It may not silently discard noncanonical
descriptions.

The root-critical statement is complete coverage, not unique encoding.

## 4. S09 Cycle 4 — R160 non-inversion and selected-J escape

Merged commit:

```text
2a72d159ed8bd79fe31b9522f84c0e1c729913e5
```

Final candidate digests:

```text
proof        7fcbd8a40640d2c712de51efb86df73302be2c97ba92eaf8dbec51154796bfa1
obligations  58e27407199889f84186a780b225ef5ecbd3d4f5431f0f8600a1acb2f5f93c46
checker      55568973f649d0b05619e695a889b64eb0efabaf5961d07a3e528d6db60cb1ee
output       2a4d965109ba2115afce879479bed29346a3a3c8a5ff756072ddb43e67c917b7
```

The exact C37 statement

```text
forall s in R160:
  exact_C37_parent(s) -> reducible(s)
```

does not imply that an actual unpaid face generates any `s in R160`. S09 gives
a pure-logic countermodel to that inversion. This is not a planar
counterexample and does not refute GSRC.

Therefore R160 is a reduction library after source identification, not an
occurrence generator.

Conditional on occurrence of the exact selected C35/C36 J-source, preserved
C36 dependencies give `d(7)>=6`. If `d(7)=6`, C37 places the source in R160 and
the unconditional reductions exclude it from a vertex-minimum counterexample.
Thus

```text
selected C35/C36 J-source in a minimum counterexample
  -> d(7)>=7.
```

The correct next GSRC target is a provenance-preserving source-or-escape
theorem, not `D0 -> R160`.

Choice-free form:

```text
for every f,a,r with
  D0(f), a in Desc48(f), Real(f,a,r),

produce nonempty Gen(f,a,r,·), and cover every generated state by
  selected C37-J
  OR an explicit disjoint source/escape class.
```

If selected C37-J occurs, the minimum-counterexample branch is already
`d(7)>=7`.

## 5. S10 Cycle 3 — corrected two-terminal ownership

Merged commit:

```text
fa0b94b59eebeb2a1b5d123dc9e07ff03fc840b0
```

Digests:

```text
ownership consumer  69ab1332effea024bb56f4479fe310b4ceec595e5f9f05173fbf37e5d3b555f6
ownership matrix    aa623407d0716e129bf7a3e4fa49d783dc7a09eca09bd63454e706b69b914916
```

Actual deletion holes:

```text
H13=(7,8,16,12)
H14=(8,15,12,17)

vertex intersection = {8,12}
edge intersection   = empty.
```

The guard arc `8->12` is exterior to both hole interiors in the unabsorbed
decomposition. The old 22-face boundary walks meeting only at `12` are not the
deletion holes.

Therefore the inter-lobe object is a vertex-only two-terminal separator
`{8,12}`, not a shared-edge `K2` tournament. The exterior guard does not make
the two lobe pieces a common tournament interface. Ordinary same-boundary
extension is insufficient: a lobe return `12->8` may close a cycle with the
exterior `8->12`.

Sound composition must retain full positive reachability in both directions
and explicit ownership.

Guard-face absorption creates a new theorem instance: boundary, aliases,
contacts, ownership, and all LIFT-O premises must be recomputed.

C47 remains restricted to delete `{13,14}` plus at most one new nonisolated
internal vertex total inside the owning disks. Its 8,136 failures are not
extrapolated to absorbed/larger interfaces.

## 6. S04 Cycle 6 — identity bound, mathematics unchanged

Merged commit:

```text
6b34ce7f7ce83b238bebd85babd7aaff6f40a3d0
```

Identity artifact:

```text
research/artifacts/candidates/opg169-a01-s04-cycle6-artifact-identity.json
SHA-256 89a2a4e26b9108907e8fe88a7918330e4c8dcca4ba4b4da27d831152d6a93e53
```

Status:

```text
identity_status = REPOSITORY_BOUND_IDENTITY_ONLY
disposition     = STANDBY
mathematical_content_promotion = none.
```

The corrected geometry/ownership content remains attributed to C43/C47/S10.
No C47 scope extension or trusted verification follows. S04 should reactivate
only on source drift, verifier mismatch, or an explicit new S04 obligation.

## 7. LIFT-O and termination status

Generic ordinary arbitrary-exterior lifting remains

```text
LIFT_O_THEOREM_CONTENT      PASS(candidate)
S11 identity-bound theorem NOT_VERIFIABLE_MISSING_SOURCE on protected main
trusted verification       UNKNOWN.
```

PR #83 is a draft transport of an S11 Lean source and is not merged or
kernel-checked.

The live lifting gates are therefore

```text
LIFT-BIND
  actual aliases/boundary/contacts/ownership,
  complete valid-Q quantifier,
  same-boundary valid-P lift,
  both-colour positive R+ inclusion,
  class-preservation guards and strict descent;

LIFT-VERIFY
  trusted verification/admission.
```

S02-B Cycle 2 still refutes raw degree/port/size ranks, history-free
complete-star release ranks, and purely local separator ranks. Fixed-interface
profile compression remains family-scoped.

The unresolved termination gates are

```text
TNORM  source-bind a normalized no-backtracking transition system
TPROG  prove every terminal normalized state yields actual mathematical progress.
```

Discovery termination alone is insufficient.

## 8. Cycle-5 live root DAG

```text
R0 root
 |
 +-- D0 actual unpaid negative face f
      |
      +-- Desc48(f) nonempty                         [PASS candidate arithmetic]
            |
            `-- for every admissible a
                  |
                  +-- R-TOTAL                        [UNKNOWN]
                  |
                  +-- G-TOTAL + G-COVER             [UNKNOWN]
                  |      source-or-escape
                  |        |
                  |        +-- selected C37-J
                  |        |      +-- d(7)=6 -> R160 kill  [PASS candidate]
                  |        |      `-- d(7)>=7 -> TNORM/TPROG [UNKNOWN]
                  |        |
                  |        `-- explicit non-J/source class  [UNKNOWN]
                  |
                  `-- structural / A / B coverage
                         +-- STRUCT contradiction
                         +-- A reduction -> LIFT-BIND -> LIFT-O -> LIFT-VERIFY
                         `-- B -> B-criticality -> reduction -> lifting
```

There is no mandatory `JMAP-UNIQUE` root node.

## 9. Exact frontier

Priority:

1. `R-TOTAL`: choice-free actual source extraction for every `(f,p[,g])`.
2. `G-TOTAL + G-COVER`: nonempty provenance-preserving source-or-escape
   generation; do not target R160 directly.
3. `TNORM + TPROG` on the selected-J `d(7)>=7` escape.
4. B-criticality: no completed S12 package.
5. `LIFT-BIND + LIFT-VERIFY`: theorem content already candidate-PASS.
6. Corrected two-terminal composition: S04 identity is bound/STANDBY; any new
   theorem must use `{8,12}`, exterior guard ownership, and full positive R+.

Current specialist delta:

```text
S09 Cycle 4   PASS(candidate substantive delta)
S10 Cycle 3   PASS(candidate substantive delta)
S04 Cycle 6   REPOSITORY_BOUND_IDENTITY_ONLY / STANDBY
S11           no completed identity-bound/kernel-checked theorem on main
S12           no new package
S13           no post-Cycle-4 generator/mapper package
S14/S15       no new package
S02-A         no normalized termination theorem
S01           PASS(import/scope only)
```

## 10. Evidence ceiling

All mathematics remains `candidate_only`. Issue/PR/merge/CI state is not
mathematical Evidence.

Fresh authoritative ledgers remain empty:

```text
EvidenceLink
Result
failed-route
```

Therefore

```text
best_verified_result=none
root_closed=false.
```

Cycle 5 changes no formal truth/control record.
