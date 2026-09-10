# R08 S01 Cycle 9 — FECT entrance integration and tag-total closure cut

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `40ac4def8af108b9da2333cea7798ce7491dc8c8`.

This is an S01 integration checkpoint. It changes only the candidate proof DAG and the location of the first root cut. It creates no EvidenceLink, Result, Solution, trusted-verifier receipt, or root closure.

## 1. Starting point from Cycle 8

Cycle 8 proved from repository-bound C48 source bytes that every actual unpaid negative face has at least one actual low descriptor:

```text
ENT:
D0_G(f) -> exists a, LowDesc_G(f,a).
```

It also separated candidate mathematical closure from trusted admission: once an **actual exact selected-J d(7)=6 row** is bound, S09 Cycle 5 identifies the exact C37 family/word before R160 is used, and C37/R160 supplies a strict arbitrary-exterior complete-Q positive-reachability reduction. Thus the selected-J d6 EC suffix is already candidate-mathematical content; absent trusted replay blocks Evidence admission only.

The Cycle-8 first missing edge was written as an existential Gate18/SameMinCE row constructor.

## 2. S13-B Cycle 6 FECT moves the entrance cut forward

Cycle-9 orchestration supplies the identity-bound S13-B Cycle-6 **First Exposure Classification Theorem (FECT)** in the following source-faithful form.

For the assumed vertex-minimum counterexample `G`, an actual `D0_G(f)`, and an actual C48 low descriptor `a`, the finite rotation of `G` can be read into one same-face `FirstExposureRecord_G(f,a,r)` while preserving:

- the physical graph identity `G`;
- the same actual root face `f` and the low-descriptor provenance;
- alias normalization and the actual alias classes;
- the complete exposed contacts / controlled-star information recorded by the constructor;
- edge/face ownership;
- source/payer identity carried from the charge ledger.

The record receives one of the six tags

```text
F0_ROOT_STAR
J_READY
COMPACT_NONJ
NONJ_QARC
PINCHED_MULTICONTACT
WIDE_CHANNEL.
```

S01 consumes FECT only at this stated type. No repository SHA, row ID, exact source predicate, or stronger closure statement is invented for specialist bytes not exposed on the fresh protected-main cutoff.

Therefore, composing C48 with FECT gives the new entrance theorem

```text
FECT-ENTRANCE:
D0_G(f)
 -> exists a,r,
      LowDesc_G(f,a)
   and FirstExposureRecord_G(f,a,r)
   and Tag6(r).
```

This is a genuine improvement over Cycle 8: the actual MinCE geometry is no longer stopped at an arithmetic/local descriptor. It is now read into an actual same-face, ownership-preserving, payer-preserving exposure record in a finite six-tag source partition.

## 3. Audit against Cycle-8 Gate18 semantics

FECT does **not** by itself prove entrance-level `SameMinCEJREL` under the existing S01 Gate18/type-J semantics.

Cycle 7/8 deliberately required a Type-J record to carry an **exact source-row key** in addition to same-`G`, same-face, aliases, contacts, complete stars, ownership and payer/source provenance. Cycle 8 wrote the constructor as

```text
LowDesc_G(f,a) and Gate18_G(f,a,j)
 -> SameMinCEJREL_G(f,a,j).
```

FECT discharges the entrance-level physical/provenance part of that contract: same MinCE, same face, finite actual rotation, aliases, contacts, ownership and payer data are now present in `r`. But a tag such as `J_READY` or `NONJ_QARC` is a **source class**, not an exact row identity. FECT as supplied does not name the exact C35/C36/C37 row, compact-row key, q-arc row, pinched row, or wide-channel row that Type J requires.

Hence introduce an explicit row-binding relation

```text
ExactRowBind_G(r,j),
```

meaning that `j` is an exact source-row identifier whose physical realization is exactly the FirstExposureRecord `r`, with no changed alias, contact, ownership, payer, edge direction, face, or controlled-star datum, and whose row tag agrees with `tag(r)`.

The correct constructor boundary is now

```text
FER-ROW-CONSTRUCT:
FirstExposureRecord_G(f,a,r)
 and ExactRowBind_G(r,j)
 -> SameMinCEJREL_G(f,a,j).
```

