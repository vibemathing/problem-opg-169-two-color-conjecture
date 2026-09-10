# R08 S01 Cycle 7 — final protected-main refinement

`candidate_only`; `best_verified_result=none`; `root_closed=false`.

Fresh protected main synchronized into this Cycle-7 branch:
`77c1f89d5c3ae67acf9d49de041d7df5957937fb`.

This refinement supplements
`opg169-a01-s01-cycle7-typed-acceptance-20260910.md`.
It changes no acceptance type or root theorem.

## 1. Sole acceptance chain remains

```text
PHYSICAL_GEOMETRY
  -- SAME_MINCE_BIND -->
SAME_MINCE_JREL_JOIN
  -- ROW_PREDICATE + EXHAUSTIVE_OMEGA_BIND -->
CLOSURE_CONSUMABLE_CERTIFICATE
  -- ALL OBLIGATIONS DISCHARGED -->
JCLOSE-EC.
```

The root route remains

```text
D0 -> LowCorners -> JREL-SOUND/TOTAL -> JCLOSE-EC -> Sigma-mu contradiction.
```

`JUNIQ` and exact-one SCUT remain optional.

## 2. Protected-main B46 source gate

The only new protected-main delta after Cycle 6 is the merged S10 Cycle-4
clean-room source gate for the historical S13-C B46 package.

Its exact disposition is source-admission only:

```text
expected_row_slots = 46
source_row_ids_recovered = 0
mathematically_consumed_rows = 0
PASS = 0
FAIL = 0
NOT_VERIFIABLE_CORRUPT_TRANSPORT = 46
```

The committed audit proves a byte/manifest inconsistency in the historical
transport and explicitly declines to reverse-engineer the missing rows from
producer code or summaries.

Therefore B46 contributes no Type-P row identities, no Type-J joins and no
Type-C closure certificates in Cycle 7.

This is a **block**, not a B-criticality failure.

## 3. Interaction with S13-A / S12-A

Two different acceptance blocks must remain separate.

1. `S13C_B46_SOURCE_BINDING = BLOCK(source-row-identity unavailable)`.
   This is a Type-P/source-identity block.
2. `BCRIT_PREDICATE_BIND = BLOCK(predicate absent)`.
   This is a Type-J -> Type-C semantic-predicate block for the 82
   `PROFILE_CRITICAL` obligations in the Cycle-7 S12-A frontier.

Neither block changes the S12-A counts and neither declares a Bcrit theorem
false.

The Cycle-7 S12-A frontier therefore remains

```text
206 ALL_EXTEND
216 STRUCT_SEPARATOR
82  PROFILE_CRITICAL          [predicate block]
40  FLIP_STAR_PROFILE_MISSING_A
240 FLIP_STAR_PROFILE_MISSING_B
0   SURVIVOR
0   TOPOLOGY_CLOSURE
```

with all 784 obligations still conditional on a same-MinCE source-row bind.

## 4. First missing root row remains unchanged

The first missing actual row is still the Type-J acceptance witness

```text
JREL(G,f,p,J0)
```

for the assumed minimum counterexample `G`, the same actual negative face
`D0(f)`, a low corner `p`, and one exact physical source row with complete
aliases/stars/contacts/ownership/payer data.

The new B46 source gate is downstream of this root bottleneck; it cannot replace
or create `JREL-TOTAL`.

## 5. Shortest route remains

The shortest visible finite root-useful route remains:

```text
SAME-MINCE JREL-TOTAL into the S12-A source universe
 -> close 216 STRUCT_SEPARATOR
 -> bind Bcrit predicate and close 82 PROFILE_CRITICAL
 -> close 40+240 flip-star-profile missing
 -> close 206 ALL_EXTEND / reductions with LIFT-BIND
 -> obtain the missing real Lean 4.28 LIFT-VERIFY receipt
 -> JCLOSE-EC.
```

If such a totality theorem cannot force the S12-A universe, the selected-J
`J_HIGHPORT` escape remains an additional `TPROG` branch.

No atlas count, B46 slot count, C35 canary, D/3 control or R160 table is used as
an occurrence theorem.

No EvidenceLink, Result, Solution, trusted verification, or root closure is
created by this refinement.
