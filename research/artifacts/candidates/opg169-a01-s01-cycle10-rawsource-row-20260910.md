# R08 S01 Cycle 10 — content-derived RawSourceRow closes FECT-ROW-TOTAL

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `58830f78c2dfd384780f76f4503f118ecfce2272`.

This is a candidate integration theorem. It creates no EvidenceLink, Result, Solution, trusted-verifier receipt, or root closure.

## 1. Cycle-9 cut and Cycle-10 objective

Cycle 9 ended at

```text
D0_G(f)
 -> exists LowDesc_G(f,a)                         [C48 PASS candidate]
 -> exists FirstExposureRecord_G(f,a,r)           [FECT PASS candidate]
 -> exact source-row identity                     [OPEN]
 -> SameMinCEJREL_G(f,a,j)
 -> tag-specific closure
 -> ONE-ROW-EC.
```

The Cycle-9 `ExactRowBind` field was deliberately kept separate from the six FECT tags. That was sound because a tag is a source class, not an exact row identity. The remaining question is whether exact row identity must be imported from C35/C37/B46-style registries, or can instead be defined directly from the actual stopping record.

Cycle 10 proves the latter. A row is identified by its complete finite source-facing payload itself. Registry or atlas membership is moved to a later optional theorem-selection relation.

## 2. Fixed setting

Fix the selected finite plane minimum counterexample `G` used by the candidate route, its fixed plane rotation system, one actual unpaid negative face `f`, one C48 low descriptor `a`, and one FECT stopping record

```text
FirstExposureRecord_G(f,a,r).
```

The consumed FECT contract gives:

1. `r` is read from this same `G` and the same actual face `f`;
2. every symbolic port in `r` denotes an actual vertex/arc/face role of `G`;
3. aliases, contacts, source/exterior ownership and payer/source provenance are preserved;
4. `r` carries one tag in
   `F0_ROOT_STAR`, `J_READY`, `COMPACT_NONJ`, `NONJ_QARC`,
   `PINCHED_MULTICONTACT`, `WIDE_CHANNEL`;
5. the stopping record is finite for this fixed finite `G`; `WIDE_CHANNEL` may have variable width across records, but its concrete ordered lists are finite.

Nothing below assumes that `r` occurs in a named finite catalogue.

## 3. Complete occurrence payload

Define the source-facing completion `Complete_G(r)` from the actual stopping record and the fixed embedded graph `G`.

### 3.1 Role support and alias normal form

Let `Roles(r)` be the finite ordered role list carried by the FECT record, including root-face roles, exposed source roles, QARC roles, contact roles and every entry of every variable-width tag list.

Two roles are alias-equivalent exactly when their FECT occurrence map names the same actual object of `G`. Quotient by this equality **before** geometry. Number quotient classes by first occurrence in the ordered FECT role stream. This gives `AliasNF(r)`.

No equality is inferred from geometric resemblance and no alias is forgotten.

### 3.2 Ordered rotations and faces

The selected `G` has a fixed plane rotation. For every exposed vertex role, record the ordered cyclic sequence of all source/QARC/contact darts visible at that role. For every role declared by FECT to have a complete exposed star, record the entire actual star from `G`, not merely the currently named local neighbours.

Record every actual exposed face walk and boundary/hole walk used by the stopping record in its FECT order. These are read from the same fixed rotation of `G`; they are not reconstructed from an abstract planar embedding test.

### 3.3 Source arcs, QARC arcs and contacts

Record all actual source-owned arcs of the stopping region, all designated QARC arcs, and the complete FECT contact frontier. A contact entry contains its actual direction, its source-side endpoint role, its exterior-side endpoint/contact role and its position in the relevant source-side rotation.

For a complete exposed star, completeness is checked against the actual incidence set in `G`. Thus an omitted extra neighbour would invalidate the raw row rather than silently move to the exterior.

### 3.4 Ownership and payer/source identity

For every recorded arc/face/contact object, retain the FECT source-versus-exterior ownership bit or owner key. Retain every payer/source ID, side assignment and no-double-spending key carried by the stopping record. These are not derivable merely from the abstract graph and therefore are copied from FECT, whose contract explicitly preserves them.

### 3.5 Tag parameters

