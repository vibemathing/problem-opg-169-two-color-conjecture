# C42 — dual-fan bounded obstruction and first guard-face child layer

**Verdict:** `candidate_only`  
**Base:** `dc6ee891ed7614602e88d48a57314416082dd022` (merged C40).  
**Target:** `obligation:opg169-root`.

This candidate treats one descendant of the first C40 catalogue residual. It does not alter the parent identity
`70 = 10 structural + 24 unguarded + 22 guarded + 14 residual`, close another parent, or close the root.
The complete proof, programs, inputs and outputs are losslessly stored in the split capsule named below.

## 1. Strong lifting contract

For an original patch `P`, smaller patch `Q`, and retained boundary `B`, every valid **complete** colouring of `Q` must have a valid colouring of `P` with identical boundary colours and
`R_P^+ ⊆ R_Q^+`, where `R^+` is all positive monochromatic boundary reachability. Exterior colours remain fixed. This is stronger than ordinary same-boundary extension. All failure tables distinguish ordinary nonextension from relation-only failure.

## 2. Corrected plane object

Controlled vertices are `{0,2,3,4,7,13,14,15}` and boundary order is `(5,6,8,11,12,16,17)`. The corrected fan-14 faces are
`(12,14,17)` and `(17,14,8)`, not `(8,14,17)` and `(17,14,12)`. The old pair conflicts with the already fixed faces at successors `8→15/17` around 14 and `14→15/17` around 12. The corrected rotation is
`14:(15,12,17,8)`.

The 22 controlled faces, full arcs and eight directions are frozen in the capsule input. Their boundary complex consists of quadrilateral lobes
`A=(5,6,11,12)` and `B=(8,16,12,17)`, meeting only at 12. The actual guard-failure arc `8→12` is retained outside the B-lobe disk.

## 3. Complete bounded two-lobe decision

Lobe A permits either no diagonal or one oriented diagonal among `5-11,6-12`, plus at most one internal point and arbitrary oriented spokes, subject to disk planarity. It has 261 canonical oriented gadgets. Lobe B analogously permits the local diagonal `16-17`, at most one internal point and spokes; `8→12` remains exterior. It has 171 gadgets.

Two separately coded exact implementations checked all
`261×171×8 = 357,048` gadget/direction pairs and every valid complete `Q` colouring. No strong-profile replacement exists.

The common failed boundary words, in order `(5,6,8,11,12,16,17)`, are
`22,54,73,105`. Equivalently, for a colour `a`,
`c5=c11=c17=a`, `c6=c8=c12=1-a`, and `c16` is arbitrary.

For `a=0`, fixed directed triangles force
`c4=0` via `4→8→12→4`, then `c0=1` via `0→4→5→0`, then `c2=0` via `0→2→6→0`, then `c7=1` via `2→11→7→2`; finally `7→8→12→7` is monochromatic. Hence the original patch has no ordinary extension. Colour complementation handles the other words.

Each bounded replacement admits every such word. In lobe A the alternating rim makes the two possible monochromatic obstructions require both crossing diagonals, impossible in one disk. In lobe B, a suitable colour for the optional point avoids a cycle; simultaneous blocking would require a separating `16-17` diagonal and spokes crossing it. A simple cycle cannot use both lobes because they meet only at 12. Thus the zero-hit catalogue has an analytic ordinary-extension obstruction, not only a finite search result.

Exact scope: this refutes only two local quadrilateral gadgets with at most one new internal point per lobe. Larger lobes, changed interfaces and more absorbed exterior faces remain open.

## 4. Guard-edge face absorption

The corrected rotations put the guard edge `8-12` between fan endpoints 16 and 17. Adding at most one optional point in either or both immediate guard-side triangular regions still admits all four obstruction words; all 27 oriented spoke states per side were checked. Therefore one-point face absorption does not change the decisive boundary precolouring.

If an immediate third-face vertex has degree four, normalize its facial neighbour cycle as `(8,12,u,v)` with fixed `8→12` and semidegree two. The exact 48-star table, using literal deletion and at most one local diagonal `8u` or `12v`, splits as
`9 unguarded + 24 guarded + 15 residual`. Every residual has at least two directed incident facial triangles (distribution 10/4/1 for two/three/four). Guarded rows apply only when every recorded reverse arc is absent in the original graph. This is a conditional child layer, not an addition to the parent count 70.

## 5. Corrected 22-face ledger

No transfer changes. On the original graph
`γ(v)=(d(v)-4-2t(v))/d(v)` and `μ(f)=|f|-4+Σ_corner γ+h(f)`.
The corrected face multiplicities are
`0:5,2:5,3:5,4:6,5:3,6:3,7:6,8:7,11:3,12:7,13:4,14:4,15:4,16:2,17:2`.
Thus the controlled total is
`-19+6γ4+6γ7+3γ5+3γ6+7γ8+3γ11+7γ12+4γ13+4γ14+2γ16+2γ17+Σh`.
Relative to the old one-side rule, all corner losses are
`t4+t7+3t5/d5+3t6/d6+7t8/d8+3t11/d11+7t12/d12+4t13/d13+4t14/d14+2t16/d16+2t17/d17`.
Every actual face receipt remains in its own `h(f)`. The corrected face provenance changes which actual faces receive payments but creates no new money. No residual-zero or global contradiction follows.

## 6. Coverage and next obligation

C40 remains `10/24/22/14`. Under one residual parent, C42 has eight dual-fan direction children; all remain residual in the bounded two-lobe class, with the same four-word obstruction. The conditional degree-four guard-face layer is `9/24/15`. The other thirteen residual parents, all twenty-two guard-failure children, higher-degree guard-face vertices, `L_join`, and any B-family criticality bridge remain independent.

The capsule audit/reproduce commands are:
```bash
python3 research/artifacts/candidates/opg169-a01-c42-unpack.py audit
python3 research/artifacts/candidates/opg169-a01-c42-unpack.py reproduce
```
The capsule contains 18 exact files, including the long proof, C++ generator/consumer, Python pressure tests, canonical inputs, execution records, coverage and ledger. Same-principal implementations are research controls, not trusted verification.

`best_verified_result=none`; `root_closed=false`. The next route is to absorb a complete degree-four guard-face star and map all aliases/guards, then follow residual directed facial triangles or the first higher-degree third-face star. No statement-faithfulness, independent verifier, Lean/axiom, EvidenceLink, Result or Solution admission is supplied.
