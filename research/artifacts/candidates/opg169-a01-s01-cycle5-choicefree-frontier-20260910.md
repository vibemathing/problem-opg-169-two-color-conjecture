# R08 S01 Cycle 5 — choice-free root semantics and latest substantive delta

Verdict: `candidate_only`. `root_closed=false`. `best_verified_result=none`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem-opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected `main` consumed: `6b34ce7f7ce83b238bebd85babd7aaff6f40a3d0`.

Cycle 5 does two things only:

1. it replaces selector-dependent root wording by a choice-free relational root contract; and
2. it imports the exact post-Cycle-4 substantive delta already merged on main:
   S10 Cycle 3 ownership/source-gate content and S09 Cycle 4 GSRC occurrence content; and
3. it absorbs the later S04 identity-only binding without promoting new mathematics.

No new S12 B-criticality package, S13 global generator / unique mapper package,
S11 identity-bound theorem, S14 cap theorem, S15 root falsifier, or new S02-A
termination theorem is imported. S04 now has a repository-bound specialist
identity, but no new S04 theorem is promoted.

## 1. Choice-free root semantics

Cycle 4 correctly repaired C48 from a face-level `F26 XOR SG` shorthand to an
existential witness relation. Cycle 5 removes the remaining unnecessary
selector pressure from the *root* architecture.

Let `D0(f)` mean that `f` is an actual unpaid negative triangular face. Let

```text
W48(f,p)   p is a corner of f and s(p)<=5
F48(f,p)   W48(f,p) and t(p)<=5
SG48(f,p)  W48(f,p) and t(p)>=6.
```

For an SG witness, let `G48(p)` be the nonempty set of singleton gaps proved by
C48.

Define the complete set of admissible arithmetic descriptions of `f`:

```text
Desc48(f) =
  { (F,p)    : F48(f,p) }
  union
  { (SG,p,g) : SG48(f,p) and g in G48(p) }.
```

C48 plus the singleton-gap lemma gives

```text
D0(f) -> Desc48(f) is nonempty.
```

There is no requirement that `Desc48(f)` have one element.

### Choice-free closure lemma

Let `Close(f,a)` be any downstream statement such that, whenever it holds for
an admissible description `a in Desc48(f)`, the assumed minimum counterexample
containing `f` yields a contradiction.

If

```text
forall f,a:
  D0(f) and a in Desc48(f) -> Close(f,a),
```

then no `D0(f)` exists.

**Proof.** Assume `D0(f)`. The C48 theorem gives `Desc48(f)` nonempty. Use
ordinary existential elimination to take an arbitrary witness description
`a in Desc48(f)`. The universally quantified downstream theorem gives
`Close(f,a)`, hence a contradiction. No global choice function, canonical
corner, canonical singleton gap, or uniqueness theorem is used. QED.

This is the root-level semantics for Cycle 5.

The proof obligation is therefore **uniformity over all admissible
descriptions**, not construction of a preferred selector.

## 2. Choice-free source relations

For an admissible description `a in Desc48(f)`, define:

```text
Real(f,a,r)   r is the actual alias-normalized local embedded realization
              extracted from the graph for description a;

Gen(f,a,r,s)  s is a source-faithful global source state generated from r,
              with source/payer identity, all ownership, and no double spending;

Class(s,c)    c is an explicit source class assigned to s.
```

The root contract is intentionally relational. It has three nonvacuity /
coverage requirements.

### R-TOTAL — local realization is total

```text
forall f,a:
  D0(f) and a in Desc48(f)
  -> exists r Real(f,a,r).
```

`r` must record actual rotations/faces, aliases before geometry, complete stars,
edge/face ownership, exterior contacts, and the source/payer key.

### G-TOTAL — global source generation is nonempty

```text
forall f,a,r:
  D0(f) and a in Desc48(f) and Real(f,a,r)
  -> exists s Gen(f,a,r,s).
```

An empty generation relation is not allowed to close the root by vacuity.

### G-COVER — every generated source is explicitly classified

```text
forall f,a,r,s:
  D0(f) and a in Desc48(f) and Real(f,a,r) and Gen(f,a,r,s)
  -> exists c Class(s,c).
```

