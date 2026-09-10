# R08 S09 Cycle 5 — narrow provenance-preserving GSRC source-or-escape lemma

`verdict=candidate_only`; `root_closed=false`; `best_verified_result=none`.

Fresh protected `main` consumed at construction:

```text
61aa9f65e0be9b00205ed0e57c7c9a5c5917f96c
```

This cycle proves only a **selected-J source classification theorem**.  Its input
is already an **actual, source-bound selected C35/C36 J occurrence** carrying
its `(f,p[,g])` provenance, actual embedding, ownership and payer/source data.
It does not generate such an occurrence from `D0`, does not infer occurrence
from `R160`, and does not claim `G-TOTAL` for arbitrary `Desc48` descriptions.

## 1. Frozen source identities

Repository-bound inputs:

```text
C35 input blob                  8f678efbb6d5d7c28464a5fa6bfa18f25d33ddbc
C36 input blob                  3538262e9b8a1fcd454091861ab55f39cdc09ce7
C36 incoming proof blob         1aa0158d67c1beafc04a9442792e034c72e73dc1
C37 input blob                  a452f67995e1b563e364382593b887bf0ec1f63d
C37 proof blob                  4aae213b6ad489880eca79f0f9b59cd81d8ea26f
S09 Cycle-3 atlas blob          05e6b31700d9c570927b8d96e76750feb32ee885
S09 Cycle-3 lineage proof blob  2d31a464630482ea3bf145495bfd497eb19d97f2
```

The selected J face is normalized as

```text
J=(0,2,3), with 0->2, 2->3, 3->0.
```

The fixed 18 directed core arcs are

```text
0->2, 0->4,
2->3, 2->6, 2->11,
3->0, 3->4, 3->7,
4->5, 4->8,
5->0, 5->6,
6->0,
7->2, 7->8,
8->3,
11->6, 11->7.
```

The ten fixed source faces are

```text
(0,2,3), (0,6,2), (0,5,6), (0,4,5), (0,3,4),
(2,7,3), (2,11,7), (2,6,11), (3,8,4), (3,7,8).
```

The complete controlled rotations inherited from the selected-J source are

```text
rot(0) = (2,6,5,4,3)
rot(2) = (0,3,7,11,6)
rot(3) = (0,4,8,7,2).
```

At vertex `7`, the selected-J anchor order is

```text
(2,3,8, W, 11)
```

where `W` is the ordered list of actual additional neighbours in the wedge from
`8` to `11`.  Source binding means the full actual star of `7`, including `W`,
is frozen before classification.

For minimum-counterexample use, the preserved C36 dependencies give

```text
d(7) >= 6.
```

This lower bound is imported; Cycle 5 does not rerun its earlier degree-four,
outgoing-d5 or old-port subproofs.

## 2. The narrow source-or-escape lemma

### Lemma GSRC-J-COVER

Let `S` be an actual source-bound selected C35/C36 J occurrence in the
triangulated source setting, with:

1. exact actual rotation/embedding;
2. complete stars of controlled vertices `0,2,3,7`;
3. explicit alias roles and actual vertex equalities;
4. provenance `(f,p[,g])`;
5. original DC2 payer/source keys;
6. a disjoint source/exterior ownership partition.

Assume the C36 minimum-counterexample lower bound `d(7)>=6`.

Then exactly one of the following holds.

```text
C37:
    d(7)=6,
    S has a unique exact C37 family in {D,X5,X6,Y4,Y5},
    a unique five-bit direction word w in {0,...,31},
    and therefore a unique exact parent identity family/w in R160;

J_HIGHPORT:
    d(7)>=7,
    S is recorded with its exact full star of 7, ordered wedge sequence,
    actual wedge faces, alias signature and direction signature.
```

The two outputs are disjoint by degree.  The theorem is classification of an
already actual source; neither branch is created by a reduction theorem.

### Proof: the degree cut

The imported lower bound gives `d(7)>=6`.

If `d(7)=6`, the fixed four anchor neighbours `2,3,8,11` leave exactly two
additional entries in the actual simple star.  Call them `x,y` in the actual
rotation order

```text
rot(7) = (2,3,8,x,y,11)
```

up to cyclic shift.  Triangulation gives the actual source faces

```text
(8,7,x), (x,7,y), (7,11,y).
```

If `d(7)>=7`, there are at least three wedge entries, so the source is not an
exact C37 degree-six parent.  Record the exact ordered wedge and all its source
data as `J_HIGHPORT`.  This class is explicit and disjoint from C37 without any
termination or reducibility claim.

It remains to prove the degree-six identification.

## 3. Degree six: alias quotient is exact

Because the star is simple, `x` and `y` are distinct and neither is
`2,3,7,8,11`.  Neither can be `0`, because `0` already has its complete
degree-five star.  Therefore an additional neighbour is either old port
`4,5,6` or genuinely new.

The ordered alias quotient has exactly thirteen possibilities:

