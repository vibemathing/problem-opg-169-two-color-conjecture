# C44 — source-faithful degree-four guard-face wheel

**Verdict:** `candidate_only`  
**Base:** `0a1df320d4d3f524a35e0609cbf10ec220a09dd8` (merged C43).  
**Target:** `obligation:opg169-root`.

This candidate starts from C43's first genuine guard-edge source-state. It treats
one third vertex of the actual edge `8->12` when that third vertex has complete
underlying degree four. It neither closes the other guard side nor changes the
C40 parent partition.

## 1. Frozen local object

Let `u` be the third vertex of one triangular face incident with the edge
`8-12`. If `d(u)=4`, write the complete cyclic neighbour order as

```
(8,12,a,b).
```

The four neighbours are distinct because the underlying graph is simple. The
four actual facial triangles are

```
(u,8,12), (u,12,a), (u,a,b), (u,b,8).
```

The edge `8->12` is fixed. The other three rim edges and the four spokes are
oriented arbitrarily subject to the already established semidegree condition
`d-(u),d+(u)>=2`. Since `d(u)=4`, exactly two spokes enter `u` and two leave it.
Thus there are exactly

```
C(4,2) * 2^3 = 48
```

labelled orientation types. No direction or degree condition is imposed on the
four retained neighbours beyond the displayed actual edges.

The local patch `P` consists of this saturated wheel. Its boundary order is
`B=(8,12,a,b)`. Every edge incident with `u` is listed, so deleting or recolouring
`u` cannot affect an unrecorded exterior arc.

## 2. Exact replacement catalogue

Delete `u`. Its four incident faces form an actual quadrilateral hole with rim
`(8,12,a,b)`. The only possible new underlying diagonals in that disk are
`8-a` and `12-b`; planarity permits at most one. The catalogue is

```
Q0: no added diagonal,
Q1/Q2: 8->a or a->8,
Q3/Q4: 12->b or b->12.
```

A new directed diagonal `x->y` is usable only when the original graph has no
reverse arc `y->x`. If `x->y` already exists on the exterior side, no duplicate
copy is inserted; that existing edge is retained once. Thus the recorded guard
is exactly the reverse direction, not an assumption that the pair was
nonadjacent.

For every valid complete colouring of a candidate `Q`, the table asks for a
colour of `u` such that both full induced colour classes in `P` are acyclic,
the four boundary colours agree, and

```
R_P^+ subseteq R_Q^+.
```

`R^+` contains every positive monochromatic directed path between boundary
vertices. Because `Q` has no internal vertex, all sixteen boundary assignments
are the complete `Q` colouring domain; invalid assignments are retained as
invalid rather than silently discarded.

## 3. Complete child classification

The exact result is

| class | types | meaning |
|---|---:|---|
| unconditional | 9 | bare induced deletion `Q0` has a strong-profile lift |
| conditional | 24 | one listed diagonal has a strong-profile lift when its reverse guard is absent |
| residual | 15 | none of the five catalogue members has a strong-profile lift |

Across the 33 positive orientation types, the selected rules contain 496 valid
complete `Q` colourings, each with an explicit centre colour. The lossless compressed table archive stores the full selected map and all
candidate summaries, not only aggregate counts. Its decoded SHA-256 is checked
before replay.

The fifteen residual types are not featureless. Counting the four actual faces
incident with `u`, their numbers of directed triangular faces are

```
2 directed triangles: 10 types
3 directed triangles:  4 types
4 directed triangles:  1 type.
```

Every residual therefore has at least two directed incident faces. This is a
structural child condition, not a proof that such a wheel is impossible.

The result applies to either incident side of `8->12` by relabelling the four
boundary positions. It does not identify the two sides, and it does not assume
the two third vertices are distinct from all other retained vertices beyond the
simplicity conditions required by the complete star under consideration.

## 4. Arbitrary-exterior lifting

Take one positive rule and form the whole smaller graph by deleting `u` and,
when needed, adding the selected diagonal subject to its reverse guard. The
operation removes one vertex. A new diagonal is drawn inside the actual
quadrilateral hole; if the same directed edge already exists, the graph simply
retains that edge once. Hence the smaller graph is finite, simple, planar and
oriented.