Retain the tag and its complete parameter payload. In particular, a `WIDE_CHANNEL` row stores its entire concrete ordered port/contact lists and their lengths. Variable width is therefore part of the raw content identity and causes no finiteness problem for an individual row.

## 4. Canonical content identity

A `RawContentKey` is the complete typed finite value

```text
(
  alias-normal-form,
  ordered rotations,
  ordered exposed faces / holes,
  complete-star declarations and full star data,
  source arcs,
  QARC arcs,
  contact arcs,
  source/exterior ownership,
  payer/source IDs,
  tag,
  tag parameters
).
```

Arbitrary temporary symbolic names are removed as follows.

1. Alias classes receive first-occurrence numbers from the FECT ordered role stream.
2. Local role references are replaced by those numbers.
3. Ordered data remain ordered: rotations, face walks, QARC order, contact order and WIDE lists are never sorted away.
4. Truly unordered finite maps/sets are serialized in lexicographic order after role normalization.
5. Type and length delimiters are part of the value, so variable-width lists cannot collide with concatenations of shorter lists.
6. Actual payer/source keys that are not local role names remain opaque stable atoms; local payer roles are represented both by their normalized local role and their preserved source key.

The **identity is this structured value itself**. A SHA-256 digest may be used as transport metadata, but no mathematical inference relies on digest collision resistance.

Define

```text
RawKey_G(r) := Canon(Complete_G(r)).
```

A source occurrence row is

```text
RawSourceRow_G(f,a,j)
```

when `j` contains the occurrence binding `(G,f,a,r)`, the canonical content value `RawKey_G(r)`, and the actual realization map from normalized local roles back to their objects in `G`.

Thus two physically different occurrences may have the same abstract catalogue shape while remaining distinct occurrence rows because their same-MinCE/root-face/payer binding is retained outside the abstract shape matcher.

## 5. Extraction theorem

### Theorem 5.1 — RAW-EXTRACT

```text
FirstExposureRecord_G(f,a,r)
 -> exists unique j RawSourceRow_G(f,a,j).
```

### Proof

Existence is constructive: form `Complete_G(r)` using the actual finite role support of `r`, the fixed rotation and incidence relation of `G`, and FECT's preserved non-graph fields; then canonicalize it as in Section 4.

Finiteness holds because `G` is finite and `r` has finite role/contact/tag lists. The WIDE width is not uniformly bounded, but each concrete list is finite.

For uniqueness, suppose `j1,j2` are two valid completions of the same `(G,f,a,r)`.

- If they differ in an alias, actual arc, rotation, exposed face, complete-star incidence or contact arc, then one of them disagrees with the fixed actual embedded graph `G` on the same named support.
- If they differ in ownership, payer/source ID or tag data, then one of them disagrees with the preserved FECT stopping record.
- If they differ only in symbolic role names, canonical first-occurrence normalization identifies them.

Hence their complete typed canonical payloads are equal and the occurrence bindings are the same. Therefore `j1=j2`. `square`

## 6. Two-completion omission test

The user-requested fail-closed test is therefore negative: there is no omitted field that forces a weaker row type under the consumed FECT contract.

Assume, for contradiction, that one FirstExposureRecord admits two completions differing only in one required raw field.

- A geometry/contact/star field is a function of the fixed actual `G`, its fixed plane rotation and the exposed support, so the two values cannot both be correct.
- Ownership, payer/source identity and tag parameters are FECT-preserved fields, so the two values cannot both preserve the same stopping record.
- Width/list order is literal tag payload, so a different WIDE list is a different FECT record.

Thus no pair of same-record completions exists. No weakening of `RawSourceRow` is needed.

If a future FECT revision weakens `preserves contacts/ownership/payer` to a partial projection, this theorem must be reopened; Cycle 10 does not silently infer missing non-graph ownership data from geometry.

## 7. Validator theorem: raw row to same-MinCE JREL

Cycle 8's Type-J semantics required an exact source-row identity in addition to same-MinCE physical/provenance data. It did **not** require that the identity be a member name of C35/C37/B46. Treating catalogue membership as identity would be a stronger premise and would reintroduce atlas-to-occurrence leakage.

Define the raw validator `RAWVALID_G(f,a,j)` to check:

