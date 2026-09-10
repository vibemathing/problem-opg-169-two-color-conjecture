# R08 S01 Cycle 8 — direct attack on SAME-MINCE JREL-TOTAL

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `0eca6d19e654257d8a98387e0a474d89092e3757`.

No EvidenceLink, Result, Solution, trusted-verifier receipt or root closure is created here.

## 1. Weakest sufficient root theorem

Fix the selected vertex-minimum counterexample `G` used by the candidate route. For an actual unpaid negative triangle `f`, define `LowDesc_G(f,a)` as follows.

A descriptor `a` is either:

- `F(p,s,t,d)`, where `p` is an actual corner of `f`, `s(p)<=5`, `t(p)<=5`, `d=3t+s`, and the fixed-corner C48 finite alternative holds; or
- `SG(p,g,s,t,d)`, where `p` is an actual corner of `f`, `s(p)<=5`, `t(p)>=6`, and `g` is one actual singleton cyclic gap supplied by C48 at `p`.

No canonical corner and no canonical gap is chosen.

Cycle 8 attacks the following theorem, which is weaker than requiring every low descriptor to have a join:

```text
JREL-EX1:
D0_G(f)
 -> exists a,j,
      LowDesc_G(f,a)
   and SameMinCEJREL_G(f,a,j)
   and ClosureEligible_G(j).
```

This is sufficient because the S13-B Cycle-5 one-row EC lemma is consumed in the exact typed form

```text
ONE-ROW-EC:
D0_G(f)
 and LowDesc_G(f,a)
 and SameMinCEJREL_G(f,a,j)
 and ClosureEligible_G(j)
 -> EC_G(f,j),
```

where `EC_G(f,j)` excludes the source row `j` from the assumed minimum counterexample while retaining the same root face/source/payer provenance. Thus one closure-eligible actual join per actual negative face is enough. `JUNIQ` is unnecessary, and no universal quantifier over all low descriptors is required.

The old phrase `JREL-TOTAL` is henceforth interpreted at the root as **per-D0 totality of the relation**: every actual `D0(f)` has at least one accepted output. It does not mean every descriptor has an output.

## 2. Factorization into independently falsifiable edges

Write the theorem as three edges.

### E — entrance

```text
ENT(f): D0_G(f) -> exists a LowDesc_G(f,a).
```

### S — same-MinCE source construction/classification

```text
SRC(f,a):
LowDesc_G(f,a)
 -> exists j,
      SameMinCEJREL_G(f,a,j)
   and SourceClass_G(j).
```

`SourceClass` may be selected-J d6, selected-J high-port, STRUCT, wide-channel/profile class, or another explicitly typed source class. A row label by itself is not a join.

### C — closure eligibility

```text
CLOSE(j):
SameMinCEJREL_G(f,a,j) and SourceClass_G(j)
 -> ClosureEligible_G(j).
```

Only one witness must satisfy all three edges. The root bridge is `E + exists-one(S and C)`, not exhaustive closure of every arithmetic descriptor.

## 3. Entrance E is proved by repository source bytes

C48 Theorem 3.1 proves that if an actual unpaid triangle `f` has negative final charge, then some actual corner `p` has `s(p)<=5`. For that fixed corner exactly one of the fixed-corner alternatives holds:

- `t(p)<=5`, yielding one of the 26 finite integer cells; or
- `t(p)>=6`, yielding at least one singleton cyclic gap.

Therefore `ENT(f)` is candidate-PASS:

```text
D0_G(f) -> exists a LowDesc_G(f,a).
```

For the singleton-gap branch, C48 goes further: after choosing an actual singleton gap, it derives the actual two-sector plane disk, complete degree-four low stars, and the exact three local alias interfaces. Hence SG descriptors possess a source-neutral physical witness in the same `G` before directions are classified.

For the finite branch, the corner itself and its complete actual rotation/star exist in `G`, but C48 does not classify that actual star into a reducible source row.

Crucially C48 explicitly states that it is **not yet a negative-face-to-reducible-parent join theorem**. Its own DAG leaves `exact rotation/direction/alias -> parent generation` open on the finite branch, and leaves source-faithful profile reductions open on the singleton branch.

So Cycle 8 closes E and no more by C48 alone.

## 4. S13-B Cycle 5 typed constructors: conditional soundness, not totality

Cycle-8 orchestration consumes S13-B Cycle 5 as an identity-bound specialist delta with two typed interfaces:

