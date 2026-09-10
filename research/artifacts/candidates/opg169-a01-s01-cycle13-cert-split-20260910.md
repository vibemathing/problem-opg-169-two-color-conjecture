# R08 S01 Cycle 13 — parallel semantic/locality branches and proof-carrying root certificates

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff: `59585493669fd2feeef00121b4464f69913fb28c`.

This is a candidate integration theorem. It creates no EvidenceLink, Result, Solution, trusted-verifier receipt, or root closure. B46 is not used.

## 1. Cycle-12 boundary and the S10 Cycle-9 correction

Cycle 12 deliberately separated tag-free physical occurrence identity from local replacement usability:

```text
actual D0 / LowDesc / FER
 -> RawPhysicalRow
 -> SameMinCEJREL0
 -> ProperFiniteSupport + BoundaryClosedSupport
 -> semantic class
 -> one closure certificate.
```

The fresh S10 Cycle-9 correction changes one logical edge, not the physical occurrence layer. After `SameMinCEJREL0`, **semantic classification and replacement locality are parallel pieces of information**. Proper locality is mandatory for a replacement theorem, but it is not a universal prerequisite for a direct source contradiction.

For example, an actual raw occurrence may occupy all of `G`. Such a row is useless as a strict local replacement patch, but if its exact actual source facts themselves contradict a theorem of the selected minimum counterexample, no replacement disk is needed.

Therefore Cycle 13 replaces the single closure type by two proof-carrying certificate types:

```text
(A) StructuralContradictionCert
(B) ReplacementClosureCert.
```

No certificate is created merely by a tag, a catalogue entry, a row count, or absence from a finite catalogue.

The S10 Cycle-9 correction is consumed as an identity-bound Cycle-13 orchestration input. At this cutoff no separately protected-main S10 Cycle-9 artifact/digest is visible, so none is fabricated.

## 2. Physical occurrence layer remains unchanged

Fix the selected plane minimum counterexample `G`, an actual unpaid negative face `f`, one actual C48 low descriptor `a`, and an actual same-face FER `r`.

Cycle 12's tag-free, cyclic-presentation-invariant physical row remains:

```text
RawPhysicalRow_G(f,a,j)
and SameMinCEJREL0_G(f,a,j).
```

Its exact identity retains:

- actual `G`, root face `f`, LowDesc `a`, FER occurrence anchor `r`;
- aliases normalized by actual equality before geometry;
- oriented source/QARC/contact incidences;
- cyclic successor relations for rotations and face/boundary walks, invariant under cyclic start-index shift but not reversal;
- complete-star declarations where the source says a star is complete;
- source/exterior/shared ownership;
- payer/source identities and ledger provenance;
- literal source-facing port/contact data.

It contains no exclusive class tag, scheduler choice, catalogue name or replacement-support policy.

Thus

```text
RAW-ID-EXTRACT:
FER_G(f,a,r) -> exists unique j RawPhysicalRow_G(f,a,j)
```

and the physical/provenance implication to `SameMinCEJREL0` remain candidate-PASS. Cycle 13 does not infer local replaceability from them.

## 3. Overlapping semantic classes remain a relation

Let

```text
AdmissibleClass_G(j,tau,w)
```

mean that the already actual raw row `j` satisfies one semantic source class with exact witness data `w`.

The class names remain

```text
F0_ROOT_STAR
J_READY
COMPACT_NONJ
NONJ_QARC
PINCHED_MULTICONTACT
WIDE_CHANNEL.
```

Multiple `(tau,w)` may be admissible for one row. No precedence or scheduler is part of the theorem.

The semantic-cover statement is still

```text
SEMANTIC-COVER:
RawPhysicalRow_G(f,a,j)
and SameMinCEJREL0_G(f,a,j)
 -> exists tau,w AdmissibleClass_G(j,tau,w).
```

Cycle 11 already restored this as OPEN because the executable six-name descriptions have literal overlaps and gaps. Cycle 13 does not repair those gaps by declaration.

However, after the S10 correction, `SEMANTIC-COVER` is **not logically mandatory for a row that already has a direct StructuralContradictionCert**. It remains the highest-leverage modular bridge for the six-class architecture, not a universal premise of every possible root certificate.