For root closure, every allowed class must then make mathematical progress:
structural contradiction, strict reduction covered by LIFT-O, or a separately
proved recursive escape whose normalized terminal states make progress.

This is stronger than selecting one convenient source and is safe under
duplicate descriptions.

## 3. Unique JMAP is not a root gate

Cycle 4 still listed

```text
GSRC -> JMAP unique L_join / exact parent identity.
```

Under the choice-free contract, uniqueness is not logically required for the
root contradiction.

Several admissible descriptions may:

- represent the same exact source after alias normalization;
- map to several source encodings of the same embedded state;
- reach different explicit source classes.

The root proof remains sound provided `G-TOTAL` and `G-COVER` hold and every
generated state is handled.

Therefore:

```text
JMAP-UNIQUE
```

is demoted from a mandatory root gate to an optional normalization theorem.

It remains useful for:

- registry compression;
- canonical source IDs;
- proving an injective payer assignment when a separate accounting argument
  actually needs injectivity;
- avoiding duplicate computation.

It may not be used to strengthen the mathematical root statement by silently
discarding noncanonical descriptions.

The root-critical obligation is **coverage**, not uniqueness.

## 4. Latest completed delta A — S09 GSRC non-inversion

Merged main commit:

```text
2a72d159ed8bd79fe31b9522f84c0e1c729913e5
```

PR #80 final-head candidate package has:

```text
proof SHA-256
7fcbd8a40640d2c712de51efb86df73302be2c97ba92eaf8dbec51154796bfa1

obligations SHA-256
58e27407199889f84186a780b225ef5ecbd3d4f5431f0f8600a1acb2f5f93c46

checker SHA-256
55568973f649d0b05619e695a889b64eb0efabaf5961d07a3e528d6db60cb1ee

output SHA-256
2a4d965109ba2115afce879479bed29346a3a3c8a5ff756072ddb43e67c917b7
```

### R160 cannot be inverted into occurrence

The exact C37 registry says

```text
forall s in R160:
  exact_C37_parent(s) -> reducible(s).
```

It does not imply

```text
forall actual unpaid faces f:
  exists s in R160 occurs(f,s).
```

S09 gives a finite pure-logic countermodel to this inference. This is not a
planar counterexample and does not refute GSRC. It proves that the registry is
a reduction library, not a source generator.

Cycle-5 consequence: remove every route edge that treats

```text
R160 total reduction coverage
```

as evidence for

```text
D0 -> R160 occurrence.
```

### Selected-J escape lemma

Conditional on occurrence of the exact selected C35/C36 J-source:

```text
minimum counterexample -> d(7)>=6
```

from the preserved C36 source chain.

If `d(7)=6`, the source is one of the exact C37 160 parents and is eliminated by
the unconditional C37 strong-profile reductions. Hence:

```text
selected C35/C36 J-source in a vertex-minimum counterexample
  -> d(7)>=7.
```

Thus R160 is now best viewed as an **equality-kill layer** inside a future
source-or-escape theorem, not as the intended GSRC occurrence target.

### Minimal next source theorem

The useful target is the choice-free form of a provenance-preserving
source-or-escape statement:

```text
forall f,a,r:
  D0(f) and a in Desc48(f) and Real(f,a,r)
  ->
  exists s Gen(f,a,r,s)
  and every generated s is in exactly the declared coverage union:
      selected-C37-J
      OR explicit disjoint source/escape class.
```

Uniqueness of the class label is optional for the root; complete coverage is
mandatory.

If the selected C37-J class occurs, the minimum-counterexample branch is
already narrowed to `d(7)>=7`.

## 5. Latest completed delta B — corrected two-hole ownership

Merged main commit:

```text
fa0b94b59eebeb2a1b5d123dc9e07ff03fc840b0
```

S10 Cycle-3 packet binds:

```text
ownership consumer SHA-256
69ab1332effea024bb56f4479fe310b4ceec595e5f9f05173fbf37e5d3b555f6

ownership matrix SHA-256
aa623407d0716e129bf7a3e4fa49d783dc7a09eca09bd63454e706b69b914916
```

The corrected source-owned holes are

```text
H13 = (7,8,16,12)
H14 = (8,15,12,17)
```