Any additional row-specific Gate18 cell remains part of `ExactRowBind`; FECT is not used to weaken the fail-closed suite.

So the answer to the Cycle-9 audit is:

```text
FECT proves same-MinCE exposure existence: YES.
FECT alone proves SameMinCEJREL existence under Gate18: NO.
Exact source-row identity still needs a separate constructor/binding: YES.
```

## 4. Minimal typed countermodel showing why the row constructor is necessary

Take one hypothetical MinCE object `G`, one actual negative face `f`, one low descriptor `a`, and one exposure record `r`. Interpret

```text
D0_G(f) = true,
LowDesc_G(f,a) = true,
FirstExposureRecord_G(f,a,r) = true,
tag(r) = J_READY,
```

and give `r` all physical/provenance data promised by FECT. Let the exact source-row universe contain no row `j` satisfying `ExactRowBind_G(r,j)`.

This model satisfies C48 entrance and the FECT theorem exactly, plus every existing source theorem that is conditional on an exact source occurrence. But `SameMinCEJREL` remains empty under the Cycle-8 type-J definition.

Thus no logical inference

```text
FirstExposureRecord -> SameMinCEJREL
```

is valid without a row-binding hypothesis. The missing fact is no longer an 18-cell geometry existential; it is the much narrower exact-row realization step.

## 5. Replace SRC-EX1 by the weakest correct tag-total closure theorem

The root never needed every `LowDesc` to map, and FECT does not require a canonical descriptor or unique exposure record. The weakest root statement after FECT is therefore still existential over the actual FECT outputs:

```text
FECT-GOOD-EX1:
D0_G(f)
 -> exists a,r,j,
      LowDesc_G(f,a)
   and FirstExposureRecord_G(f,a,r)
   and ExactRowBind_G(r,j)
   and ClosureEligible_G(j).
```

This is the direct replacement for Cycle-8 `SRC-EX1/JREL-GOOD-EX1`.

For a finite compositional proof it is useful to define, for each tag `tau`,

```text
TagClose_tau(r) :=
  tag(r)=tau
  and exists j,
       ExactRowBind_G(r,j)
   and ClosureEligible_G(j).
```

A uniform six-tag theorem

```text
TAG-TOTAL-CLOSE:
FirstExposureRecord_G(f,a,r)
 -> TagClose_F0(r)
    or TagClose_JREADY(r)
    or TagClose_COMPACT(r)
    or TagClose_QARC(r)
    or TagClose_PINCHED(r)
    or TagClose_WIDE(r)
```

is sufficient with FECT-ENTRANCE and ONE-ROW-EC. If FECT admits multiple possible records for one `(f,a)`, this uniform theorem is stronger than the bare root existential `FECT-GOOD-EX1`; S01 does not silently claim equivalence. The root-exact obligation is `FECT-GOOD-EX1`; `TAG-TOTAL-CLOSE` is the clean finite program for proving it without a selector.

`JUNIQ` remains optional.

## 6. J_READY: d6 candidate EC suffix is closed, row binding is the only prefix cut

For an **actual** FECT record tagged `J_READY`, once an exact selected-J source row `j` is bound, merged S09 Cycle 5 supplies

```text
d(7)>=6,
```

with the exact split

```text
d(7)=6  -> actual rotation/alias/directions determine exact C37 family/word;
d(7)>=7 -> J_HIGHPORT.
```

Therefore the d6 suffix is now frozen as

```text
J_READY exposure
 -> ExactRowBind to actual selected-J row                   [OPEN prefix]
 -> d(7)=6
 -> exact C37 identity                                     [PASS candidate]
 -> R160 arbitrary-exterior strict reduction              [PASS candidate]
 -> ClosureEligible_CANDIDATE                              [PASS candidate]
 -> ONE-ROW-EC                                             [PASS candidate].
```

Status:

```text
J_READY_D6_ROW_BIND = OPEN
J_READY_D6_EC_SUFFIX = PASS(candidate mathematics)
TRUSTED_ADMISSION = separate / not supplied
```

No atlas or R160 registry is inverted into occurrence.

## 7. The other five tags: first closure lemma after row binding

Every tag still first needs `ExactRowBind`. The table below names the **first closure theorem after that common constructor**.

