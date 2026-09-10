# R08 S01 Cycle 7 — typed acceptance bridge and refined JCLOSE-EC frontier

**Verdict:** `candidate_only`  
**best_verified_result:** `none`  
**root_closed:** `false`

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected-main cutoff at branch creation: `8541c137f7769ec29c1f6043f017b8cace9efc87`.

This is an S01 integration checkpoint. It changes only the candidate proof DAG and source/cut typing. It creates no EvidenceLink, Result, Solution, trusted-verifier receipt, or root closure.

## 1. Sole root DAG

Cycle 6 remains the governing root shape:

```text
minimum counterexample G
  -> Sigma_f mu(f) = -8
  -> actual unpaid negative triangle D0(f)
  -> nonempty LowCorners(f)
  -> JREL-SOUND + JREL-TOTAL
  -> JCLOSE-EC
  -> every actual D0 impossible
  -> contradiction with Sigma_f mu(f) = -8.
```

`JUNIQ` is optional. Exact-one `SCUT` is optional. Root soundness needs a total relation from actual negative-face data to closure-consumable actual source rows; it does not need a canonical corner, a canonical singleton gap, a unique join encoding, or a mutually exclusive closure label.

No finite atlas count is an occurrence theorem. In particular C35 finite canaries, C37 R160, S12-A obligation counts, or any finite source catalogue do not produce a `D0 -> source` existential.

## 2. Exact acceptance type transition

Cycle 7 makes the source boundary explicit as a three-stage typed transition.

### Type P — `PHYSICAL_GEOMETRY`

A record `P` is physical-geometry certified when it freezes a concrete plane-orientation patch:

```text
physical_graph_key,
physical vertex and arc identities,
rotation at every controlled vertex,
actual face list / holes,
alias partition normalized before geometry,
complete controlled stars,
all patch-to-exterior contacts,
edge/face ownership,
source/payer keys,
one or more root-description/provenance labels.
```

`PHYSICAL_GEOMETRY` means the picture is a genuine embedded configuration in the graph named by `physical_graph_key`. It does **not** say that graph is the assumed minimum counterexample, that the named face is the current `D0`, or that the record occurs in the root proof.

### Type J — `SAME_MINCE_JREL_JOIN`

Fix the assumed vertex-minimum counterexample `G`, an actual `D0(f)`, and `p in LowCorners(f)`. A physical record `P` is accepted to Type J only when all of the following are bound:

```text
P.physical_graph_key = G,
P.root_face_id = f,
D0_G(f),
Low_G(f,p),
every P vertex/arc/face is the actual object of G,
the alias quotient is the actual quotient in G,
complete-star declarations are actual in G,
all exterior contacts and owned boundary edges are complete,
source/payer ownership agrees with the charge ledger of G,
the exact source-row key is fixed,
every root/gap description used by the row points back to the same actual f.
```

Call the resulting record `JREL(G,f,p,j)`.

This is the first type that can discharge root occurrence.

### Type C — `CLOSURE_CONSUMABLE_CERTIFICATE`

A Type-J record becomes closure-consumable only after an exact finite or symbolic colouring-obligation universe `Omega(j)` is bound to it. A Type-C record must contain:

```text
the exact source-row identity from j,
the exact complete-colouring quantifier and nonvacuity convention,
an exhaustive partition of Omega(j),
per-obligation witnesses/metadata needed by its closure label,
the identity and semantics of every predicate used by those labels,
all geometry/ownership/guard/descent data required by the closure theorem,
the applicable lifting interface and positive-reachability contract.
```

A label name or integer bucket count is not enough. If a predicate used by the label has no exact statement, the transition `J -> C` is blocked for that bucket.

Finally,

```text
JCLOSE-EC(j)
```

means every obligation in `Omega(j)` has an actual source-valid discharge through `STRUCT`, `L_A`, `L_B`, or an explicit useful `ESC`, with the required lifting/ownership conditions.

Hence the exact acceptance chain is

```text
PHYSICAL_GEOMETRY
  -- SAME_MINCE_BIND -->
SAME_MINCE_JREL_JOIN
  -- ROW_PREDICATE + EXHAUSTIVE_OMEGA_BIND -->
CLOSURE_CONSUMABLE_CERTIFICATE
  -- ALL OBLIGATIONS DISCHARGED -->
JCLOSE-EC.
```

