# R08 S01 Cycle 4 — A48 witness semantics and completed bridge integration

Verdict: `candidate_only`. `root_closed=false`. `best_verified_result=none`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected `main` consumed: `3bec7e8d2c4fec368707f3f86cccfc7af8120472`.

Cycle 4 repairs the quantifier semantics of C48/A48 and consumes three newly completed repository-bound candidate bridges on top of Cycle 3:

1. S09 exact C37 `d(7)=6` source registry and lineage;
2. S10 theorem-content consumer for ordinary arbitrary-exterior lifting;
3. S02-B Cycle 2 adversarial escape-rank audit.

No completed S13 global source generator / unique mapper, S12 B-criticality package, S11 artifact identity, S14 cap theorem, S15 new root falsifier, or S04 two-terminal disposition is imported.

## 1. A48 is a witness relation, not a face branch

Let `D0(f)` mean that `f` is an actual unpaid negative triangular face in the candidate C34/C35 ledger. For a corner `p` of `f`, retain C48's arithmetic data

```text
d(p) = 3 t(p) + s(p),
s(p) >= 0,
t(p) + s(p) >= 4.
```

Define

```text
W48(f,p)  :<=>  p is a corner of f and s(p) <= 5,
F48(f,p)  :<=>  W48(f,p) and t(p) <= 5,
SG48(f,p) :<=>  W48(f,p) and t(p) >= 6.
```

The C48 theorem has the exact quantifier form

```text
forall f:
  D0(f) -> exists p W48(f,p),

forall f,p:
  W48(f,p) -> exactly_one(F48(f,p), SG48(f,p)).
```

It does **not** prove a unique low-slack corner, and it does **not** prove

```text
D0(f) -> exactly_one(
    exists p F48(f,p),
    exists p SG48(f,p)
).
```

Therefore the Cycle-3 shorthand `A48: F26 XOR SG` is superseded whenever it is read as a face-level partition. F/SG exclusivity is valid only after a witness corner `p` has been fixed.

### Arithmetic pressure test

The arithmetic triples

```text
(s,t,d) = (5,0,5), (5,6,23), (5,0,5)
```

satisfy the C48 integer-domain inequalities. Their corner contributions are

```text
1/5, 7/23, 1/5,
```

so the corresponding arithmetic face charge is

```text
-1 + 1/5 + 7/23 + 1/5 = -34/115 < 0.
```

The first and third corners are F-tagged and the middle corner is SG-tagged. This is an arithmetic countermodel to deriving face-level F/SG XOR from the C48 arithmetic premises. It is **not** claimed to be a geometrically realizable minimum-counterexample face.

Any downstream source theorem must therefore carry the witness `(f,p)` as provenance, quantify uniformly over all eligible witnesses, or prove a canonical selector.

## 2. F and SG have different choice semantics

For a fixed F witness `(f,p)`, `(s(p),t(p))` determines one of C48's 26 arithmetic cells. The `26` labels are arithmetic cells, not embedded parent states.

For a fixed SG witness `(f,p)`, let `G48(p)` be the set of singleton cyclic gaps between consecutive marked pair blocks. C48 proves

```text
|G48(p)| >= t(p)-s(p) >= 1,
```

not `|G48(p)|=1`.

C48 then chooses one `g in G48(p)` and derives for that selected gap the two-sector local geometry with three surviving alias interfaces and

```text
3 * 8^2 = 192
```

normalized direction patterns, conditional on the frozen eight-sector direction catalogue.

Thus `192` is a **selected-gap local atlas** for `(f,p,g)`. It is not the number of all SG states attached to `p`, to `f`, or to the root problem.

The correct arithmetic-to-source interface is

