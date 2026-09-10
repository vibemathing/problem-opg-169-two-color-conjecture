# R08 S01 Cycle 12 — physical identity, proper locality, relation cover, proof-carrying closure

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `81932d240289c11855614fc4c9c0873902053e5f`.

No EvidenceLink, Result, Solution, trusted-verifier receipt, B46 dependency, or root closure is created here.

## 1. Cycle-11 boundary and the Cycle-12 correction

Cycle 11 repaired the six FECT names from a purported disjoint partition to an overlap-permitting relation. Its sole DAG ended at

```text
D0
 -> LowDesc
 -> actual FirstExposureRecord (FER)
 -> precedence-free RawSourceRow
 -> SameMinCEJREL0
 -> FER-CLASS-COVER
 -> exists one admissible closed class witness
 -> ONE-ROW-EC.
```

The new S10 Cycle-7 clean-room audit is consumed in the exact tag-free sense supplied to S01: raw physical identity must not depend on the starting index chosen to print a cyclic rotation, but it must retain the actual occurrence anchor and root/provenance data. The same audit separates a physical occurrence record from a **proper local replacement interface**.

The S15 concern is decisive at this second boundary. If contact completion is implemented as a fixed-point rule that recursively absorbs every newly touched contact endpoint and then completes its star, the least fixed point can equal all of a connected `G`. Such a full-graph occurrence may still satisfy every same-MinCE physical/provenance identity check. It is nevertheless useless for any local strict-replacement theorem whose interface requires a proper patch with an exterior boundary.

Therefore Cycle 12 does **not** retract content-derived physical occurrence identity. It splits the old overloaded `RAW-PHYS-EXTRACT` claim into:

```text
RAW-ID-EXTRACT       -- actual physical/provenance identity only
PROPER-ROW-EXTRACT   -- a proper, boundary-closed local support usable by closure theorems
```

Only the first is retained as candidate-PASS. The second is restored as the first root cut.

No repository-bound S10 Cycle-7 specialist package with an exact digest was found on protected main at this cutoff. The supplied S10 finding is therefore consumed as an identity-bound orchestration input and no repository SHA or row set is fabricated for it.

## 2. Cyclic-presentation-invariant physical payload

Fix the selected finite plane minimum counterexample `G`, one actual unpaid negative face `f`, one C48 low descriptor `a`, and an actual FECT record `r` read from the same `G,f`.

Cycle 11 used literal ordered rotation tuples in its explanatory key. Cycle 12 replaces those presentation tuples by the underlying cyclic structures.

### 2.1 Occurrence support and aliases

Let `Supp_V(r)` be the actual vertices explicitly controlled by the FER stopping support before any recursive contact saturation. Let `Supp_A(r)`, `Supp_F(r)` and `Supp_C(r)` be respectively its actual source/QARC arcs, exposed faces/holes, and explicitly carried contact incidences.

Symbolic FER roles are quotient-normalized by equality of their actual realizations in `G` before any geometry comparison. The resulting alias classes carry their actual realization map back to `G`.

### 2.2 Cyclic rotations without a starting dart

For every controlled vertex `v`, let `D_v` be the typed actual darts recorded at `v`. Instead of storing a tuple

```text
(d_0,d_1,...,d_{k-1})
```

with an arbitrary index zero, store the cyclic successor relation

```text
RotSucc_v subset D_v x D_v,
```

where every dart has exactly one successor and predecessor in the actual plane rotation. The mathematical object is unchanged by cyclically shifting a printed tuple. Reversal is **not** identified: the fixed plane rotation orientation remains part of the occurrence.

For any complete-star vertex, `D_v` is the full actual star in `G`. For a boundary-controlled vertex, the payload records every support dart plus every explicit contact position used by the row; completeness is a later locality condition unless FECT explicitly declares the star complete.

### 2.3 Faces, holes and boundary components

Each actual exposed face, hole or cyclic boundary component is likewise stored by its cyclic successor relation on the realized boundary darts rather than by an arbitrary first position. A linear interval between two distinguished actual endpoints remains linear and retains its two endpoint marks.

### 2.4 Anchor and provenance are retained

Cyclic presentation invariance does not mean anchor erasure. The physical identity retains:

- the same assumed `G`;
- actual root face `f`;
- C48 low descriptor `a`, including the actual corner and actual singleton gap when applicable;
- the FER stopping/entry occurrence marks needed to identify the source-facing support inside `G`;
- all actual payer/source IDs and no-double-spending ownership keys;
- actual source/exterior ownership of recorded objects.

