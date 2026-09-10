# R08 S01 Cycle 11 — choice-free FECT class cover after the clean-room overlap/gap audit

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `88af1f947ecbdbac4562d57e4b4f195250319eb4`.

No EvidenceLink, Result, Solution, trusted-verifier receipt or root closure is created here. B46 is not used.

## 1. Why Cycle 10 needs a classification repair, not a raw-row retraction

Cycle 10 proved a content-derived occurrence construction:

```text
actual FirstExposureRecord
 -> RawSourceRow
 -> SameMinCEJREL.
```

The new S10 Cycle-6 clean-room finding attacks a different claim. The six names

```text
F0_ROOT_STAR
J_READY
COMPACT_NONJ
NONJ_QARC
PINCHED_MULTICONTACT
WIDE_CHANNEL
```

are not yet an executable disjoint partition. The clean-room audit reports literal overlaps between current class descriptions and literal gaps in their current executable interpretation. Therefore neither exact-one classification nor a precedence-based scheduler may be imported into the root proof.

Overlap does **not** damage occurrence identity. A physical stopping record can satisfy two later theorem classes. A gap does **not** damage occurrence identity either. It only means the present six-class language has not yet been proved total on every actual stopping row.

Thus Cycle 11 keeps the content-derived raw row and removes exclusive source-class data from its mathematical identity.

## 2. Precedence-free physical RawSourceRow

Fix the selected finite plane minimum counterexample `G`, one actual unpaid negative face `f`, one C48 low descriptor `a`, and one actual FECT stopping record `r` read from that same `G,f`.

Define the precedence-free physical key

```text
PhysKey_G(r) := Canon(
  alias normal form,
  ordered actual rotations,
  ordered actual exposed faces and holes,
  complete-star declarations and complete exposed-star data,
  all source arcs,
  all QARC arcs,
  all contact arcs and contact positions,
  source/exterior ownership,
  payer/source IDs,
  all literal ordered port/contact sequences carried by r,
  stopping support and source-facing occurrence parameters
).
```

The variable-width data formerly described as `WIDE` remain in the physical key when they are literal port/contact lists of the stopping record. What is removed from the key is the assertion that a particular later class name has priority, is unique, or even currently applies.

A `RawSourceRow_G(f,a,j)` carries

```text
(G, f, a, r, PhysKey_G(r), realization-map-to-G).
```

It has no scheduler field and no chosen class field.

### Lemma 2.1 — RAW-PHYS-EXTRACT

```text
FirstExposureRecord_G(f,a,r)
 -> exists unique j RawSourceRow_G(f,a,j).
```

The Cycle-10 proof survives unchanged after deleting the class annotation from the key. Geometry is uniquely read from the fixed embedded `G` and stopping support; ownership and payer/source identity are preserved by the FECT record. Removing a non-unique classification field cannot destroy existence or uniqueness of the remaining physical payload.

### Lemma 2.2 — RAW-PHYS-JREL

```text
RawSourceRow_G(f,a,j)
 -> SameMinCEJREL0_G(f,a,j).
```

Here `SameMinCEJREL0` is the source-facing actual-occurrence relation: same assumed MinCE, same actual face and LowDesc provenance, exact aliases, rotations, faces, complete stars, all contacts/QARCs, ownership and payer/source identity, with exact content identity given by `PhysKey`.

If older notation `SameMinCEJREL` bundled one exclusive class label into the same record, Cycle 11 replaces that packaging by

```text
SameMinCEJREL0(j)                  -- physical/provenance occurrence
TypedJREL(j,tau,w) := SameMinCEJREL0(j) and AdmissibleClass(j,tau,w).
```

No theorem about occurrence is retracted. Only the unjustified single-valued classification packaging is removed.

## 3. Producer labels are not semantic class witnesses

A FECT implementation may have emitted a literal label or stopped under a named branch. Call this

```text
ProducerAnnotation(r,tau).
```

The clean-room overlap/gap audit means that the root cannot identify this field with a proved semantic partition.

For each of the six class names define instead a relation

```text
AdmissibleClass_G(j,tau,w),
```

where `w` is all class-specific witness data: anchor choice, endpoint choice, selected q-arc, compact interface witness, pinched contact decomposition, wide ordered sublist, or selected-J data as appropriate.

Properties:

1. `AdmissibleClass` is evaluated on an already actual raw row.
2. Multiple `(tau,w)` may be admissible for one row.
3. No precedence is imposed between admissible pairs.
4. Class witnesses do not participate in `PhysKey` identity.
5. A catalogue match, if used, is downstream of an admissible witness and cannot create occurrence.

Define

```text
ClassSet(j) := { (tau,w) : AdmissibleClass_G(j,tau,w) }.
```

The set is finite for a fixed finite raw row when witnesses are drawn from its finite support, even though no uniform width bound is assumed for `WIDE_CHANNEL`.

## 4. The exact cover theorem is restored as the first cut

The weakest class-totality statement is

