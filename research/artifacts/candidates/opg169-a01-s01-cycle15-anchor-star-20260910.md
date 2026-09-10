# R08 S01 Cycle 15 — anchor-star stop support closes the entry-locality cut

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `7397e363825bd9942424a5fad8280dc90c01e783`.

No B46, EvidenceLink, Result, Solution, trusted verification or root closure is created here.

## 1. Cycle-14 question and the correction

Cycle 14 attached replacement locality to the canonical least source-owned carrier `K_G(r)` of a FirstExposureRecord and isolated

```text
FER-EXTERIOR-SURVIVES:
  V(K_G(r)) proper-subset V(G)
```

as the first missing source condition.

That condition is sufficient, but it is not root-minimal. It conflates two different roles:

1. **FER constructor control/provenance**, which must never be changed by an integrator; and
2. **replacement-entry support control**, which merely declares which actual vertices are allowed to be changed by a later local replacement while every other actual incidence remains frozen context or a typed boundary contact.

S15's locality attack correctly forbids silently shrinking the first object. It does not forbid defining the second object as an additional role on the same unchanged raw occurrence.

Cycle 15 makes that distinction explicit and proves that every actual FER has a proper source-sound replacement-entry support already at its C48 low-descriptor anchor.

The canonical least source carrier remains a useful optional support. Its properness is no longer a mandatory root source axiom.

## 2. Frozen FER control versus support role

Fix an actual chain in the selected vertex-minimum counterexample `G`:

```text
D0_G(f)
LowDesc_G(f,a)
FirstExposureRecord_G(f,a,r)
RawPhysicalRow_G(f,a,j)
SameMinCEJREL0_G(f,a,j).
```

Every low descriptor `a` contains an actual corner vertex `p`; write

```text
Anchor_G(a)=p.
```

For an SG descriptor the actual singleton gap `g` remains part of `a`; choosing the anchor `p` does not discard `g` or any other raw provenance.

Let

```text
FERCtrl(r)
```

mean the constructor's own controlled vertices/objects. Cycle 15 never changes, shrinks, quotients or reclassifies `FERCtrl(r)`. All aliases, source/exterior/shared ownership, root identity, anchor identity, payer/source identity and constructor-specific extra stars remain exactly as in `r` and `j`.

Define a separate replacement-entry support role

```text
SupportInterior(s) subseteq V(G).
```

An object can therefore be source-owned in the FER provenance while lying outside `SupportInterior(s)`. Its source ownership is unchanged; `boundary contact` is an additional support-role annotation, not a rewrite of source ownership.

This orthogonality is the key point. A source-owned arc `p->u`, for example, may remain source-owned in `j` and simultaneously be a crossing contact of a support whose controlled interior is `{p}`.

No theorem below asserts that the FER constructor itself could have been generated with a smaller `FERCtrl` set.

## 3. Anchor-star support

For the actual anchor `p`, read the complete oriented star from the same fixed plane graph:

```text
FullStar_G(p).
```

C02 already gives, for every vertex of the selected minimum counterexample,

```text
d+(p)>=2,
d-(p)>=2,
```

and hence at least four distinct neighbors because the orientation is simple and has no digons.

Define `AnchorStarStop_G(j,p,s)` by the following exact payload.

### Controlled interior

```text
SupportInterior(s) = {p}.
```

### Boundary/contact data

For every actual neighbor `u` of `p`, record the actual incidence between `p` and `u` as a boundary contact with:

- endpoint identities `p,u`;
- the actual arc direction;
- its cyclic position in `rot_G(p)`;
- its unchanged source/exterior/shared ownership from `j`;
- alias-normalized endpoint identities;
- every actual incident facial corner needed to reconstruct the plane star;
- root/LowDesc/gap relation when that incidence is part of `f` or `a`;
- payer/source identity when the incidence participates in the source/charge ledger.

The neighbor endpoint `u` is a contact endpoint, not a controlled interior vertex.

