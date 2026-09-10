# S07 Cycle 5 — transport recovery for residuals #6–#9

`verdict=candidate_only`  
`base_revision=23df7d6625eafed849c8654c504c23da32b37b3c`  
`root_closed=false`

## Purpose

This transaction preserves two bounded negative results produced in S07 Cycles 3 and 4. It performs no new parent classification, changes no C40/C43/C44/C45 statement, and does not append a failed-route or truth record.

The owned C40 residual parents remain distinct:

- #6 `new/11/2`;
- #7 `new/11/4`;
- #8 `new/11/5`;
- #9 `new/12/2`.

Canonical C40 parent coverage remains `10 structural + 24 unguarded + 22 guarded + 14 residual`.

## Cycle 3: merged-{0,2} quotient

Contract the actual plane edge `0->2`, delete the resulting loop, and resolve the inherited opposite pairs at common neighbours 3 and 6. There are exactly four simple oriented quotient variants. The retained boundary is `(5,6,8,11,12,13,14)`.

A separately coded Kahn/BFS oracle and DFS/bitset oracle, both produced by the same research principal, agree on 49,152 complete P/Q colourings. Across the sixteen parent/variant rules there are 4,722 valid Q colourings: 4,522 satisfy the strong lift and 200 fail, split into 40 ordinary nonextensions and 160 relation-only failures.

No variant closes any owned parent. Parents #6 and #9 have ordinary failures. Parents #7 and #8 have relation-only failures. A common Q mask 86 defeats all sixteen variants: for #6–#8 every P lift adds the positive monochromatic relation `14->8`; for #9 no ordinary P extension exists.

Scoped conclusion: the merged-{0,2} quotient alone cannot support an arbitrary-exterior lifting lemma for residual #6, #7, #8, or #9.

## Cycle 4: saturated degree-six high-port wheel

For fixed wheel degree d, deleting the centre has the exact state test: a centre colour h is usable precisely when every same-colour incoming spoke endpoint reaches every same-colour outgoing spoke endpoint in Q. This is a fixed-d finite automaton, not a degree-independent finite-state theorem.

For each owned parent a fresh-rim complete degree-six star at q was embedded with rotation `(5,4,r,20,21,22)`. The source-valid catalogue permits deletion of one controlled vertex and any noncrossing oriented diagonal subset in its actual hole, with every retained shortcut carrying its reverse-arc guard.

Exact candidate counts and best remaining failures are:

| parent | candidates | best remaining failures |
|---|---:|---:|
| #6 | 688 | 6 relation-only |
| #7 | 688 | 20 relation-only |
| #8 | 688 | 24 relation-only |
| #9 | 676 | 8 = 6 ordinary + 2 relation-only |

Thus all 2,740 rules fail. Every candidate has a nonvacuous complete Q domain. The differential consumer verifies all 2,740 stored first witnesses and recomputes all 24 deletion-class minima. It is a same-principal differential check, not a trusted independent verifier.

Scoped conclusion: the stated degree-six saturated-wheel, one-deletion/hole-diagonal replacement class closes none of residual #6–#9. It does not exclude multiple deletions, new internal vertices, larger separators, rim-star absorption, aliases, or higher-degree replacements.

## Fresh-main drift audit

C43 repairs the separate dual-fan/guard-edge geometry and records the S07 merged quotient only as a candidate negative leaf. C44 classifies a degree-four third vertex on the guard edge `8->12`. C45 absorbs an endpoint of C44's first residual. Those nodes are in a different child tree and do not modify the identities, arcs, rotations, witnesses, or scope of S07 residual #6–#9.

A concurrent C46 guard-failure PR likewise concerns the C44/C45 tree. This recovery branch does not modify, supersede, or depend on that moving branch.

## Evidence ceiling

The preserved programs and differential consumers share one generator principal. There is no registered verifier receipt, formal elaboration, axiom report, statement-faithfulness admission, EvidenceLink, Result, residual-zero theorem, global coverage theorem, or root closure.

`remaining_owned_parents={6,7,8,9}`  
`root_closed=false`