## 4. Source-sound replacement-locality policy

A replacement theorem must not obtain locality by recursively swallowing contact endpoints or by selecting an arbitrary convenient subset of the raw row.

Define

```text
SourceSoundLocality_G(j,s)
```

for a policy witness `s` containing an actual source patch `P_s`, vertex support `S_s`, changed/deleted interior `I_s`, interface/boundary `B_s`, and exact ownership/contact map, with the following requirements.

### 4.1 Source-faithful selection

The support is selected by a theoremically justified source policy from the actual raw occurrence. Every vertex/arc/face role used by the local theorem realizes in the same `G`; aliases are normalized before selecting geometry. The policy may restrict the raw occurrence only where the source theorem permits that restriction.

No control graph, catalogue member or isomorphic abstract patch is substituted for the actual row.

### 4.2 Proper finite support

```text
ProperFiniteSupport_G(j,s) :=
  S_s is finite and S_s is a strict subset of V(G).
```

Since `G` is finite, finiteness alone is automatic once a concrete support is named; the substantive condition is properness. At least one actual exterior vertex survives.

Properness is not inferred by recursively adding contact endpoints until there are no unrecorded contacts. The Cycle-12/S15 fixed-point example shows that policy can reach all of a connected `G`.

### 4.3 Boundary closure without absorption

```text
BoundaryClosedSupport_G(j,s)
```

requires every actual arc crossing between the changed support/interior and its exterior to be recorded exactly with direction, endpoints/roles, cyclic position and ownership. Complete-star claims are checked against actual `G`.

An exterior endpoint remains exterior. Recording a contact is not permission to absorb that endpoint into `S_s`.

### 4.4 Source/ownership/payer soundness

The support policy retains exact source-versus-exterior ownership for every changed, retained or shared arc/face; every payer/source ID agrees with the same actual charge ledger; no payer is duplicated or reassigned merely to make a local theorem apply.

Define the root-useful local policy predicate

```text
SourceSoundProperSupport_G(j,s) :=
    SourceSoundLocality_G(j,s)
 and ProperFiniteSupport_G(j,s)
 and BoundaryClosedSupport_G(j,s).
```

Cycle 13 does **not** mark

```text
RawPhysicalRow + SameMinCEJREL0 -> exists s SourceSoundProperSupport(j,s)
```

PASS. It is an OPEN replacement-branch subcut. The full-graph fixed-point construction disproves the naive extraction policy; it does not prove that no better source-sound proper support exists.

## 5. Certificate A — StructuralContradictionCert

A structural certificate proves that this actual source occurrence cannot exist in the selected minimum counterexample **without changing the graph**.

Define

```text
StructuralContradictionCert_G(j,kappa)
```

only when `kappa` contains:

1. the exact identity of `G,f,a,r,j` used by the proof;
2. every actual vertex/arc/face/rotation/ownership/payer fact used by the contradiction;
3. the exact theorem or directly supplied proof that applies to those facts in the selected MinCE class;
4. a derivation of an actual contradiction: e.g. violation of a proved semidegree/minimality/planarity/ownership constraint, an impossible same-source configuration, or another explicit `False` conclusion;
5. no occurrence inference from an atlas, row count, control graph, or catalogue absence.

A class witness may be included in `kappa` if the structural theorem is class-specific, but it is not required by the certificate type.

### Structural soundness lemma

```text
RawPhysicalRow_G(f,a,j)
and SameMinCEJREL0_G(f,a,j)
and StructuralContradictionCert_G(j,kappa)
 -> contradiction in G.
```

This is tautological only in the proof-carrying sense: a valid certificate contains the checked theorem premises and their actual realization. The validator is forbidden to accept a label such as `STRUCT`, `F0`, or `separator` without the proof of contradiction.

### Locality bypass is narrow

`StructuralContradictionCert` does **not** require `ProperFiniteSupport`. A full-graph row is allowed because no local replacement is performed.

This bypass cannot be used for a statement of the form “no replacement from library L was found” or “all tested templates fail”. Those are not contradictions in the actual source graph.

## 6. Certificate B — ReplacementClosureCert