1. fail-closed constructors for physical/source data -> `SameMinCEJREL`;
2. the `ONE-ROW-EC` lemma above.

The constructors are used only conditionally. They do not synthesize missing geometry or root identity.

Let `Gate18_G(f,a,j)` denote the conjunction of the eighteen acceptance cells frozen by the S13-D Cycle-8 fail-closed suite. S01 does not rename or weaken individual specialist cells whose source bytes are not exposed in protected main; it uses the conjunction as the typed constructor premise.

The consumed constructor interface is:

```text
CONSTRUCT-J:
LowDesc_G(f,a)
 and Gate18_G(f,a,j)
 -> SameMinCEJREL_G(f,a,j).
```

The Cycle-8 S13-D suite is consumed as a fail-closed rule:

```text
any missing/false gate -> no SameMinCEJREL constructor result.
```

This is a soundness theorem, not an existence theorem. In particular it does not prove

```text
LowDesc_G(f,a) -> exists j Gate18_G(f,a,j).
```

That existential is the first missing source hypothesis.

The gate suite is essential. C35 and D/3 are controls showing that physical realization is insufficient:

- C35 has an actual twelve-vertex plane orientation with negative faces and a fixed saturated degree-five patch possessing a complete arbitrary-exterior reduction, but the graph is explicitly colourable and is not the assumed minimum counterexample.
- D/3 is an actual physical source control with multiple provenance descriptions, but likewise is not a root minimum-counterexample join.

Therefore a constructor omitting the same-`G` / same actual `D0(f)` identity gates would falsely promote concrete controls into root occurrences.

## 5. Minimal countermodel to source totality

No actual planar noncolourable counterexample is constructed here; doing so would settle the root in the wrong direction. The relevant falsifier is a minimal typed relational model showing that the current source theory does not logically imply `SRC`.

Take one hypothetical minimum-counterexample object `G`, one face `f`, and one descriptor `a`. Interpret

```text
D0_G(f) = true,
LowDesc_G(f,a) = true.
```

Interpret `Gate18_G(f,a,j)` as false for every `j`, so `SameMinCEJREL` is empty. Interpret every C32--C48 unconditional arithmetic/embedding statement exactly as stated and every source-reduction theorem conditionally on its exact source occurrence.

This model satisfies:

- C48 entrance;
- C48 finite/singleton dichotomy;
- all conditional C35/C36/C37 replacement theorems;
- S09's no-registry-inversion discipline;
- S13-B constructor soundness, vacuously because no `Gate18` witness exists;
- S13-D fail-closed semantics.

But it falsifies `JREL-EX1`.

Thus the missing hypothesis is not another arithmetic inequality. It is the source-generation statement

```text
SRC-EX1:
D0_G(f)
 -> exists a,j,
      LowDesc_G(f,a)
   and Gate18_G(f,a,j).
```

Equivalently: at least one C48 low descriptor of every actual negative face must pass all same-MinCE constructor gates and receive an exact source-row identity.

## 6. Source classification after a join: what is already proved

Once an actual join exists, some classification edges are source-backed.

### Selected-J

Merged S09 Cycle 5 starts from an already actual, source-bound selected C35/C36 J occurrence. It proves the disjoint degree cover

```text
d(7)=6  -> exact C37 family/word identity,
d(7)>=7 -> J_HIGHPORT.
```

The degree-six identity is established from actual rotation, alias type and the five physical edge directions **before** R160 is invoked. Hence no registry-to-occurrence inversion occurs.

### C48 channels

C48 itself classifies low descriptors only into finite low-`t` versus singleton-gap channels. It does not prove that either channel always becomes selected-J, STRUCT or another closure-ready row.

### STRUCT and wide-channel

The Cycle-7 S12-A labels and the Cycle-8 S13-A/S13-C source-block updates do not create a source occurrence. A `STRUCT` or wide/profile label can be consumed only after the same-MinCE row and the exact predicate/theorem interface have both been bound.

S13-A Cycle 10 and S13-C Cycle 6 are consumed only as newly confirmed source blocks. They supply no positive `SRC` or `CLOSE` implication and are not mathematical failures. Cycle 8 does not wait for, reconstruct, or reverse-engineer B46.

## 7. A second countermodel: join without closure

Even if `SRC-EX1` is added, closure is not automatic.

Extend the previous typed model by one row `j` with

```text
Gate18_G(f,a,j) = true,
SameMinCEJREL_G(f,a,j) = true.
```