| FECT tag | first closure lemma after exact row binding | current state |
|---|---|---|
| `F0_ROOT_STAR` | **F0-ROOT-CLOSE:** every exact F0 root-star row has a source-faithful STRUCT contradiction or strict arbitrary-exterior replacement | OPEN; C32 root-star/wheel work contains residual types, so generic star reducibility cannot be assumed |
| `COMPACT_NONJ` | **COMPACT-NONJ-CLOSE:** every exact compact non-J row admits a finite bounded-interface complete-Q/full-`R+` reduction or STRUCT closure | OPEN; compactness suggests finite closure but no total row theorem is consumed here |
| `NONJ_QARC` | **D4-ENDPOINT-TOPOLOGY:** instantiate the exact q-arc row in the S12-A symbolic D4 schema and convert its symbolic blocker structure into an actual endpoint-valid separator/reduction | OPEN only at endpoint-sensitive topology after the D4 symbolic payload is bound |
| `PINCHED_MULTICONTACT` | **PINCH-MULTICONTACT-COMPOSE:** exact same-MinCE multiconact/pinched composition with aliases, ownership and full positive `R+` over the real interface | OPEN; no tournament/same-boundary shortcut |
| `WIDE_CHANNEL` | **WIDE-TPROG:** a source-faithful finite-state/profile or well-founded terminal-usefulness theorem for the growing wide interface | OPEN; longest current lane |

### Operational ranking among the five non-J tags

After the common exact-row constructor, the shortest currently visible non-J closure path is

```text
1. NONJ_QARC
2. COMPACT_NONJ
3. F0_ROOT_STAR
4. PINCHED_MULTICONTACT
5. WIDE_CHANNEL.
```

Reason for rank 1: Cycle-9 S12-A has already supplied a substantial symbolic D4 theorem for the q-arc-style closure interface; the remaining mathematical obstruction is endpoint-sensitive topology rather than the earlier fibre/SCC/flip algebra. The rank is conditional on the exact `NONJ_QARC -> D4` row instantiation being supplied by `ExactRowBind`; tag text alone is not used as that identity.

`COMPACT_NONJ` is next because its interface is bounded and therefore amenable to a finite complete-Q/full-`R+` closure theorem. `F0_ROOT_STAR` remains behind it because repository C32 already exhibits genuine residual root-star/wheel types, so a naive universal star replacement is known to be insufficient. `PINCHED_MULTICONTACT` needs topology/ownership-sensitive composition, and `WIDE_CHANNEL` still needs a global terminal/profile theorem.

## 8. S12-A Cycle 9 symbolic D4 payload

Cycle-9 orchestration supplies the S12-A Cycle-9 D4 result with the following exact trust boundary.

The following are theoremically available inside the symbolic D4 schema:

```text
rigid fibre structure,
SCC formulation/control,
four flip blockers,
pair-phase organization.
```

What is **not** available is the endpoint-sensitive planar/topological implication that turns those symbolic facts into a valid same-MinCE closure certificate.

Therefore S01 records

```text
D4_FIBRE = PASS(candidate theorem content)
D4_SCC = PASS(candidate theorem content)
D4_FOUR_FLIP_BLOCKERS = PASS(candidate theorem content)
D4_PAIR_PHASE = PASS(candidate theorem content)
D4_ENDPOINT_TOPOLOGY = OPEN
```

and does not write `D4 closed`.

The D4 theorem is consumed only after an exact FECT row is shown to instantiate its source schema. In particular a tag name by itself does not prove the D4 hypotheses.

## 9. Updated cut matrix

