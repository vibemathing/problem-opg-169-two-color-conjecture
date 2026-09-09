# C45 — first C44 residual: degree-four endpoint absorption

**Verdict:** `candidate_only`  
**Base:** `d579bbf457d01e084bc8ffaee308441db3f14765` (merged C44).  
**Target:** `obligation:opg169-root`.

This candidate treats only the lexicographically first residual wheel in C44,
and only the subcase in which one endpoint of one forced directed triangle has
complete degree four. It gives two unconditional reductions, two guarded
reductions, and a quantified same-boundary obstruction when the common guard
fails. It does not close the other fourteen C44 residual wheels or the root.

## 1. Frozen residual wheel

Use boundary order

```
(8,12,a,b)
```

and centre `u`. The complete arcs are

```
8->12,
a->12,
b->a,
b->8,
8->u,
12->u,
u->a,
u->b.
```

The centre rotation is `(8,12,a,b)`. Two opposite incident faces are directed
triangles:

```
12->u->a->12,
u->b->8->u.
```

This is C44 row `spoke_in_mask=3, rim_word=4`. The boundary colouring

```
c(8)=c(b)=0,
c(12)=c(a)=1
```

blocks both colours of `u`, so bare centre deletion has ordinary nonextension.

## 2. Absorb a complete degree-four endpoint

Assume `d(a)=4`. Its known neighbours are `12,u,b`; write its fourth neighbour
as `z`. The complete rotation may be written

```
(12,u,b,z),
```

with actual outside faces `(a,b,z)` and `(a,z,12)`. At `a`, the arcs `u->a` and
`b->a` already give two incoming arcs, while `a->12` is its only known outgoing
arc. The previously proved semidegree bound therefore forces

```
a->z.
```

Simplicity makes `z` distinct from `a,12,u,b`. The alias `z=8` is also
impossible in the canonical C43 source: the six faces of the expanded patch
would close the link of `8` on the four neighbours `u,12,a,b`, forcing
`d(8)=4`, whereas the C43 frozen graph already gives distinct neighbours
`3,4,7,12,13,14,15,16,17` of `8`. Any other alias to an exterior vertex is
retained, provided its pre-existing arcs agree with the displayed orientation.
No unknown edge incident with `u` or `a` exists, because both stars are complete.

The controlled set is `{u,a}` and the four fixed exterior ports, in boundary
order, are

```
B=(8,12,z,b).
```

The expanded patch consists of the six actual triangles

```
(u,8,12), (u,12,a), (u,a,b), (u,b,8),
(a,12,z), (a,z,b).
```

The two remaining edge directions are `12-z` and `z-b`, giving exactly four
labelled words.

## 3. Four direction words and exact reductions

Use bit zero for `12->z` (unset means `z->12`) and bit one for `z->b`
(unset means `b->z`). The complete allocation is:

| word | outside directions | replacement | guard | valid Q / equal R / strict decrease |
|---:|---|---|---|---:|
| 0 | `z->12`, `b->z` | delete `u`, add `8->a` | none | 32 / 26 / 6 |
| 1 | `12->z`, `b->z` | delete `u`, add `8->a` | none | 32 / 30 / 2 |
| 2 | `z->12`, `z->b` | delete `{u,a}`, add `8->z` | actual `z->8` absent | 12 / 10 / 2 |
| 3 | `12->z`, `z->b` | delete `{u,a}`, add `8->z` | actual `z->8` absent | 12 / 12 / 0 |

Thus the four endpoint directions split as

```
2 unconditional + 2 conditional.
```

For words 0 and 1, the arc `8->a` lies in the quadrilateral hole created by
deleting `u`. Its reverse cannot be an exterior arc: the complete degree-four
star of `a` has neighbours exactly `12,u,b,z`, and `z!=8`.

For words 2 and 3, deleting `u,a` produces the quadrilateral disk with boundary
`(8,12,z,b)`. The arc `8->z` is drawn in that disk. If it already exists on the
exterior side, it is retained once; if the reverse `z->8` exists, the rule is
not applicable because it would create a digon. That reverse arc is therefore
the exact guard, not a generic nonadjacency assumption.

Every table entry quantifies over a **complete** valid colouring of `Q`. It gives
a complete colouring of the original patch with identical colours on `B` and

```
R_P^+ subseteq R_Q^+.
```

The 88 selected entries include every valid complete smaller colouring; invalid
smaller colourings remain explicitly invalid.

## 4. Arbitrary exterior and strict class preservation

For a positive row, form the whole smaller graph by the displayed deletion and,
where needed, the cofacial shortcut. The result has one or two fewer vertices.
The shortcut is embedded in the actual deletion disk; every reverse conflict is
either impossible from a complete star or named as the guard. Consequently the
smaller graph remains finite, simple, planar and oriented.

