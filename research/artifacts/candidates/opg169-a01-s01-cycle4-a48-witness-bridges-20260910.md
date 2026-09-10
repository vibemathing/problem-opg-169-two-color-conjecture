# R08 S01 Cycle 4 — A48 witness semantics and completed source bridges

Verdict: `candidate_only`. `root_closed=false`. `best_verified_result=none`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected `main` consumed: `598d2c887a119fbb762ce51f9d6dc4af9431aff9`.

Cycle 4 makes one semantic repair and imports one newly completed repository-bound specialist package, S09 Cycle 3. S02-B and S10 remain active Cycle-3 dependencies. No completed S11, S12, S13 unique-mapper, S14, S15, or S04 successor is imported at this read.

## 1. A48 is an existential witness relation, not a face partition

Let `D0(f)` mean that `f` is an actual unpaid negative triangular face in the C34/C35 candidate ledger, so `mu(f)<0`.

For a corner `p` of `f`, retain the C48 parameters

```text
d(p) = 3 t(p) + s(p),
s(p) >= 0,
t(p)+s(p) >= 4.
```

Define the low-slack witness relation

```text
W48(f,p)  :<=>  p in V(f) and s(p) <= 5.
```

For a witness `(f,p)` define two arithmetic tags

```text
F48(f,p)  :<=>  W48(f,p) and t(p) <= 5,
SG48(f,p) :<=>  W48(f,p) and t(p) >= 6.
```

C48 Theorem 3.1 proves exactly the following quantifier pattern:

```text
forall f:
  D0(f) -> exists p W48(f,p),

forall f,p:
  W48(f,p) -> exactly_one(F48(f,p), SG48(f,p)).
```

It does **not** prove

```text
D0(f) -> exactly_one(
    exists p F48(f,p),
    exists p SG48(f,p)
).
```

It also does not prove a unique low-slack corner.

Therefore the Cycle-3 shorthand

```text
A48: F26 XOR SG
```

is superseded whenever it is read as a face-level branch partition. The XOR is valid only after a witness corner `p` has been fixed.

### Arithmetic pressure test for the distinction

At the arithmetic level consider three corner parameter triples

```text
(s,t,d) = (5,0,5), (5,6,23), (5,0,5).
```

Each satisfies the C48 integer-domain inequalities. Their corner contributions are

```text
gamma = 1/5, 7/23, 1/5,
```

so

```text
mu = -1 + 1/5 + 7/23 + 1/5
   = -34/115 < 0.
```

The first and third corners have the finite tag, while the second has the singleton-gap tag. This is an arithmetic countermodel to deriving face-level XOR from the C48 arithmetic premises. It is **not** asserted to be a geometrically realizable minimum-counterexample face.

Hence any later source theorem must carry the chosen witness `(f,p)` as provenance, or quantify uniformly over every eligible witness. It may not silently identify the face with an F or SG branch.

## 2. The finite tag and singleton tag have different choice semantics

### F tag

For a fixed F-tagged witness `(f,p)`, the pair `(s(p),t(p))` determines exactly one of C48's 26 arithmetic cells, with `d=3t+s`.

This gives a unique **arithmetic cell label for that witness**. It does not give a unique embedded parent. Rotation, directions, aliases, complete stars, edge ownership, and exterior contacts remain geometric data.

Thus `26` is a finite arithmetic type list, not a 26-parent source census.

### SG tag

For a fixed SG-tagged witness `(f,p)`, let `G48(p)` be the set of singleton cyclic gaps between consecutive marked pair blocks. C48 proves

```text
|G48(p)| >= t(p)-s(p) >= 1.
```

It does not prove `|G48(p)|=1`.

For example, at the arithmetic parameters `t=6,s=0`, all six positive gaps must have size one, so the gap selector is maximally nonunique. Again, this is an arithmetic observation, not a geometric realization claim.