| role pair `(x,y)` | normalized type | disposition |
|---|---|---|
| new,new | D | survive |
| 4,new | X4 | impossible: `x=4` closes the actual degree-three link of 8 |
| 5,new | X5 | survive |
| 6,new | X6 | survive |
| new,4 | Y4 | survive |
| new,5 | Y5 | survive |
| new,6 | Y6 | impossible: `y=6` closes the actual degree-three link of 11 |
| 4,5 | O45 | impossible by the `x=4` link obstruction |
| 4,6 | O46 | impossible by both link obstructions |
| 5,4 | O54 | incompatible successor requirements at 5 |
| 5,6 | O56 | impossible by the `y=6` link obstruction |
| 6,4 | O64 | 9 vertices and 23 edges, contradicting `e<=3v-6` |
| 6,5 | O65 | incompatible successor requirements at 6 |

Thus the only actual degree-six source geometries are exactly

```text
D=(12,13)
X5=(5,13)
X6=(6,13)
Y4=(12,4)
Y5=(12,5).
```

Here `12,13` are canonical role names assigned in wedge order to genuinely new
vertices.  Alias normalization does **not** quotient the graph or identify two
distinct actual vertices; it only maps role symbols to already equal actual
vertices.  Hence rotations, payer/source keys and ownership do not change.

The exact underlying patch rotations stored by the Cycle-5 row schema are
reconstructed from the thirteen stipulated source triangles using the same
rotation convention as C37.  In every surviving family

```text
d(0)=d(2)=d(3)=5, d(7)=6
```

and all four controlled stars are complete.

## 4. Degree six: unique word and parent identity

For a surviving alias family `(x,y)`, the five additional physical edges are

```text
(8,x), (x,7), (x,y), (y,7), (y,11).
```

The actual orientation chooses exactly one direction on each edge.  Define
bit `i=1` when the actual direction reverses the listed role edge and `0`
otherwise.  The five bits determine a unique word `w in {0,...,31}`.

Therefore the pair

```text
(family, word)
```

is uniquely determined by the already actual source geometry and directions.
Its exact parent identity is

```text
parent_id = family + "/" + decimal(word).
```

No reduction result is used in this identification.  The Cycle-3 expanded
parent-ID digest remains

```text
cb8b4171491572de52a1ca5f3ebe1235e6091dd7298c5b380f0477d0c9789b74.
```

This proves the `d(7)=6 -> exact C37 parent` half of GSRC-J-COVER.

## 5. Ownership and payer/source preservation

The source record owns exactly the edges and faces used to certify the selected
J occurrence.  Every other arc/contact is exterior-owned.

At degree six, family extraction may change which boundary-role edges are
source-owned.  For example, in `X5` the physical edge `8-5` is a source edge
because it lies on `(8,7,5)`; in `D` the same possible boundary chord is
exterior unless separately present.  Ownership is therefore recomputed from
the actual source triangles, not inherited from a stale C36 boundary picture.

Alias normalization preserves ownership because it is only a role-name
normalization of the existing actual graph.  It creates no edge, deletes no
edge and merges no distinct vertices.

The original DC2 payment ledger is likewise carried unchanged.  Classification
does not create a donor, mark, unit payment or positive-face credit.  A row must
carry:

```text
source face identity,
witness p and optional gap g,
actual marked pairs,
payer IDs,
face h values,
and a no-double-spending key.
```

If the actual source has no marked pair, the exact payer set is empty; `null`
is data, not a missing payer.

## 6. After identity only: the C37 degree split

Now suppose the source occurs in a vertex-minimum counterexample.

For the C37 branch, exact occurrence has already been established by the
preceding geometry/identity proof.  Only now may the imported R160 reduction
library be applied:

```text
d(7)=6
    -> exact family/word parent in R160
    -> imported strict all-exterior parent reduction
    -> contradiction to vertex-minimality.
```

This is use of reduction **after occurrence**, not occurrence manufactured from
coverage.

Hence, inside the already selected-J minimum-counterexample source,

```text
d(7)>=7.
```

The surviving branch is the explicit `J_HIGHPORT` source class.  Cycle 5 does
not claim it is reducible, finite-state, terminating, or covered by the
S02-B stress families.

## 7. Fully instantiated actual source record: D/3

The repository C37 whole-graph witness supplies an actual eleven-vertex plane
triangulation.  Cycle 5 binds it to the actual source face

```text
f=(0,2,3), p=0.
```

At `p=0`,

```text
d=5, t=0, s=d-3t=5,
```

so this is an `F48` witness.  On `f`, all three corners have `gamma=1/5`,
`h(f)=0`, and

```text
mu(f)=-1+3/5=-2/5.
```

There are no marked pairs in the whole witness, so

```text
payer_ids = []
```

is the exact payer record.

The selected degree-six wedge is

```text
x=12, y=13,
rot(7)=(2,3,8,12,13,11).
```

The five actual extra arcs are

