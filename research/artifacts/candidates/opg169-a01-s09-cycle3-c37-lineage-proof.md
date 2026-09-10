# R08 S09 Cycle 3 — C37 full 160-parent source-lineage atlas

`verdict=candidate_only`; `root_closed=false`; `best_verified_result=none`.

Fresh protected base at construction: `160fa1085f274191bc09185f289d5ac2c4c6362e`.

## 1. What this cycle certifies

S10's merged clean-room receipt confirms exact C37 `d(7)=6` coverage `160/160`, but records S09 as `NOT_VERIFIABLE_MISSING_SOURCE` because no repository-bound exact S09 remaining/source-lineage registry existed. This cycle supplies that missing source object.

It does **not** enumerate C40 guard children and does not rerun the profile search. It freezes all `5 x 32 = 160` C37 parents in a machine-readable generative normal form and proves the exact-parent inheritance condition needed by C48 ancestor precedence.

Files:

```text
research/artifacts/candidates/opg169-a01-s09-cycle3-c37-lineage-atlas.json
research/artifacts/candidates/opg169-a01-s09-cycle3-lineage-check.py
```

Atlas SHA-256: `1502702e3825a8ccc79f9162fe412371bc14091a8260a42b90f6826f44fda606`  
Expanded parent-ID SHA-256: `cb8b4171491572de52a1ca5f3ebe1235e6091dd7298c5b380f0477d0c9789b74`  
Expanded 160-row SHA-256: `65357c97e5fdb35ba150c7d658ed053489097ee6d1013ec03529685f643b6dab`  
Checker SHA-256: `5a319d5d329f0ea80d2f22c04d715fcb56af1e51a80f61cb5a563c5ea643e609`

The checker expands the normal form to all 160 rows and validates source identities, direct-fan physical reverse conflicts, rule-class counts and the exact `D/19 -> C40` core identity. It deliberately does not recompute strong-profile tables.

## 2. Exact 160-parent universe

C37 controls

```text
I={0,2,3,7},  degrees=(5,5,5,6),
```

and fixes the 18-arc J core. The surviving equality families are

```text
D=(12,13), X5=(5,13), X6=(6,13), Y4=(12,4), Y5=(12,5).
```

For a family `(x,y)`, word `w in {0,...,31}` acts on

```text
(8,x), (x,7), (x,y), (y,7), (y,11)
```

by reversing edge-role `i` iff bit `i` of `w` is one. C37 says all 32 words occur in each surviving family. The atlas stores the family aliases, complementary regions and exact bit semantics; the checker materializes the five directed extra arcs for every `(family,word)` and binds the expanded row set by digest.

Thus the registry is exactly

```text
{D,X5,X6,Y4,Y5} x {0,...,31},
```

with 160 unique source IDs.

## 3. Ancestor reduction classes

S06 supplies a final unconditional menu of 156 merged `delete {0,2}` rows plus four bare `delete 3` rows. S10 independently reimplemented the finite consumer and reports the same split, `21,732` complete valid Q colourings, `16,536` equal positive-reachability lifts, `5,196` strict lifts and zero failures. S10 is candidate-level clean-room corroboration, not a trusted verifier.

The atlas makes the source-lineage allocation explicit.

### 3.1 96 exact direct-fan parents

Deleting `{0,2}` leaves the actual hole

```text
H=(3,4,5,6,11,7).
```

The literal fan

```text
5->7, 6->7, 7->4
```

is source-valid iff no reverse source arc `7->5`, `7->6` or `4->7` is present.

This gives a symbolic, non-enumerative split:

```text
D : all 32 words.
X5: bit1=0 -> 16 words.
X6: bit1=0 -> 16 words.
Y4: bit3=1 -> 16 words.
Y5: bit3=0 -> 16 words.
```

Total: `96`. The atlas records these exact word sets and the exact fan literal.

### 3.2 60 other merged-hexagon parents

The direct fan is class-invalid on 64 parents because a desired fan arc is opposite to a real parent arc. Four of those use the bare rule below. The other 60 have an unconditional `delete {0,2}` rule in S06's complete merged-hexagon catalogue, clean-room corroborated by S10.

S09 does not fabricate the 60 literal added-arc sets. Their atlas class is

```text
merged_delete_0_2_catalogue
```

with the literal bound to the frozen S06 postprocess output SHA-256

```text
a3ceecc524f1ef24f81e132fe99ddd4daff3feaa649ea0255898a213ae64a8e5
```

rather than rederived here.

### 3.3 Four exact bare-delete parents

Exactly

```text
Y4/0, Y4/4, Y4/16, Y4/20
```

use bare `delete 3`, with no added arc. The actual deletion hole is

```text
(0,4,8,7,2).
```

Therefore the complete atlas partition is