1. the occurrence binding names the assumed `G`, actual `f` and descriptor `a`;
2. the canonical payload is exactly `RawKey_G(r)` for its witnessed FECT record;
3. alias normalization agrees with actual equality in `G`;
4. every ordered rotation/face/star/arc/contact entry realizes in `G`;
5. every declared complete star is complete in `G`;
6. all QARC/contact directions and positions agree with `G`;
7. ownership and payer/source keys agree with the FECT record;
8. the tag and full parameter payload agree with the FECT record.

### Theorem 7.1 — RAW-JREL

```text
RawSourceRow_G(f,a,j)
 -> SameMinCEJREL_G(f,a,j).
```

### Proof

The row already carries the same `G`, same actual face and LowDesc provenance. Items 3--6 give the complete actual source geometry and contact interface. Item 7 supplies the source/exterior/payer ownership gates. Item 8 preserves the source class without turning it into a catalogue occurrence claim. The exact-row-identity gate is satisfied by the complete canonical content value itself. Hence every source-facing Gate18 requirement is represented by actual data of the same MinCE occurrence, so the typed constructor accepts `j`. `square`

Combining Theorems 5.1 and 7.1 gives the Cycle-9 first cut:

### Corollary 7.2 — FECT-ROW-TOTAL

```text
FirstExposureRecord_G(f,a,r)
 -> exists j,
      RawSourceRow_G(f,a,j)
   and SameMinCEJREL_G(f,a,j)
   and RowTag(j)=tag(r).
```

This is candidate-PASS. It uses no finite atlas membership.

## 8. Catalogue matching is later and optional

For any existing theorem catalogue `C`, define only later

```text
CatalogueMatch_C(j,c)
```

to mean that the abstract source-facing shape/properties required by catalogue row `c` match the already actual raw row `j`, with all guards and theorem-specific hypotheses checked.

The logical direction is now

```text
actual FECT occurrence
 -> RawSourceRow / SameMinCEJREL
 -> optional CatalogueMatch
 -> reuse a catalogue closure theorem.
```

Never

```text
catalogue row exists
 -> actual occurrence.
```

`CatalogueMatch` may be many-to-many. `JUNIQ` remains optional.

For `J_READY,d(7)=6`, merged S09 Cycle 5 is exactly such a source-derived matcher: actual geometry determines one C37 family/word before R160 is invoked. This post-occurrence matching remains valid.

## 9. Tag closure frontier after row extraction

The common row-constructor cut is now closed. The first remaining root work is tag-specific closure.

### 9.1 `J_READY`

If the raw tag parameters give the selected-J degree-six case, the candidate mathematical suffix is already closed:

```text
RawSourceRow + J_READY + d(7)=6
 -> S09 C5 exact C37 family/word
 -> R160 arbitrary-exterior strict reduction
 -> ClosureEligible_CANDIDATE
 -> ONE-ROW-EC.
```

If `d(7)>=7`, the row is `J_HIGHPORT`; `TPROG/useful-terminal` remains open.

### 9.2 `NONJ_QARC` — first unclosed short lane

S12-A Cycle 9 supplies theorem content for the D4 symbolic core:

```text
rigid fibre          available,
SCC structure        available,
four flip blockers   available,
pair-phase           available,
endpoint-sensitive topology OPEN.
```

The raw row now gives an exact source-facing QARC/contact/rotation payload, so theorem-specific D4 schema matching can be checked **after occurrence**. The remaining mathematical bridge for a matching row is `D4-ENDPOINT-TOPOLOGY`: turn pair-phase/blocker data into the actual endpoint-sensitive planar obstruction or source-valid reduction.

Among currently unclosed tag lanes this is the shortest visible one.

### 9.3 Other tags

- `COMPACT_NONJ`: first lemma `COMPACT-NONJ-CLOSE`.
- `F0_ROOT_STAR`: first lemma `F0-ROOT-CLOSE`; C32 residual star types forbid assuming a universal star replacement.
- `PINCHED_MULTICONTACT`: first lemma `PINCH-MULTICONTACT-COMPOSE`, preserving aliases, ownership and full positive `R+`.
- `WIDE_CHANNEL`: first lemma `WIDE-TPROG`, allowing variable-width contact/port lists.

