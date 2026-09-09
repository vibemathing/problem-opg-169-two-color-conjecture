# C46 — guard-failure child with the fourth neighbour of degree four

**Verdict:** `candidate_only`  
**Base:** `23df7d6625eafed849c8654c504c23da32b37b3c` (merged C45).  
**Target:** `obligation:opg169-root`.

This candidate continues only the two C45 conditional words after their exact
reverse guard `z->8` is present, and only the subcase `d(z)=4`. One word violates
the known semidegree bound; the other is an oriented octahedral patch admitting
an unguarded one-vertex reduction. No other C44 residual or higher-degree
endpoint is treated.

## 1. Frozen guard-failure source

Use the six vertices

```
8, 12, a, b, u, z.
```

The common arcs from C45 are

```
8->12,
8->u, 12->u, u->a, u->b,
a->12, b->a, b->8,
a->z, z->b, z->8.
```

The two C45 words differ only on the edge `12-z`:

```
word 2: z->12,
word 3: 12->z.
```

Assume `d(z)=4`. Since its four displayed neighbours `a,b,8,12` are distinct,
this is its complete star.

## 2. Word 2 is structurally impossible

In word 2 the only incoming arc at `z` is `a->z`; the arcs from `z` go to
`12,b,8`. Thus

```
d-(z)=1, d+(z)=3.
```

This contradicts the previously proved minimum-counterexample condition
`d-(z),d+(z)>=2`. No replacement or colouring computation is needed for this
word.

## 3. Word 3 is an oriented octahedron

In word 3 the complete rotations can be written

```
u: (8,12,a,b),
a: (12,u,b,z),
z: (12,a,b,8).
```

The eight actual faces are

```
(u,8,12), (u,12,a), (u,a,b), (u,b,8),
(z,8,12), (z,12,a), (z,a,b), (z,b,8).
```

The underlying graph has all pairs among these six vertices except

```
u-z, 8-a, 12-b.
```

Hence it has twelve edges, the planar maximum `3*6-6`. In particular the edge
`12-b` is absent in the full original planar graph: adding it to this six-vertex
subgraph would give thirteen edges on six vertices, impossible for a simple
planar graph. This is a source-valid nonedge proof, not a guessed inverse-arc
guard.

The semidegrees of `z` are now two and two, so no structural contradiction is
available.

## 4. Unguarded strict reduction

Take the controlled set

```
I={u,a,z}
```

and retained boundary

```
B=(8,12,b).
```

Delete `a`. Its complete neighbour cycle is

```
(12,u,b,z),
```

so the deletion leaves an actual quadrilateral hole. Add the diagonal

```
12->b
```

inside that hole. The preceding planar edge count proves that neither direction
of the edge `12-b` existed in the original graph. Therefore this addition is
unguarded and cannot create a loop, parallel edge or digon. The whole smaller
graph has exactly one fewer vertex and remains finite, simple, planar and
oriented.

The exact table covers all complete colourings of the five-vertex smaller
patch. Sixteen are valid. Each has an original-patch lift with the same colours
on `8,12,b`; the colours of the surviving controlled vertices `u,z` may be
reassigned. For all sixteen entries,

```
R_P^+ = R_Q^+.
```

Thus no relation-only gap remains in this degree-four child.

## 5. Arbitrary-exterior lifting

Let `F` contain all vertices and arcs outside the saturated octahedral patch,
meeting it only at `B`. Every arc incident with the recoloured vertices `u,z`
and the deleted vertex `a` is listed because all three have complete degree-four
stars.

Take any valid colouring of the whole smaller graph. Restrict it to `Q`, choose
the saved lift, and keep every vertex outside `I` fixed. A new monochromatic
cycle wholly in the original patch or exterior is excluded by the table or the
smaller colouring. A crossing cycle splits at boundary visits. Replace every
positive original-patch segment by the same-colour `Q` path supplied by
`R_P^+ subseteq R_Q^+`; the unchanged exterior segments then give a positive
monochromatic closed walk in the smaller graph, hence a directed cycle. This is
impossible.

Therefore word 3 with `d(z)=4` cannot occur in a minimum-order counterexample.
Together with the semidegree contradiction for word 2,

```
C45 guard failure + d(z)=4  =>  no remaining word.
```

Equivalently, in the surviving C45 guard-failure source state a minimum
counterexample must satisfy

```
d(z)>=5.
```

## 6. Exact ledger

No payment rule changes. The three controlled degree-four vertices satisfy

```
gamma(u)=gamma(a)=gamma(z)=0,
t(u)=t(a)=t(z)=0.
```

Summing all eight actual octahedral faces gives

```
-8 + 4*gamma(8) + 4*gamma(12) + 4*gamma(b)
   + sum_{eight faces} h(f).
```

Relative to the old one-side payment rule, the full corner deduction over this
region is

```
4*t(8)/d(8) + 4*t(12)/d(12) + 4*t(b)/d(b).
```

The added edge `12->b` belongs only to the smaller minimality graph. It creates
no payment or charge in the original graph. Every actual original face keeps
its own `h(f)` receipt.

## 7. Coverage and next source-state

The C40 parent matrix remains `10/24/22/14`. Under C44's first residual and
C45's two guard-failure children, C46 gives

```
z has degree four:
word 2 -> structural semidegree contradiction,
word 3 -> unguarded strict profile reduction,
remaining -> 0.
```

This does not update the unverified `10/35/11/14` proposal. It does not treat
`d(z)>=5`, the opposite endpoint, the opposite guard side, the other fourteen
C44 residuals, S07's quotient-negative leaf, S03's local DC2-R leaf, `L_join`,
or B-family criticality.

The next source-faithful state is the same guard-failure child with `d(z)>=5`.
Its complete fan beyond the four known neighbours must be absorbed or converted
into a directed-return/degree-escalation argument.

## 8. Reproduction and trust boundary

Run the exact generator and independent consumer recorded in this candidate.
The selected CPython 3.13.5 runs exited zero. The generator uses Kahn deletion
and transitive closure; the consumer uses recursive DFS and BFS. They share one
research principal, so they are not an independent verifier.

`best_verified_result=none`; `root_closed=false`. No statement-faithfulness
receipt, Lean/axiom report, EvidenceLink, Result or Solution is supplied.