```text
96 exact direct-fan delete {0,2}
60 other merged-catalogue delete {0,2}
 4 exact bare delete 3
-----------------------------------------------
160 unconditional ancestor parents
```

By family:

```text
D : 32 direct
X5: 16 direct + 16 catalogue
X6: 16 direct + 16 catalogue
Y4: 16 direct + 12 catalogue + 4 bare
Y5: 16 direct + 16 catalogue
```

No C40 guard truth-cell count appears in this partition.

## 4. Full source-lineage theorem

Fix any atlas key `s`, its exact C37 patch `P_s`, controlled set `I={0,2,3,7}`, boundary `B_s=V(P_s)-I`, and an imported unconditional parent replacement `Q_s`.

A child is atlas-dominated only when it:

1. preserves every source arc of `P_s`;
2. preserves rotations and complete stars of `0,2,3,7`;
3. preserves the parent interface and deletion hole;
4. fixes only vertices, arcs, aliases, directions, degrees or guard outcomes in the arbitrary exterior already quantified by the parent rule;
5. does not identify distinct parent vertices or introduce a new adjacency to a controlled vertex.

Under these conditions write the child as `P_s union F`, where `F` is exterior to the saturated controlled patch. Replace `P_s` by `Q_s` and leave `F` unchanged.

For any valid complete colouring of the smaller whole graph, the parent certificate supplies a same-boundary valid colouring of `P_s` satisfying, in both colours,

```text
R_P^+ subseteq R_Q^+.
```

If lifting creates a monochromatic directed cycle crossing the interface, split it at successive boundary visits. Replace each positive `P_s` segment by the certified same-colour positive `Q_s` path and leave every exterior segment unchanged. The smaller colouring then contains a nonempty monochromatic closed directed walk and hence a directed cycle, contradiction.

Therefore every child satisfying the five lineage conditions is provisionally dominated by its C37 ancestor. This covers one-region and two-region alias families because C37/S06 quantify the entire retained boundary and arbitrary complementary exterior; the interface need not be one simple cycle.

If a child changes a source arc, controlled star, rotation, interface or parent alias, it is a new source state and the atlas gives no dominance claim.

## 5. Named repository lineage: exactly D/19

Logical exterior refinements are possible under every row, but the atlas assigns a current named C38/C39/C40 repository chain to exactly one source key:

```text
D/19.
```

Its C37 extra arcs are

```text
12->8, 7->12, 12->13, 13->7, 11->13.
```

Apply C38's label swap `12 <-> 13`. Together with the unchanged 18-arc core, the result is exactly C40 `BASE_ARCS`, whose five D-sector additions are

```text
13->8, 7->13, 13->12, 12->7, 11->12.
```

The checker compares the complete 23-arc sets, not only these five arcs.

C39 then completes boundary vertex 4 with rotation

```text
(0,5,q,r,8,3),
```

and C40 only adds/fixes data in that exterior sector and candidate reverse-guard outcomes. The C37 controlled stars remain unchanged. Hence a physical C40 reverse guard can invalidate a C40 shortcut but cannot invalidate the C37 ancestor rule.

No other one of the 159 parents is assigned a C38/C39/C40 named chain. The atlas nevertheless supplies its exact source ID and generic exterior-refinement dominance condition for future descendants.

## 6. No-overlap and mutation tests

The checker rejects:

1. a missing or duplicated family/word source key;
2. any mutation of the five-bit direction convention;
3. a wrong family alias `(x,y)`;
4. a direct-fan row whose physical reverse source arc is present;
5. any change to the four bare-delete rows;
6. a named C38/C39/C40 lineage on a row other than `D/19`;
7. a `D/19` label swap that fails exact C40 core equality;
8. any count other than `96 + 60 + 4 = 160`.

A semantic mutation is intentionally not hidden: if an independent consumer later refutes an imported parent profile rule, that row must be reactivated. This atlas certifies source identity and inheritance, not the producer table by itself.

## 7. Trust boundary and disposition

Repository-bound inputs are C37 source geometry, S06's 160-parent candidate and frozen postprocess digest, C39/C40 source definitions, C48 exact-parent precedence, and S10's clean-room receipt.

S10 imported no S06 producer checker, lift vector or helper, but it remains in the candidate-generation trust domain. No EvidenceLink, Result or root closure is created here.

Cycle 3 disposition:

```text
exact C37 source parents                   160
repository-bound atlas source keys         160
unconditional ancestor parents             160
delete {0,2} ancestors                     156
bare delete-3 ancestors                      4
named C38->C39->C40 rows                     1
C40 guard-child enumeration required         0
S09 missing-source blocker      closed at candidate level
best_verified_result                       none
root_closed                                false
```

Non-claims: no `d(7)>=7`; no other J orientation; no negative-face generation/unique mapper; no B-criticality; no termination theorem; no global `L_join`; no root closure.
