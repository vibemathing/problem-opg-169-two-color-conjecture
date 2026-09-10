# R08 S09 Cycle 4 — GSRC occurrence audit from the C37 160-parent registry

`verdict=candidate_only`; `root_closed=false`; `best_verified_result=none`.

Fresh protected base at construction: `a31eb9646c828e05ed9071f6830a24df28f5b64d`.

This cycle does **not** enumerate C40 descendants or guard truth cells. It asks the
opposite-direction question left after Cycle 3: can the exact C37 160-parent
reduction registry itself force an actual unpaid negative DC2 face to occur in
one of those source parents?

The answer is **no as an inference from the registry**, and current repository
artifacts do not supply the missing occurrence bridge. The useful positive
consequence is instead a conditional escape lemma: if the already selected
C35/C36 J-source occurs in a vertex-minimum counterexample, then the C37
`d(7)=6` registry eliminates the equality case and the source must have
`d(7)>=7`.

## 1. Frozen inputs and type discipline

The Cycle-3 S09 registry freezes exactly five C37 families

```text
D, X5, X6, Y4, Y5
```

and all 32 direction words in each family, for 160 exact C37 source parents.
It allocates an unconditional strict all-exterior reduction to every parent,
with 156 delete-`{0,2}` ancestors and four bare delete-3 ancestors.

That statement has the logical form

```text
for every s in R160:
    exact_C37_parent(s) -> reducible(s).
```

It is a **conditional reduction theorem**. It contains no existential statement
saying that a given negative face generates an element of `R160`.

Repository-bound source identities used by this audit:

- Cycle-3 atlas git blob `05e6b31700d9c570927b8d96e76750feb32ee885`;
- Cycle-3 lineage proof git blob `2d31a464630482ea3bf145495bfd497eb19d97f2`;
- C35 proof git blob `621cb2455dfeb71b3b078ec05ef842f5d89f26fc`;
- C36 incoming proof git blob `1aa0158d67c1beafc04a9442792e034c72e73dc1`;
- C48 proof git blob `2ae68b69ca5de217ea923e2dac08cd70ea2cf3fe`;
- S01 Cycle-3 type repair git blob `fcc40a0137fe225cbc991020f75b5a1b08d76a7b`;
- S02-B high-port audit git blob `81233ffe3a8c9addb6ed9388505720f08f08ab7c`.

No source is promoted beyond its repository verdict.

## 2. Non-inversion lemma

Let `R160` be any 160-element set and suppose

```text
forall s in R160, reducible(s).
```

This premise does not imply

```text
forall actual unpaid faces f, exists s in R160, occurs(f,s).
```

A finite logical countermodel is enough. Take one face symbol `f`, keep all
160 registry symbols, set `reducible(s)=true` for every registry symbol, and
set the binary occurrence relation empty. The registry premise is true, while

```text
exists s in R160, occurs(f,s)
```

is false.

This is a countermodel to the **logical inversion**, not a planar graph
counterexample and not a refutation of GSRC. It proves that an occurrence
theorem needs additional mathematical premises connecting an actual negative
face to a source state.

The machine-readable obligations file freezes this countermodel explicitly.

## 3. The upstream artifacts stop before GSRC

C35 deliberately distinguishes:

```text
integer arithmetic parameters
actual planar realizations
genuine minimum-counterexample occurrences.
```

It says arithmetic admissibility does not imply either later domain. Its six
LLL/LLN/LNN/LLP/LNP/LPP negative families are symbolic and can have unbounded
degree; the constructed degree-five graph is only a realizability/control
example, not a global occurrence theorem.

C48 likewise proves an arithmetic low-slack locator from every unpaid negative
triangle:

```text
D0 -> A48 = F26 XOR singleton-gap.
```

But C48 explicitly states that the 26 cells are not thereby reducible and that
the singleton gap does not automatically yield the later shell/cap structure.
Arithmetic admissibility alone does not establish planar realizability or
minimum-counterexample occurrence.

S01 Cycle 3 therefore correctly retypes the live chain as

```text
D0 -> A48 -> LSRC -> GSRC -> JMAP -> SCUT,
```

with `LSRC`, `GSRC`, and `JMAP` open.

There is also no repository-bound identification between C48's 192 normalized
singleton-gap direction parents and the C37 160-parent J registry. They are
different source normal forms. Treating one atlas as the occurrence source of
the other would silently change complete stars, rotations, and source identity.

## 4. What C36 and R160 actually imply: selected-J escape

C36 works only after fixing the C35 J-direction. In the incoming fifth-neighbour
case it controls the complete degree-five stars and proves the four remaining
incoming `d(7)=5` directions reducible. Combined with the separately preserved
earlier C36 degree-four, outgoing-`d5`, and old-port cases, its own conclusion is:

```text
in this selected J-direction, a minimum counterexample must have d(7)>=6.
```

Now assume this exact selected J-source occurs in a vertex-minimum
counterexample and suppose `d(7)=6`.

At degree six, C37's exact source classification leaves exactly the five
families in the Cycle-3 registry, with all 32 directions in each family.
Thus the source is one of `R160`. The imported S06 catalogue, corroborated at
candidate level by S10's clean-room consumer, gives an unconditional strict
all-exterior strong-profile reduction for every one of those 160 exact parents.
Minimum order then excludes the source.

