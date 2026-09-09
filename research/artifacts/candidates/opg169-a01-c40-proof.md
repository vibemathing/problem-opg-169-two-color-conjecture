# C40 — D/19 high-port catalogue and first guarded layers

`verdict=candidate_only`; target `obligation:opg169-root`; base `adfb9b03f740c8033a40391f7398b2ac85cd0935`.
No candidate, computation, PR, CI, or merge below is Evidence or root closure.

## 1. Frozen scope

A valid colouring of a finite simple planar orientation makes both **full induced** colour classes acyclic. Boundary reachability is positive-length monochromatic reachability. A replacement must strictly reduce vertex number, preserve the contract, fix every exterior colour, and satisfy
\[
\sigma_P=\sigma_Q,\qquad R_P\subseteq R_Q
\]
for every valid complete colouring of the smaller local graph.

The D/19 core uses
```text
0→2,0→4,2→3,2→6,2→11,3→0,3→4,3→7,4→5,4→8,
5→0,5→6,6→0,7→2,7→8,8→3,11→6,11→7,
11→12,13→12,13→8,12→7,7→13.
```
The controlled set is `I={0,2,3,4,7}`. At vertex 4,
\[
\operatorname{rot}(4)=(0,5,q,r,8,3),
\]
with actual faces `(5,4,q),(q,4,r),(r,4,8)` and fixed directed face `4→5→q→4`. The word bits are: `q→r`, `r→8`, `r→4`; an unset bit reverses that arc.

Exact-name searches found no separately citable S02/S03/S11 artifact. Only independently checked content is used: ordinary extension is weaker than profile lifting; shortcut reverse arcs require explicit guards; C35's six arithmetic sign families do not prove geometric coverage.

## 2. Exact replacement catalogue

For each of C39's 70 compatible labelled types, choose one `v∈I`, delete it, and add any noncrossing oriented diagonal subset in its actual hole:
```text
0:(2,6,5,4,3)   2:(0,3,7,11,6)   3:(0,4,8,7,2)
4:(0,5,q,r,8,3) 7:(2,3,8,13,12,11).
```
Loops and opposite known arcs are rejected. If a new arc `a→b` has two retained endpoints, the rule carries the guard that the exterior has no `b→a`. No guard is inferred from planarity.

Every valid complete `Q` colouring is tested against every original internal colouring. A rule succeeds only with equal boundary colours, two acyclic induced classes, and complete `R_P⊆R_Q`. Every chosen rule removes one vertex; added arcs lie in the deletion hole. With its guards, the smaller graph is finite, simple, planar, and oriented.

For an arbitrary exterior, split any alleged new monochromatic cycle at interface visits and replace every `P` segment by the certified same-colour `Q` path. This creates a positive monochromatic closed walk in the originally valid smaller graph, hence a directed cycle. Thus the finite profile table lifts every exterior colouring; no finite exterior-path cutoff is used.

## 3. First relation-only row closed

For `(q,r,w)=(11,12,3)`, the added star arcs are
```text
5→11,11→4,11→12,12→8,4→12.
```
Delete 0 and add `6→4` inside hole `(2,6,5,4,3)`. Vertex 4 has a complete controlled star, so an unlisted exterior `4→6` cannot exist; the rule has no guard. All 194 valid complete `Q` colourings lift: 182 preserve `R` and 12 strictly decrease it.

The same unguarded shortcut handles all compatible `q=11` types: `11/12/{1,3,5,7}` and `11/new/{0,…,7}`.

## 4. Mutually exclusive coverage of the 70 types

| class | count | scope |
|---|---:|---|
| structural semidegree impossibility | 10 | an actual closed degree-four star has semidegree one |
| unguarded profile reduction | 24 | strict reduction, no exterior condition |
| guarded profile reduction | 22 | strict reduction when every listed reverse guard holds |
| catalogue residual | 14 | no rule in this exact one-deletion/hole-diagonal catalogue |

Structural rows:
```text
11/13/{2,3,6,7}; 12/13/{2,6}; new/13/{2,3,6,7}.
```
Their closed star at 8 has semidegree `(3,1)`; `12/13/6` also closes 13 with `(1,3)`.

Unguarded rows:
```text
11/12/{1,3,5,7}; 11/new/{0,1,2,3,4,5,6,7};
13/new/{1,3,4,6,7}; new/6/{3,4,5,6,7}; new/12/{3,7}.
```

Residual rows:
```text
12/new/{2,5}; 13/new/{2,5}; new/6/{2};
new/11/{2,4,5}; new/12/{2,4,5}; new/new/{2,4,5}.
```
Their catalogue sizes are
```text
523,523,461,461,421,473,473,473,461,461,461,523,523,523,
```
6,760 total. All return no strong-profile rule. This blocks only the stated catalogue, not arbitrary gadgets or larger interfaces.

The lossless audit archive stores all 70 rows, all 46 selected lift vectors, guards, and equal/strict counts.

## 5. First residual: degree-four outport absorption