| lane | C48 LowDesc | FECT same-MinCE exposure | exact source-row bind | closure suffix | first missing item |
|---|---|---|---|---|---|
| root entrance | PASS | **PASS candidate FECT** | n/a | n/a | none at exposure level |
| `J_READY,d6` | PASS | PASS when tagged | **OPEN** | **PASS candidate EC suffix** | exact selected-J row key |
| `J_READY,high-port` | PASS | PASS when tagged | OPEN | OPEN | exact row key, then TPROG |
| `F0_ROOT_STAR` | PASS | PASS when tagged | OPEN | OPEN | exact row key, then F0-ROOT-CLOSE |
| `COMPACT_NONJ` | PASS | PASS when tagged | OPEN | OPEN | exact row key, then COMPACT-NONJ-CLOSE |
| `NONJ_QARC` | PASS | PASS when tagged | OPEN | D4 symbolic core available | exact row key; then endpoint topology |
| `PINCHED_MULTICONTACT` | PASS | PASS when tagged | OPEN | OPEN | exact row key; then multiconact composition |
| `WIDE_CHANNEL` | PASS | PASS when tagged | OPEN | OPEN | exact row key; then WIDE-TPROG |
| D/3 control | control only | not a root FECT occurrence | n/a | control only | no promotion |
| C35 control | control only | `actual_c35_face_geometry_certified_unjoined` remains non-root control | n/a | local certificates only | no promotion |
| final root | PASS | **PASS exposure totality** | **FIRST OPEN ROOT CUT** | one eligible tag suffices | `FECT-GOOD-EX1` / common row constructor |

No B46 lane is used.

## 10. Updated sole root DAG

```text
minimum counterexample G
 |
 +-- Sigma mu=-8
 |     -> actual D0_G(f)
 |
 +-- C48
 |     -> exists LowDesc_G(f,a)                           [PASS]
 |             |
 |             v
 +-- S13-B C6 FECT
 |     -> exists same-face FirstExposureRecord r         [PASS candidate]
 |     -> aliases/contacts/ownership/payer preserved
 |     -> tag(r) in
 |        {F0_ROOT_STAR, J_READY, COMPACT_NONJ,
 |         NONJ_QARC, PINCHED_MULTICONTACT, WIDE_CHANNEL}
 |             |
 |             v
 +-- ExactRowBind_G(r,j)                                  [FIRST OPEN CUT]
 |     -> SameMinCEJREL_G(f,a,j)
 |             |
 |             +-- J_READY,d6
 |             |     -> C37/R160 -> ONE-ROW-EC            [suffix PASS]
 |             |
 |             +-- J_READY,high-port -> TPROG             [OPEN]
 |             +-- F0_ROOT_STAR -> F0-ROOT-CLOSE          [OPEN]
 |             +-- COMPACT_NONJ -> COMPACT-NONJ-CLOSE    [OPEN]
 |             +-- NONJ_QARC -> D4 symbolic core          [PASS core]
 |             |                -> endpoint topology      [OPEN]
 |             +-- PINCHED_MULTICONTACT -> composition    [OPEN]
 |             `-- WIDE_CHANNEL -> WIDE-TPROG             [OPEN]
 |
 `-- FECT-GOOD-EX1 for every actual D0
       -> ONE-ROW-EC for one actual row per face
       -> no actual negative face
       -> contradiction with Sigma mu=-8.
```

## 11. One highest-value next theorem

The highest-value next theorem is not a tag-specific colouring enumeration. It is the common constructor that moves every FECT output across the current first cut:

```text
FECT-ROW-TOTAL:
For every actual FirstExposureRecord_G(f,a,r),
there exists an exact source-row key j such that
  ExactRowBind_G(r,j)
  and SameMinCEJREL_G(f,a,j)
  and RowTag(j)=tag(r),
with every physical vertex/arc/rotation/alias/contact/ownership/payer datum
identical to r.
```

Why this theorem has highest value:

1. it is exactly the first open implication after a now-total same-MinCE exposure theorem;
2. it is shared by all six tags, so it avoids six duplicated occurrence proofs;
3. for an actual `J_READY,d6` output it immediately reaches an already closed candidate EC suffix;
4. for `NONJ_QARC` it exposes the exact endpoint-topology obligation on top of the already available S12-A D4 symbolic core;
5. it cannot be faked by D/3, C35, atlas counts or class labels, because the theorem requires exact same-MinCE row identity and byte-for-byte physical/provenance agreement.

A weaker root theorem could existentially bind only one good FECT output per `D0`; a stronger universal row constructor is recommended here because it attacks the common first cut directly. S01 does **not** claim it has been proved.

## 12. Truth boundary

This Cycle-9 integration remains candidate-only.

- no EvidenceLink is created;
- no Result or Solution is created;
- no B46 recovery is attempted;
- no tag count is interpreted as occurrence;
- no exact row key is invented from a tag;
- no trusted kernel/admission receipt is claimed;
- `best_verified_result=none`;
- `root_closed=false`.
