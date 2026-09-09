# C43 — canonical C41 geometry recovery and corrected source-state

**Verdict:** `candidate_only`  
**Repository:** `vibemathing/problem-opg-169-two-color-conjecture`  
**Base revision:** `dc6ee891ed7614602e88d48a57314416082dd022`  
**Target:** `obligation:opg169-root`

This candidate repairs the source geometry below the first C40 residual. It does
not close that residual, another C40 parent, the discharging join, or the root.

## 1. Transport identity and quarantine

Fresh repository state at the beginning of this cycle:

- `main = dc6ee891ed7614602e88d48a57314416082dd022`;
- Issue `#3` is the unique open `web-research-question`;
- `research/records/failed-routes.jsonl` is empty;
- there is no open pull request;
- an incomplete branch
  `web/attempt-opg169-a01-c42-dual-fan-20260910` exists at
  `b56521ec411d705450d3e375f4234a25799c9737`, seven commits ahead of the
  base, with no Web attempt packet and no PR.

That partial C42 branch is source material, not an admitted candidate
transaction. Its proof index correctly notices one ordered-face repair, but
then conflates two different pairs of regions. The branch is therefore
quarantined and is not merged or relabelled as a mathematical failed route.

The transport fingerprint is the SHA-256 of the repository, base, Issue,
partial branch/head and canonical geometry digest:

`64d35f5fb4aaf8976335664222fd3b35af5941b44f0709b7a0658765f2785657`.

## 2. Canonical ordered faces

The controlled vertices are
`{0,2,3,4,7,13,14,15}` and the retained vertices are
`{5,6,8,11,12,16,17}`. The canonical input records all fixed arcs, the three
direction bits giving eight orientations, and these 22 ordered triangular
faces:

```
(0,2,3) (0,6,2) (0,5,6) (0,4,5) (0,3,4)
(2,7,3) (2,11,7) (2,6,11) (3,8,4) (3,7,8)
(8,7,13) (13,7,12) (12,7,11)
(5,4,12) (12,4,15) (15,4,8)
(12,15,14) (14,15,8)
(8,13,16) (16,13,12)
(12,14,17) (17,14,8)
```

The previously used final two ordered faces were

```
(8,14,17), (17,14,12).
```

They preserve the same two *unordered* triangular faces but are incompatible
with the preceding ordered faces:

```
succ_14(8)=15  and succ_14(8)=17,
succ_12(14)=15 and succ_12(14)=17.
```

Replacing them by

```
(12,14,17), (17,14,8)
```

removes both conflicts. The complete controlled rotations, up to cyclic
shift, are then

```
0:  (2,6,5,4,3)
2:  (0,3,7,11,6)
3:  (0,4,8,7,2)
4:  (0,5,12,15,8,3)
7:  (2,3,8,13,12,11)
13: (7,8,16,12)
14: (8,15,12,17)
15: (4,12,14,8)
```

For every one of the eight direction words the arc set is a simple
orientation of the same 38-edge underlying graph, every listed ordered face
uses actual edges, and vertices `13,14,15` have both semidegrees at least two.

Two separately coded exact checkers recover the rotations by different
methods: successor maps, and link multiplicities plus directed face wedges.
Both accept the canonical input and reject the old face order with exactly the
two conflicts above.

## 3. The two region notions must not be identified

Deleting the fan centre `13` gives the actual quadrilateral hole

```
H13=(7,8,16,12).
```

Deleting `14` gives

```
H14=(8,15,12,17).
```

Therefore

\[
V(H_{13})\cap V(H_{14})=\{8,12\}.
\]

The old one-terminal pinch statement, under which every path between the two
fan holes had to pass through `12`, is false for this geometry: a path can
communicate through either `8` or `12`.

There is a different fact. The union of the 22 listed faces has two oriented
boundary walks

```
A=(5,6,11,12),   B=(12,16,8,17),
```

which meet only at `12`. The 22-face complex uses 15 vertices, 37 face-edges
and 22 faces, hence has Euler characteristic zero. The guard edge `8-12` is
the 38th graph edge but is incident with none of these 22 faces.

The boundary walks `A,B` are not the individual deletion holes `H13,H14`.
No proof has been supplied that gadgets drawn in the complementary regions
bounded by `A,B` are replacements drawn inside the region removed from the
original graph. Consequently the partial C42 product count `261*171*8` and
its infinite one-point pinch extrapolation are quarantined. They are neither
accepted results nor authoritative failed routes.

A source-faithful replacement using both fan holes is a **two-terminal**
composition problem with separator `{8,12}`. Its state must permit paths and
cycles alternating through both terminals; independent one-terminal lobe
profiles are insufficient.

## 4. Corrected bounded two-hole baseline