The consecutive-neighbor rim incidences bounding the facial triangles around `p` are recorded as interface/frozen-context incidences with their actual ownership. Nonconsecutive neighbor chords and every incidence not meeting `p` remain frozen exterior/source provenance. Nothing is deleted from `j`.

### Frozen provenance

Store an identity reference to the complete unchanged `RawPhysicalRow_G(f,a,j)`. Constructor-specific controlled vertices other than `p`, other source-owned arcs, multi-separator data, extra holes, q-arcs, channel lists, guards and payer objects remain facts about the original occurrence. The entry support neither owns nor rewrites them merely because they occur in the FER payload.

## 4. Source soundness of the role split

The relevant source-soundness assertion is not

```text
FERCtrl(r) = SupportInterior(s).
```

That assertion is generally false and is not needed.

Instead define

```text
EntrySourceSound_G(j,s)
```

to mean:

1. `j` itself is unchanged and remains the sole source/provenance record;
2. every support contact is an actual incidence of `G` with all original ownership/payer/source labels copied verbatim;
3. every incidence touching a controlled interior vertex is recorded, so no hidden contact can be affected by changing that interior;
4. all facts of `j` not represented inside the support remain frozen context and are not inferred from the support;
5. later replacement mathematics must explicitly recheck every raw fact it uses, including guards, aliases, ownership, payer and boundary identity.

### Lemma 4.1 — ROLE-ORTHOGONALITY

Adding support roles as above cannot falsify or strengthen any FER source predicate, because no field of the raw occurrence is changed.

**Proof.** The support payload is a derived annotation on actual objects of the same fixed graph. Source ownership remains source ownership; an arc's being a boundary contact says only that one endpoint is outside the chosen replacement interior. `FERCtrl`, root/anchor, payer, aliases, rotations, faces and all constructor-specific data are read-only. Hence every source predicate has exactly the same truth value before and after adding the support annotation. Conversely, the support annotation does not imply a FER predicate not already present in `j`. ∎

This is why an arbitrary shrink of `FERCtrl` is unsafe while an independent support projection is sound.

## 5. Boundary closure and properness

### Lemma 5.1 — ANCHOR-STAR-BOUNDARY-CLOSED

`AnchorStarStop_G(j,p,s)` records every actual incidence crossing `SupportInterior(s)={p}`.

**Proof.** Every graph arc crossing the singleton controlled interior is incident with `p`, hence belongs to `FullStar_G(p)` and is explicitly recorded. The fixed plane rotation supplies all cyclic positions and facial corners. Incidences not incident with `p` cannot cross the singleton interior. Recording a neighbor endpoint never adds it to `SupportInterior`. ∎

### Lemma 5.2 — ANCHOR-STAR-PROPER

The anchor-star entry support is proper and has actual exterior/contact witnesses.

**Proof.** C02 gives four distinct neighbors of `p`. Thus `G` has at least five vertices, while `SupportInterior(s)` has exactly one. Every incident edge from `p` to a neighbor is an actual boundary contact with its other endpoint outside the controlled interior. Hence the support has a nonempty actual interface even if the closed geometric star happens to contain every vertex of `G`. Properness here is properness of the replacement-controlled interior, not the stronger Cycle-14 requirement that every interface endpoint lie outside a closed source carrier. ∎

No connectedness argument and no `FER-CARRIER-PROPER` hypothesis are required.

## 6. The stop-support theorem

### Theorem 6.1 — FER-ANCHOR-STAR-STOP

For every actual FER/raw/JREL0 occurrence based at a C48 low descriptor,

```text
LowDesc_G(f,a)
and FER_G(f,a,r)
and RawPhysicalRow_G(f,a,j)
and SameMinCEJREL0_G(f,a,j)
 -> exists p,s,
      Anchor_G(a)=p
   and AnchorStarStop_G(j,p,s)
   and EntrySourceSound_G(j,s)
   and ProperFiniteControlledInterior_G(s)
   and BoundaryClosedSupport_G(s)
   and ActualBoundaryContactWitness_G(s).
```