A replacement certificate proves that the actual occurrence is reducible by replacing an actual proper source patch while holding the arbitrary exterior fixed.

Define

```text
ReplacementClosureCert_G(j,tau,w,s,kappa)
```

only if all of the following are carried and validated.

### 6.1 Actual class and source policy

```text
AdmissibleClass_G(j,tau,w)
and SourceSoundProperSupport_G(j,s).
```

The class witness and support policy must be mutually compatible: the patch on which the class theorem acts is the actual patch selected by `s`, not a different isomorphic control.

### 6.2 Concrete replacement

`kappa` contains the finite replacement `Q`, exact common boundary/interface identification and all changed/retained arcs. Alias normalization occurs before geometry. The resulting whole graph `H=G[P_s -> Q]` must be a finite simple plane orientation in the frozen class.

### 6.3 Exact guards

Every inserted or reused arc has an actual guard check. If a reverse actual arc exists, the proposed insertion is rejected. Same-direction reuse is allowed only where ownership/interface semantics explicitly permit it. All theorem-specific guards are checked on actual `G`.

### 6.4 Ownership and payer preservation

Every changed, deleted, shared and exterior arc/face has exact ownership. The same actual payer/source IDs are retained and no payer is double-spent or silently moved across the patch/exterior boundary.

### 6.5 Strict descent

The whole replacement graph satisfies the strict order used to choose the minimum counterexample:

```text
order(H) < order(G).
```

The certificate states the exact descent witness. “Different graph” or “smaller local picture” is insufficient.

### 6.6 Nonvacuous complete-Q universe

The complete replacement-colouring universe is nonempty:

```text
valid_Q_count > 0.
```

The certificate quantifies over **all** valid complete colourings of `Q` consistent with the shared boundary/interface, not one convenient colouring or one producer orbit.

### 6.7 Same-boundary source lift and both-colour positive reachability

For every valid complete `Q` colouring `chi_Q`, the certificate supplies a valid complete colouring `chi_P` of the actual source patch with the same boundary colours and, for each colour `c in {0,1}`,

```text
R^+_{P,c}(chi_P) subseteq R^+_{Q,c}(chi_Q).
```

Zero-length reachability is not substituted for positive reachability.

### 6.8 Arbitrary-exterior lifting

The exact boundary/contact/ownership data satisfy the ordinary arbitrary-exterior lifting theorem content. Therefore the colouring of the strictly smaller whole graph `H`, supplied by minimum order, lifts across the actual patch while every exterior vertex/arc stays fixed. This yields a valid colouring of `G`, contradicting minimum-counterexample status.

### Replacement soundness lemma

```text
RawPhysicalRow_G(f,a,j)
and SameMinCEJREL0_G(f,a,j)
and ReplacementClosureCert_G(j,tau,w,s,kappa)
 -> contradiction in G.
```

The proof is exactly strict minimality followed by the complete-Q/full-positive-R arbitrary-exterior lift. Trusted Evidence admission is a separate later concern; this is candidate mathematical theorem content.

## 7. One proof-carrying row certificate

Define

```text
RowClosureCert_G(j) :=
    (exists kappa,
       StructuralContradictionCert_G(j,kappa))
 or (exists tau,w,s,kappa,
       AdmissibleClass_G(j,tau,w)
   and SourceSoundProperSupport_G(j,s)
   and ReplacementClosureCert_G(j,tau,w,s,kappa)).
```

The second disjunct intentionally repeats the semantic/support predicates even though a well-formed `ReplacementClosureCert` checks them internally. This makes the root quantifiers explicit and prevents a transport object from hiding the source gates.

`RowClosureCert` is scheduler independent. If several class witnesses or support policies are admissible, the proof needs only one exhibited certificate.

No `ALL applicable tags close` condition appears.

## 8. Weakest face-level root theorem — ROOT-CERT-EX1

The weakest root statement consistent with the established choice-free architecture is not universal closure of every LowDesc/FER/raw row. One certified actual chain per actual negative face is sufficient.

Define