As a cheapest corrected control, delete `13` and `14` and permit at most one
local diagonal in each actual quadrilateral hole.

- In `H13` the only new underlying diagonal is `7-16`, with choices
  `none`, `7->16`, `16->7`.
- In `H14` the only new underlying diagonal is `15-17`, with choices
  `none`, `15->17`, `17->15`.
- The edge `8->12` already exists with a fixed embedding outside these two
  controlled hole interiors; it is not redrawn as a parallel hole diagonal.

Thus there are `8*3*3=72` exact cases. For each case the complete smaller
colourings are checked. A lift must retain every boundary colour and satisfy

\[
R_P^+\subseteq R_Q^+
\]

for both colours, with positive reachability on boundary order
`(5,6,8,11,12,16,17)`.

A C++ bit-closure generator and an independently coded Python DFS/BFS consumer
agree on all 72 rows. There is no strong-profile rule in this bounded class.
The best rows still have both ordinary and relation-only failures:

| direction | best local diagonals `(H13,H14)` | valid Q | failures | ordinary | relation-only |
|---:|---|---:|---:|---:|---:|
| 0 | `(16->7,17->15)` | 442 | 62 | 20 | 42 |
| 1 | `(16->7,none)` | 636 | 72 | 24 | 48 |
| 2 | `(16->7,17->15)` | 442 | 62 | 20 | 42 |
| 3 | `(16->7,none)` | 636 | 72 | 24 | 48 |
| 4 | `(16->7,17->15)` | 386 | 36 | 20 | 16 |
| 5 | `(16->7,17->15)` | 444 | 46 | 24 | 22 |
| 6 | `(16->7,17->15)` | 386 | 36 | 20 | 16 |
| 7 | `(16->7,17->15)` | 444 | 46 | 24 | 22 |

This is a new bounded failed-route signature only:

```
FR-C43-CORRECTED-TWO-HOLE-DIAGONALS
delete {13,14}; add at most one legal diagonal in each actual hole;
72 cases; zero strong-profile rules.
```

It does not exclude internal gadgets, changed interfaces, guard-face
absorption, or a joint two-terminal replacement.

## 5. First source-faithful guard-face state

The selected root representative may be chosen among minimum-order
counterexamples to maximize its number of underlying edges. If its underlying
graph were not edge-maximal planar, add a planar missing edge and orient it
arbitrarily. Any valid colouring of the supergraph would restrict to one of
the original graph, so the supergraph would remain a counterexample on the
same vertices, contradicting the choice. Thus the selected underlying graph
is maximal planar. Since the already proved candidate bound gives minimum
degree at least four, it has at least five vertices; the standard maximal
planar theorem gives 3-connectivity.

This removes global cut-vertex and 2-cut branches for the selected
representative. It does not remove separating triangles. Edge saturation also
does not imply arc-criticality: deleting an existing arc is the opposite
operation and need not produce a colourable graph.

Because `8-12` is an edge in this maximal plane graph, its two incident faces
are triangles. Orient the facial walks as

```
(u,8,12), (12,8,v).
```

The 22-face rotations and the complete stars already known give an exact
alias classification.

For the first face, the only old vertex that can be `u` is `11`; otherwise
`u` is fresh. For the second, the only old vertex that can be `v` is `5`;
otherwise `v` is fresh. The apparent single-side aliases `u=6` and `v=6`
already give 15 vertices and 40 distinct edges, exceeding the planar bound
39. All other old aliases are rejected by an ordered-rotation conflict,
overflow of a complete controlled star, a closed degree-three link, or use of
an endpoint of the edge itself.

Combining the two sides, the sole old-old possibility `(u,v)=(11,5)` gives
15 vertices and 40 edges and is also impossible. Exactly three labelled alias
classes survive:

```
(u,v)=(11,new_v),
(u,v)=(new_u,5),
(u,v)=(new_u,new_v).
```

No direction or degree assumption on the fresh vertices has yet been added.
The first genuine open source-state is the fresh-fresh class. Its next exact
subproblem is to freeze the four incident arc directions, then process a
complete degree-four star on one third vertex before any higher-degree
escalation.

## 6. Corrected charge ledger

For each original face,

\[
\mu(f)=|f|-4+\sum_{x\in f}\gamma(x)+h(f),
\qquad
\gamma(x)=\frac{d(x)-4-2t(x)}{d(x)}.
\]

The two geometry implementations independently recover these 22-face corner
multiplicities:

```
0:5, 2:5, 3:5, 4:6, 5:3, 6:3, 7:6, 8:7,
11:3, 12:7, 13:4, 14:4, 15:4, 16:2, 17:2.
```

Therefore the raw sum over all 22 triangular faces is