**Proof.** Take the actual low-descriptor corner `p`. Construct `s` from the singleton controlled interior and the complete actual star. Role-orthogonality is Lemma 4.1; boundary completeness is Lemma 5.1; properness and a contact witness are Lemma 5.2. Every identity/provenance field is copied or referenced from the same `j`. ∎

The construction is canonical once the actual descriptor `a` is fixed; no FECT tag, scheduler or catalogue is used.

## 7. Constructor-by-constructor audit

FECT's protected-main-facing contract does not expose executable definitions of all internal stopping constructors, so S01 does not fabricate constructor names, row IDs or private support predicates. Nevertheless the theorem above is constructor-independent because every FECT output in scope starts from an actual `LowDesc(f,a)` and preserves that provenance.

For every actual FECT constructor, exactly one of the following statements is used:

```text
constructor-specific FERCtrl/provenance: frozen, untouched;
replacement-entry SupportInterior:       {Anchor(a)};
all other actual incidences:             contacts/frozen context, labels unchanged.
```

Thus no constructor-local weakening theorem is required merely to create a stop support.

What remains constructor-specific is **usefulness**: a later `ReplacementClosureCert` may need a larger or differently shaped working patch. The anchor-star theorem does not claim that every class can be reduced by deleting only `p`.

### Why the stronger shrink claim is still invalid

The following typed schema remains a valid S15 canary:

```text
CONTROL-LOCK:
  FERCtrl(r) contains distinct controlled objects c,d;
  a constructor predicate explicitly requires both complete stars;
  an ownership/payer-sensitive source incidence ties c and d;
  deleting d from FERCtrl or relabelling that source incidence as exterior
  changes the constructor predicate.
```

Cycle 15 does not perform that operation. It leaves `FERCtrl(r)` intact and chooses a separate support interior.

Therefore no missing `FERCtrl-restriction` axiom is needed for entry, while any theorem that truly wants to replace the constructor control set must still supply such an axiom explicitly.

## 8. S04 finite one-centre star completion

The fresh S04 specialist completion is consumed only in the identity-bound statement supplied to this cycle: a finite one-centre completed star can stop on its actual interface while guard-side incidences remain typed boundary/exterior objects rather than forcing recursive absorption.

This is a positive model of `FER-ANCHOR-STAR-STOP`, not a repository-bound universal FECT theorem. Protected main still carries only the S04 identity/STANDBY object plus C43/C47/S10 ownership mathematics.

The S04 result confirms two design choices:

- completeness means complete incidence recording at the centre, not ownership of every contact endpoint;
- an exterior-owned guard can remain exterior while still being explicitly recorded in the support interface.

It does **not** license changing ownership of a source-owned guard in another constructor.

## 9. S15 locality attack

S15's locality attack remains valid against either of these bad policies:

```text
contact endpoint -> automatically controlled;
```

or

```text
replace FERCtrl by an arbitrary proper subset and keep the same source theorem.
```

The first can saturate to all of `G`; the second can change constructor semantics.

The anchor-star theorem uses neither policy. Boundary contacts are recorded without control absorption, and FER constructor roles remain immutable. Hence S15 no longer blocks **entry locality**. It still constrains every class-specific working-support theorem and every replacement certificate.

## 10. S02-A unbounded width

The S02-A annular specialist result is consumed in the exact identity-bound orchestration scope supplied to S01: each finite annular source support may be proper while the interface/adhesion grows without a universal bound.

The anchor-star theorem is compatible with this pressure. Its interface size is `deg_G(p)`, which is finite for each actual graph but need not be bounded uniformly over FERs or minimum-counterexample candidates.

No bounded-degree, bounded-adhesion, bounded-hole-count or finite-atlas inference is added.

For WIDE/high-port rows, a later replacement certificate may have to enlarge/refine the star entry to an arbitrarily wide finite working support. That refinement remains part of the class/certificate theorem, not the entry theorem.