C48 Section 4 then **chooses one** singleton gap `g in G48(p)`. For that selected gap it derives:

- the exact two-sector plane source state;
- three surviving local alias interfaces;
- `3 * 8^2 = 192` normalized direction patterns, conditional on the frozen eight-sector direction catalogue.

Therefore `192` is a **selected-gap local atlas**. It is not the number of all SG source states for a witness, a face, or the root problem.

## 3. Corrected A48 interface

The live arithmetic-to-source interface is now relational:

```text
D0 actual unpaid negative face f
 |
 +-- W48: choose/carry a low-slack witness p                  [PASS candidate]
      |
      +-- F48(f,p)                                            [per-witness tag]
      |     |
      |     +-- CELL48(p): unique one of 26 arithmetic cells
      |     `-- LSRC-F: actual embedded realizations           [UNKNOWN]
      |
      `-- SG48(f,p)                                           [per-witness tag]
            |
            +-- choose/carry g in G48(p)
            +-- GAP48(f,p,g): selected-gap local atlas
            |     3 alias interfaces / 192 normalized patterns
            |     conditional on the 8-sector catalogue
            `-- LSRC-SG: actual embedded realizations          [UNKNOWN]
```

There are two sound downstream disciplines:

1. **choice-free:** prove the next source theorem uniformly for every admissible witness `p` and, on SG, every selected singleton gap `g`; or
2. **selector-based:** define a canonical selector and prove that it is source-faithful before using it.

No selector theorem is imported in Cycle 4. A model-selected witness or gap without provenance is not a `JMAP`.

## 4. Global generation and unique mapping remain downstream

The corrected source chain is

```text
D0(f)
  -> W48(f,p) and a per-witness arithmetic tag
  -> LSRC(f,p[,g]) local embedded realization
  -> GSRC source generation from the actual face with payer/source identity
  -> JMAP unique L_join / exact parent identity
  -> SCUT exactly one STRUCT / A / B leaf.
```

`GSRC` and `JMAP` must resolve duplicate descriptions caused by multiple low-slack corners, multiple singleton gaps, aliases, or symmetries. They may not inherit uniqueness from A48, because A48 supplies none at face level.

The first genuine source-faithful cut therefore remains `SCUT`, and remains `UNKNOWN`.

## 5. Newly completed bridge: S09 exact C37 source-lineage atlas

Cycle 4 imports the completed S09 Cycle-3 package merged as main commit

```text
598d2c887a119fbb762ce51f9d6dc4af9431aff9.
```

Its repository-bound identities include:

```text
atlas SHA-256
1502702e3825a8ccc79f9162fe412371bc14091a8260a42b90f6826f44fda606

expanded parent-ID SHA-256
cb8b4171491572de52a1ca5f3ebe1235e6091dd7298c5b380f0477d0c9789b74

expanded 160-row SHA-256
65357c97e5fdb35ba150c7d658ed053489097ee6d1013ec03529685f643b6dab

lineage checker SHA-256
5a319d5d329f0ea80d2f22c04d715fcb56af1e51a80f61cb5a563c5ea643e609

lineage proof SHA-256
9d23c6846ff89f1acb39ef664ef800e6968aa569776b93d0e18dcbceddee4b61
```

### REG37 — exact source registry

The exact C37 `d(7)=6` source universe is now repository-bound as

```text
{D,X5,X6,Y4,Y5} x {0,...,31},
```

with five-bit direction semantics, aliases, controlled stars, and complementary-region data.

Status: `PASS(candidate source-registry)`.

### RED37 — ancestor rule allocation

The 160 rows partition exactly as

```text
96  exact direct-fan delete {0,2}
60  other unconditional merged-catalogue delete {0,2}
 4  bare delete 3: Y4/0,4,16,20