```text
D0(f)
 |
 +-- W48(f,p): choose/carry low-slack witness p
      |
      +-- F48(f,p)
      |      -> unique arithmetic cell among 26
      |      -> LSRC-F(f,p,geometry)                     [UNKNOWN]
      |
      `-- SG48(f,p)
             -> choose/carry g in G48(p)
             -> selected-gap local atlas (3 / 192)
             -> LSRC-SG(f,p,g,geometry)                  [UNKNOWN]
```

No canonical witness selector or singleton-gap selector is imported in Cycle 4.

## 3. Global source generation remains downstream

The live source chain is relational:

```text
D0(f)
  -> W48(f,p) + per-witness arithmetic tag
  -> LSRC(f,p[,g]) actual local embedded realization
  -> GSRC global generation from the actual face
       with source/payer identity, ownership, and no double spending
  -> JMAP unique L_join / exact parent identity
  -> SCUT exactly one STRUCT / A / B leaf.
```

`GSRC` and `JMAP` must resolve duplicate descriptions from multiple low-slack corners, multiple singleton gaps, aliases, and symmetries. A48 supplies no face-level uniqueness to inherit.

`SCUT`, the first genuine source-faithful leaf cut, remains `UNKNOWN`.

## 4. Completed bridge: S09 exact C37 source lineage

Merged S09 main commit:

```text
598d2c887a119fbb762ce51f9d6dc4af9431aff9
```

Frozen identities:

```text
atlas SHA-256
1502702e3825a8ccc79f9162fe412371bc14091a8260a42b90f6826f44fda606

expanded parent-ID SHA-256
cb8b4171491572de52a1ca5f3ebe1235e6091dd7298c5b380f0477d0c9789b74

expanded 160-row SHA-256
65357c97e5fdb35ba150c7d658ed053489097ee6d1013ec03529685f643b6dab

checker SHA-256
5a319d5d329f0ea80d2f22c04d715fcb56af1e51a80f61cb5a563c5ea643e609

proof SHA-256
9d23c6846ff89f1acb39ef664ef800e6968aa569776b93d0e18dcbceddee4b61
```

### REG37

The exact C37 `d(7)=6` source universe is repository-bound as

```text
{D,X5,X6,Y4,Y5} x {0,...,31}
```

with 160 exact source IDs.

Status: `PASS(candidate source registry)`.

### RED37

The exact 160 rows partition as

```text
96 direct-fan delete {0,2}
60 other unconditional merged-catalogue delete {0,2}
 4 bare delete 3: Y4/0,4,16,20
---
160
```

The 60 literal catalogue rules remain bound to the frozen S06 postprocess rather than being regenerated by S09.

S10's clean-room finite consumer independently corroborates the aggregate `156+4` allocation and the complete-Q / positive-reachability totals at candidate level.

### LINEAGE37

A child is ancestor-dominated only when it preserves:

1. every source arc of the exact C37 parent;
2. rotations and complete stars of controlled vertices `0,2,3,7`;
3. the parent interface and deletion hole;
4. only data in the arbitrary exterior already quantified by the parent rule; and
5. all parent identities and controlled adjacencies.

A changed source arc, star, rotation, interface, alias, or controlled adjacency creates a new source state.

Status: `PASS(candidate exact-parent lineage bridge)`.

### D19-ID

Exactly `D/19` carries the current named C38 -> C39 -> C40 repository chain. After C38's `12 <-> 13` relabeling, its complete 23-arc source is exactly C40 `BASE_ARCS`.

A physical C40 reverse guard may invalidate a child shortcut but does not invalidate the unconditional C37 ancestor rule.

No descendant chain is invented for the other 159 rows.

### S09 disposition

The Cycle-3 source blocker `NOT_VERIFIABLE_MISSING_SOURCE` is repaired inside the exact C37 `d(7)=6` universe.

```text
exact source parents                         160
unconditional ancestor parents               160
named C38->C39->C40 source rows                 1
C40 guard-child enumeration required            0
```

The final zero follows from exact-parent ancestor precedence, not from separately reducing every guard child.

S09 guard-difference work is retired inside this exact universe and remains inapplicable to changed sources, `d(7)>=7`, or another J orientation.

## 5. Completed bridge: ordinary LIFT-O theorem content

Merged S10 theorem-content consumer main commit:

```text
a31eb9646c828e05ed9071f6830a24df28f5b64d
```

Frozen candidate identities:

```text
theorem consumer SHA-256
319764672c907c40e0cea74376040548b121f55fbc9e9140f8ef7c4f1a298c01