```text
12->8, 7->12, 12->13, 13->7, 13->11.
```

Relative to the C37 role order, bits 0 and 1 are reversed and the remaining
three are not, so

```text
word = 3,
family = D,
parent_id = D/3.
```

The complete actual rotation is

```text
0 : (2,6,5,4,3)
2 : (0,3,7,11,6)
3 : (0,4,8,7,2)
4 : (0,5,8,3)
5 : (0,6,13,12,8,4)
6 : (0,2,11,13,5)
7 : (2,3,8,12,13,11)
8 : (3,4,5,12,7)
11: (2,7,13,6)
12: (5,13,7,8)
13: (5,6,11,7,12).
```

The source owns the 18 core arcs plus the five C37 extra arcs, for 23
source-owned arcs.  The remaining four actual arcs

```text
8->5, 5->12, 6->13, 5->13
```

are exterior-owned.  The partition is disjoint and exhaustive.

For `D/3`, the Cycle-3 atlas class is the direct-fan ancestor:

```text
delete {0,2},
add 5->7, 6->7, 7->4,
actual hole (3,4,5,6,11,7).
```

That rule is recorded only after the exact `D/3` source identity.

The full machine-readable record is

```text
research/artifacts/candidates/opg169-a01-s09-cycle5-gsrc-source-record-D3.json
```

## 8. Source-or-escape row schema

Every row has the top-level form

```text
occurrence_id
provenance
selected_J
actual_embedding
ownership
payments
classification
```

For a C37 row, `classification` must include

```text
degree7=6
ordered wedge [x,y]
alias signature
family
five-bit word
parent_id
exact family-template rotation match.
```

For a `J_HIGHPORT` row it must include

```text
degree7>=7
complete actual star of 7
ordered wedge neighbours
actual wedge faces
alias signature
direction signature
escape_key.
```

The source schema freezes all five C37 family rotations and all thirteen alias
cells.  The high-port class is intentionally open-ended in size but exact in
source data; its disjointness from C37 is the degree predicate.

## 9. Mutation tests

Cycle 5 rejects:

1. `D0 -> R160`;
2. using R160 coverage to infer an occurrence;
3. dropping `(f,p[,g])` after source binding;
4. treating role alias normalization as a graph quotient;
5. using a stale boundary ownership partition after an alias makes a boundary
   role edge part of a source face;
6. omitting any controlled complete star;
7. inferring a C37 family without actual rotation/faces;
8. inferring a word without all five actual edge directions;
9. identifying `d(7)>=7` with a C37 parent;
10. turning `J_HIGHPORT` into a reduction/termination claim;
11. inventing payer data or silently double spending;
12. any descendant census.

## 10. Reproduction and digests

Files:

```text
research/artifacts/candidates/opg169-a01-s09-cycle5-gsrc-source-or-escape-schema.json
research/artifacts/candidates/opg169-a01-s09-cycle5-gsrc-source-record-D3.json
research/artifacts/candidates/opg169-a01-s09-cycle5-gsrc-source-or-escape-check.py
research/artifacts/candidates/opg169-a01-s09-cycle5-gsrc-source-or-escape-output.json
```

Frozen SHA-256:

```text
schema   39dbe5fd5157346d9e9a6b530f88dda36d15d383813a12be5b66f88b92e7f46d
record   85402f19ce74a61231b432d2eb37cb821dfbef9e5d7e0561ba404358d3e87552
checker  0374baf1a904376acd0305cdcf855084b8e485719d72c2db7d6c1a256a52cf71
output   8dcbe0df2fe7a5368854ac68800935a8e6a3e9b9e52f3e5a697a4f149547f80a
```

Run:

```bash
python3 opg169-a01-s09-cycle5-gsrc-source-or-escape-check.py
```

The checker reconstructs all five degree-six plane family templates, verifies
the exact thirteen-cell alias quotient, checks the full D/3 plane embedding,
complete stars, actual source face, payer-empty ledger, source/exterior ownership
partition, unique word and parent ID, and the disjoint degree cut.  It performs

```text
descendant_census_runs = 0
profile_recomputations = 0.
```

## 11. Disposition

```text
input: already actual source-bound selected J          REQUIRED
narrow selected-J G-COVER                              PASS(candidate)
d(7)=6 source identification                           exact C37 family/word
d(7)=6 minimum-counterexample branch                   R160 -> contradiction [candidate]
d(7)>=7                                                J_HIGHPORT escape
R-TOTAL from arbitrary Desc48                          NOT CLAIMED
G-TOTAL from arbitrary Desc48                          NOT CLAIMED
D0 -> R160                                             NOT CLAIMED
registry inversion                                     FORBIDDEN
best_verified_result                                   none
root_closed                                            false
```

The first still-open root bridge is **before** this lemma: producing an actual,
source-bound selected-J state (or an explicit non-J source class) uniformly from
each admissible `Desc48` description.  Cycle 5 does not repair that totality
gate and does not claim root closure.