with

```text
V(H13) intersect V(H14) = {8,12}
E(H13) intersect E(H14) = empty.
```

The guard arc

```text
8->12
```

is exterior to both hole interiors in the unabsorbed decomposition.

The old two 22-face-complex boundary walks meeting only at `12` are not the
deletion holes and may not be used to recover a one-terminal pinch.

### Correct interface type

The inter-lobe object is a vertex-only two-terminal separator

```text
T = {8,12},
```

not a shared-edge `K2` tournament.

The exterior arc `8->12` does not change that ownership fact.

Therefore the complete-tournament ordinary-extension shortcut is unavailable
for the two lobes. A same-colour lobe return `12->8` can combine with exterior
`8->12` to form a cycle.

Any sound composition must retain complete positive reachability in both
directions and explicit ownership.

### Guard-face absorption

If a guard-edge incident face is absorbed into a patch, the theorem instance
changes. Boundary, aliases, exterior contacts, arc ownership, and all LIFT-O
premises must be recomputed.

C47 remains bounded exactly to:

```text
delete {13,14}
plus at most one new nonisolated internal vertex total,
with edges inside their owning disks.
```

Its 8,136 failures do not extend to guard-face absorption, two new internal
vertices, larger interfaces, extra complete stars, or cross-hole shortcuts.

Cycle-5 effect: S04 now has a repository-bound identity-only artifact, but no
new theorem content is promoted. The two-terminal ownership semantics are a
repository-derived source contract from C43/C47/S10 that any future
substantive S04/GSRC state must obey.


## 5A. Latest identity delta — S04 is repository-bound and STANDBY

Merged main commit:

```text
6b34ce7f7ce83b238bebd85babd7aaff6f40a3d0
```

PR #82 adds the repository specialist identity artifact

```text
research/artifacts/candidates/opg169-a01-s04-cycle6-artifact-identity.json

SHA-256
89a2a4e26b9108907e8fe88a7918330e4c8dcca4ba4b4da27d831152d6a93e53
```

Its identity status is

```text
REPOSITORY_BOUND_IDENTITY_ONLY
```

and its disposition is

```text
STANDBY.
```

This repairs only the S04 source-identity gate. It promotes no mathematical
content: the corrected holes, ownership, C47 bounded negative result, and
two-terminal semantics remain attributed to the already merged C43/C47/S10
source chain.

Therefore Cycle 5 distinguishes:

```text
S04 identity       BOUND(candidate metadata)
S04 content        repository-derived C43/C47/S10
new S04 theorem    none
trusted verification none
disposition        STANDBY
```

S04 should reactivate only on C43/C47/S10 source drift, verifier mismatch, or
an explicit new S04 obligation. Its identity binding does not re-open the old
one-terminal geometry and does not extend C47 beyond its frozen scope.

## 6. LIFT-O status after the ownership repair

The generic theorem content from S10 Cycle 2 remains unchanged:

```text
LIFT_O_THEOREM_CONTENT      PASS(candidate)
S11 identity-bound theorem NOT_VERIFIABLE_MISSING_SOURCE
trusted verification       UNKNOWN
```

The S04 correction does not refute LIFT-O; it prevents a wrong invocation.

For every concrete reduction row, source binding must still verify:

```text
actual alias quotient
actual boundary
all patch/exterior contacts
shared-edge ownership/direction
complete valid-Q quantifier
same-boundary valid-P lift
both-colour positive R+ inclusion
class-preservation guards
strict order decrease
simple planar orientation membership.
```

Thus the live lifting gate is now:

```text
LIFT-BIND + LIFT-VERIFY
```

not reproving the generic theorem.

## 7. Termination stays split: TNORM and TPROG

S02-B Cycle 2 remains unchanged by the new deltas.

Refuted in exact scopes:

```text
raw degree/port/size rank
history-free complete-star release rank
purely local separator rank.
```

Not refuted:

```text
history-aware normalized source-discovery bookkeeping.
```

But discovery termination alone does not close the root.

The live obligations remain:

```text
TNORM
  source-bind a no-backtracking normalized transition system;

TPROG
  prove every terminal normalized state yields:
    structural contradiction,
    source class already covered,
    or strict source-valid reduction.
```