These are **occurrence anchors/provenance**. Later theorem-specific choices such as a selected q-arc, selected wheel center, chosen compact enlargement, pinched decomposition, or wide subinterval are class witnesses and do not belong to physical identity.

### 2.5 Tag-free payload object

Define

```text
RawPhysicalPayload_G(f,a,r) :=
(
  actual occurrence support,
  alias quotient and realization map,
  all RotSucc_v cyclic relations,
  all exposed face/hole cyclic relations,
  source and QARC arcs,
  explicit contact incidences and rotation positions,
  source/exterior ownership,
  payer/source IDs,
  occurrence anchors and root provenance
).
```

No FECT class name, class precedence, scheduler output or class-specific anchor occurs in this object.

For transport one may serialize a cyclic relation by choosing the lexicographically least rotation of a typed token sequence after alias normalization, but the **mathematical identity is the cyclic relation/equivalence class itself**. No proof depends on the serializer choice or a digest collision assumption.

A `RawPhysicalRow_G(f,a,j)` contains this payload plus the occurrence binding back to actual objects of `G`.

## 3. RAW-ID-EXTRACT survives

### Lemma 3.1 — RAW-ID-EXTRACT

```text
FirstExposureRecord_G(f,a,r)
 -> exists unique j RawPhysicalRow_G(f,a,j).
```

**Candidate proof.** The same actual embedded graph, FER stopping support and preserved source/payer data determine every field in Section 2. Replacing a linear presentation of a cyclic rotation by its successor relation removes artificial start-index dependence and therefore cannot create a second physical occurrence. Conversely any two payloads differing in an actual alias, cyclic successor, exposed face incidence, source/QARC/contact arc, ownership key, payer/source ID, root face or occurrence anchor disagree on the same actual `G,f,r`. Thus the tag-free physical row is unique.

This lemma is about **identity only**. It does not say that its support is a proper subset of `G` or that every boundary incidence needed by a replacement theorem has been captured.

### Lemma 3.2 — RAW-ID-JREL0

```text
RawPhysicalRow_G(f,a,j)
 -> SameMinCEJREL0_G(f,a,j).
```

Here `SameMinCEJREL0` means only same-MinCE physical/provenance occurrence: same `G`, same actual `D0` face provenance, exact aliases, actual cyclic rotations/faces on the carried support, actual source/QARC/contact objects, ownership and payer/source identity. It is intentionally weaker than “usable proper local replacement row”.

Cycle 12 therefore retains `RAW-ID-EXTRACT` and `RAW-ID-JREL0` as candidate-PASS while removing them from the list of sufficient premises for `CatalogueMatch`.

## 4. The explicit locality gates

Let `S(j)=Supp_V(j)` be the actual vertex support of a raw row.

### 4.1 ProperFiniteSupport

Define

```text
ProperFiniteSupport_G(j) :=
  S(j) is finite
  and S(j) is a strict subset of V(G).
```

The finiteness clause alone is automatic for a finite `G`; it is written explicitly because later theorem libraries operate on finite patch interfaces. The substantive clause is **properness**: at least one actual vertex of `G` remains exterior to the support.

When a particular strict replacement theorem uses a stronger order than vertex number, its own theorem-specific `StrictDecrease` premise is still required. `ProperFiniteSupport` only guarantees a nontrivial local/exterior split; it does not by itself prove the replacement is smaller.

### 4.2 BoundaryClosedSupport

For an actual support `S`, let

```text
Cross_G(S) :=
  { directed arc incidences xy of G : exactly one of x,y lies in S }.
```

Define `BoundaryClosedSupport_G(j)` to require:

1. every incidence in `Cross_G(S(j))` is represented exactly once after alias normalization by a boundary/contact entry of `j` with its actual direction;
2. every recorded boundary/contact entry is an actual crossing incidence of `G` (or an explicitly typed boundary-face incidence required by the row), not a fabricated local edge;
3. the source-side rotation position of every crossing incidence is recorded in the cyclic rotation relation;
4. source/exterior ownership and payer/source keys agree with the actual source ledger;
5. every vertex declared to have a complete exposed star is checked against its full actual incidence set in `G`;
6. there is no unrecorded source-owned/QARC arc crossing the support boundary;
7. **boundary enumeration does not recursively absorb the exterior endpoint into `S(j)` merely because it appears in a contact entry.**

Item 7 is the critical distinction between boundary closure and contact saturation. A local patch can know every arc crossing its boundary without turning every exterior contact endpoint into an interior controlled vertex.