Assign `j` to `J_HIGHPORT`, or to a wide/profile class whose required predicate is source-blocked, and set

```text
ClosureEligible_G(j) = false.
```

This is compatible with the S09 selected-J classifier and the current high-port/wide-channel open frontier. It falsifies `JREL-EX1` even though a same-MinCE join exists.

Thus entrance/source existence and closure are independently falsifiable obligations.

## 8. Closure C: exact selected-J d6 rows are already candidate-eligible

Cycle 7 kept selected-J d6 behind a combined `LIFT-BIND/LIFT-VERIFY` label. Cycle 8 separates mathematical candidate closure from trusted admission.

For an **actual** selected-J d6 Same-MinCE row:

1. S09 Cycle 5 gives one exact C37 family/word identity from the actual geometry.
2. The repository-bound exact C37/R160 parent library supplies a strict smaller simple planar oriented replacement for every exact parent, with all valid complete Q colourings covered and same-boundary lifts satisfying both-colour positive reachability containment.
3. C37's source proof explicitly quantifies arbitrary exterior graphs, keeps every exterior vertex fixed, preserves complete stars/ownership and proves the crossing-cycle replacement argument.
4. S09 Cycle-3 lineage/source identity prevents using a rule on a changed parent.

Therefore at the **candidate mathematical** level:

```text
SameMinCEJREL(selected-J,d6 exact row)
 -> ClosureEligible_CANDIDATE(j).
```

The absent S11 Lean 4.28 receipt remains a block on trusted Evidence/admission, not on this natural-language candidate implication. No EvidenceLink is created.

Consequently the S13-B one-row EC lemma gives the shortest currently source-backed local EC implication:

```text
actual selected-J d6 SameMinCEJREL
 -> exact C37 identity
 -> R160 arbitrary-exterior strict reduction
 -> ClosureEligible_CANDIDATE
 -> ONE-ROW-EC.
```

This still does **not** prove that any actual `D0` has such a join.

## 9. STRUCT versus selected-J d6 versus wide-channel

Three possible one-row witnesses must be distinguished.

### Selected-J d6

This is the **shortest currently attainable from source-backed post-join mathematics**. After the same-MinCE join, exact classification and arbitrary-exterior strict reduction are already repository-bound at candidate level.

Remaining root missing input: the actual join itself.

### STRUCT

A STRUCT row would be logically even shorter **if** it arrived with the exact same-MinCE separator geometry and the structural contradiction certificate already attached: then the one-row EC lemma needs no replacement/lifting step.

But the currently available STRUCT labels do not themselves provide those same-MinCE premises. Therefore STRUCT is not currently a more attainable witness than selected-J d6.

### Wide-channel / profile channel

This is not shortest. Its exact source/predicate/closure interface is among the newly confirmed S13-A/S13-C source blocks or the open flip-star/high-port frontier. It has no comparable source-backed one-row closure theorem.

Hence the operational ranking is:

```text
source-backed attainable after join: selected-J d6  [best]
logical edge-count if a full separator cert appeared: STRUCT
currently open/blocked: wide-channel
```

## 10. The maximal theorem proved in Cycle 8

Cycle 8 proves the following composite conditional theorem.

### Theorem JREL-EX1-COND

For every actual `D0_G(f)`:

1. there exists a C48 low descriptor `a`;
2. for any `a,j`, if all S13-D constructor gates hold then S13-B constructs `SameMinCEJREL_G(f,a,j)`;
3. if that `j` is an exact selected-J d6 row, source-backed C37/R160 mathematics makes it candidate closure-eligible and S13-B's one-row lemma excludes it;
4. the same one-row lemma applies to any other row once its exact `ClosureEligible` payload is supplied.

What is **not** proved is the existential middle statement that some descriptor of every actual `D0` passes the constructor and lands in an eligible class.

So the exact remaining theorem is

```text
JREL-GOOD-EX1:
D0_G(f)
 -> exists a,j,
      LowDesc_G(f,a)
   and Gate18_G(f,a,j)
   and ClosureEligible_G(j).
```

Because `CONSTRUCT-J` is already available, `JREL-GOOD-EX1` is equivalent to the desired `JREL-EX1` at the current interface.

## 11. Updated row-level cut matrix