---
160
```

The 60 catalogue literals remain bound to the frozen S06 postprocess digest rather than being re-fabricated by S09.

S10 independently corroborates the aggregate `156+4` allocation and the full finite profile totals at candidate level.

### LINEAGE37 — exact-parent inheritance

S09 gives an explicit lineage gate. A descendant is ancestor-dominated only if it preserves:

1. every source arc of the C37 parent;
2. rotations and complete stars of controlled vertices `0,2,3,7`;
3. the parent interface and deletion hole;
4. only additional data in the arbitrary exterior already quantified by the parent rule; and
5. all parent vertex identities and controlled adjacencies.

Under those conditions the child is an exterior refinement of the exact parent and inherits its arbitrary-exterior positive-reachability reduction.

If any source arc, controlled star, rotation, interface, parent alias, or controlled adjacency changes, the object is a new source state and `LINEAGE37` does not apply.

Status: `PASS(candidate lineage bridge)`.

### D19-ID — named descendant identity

Exactly one current named C38/C39/C40 repository chain is assigned by the atlas:

```text
D/19.
```

After C38's `12 <-> 13` label swap, its complete 23-arc source equals C40 `BASE_ARCS`. Thus a physical C40 reverse guard may invalidate a C40 child shortcut but does not invalidate the unconditional C37 ancestor rule.

No named C38/C39/C40 chain is invented for the other 159 rows.

Status: `PASS(candidate exact identity bridge)`.

## 6. S09 blocker disposition

Cycle 3 recorded

```text
S09 = FAIL(source-admission gate):
missing exact remaining-child registry / source digests.
```

That specific blocker is now repaired at candidate level.

Within the exact C37 `d(7)=6` universe:

```text
registered exact source parents            160
unconditional ancestor parents             160
named C38->C39->C40 source rows              1
C40 guard-child enumeration required         0
```

The last zero is due to exact-parent ancestor precedence, not because every guard child was separately enumerated or contradicted.

Therefore the old S09 "remaining guard difference" lane is retired **inside this exact source universe**. It remains inapplicable, rather than solved, for changed sources, `d(7)>=7`, other J orientations, or any state failing the lineage gate.

## 7. Completed conditional C37 bridge

Combining the already merged S06/S10 finite profile work with the newly merged S09 registry/lineage work gives the following candidate conditional bridge:

```text
EXACT-C37(s)
  -> REG37 source identity                         [S09 PASS candidate]
  -> RED37 unconditional selected reduction        [S06 + S10 PASS candidate]
  -> LINEAGE37 arbitrary-exterior inheritance      [S09 PASS candidate]
  -> exclusion from a vertex-minimum counterexample
```

This bridge is strong enough that, **once** a future GSRC/JMAP theorem identifies an actual negative-face source with one of these 160 exact parents, the C37 `d(7)=6` finite reduction lane is no longer a live research blocker.

It does not provide the missing implication

```text
A48 witness -> EXACT-C37(s).
```

That remains a GSRC/JMAP problem.

## 8. Interaction with high-port termination

S02-B remains unchanged:

- raw degree/port/sector/size ranks fail on an arbitrarily long locally source-valid `d(7)>=7` family;
- its exact fixed four-port tail is profile-compressible;
- growing-interface / separator-crossing / complete-star escape remains the termination target.

S09 is exact `d(7)=6`. Its new source registry does not restrict or classify the S02-B high-port family.

Thus no ancestor-precedence edge is drawn from `REG37` into `d(7)>=7`.

## 9. Repaired live typed DAG

```text
R0 root
 |
 +-- D0 actual unpaid negative DC2 face f
      |
      +-- W48 witness relation: exists low-slack p
            |
            +-- per-witness F48
            |      -> unique arithmetic cell among 26
            |      -> LSRC-F                              [UNKNOWN]
            |
            `-- per-witness SG48
                   -> choose singleton gap g
                   -> selected-gap 3-interface / 192 atlas
                   -> LSRC-SG                             [UNKNOWN]

LSRC(f,p[,g])
 |
 +-- TERM side gate on recursive source/interface change
 |      raw degree/port/size rank                         [FAIL candidate route]
 |      fixed C37 four-port profile compression          [PASS exact family]
 |      growing-interface / separator escape rank        [UNKNOWN]
 |
 v
GSRC global source generation                             [UNKNOWN]
 |
 v
JMAP unique L_join / exact parent identity                [UNKNOWN]
 |
 v
SCUT exactly one STRUCT / A / B                           [UNKNOWN]
      |
      +-- STRUCT -> contradiction
      |
      +-- A -> strict ordinary reduction
      |       |
      |       +-- if EXACT-C37 d(7)=6:
      |       |     REG37 -> RED37 -> LINEAGE37           [PASS candidate bridge]
      |       |
      |       `-- LIFT-O
      |
      `-- B -> B-criticality                              [UNKNOWN]
              -> strict ordinary reduction
              -> LIFT-O

LIFT-O general arbitrary-exterior theorem/verification    [UNKNOWN]
 -> contradiction
```