```text
FER-CLASS-COVER:
FirstExposureRecord_G(f,a,r)
 and RawSourceRow_G(f,a,j)
 -> exists tau,w AdmissibleClass_G(j,tau,w).
```

Equivalently, `ClassSet(j)` is nonempty for every actual FER row.

Cycle 11 does **not** mark this PASS. S10 Cycle 6 reports literal gaps in the currently executable six-name classification, and no independent protected-main source theorem was found that proves the semantic relation above is total despite those gaps. The earlier producer-facing phrase “tagged one of six” is therefore retained only as annotation/intent, not promoted to `FER-CLASS-COVER`.

This is now the first root cut.

The overlap part of S10 is harmless to this theorem: cover asks only nonemptiness. The gap part is decisive: without a new source theorem or repaired class predicates, nonemptiness is not established.

## 5. Existential closure versus closing every admissible tag

For a typed witness define

```text
ClassClose_G(j,tau,w)
```

to mean that the hypotheses of the source-faithful closure theorem for that class witness are met and yield `ClosureEligible_G(j)` / ONE-ROW-EC for this actual row.

Two natural formulations are:

### SOME-CLOSE

```text
SomeClose(j) :=
  exists tau,w,
    AdmissibleClass(j,tau,w)
    and ClassClose(j,tau,w).
```

### ALL-CLOSE

```text
AllClose(j) :=
  ClassSet(j) != empty
  and forall tau,w,
        AdmissibleClass(j,tau,w)
        -> ClassClose(j,tau,w).
```

### Lemma 5.1 — SOME-CLOSE is sufficient for the root

Assume `SomeClose(j)`. Choose the exhibited `(tau,w)`. Its class closure makes the already actual `SameMinCEJREL0` row closure-eligible. The S13-B one-row EC interface then excludes this actual source occurrence from the assumed minimum counterexample. No statement about any other simultaneously admissible class is used.

Therefore one closure-eligible admissible class is sufficient.

### Lemma 5.2 — ALL-CLOSE is strictly stronger in proof obligations

`AllClose(j)` plus cover immediately implies `SomeClose(j)`. The converse is not logically valid: a row may satisfy two admissible classes, one having a closure theorem and one still open. Such a row is already excluded by the first class, so requiring the second class to close adds an unnecessary proof obligation.

No actual graph counterexample is needed for this logical separation; a two-element relation model with one closed and one open admissible witness proves non-implication.

## 6. Scheduler and anchor independence

There are two different notions of “choice independence” that must not be conflated.

### 6.1 Mathematical root proof

The root proof should never define a scheduler. Use the joint relation

```text
exists tau,w,
  AdmissibleClass(j,tau,w)
  and ClassClose(j,tau,w).
```

This formula is invariant under reordering the six names, changing precedence, duplicating class witnesses, or choosing a different presentation of an anchor. The witness is part of the proof, not the output of an arbitrary scheduling policy. Hence `SomeClose` is choice-free and scheduler/anchor independent **as a mathematical theorem**.

### 6.2 Correctness of an arbitrary operational scheduler

If a program commits to an arbitrary function

```text
pick(j) in ClassSet(j)
```

and wants to close the row using whatever pair it picks, then `SomeClose` is not enough. One needs either:

- `AllClose(j)`, or
- a separately verified scheduler theorem saying `pick(j)` always selects a closed admissible pair.

The root conjecture does not require such an arbitrary-scheduler theorem. Cycle 11 therefore keeps the weaker relational `SomeClose` target and forbids scheduler output from being treated as a proof premise.

The same distinction applies to anchors. Existence of one source-valid anchor/typed witness that closes is enough for the root; arbitrary-anchor robustness is stronger and unnecessary unless an implementation commits to an unchecked anchor selector.

## 7. Choice-free root theorem after the repair

The weakest sufficient bridge is now

```text
FECT-GOOD-CLASS-EX1:
D0_G(f)
 -> exists a,r,j,tau,w,
      LowDesc_G(f,a)
   and FirstExposureRecord_G(f,a,r)
   and RawSourceRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and AdmissibleClass_G(j,tau,w)
   and ClassClose_G(j,tau,w).
```

This one formula implies the desired ONE-ROW-EC contradiction for `f` and contains no scheduler or precedence function.

A modular stronger program factors it into:

```text
A. FER-CLASS-COVER:
   every actual raw FER row has at least one admissible class;

B. FER-SOME-CLOSE:
   every actual raw FER row has at least one admissible class witness that closes.
```

`B` implies `A`, so for a shortest proof one may prove `FECT-GOOD-CLASS-EX1` directly. For a reusable six-lane architecture, proving `FER-CLASS-COVER` separately is still valuable.

## 8. Status of the six closure lanes

Class names below denote semantic `AdmissibleClass` witnesses, never exclusive producer tags.

### J_READY

Conditional on an actual raw row and a valid `J_READY` witness with selected-J `d(7)=6`, the candidate suffix remains closed:

```text
actual raw row
 + admissible J_READY,d6 witness
 -> S09 Cycle 5 derives exact C37 family/word from actual geometry
 -> R160 arbitrary-exterior strict reduction
 -> ClassClose
 -> ONE-ROW-EC.
```