```text
ROOT-CERT-EX1:
D0_G(f)
 -> exists a,r,j,
      LowDesc_G(f,a)
   and FirstExposureRecord_G(f,a,r)
   and RawPhysicalRow_G(f,a,j)
   and SameMinCEJREL0_G(f,a,j)
   and RowClosureCert_G(j).
```

### Sufficiency proof

Assume an actual `D0_G(f)`. Apply `ROOT-CERT-EX1` and take the exhibited actual chain.

- If the row carries a `StructuralContradictionCert`, Section 5 gives an immediate contradiction in the same `G`.
- If it carries a `ReplacementClosureCert`, Section 6 gives a strictly smaller graph in the frozen class; minimum order colours it, and the proof-carrying complete-Q/full-R+ lift colours `G`, again a contradiction.

Hence no actual `D0` can exist. The unchanged charge ledger has total final charge `-8`; if no final face is negative while vertices finish nonnegative/zero as in the candidate route, the final charge step contradicts that total.

Therefore `ROOT-CERT-EX1`, together with the already consumed entrance/charge interfaces, is sufficient for the root route.

Cycle 13 does **not** prove `ROOT-CERT-EX1`.

### Stronger optional row theorem

A reusable stronger statement is

```text
ROW-CERT-TOTAL:
LowDesc(f,a) and FER(f,a,r)
and RawPhysicalRow(f,a,j) and SameMinCEJREL0(f,a,j)
 -> RowClosureCert(j).
```

It implies `ROOT-CERT-EX1` using C48/FECT entrance, but the root does not require every alternative descriptor or raw occurrence to be certified. This distinction preserves the prior choice-free weakening.

## 9. Parallel rather than serial DAG after SameMinCEJREL0

The corrected local architecture is:

```text
                         +--> direct structural theorem
                         |       -> StructuralContradictionCert
                         |
RawPhysicalRow/JREL0 ----+--> AdmissibleClass(j,tau,w) -------------+
                         |                                            |
                         +--> SourceSoundProperSupport(j,s) -----------+--> ReplacementClosureCert
```

Classification and locality are therefore parallel relations on the actual row. They meet when a replacement certificate requires both.

A class-specific structural theorem may use `AdmissibleClass` and then produce a `StructuralContradictionCert` without joining the locality branch.

## 10. Ranked live subcuts

There is no strict logical chain between the first two items because a direct structural certificate can bypass both. The following ranking is by current modular root leverage.

### Rank 1 — semantic cover

```text
SEMANTIC-COVER:
actual RawPhysicalRow/JREL0
 -> exists tau,w AdmissibleClass(j,tau,w).
```

Status: **OPEN**. The Cycle-11 overlap/gap audit still blocks totality. This bridge gives every non-directly-structural row a typed theorem lane and is therefore the broadest reusable missing source theorem.

It is not required for a row already possessing a class-free structural contradiction.

### Rank 2 — source-sound proper support

```text
SOURCE-SOUND-PROPER-SUPPORT:
actual RawPhysicalRow/JREL0
 -> exists s SourceSoundProperSupport(j,s).
```

Status: **OPEN for the replacement branch**. The S15 full-contact fixed point shows naive contact saturation is unsound as an extraction proof. A source theorem must exhibit a proper support policy and exact boundary without changing the source meaning.

This rank is lower than semantic cover because it is irrelevant to a structural contradiction branch, but it is mandatory for every replacement certificate.

### Rank 3 — first honest class close

After an exact semantic witness exists, and after proper support exists when the intended proof is a replacement, the first class theorem must actually produce one of the two certificate types.

Several narrow suffixes are already conditional candidate-PASS; the first currently honest **unclosed class-wide** bridge remains

```text
NONJ_QARC -> D4-ENDPOINT-TOPOLOGY.
```

The D4 result must declare its output type. If endpoint-sensitive topology yields a contradiction directly in the actual source, it is a `StructuralContradictionCert` and needs no proper-support premise. If it constructs a smaller patch replacement, every Section-6 replacement gate becomes mandatory.

## 11. Conditional integration — J_READY and S02 pressure

### J_READY,d6

For an actual admissible selected-J degree-six witness whose replacement support is source-sound/proper/boundary-closed, S09 Cycle 5 derives the exact C37 family/word from actual geometry before the R160 rule is used. C37/R160 supplies strict arbitrary-exterior complete-Q/full-R+ reduction data.