A terminal state that merely means "the finite graph has been fully exposed"
is not mathematical progress.

## 8. Cycle-5 choice-free live DAG

```text
R0 root
 |
 +-- D0 actual unpaid negative face f
      |
      +-- Desc48(f) nonempty                              [PASS candidate arithmetic]
            |
            +-- for every admissible description a
                   |
                   +-- R-TOTAL: actual source extraction  [UNKNOWN]
                   |
                   +-- TNORM / TPROG if recursive         [UNKNOWN]
                   |
                   `-- G-TOTAL + G-COVER
                         provenance-preserving
                         source-or-escape relation         [UNKNOWN]
                              |
                              +-- selected C37 J source
                              |      |
                              |      +-- d(7)=6
                              |      |     -> R160 kill    [PASS candidate]
                              |      |
                              |      `-- d(7)>=7
                              |            -> high-port
                              |            -> TNORM/TPROG [UNKNOWN]
                              |
                              +-- explicit non-J class     [UNKNOWN classification]
                              |
                              `-- structural / A / B class
                                      |
                                      +-- STRUCT contradiction
                                      |
                                      +-- A strict reduction
                                      |      -> LIFT-BIND   [row-dependent]
                                      |      -> LIFT-O content [PASS candidate]
                                      |      -> LIFT-VERIFY [UNKNOWN]
                                      |
                                      `-- B
                                             -> B-criticality [UNKNOWN]
                                             -> reduction
                                             -> LIFT-BIND/VERIFY
```

There is no mandatory `JMAP-UNIQUE` node in this root DAG.

A future unique mapper may compress this graph; it may not be required for
logical root closure unless a separate payer/injectivity argument proves that
uniqueness is mathematically necessary.

## 9. Exact current frontier

Priority order after the two new substantive deltas:

1. **Choice-free R-TOTAL / GSRC source-or-escape.**
   For every admissible `(f,p[,g])`, extract the actual source geometry with
   ownership and produce a nonempty globally source-faithful generation
   relation. Do not target R160 directly.

2. **G-COVER.**
   Prove every generated state lies in the explicit coverage union. Duplicate
   descriptions are allowed. Empty or unclassified generation is not.

3. **TNORM + TPROG on the selected-J `d(7)>=7` escape.**
   History-free/local ranks are already refuted.

4. **B-criticality.**
   No completed S12 package exists.

5. **LIFT-BIND + LIFT-VERIFY.**
   Generic theorem content is candidate-PASS; source-row ownership and trusted
   verification remain.

6. **Two-terminal composition under corrected ownership.**
   S04 identity is bound and STANDBY. Any future substantive theorem must use the
   vertex-only `{8,12}` interface, exterior guard ownership, and full positive
   reachability.

## 10. Specialist status after Cycle 5

```text
S09 Cycle 4
  PASS(candidate substantive delta):
  R160 non-inversion + selected-J d(7)>=7 escape
  + source-or-escape target.

S10 Cycle 3
  PASS(candidate substantive delta):
  corrected two-hole ownership/content;
  S11 theorem identity remains source-gated; S04 identity is metadata-bound/STANDBY.

S11 identity-bound theorem
  NOT_VERIFIABLE_MISSING_SOURCE on protected main.
  PR #83 is draft transport of a Lean source and is not a completed/kernel-checked bridge.

S04
  REPOSITORY_BOUND_IDENTITY_ONLY; disposition STANDBY.
  No new theorem or C47 scope extension is promoted.

S12
  no new repository-bound branch/package.

S13
  no post-Cycle-4 generator/mapper package.

S14 / S15
  no new repository-bound branch/package.

S02-A
  no new normalized termination theorem.

S01
  PASS(import/scope only):
  choice-free root semantics + latest completed substantive delta.
```

## 11. Evidence ceiling

All imported mathematical statements remain `candidate_only`.

No Issue/PR/merge/CI state is mathematical Evidence.

At this fresh read:

```text
EvidenceLink ledger   empty
Result ledger         empty
failed-route ledger   empty
best_verified_result  none
root_closed           false
```

Cycle 5 does not alter the admitted sparse formal obligation graph and does not
write any truth/control record.
