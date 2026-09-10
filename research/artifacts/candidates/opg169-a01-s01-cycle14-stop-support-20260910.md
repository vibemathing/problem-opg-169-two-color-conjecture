# R08 S01 Cycle 14 — canonical stop-at-interface support and the first source axiom

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `394f1636a1170ca95e7edd686c65d217fc1c8c20`.

No B46, EvidenceLink, Result, Solution, trusted verification or root closure is created here.

## 1. Exact question after Cycle 13

Cycle 13 reduced the root to one actual raw occurrence with either a direct source contradiction or a fully gated strict replacement. The earliest unresolved source question is therefore not yet a class theorem. It is whether an actual `FirstExposureRecord` admits a source-faithful place to stop before replacement mathematics begins.

The desired object must satisfy all of the following simultaneously:

- be identity-bound to the same selected minimum counterexample `G`, actual root face `f`, C48 low descriptor `a`, FER `r` and raw occurrence `j`;
- be invariant under cyclic re-presentation of rotations/faces;
- retain the actual root/anchor, source/payer identities and all ownership data;
- contain all controlled/source/interface objects that the FER source semantics says belong to the local occurrence;
- contain complete stars for every controlled vertex;
- record every actual support/exterior crossing incidence without recursively adding its exterior endpoint to the support;
- allow more than one boundary component, pinched interfaces and arbitrarily large finite width;
- and, for replacement use, be a strict proper support of `G`.

The last clause is the only clause not currently forced by the consumed FECT source semantics.

## 2. Canonical source carrier

Fix an actual FER/raw occurrence

```text
FirstExposureRecord_G(f,a,r)
RawPhysicalRow_G(f,a,j)
SameMinCEJREL0_G(f,a,j).
```

Let `Seed(r)` be the set of actual vertices, arcs, facial incidences and interface objects explicitly assigned by the FER/raw occurrence to its controlled/source/interface payload. It includes the actual root/anchor objects and every endpoint that is itself an interface object. Merely appearing as the *exterior endpoint* of a contact does not put a vertex in `Seed(r)`.

Define `K_G(r)` to be the least actual incidence subcomplex containing `Seed(r)` and closed under **source-owned incidence only**. In particular:

```text
source-owned internal incidence  -> close inside K;
interface object                  -> retain in K;
contact to an exterior endpoint   -> record the contact, do NOT absorb endpoint;
exterior-owned arc/face           -> do NOT close K through it merely by ownership.
```

The graph `G` is finite, hence `K_G(r)` is finite even when its width is not uniformly bounded over a family of FERs.

### Lemma 2.1 — CANONICAL-CARRIER

`K_G(r)` is uniquely determined by the actual raw occurrence and is invariant under cyclic changes of presentation.

Proof. `Seed(r)` is a set of actual graph/incidence identities, not an ordered serialization. Source ownership is also an identity-bound relation on those actual objects. The least fixed point of the source-incidence closure operator is therefore independent of which half-edge of a cyclic rotation was written first. Reversal is not identified because the fixed plane rotation/orientation is part of the actual source object. Least-fixed-point uniqueness is ordinary set-theoretic uniqueness. No class tag, scheduler, catalogue label or anchor priority is used. ∎

This lemma is candidate-PASS at the same source/identity level as Cycle-12 `RAW-ID-EXTRACT`.

## 3. Exact stars and crossing ledger are constructible without contact absorption

Let

```text
Ctrl(r) = actual vertices marked controlled by the FER/raw occurrence.
```

For every `v in Ctrl(r)`, define

```text
FullStar_G(v)
```

to be the complete actual oriented star read from the fixed embedded `G`. This is a fact about the actual source graph, not a request to recursively enlarge `K_G(r)`.

Define the crossing-incidence ledger by the actual graph:

```text
Cross_G(K) := {
  every oriented arc / facial incidence / declared contact
  with one support-side incidence in K and an exterior-side vertex or cell outside K
}.
```

Each ledger entry records:

- actual endpoint identities;
- direction;
- cyclic position at every support-side endpoint where the rotation is relevant;
- source/exterior/shared ownership;
- alias-normalized identities;
- root/anchor relation when applicable;
- payer/source identity when the incidence belongs to the charge/source ledger.