ownership/checklist SHA-256
35050f2ef18d450f5a2d6c94e02ce89cab4b92ddefec70c6809d9965f7507e03
```

Cycle-4 disposition:

```text
LIFT_O_THEOREM_CONTENT        PASS(candidate, repository-derived)
LIFT_O_SOURCE_OWNERSHIP       row-dependent
LIFT_O_TRUSTED_VERIFICATION   UNKNOWN
S11_ARTIFACT_BINDING          NOT_VERIFIABLE_MISSING_SOURCE
```

The generic theorem content is:

Let `P,Q,F` meet exactly in an alias-normalized boundary `B`; all patch/exterior contacts occur through `B`; shared boundary arcs have consistent ownership and direction. If every valid complete `Q` colouring has a same-boundary valid `P` lift with both-colour positive reachability

```text
R_P^+ subseteq R_Q^+,
```

then every valid colouring of `Q union F` lifts to a valid colouring of `P union F` while the exterior `F` stays fixed.

The repository proof chain is C13 exact boundary gluing, C31 one-sided profile replacement and shared-edge semantics, C34 saturated-star ownership/pinched-interface application, C37 complete-Q instantiation, and C48 exact-parent packaging. S10 clean-room mutation controls pressure-test the finite row semantics.

The audit covers repeated boundary visits, boundary-owned edges, positive-length/zero-length hazards, disconnected patches, aliases, reused walks, pinched/two-region interfaces, and unrecorded exterior contacts.

Strict order decrease, simple-planar-orientation membership, reverse guards, and actual complete-star ownership remain row/source obligations for minimal-counterexample use.

On an exact common tournament interface with identical directions, ordinary same-boundary extension suffices because boundary reachability is fixed by the tournament orientation. This shortcut does **not** extend to generic partial or two-terminal interfaces.

DAG effect: proving the generic mathematical implication is no longer the live LIFT-O blocker. Remaining work is source-specific ownership/class-preservation binding and trusted verification/admission.

## 6. Completed bridge: S02-B escape-rank adversarial audit

Merged S02-B Cycle-2 main commit:

```text
3bec7e8d2c4fec368707f3f86cccfc7af8120472
```

Frozen identities:

```text
proof SHA-256
34bd93025bec1fb2645edc4303a55aad61ae1337a91c59df330cea760577d972

checker SHA-256
aaacfaaa24229919fdcacc79ce00532480fab45d068504542b8b275bb0b77b6b