## 10. Conditional fresh S09/S11 consumers

No new protected-main S09 C35 physical-closure package or S11 source-facing wrapper is repository-bound at this fresh cutoff. They are therefore integrated only through conditional interfaces.

### S09 C35 physical closures — conditional

If a future identity-bound S09 closure theorem supplies

```text
C35PhysicalClose(c)
```

and an already actual raw row satisfies `CatalogueMatch_C35(j,c)` with all physical/ownership hypotheses, then the theorem may yield `ClosureEligible_CANDIDATE(j)`. This uses C35 only for theorem reuse after occurrence. It does not infer a FECT tag, a raw row or root occurrence from the C35 catalogue.

### S11 source-facing wrapper — conditional

If an identity-bound S11 wrapper accepts a `RawSourceRow` together with a concrete replacement/certificate and checks the exact boundary, ownership, complete-Q and positive-reachability lifting premises, it may transport that certificate into the generic LIFT-O theorem content. Such a wrapper does not generate the raw row, does not synthesize a replacement, and does not supply trusted Evidence without its separate replay/admission receipt.

The currently open draft PR #83 remains raw Lean transport with no trusted kernel admission.

## 11. Weakest remaining root theorem

Because C48 entrance, FECT entrance and FECT-ROW-TOTAL are now candidate-PASS, the weakest remaining root bridge is purely closure-existential:

```text
FECT-CLOSE-EX1:
D0_G(f)
 -> exists a,r,j,
      LowDesc_G(f,a)
   and FirstExposureRecord_G(f,a,r)
   and RawSourceRow_G(f,a,j)
   and ClosureEligible_G(j).
```

A modular stronger route is to prove six tag lemmas covering every raw FECT row. The root itself only needs one closed exposure output for each actual `D0`.

## 12. Updated sole root DAG

```text
minimum counterexample G
 |
 +-- Sigma mu = -8
 |     -> actual D0(f)
 |
 +-- C48
 |     -> exists LowDesc(f,a)                         [PASS candidate]
 |
 +-- FECT
 |     -> exists same-face FirstExposureRecord r     [PASS candidate]
 |        tag in {F0,J_READY,COMPACT,NONJ_QARC,PINCHED,WIDE}
 |
 +-- RAW-EXTRACT
 |     -> unique content-derived RawSourceRow j       [PASS candidate]
 |
 +-- RAW-JREL
 |     -> SameMinCEJREL(f,a,j)                        [PASS candidate]
 |        no catalogue membership premise
 |
 +-- tag closure                                      [FIRST OPEN ROOT CUT]
 |     +-- J_READY,d6 -> C37/R160 -> EC              [PASS candidate suffix]
 |     +-- J_READY,highport -> TPROG                  [OPEN]
 |     +-- NONJ_QARC -> D4-ENDPOINT-TOPOLOGY          [OPEN; shortest]
 |     +-- COMPACT_NONJ -> COMPACT-NONJ-CLOSE         [OPEN]
 |     +-- F0_ROOT_STAR -> F0-ROOT-CLOSE              [OPEN]
 |     +-- PINCHED -> PINCH-MULTICONTACT-COMPOSE      [OPEN]
 |     `-- WIDE -> WIDE-TPROG                         [OPEN]
 |
 `-- one closed raw exposure for every actual D0
       -> no negative final face
       -> contradiction with Sigma mu = -8.
```

## 13. Highest-value next theorem

After Cycle 10 the common occurrence/source-row constructor is no longer the bottleneck. The highest-value short closure theorem is

```text
D4-ENDPOINT-TOPOLOGY
```

for exact raw `NONJ_QARC` rows that satisfy the D4 schema: combine the already available rigid-fibre/SCC/four-blocker/pair-phase theorem content with the actual ordered endpoints, QARC directions, contacts and plane rotations in the raw row, and prove the endpoint-sensitive planar contradiction or strict source-valid reduction.

A separate high-port `TPROG` theorem remains necessary for `J_READY,d>=7` unless a stronger root argument avoids that subcase.

No B46 dependency is introduced.

**State:** `candidate_only`; `best_verified_result=none`; `root_closed=false`.