Crucially, constructing `Cross_G(K)` does **not** change `K`.

### Lemma 3.1 — CONTACT-TOTAL-BY-READBACK

For the canonical carrier `K_G(r)`, every controlled star and every actual crossing incidence can be recorded exactly from the same fixed plane MinCE `G` without absorbing any exterior endpoint.

Proof. `G` is a fixed finite actual graph with fixed rotation. The complete star of a controlled vertex is the finite list of all incident darts in `G`. The crossing ledger is the finite set difference determined by membership in `K_G(r)`. Reading an incidence and recording its endpoint identity is not an incidence-closure rule. Hence no fixed-point contact saturation occurs. Ownership/payer/source data are read from the already identity-bound source bookkeeping and preserved verbatim. ∎

Thus the Cycle-12 S15 fixed-point falsifier attacks only the *bad policy* “every contact endpoint becomes support”. It does not prevent an exact stop-at-interface readback policy.

## 4. Multi-hole and unbounded-width interface semantics

A stop support is not required to be a disk. Define its interface as the actual incidence structure induced by `Cross_G(K)` together with all retained interface vertices/edges/faces in `K`. Boundary components may:

- be several disjoint cycles;
- meet in actual shared vertices;
- be pinched at a terminal pair;
- contain exterior-owned guard arcs between retained interface vertices;
- or have arbitrary finite length.

No theorem below uses a uniform bound on boundary size or adhesion.

This is necessary for the latest specialist pressure:

1. **S02-A unbounded-width annulus.** The specialist result is consumed only as an identity-bound orchestration statement here: its annular source carriers remain proper for each finite state while interface width is unbounded over the family. Therefore any putative `FER-STOP` theorem with a universal constant bound on width/adhesion is too strong. Properness and finiteness, not bounded width, are the correct notions.
2. **S04 one-centre guard-side support.** The corrected two-hole/guard-side geometry shows that a source support may stop with guard-owned/exterior incidence retained rather than absorbed. This is compatible with `K_G(r)` because exterior ownership never forces support closure. Existing protected-main S04 remains identity-only/STANDBY; no new S04 theorem digest is fabricated.
3. **S09/S13C separator-profile residuals.** Profile/separator information can be attached to an already actual carrier and interface, but finite profile rows or separator catalogues do not create the carrier or prove it occurs. Their residuals therefore belong downstream of the stop-support source theorem.
4. **S11 multi-hole identity.** Multi-hole/shared-boundary identity is compatible with the incidence-valued interface above. Ordinary lifting may later quantify over such an exact interface only under its own theorem hypotheses. No new repository-bound S11 admission is claimed.

These four results constrain the theorem's *shape*. None supplies the missing universal source premise identified below.

## 5. Properness is the exact remaining source condition

Define

```text
CarrierProper_G(r) := V(K_G(r)) proper-subset V(G).
```

and

```text
CanonicalStopSupport_G(r,s)
```

to mean that `s` consists of `K_G(r)`, all complete controlled stars, the exact `Cross_G(K_G(r))` ledger, actual interface incidence structure, and the unchanged root/anchor/ownership/payer/source identities.

Because the selected minimum counterexample is connected, if `K_G(r)` is nonempty and proper then there is at least one actual graph edge/contact crossing from `K_G(r)` to `V(G)\V(K_G(r))`. Its exterior endpoint is an explicit witness that an actual exterior vertex survives.

### Lemma 5.1 — STOP-SUPPORT-IF-PROPER

```text
FER_G(f,a,r)
and RawPhysicalRow_G(f,a,j)
and SameMinCEJREL0_G(f,a,j)
and CarrierProper_G(r)
 -> exists unique s,
      CanonicalStopSupport_G(r,s)
   and ProperFiniteSupport_G(s)
   and BoundaryClosedSupport_G(s)
   and SourceSoundStopPolicy_G(s).
```

Proof. Finiteness and canonicity are Lemma 2.1. Exact complete stars and exact crossing ledger are Lemma 3.1. Properness is the displayed hypothesis. Connectedness supplies at least one crossing contact/exterior vertex. `SourceSoundStopPolicy` is precisely the rule used in the construction: source-owned incidence closes the carrier; contact/exterior incidence is recorded but does not enlarge the carrier. Root/anchor/ownership/payer identities were never changed. ∎

