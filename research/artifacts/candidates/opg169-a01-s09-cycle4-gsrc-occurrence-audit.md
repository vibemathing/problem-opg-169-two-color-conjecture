# R08 S09 Cycle 4 — GSRC occurrence audit from the C37 160-parent registry

`verdict=candidate_only`; `root_closed=false`; `best_verified_result=none`.

Fresh protected base after Cycle-4 witness-semantics synchronization:
`a2a9973d2f995de71095a6bea814cbe882cb7718`.

This cycle performs **zero descendant census**.  It asks the reverse-source
question left after Cycle 3: can the exact C37 160-parent conditional reduction
registry itself force an actual unpaid negative DC2 face to occur in one of
those parents?

The answer is **no as an inference from the registry**.  The repository also
does not currently supply the missing global-occurrence bridge.  The useful
positive consequence is instead a conditional escape lemma: if the exact
selected C35/C36 J-source occurs in a vertex-minimum counterexample, the C37
`d(7)=6` registry kills the equality case, so that selected source must have
`d(7)>=7`.

## 1. Frozen inputs and the corrected witness semantics

Cycle 3 freezes the exact C37 `d(7)=6` registry

```text
R160 = {D,X5,X6,Y4,Y5} x {0,...,31},
```

with 160 exact source IDs and an unconditional strict all-exterior reduction for
each parent.  That has the logical direction

```text
forall s in R160:
    exact_C37_parent(s) -> reducible(s).
```

It contains no existential statement saying that an actual negative face
generates a member of `R160`.

S01 Cycle 4 also repairs the quantifier semantics upstream of GSRC.  For an
actual unpaid negative face `f` and a corner `p`, write

```text
D0(f)       actual unpaid negative triangular face
W48(f,p)    p is a corner of f and s(p)<=5
F48(f,p)    W48(f,p) and t(p)<=5
SG48(f,p)   W48(f,p) and t(p)>=6.
```

The exact arithmetic theorem is

```text
forall f:
    D0(f) -> exists p W48(f,p),

forall f,p:
    W48(f,p) -> exactly_one(F48(f,p), SG48(f,p)).
```

It does **not** give a unique low-slack corner and does **not** give a
face-level XOR between “there exists an F corner” and “there exists an SG
corner”.  On the SG side it can also leave several singleton gaps; a selected
gap `g` must be carried as provenance.  Thus the arithmetic-to-source state is
relational in `(f,p[,g])`, not a single face label.

Repository-bound identities consumed here are:

```text
Cycle-3 R160 atlas blob       05e6b31700d9c570927b8d96e76750feb32ee885
Cycle-3 lineage proof blob    2d31a464630482ea3bf145495bfd497eb19d97f2
C35 proof blob                621cb2455dfeb71b3b078ec05ef842f5d89f26fc
C36 incoming proof blob       1aa0158d67c1beafc04a9442792e034c72e73dc1
C48 proof blob                2ae68b69ca5de217ea923e2dac08cd70ea2cf3fe
S01 Cycle-3 type-repair blob  fcc40a0137fe225cbc991020f75b5a1b08d76a7b
S01 Cycle-4 witness blob      d35127a24cdc96b98c58676a4120bc0ac3318954
S02-B high-port blob          81233ffe3a8c9addb6ed9388505720f08f08ab7c
```

No source is promoted beyond its repository verdict.

## 2. Registry non-inversion lemma

Let `R160` be any 160-element set and suppose

```text
forall s in R160, reducible(s).
```

This premise does not imply

```text
forall actual unpaid faces f,
    exists s in R160, occurs(f,s).
```

A finite pure-logic countermodel suffices.  Take one face symbol `f`; keep all
160 registry symbols; set `reducible(s)=true` for every registry symbol; and
set the occurrence relation empty.  The registry premise is true while

```text
exists s in R160, occurs(f,s)
```

is false.

This is a countermodel only to the **logical inversion**.  It is not a plane
graph counterexample, does not assert that such an `f` exists in a graph, and
does not refute GSRC.  It proves that an occurrence theorem needs additional
premises linking `(f,p[,g])` to an exact embedded source state.

## 3. Why A48 cannot supply the missing implication