output SHA-256
c6587703d780e1ad0d695bad5fc7924543b006837ca8e0a36299b53a6a85093d
```

This sharpens the Cycle-3 termination frontier.

### History-free complete-star release fails

In the exact C37-derived alternating high-port strip, the natural raw state space that remembers only the currently active complete degree-four wheel admits literal two-cycles

```text
W_i -> W_{i+1} -> W_i.
```

Therefore no well-founded rank can strictly decrease on **every unnormalized/history-free** complete-star release transition.

This is a candidate falsifier for that transition definition. The actual normalized S02-A transition system remains unbound.

### Purely local separator rank fails

Repeated directed octahedral shells can be nested to arbitrary depth inside an actual directed face of the C37-derived high-port strip while preserving the old embedding footprint and minimum semidegree. The bounded control reaches depth 32 and exhibits 31 genuine locally identical separating triangles.

Thus separator type, local shell geometry, or purely local separator depth pattern cannot by itself be the required decreasing rank.

The construction remains inside a fixed outer interface, so it does not refute global fixed-interface profile compression.

### Root-class stress test is source-separated

Alternating oriented bipyramids give a separate finite root-class cyclic stress test for a locally canonical release rule. They are not claimed to be C37 descendants or GSRC/JMAP children.

### Surviving termination form

The current adversarial results do not refute a **normalized history-aware discovery rank** recording, for example:

```text
unseen vertices,
incompletely exposed complete stars,
unprocessed rooted separator sides.
```

Such a monotone rank can prove that source discovery on a fixed finite graph terminates. It does **not** prove that the terminal discovered state is reducible, belongs to a finite leaf library, satisfies GSRC/JMAP, or closes the root.

Therefore the former single node `ESCAPE-RANK` is superseded by two obligations:

```text
TNORM  define/source-bind a normalized no-backtracking transition system
TPROG  prove every terminal normalized state makes mathematical progress
       (structural contradiction, exact mapped leaf, or strict reduction)
```

Current status:

```text
raw degree/port/size rank                 FAIL(candidate route)
history-free star-release rank            FAIL(candidate route)
purely local separator rank               FAIL(candidate route)
fixed four-port C37 profile compression   PASS(candidate, exact family)
history-aware discovery rank              NOT REFUTED / only discovery
TNORM                                      UNKNOWN
TPROG                                      UNKNOWN
```

No global termination theorem is claimed.

## 7. Exact C37 conditional leaf bridge

The S06/S10/S09/LIFT-O content now composes conditionally as:

```text
EXACT-C37(s)
  -> REG37 exact source identity                 [S09 PASS candidate]
  -> RED37 strict parent reduction               [S06/S10 PASS candidate]
  -> LINEAGE37 ownership/exterior inheritance    [S09 PASS candidate]
  -> LIFT-O theorem content                      [PASS candidate]
  -> exclusion from a vertex-minimum counterexample
```

The missing implication is still

```text
A48 witness -> EXACT-C37(s).
```

That is a GSRC/JMAP problem, not a finite-reduction or lifting problem.

## 8. Repaired live DAG

```text
R0 root
 |
 +-- D0 actual unpaid negative DC2 face f
      |
      +-- W48(f,p): nonempty low-slack witness relation
            |
            +-- fixed p: F48
            |      -> one arithmetic cell among 26
            |      -> LSRC-F(f,p,geometry)                    [UNKNOWN]
            |
            `-- fixed p: SG48
                   -> choose/carry g in G48(p)
                   -> selected-gap 3-interface / 192 atlas
                   -> LSRC-SG(f,p,g,geometry)                 [UNKNOWN]

LSRC
 |
 +-- TERM / recursive source-discovery discipline
 |      raw-size rank                                         [FAIL]
 |      history-free star-release rank                        [FAIL]
 |      purely local separator rank                           [FAIL]
 |      fixed-interface profile compression                  [PASS exact family]
 |      TNORM normalized history-aware transition             [UNKNOWN]
 |      TPROG terminal mathematical progress                  [UNKNOWN]
 |
 v
GSRC global source generation                                 [UNKNOWN]
 |
 v
JMAP unique L_join / exact parent identity                    [UNKNOWN]
 |
 v
SCUT exactly one STRUCT / A / B                               [UNKNOWN]
      |
      +-- STRUCT -> contradiction
      |
      +-- A -> strict ordinary reduction
      |       |
      |       +-- if EXACT-C37 d(7)=6:
      |       |      REG37 -> RED37 -> LINEAGE37              [PASS candidate]
      |       |
      |       `-- LIFT-O theorem content                      [PASS candidate]
      |              source ownership / trusted admission     [row-dependent/UNKNOWN]
      |
      `-- B -> B-criticality                                  [UNKNOWN]
              -> strict ordinary reduction
              -> LIFT-O theorem content                       [PASS candidate]
                 + source ownership/admission
```