This theorem does not assume a single disk, bounded adhesion, a class tag, a catalogue row or a replacement.

## 6. What FECT does not currently prove

The currently consumed FECT contract gives an actual same-face FER/raw occurrence with physical/provenance content. It does not expose a protected-main source theorem of the form

```text
FER_G(f,a,r) -> CarrierProper_G(r).
```

Equivalently, it does not currently prove that the least source carrier leaves a vertex of the actual selected `G` outside.

Call the missing statement

```text
FER-CARRIER-PROPER:
forall actual FER r,
  V(K_G(r)) proper-subset V(G).
```

or equivalently, in source-facing language,

```text
FER-EXTERIOR-SURVIVES:
forall actual FER r,
  exists x in V(G) \ V(K_G(r)).
```

A still weaker root-useful version is existential per actual D0 face:

```text
FER-GOOD-ENTRY-EX1:
D0_G(f)
 -> exists a,r,j,
      LowDesc_G(f,a)
   and FER_G(f,a,r)
   and RawPhysicalRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and (
        exists k StructuralContradictionCert_G(j,k)
        or CarrierProper_G(r)
      ).
```

The universal theorem is useful for architecture; the existential theorem is all the root requires.

## 7. Smallest source-semantic failure state

No actual minimum-counterexample instance can be exhibited without resolving the root conjecture. Therefore Cycle 14 does not fabricate a plane MinCE counterexample.

The smallest **source-data state not excluded by the current consumed FECT premises** is instead:

```text
FULL_CARRIER branch:
  one actual FER/raw identity j;
  K_G(r) = V(G);
  all controlled stars exact;
  Cross_G(K_G(r)) = empty;
  root/anchor/ownership/payer identities exact;
  no StructuralContradictionCert supplied.
```

Every physical/provenance statement can hold in this source-semantic state, yet no proper replacement support follows. This is a typed nonderivability model, not a claimed realized MinCE.

It identifies the missing source axiom exactly: the stopping semantics must guarantee that at least one actual exterior vertex survives the canonical source carrier, or else directly produce a structural contradiction before replacement is attempted.

A stronger axiom such as bounded width, bounded number of holes, unique class or catalogue membership is neither necessary nor supported by the specialist results.

## 8. Earliest root theorem after the audit

Define

```text
FER-DISCHARGE-ENTRY_G(r,j) :=
    (exists k StructuralContradictionCert_G(j,k))
 or (CarrierProper_G(r)
     and exists s CanonicalStopSupport_G(r,s)).
```

Then the root-minimal theorem is

```text
FER-DISCHARGE-ENTRY-EX1:
D0_G(f)
 -> exists a,r,j,
      LowDesc_G(f,a)
   and FER_G(f,a,r)
   and RawPhysicalRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and FER-DISCHARGE-ENTRY_G(r,j).
```

Status: **OPEN_FIRST_ROOT_SOURCE CUT**.

Why this is earlier than semantic cover: a class-free structural contradiction can discharge an FER with no class witness, while a proper replacement entry reaches class semantics only after the source carrier is certified proper. The six class predicates therefore remain a downstream overlapping relation, not part of stop-support identity.

## 9. Downstream class boundary after a proper entry

For a proper canonical stop support `s`, replacement mathematics may use

```text
AdmissibleClass_G(j,tau,w)
```

with overlaps allowed. Root acceptance remains existential over one proof-carrying replacement certificate:

```text
exists tau,w,k,
  AdmissibleClass_G(j,tau,w)
  and ReplacementClosureCert_G(j,s,tau,w,k).
```

No scheduler and no `ALL applicable tags close` theorem is needed.

The Cycle-13 replacement certificate gates remain unchanged: exact source-sound support policy; proper finite support; boundary closure; aliases/geometry; guards; ownership; payer/source identities; strict descent; `valid_Q_count>0`; ALL complete valid Q colourings; same-boundary P lifts; both-colour positive `R+`; arbitrary-exterior lifting.