C35 explicitly separates three domains:

```text
integer arithmetic parameters
actual planar realizations
genuine minimum-counterexample occurrences.
```

Its arithmetic negative families are symbolic and can have unbounded degree.
The degree-five graph built there is a realizability/control example, not a
global source-generation theorem.

C48 and S01 Cycle 4 sharpen the same distinction.  From `D0(f)` we may choose
or carry a witness `p` satisfying `W48(f,p)`.  For that **fixed** witness:

```text
F48(f,p):
    one of 26 arithmetic cells
    -> LSRC-F(f,p,geometry)                    [OPEN]

SG48(f,p):
    choose/carry g in G48(p)
    -> selected-gap 3-interface / 192-direction atlas
    -> LSRC-SG(f,p,g,geometry)                 [OPEN].
```

The 26 labels are arithmetic cells, not embedded parents.  The 192 labels are
a selected-gap local atlas for `(f,p,g)`, not all source states attached to the
face.  Multiple eligible corners, multiple singleton gaps, aliases, and
symmetries can describe overlapping or different local states.  GSRC/JMAP must
resolve those descriptions; A48 gives no canonical selector.

There is no repository-bound identification of either the 26 arithmetic cells
or the selected-gap 192 atlas with the C37 160-parent J registry.  Treating
them as the same source would silently change complete stars, rotations,
interfaces, or provenance.

Hence the live source chain relevant to this audit is

```text
D0(f)
 |
 +-- choose/carry p with W48(f,p)
       |
       +-- F48(f,p)
       |     -> LSRC-F(f,p,geometry)                  [OPEN]
       |
       `-- SG48(f,p)
             -> choose/carry g
             -> LSRC-SG(f,p,g,geometry)               [OPEN]
                    |
                    v
                  GSRC
        source/payer identity + ownership
        + no double spending                           [OPEN]
                    |
                    +-- C37J specialization            [OPEN]
                    |
                    `-- other explicit source class    [OPEN]
                    |
                    v
                  JMAP                                 [OPEN]
```

There is still no edge from an actual unpaid face to `R160`.

## 4. Positive result: the selected-J escape lemma

C36 works only after fixing the C35 J-direction.  Its incoming fifth-neighbour
candidate, together with the separately preserved earlier C36 degree-four,
outgoing-`d5`, and old-port cases, has the scoped conclusion

```text
selected C35/C36 J-source in a minimum counterexample
    -> d(7)>=6.
```

Assume now that this exact selected J-source occurs in a vertex-minimum
counterexample and suppose `d(7)=6`.

C37's exact degree-six source classification then leaves precisely the five
families

```text
D, X5, X6, Y4, Y5
```

with all 32 direction words in each family.  Therefore the exact source has one
of the 160 Cycle-3 registry IDs.  S06 supplies a strict all-exterior
strong-profile reduction for every one of those exact parents, and S10 gives
candidate-level clean-room corroboration of the aggregate `160/160` result.

Minimum order therefore excludes the `d(7)=6` branch.  Consequently,

```text
selected C35/C36 J-source in a vertex-minimum counterexample
    -> d(7)>=7.
```

This is the strongest positive occurrence-related conclusion in Cycle 4.  It
is deliberately conditional on already having the selected J-source.

It is **not**

```text
D0(f) -> exists s in R160 occurs(f,s).
```

In fact, within a minimum counterexample the exact selected-J degree-six branch
is the branch `R160` forbids.

## 5. High-port pressure confirms that degree six is not an occurrence target

No corrected A48 witness theorem forces the vertex later called `7` to have
degree six.  The F witness cells contain many degrees other than six, and the
SG witness branch is unbounded.

S02-B gives additional source-level pressure: within the C37 J-sector it
constructs arbitrarily long locally source-valid plane expansions with

```text
d(7)=6+n, n>=1.
```

Those constructions are not globally generated from `D0(f)`, so they do not
refute GSRC.  They do refute an attempted local shortcut saying that
source-valid J geometry itself collapses to degree six.

The newer S02-B escape-rank audit further attacks history-free release and
purely local separator ranks.  That affects the downstream `d(7)>=7` escape
lane, not the occurrence implication proved here.