| lane | entrance / physical | same-MinCE constructor | source classification | closure candidate | first missing item |
|---|---|---|---|---|---|
| C48 finite `F` descriptor | PASS actual corner/star | **OPEN existential** | only 26 arithmetic cells | not uniform | one Gate18 exact source row |
| C48 singleton `SG` descriptor | PASS actual two-sector disk / 3 alias types | **OPEN existential** | 192 local direction targets only | not uniform | one Gate18 exact source row |
| D/3 multi-root control | PASS control geometry | FAIL-CLOSED as root join | exact D/3 control | local control only | same-MinCE graph/root-face identity |
| C35 canary/control | PASS `actual_c35_face_geometry_certified_unjoined` | FAIL-CLOSED as root join | local C35 row | local reduction can be complete | same-MinCE graph/root-face identity |
| selected-J input | conditional | requires Gate18 | S09 C5 d6/high-port cover | partial | actual selected-J join |
| selected-J d6 | PASS once joined | PASS once actual | exact C37 family/word | **PASS candidate math** via R160 | actual join; trusted admission separate |
| selected-J high-port | PASS once joined | PASS once actual | `J_HIGHPORT` | OPEN | TPROG/useful terminal theorem |
| STRUCT | row-dependent | requires Gate18 | label/predicate required | conditional | actual row + separator certificate |
| wide/profile | row-dependent | requires Gate18 | source-blocked/open | BLOCKED | exact source predicate/closure theorem |
| B46 historical | no usable row IDs | n/a | n/a | n/a | source transport; deliberately bypassed |
| final root | C48 entrance PASS | **JREL-GOOD-EX1 OPEN** | one eligible class sufficient | ONE-ROW-EC available | constructor existence |

## 12. Updated root DAG

```text
minimum counterexample G
 |
 +-- Sigma mu=-8 -> actual D0(f)
 |
 +-- C48
 |     -> exists LowDesc(f,a)                         [PASS candidate]
 |            |
 |            +-- finite F actual rooted corner/star
 |            `-- SG actual two-sector disk / alias type
 |                    |
 |                    v
 |             exists j Gate18(f,a,j)                 [FIRST OPEN ROOT CUT]
 |                    |
 |                    v
 |             SameMinCEJREL(f,a,j)                   [constructor PASS conditional]
 |                    |
 |                    +-- selected-J d6
 |                    |      -> exact C37 identity
 |                    |      -> R160 arbitrary-exterior reduction
 |                    |      -> ClosureEligible       [PASS candidate math]
 |                    |      -> ONE-ROW-EC
 |                    |
 |                    +-- STRUCT
 |                    |      -> exact separator cert  [OPEN]
 |                    |      -> ClosureEligible
 |                    |      -> ONE-ROW-EC
 |                    |
 |                    +-- selected-J J_HIGHPORT       [TPROG OPEN]
 |                    |
 |                    `-- wide/profile                [SOURCE/CLOSURE BLOCK]
 |
 `-- one EC witness for every D0
       -> no actual negative face
       -> contradict Sigma mu=-8.
```

The direct root priority is now sharper than Cycle 7:

```text
FIRST: produce one Gate18 same-MinCE row from one C48 LowDesc per D0.
THEN: preferentially land it in selected-J d6, because that class already has candidate one-row closure.
```

No B46 reconstruction is on this shortest route.

## 13. Status

```text
ENTRANCE_C48_LOW_DESC               PASS(candidate)
S13B_TYPED_CONSTRUCTOR_SOUNDNESS     PASS(candidate, identity-bound specialist delta)
S13D_18_GATE_FAIL_CLOSED             PASS(candidate, identity-bound specialist delta)
SAME_MINCE_CONSTRUCTOR_EXISTENCE     UNKNOWN / FIRST ROOT CUT
S09_SELECTED_J_CLASSIFIER            PASS(candidate after join)
SELECTED_J_D6_CLOSURE_ELIGIBLE       PASS(candidate mathematics)
STRUCT_ONE_ROW_ELIGIBILITY            OPEN actual separator certificate
WIDE_CHANNEL_ELIGIBILITY             BLOCK/OPEN
S13A_C10_SOURCE_BLOCK                BLOCK, not failure
S13C_C6_SOURCE_BLOCK                 BLOCK, not failure
S11_KERNEL_RECEIPT                   BLOCK for trusted admission, not candidate math
JREL-EX1                             UNKNOWN
JCLOSE-EC                            UNKNOWN root-wide
best_verified_result                 none
root_closed                          false
```

No EvidenceLink, Result, Solution or trusted mathematical admission is created.