Contradiction. Therefore, under the stated selected-J dependencies,

```text
selected C35/C36 J-source in a minimum counterexample
    => d(7)>=7.
```

This is the strongest positive source consequence obtained in this cycle.

It is **not**

```text
D0 => an R160 parent occurs.
```

Indeed, inside a minimum counterexample the exact selected-J `d(7)=6` branch is
the branch R160 forbids.

## 5. Why degree six cannot be forced from A48

C48's 26 finite cells include many degrees other than six and its high-`t`
singleton branch is unbounded. No C48 arithmetic statement forces the vertex
that would play C37's `7` to have degree six.

S02-B supplies additional adversarial pressure: within the C37 J-sector it
constructs arbitrarily long locally source-valid plane expansions with

```text
d(7)=6+n,  n>=1.
```

Those graphs are not claimed to be globally generated from an unpaid negative
face, so they do not refute GSRC. They do refute any attempted local inference
that source-valid J geometry itself collapses to `d(7)=6`.

Thus replacing `d(7)>=6` by `d(7)=6` is an invalid mutation.

## 6. Exact GSRC occurrence obligation DAG

The current source-direction DAG is:

```text
D0  actual unpaid negative face
 |
 v
A48 arithmetic locator                         PASS candidate arithmetic
 |
 |  missing: actual rotations/faces/aliases/stars/ownership
 v
LSRC local source realization                  OPEN
 |
 |  missing: source/payer identity + no double spending
 v
GSRC global source generation                  OPEN
 |
 +-- missing specialization: exact C35/C36/C37 selected J-source
 |      |
 |      +-- d(7)=6 -> R160 -> strict reduction -> contradiction
 |      |
 |      `-- d(7)>=7 -> high-port / escape resolution            OPEN
 |
 `-- other explicitly typed source class                        OPEN

JMAP / unique L_join                                            OPEN
```

The registry therefore removes a leaf **after** source identification; it does
not create the source-identification edge.

The exact missing edges recorded by Cycle 4 are

```text
A48 -> LSRC
LSRC -> GSRC
GSRC -> C37J
GSRC -> JMAP
```

No descendant edge is part of this audit.

## 7. Smallest useful next theorem

The smallest theorem that would make the registry relevant to GSRC occurrence
is not `D0 -> R160`. That statement is too strong and conflicts with the
selected-J escape conclusion in a minimum counterexample.

The appropriate target is a **GSRC source-or-escape lemma**:

> Every actual unpaid negative face generates a source-faithful state with
> exact payer/source identity and ownership, and that state either specializes
> to the selected C37 J-source or belongs to an explicit disjoint escape class.

Then:

- if the C37-J specialization reaches `d(7)=6`, R160 closes it immediately;
- if it has `d(7)>=7`, it enters the high-port/escape lane;
- a non-C37 source remains explicitly typed instead of being silently forced
  into the registry.

A uniqueness theorem (`JMAP`) is a separate later obligation.

## 8. Mutation tests

Cycle 4 rejects each of the following moves:

1. invert `forall s in R160, reducible(s)` into an occurrence existential;
2. equate A48 arithmetic membership with a plane/source occurrence;
3. equate a locally source-valid patch with global generation from `D0`;
4. replace C36's `d(7)>=6` by `d(7)=6`;
5. drop payer/source identity, ownership, or no-double-spending data;
6. infer a theorem from an empty/unmerged specialist branch name;
7. restart C40 guard-child or descendant enumeration.

The static checker also requires

```text
descendant_census_runs = 0.
```

## 9. Reproduction and digests

Files:

```text
research/artifacts/candidates/opg169-a01-s09-cycle4-gsrc-occurrence-obligations.json
research/artifacts/candidates/opg169-a01-s09-cycle4-gsrc-occurrence-check.py
research/artifacts/candidates/opg169-a01-s09-cycle4-gsrc-occurrence-output.json
```

Frozen candidate SHA-256 values:

```text
obligations  2842785b406a1781a39f48b4dfa7e45a3e8ea851aab9ebffb5d4bf37017075fb
checker      f0c63c34ea906871799b60daef5288dd14289b4271778d26fd07b77e718943c2
output       956501e11d5e1655921168f340e055ddfc08f22d912d259221a7c905df0107f1
```

Run from the candidate directory:

```bash
python3 opg169-a01-s09-cycle4-gsrc-occurrence-check.py
```

The checker expands no descendants and recomputes no strong-profile tables. It
checks only the 160 registry identity/counts, the pure-logic non-inversion
countermodel, the open occurrence edges, the conditional selected-J escape
status, and the zero-descendant-census invariant.

## 10. Disposition

```text
R160 exact conditional reduction registry          160/160
registry-to-GSRC occurrence implication             INVALID inference
D0-to-R160 occurrence edges proved                  0
selected-J minimum-counterexample escape            d(7)>=7  [candidate]
descendant census runs                              0
GSRC occurrence                                     OPEN
minimal next target                                 source-or-escape lemma
best_verified_result                                none
root_closed                                         false
```

Non-claims: GSRC is not refuted; no claim is made that an arbitrary graph cannot
contain a C37 parent; no `d(7)>=7` classification or termination theorem is
proved; no global `L_join`, unique mapper, EvidenceLink, Result, or root closure
is claimed.
