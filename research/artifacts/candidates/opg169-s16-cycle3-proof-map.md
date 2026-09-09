# S16 Cycle 3 — Substantive Glue Kernel

```text
verdict: candidate_only
frozen_main: dc6ee891ed7614602e88d48a57314416082dd022
substantive_glue_source: complete
kernel_replay: not_run
global_configuration_premise: open
root_closed: false
```

## 1. Hidden conclusion removed

An earlier draft placed the rule-specific conclusion

```lean
Good Plane G (restoreColour colourH p e)
```

inside a `restoreGood` field. That would merely rename the gluing obligation.
The final source removes that field. A concrete rule supplies only primitive,
checkable decomposition data for each colour:

```lean
structure ExactColourGluing (whole) (p e) (k) where
  embed                : B → V
  patch exterior       : V → V → Prop
  patchAcyclic          : Acyclic patch
  exteriorAcyclic       : Acyclic exterior
  meetOnlyAtBoundary    : MeetOnlyAtBoundary patch exterior embed
  wholeExact            : whole x y ↔ patch x y ∨ exterior x y
  patchReachExact       : p.reach k x y ↔ PosWalk patch (embed x) (embed y)
  exteriorReachExact    : e.reach k x y ↔ PosWalk exterior (embed x) (embed y)
```

None of these fields asserts acyclicity of `whole`.

## 2. The proved cycle-compression theorem

For relations `P,E : V → V → Prop` and a labelled boundary embedding
`embed : B → V`, define

```lean
BoundaryMacro P E embed a b :=
  PosWalk P (embed a) (embed b) ∨
  PosWalk E (embed a) (embed b)
```

and require only that a switch between consecutive `P` and `E` edges occurs
at an embedded boundary vertex.

The theorem proved in source is

```lean
acyclic_union_of_boundary_macro :
  MeetOnlyAtBoundary P E embed →
  Acyclic P →
  Acyclic E →
  Acyclic (BoundaryMacro P E embed) →
  Acyclic (fun x y => P x y ∨ E x y)
```

The proof does not assume a cycle-localization oracle. It normalizes every
positive union walk into homogeneous runs:

```lean
inductive WalkDecomp
  | hom   : one positive P-run or E-run
  | mixed : positive first run
          → reflexive-or-positive boundary macro walk
          → positive last run
```

`WalkDecomp.append` is the normalization engine. Equal-side adjacent runs are
merged. Different-side adjacent runs invoke `MeetOnlyAtBoundary` and record the
switch as a labelled boundary vertex. Thus every closed union walk has exactly
two possible outcomes:

1. it is homogeneous, contradicting `Acyclic P` or `Acyclic E`; or
2. its runs form a nonempty closed `BoundaryMacro` walk, contradicting macro
   acyclicity.

This is the substantive finite walk-cutting argument from the C13 prose proof.

## 3. Exact gluing equivalence

For one colour `k`, an `ExactColourGluing whole p e k` proves both directions:

```lean
ExactColourGluing.acyclic_iff_joined :
  Acyclic whole ↔ Acyclic (Joined p e k)
```

where

```lean
Joined p e k x y := p.reach k x y ∨ e.reach k x y
```

### Whole to boundary

Each joined-state edge expands, using reachability exactness, to a positive
walk in one piece and then to a positive whole walk. `PosWalk.expand` replaces
all macro edges and concatenates the resulting paths. A joined closed walk
would therefore be a whole closed walk.

### Boundary to whole

Actual patch/exterior boundary reachability maps into `Joined`. Joined
acyclicity therefore implies actual macro acyclicity. The cycle-compression
theorem then proves the union acyclic, and `wholeExact` transports this to the
whole monochromatic relation.

Shared boundary arcs cause no exception: they may belong to either piece, but
any artificial side switch still occurs at a boundary endpoint.

## 4. Arbitrary-exterior monotonicity

For boundary states

```lean
Refines p q :=
  p.colour = q.colour ∧
  ∀ {k x y}, p.reach k x y → q.reach k x y
```

the source proves

