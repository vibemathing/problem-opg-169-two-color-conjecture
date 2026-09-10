# S10 Cycle 3 — exact S11 Cycle-4 source gate and S04 two-hole ownership correction

Verdict: `candidate_only`. `root_closed=false`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected source base: `a2a9973d2f995de71095a6bea814cbe882cb7718`.

This is an S10 consumer audit. It distinguishes an identity-bound specialist
artifact from theorem/ownership content already present in repository-bound
sources. Missing specialist identity is never converted into PASS by matching
mission wording.

## 1. Fresh identity binding

At the source base above, exact repository searches find no S11 Cycle-4
branch, pull request, commit, candidate artifact, packet, or Issue-bound source
locator. The only `s11` branches are the already merged S10 Cycle-2 consumer
and its mechanical synchronization branch. The repository's Cycle-4 branches
are S01, S08 and S09 lanes, not S11. Commit search for `S11` returns only the
S10 Cycle-2 consumer commit. S01 Cycle 4 explicitly states that its imported
LIFT-O bridge has no repository-bound S11 identity.

The same fresh search finds no S04 branch, pull request, commit, packet or
candidate artifact. Therefore the requested specialist identities remain
source-gated:

```text
S11_CYCLE4_ARTIFACT_BINDING = NOT_VERIFIABLE_MISSING_SOURCE
S11_CYCLE4_IDENTITY_CONSUMPTION = BLOCKED_BY_SOURCE_GATE
S04_ARTIFACT_BINDING = NOT_VERIFIABLE_MISSING_SOURCE
```

This does not withdraw S10 Cycle 2's theorem-content result. The generic
ordinary arbitrary-exterior lifting implication remains
`PASS(candidate, repository-derived)` from its already bound source chain.
There is no identity-bound upgrade to an S11 Cycle-4 theorem in this cycle.

## 2. Exact repository source for the S04 ownership correction

Although no S04-labelled artifact is repository-bound, the requested ownership
correction is derivable exactly from merged C43 and C47 source objects.

C43 freezes the actual fan-centre deletion holes

```text
H13 = (7,8,16,12)
H14 = (8,15,12,17)
```

so

```text
V(H13) ∩ V(H14) = {8,12}
E(H13) ∩ E(H14) = empty.
```

The fixed guard arc is `8->12`. It is embedded outside both deletion-hole
interiors. Neither incident face of edge `8-12` belongs to the frozen 22-face
complex; those two faces require separate absorption data.

This is not the same as C43's two 22-face-complex boundary walks

```text
A = (5,6,11,12)
B = (12,16,8,17),
```

which meet only at `12`. Those walks are not the deletion holes. Hence the
obsolete inference "the two fan regions meet only at 12" is source-invalid.

C47 independently freezes the same correction and makes edge ownership
explicit: its two-hole patch has retained boundary

```text
B47 = (7,8,16,12,15,17),
```

the two hole closures meet in terminals `{8,12}`, the guard `8->12` stays in
the exterior, every replacement edge belongs to its owning disk, and no
cross-hole shortcut is admitted.

Thus the correct inter-lobe separator is

```text
T = {8,12}
```

as a **vertex separator only**. It is not a shared-edge interface.

## 3. Ownership-normalized factorization contract

Let `L13` be a source-faithful piece drawn in the `H13` disk, `L14` a
source-faithful piece drawn in the `H14` disk, and `F` the remainder of the
graph under the unabsorbed C43/C47 decomposition. The source-faithful default
ownership is:

```text
V(L13) ∩ V(L14) = {8,12};
E(L13) ∩ E(L14) = empty;

8->12 ∈ E(F);
8->12 ∉ E(L13);
8->12 ∉ E(L14);

every new/replacement edge of L13 lies in the H13 disk;
every new/replacement edge of L14 lies in the H14 disk;
no L13-interior -- L14-interior cross edge is silently permitted.
```

Any larger global patch must additionally freeze its actual outer boundary;
`T={8,12}` is the inter-lobe separator, not automatically the full
patch/exterior boundary. In C47 the full retained boundary is `B47`, not just
`T`.

If either guard-edge incident face is absorbed, ownership changes. The new
patch must explicitly import the absorbed face edges/third vertex, recompute
the actual boundary, aliases and all exterior contacts, and then re-run the
lifting hypotheses. One may not simultaneously say "`8->12` is exterior" and
use it as a patch-owned edge after guard-face absorption.

## 4. Consequence for LIFT-O

S10 Cycle 2's Replacement Lifting Lemma remains sound under this correction.
The lemma is topology-agnostic but ownership-sensitive: each invocation must
use the actual common boundary and the actual P/Q/F arc partition.

For a two-lobe decomposition, C13's multi-piece form applies by taking the
positive transitive closure of the union of the same-colour positive
reachability relations of all pieces. Paths and cycles may alternate between
the two lobes through both terminals. Therefore independent one-terminal
profiles are insufficient.

In particular, the complete-tournament shortcut from S10 Cycle 2 is **not**
available for the two deletion-hole lobes merely because the whole graph has
the edge `8->12`. A two-vertex tournament would require that arc to be the
same common interface arc in the compared patch pieces. Here C43/C47 place it
in the exterior, outside both hole interiors. Artificially adding it to a
lobe would change that lobe's validity and reachability profile.