No arrow may be skipped.

## 3. S13-B Cycle 4 — alias/overlap JREL-SOUND schema

Cycle-7 orchestration identifies S13-B Cycle 4 as the identity-bound specialist source for the alias/overlap `JREL-SOUND` schema and its D/3 multi-root control. S01 consumes only the stated typed consequences and does not manufacture a repository SHA for source bytes not independently exposed at the fresh protected-main cutoff.

The schema upgrades `JREL-SOUND` at the **type/checking** level:

1. aliases are normalized before any geometry comparison;
2. different provenance roots may map to the same physical source key;
3. overlapping source records are allowed only when every shared physical vertex, arc, face, contact, and ownership datum agrees;
4. overlap never licenses double spending of a payer/source object;
5. duplicate provenance descriptions do not require duplicate closure work once the same physical closure certificate applies;
6. none of this supplies a same-MinCE occurrence existential.

The D/3 multi-root control is therefore interpreted as

```text
one physical embedded source
  <- several admissible root/provenance descriptions.
```

This is positive evidence for using a **relation** rather than a unique map. It is not `JUNIQ`, and it is not `JREL-TOTAL`.

`JUNIQ` remains optional.

## 4. S13-D Cycle 7 correction — C35 canaries stop at Type P

Cycle-7 orchestration identifies the corrected status of the C35 canaries as exactly

```text
actual_c35_face_geometry_certified_unjoined.
```

This is a type correction.

The word `actual` means that the displayed C35 face/patch is physically realized in the concrete C35 control graph. It does **not** mean the face is the actual `D0` of the assumed minimum counterexample.

Thus the correct acceptance status is

```text
C35 canary
  -> PHYSICAL_GEOMETRY: YES
  -> SAME_MINCE_JREL_JOIN: NO / UNBOUND
  -> root occurrence: NO.
```

Any local colouring/reduction certificate attached to the canary remains useful as a row library after a future same-MinCE bind, but it cannot create that bind.

The same discipline applies to the D/3 multi-root control: it is a physically instantiated control source, not a root actual join.

## 5. S09 Cycle 5 — merged narrow selected-J classifier

Protected main already contains merged S09 Cycle 5. Its input contract starts **after** a Type-J selected C35/C36 occurrence already exists.

For such an actual selected-J join:

```text
d(7) >= 6.
```

Then exactly one degree predicate holds:

```text
d(7)=6
  -> actual rotation/alias data determine an exact C37 family/word identity
  -> only then may R160 be applied
  -> candidate equality branch is killed through L_A/lifting;

d(7)>=7
  -> exact-source class J_HIGHPORT
  -> ESC/TPROG remains open.
```

This is a post-join class/closure bridge. It does not prove `JREL-TOTAL`, and it never inverts C37 R160 into source occurrence.

For a single row, selected-J `d(7)=6` is therefore the shortest currently known local route from a Type-J record to a reduction certificate.

## 6. S12-A Cycle 7 — refined 784-obligation closure frontier

The inherited S12-A universe has 784 exact complete-colouring obligations:

```text
206 ALL_EXTEND
578 blocker-side obligations.
```

Cycle 7 refines the 578 blocker frontier exactly as

| blocker label | count |
|---|---:|
| `STRUCT_SEPARATOR` | 216 |
| `PROFILE_CRITICAL` | 82 |
| `FLIP_STAR_PROFILE_MISSING_A` | 40 |
| `FLIP_STAR_PROFILE_MISSING_B` | 240 |
| `SURVIVOR` | 0 |
| `TOPOLOGY_CLOSURE` | 0 |
| **total** | **578** |

The two flip-star-profile missing classes total 280, but their 40/240 source identities remain separate.

The zero counts mean only that no S12-A Cycle-7 blocker obligation is assigned to the `SURVIVOR` or `TOPOLOGY_CLOSURE` buckets. They do **not** imply that the 578 blockers are all closed.

These 784 obligations become root-relevant only after the corresponding source row has crossed Type P -> Type J. The counts cannot supply that occurrence transition.

### Closure interpretation