Thus it fits `ReplacementClosureCert` conditionally after the new source-locality gates.

Cycle 13 does not infer J_READY occurrence from C37.

### S02 high-port stress

Merged S02-B Cycle 3 supplies a root-class high-port stress family with growing exposure interface and no strict same-boundary replacement for every consecutive A-star block of sizes one through three in its stated finite-exhaustive scope.

This is **not** a StructuralContradictionCert for an actual FER row and not a proof that a larger/nonlocal replacement cannot exist. It is pressure against silently assuming a small source-sound support or a universally useful bounded terminal.

It may be consumed only after an actual source occurrence is proved to satisfy the S02 family hypotheses. No stress-family count or family existence is inverted into a MinCE occurrence.

## 12. Conditional integration — S04 / C47 two-terminal geometry

The repository-bound S04 identity points back to C43/C47/S10 for mathematics. The exact two-hole geometry remains

```text
H13=(7,8,16,12)
H14=(8,15,12,17)
intersection of vertices = {8,12}
no shared edge
guard 8->12 exterior.
```

The lobe interface is a vertex-only two-terminal separator, not a common `K2` tournament.

Consequently, for an actual row matching this source geometry, any proposed pinched/multicontact `ReplacementClosureCert` must preserve the exterior ownership of the guard, use the actual two-terminal boundary, and check full positive `R+`; ordinary same-boundary extension alone is insufficient.

C47's negative/finite scope remains delete `{13,14}` plus at most one new nonisolated internal vertex total in the owning disks. Failure inside that scope is not a StructuralContradictionCert and is not extrapolated to all replacements.

No S04 control/count creates occurrence.

## 13. Conditional integration — F0 wheel results

Repository wheel theorems C18/C19 are consumed only after an actual raw occurrence and exact wheel/source hypotheses are matched.

C18 gives the exact degree-five wheel fixed-colouring extension obstruction with its genuine exterior return-path bit. It is a source theorem about an actual wheel when its hypotheses are realized, not a general F0 closure certificate.

C19 proves that, in the selected triangulation, an exact degree-five wheel with exactly one directed incident face forces an actual directed separating triangle with at least four vertices on each side.

This is a **structural consequence**, not automatically a `StructuralContradictionCert`: the current root route has not proved that such a separator is impossible. If an additional exact source theorem later supplies `no such directed separator` for the same selected MinCE/row, then C19 plus that theorem would form a structural certificate and would not need ProperFiniteSupport.

No wheel-subclass count or catalogue match implies F0 occurrence or F0 class totality.

## 14. Conditional integration — COMPACT_NONJ Cycle 9

The fresh S09 Cycle-9 compact branch at commit `b459b83b5b7c3ae7e19631c133839750132f393f` gives a row-level conditional theorem, not an occurrence theorem.

Its exact acceptance predicate `COMPACT20(r)` requires an actual six-boundary compact source patch with nonempty source interior, complete contacts/stars, exact ownership/payer data, source-safe chord guards, nonvacuous complete-Q and the two-colour positive-reachability profile.

Under an actual compact occurrence and those exact hypotheses, deleting the nonempty interior and inserting the source-safe template is strict, and the arbitrary-exterior lifting theorem yields closure. Rephrased in Cycle-13 types:

```text
actual RawPhysicalRow/JREL0
+ AdmissibleClass(j,COMPACT_NONJ,w)
+ SourceSoundProperSupport(j,s)
+ COMPACT20 compatibility on that actual support
 -> ReplacementClosureCert(j,COMPACT_NONJ,w,s,kappa).   [candidate]
```

The branch's one-reverse-edge compact counterrow is especially important: the local profile has one candidate template before exterior guards, but an actual exterior reverse arc kills it. Therefore class membership/profile alone cannot manufacture a replacement certificate; exact guards and ownership remain mandatory.

The 20 C35 controls/19 systems/85 symmetry-closed systems are controls/library data only. They are never inverted into occurrence or class totality.

## 15. Conditional integration — D4 symbolic result

