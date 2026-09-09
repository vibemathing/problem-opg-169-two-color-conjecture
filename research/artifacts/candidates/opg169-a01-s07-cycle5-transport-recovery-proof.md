# S07 Cycle 5 — transport recovery: merged-{0,2} and saturated high-port wheel

`verdict=candidate_only`  
`transport_base=23df7d6625eafed849c8654c504c23da32b37b3c` (merged C45)  
`mathematical_source_base=dc6ee891ed7614602e88d48a57314416082dd022` (merged C40)  
`target=obligation:opg169-root`  
`root_closed=false`

## 1. Recovery scope and current-state drift audit

This transaction gives stable repository locators and digests to two S07
negative leaves that previously existed only as session artifacts:

1. Cycle 3: all four simple-orientation variants of the plane-edge quotient
   merging `0` and `2`, on each of C40 residual parents #6–#9;
2. Cycle 4: a fresh degree-six saturated `q=14` wheel child for each parent,
   with every one-controlled-vertex deletion and every source-valid
   noncrossing oriented diagonal subset in the actual deletion hole.

Current main has advanced through C43, C44, and C45. Those candidates repair and
then analyse the C41 guard-edge `8->12` branch. They do not edit the C40 D/19
core, the stable fourteen-residual ordering, or the four parent identities
used here. Current C43 explicitly records the Cycle-3 conclusion only as an
uncitable S07 chat leaf; this recovery supplies the missing frozen bytes.
C44 and C45 are child analyses on the separate guard-edge source-state: C45 absorbs one degree-four endpoint of the first C44 residual. Neither changes the C40 parent arcs, ordering, or coverage used here. Hence the computations retain source revision
`dc6ee891ed7614602e88d48a57314416082dd022`, while this transport is based on `23df7d6625eafed849c8654c504c23da32b37b3c`.

Canonical owned parents remain:

```text
#6 new/11/2
#7 new/11/4
#8 new/11/5
#9 new/12/2
```

No result below modifies the canonical C40 partition `10/24/22/14`. C45 treats a C44 guard-face endpoint and is disjoint from the four C40 residual parents recovered here.

## 2. Frozen lifting contract

A valid binary colouring makes both full induced colour classes acyclic.
Boundary reachability is positive-length monochromatic reachability. For every
valid complete colouring of a strictly smaller simple plane orientation `Q`,
a rule needs a same-boundary colouring of the original patch `P` satisfying

`R_P^+ subseteq R_Q^+`.

This is the quantifier required for arbitrary exterior gluing. Ordinary
same-boundary extension alone is insufficient. Every added retained shortcut
carries its literal reverse-arc guard; no guard is inferred from planarity.

## 3. Cycle 3: merged-{0,2} quotient is not a rule

Contract the actual plane edge `0->2` to `m`, delete the loop, and choose one
direction from each inherited antiparallel pair at common neighbours `3,6`.
The four variants are

```text
m->3,m->6;  m->3,6->m;  3->m,m->6;  3->m,6->m.
```

Each Q has 11 vertices and 25 arcs, with
`rot(m)=(6,5,4,3,7,11)` up to cyclic shift and boundary
`B=(5,6,8,11,12,13,14)`.

All sixteen parent/variant rules fail:

| parent | valid P | valid Q across four variants | failures per variant |
|---|---:|---:|---:|
| #6 | 372 | 324/258/336/288 | 14 = 2 ordinary + 12 relation-only |
| #7 | 378 | 312/246/336/270 | 12 relation-only |
| #8 | 378 | 312/246/336/270 | 12 relation-only |
| #9 | 394 | 316/252/336/284 | 12 = 8 ordinary + 4 relation-only |

The common valid Q mask `86`, in order
`(3,4,5,6,7,8,11,12,13,14,m)`, has colour-one set `{4,5,7,11}`.
For #6–#8 its unique P extension creates `14->4->8`, absent from every Q
relation. For #9 the same boundary has no P extension: the four directed
triangles force `4=7=0=1` and `2=0`, after which `0->4->5->0` is monochromatic.

Two separately coded acyclicity/reachability routines agree on 49,152 complete
P/Q colourings. Across all sixteen rules there are 4,722 valid Q colourings;
4,522 pass and 200 fail, split as 40 ordinary and 160 relation-only.

## 4. Cycle 4: saturated degree-six high-port wheel remains open

For each parent add fresh vertices `20,21,22` and freeze

`rot(14)=(5,4,r,20,21,22)`

with common new arcs

```text
14->20, 21->14, 22->14, 20->r, 20->21, 22->21, 5->22.
```