For a concrete finite row this predicate is checkable from the actual `G`. Cycle 12 does not infer it merely from a producer class label.

### 4.3 ProperLocalRow

Define

```text
ProperLocalRow_G(f,a,j) :=
  RawPhysicalRow_G(f,a,j)
  and SameMinCEJREL0_G(f,a,j)
  and ProperFiniteSupport_G(j)
  and BoundaryClosedSupport_G(j).
```

From Cycle 12 onward **no `CatalogueMatch`, strict replacement rule, LIFT-O wrapper or class closure certificate may be invoked before `ProperLocalRow` is established.**

## 5. S15 fixed-point contact-closure falsifier

The concern that contact closure can swallow all of `G` is real at the logical level.

Take any connected finite underlying graph `G` and any nonempty seed support `S_0`. Consider the completion operator

```text
C(S) := S union { y : some x in S has an actual contact/incidence xy in G }.
```

If an implementation additionally completes the full star of every newly absorbed endpoint, this only enlarges `C` faster. Let

```text
S_infty := union_n C^n(S_0).
```

Because `G` is connected, every vertex has finite graph distance from `S_0`; induction on that distance gives

```text
S_infty = V(G).
```

At the fixed point every actual arc, rotation and ownership datum can still be recorded correctly. The boundary is empty, so the resulting full-graph physical occurrence can satisfy `RawPhysicalRow` and `SameMinCEJREL0`. It fails only

```text
ProperFiniteSupport_G(j).
```

Nothing in same-MinCE identity forbids this.

This is a typed locality countermodel, not an actual non-2-colorable planar orientation. It shows that the old implication

```text
FER -> root-usable local row
```

cannot be obtained from finite physical extraction plus contact saturation alone.

A full-graph row may in principle admit some wholly global strict reduction theorem, but none of the current local patch/catalogue interfaces is licensed to assume such a theorem. In particular, “the row is all of G” cannot be used to infer a same-boundary local replacement or an arbitrary-exterior lift.

## 6. PROPER-ROW-EXTRACT is restored as the first cut

The exact missing theorem is

```text
PROPER-ROW-EXTRACT:
FirstExposureRecord_G(f,a,r)
 -> exists j,
      RawPhysicalRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and ProperFiniteSupport_G(j)
   and BoundaryClosedSupport_G(j).
```

Because `RAW-ID-EXTRACT` gives a unique physical row, this is equivalently the assertion that the unique FER row is proper and boundary-closed.

Cycle 12 marks:

```text
RAW-ID-EXTRACT        PASS(candidate)
RAW-ID-JREL0          PASS(candidate)
PROPER-ROW-EXTRACT    OPEN_FIRST_ROOT_CUT
```

The source material presently consumed for FECT supplies finite same-MinCE stopping data but no theorem that an exterior vertex must remain outside the fixed-point physical/contact completion. Therefore proper locality is **not derivable from FER at the current interface**.

This cut is earlier than the Cycle-11 `FER-CLASS-COVER` cut. Classification is irrelevant until a root-usable local occurrence exists.

## 7. Relation-valued class cover moves after locality

The six source classes remain the overlap-permitting relation

```text
AdmissibleClass_G(j,tau,w),
```

with

```text
tau in {
  F0_ROOT_STAR,
  J_READY,
  COMPACT_NONJ,
  NONJ_QARC,
  PINCHED_MULTICONTACT,
  WIDE_CHANNEL
}.
```

`w` carries the class-specific witness/anchor. Multiple pairs may apply to one `j`. No precedence or scheduler is part of the theorem.

The modular class-cover theorem is now explicitly local:

```text
LOCAL-FER-CLASS-COVER:
FirstExposureRecord_G(f,a,r)
 and ProperLocalRow_G(f,a,j)
 -> exists tau,w AdmissibleClass_G(j,tau,w).
```

Cycle 11's S10 overlap/gap audit still applies: overlap is harmless, but literal semantic gaps mean this total cover is not currently proved. Thus

```text
LOCAL-FER-CLASS-COVER   OPEN_SECOND_ROOT_CUT
```

once `PROPER-ROW-EXTRACT` is supplied.

No producer label, row count, finite catalogue count or scheduler output discharges this theorem.

## 8. Proof-carrying closure acceptance: EXISTS, never ALL

For an actual local row define a proof-carrying certificate

```text
ClosureEligibleCert_G(j,tau,w,kappa)
```