## 11. S09/S13C multi-separator residuals

Fresh separator/profile residual statements are consumed only after exact actual source identity. They do not generate an occurrence, but they also do not obstruct the anchor-star entry.

Their multiple separators, return profiles and ownership records remain frozen in `j`. If a downstream structural theorem derives a contradiction directly from them, it produces a class-free or class-bound `StructuralContradictionCert` without needing the star support. If a replacement theorem uses them, its full `ReplacementClosureCert` must bind a working support that records every separator contact it uses.

Counts, profile hashes and residual labels never imply that the current FER has one of those rows.

## 12. S11 multi-hole identity

S11's multi-hole/interface identity is likewise downstream. The existence of a single-centre entry support does not assert that the final replacement working support is a disk or has one boundary component.

A full `ReplacementClosureCert` may carry a working support `s1` together with an exact same-occurrence relation

```text
WorkingSupportFor_G(j,s1)
```

and may use several holes, shared terminals or pinches. It must still satisfy all Cycle-13 gates: exact contacts, ownership, guards, strict descent, nonvacuous complete-Q, same-boundary lifts, both-color positive `R+` and arbitrary-exterior lifting.

The anchor-star support is therefore an **entry witness**, not a universal replacement normal form.

## 13. FER-DISCHARGE-ENTRY-EX1 is now candidate-PASS

Cycle 14 defined the root-minimal source entry as one actual FER/raw/JREL0 chain with either a structural contradiction or a proper source-sound support.

Replace the unnecessarily strong canonical-carrier branch by the weaker entry-support branch:

```text
FER-DISCHARGE-ENTRY_G(r,j) :=
    (exists k StructuralContradictionCert_G(j,k))
 or (exists p,s,
       Anchor_G(a)=p
    and AnchorStarStop_G(j,p,s)
    and EntrySourceSound_G(j,s)
    and ProperFiniteControlledInterior_G(s)
    and BoundaryClosedSupport_G(s)).
```

C48 gives an actual low descriptor, FECT gives an actual same-face FER, and Cycle 10--13 give the raw/JREL0 occurrence interface. Theorem 6.1 supplies the second disjunct for every such FER. Hence:

### Theorem 13.1 — FER-DISCHARGE-ENTRY-EX1

```text
D0_G(f)
 -> exists a,r,j,
      LowDesc_G(f,a)
   and FER_G(f,a,r)
   and RawPhysicalRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and FER-DISCHARGE-ENTRY_G(r,j).
```

Status: **PASS(candidate mathematics)**.

No StructuralContradictionCert is required to establish entry; the structural branch remains an independent earlier exit whenever one is actually proved.

`FER-CARRIER-PROPER` remains OPEN as an optional stronger property of the canonical source-owned carrier, but it is removed from the mandatory root DAG.

## 14. What remains open after entry

The root still needs a proof-carrying discharge certificate, not merely a place to stop.

After an anchor-star replacement entry, semantic classification remains the overlapping relation

```text
AdmissibleClass_G(j,tau,w).
```

A direct `StructuralContradictionCert` can bypass semantic cover completely.

The replacement branch requires one full certificate. The certificate may use the entry star itself or an exact same-occurrence working-support refinement, but no refinement is accepted merely from a catalogue label. The certificate must prove all of:

- actual class witness;
- source-sound working support attached to the same `j`;
- complete boundary/contact ledger;
- exact aliases/geometry;
- all guards including reverse arcs;
- exact ownership and payer/source identities;
- strict frozen-order descent;
- `valid_Q_count>0`;
- ALL complete valid Q colourings;
- same-boundary valid P lifts;
- both-color positive `R_P^+ subseteq R_Q^+`;
- arbitrary-exterior lifting.

Thus Cycle 15 moves the first open modular replacement cut from source locality to **semantic/certificate coverage**. It does not close any class by itself.

## 15. Conditional class status

### J_READY d6