- `206 ALL_EXTEND`: candidate `L_A` lane after exact row binding; still requires `LIFT-BIND`, positive `R+`, and eventual `LIFT-VERIFY`.
- `216 STRUCT_SEPARATOR`: source-bound structural frontier. The row may enter `STRUCT` only when the same-MinCE separator geometry/ownership hypotheses of the structural theorem are attached to the Type-J record.
- `82 PROFILE_CRITICAL`: classification is retained, but closure acceptance is blocked until the exact critical predicate and theorem interface are bound.
- `40 + 240 FLIP_STAR_PROFILE_MISSING`: not closure-consumable yet; the required flip-star-profile predicate/witness theorem is missing.
- no additional survivor/topology bucket remains.

Thus S12-A Cycle 7 substantially narrows `JCLOSE-EC`, but does not close it.

## 7. S13-A Cycle 9 — missing Bcrit predicate is a block, not a failure

The Cycle-7 orchestration reports that S13-A Cycle 9 lacks the exact Bcrit predicate needed to consume the critical frontier.

Disposition:

```text
BCRIT_PREDICATE_BIND = BLOCK(predicate_absent)
```

not

```text
BCRIT theorem = false.
```

Consequences:

1. the 82 `PROFILE_CRITICAL` obligations cannot yet pass the `J -> C` acceptance boundary as B-critical closure certificates;
2. no Bcrit row is declared false;
3. no S12-A count is changed;
4. a future exact predicate must specify all source-owned geometry, path/topology conditions, payer/source identity, and colour quantifiers before a criticality lemma can be applied.

## 8. S11 Cycle 8 — missing Lean 4.28 kernel receipt is a block, not a failure

Fresh repository state still has draft PR #83 with raw Lean source, but no executed Lean 4.28 kernel receipt. The visible source transport itself explicitly lacks kernel execution.

Therefore:

```text
LIFT_O_THEOREM_CONTENT = PASS(candidate theorem content)
LIFT_BIND             = row-specific OPEN/PARTIAL
LIFT_VERIFY           = BLOCK(Lean-4.28-kernel-receipt-absent)
```

This is not a mathematical failure of the lifting theorem.

GitHub transport, static no-`sorry` scans, candidate CI, or source presence cannot substitute for a real pinned kernel replay plus axiom/statement-faithfulness/trusted admission.

## 9. Row-level dependency/cut matrix

| row / family | physical geometry | same-MinCE JREL | closure-consumable status | first cut |
|---|---|---|---|---|
| C48 low-corner descriptions | arithmetic/local cover only | no | no | physical source extraction + same-MinCE bind |
| S13-B D/3 multi-root control | certified physical control | no | local schema/control only | actual `D0` same-MinCE bind |
| S13-D C35 canaries | `actual_c35_face_geometry_certified_unjoined` | **no** | local row certificates remain conditional | **same-MinCE JREL join** |
| selected-J input | conditional physical source row | required | only after join | root-wide selected-J occurrence/JREL |
| selected-J `d6` | yes once joined | yes conditionally | exact C37 identity -> R160 -> `L_A` | row lifting/admission |
| selected-J `J_HIGHPORT` | yes once joined | yes conditionally | exact escape class only | TPROG/useful terminal theorem |
| S12-A 206 `ALL_EXTEND` | source-row dependent | required | `L_A` after row bind | same-MinCE join, then lifting |
| S12-A 216 `STRUCT_SEPARATOR` | source-row dependent | required | structural label bound | same-MinCE separator theorem premises |
| S12-A 82 `PROFILE_CRITICAL` | source-row dependent | required | **blocked before Type C** | S13-A exact Bcrit predicate |
| S12-A 40 flip-star-profile | source-row dependent | required | **blocked before Type C** | flip-star-profile predicate/theorem |
| S12-A 240 flip-star-profile | source-row dependent | required | **blocked before Type C** | flip-star-profile predicate/theorem |
| S12-A survivor/topology | zero rows | n/a | n/a | no residual rows in these buckets |
| generic lifting | n/a | row-specific | theorem content candidate-PASS | S11 kernel receipt for trusted admission |
| final charge | actual `D0` exists from ledger | needs root-wide totality | needs all joined rows closed | `JREL-TOTAL + JCLOSE-EC` |