Anchored contracts remain a disjoint lane; S08 `ATC_any_old` cannot close an ordinary edge without a separately proved conversion theorem.

## 9. Cycle-4 status ledger

| Node / lane | Status | Exact meaning |
|---|---|---|
| `W48` existence | PASS(import/scope) | every negative unpaid face has at least one low-slack witness |
| face-level F/SG XOR | FAIL(semantic inference) | C48 gives XOR only for a fixed witness |
| F arithmetic cell label | PASS per fixed witness | one of 26 arithmetic cells; no source realization |
| SG singleton-gap existence | PASS per fixed witness | at least one gap; not unique |
| selected-gap 192 atlas | PASS(import/scope) | one selected `(p,g)`; conditional on 8-sector catalogue |
| LSRC | UNKNOWN | actual realizations/provenance |
| GSRC | UNKNOWN | global source/payer generation |
| JMAP | UNKNOWN | unique source/leaf mapper |
| exact C37 REG37 | PASS(candidate) | 160 repository-bound exact source IDs |
| exact C37 RED37 | PASS(candidate) | 160/160 strict finite parent rules |
| exact C37 LINEAGE37 | PASS(candidate) | exact-parent exterior inheritance |
| S09 old guard-difference lane | RETIRED in exact C37 | no separate C40 child census needed |
| LIFT-O theorem content | PASS(candidate) | generic R+ lifting implication |
| LIFT-O trusted verification | UNKNOWN | no trusted receipt |
| S11 artifact identity | FAIL(source-binding gate) | no repository-bound S11 artifact |
| raw/history-free/local TERM ranks | FAIL(candidate routes) | explicit counterfamilies/cycles |
| TNORM | UNKNOWN | normalized history-aware transition not source-bound |
| TPROG | UNKNOWN | terminal discovery -> actual mathematical progress missing |
| B-criticality | UNKNOWN | S12 package absent |
| S04 two-terminal | UNKNOWN | no completed disposition |
| S14 caps | UNKNOWN | no completed source-bound successor |
| root | OPEN | no EvidenceLink / Result |

## 10. Live frontier

Priority after Cycle 4:

1. **A48 witness -> LSRC/GSRC bridge.** Carry `(f,p[,g])` provenance or prove a selector; do not use face-level F/SG branch language.
2. **JMAP / unique `L_join`.** Resolve multiple witness/gap/source descriptions and map to one exact source/leaf, or provide an ambiguity/unmapped falsifier.
3. **TNORM + TPROG.** Stop searching for raw local ranks; bind a normalized no-backtracking transition and prove terminal mathematical progress.
4. **B-criticality.** Blocking-path/topology/falsifier agreement remains absent.
5. **LIFT-ADMISSION.** Generic theorem content is available; remaining work is row ownership/class-preservation and trusted verification, not re-proving the generic lemma.
6. **S04 / S14.** Only source-faithful successors surviving ancestor precedence matter.

Exact C37 `d(7)=6` finite descendants and the old S09 guard-difference census are no longer live blockers once exact source identity is established.

## 11. Non-claims

This checkpoint does not claim:

- a unique low-slack corner;
- face-level F/SG exclusivity;
- a unique singleton gap;
- that the 26 arithmetic cells are 26 source parents;
- that 192 is a complete SG source census;
- realizability of every arithmetic witness;
- A48-to-C37 generation;
- GSRC or a unique `L_join`;
- a completed STRUCT/A/B source cut;
- `d(7)>=7` coverage from S09/C37;
- a global termination theorem;
- terminal reducibility from history-aware discovery;
- B-criticality;
- a repository-bound S11 artifact;
- trusted independent verification;
- an anchored-to-ordinary conversion;
- a two-terminal theorem;
- a singleton-cap theorem;
- EvidenceLink, Result, Solution, or root closure.

`best_verified_result=none`  
`root_closed=false`