to mean that `kappa` contains the actual source-valid discharge for this row/witness. Depending on the lane it includes a strict replacement with exact boundary/lifting data, a structural contradiction, or another source-faithful exclusion theorem. In every replacement lane it must carry the theorem-specific geometry, guards, ownership, nonvacuous complete-Q quantifier and positive-reachability data actually required by that theorem.

The root acceptance predicate is

```text
ExistsClosureCert_G(j) :=
  exists tau,w,kappa,
    AdmissibleClass_G(j,tau,w)
    and ClosureEligibleCert_G(j,tau,w,kappa).
```

This is scheduler independent. Reordering classes, adding duplicate witnesses, or choosing a different unused admissible anchor does not change whether the existential proof certificate exists.

Cycle 12 explicitly does **not** require

```text
forall tau,w,
  AdmissibleClass(j,tau,w) -> exists kappa ClosureEligibleCert(j,tau,w,kappa).
```

That arbitrary-choice robustness is stronger than the root proof needs. One actual proof-carrying closure certificate is enough for the S13-B one-row exclusion interface.

## 9. CatalogueMatch is now a third-stage relation

For any existing theorem catalogue `C`, define

```text
CatalogueMatch_C(j,c)
```

only under the premise `ProperLocalRow(j)`. A valid match must compare the already actual local payload with the theorem row's exact hypotheses, including cyclic geometry, boundary contacts, ownership and every theorem-specific guard.

The only allowed direction is

```text
actual FER
 -> RawPhysicalRow
 -> ProperLocalRow
 -> optional AdmissibleClass witness
 -> optional CatalogueMatch
 -> theorem-specific ClosureEligibleCert.
```

Never

```text
catalogue entry/count exists
 -> actual occurrence
```

and never

```text
full-graph RawPhysicalRow
 -> local CatalogueMatch
```

without a separate global theorem designed for that interface.

## 10. Conditional partial closures after actual match

Cycle 12 consumes the fresh partial F0 and COMPACT information only as post-occurrence theorem-selection interfaces. Neither is class-total and neither creates an occurrence.

### 10.1 F0 repository wheel subclasses

The repository already contains source-bound degree-five wheel interface theorems such as C18/C19. They are narrow: C18 is an exact fixed-exterior wheel extension test with one return-path bit, and C19 treats the one-directed-face degree-five subcase by forcing a directed separating triangle. They do not establish a universal `F0_ROOT_STAR` closure.

A fresh F0 partial closure may therefore be used only in the form

```text
ProperLocalRow(j)
and AdmissibleClass(j,F0_ROOT_STAR,w)
and F0WheelCatalogueMatch(j,c)
and F0WheelSubclassClose(c,kappa)
 -> ClosureEligibleCert(j,F0_ROOT_STAR,w,kappa).
```

This is a conditional reuse theorem for an **already actual matched row**. The number of repository wheel rows/subclasses, if any, is not an occurrence theorem.

### 10.2 COMPACT_NONJ one-face enlargement

Likewise the fresh one-face enlargement is consumed only as

```text
ProperLocalRow(j)
and AdmissibleClass(j,COMPACT_NONJ,w)
and CompactOneFaceMatch(j,e)
and CompactOneFaceEnlargementClose(e,kappa)
 -> ClosureEligibleCert(j,COMPACT_NONJ,w,kappa).
```

The enlargement must preserve the actual cyclic boundary, ownership and proper exterior interface of `j`; it cannot be invoked on an abstract count-equivalent compact row. This gives a partial certificate lane, not `COMPACT-NONJ-CLOSE` for the whole semantic class.

No protected-main specialist artifact carrying a stronger fresh F0/COMPACT total theorem was found at the cutoff. The two partial interfaces are therefore recorded conditionally and are not promoted beyond their stated matched scopes.

## 11. Existing class suffixes after proper locality and actual match

### J_READY degree six

Conditional on

```text
ProperLocalRow(j)
and AdmissibleClass(j,J_READY,w)
and d(7)=6,
```

S09 Cycle 5 may derive the exact C37 family/word from the actual geometry before R160. The candidate suffix remains closed:

```text
actual proper J_READY,d6
 -> exact C37 identity
 -> R160 strict arbitrary-exterior replacement
 -> ClosureEligibleCert
 -> ONE-ROW-EC.
```

High-port J_READY remains `TPROG`-open.

### NONJ_QARC

After an actual proper row and q-arc/D4 witness, the symbolic rigid fibre, SCC, four flip blockers and pair-phase content remains available. The first missing class-wide bridge is still

```text
D4-ENDPOINT-TOPOLOGY.
```

It must use the actual endpoint order and boundary contacts of the proper local row.