\[
\begin{aligned}
-22
&+5\gamma_0+5\gamma_2+5\gamma_3+6\gamma_4+3\gamma_5+3\gamma_6
 +6\gamma_7+7\gamma_8+3\gamma_{11}+7\gamma_{12}\\
&+4\gamma_{13}+4\gamma_{14}+4\gamma_{15}
 +2\gamma_{16}+2\gamma_{17}
 +\sum_{f\in F_{22}}h(f).
\end{aligned}
\]

In the frozen layer `d(0)=d(2)=d(3)=5,t=0`, contributing three units in total,
and `gamma_13=gamma_14=gamma_15=0`. After those substitutions this becomes

\[
-19+6\gamma_4+3\gamma_5+3\gamma_6+6\gamma_7+7\gamma_8
+3\gamma_{11}+7\gamma_{12}+2\gamma_{16}+2\gamma_{17}
+\sum_{F_{22}}h(f).
\]

Thus the legacy `-19` constant comes from the three degree-five **corner
contributions**, not from three unnamed payments. Every payment remains in
its own `h(f)`. C43 corrects the provenance while preserving the final
algebraic value.

Absorbing the two guard-edge faces adds exactly

\[
-2+2\gamma_8+2\gamma_{12}+\gamma_u+\gamma_v
+h(u,8,12)+h(12,8,v).
\]

If an alias is present, repeated coefficients are aggregated for the same
vertex, while the two actual face receipts remain distinct. No payment rule is
changed and no local exclusion creates charge.

## 7. Proof-DAG integration of specialist handoffs

The following nodes are kept distinct.

```
NF
  selected minimum-order / maximum-edge counterexample
  -> maximal planar -> 3-connected
  -> global 1-cut and 2-cut branches removed
  -> separating triangles remain

GEO
  canonical 22 ordered faces
  -> corrected rotations
  -> H13 intersect H14 = {8,12}
  -> old one-terminal pinch claim removed

CAT
  corrected 72-case two-hole diagonal catalogue
  -> bounded zero-hit only

GF
  guard edge 8-12 has two external incident faces
  -> exactly three alias classes
  -> fresh-fresh is first open source-state
```

The proposed S10 parent refinement

```
10 structural + 35 unconditional + 11 conditional + 14 residual
```

is not adopted. The canonical C40 parent partition remains

```
10 structural + 24 unguarded + 22 guarded + 14 residual.
```

Promotion requires a per-parent nonplanarity/Kuratowski witness compatible
with the original rotation, plus the same complete-Q lifting audit.

The S07 handoff that the merged `{0,2}` quotient fails residuals `#6-#9`
(all 16 orientations; `#6/#9` ordinary and `#7/#8` relation-only) is stored as
a candidate negative leaf only. No citable statement digest was present in
current main or Issue state, so it is not used to close any parent and no S06
positive rule is imported.

The S03 single-high-endpoint transfer is stored only as a local DC2-R leaf.
Negative-charge migration, nonduplicate global composition and `L_join`
remain unproved.

## 8. Remaining join gaps

The first geometric source-state is `C43-GUARD-FACE-FRESH-FRESH`. The first
global join gap is still:

```
a local reduction/transfer for one signed cell
    does not imply
a mutually exclusive, globally conserved cover of every negative face.
```

In particular, B-family criticality and `L_join` remain independent root
obligations. The corrected geometry neither changes the 70-parent identity
nor closes the other 13 C40 residual parents or any unprocessed guard-failure
child.

## 9. Reproduction and limits

The direct repository replay entry point is:

```bash
python3 research/artifacts/candidates/opg169-a01-c43-unpack.py audit
python3 research/artifacts/candidates/opg169-a01-c43-unpack.py reproduce
```

`audit` verifies the compressed file map and every inner SHA-256. `reproduce`
extracts to a temporary directory, runs both geometry implementations, compiles
and runs the C++ corrected-hole generator, and runs the separate Python
DFS/BFS consumer against all 72 rows.

The selected executions used CPython 3.13.5 and g++ 14.2.0 and exited zero
under explicit timeouts. The two geometry implementations and the two
two-hole implementations were written by the same principal; they are
differential research controls, not independent verification.

No Lean elaboration, axiom report, statement-faithfulness receipt,
EvidenceLink, Result or Solution admission is supplied.

```text
checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
canonical_parent_coverage: 10/24/22/14
corrected_two_hole_successes: 0 of 72 in the stated bounded class
first_open_source_state: C43-GUARD-FACE-FRESH-FRESH
next_route: degree-four complete-star absorption at one fresh guard-face third vertex,
            with all aliases, directions, reverse guards, full-Q profile and 24-face ledger
root_closed: false
```