```lean
compatible_of_refines :
  Refines p q → Compatible q e → Compatible p e
```

for an arbitrary unchanged exterior state `e`. For each colour,

```text
Joined(p,e) ⊆ Joined(q,e).
```

Any positive closed walk on the left maps edgewise to one on the right. This
is exactly the C40 direction `R_P⁺ ⊆ R_Q⁺`.

## 5. Complete-Q, same-exterior lifting

`StrongProfileReplacement Plane G H` requires:

- an actual contract object `H`;
- `split`, extracting the actual complete local state `q` and actual full
  exterior state `e` from every valid whole colouring of `H`;
- `simulate`, quantified over every valid complete `q`;
- an explicit restoration function;
- an exact primitive gluing decomposition for every restored colour; and
- literal equality on all represented retained vertices.

It no longer contains a `restoreGood` conclusion.

The proved theorem is

```lean
StrongProfileReplacement.lift_with_same_exterior :
  Good Plane H colourH →
  ∃ colourG e,
    Good Plane G colourG ∧
    exteriorOf colourH e ∧
    ∀ x : retainedType,
      colourG (retainedOriginal x) = colourH (retainedSmaller x)
```

Proof chain:

```text
Good(H, colourH)
  → split obtains actual q and actual e with Compatible(q,e)
  → complete simulate obtains p with Refines(p,q)
  → compatible_of_refines gives Compatible(p,e)
  → ExactColourGluing.acyclic_iff_joined, for both colours
  → Good(G, restoreColour colourH p e).
```

`split` also proves the complete-Q domain nonempty whenever minimality provides
a colouring of `H`; vacuous replacement profiles cannot pass this theorem.

## 6. Minimal-counterexample elimination

A strict reduction contains an actual smaller contract graph:

```lean
structure StrictProfileReduction (G) where
  m            : Nat
  smaller_lt   : m < n
  smallerGraph : PlaneOrientation Plane m
  rule         : StrongProfileReplacement Plane G smallerGraph
```

The strong induction hypothesis colours `smallerGraph`; the lifting theorem
colours `G`. Hence:

```lean
minimalBad_forbids_strictProfileReduction :
  MinimalBad Plane G →
  StrictProfileReduction Plane G →
  False
```

## 7. The one remaining root premise

The exact open theorem is

```lean
def MinimalReductionComplete : Prop :=
  ∀ n G,
    MinimalBad Plane G →
    Nonempty (StrictProfileReduction Plane G)
```

It is deliberately restricted to vertex-minimal bad graphs. Configuration and
discharging arguments may use every consequence of minimality; no reduction is
required for arbitrary bad graphs.

The source proves the complete conditional chain:

```lean
MinimalReductionComplete Plane
  → ShortestRootCut Plane
  → Root Plane
```

through

```lean
shortestRootCut_of_minimalReductionComplete
root_of_shortestRootCut
root_of_minimalReductionComplete
```

Thus the generic glue beneath the one-node cut is no longer open. The global
configuration theorem `MinimalReductionComplete ConcretePlane` remains open.

## 8. Concrete obligations not discharged here

For each catalogue rule or structural leaf, the producer still must prove:

1. the replacement is an actual strictly smaller simple plane orientation;
2. the local and exterior relations cover the full restored monochromatic arc
   relation exactly;
3. the two pieces meet only at the labelled boundary;
4. both piece colourings are acyclic;
5. boundary reachability is exact in both directions, including paths through
   other boundary vertices;
6. aliases, rotations, shared boundary arcs, and retained-vertex coverage are
   faithful; and
7. every minimal bad graph reaches such a rule, including guard failures,
   residual parents, and the dual-fan/high-degree branch.

These are source/geometry/completeness obligations, not missing generic gluing
logic.

## 9. Assurance

The Lean source imports only `Init`, contains no `sorry`, `admit`, declared
axiom, `unsafe`, or tactic hole, and includes `#print axioms` commands for the
main theorem chain. The current host has no Lean executable. Direct acquisition
of the official v4.33.0 Linux distribution was not completed, so elaboration,
kernel acceptance, and axiom output are not claimed.