### Other classes

- `F0_ROOT_STAR`: partial matched wheel subclasses may close; class-total `F0-ROOT-CLOSE` remains open.
- `COMPACT_NONJ`: partial one-face enlargement may close; class-total `COMPACT-NONJ-CLOSE` remains open.
- `PINCHED_MULTICONTACT`: `PINCH-MULTICONTACT-COMPOSE` remains open with exact ownership/full positive `R+`.
- `WIDE_CHANNEL`: `WIDE-TPROG` remains open without a uniform-width assumption.

## 12. Exact ranking of the live cuts

### Root-order ranking

1. **`PROPER-ROW-EXTRACT`** — first and highest-priority cut. Without a proper boundary-closed local row there is no sound local catalogue/replacement interface at all.
2. **`LOCAL-FER-CLASS-COVER`** — second. It matters only after proper locality is established; S10's gaps still block totality.
3. **class-specific closure** — third. `J_READY,d6` is already candidate-closed conditionally; partial F0/COMPACT certificates may fire after an actual match.

### First honest unclosed class-wide lemma

Among semantic class lemmas not already closed on a matched subclass, the shortest currently visible one remains

```text
D4-ENDPOINT-TOPOLOGY
```

for `NONJ_QARC`.

The F0 wheel and COMPACT one-face results are useful **partial certificate rules**, not replacements for either `PROPER-ROW-EXTRACT`, class cover, or a class-total closure theorem.

## 13. Weakest direct root theorem

The root never needs ALL applicable tags. The direct choice-free target is

```text
LOCAL-FECT-GOOD-EX1:
D0_G(f)
 -> exists a,r,j,tau,w,kappa,
      LowDesc_G(f,a)
   and FirstExposureRecord_G(f,a,r)
   and RawPhysicalRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and ProperFiniteSupport_G(j)
   and BoundaryClosedSupport_G(j)
   and AdmissibleClass_G(j,tau,w)
   and ClosureEligibleCert_G(j,tau,w,kappa).
```

One such certificate for each actual negative face gives ONE-ROW-EC. No scheduler or class priority occurs in this theorem.

## 14. Updated sole root DAG

```text
minimum counterexample G
 |
 +-- Sigma mu = -8
 |     -> actual D0(f)
 |
 +-- C48
 |     -> exists LowDesc(f,a)                          [PASS candidate]
 |
 +-- FECT physical entrance
 |     -> actual same-face FER r                      [PASS candidate]
 |
 +-- RAW-ID-EXTRACT
 |     -> cyclic-invariant tag-free RawPhysicalRow j  [PASS candidate]
 |
 +-- RAW-ID-JREL0
 |     -> SameMinCEJREL0                              [PASS candidate]
 |
 +-- PROPER-ROW-EXTRACT                               [OPEN FIRST ROOT CUT]
 |     -> ProperFiniteSupport
 |     -> BoundaryClosedSupport
 |     -> ProperLocalRow
 |
 +-- LOCAL-FER-CLASS-COVER                            [OPEN SECOND CUT]
 |     -> exists admissible (tau,w), overlap allowed
 |           |
 |           +-- J_READY,d6 -> C37/R160 -> cert       [PASS conditional suffix]
 |           +-- J_READY,highport -> TPROG            [OPEN]
 |           +-- NONJ_QARC -> D4 endpoint topology    [OPEN first class-wide]
 |           +-- F0 wheel subclasses                  [PARTIAL after actual match]
 |           +-- COMPACT one-face enlargement         [PARTIAL after actual match]
 |           +-- PINCHED multicontact                 [OPEN]
 |           `-- WIDE                                 [OPEN]
 |
 +-- EXISTS one proof-carrying ClosureEligibleCert   [SUFFICIENT; no ALL]
 |
 `-- ONE-ROW-EC for every actual D0
       -> no negative final face
       -> contradiction with Sigma mu = -8.
```

## 15. Candidate boundary

Cycle 12 makes three corrections and no root promotion:

1. content-derived physical identity survives, now invariant under cyclic presentation and tag-free;
2. a full-graph physical occurrence falsifies any unqualified implication from FER to a proper local replacement row, so `PROPER-ROW-EXTRACT` is restored as the first cut;
3. class cover and closure are downstream relations, and the root accepts **existence of one proof-carrying closure certificate**, not closure of every applicable tag.

No B46 reconstruction, count-to-occurrence inference, EvidenceLink, Result, Solution, trusted admission or root closure is made.

`candidate_only`; `best_verified_result=none`; `root_closed=false`.