This does not prove that every FER has a J_READY witness.

A J_READY high-port witness still enters `J_HIGHPORT/TPROG` and is open.

### NONJ_QARC

Conditional on an admissible q-arc/D4 witness, S12-A Cycle 9 already supplies the symbolic rigid-fibre, SCC, four-flip-blocker and pair-phase content. The first missing closure lemma remains

```text
D4-ENDPOINT-TOPOLOGY.
```

It must use the actual raw endpoint, rotation and contact data. This is the shortest honest **unclosed tag-specific closure lemma** currently visible.

### Other classes

- `COMPACT_NONJ`: `COMPACT-NONJ-CLOSE` open.
- `F0_ROOT_STAR`: `F0-ROOT-CLOSE` open; C32 residual root-star types forbid a universal shortcut.
- `PINCHED_MULTICONTACT`: `PINCH-MULTICONTACT-COMPOSE` open, with exact aliases/ownership/full positive `R+`.
- `WIDE_CHANNEL`: `WIDE-TPROG` open, with no uniform-width assumption.

Operational closure ranking after a semantic class witness exists:

```text
1. J_READY,d6                  already candidate-closed suffix
2. NONJ_QARC                   D4-ENDPOINT-TOPOLOGY
3. COMPACT_NONJ                COMPACT-NONJ-CLOSE
4. F0_ROOT_STAR                F0-ROOT-CLOSE
5. PINCHED_MULTICONTACT        PINCH-MULTICONTACT-COMPOSE
6. WIDE_CHANNEL                WIDE-TPROG
```

The current **root** priority is nevertheless `FER-CLASS-COVER`, because a gap row cannot enter any lane at all.

## 9. S13-D row-identity audit

A fresh search of protected main, visible specialist branches and Issue #3 checkpoints found no new repository-bound S13-D row-identity audit beyond the older same-face/canary corrections already integrated. Therefore Cycle 11 does not import a new S13-D theorem or fabricate a locator.

If a later S13-D audit confirms that occurrence identity is independent of scheduler/class annotations, it corroborates `PhysKey`; if it instead identifies a genuinely missing physical/provenance field, `RAW-PHYS-EXTRACT` must be reopened on that exact field. Neither conclusion is pre-assumed here.

## 10. S10 Cycle-6 clean-room status discipline

The S10 Cycle-6 overlap/gap finding is consumed exactly at the classification layer:

- exact-one/disjoint six-tag partition: rejected;
- precedence/scheduler classification as proof: rejected;
- total six-class semantic cover: **not established** and restored as a cut;
- content-derived physical row identity: unaffected;
- same-MinCE physical/provenance validation: unaffected.

No exact overlap/gap row IDs or counts are invented here because no corresponding protected-main specialist artifact was exposed at this cutoff.

## 11. Sole root DAG

```text
minimum counterexample G
 |
 +-- Sigma mu = -8
 |     -> actual D0(f)
 |
 +-- C48
 |     -> exists LowDesc(f,a)                         [PASS candidate]
 |
 +-- FECT physical entrance
 |     -> actual same-face FirstExposureRecord r     [PASS candidate]
 |
 +-- RAW-PHYS-EXTRACT
 |     -> unique precedence-free RawSourceRow j      [PASS candidate]
 |
 +-- RAW-PHYS-JREL
 |     -> SameMinCEJREL0(f,a,j)                       [PASS candidate]
 |
 +-- FER-CLASS-COVER                                  [OPEN FIRST ROOT CUT]
 |     -> exists admissible (tau,w)
 |        overlap allowed; no scheduler/precedence
 |           |
 |           +-- J_READY,d6 -> C37/R160 -> EC        [PASS conditional suffix]
 |           +-- J_READY,highport -> TPROG           [OPEN]
 |           +-- NONJ_QARC -> D4 endpoint topology   [OPEN shortest closure]
 |           +-- COMPACT_NONJ -> compact close       [OPEN]
 |           +-- F0_ROOT_STAR -> root-star close     [OPEN]
 |           +-- PINCHED -> multicontact compose     [OPEN]
 |           `-- WIDE -> wide TPROG                  [OPEN]
 |
 +-- SOME-CLOSE for one admissible witness           [SUFFICIENT target]
 |
 `-- ONE-ROW-EC for every actual D0
       -> no negative final face
       -> contradiction with Sigma mu = -8.
```

## 12. Exact next priorities

**First root theorem:**

```text
FER-CLASS-COVER
```

or, if easier, the directly sufficient stronger-in-content but existential theorem `FECT-GOOD-CLASS-EX1` that simultaneously produces one admissible closed witness.

**First honest unclosed class lemma after a witness exists:**

```text
D4-ENDPOINT-TOPOLOGY
```

for `NONJ_QARC`.

No B46 reconstruction, atlas-count occurrence inference, EvidenceLink, Result, Solution or root closure is made.

`candidate_only`; `best_verified_result=none`; `root_closed=false`.