The six actual incident faces at 14 are

```text
(14,5,4) (14,4,r) (14,r,20)
(14,20,21) (14,21,22) (14,22,5).
```

In the standard directed-wheel encoding, the selected words are
`(53,53)` for #6/#9, `(53,55)` for #7, and `(49,55)` for #8. Each is a
standalone residual wheel at degree six and satisfies both centre semidegree
bounds.

Control `{0,2,3,4,7,14}`; retain boundary
`(5,6,8,11,12,13,20,21,22)`. Deleting any one controlled vertex and adding
any source-valid noncrossing oriented diagonal subset in its actual hole gives
2,740 candidates:

| parent | candidates | best rule | best complete vector |
|---|---:|---|---|
| #6 | 688 | delete 3; add 7->4 | 1,896 valid Q; 6 relation failures |
| #7 | 688 | delete 3; add nothing | 1,776 valid Q; 20 relation failures |
| #8 | 688 | delete 3; add nothing | 2,160 valid Q; 24 relation failures |
| #9 | 676 | delete 14; add 12->22,22->4,22->20 | 1,280 valid Q; 6 ordinary + 2 relation failures |

Every candidate has an explicit complete-Q failure witness. A separately coded Python
consumer regenerates the noncrossing catalogue by a ternary
product, checks each witness with DFS/BFS and Kahn/Warshall, enumerates all 64
P restorations, and recomputes the complete vectors of all 24 deletion-class
minima. It verifies 2,740 witnesses and performs 178,100 oracle comparisons.
Both implementations were produced by the same principal; this is differential
candidate checking, not a trusted independent-verifier receipt.

The standalone fixed-degree wheel census gives:

| degree | wheel types | reducible | residual |
|---:|---:|---:|---:|
| 4 | 96 | 66 | 30 |
| 5 | 640 | 480 | 160 |
| 6 | 3,200 | 2,582 | 618 |
| 7 | 14,336 | 12,292 | 2,044 |

The observed prefix counts are finite data only. No recurrence or all-degree
closure is claimed.

## 5. Reproduction and byte recovery

The committed sixteen-part recovery capsule losslessly stores an 18-file map, including the 805,141-byte Cycle-4 certificate,
decoded SHA-256

`b1ce2a030f96b99bea1ade41dc9484552353bcc573434136026a7be221542ff5`.

Run from the candidate directory:

```bash
python3 opg169-a01-s07-cycle5-unpack.py audit
python3 opg169-a01-s07-cycle5-unpack.py reproduce
```

`audit` checks all sixteen segment hashes, the assembled capsule, all 18 inner file hashes, and the decoded certificate.
`reproduce` extracts to a temporary directory, invokes the inner replay, reruns the Cycle-3 checker, the Cycle-4 separate consumer, and
the degree 4–7 census semantics. Each full generator shard is separately bound
by size and SHA-256 and can be replayed within a short foreground command: `python3
opg169-a01-s07-cycle5-unpack.py parent N` for `N=6,7,8,9`; the deterministic
assembler then reconstructs the archived certificate. The inner and outer execution records preserve CPython 3.13.5 and g++ 14.2.0 runs.
The selected outer recovery replay exited zero under CPython 3.13.5 and g++ 14.2.0:

```text
audit stdout sha256    69aa9a2ddc9dd3cb441438bb983635e69386cfaabd4424b7509c3cfcc78e3800
reproduce stdout sha256 b851794d11fcb8657ae0b8ab8904a5e273bf2afa581ab352c4aa5bdbf97914ac
unpack source sha256    e1ebaefbdeb3435a3d30e47b86fa8c53f1481b0daf9c5b8e4f60b8524d5b6efd
```

The 18 inner paths are archived rather than separately committed. No network was used by those computations, but session replay and transport CI
are not mathematical evidence.

## 6. Scoped failed-route conclusion

Within their exact classes:

- the merged-`{0,2}` quotient cannot be used as an arbitrary-exterior lift
  for any of residual #6–#9;
- a single fresh saturated high-port wheel plus one controlled deletion and
  arbitrary noncrossing hole diagonals does not close any of the four parents.

This does not exclude multi-vertex deletion, another contraction, new internal
vertices, a larger boundary, absorption of a rim vertex's complete star,
forced exterior return paths, or wheel-neighbour aliases.

```text
checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
owned_parents_before: 4
closed_by_recovered_rules: 0
remaining_owned_parents: 6,7,8,9
best_verified_result: none
next_obligation: obligation:opg169-root
root_closed: false
```