Unchanged. Only after an actual `J_READY,d6` semantic/source match and a class-compatible working support may S09 Cycle 5 identify the exact C37 family/word and R160 supply its strict replacement certificate suffix.

```text
J_READY,d6 suffix = PASS candidate, conditional.
J_READY occurrence / support match = not inferred from anchor-star entry.
J_READY high-port = OPEN.
```

### NONJ_QARC

D4 rigid fibre, SCC, four flip blockers and pair-phase remain available only after exact actual instantiation. `D4-ENDPOINT-TOPOLOGY` remains the first honest unclosed class-wide theorem and must end in either a StructuralContradictionCert or a fully gated ReplacementClosureCert.

### COMPACT_NONJ

Visible S09 Cycle-9 `COMPACT20` remains a conditional matched replacement theorem. The anchor-star entry does not imply `COMPACT20` or a six-hole support.

### F0_ROOT_STAR

S04 one-centre locality makes star support unsurprising, but F0 closure remains open except for exact matched wheel/structural subclasses already recorded. Support existence is not reducibility.

### PINCHED_MULTICONTACT

OPEN. S04/C47 and S11 constrain its multi-terminal/multi-hole ownership and positive-`R+` requirements; the generic anchor-star entry does not collapse the pinch.

### WIDE_CHANNEL / high-port

OPEN. S02-A/B forbid bounded-width local assumptions. A class-compatible certificate may require arbitrarily wide finite support.

## 16. Updated sole DAG

```text
minimum counterexample G
 |
 +-- Sigma mu = -8
 |     -> actual D0(f)
 |
 +-- C48 -> exists LowDesc(f,a)                         [PASS]
 |
 +-- FECT -> actual same-face FER r                     [PASS candidate interface]
 |
 +-- RawPhysicalRow / SameMinCEJREL0                    [PASS candidate]
 |
 +-- FER-ANCHOR-STAR-STOP                               [PASS candidate]
 |     +-- SupportInterior={Anchor(a)}
 |     +-- complete actual star / all crossing contacts
 |     +-- FERCtrl + source ownership unchanged
 |     +-- proper by semidegree>=2
 |     `-- no bounded-width assumption
 |
 +-- FER-DISCHARGE-ENTRY-EX1                            [PASS candidate]
 |     |
 |     +-- StructuralContradictionCert                  [independent class-free exit]
 |     |
 |     `-- replacement entry
 |           -> overlapping AdmissibleClass             [OPEN semantic cover]
 |           -> class-compatible working support         [inside certificate]
 |           -> one full ReplacementClosureCert          [OPEN totality]
 |                +-- J_READY,d6 C37/R160               [conditional PASS suffix]
 |                +-- NONJ_QARC D4 endpoint topology    [OPEN first class-wide]
 |                +-- COMPACT matched partials           [conditional]
 |                +-- F0 matched/structural partials     [conditional]
 |                +-- PINCHED                            [OPEN]
 |                `-- WIDE/high-port                     [OPEN]
 |
 `-- ROOT-CERT-EX1                                       [OPEN]
       -> one structural or replacement certificate per D0
       -> no D0
       -> contradiction with Sigma mu=-8.
```

## 17. Claims boundary

Cycle 15 genuinely strengthens the route in one place only:

```text
FER-DISCHARGE-ENTRY-EX1: OPEN -> PASS(candidate)
```

by replacing the overly strong requirement that the whole canonical source carrier be proper with a source-role-preserving singleton anchor-star entry support.

It does **not** claim:

- that `FERCtrl` can be shrunk;
- that the canonical carrier is proper;
- that every FER has a bounded interface;
- that every entry star has a useful strict replacement;
- that the six semantic classes form a total disjoint partition;
- that any catalogue row occurs;
- that J_READY d6 occurs;
- that multi-separator/profile counts imply an occurrence;
- that S11 is trusted/kernel admitted;
- any B46 theorem, EvidenceLink, Result or Solution;
- or root closure.

`candidate_only`; `best_verified_result=none`; `root_closed=false`.