Take any valid two-colouring of the whole smaller graph. Restrict it to the
saved `Q` input, choose its certified original-patch lift, and keep every vertex
outside `{u,a}` fixed. If a new monochromatic cycle crosses the patch boundary,
split it at consecutive vertices of `B`. Each positive original-patch segment
belongs to `R_P^+` and can be replaced by a same-colour `Q` segment. The exterior
segments are unchanged, yielding a positive monochromatic closed walk in the
originally valid smaller colouring, hence a directed cycle. This contradiction
proves the lift for every exterior, not merely for direct boundary chords.

Therefore words 0 and 1 cannot occur in a minimum-order counterexample with
`d(a)=4`. Words 2 and 3 cannot occur when their exact reverse guard is absent.

## 5. Guard failure: no same-boundary strict replacement exists

Now take word 2 or 3 and suppose the actual reverse guard

```
z->8
```

is present. Fix the boundary colouring

```
c(8)=0, c(12)=1, c(z)=0, c(b)=0.                 (*)
```

The original patch has no extension:

- if `c(a)=0`, then `a->z->b->a` is a monochromatic directed triangle;
- if `c(a)=1` and `c(u)=1`, then `12->u->a->12` is monochromatic;
- if `c(a)=1` and `c(u)=0`, then `u->b->8->u` is monochromatic.

This is an **ordinary** nonextension, not only a reachability-containment
failure.

Consider any replacement inside the same four-vertex boundary that preserves
the four distinct ports and is strictly smaller than the two-internal-vertex
patch. It has at most one internal vertex `w`. Under (*), colour `w` by 1.
The colour-zero boundary digraph consists, at most, of

```
z->b->8 and z->8,
```

which is acyclic. The other possible boundary diagonal is `12-b`, which is
bichromatic under (*). The colour-one class has at most the two vertices
`{12,w}` and is acyclic in a simple orientation, since no loop or digon is
allowed. Removing boundary arcs only makes these classes sparser.

Hence **every** same-boundary strictly smaller simple oriented replacement has
at least one valid colouring extending (*), while the original patch has none.
No such replacement can satisfy even ordinary all-Q lifting, and therefore none
can satisfy strong profile lifting.

This obstruction is not an impossibility theorem for a larger interface. It
proves that the next successful route must release at least one of the four
ports `8,12,z,b` (or otherwise change the exterior interface) and include the
released vertex's complete star.

## 6. Full six-face double-payment ledger

No transfer rule changes. On the original graph

```
gamma(v)=(d(v)-4-2t(v))/d(v),
mu(f)=|f|-4 + sum_corner gamma + h(f).
```

Both controlled vertices have degree four, so `t(u)=t(a)=0` and
`gamma(u)=gamma(a)=0`. The complete sum over the six actual faces is

```
-6 + 2*gamma(8) + 3*gamma(12) + 2*gamma(z) + 3*gamma(b)
   + h(u,8,12)+h(u,12,a)+h(u,a,b)+h(u,b,8)
   + h(a,12,z)+h(a,z,b).
```

Relative to the old one-side payment rule, the complete corner deduction is

```
2*t(8)/d(8) + 3*t(12)/d(12) + 2*t(z)/d(z) + 3*t(b)/d(b).
```

If an exterior alias identifies two displayed boundary names, the coefficients
of that actual vertex are aggregated, while distinct face payments remain
distinct. The guard edge `z->8` lies outside this six-face disk; its two incident
faces are not silently added to the local ledger. No local reduction creates
charge or proves that a residual face is nonnegative.

## 7. Coverage and next source-state

The C40 parent matrix remains

```
10 structural + 24 unguarded + 22 guarded + 14 residual.
```

Under C44's first residual wheel, C45 adds the mutually exclusive child layer

```
endpoint a has degree four:
2 unconditional + 2 conditional;
if a conditional guard fails: 2 same-boundary interface obstructions.
```

This is not the quarantined parent refinement `10/35/11/14`. It does not alter
the other fourteen C44 residual wheels, the opposite endpoint `b`, the opposite
guard-face third vertex, higher-degree endpoints, S07's quotient-negative leaf,
S03's local DC2-R leaf, `L_join`, or B-family criticality.

The next source-faithful state is word 2 or 3 with actual `z->8`. The proved
interface obstruction directs the next search to a complete degree layer at
`z` or `b`, not another same-boundary gadget catalogue.

## 8. Reproduction and trust boundary

Run

```bash
python3 research/artifacts/candidates/opg169-a01-c45-replay.py audit
python3 research/artifacts/candidates/opg169-a01-c45-replay.py reproduce
```

The generator uses Kahn deletion and transitive closure; the separately written
consumer uses recursive DFS and BFS. Both were run with CPython 3.13.5 and
exited zero. They share one research principal, so this is differential
candidate control rather than independent verification.

`best_verified_result=none`; `root_closed=false`. No statement-faithfulness
receipt, Lean/axiom report, EvidenceLink, Result or Solution is supplied.