Fix any valid colouring of the whole smaller graph. Restrict it to `Q` and use
the table to colour `u`, leaving every other vertex unchanged. A new
monochromatic cycle cannot lie wholly in the exterior or wholly in `P`. If it
crosses the interface, cut it at successive vertices of `B`. Each positive
`P` segment has the same-colour endpoints and belongs to `R_P^+`; containment
supplies a `Q` path with the same endpoints. Replacing every local segment gives
a positive monochromatic closed walk in the originally valid smaller graph,
which contains a directed cycle. This contradiction proves the lift for every
exterior, not only for direct boundary chords.

Consequently the nine unconditional child types cannot occur in a
minimum-order counterexample. Each of the twenty-four conditional child types
cannot occur when its exact reverse guard is absent. A failed guard is a new
source-valid child and is not counted as a reduction.

## 5. Geometry, aliases and pressure tests

The proof uses the actual union of all four faces at `u`; the local boundary is
not C42's obsolete one-terminal lobe. The four rim vertices are distinct, but
`a` or `b` may coincide with another previously named vertex outside this
five-vertex patch. Such an alias remains a boundary vertex and does not alter
the complete-star lift. Its pre-existing arcs remain exterior, and any reverse
arc against a proposed diagonal is caught by the guard.

Pressure checks retained in the table and independent consumer include:

1. all 48 spoke/rim direction types;
2. all five smaller candidates per compatible type;
3. all sixteen complete smaller colourings;
4. ordinary nonextension separated from relation-only failure;
5. positive rather than reflexive reachability;
6. full arc reversal and side relabelling as theorem symmetries, not extra
   parent counts;
7. exact one-vertex order decrease;
8. no use of minimum semidegree in the smaller graph.

The finite classification verifies this fixed wheel only. It is not a finite
proof of the root conjecture and does not settle a degree-five or higher third
vertex.

## 6. Full double-payment ledger

No charge rule changes. On the original graph

```
gamma(x)=(d(x)-4-2t(x))/d(x),
mu(f)=|f|-4 + sum_corner gamma + h(f).
```

A degree-four third vertex is not a donor in this rule, so `t(u)=0` and
`gamma(u)=0`. The exact sum over its four incident triangular faces is

```
-4 + 2*gamma(8)+2*gamma(12)+2*gamma(a)+2*gamma(b)
   + h(u,8,12)+h(u,12,a)+h(u,a,b)+h(u,b,8).
```

Starting from C43's 24-face region (the corrected 22 faces plus both faces of
edge `8-12`), absorbing the rest of the `u` star adds the three rows

```
-3 + gamma(8)+gamma(12)+2*gamma(a)+2*gamma(b)
   + h(u,12,a)+h(u,a,b)+h(u,b,8).
```

Relative to the old one-side payment rule, the complete four-face corner loss
is

```
2*t(8)/d(8)+2*t(12)/d(12)+2*t(a)/d(a)+2*t(b)/d(b),
```

while every actual new unit receipt remains in its own `h(f)`. No positive face
from an older ledger is reused without these deductions. The reductions remove
configurations from a hypothetical minimum counterexample; they do not create
charge or imply that the remaining residual faces are nonnegative.

## 7. Coverage and proof-DAG update

The canonical C40 parent identity remains

```
10 structural + 24 unguarded + 22 guarded + 14 residual.
```

C44 adds a child matrix under C43's guard-face fresh-state:

```
degree-four third vertex:
9 unconditional + 24 conditional + 15 residual = 48.
```

This child matrix is not the proposed S10 parent refinement
`10/35/11/14`. That proposal still requires per-parent rotation-compatible
nonplanarity certificates. The S07 quotient negative and S03 one-high-endpoint
DC2-R transfer remain non-closing candidate leaves. `L_join`, B-family
criticality, the opposite guard side, all higher-degree third vertices, the
other thirteen C40 residual parents and all unprocessed guard-failure children
remain open.

## 8. Reproduction and trust boundary

Run

```bash
python3 research/artifacts/candidates/opg169-a01-c44-replay.py audit
python3 research/artifacts/candidates/opg169-a01-c44-replay.py reproduce
```

The selected execution used CPython 3.13.5. The generator uses Kahn deletion
and transitive closure; the separate consumer uses recursive DFS and BFS and
does not import generator predicates. Both exited zero. They are still written
and run by one principal, so this is differential candidate control, not an
independent verifier receipt.

`best_verified_result=none`; `root_closed=false`. The next executable source
state is either the first residual wheel with two directed incident faces, or
a conditional wheel whose actual reverse guard is present. No
statement-faithfulness, Lean/axiom, EvidenceLink, Result or Solution admission
is supplied.