## 10. Conditional specialist consumers after exact entry

Nothing below creates a FER, support or class occurrence.

### J_READY d6

Only after an actual proper stop support and actual admissible `J_READY,d6` witness may S09 Cycle 5 derive the exact C37 family/word and use R160. The suffix remains candidate-PASS; `J_READY` occurrence and the high-port branch remain open.

### S02-A / S02-B

Unbounded annular/high-port families forbid silently adding a uniform width bound to source support and pressure any local replacement strategy. They create neither a root occurrence nor a structural contradiction certificate.

### S04

The exact corrected guard/two-terminal ownership remains a constraint on a matching support/replacement certificate. It cannot be inverted into a pinched FER occurrence, and C47 remains narrowly scoped.

### S09/S13C separator-profile residuals

Any separator/profile theorem is consumed only after the actual `K_G(r)`, interface and source hypotheses match. Counts, profile hashes and residual catalogues cannot prove `CarrierProper`, `AdmissibleClass` or occurrence.

### S11

Multi-hole identity/lifting is a downstream consumer only after an exact multi-hole support is bound. It does not prove that a generic FER has nonempty exterior.

### F0 / COMPACT / D4

Existing partial F0 and COMPACT consumers remain conditional on actual matched support. D4 retains the rigid-fibre/SCC/four-blocker/pair-phase core, but endpoint-sensitive topology remains open. `D4-ENDPOINT-TOPOLOGY` is still the first honest unclosed **class-wide** closure lemma after source entry and semantic instantiation.

## 11. Updated sole DAG

```text
minimum counterexample G
 |
 +-- Sigma mu = -8
 |     -> actual D0(f)
 |
 +-- C48 -> exists LowDesc(f,a)                         [PASS]
 |
 +-- FECT -> actual FER r                               [PASS candidate interface]
 |
 +-- RawPhysicalRow / SameMinCEJREL0                    [PASS candidate]
 |
 +-- canonical least source carrier K(r)               [PASS candidate]
 |     +-- complete controlled stars                    [PASS by actual-G readback]
 |     +-- exact crossing-contact ledger                [PASS by actual-G readback]
 |     +-- multi-hole / arbitrary finite width allowed
 |     `-- root/anchor/ownership/payer preserved
 |
 +-- FER-DISCHARGE-ENTRY-EX1                            [OPEN FIRST SOURCE CUT]
 |     |
 |     +-- StructuralContradictionCert                  [class-free option]
 |     |
 |     `-- CarrierProper / FER-EXTERIOR-SURVIVES        [MISSING SOURCE AXIOM]
 |           -> CanonicalStopSupport                    [PASS conditional]
 |           -> overlapping AdmissibleClass             [semantic cover OPEN]
 |                 |
 |                 +-- J_READY,d6 -> C37/R160           [conditional PASS suffix]
 |                 +-- NONJ_QARC -> D4 endpoint topo    [OPEN first class-wide]
 |                 +-- COMPACT matched partials          [conditional only]
 |                 +-- F0 matched partials               [conditional only]
 |                 +-- PINCHED                            [OPEN]
 |                 `-- WIDE/high-port                     [OPEN]
 |           -> one ReplacementClosureCert
 |
 `-- one structural or replacement certificate per D0
       -> no actual D0
       -> contradiction with Sigma mu = -8.
```

## 12. Exact disposition

Candidate-PASS:

- canonical source carrier construction;
- cyclic-presentation invariance;
- complete controlled-star and crossing-contact readback without contact absorption;
- arbitrary finite width / multi-hole compatible interface type;
- `STOP-SUPPORT-IF-PROPER`.

OPEN:

- universal `FER-CARRIER-PROPER`;
- weaker root-minimal `FER-DISCHARGE-ENTRY-EX1`;
- downstream semantic cover;
- all class-wide closures except already conditional suffixes.

The highest-value next source theorem is therefore not another catalogue. It is either:

```text
FER-EXTERIOR-SURVIVES
```

for the actual FECT stopping semantics, or the weaker root theorem that for each actual D0 one FECT output is either directly structurally contradictory or has a surviving exterior vertex.

`candidate_only`; `best_verified_result=none`; `root_closed=false`.