Take residual `12/new/2`, with `q=12,r=15` and
```text
5→12,12→4,15→12,15→8,4→15.
```
Assume `d(15)=4`. Its fourth neighbour `z` lies in actual faces `(12,15,z),(z,15,8)`; semidegree at least two forces `z→15`. The remaining bits orient `z12,z8`.

Complete alias and rotation checks leave `z=5,13,new`. `z=6` has 31 edges on 12 vertices, above the planar maximum 30; `z=11` has inconsistent facial successors.

Seven compatible rows remain. Four with `z→8` reduce by deleting 15. Alias `z=5`, word 1, reduces by deleting 4 and adding `0→8,12→8`; the apparent guard edge `8→12` would itself violate the planar edge bound. For fresh `z` with `8→z`, deleting 4 and adding
\[
0\to8,\quad8\to5,\quad12\to8
\]
has complete lifts. The `5→8` reverse is impossible in the fixed embedding, but `8→12` is a genuine guard.

Hence this degree-four outport layer leaves only
\[
\boxed{z\text{ new},\quad8\to z\to15,\quad8\to12\text{ actual}.}
\]
After inserting `8→12`, the same complete catalogue finds no rule for either orientation of `z12`.

## 6. Fan-end audit inside that guard branch

Keep fresh `z`, `8→z`, and actual edge `8→12`.

If `d(13)=4`, let `a` be its fourth neighbour; semidegree forces `a→13`. Deleting 13 works whenever `a→8`. Survival therefore forces the directed triangle
\[
8\to a\to13\to8.
\]

If `d(z)=4`, let `b` be its fourth neighbour. According to the fixed orientation of `z12`, deleting `z` works in exactly the noncyclic half of the four fan directions. Survival forces one of
\[
12\to z\to b\to12,
\qquad
12\to b\to z\to12.
\]

When both endpoints are degree four and both forced triangles are cyclic, all eight combined directions have an ordinary nonextension in the tested bare-deletion family. No arbitrary replacement impossibility is claimed. This dual-fan cyclic layer is the first new open configuration.

## 7. Failure predicates

- `strong_profile`: every valid complete `Q` colouring has a same-boundary lift with `R_P⊆R_Q`;
- `ordinary_only`: ordinary same-boundary acyclic lifts exist, but some valid `Q` input has no relation-contained lift;
- `ordinary_failure`: some valid `Q` input has no same-boundary acyclic lift.

A relation-only witness is not a colouring obstruction. Ordinary extension alone is insufficient for arbitrary-exterior composition.

## 8. Full DC2 accounting

No transfer changes:
\[
\gamma(v)=\frac{d(v)-4-2t(v)}{d(v)},\qquad
\mu(f)=\ell(f)-4+\sum_{v\in f}\gamma(v)+h(f).
\]
Each marked pair receives one unit on each incident face, and every vertex sends `2t+dγ=d−4`.

The C39 sixteen controlled faces total
\[
-13+6g_7+6g_4+3g_5+3g_6+3g_{11}+4g_8
+2g_{12}+2g_{13}+2g_q+2g_r+\sum h.
\]
Relative to the old single-payment rule, all corner losses are
\[
t_7+t_4+3t_5/d_5+3t_6/d_6+3t_{11}/d_{11}+4t_8/d_8
+2t_{12}/d_{12}+2t_{13}/d_{13}+2t_q/d_q+2t_r/d_r.
\]

The outport eighteen-face layer totals
\[
-15+6g_4+6g_7+3g_5+3g_6+5g_8+3g_{11}+5g_{12}+2g_{13}+2g_z+\sum h,
\]
with losses
\[
t_4+t_7+3t_5/d_5+3t_6/d_6+5t_8/d_8+3t_{11}/d_{11}
+5t_{12}/d_{12}+2t_{13}/d_{13}+2t_z/d_z.
\]
Every `h` is the actual per-face receipt. Nothing here gives `residual=0` or a global charge contradiction.

## 9. Reproduction and trust boundary

`opg169-a01-c40-replay.py audit` decodes the frozen audit archive, verifies its size and SHA-256, runs the independent consumer, and checks the residual archive. The selected CPython 3.13.5 audit exited 0 with summary
```json
{"coverage":{"guarded_reduction":22,"residual":14,"structural_semidegree":10,"unguarded_reduction":24},"degree4_outport_rows":7,"fan13_rows":8,"fan14_rows":8,"rows":70,"selected_rules":46,"status":"ok"}
```
All 14 residual searches exited 0. `opg169-a01-c40-search.py` regenerates each output. Finite checks cover only the stated local domains.

The programs and tables share one generator trust domain. No Lean elaboration, axiom report, independent verifier acknowledgement, statement-faithfulness receipt, EvidenceLink, Result, or root closure exists.

## 10. Checkpoint

```text
checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
first_open_configuration: dual-fan cyclic guard branch, or a high-degree endpoint there
other_open_work: actual guard failures and the remaining 13 residual parent rows
next_obligation: obligation:opg169-root
root_closed: false
```