For same-coloured terminals the exterior guard itself contributes the positive
relation `8 -> 12`. Consequently a lobe relation `12 -> 8` can close a
monochromatic directed cycle with the exterior guard. This is exactly the
kind of return information lost by ordinary same-boundary extension or a
one-terminal factorization.

A sound factorization must therefore preserve, for both colours, the complete
positive terminal relation on `T` (and the complete positive relation on the
full outer boundary when used as a replacement certificate). Zero-length
paths remain excluded.

## 5. What the correction does and does not change

The correction confirms these candidate-level statements:

```text
S04_TWO_HOLE_OWNERSHIP_CONTENT = PASS(repository-derived candidate)
TWO_TERMINAL_SEPARATOR = {8,12}
TWO_TERMINAL_SHARED_EDGE_SET = empty
GUARD_8_TO_12_OWNER = exterior under the unabsorbed C43/C47 decomposition
ONE_TERMINAL_MEET_ONLY_AT_12 = FAIL(source-faithfulness)
ORDINARY_TWO_TERMINAL_SHORTCUT = FAIL
RPLUS_MULTI_PIECE_COMPOSITION = PASS(candidate theorem-content)
```

It does **not** make C47's 8,136 failures universal. C47 covers only deletion
`{13,14}` with at most one new nonisolated internal point total, simple
oriented edges drawn in their owning disks, and the exterior guard retained.
Absorbed guard faces, larger interfaces, additional controlled stars, two new
internal points, cross-region source changes, or a global criticality proof
are outside that failed class.

It also does not promote an S04-labelled theorem by identity. The content is
bound to C43/C47; `S04_ARTIFACT_BINDING` remains missing until an exact S04
source locator exists.

## 6. Exact compatibility checks against the Cycle-2 S10 contract

The Cycle-2 ownership checklist survives with the following specialization.

1. **Alias normalization before geometry:** PASS for the frozen C43/C47
   vertices; any absorbed guard-face aliases require a new instance.
2. **Actual boundary:** PASS only when the caller distinguishes the inter-lobe
   terminal set `T` from the global replacement boundary.
3. **All exterior contacts:** the guard arc `8->12` is an explicit exterior
   contact/edge; it cannot disappear from `F`.
4. **Shared arcs:** the two lobes share no edge. The guard is not a shared lobe
   edge.
5. **No hidden cross-contact:** C47's catalogue enforces owning-disk edges and
   forbids cross-hole shortcuts. A larger theorem must source-bind any new
   contact.
6. **Complete-Q and same-boundary lift:** unchanged.
7. **Both-colour positive R+ inclusion:** unchanged and essential.
8. **Class preservation / reverse guards / planarity / strict descent:**
   separately row-bound, unchanged.
9. **Tournament specialization:** inapplicable to the unabsorbed two-lobe
   factorization.
10. **Pinched/multi-region topology:** not an obstruction to LIFT-O once
    ownership and the full relation are correct.

No Cycle-2 PASS is weakened by the C43/C47 correction; rather, the correction
prevents a false theorem invocation with the wrong piece intersection.

## 7. Admission rule for a future S11 Cycle-4 source

When an actual S11 Cycle-4 artifact appears, S10 should bind it by exact
repository path, revision/blob, packet and PR/commit identity and compare it
against this frozen contract. It may receive identity-bound PASS only if it
states or implies all of:

```text
actual alias quotient before geometry
actual common boundary after aliases
complete P/Q/exterior vertex and arc ownership
shared-arc direction agreement
no hidden internal-to-exterior contact
positive-length R+
every complete valid Q colouring
same-boundary valid P lift
both-colour R_P^+ subseteq R_Q^+
multi-piece/repeated-boundary-visit soundness
separate class-preservation and strict-descent premises
```

For the corrected two-hole source it must additionally respect:

```text
H13=(7,8,16,12)
H14=(8,15,12,17)
vertex intersection {8,12}
edge intersection empty
8->12 exterior unless guard faces are explicitly absorbed
no reuse of the 22-face boundary-walk intersection {12} as hole geometry
```

Any mismatch yields a precise `FAIL` or `UNKNOWN`; matching prose without
source identity is not enough.

## 8. Consumer disposition

```text
S11_CYCLE4_ARTIFACT_BINDING: NOT_VERIFIABLE_MISSING_SOURCE
S11_CYCLE4_IDENTITY_CONSUMPTION: BLOCKED_BY_SOURCE_GATE
LIFT_O_THEOREM_CONTENT: PASS(candidate, unchanged)
S04_ARTIFACT_BINDING: NOT_VERIFIABLE_MISSING_SOURCE
S04_TWO_HOLE_OWNERSHIP_CONTENT: PASS(candidate, repository-derived C43/C47)
S04_ONE_TERMINAL_GEOMETRY: RETIRED/FAIL(source-faithfulness)
C47_BOUNDED_NEGATIVE_SCOPE: unchanged
TRUSTED_VERIFIER_RECEIPT: absent
EvidenceLink: absent
Result: absent
root_closed: false
```

No GSRC, JMAP, `L_join`, B-criticality, global termination, anchored-to-ordinary
conversion, EvidenceLink, Result, Solution or root closure follows.