The exact C37 conditional bridge is a leaf library. It is not `GSRC`, `JMAP`, or `SCUT`.

## 10. Current frontier after Cycle 4

1. **A48-to-source bridge with witness provenance.** Produce LSRC/GSRC from actual negative faces without treating F/SG or singleton-gap choice as a unique face branch.
2. **JMAP / unique `L_join`.** Resolve multiple witness/gap/source descriptions and prove exact unique parent/leaf identity, or provide an ambiguity/unmapped falsifier.
3. **ESCAPE-RANK.** Decide growing-interface / separator / complete-star termination.
4. **B-criticality.** Blocking-path, topology, and falsifier agreement remain missing.
5. **LIFT-O general theorem.** S09 gives a specialized exact-parent path-composition bridge; S10 finite corroboration does not replace the general S11 theorem.
6. **S04 / S14.** Corrected two-terminal and singleton-cap lanes remain `UNKNOWN` until a completed repository-bound successor survives source precedence.

S09 guard-child difference is no longer on the live frontier for exact C37 `d(7)=6`.

## 11. Wave status delta

| Slot | Cycle 4 status | Effect |
|---|---|---|
| S09 | PASS(candidate source bridge) | missing registry repaired; exact C37 guard-child census unnecessary under ancestor precedence |
| S10 | PASS(clean-room candidate, carried) | exact C37 finite profiles corroborated; anchored S08 remains separate |
| S02-B | PASS/FAIL split, carried | raw-size termination refuted; fixed-interface compression family-scoped |
| S13-A/B/C/D | UNKNOWN | A48 witness-to-source generation / unique mapper not completed |
| S12-A/B/C | UNKNOWN | B-criticality not completed |
| S02-A | UNKNOWN | escape rank not completed |
| S11 | UNKNOWN | general lifting theorem not completed |
| S14 | UNKNOWN | no completed cap successor |
| S15 | UNKNOWN | no completed new falsifier package |
| S04 | UNKNOWN | no completed two-terminal disposition |
| S01 | PASS(import/scope) | A48 semantics repaired and completed bridges integrated |

## 12. Truth boundary and non-claims

No truth-ledger status is inferred from candidate PRs or CI.

This checkpoint does not claim:

- a unique low-slack corner of a negative face;
- face-level F/SG exclusivity;
- a unique singleton gap at an SG witness;
- that 26 cells are source parents;
- that 192 is a complete SG source census;
- geometric realizability of every arithmetic witness;
- A48-to-C37 generation;
- a global source generator or unique `L_join`;
- a completed STRUCT/A/B cut;
- `d(7)>=7` coverage from S09;
- a global termination theorem;
- B-criticality;
- a general LIFT-O theorem;
- ordinary use of anchored S08 results;
- a two-terminal theorem or singleton-cap theorem;
- trusted independent verification;
- EvidenceLink, Result, Solution, or root closure.

`best_verified_result=none`  
`root_closed=false`