The matrix distinguishes individually certified physical controls from actual-root joins. Neither the D/3 multi-root control nor the C35 canaries count as a root join.

## 10. First missing actual row

After all Cycle-7 deltas, the first missing actual row is still **before** the S12-A 578 frontier.

It is a Type-J record of the form

```text
J0 = (
  G = the assumed vertex-minimum counterexample,
  f = an actual D0 face of G,
  p in LowCorners(f),
  exact physical source key after alias normalization,
  exact source-row ID,
  complete stars/contacts/ownership,
  payer/source identity,
  same-face provenance
)
```

such that

```text
JREL(G,f,p,J0).
```

Equivalently: the missing row is the first **physical-geometry -> same-MinCE** acceptance witness.

C35 canaries stop immediately before this row. D/3 multi-root controls stop immediately before this row. S12-A counts start logically after this row. S09 Cycle 5 also starts after this row for the selected-J family.

Therefore the earliest root bottleneck remains `JREL-TOTAL`, not a colouring count.

## 11. Shortest current route to `JCLOSE-EC`

There are two useful notions of shortest route.

### Per-row shortest route

If a future actual Type-J row is selected-J with `d(7)=6`:

```text
actual JREL selected-J
 -> S09 C5 exact C37 family/word
 -> R160 strict reduction
 -> LIFT-BIND
 -> LIFT-O theorem content
 -> LIFT-VERIFY
 -> row closed.
```

That is the shortest known individual-row route.

### Shortest route to a finite exhaustive `JCLOSE-EC` theorem

The shortest currently visible root-useful strategy is to prove a `JREL-TOTAL` theorem whose codomain is contained in the S12-A 784-obligation source universe. Then no `J_HIGHPORT` branch has to be solved merely because selected-J was chosen.

After that same-MinCE totality theorem, the remaining finite closure work is concentrated in:

```text
206 ALL_EXTEND
  -> L_A + lifting;

216 STRUCT_SEPARATOR
  -> same-MinCE separator closure;

82 PROFILE_CRITICAL
  -> bind exact Bcrit predicate
  -> profile-critical closure;

40 + 240 FLIP_STAR_PROFILE_MISSING
  -> one source-faithful flip-star-profile theorem if one common statement
     really covers both named classes, otherwise two explicit specializations.
```

There are no `SURVIVOR` or `TOPOLOGY_CLOSURE` rows left to chase.

So the shortest visible proof program is:

```text
(A) SAME-MINCE JREL-TOTAL into the S12-A source universe;
(B) separator closure for the 216;
(C) exact Bcrit predicate + critical closure for the 82;
(D) flip-star-profile closure for the 40 and 240;
(E) LIFT-BIND on reduction/all-extend rows;
(F) real Lean 4.28 LIFT-VERIFY receipt for trusted admission;
(G) conclude JCLOSE-EC for every actual join.
```

If step (A) cannot force the S12-A universe, then the selected-J `J_HIGHPORT` escape remains an additional branch and `TPROG` must also be solved.

## 12. Final charge contradiction remains unchanged

No new charge transfer is introduced.

The candidate discharging argument remains:

```text
Sigma_f mu(f) = -8
 -> some actual D0(f)
 -> LowCorners(f) nonempty
 -> JREL-TOTAL gives at least one required same-MinCE join
 -> JCLOSE-EC makes every such actual D0 impossible
 -> contradiction.
```

No local reduction is represented as numerically adding charge to the original graph. Payer/source ownership remains attached to the same actual minimum-counterexample object throughout.

## 13. Source/admission discipline

At this fresh cutoff:

- S09 Cycle 5 is protected-main repository-bound and consumed in its narrow post-join scope.
- S13-B Cycle 4, S12-A Cycle 7, S13-D Cycle 7, and S13-A Cycle 9 are consumed only under the exact named specialist-cycle identities and typed conclusions supplied to this Cycle-7 integration; S01 does not invent missing repository digests or row IDs.
- S11's visible repository transport remains draft and lacks a Lean 4.28 kernel receipt.
- no atlas size, finite colouring count, multi-root control, or geometry canary is interpreted as source occurrence.
- no candidate is promoted to Evidence.

`candidate_only`; `best_verified_result=none`; `root_closed=false`.
