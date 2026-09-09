# C47 — corrected C41 two-hole catalogue with at most one new point total

**Verdict:** `candidate_only`  
**Repository:** `vibemathing/problem-opg-169-two-color-conjecture`  
**Base:** `a0b2908f88ef017d6bd58e7fb006a2c7135589ec`  
**Target:** `obligation:opg169-root`

This candidate adds one bounded negative result to the already merged C43 canonical geometry. It does not repeat or replace C43's ordered-face repair, its 72 bare/diagonal cases, or the later C44--C46 guard-face and endpoint reductions.

## 1. Frozen source and lifting contract

The sole geometric source is the merged C43 file
`research/artifacts/candidates/opg169-a01-c43-c41-geometry.json`, Git blob
`4242925c0443c0e62e8565d00646cb12f1b1de8e`. Its corrected saturated fan-centre holes are

```
H13 = (7,8,16,12),
H14 = (8,15,12,17),
V(H13) intersect V(H14) = {8,12},
E(H13) intersect E(H14) = empty.
```

The already existing guard arc `8->12` is embedded outside both deletion-hole interiors. It is retained in the exterior and is not generated as a diagonal of either hole.

For an original patch `P`, a smaller patch `Q`, and retained boundary

```
B = (7,8,16,12,15,17),
```

a successful rule would require: for every valid **complete** two-colouring of `Q`, there is a valid colouring of `P` with the same boundary colours and

```
R_P^+ subseteq R_Q^+,
```

where `R^+` is the complete positive-length monochromatic reachability relation on `B`. Ordinary extension and relation containment are recorded separately.

## 2. Exact gadget class and completeness

The replacement deletes the two degree-four fan centres `13,14`. Each actual quadrilateral disk may contain no new point or one new point. The only possible boundary diagonal internal to `H13` is `7-16`; the other diagonal `8-12` is the fixed exterior guard edge. Similarly the only internal boundary diagonal of `H14` is `15-17`.

For either disk, the canonical catalogue has 171 simple plane oriented gadgets:

1. no new point: no diagonal, or either orientation of the unique allowed diagonal — 3 gadgets;
2. one new nonisolated point and no diagonal: each of its four possible spokes is absent, inward, or outward — `3^4-1=80` gadgets;
3. one new nonisolated point plus an oriented diagonal: the point lies in one of the two triangular sides and may have any nonempty oriented spoke subset to that side's three vertices; duplicate encodings are canonicalised — 88 further gadgets.

Thus each disk has `3+168=171` gadgets. An isolated new point is omitted without loss: deleting it preserves every boundary colour and boundary reachability and gives a strictly smaller replacement.

The original operation removes two vertices. Strict descent therefore permits at most one new internal point **in total**. The complete pair count per direction is

```
3*3 + 3*168 + 168*3 = 1017.
```

C43 freezes eight direction words. Hence this search checks exactly

```
8*1017 = 8136
```

source-valid, strictly smaller two-hole replacements. Every edge belongs to its owning disk; no cross-hole shortcut is admitted.

## 3. Exact finite result

The generator enumerates every valid complete `Q` colouring for every candidate pair and compares it against every valid original colouring with the same boundary word. A separate implementation regenerates the gadget catalogues, uses Kahn deletion for acyclicity and BFS for positive reachability, and recomputes all pair statuses.

The result is:

```
strong-profile pairs: 0
ordinary-only pairs:  0
ordinary-failure pairs: 8136
```

Every tested replacement has at least one boundary colouring with no ordinary extension to the original patch, so the failure occurs before the reachability-containment condition. The minimum numbers of failed valid smaller colourings are:

| C43 direction word | minimum failures |
|---:|---:|
| 0 | 8 |
| 1 | 4 |
| 2 | 6 |
| 3 | 4 |
| 4 | 8 |
| 5 | 6 |
| 6 | 6 |
| 7 | 6 |

The intersection of failed boundary words over all 1017 gadgets is empty for every direction. Therefore C42's former four-word obstruction is not transferred to the corrected geometry; the negative conclusion rests on the complete per-gadget certificate, not on a universal boundary word.

Canonical pair-status digest:

```
882314feee82b1c6583974643c56979efab4b00e9fa811f6991c2398d76fe4bd
```

## 4. Failed-route signature and exact non-claim

The frozen failed route is:

> Delete `13,14`; preserve the corrected two quadrilateral disks and the exterior guard arc `8->12`; place at most one new nonisolated point in total; add only simple oriented edges drawable in the owning disk. No member of this class has the universal strong-profile lifting property, for any of the eight C43 directions.

This does **not** exclude:

- two new points, which would not strictly reduce the vertex count;
- a replacement with different retained vertices or a larger absorbed interface;
- absorption of either face incident with the actual guard edge;
- gadgets using additional original vertices whose complete stars are controlled;
- any proof based on global criticality rather than this finite interface.

It is not a counterexample to the Two Color Conjecture.

## 5. Coverage and proof-DAG effect

The authoritative C40 parent partition remains

```
10 structural + 24 unguarded + 22 guarded + 14 catalogue residual.
```

C47 is a child statement under one residual and changes no parent count. At the corrected dual-fan child it strengthens the bounded negative knowledge from C43's 72 no-point/diagonal choices to all 8136 strictly smaller choices with at most one new internal point total:

```
corrected two-hole class: 0 reduced / 8 residual directions.
```

C44--C46 already take the productive route of absorbing the actual guard-edge faces and then complete endpoint stars. They remain the active forward branch. The unverified `10/35/11/14` refinement is not adopted; the reported merged-{0,2} quotient failures remain a scoped negative handoff; the single-high-endpoint `DC2-R` transfer remains a local ledger leaf. None closes `L_join` or the B-family criticality bridge.

## 6. Reproduction and trust boundary

Run from the repository root:

```bash
python3 research/artifacts/candidates/opg169-a01-c47-unpack.py audit
python3 research/artifacts/candidates/opg169-a01-c47-unpack.py reproduce
```

The capsule losslessly stores the exact generator, complete output, independently coded Kahn/BFS consumer, execution record and review request. `reproduce` extracts them to a temporary directory, regenerates the 8,136-pair output and reruns the consumer.

Selected runs used CPython 3.13.5, one process, a 512 MiB address-space cap and a 30-second CPU cap. The generator and audit exited zero with empty stderr. They are two implementations under one generating principal, not independent trusted verification. No Lean elaboration, axiom report, statement-faithfulness receipt, EvidenceLink, Result, Solution, residual-zero, global charge contradiction, or root closure is supplied.

`best_verified_result=none`; `root_closed=false`.