The consumed S12-A Cycle-9 D4 content still supplies, conditionally on exact actual q-arc/D4 instantiation:

- rigid fibre;
- SCC structure;
- four flip blockers;
- pair-phase.

Endpoint-sensitive topology remains the missing theorem.

Cycle 13 sharpens its target type:

```text
D4-ENDPOINT-TOPOLOGY
 -> either StructuralContradictionCert
    or ReplacementClosureCert with every replacement gate.
```

A symbolic blocker table, flip orbit or pair-phase statement by itself is neither certificate. The theorem must bind actual endpoints/rotation/contacts/source ownership and finish one of the two proof types.

## 16. Conditional fresh-result discipline

At the fresh protected-main cutoff no newer merged S02 or S04 theorem, no protected-main S10 Cycle-9 artifact, and no protected-main D4 endpoint theorem were found. They are therefore consumed only in the exact already repository-bound/orchestration-bound scopes stated above.

The S09 Cycle-9 COMPACT branch is an exact visible branch commit and is consumed conditionally as a row-level theorem interface; it is not treated as protected-main admission.

F0 uses the exact repository C18/C19 theorem bytes already on main, conditional on actual source matching.

No source count, finite atlas, branch existence or PR status is mathematical occurrence evidence.

## 17. Updated sole proof DAG

```text
minimum counterexample G
 |
 +-- Sigma mu = -8
 |     -> actual D0(f)
 |
 +-- C48
 |     -> exists LowDesc(f,a)                              [PASS candidate]
 |
 +-- FECT physical entrance
 |     -> actual same-face FER r                           [PASS candidate interface]
 |
 +-- RAW-ID-EXTRACT / SameMinCEJREL0
 |     -> actual cyclic-invariant RawPhysicalRow j         [PASS candidate]
 |
 +-- certificate search                                    [ROOT-CERT-EX1 OPEN]
 |     |
 |     +-- STRUCTURAL BRANCH
 |     |     actual source theorem/proof
 |     |       -> StructuralContradictionCert              [OPEN generally]
 |     |       -> contradiction
 |     |
 |     `-- REPLACEMENT BRANCH
 |           +-- AdmissibleClass(j,tau,w)                  [SEMANTIC-COVER OPEN]
 |           |
 |           +-- SourceSoundProperSupport(j,s)             [OPEN]
 |           |
 |           `-- exact guards/ownership/payer
 |               + strict descent
 |               + nonvacuous ALL complete-Q
 |               + same-boundary P lift
 |               + both-colour positive R+
 |               + arbitrary-exterior lifting
 |                    -> ReplacementClosureCert
 |                    -> contradiction
 |                    |
 |                    +-- J_READY,d6                       [conditional PASS]
 |                    +-- COMPACT20 matched row             [conditional PASS]
 |                    +-- F0 wheel consequences             [partial; not general cert]
 |                    +-- NONJ_QARC / D4 endpoint topology  [OPEN class-wide]
 |                    +-- PINCHED / S04 two-terminal gates  [OPEN]
 |                    `-- WIDE / high-port                  [OPEN]
 |
 +-- one proof-carrying certificate for one actual row per D0
 |     -> no actual D0
 |
 `-- final charge contradiction.
```

The diagram is intentionally not a serial `class -> locality -> closure` chain. Semantic class and local support are parallel predicates and only the replacement certificate requires their intersection.

## 18. Exact next priorities

### Highest-value theorem

```text
ROOT-CERT-EX1
```

is the weakest direct root bridge. A successful proof may mix structural rows and replacement rows; it need not force every row through local replacement.

### Modular subcut priority

1. `SEMANTIC-COVER`, for rows not already directly structurally contradictory;
2. `SOURCE-SOUND-PROPER-SUPPORT`, replacement branch only;
3. first honest unclosed class-wide certificate theorem, currently `D4-ENDPOINT-TOPOLOGY`.

This ranking is by reuse/root leverage, not a claim that 1 and 2 are logically serial.

No B46 reconstruction, EvidenceLink, Result, Solution, trusted admission, count-to-occurrence inference, or root closure is made.

`candidate_only`; `best_verified_result=none`; `root_closed=false`.