## 6. Exact GSRC occurrence obligations

Cycle 4 freezes the following statement statuses.

Established arithmetic/source facts:

```text
D0(f) -> exists p W48(f,p)

for fixed (f,p):
W48(f,p) -> exactly_one(F48(f,p), SG48(f,p))

selected J-source + minimum counterexample -> d(7)>=7
```

Open source-generation edges:

```text
F48(f,p) -> LSRC-F(f,p,geometry)

SG48(f,p) + chosen g -> LSRC-SG(f,p,g,geometry)

LSRC-F / LSRC-SG -> GSRC
    with exact payer/source identity, edge/face ownership,
    and no double spending

GSRC -> C37J specialization OR an explicit disjoint source class

GSRC -> JMAP / unique L_join.
```

The registry is therefore a kill-switch **after** exact source identification;
it cannot create the source-identification edge.

## 7. Smallest useful next theorem

The next target should not be `D0 -> R160`.  It is both unsupported and too
narrow for the current source architecture.

The smallest useful target is a provenance-preserving **GSRC
source-or-escape lemma**:

> For every actual unpaid negative face `f`, and for every selected/canonical
> low-slack witness description `(f,p[,g])` used by the construction, produce
> an actual source-faithful embedded state with exact payer/source identity and
> ownership; after quotienting duplicate descriptions explicitly, each generated
> state either specializes to the selected C37 J-source or is assigned to an
> explicit disjoint escape/source class.

Then:

- C37J with `d(7)=6` is killed immediately by `R160`;
- C37J with `d(7)>=7` enters the high-port/escape lane;
- non-C37 source states remain explicitly typed instead of being silently
  forced into the registry;
- a separate `JMAP` theorem can later prove uniqueness/canonical ownership.

## 8. Mutation tests

Cycle 4 rejects these mutations:

1. invert `forall s in R160 reducible(s)` into an occurrence existential;
2. read fixed-witness `F48 XOR SG48` as face-level XOR;
3. discard the witness corner `p`;
4. on SG, discard the selected singleton gap `g`;
5. identify arithmetic-cell membership with plane/source occurrence;
6. identify a locally source-valid patch with global generation from `D0`;
7. replace C36's `d(7)>=6` by `d(7)=6`;
8. omit payer/source identity, ownership, or no-double-spending data;
9. treat an unmerged/empty specialist branch name as a theorem;
10. restart C40 guard-child or any descendant census.

The static checker requires

```text
descendant_census_runs = 0.
```

## 9. Reproduction

Files:

```text
research/artifacts/candidates/opg169-a01-s09-cycle4-gsrc-occurrence-obligations.json
research/artifacts/candidates/opg169-a01-s09-cycle4-gsrc-occurrence-check.py
research/artifacts/candidates/opg169-a01-s09-cycle4-gsrc-occurrence-output.json
```

Run from the candidate directory:

```bash
python3 opg169-a01-s09-cycle4-gsrc-occurrence-check.py
```

The checker expands no descendants and recomputes no strong-profile tables.  It
checks the exact Cycle-3 registry identity, the corrected A48 witness
quantifiers, the pure-logic non-inversion countermodel, the selected-J escape
status, the open provenance-preserving GSRC edges, and the zero-descendant
invariant.

## 10. Disposition

```text
R160 exact conditional reduction registry          160/160
registry -> GSRC occurrence by inversion            INVALID inference
D0 -> R160 occurrence theorem                       OPEN / not derived
A48 face-level F-vs-SG XOR                          INVALID reading
fixed-witness F48-vs-SG48 XOR                       VALID candidate arithmetic
selected-J minimum-counterexample escape            d(7)>=7 [candidate]
descendant census runs                              0
GSRC occurrence                                     OPEN
minimal next target                                 GSRC source-or-escape lemma
best_verified_result                                none
root_closed                                         false
```

Non-claims: GSRC is not refuted; no claim is made that an arbitrary graph cannot
contain a C37 parent; no `d(7)>=7` classification or termination theorem is
proved; no canonical witness/gap selector, global `L_join`, unique mapper,
EvidenceLink, Result, or root closure is claimed.
