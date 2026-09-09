# S08 Cycle 4 — transport recovery for the universal D/19 rule

`verdict=candidate_only`; target `obligation:opg169-root`. The recovered
computations use source snapshot
`dc6ee891ed7614602e88d48a57314416082dd022`; this transport is based on fresh
main `23df7d6625eafed849c8654c504c23da32b37b3c`.

This packet recovers the essential Cycle 2 and Cycle 3 artifacts that were
produced locally but never transported. It adds no truth-ledger entry,
EvidenceLink, Result, or root closure.

Fresh-main compatibility was checked before transport. C43--C45 concern the
C40 first residual `12/new/2`, its external guard-edge faces, and a degree-four
endpoint of that guard-face wheel. They do not alter the C39/C40 rotations,
complete stars, or stable residual identities 10--14 used here. This recovery
makes no claim about the C43--C45 branches.

## 1. Frozen scope

The underlying ProblemContract is the two-colour conjecture for finite simple
planar orientations: both full induced colour classes must be acyclic.
Positive boundary reachability means a monochromatic directed path of positive
length. A replacement is usable against an arbitrary exterior only when every
valid complete colouring of the smaller graph has a same-boundary lift with

\[
R_P^+\subseteq R_Q^+.
\]

The original contract does not itself impose a triangle-clean condition. Cycle
3 therefore freezes three different strengthened contracts rather than
silently conflating them:

- `ATC_any_old`: every new directed triangle has a retained oriented edge that
  lies on an explicitly certified directed triangle of the original patch;
- `ATC_deleted_only`: the witnessing original triangle must meet the deleted
  set `D={0,2}`;
- `strict_zero_new`: the replacement creates no directed triangle absent from
  `P-D`.

The positive conclusion below is only for `ATC_any_old`.

## 2. Five owned parents and the universal rule

The stable C40 residual indices 10--14 are

```text
P10 = new/12/4
P11 = new/12/5
P12 = new/new/2
P13 = new/new/4
P14 = new/new/5
```

They use the C40 D/19 core and complete controlled stars
`I={0,2,3,4,7}`. Deleting the adjacent complete-star vertices `0,2`
leaves the actual hexagonal hole

```text
H=(3,4,5,6,11,7).
```

The recovered replacements are

```text
P10,P11:
    delete {0,2}; add 4→11, 7→4

P12,P13,P14:
    delete {0,2}; add 4→6, 4→11, 7→4.
```

All added arcs are noncrossing diagonals of `H`, sharing endpoint 4. The
complete star of 4 excludes old edges to 6,7,11; the complete star of 7 also
excludes 4--7. Consequently no loop, duplicate edge, opposite arc, or exterior
reverse-arc guard is introduced. Every rule lowers order by two.

## 3. Complete strong-profile table

The exact complete-colouring replay gives

| parent | valid Q | equal relation | strict decrease | ordinary failure | relation failure |
|---|---:|---:|---:|---:|---:|
| P10 | 144 | 140 | 4 | 0 | 0 |
| P11 | 144 | 140 | 4 | 0 | 0 |
| P12 | 420 | 330 | 90 | 0 | 0 |
| P13 | 396 | 250 | 146 | 0 | 0 |
| P14 | 396 | 250 | 146 | 0 | 0 |

The retained vertex 8 is a boundary port. Its unlisted neighbours, arcs,
fan length, aliases, chords, and distant paths belong to the arbitrary
exterior and keep their colours. The table therefore does not extrapolate
from a finite `d(8)` atlas: the profile lemma directly covers every actual
`d(8)`.

The arbitrary-exterior proof is the standard segment replacement argument.
Any new crossing monochromatic cycle splits into local and exterior positive
boundary paths. Replace each local P segment by the certified Q path. The
result is a positive monochromatic closed walk in the supposedly valid smaller
whole graph and hence contains a directed cycle.

## 4. `ATC_any_old` survives

Because every new arc meets the complete-star vertex 4 or 7, a new triangle
cannot use an unrecorded third neighbour of either vertex. Pairs between
non-complete retained vertices were nevertheless treated as optional exterior
arcs, giving a safe superdomain of every source-valid exterior.

The possible new directed triangles number `3,3,3,5,5` for P10--P14. Every
one has a retained edge on an actual directed face of P:

```text
4→11→7→4      anchor 11→7 on face (2,7,11)
4→11→12→4     anchor 12→4 on face (4,8,12)
4→6→14→4      anchor 14→4 on face (4,5,14)
4→11→14→4     anchor 14→4 on face (4,5,14)
4→6→15→4      anchor 15→4 on face (4,8,15)
4→11→15→4     anchor 15→4 on face (4,8,15)
```

Only the triangles compatible with a given parent occur. The exact per-parent
list and face witnesses are stored in the anchored result and facial-anchor
output. Thus the Cycle 2 rule survives unchanged under `ATC_any_old`.

## 5. The two stronger contracts fail in the tested family

For each parent, all 215 noncrossing oriented diagonal subsets of the actual
hexagonal hole were tested after deleting `{0,2}`. The number of strong-profile
candidates and zero-new-triangle candidates is

| parent | strong profile | zero-new triangle | intersection |
|---|---:|---:|---:|
| P10 | 6 | 101 | 0 |
| P11 | 6 | 101 | 0 |
| P12 | 3 | 113 | 0 |
| P13 | 3 | 113 | 0 |
| P14 | 3 | 113 | 0 |

Hence `strict_zero_new` has no rule in this exact replacement family.

For `ATC_deleted_only`, use P12 with actual exterior arcs `6→14,13→6`.
The supplied plane certificate has 13 vertices, 30 edges, 19 faces and Euler
characteristic 2. Its complementary-disk faces are

```text
(5,14,6), (14,15,8,13,6), (13,12,11,6).
```

Among the 215 candidates, 140 satisfy the deleted-anchor condition and three
satisfy strong profile, but the intersection is zero. This is a source-valid
counterexample to the unchanged rule under the stricter anchor meaning and a
complete negative only for this exact same-hole family.

## 6. Recovery replay

The recovered capsule-member result digests are

```text
universal result:
e0161a3680e5626412b7a83bc99f0563407090f22744d5cde9b6b60e61103127

anchored result:
5ac55ef87c52dbfc16c88096dbb06c8d4fe237d1e84dd4261fc48739e97653dd

plane witness output:
d8bb3cc4821dd78bea1abfe289e6123562fdd69fa2a9207cf980e139efaa6fb2

facial-anchor output:
aafc9415d3a6e264240eb7f8ff3f0500157fd15b0d3fa8b2d61bbaf9bfba9e54
```

`opg169-s08-cycle4-replay.py` verifies and reconstructs the three-part
UTF-8 capsule in a temporary directory, regenerates both result objects,
compares exact bytes, runs a separately written DFS/BFS consumer,
and replays the plane and facial-anchor checks. The six anchored consumer
modes run as bounded parallel subprocesses. A first serial orchestration
attempt exceeded the platform command window without producing a conflicting
mathematical output; the bounded parallel wrapper completed with `status=ok`.

The repository at the transport-base revision does not contain the generic
`scripts/compute_plan.py` named by the installed computation skill, so no such
receipt is claimed. These are small exact finite enumerations and were routed
to CPU. Runtime and file identities are recorded in the execution manifest.

## 7. Coverage and handoff

Under `ATC_any_old`, all five S08-owned parents remain candidate-excluded for
arbitrary exterior and arbitrary degree of 8:

```text
remaining_owned_parents: none
```

Under either stronger meaning, the five parents are not closed by this rule.
This contract distinction must remain explicit in S01.

Fixed handoff statements:

```text
S08-C4-F1  Delete {0,2}; the actual hole is (3,4,5,6,11,7).
S08-C4-F2  P10/P11 add {4→11,7→4}; P12--P14 also add 4→6.
S08-C4-F3  The five complete profile counts are
           144/140/4, 144/140/4, 420/330/90,
           396/250/146, 396/250/146, with zero failures.
S08-C4-F4  Since 8 remains a boundary port, the rule is uniform in d(8).
S08-C4-F5  `ATC_any_old` passes with nineteen actual-face anchor witnesses.
S08-C4-F6  `ATC_deleted_only` fails on the explicit P12 exterior witness.
S08-C4-F7  `strict_zero_new` has zero strong/clean intersection for each
           parent in the exact 215-candidate same-hole family.
```

## 8. Evidence ceiling and non-claims

The producer and second consumer remain in one local generator trust domain.
There is no registered trusted-verifier acknowledgement, Lean elaboration,
axiom report, EvidenceLink, or Result.

No claim is made that:

- `ATC_any_old` is the coordinator's intended anchored contract;
- the 215-candidate negatives exclude larger interfaces or arbitrary gadgets;
- residuals 1--9 or any guarded C40 parent are handled;
- any DC2 ledger or global completeness theorem follows;
- the root conjecture is closed.

```text
checkpoint_state: NONTERMINAL_CHECKPOINT
best_verified_result: none
best_candidate_result: the five owned D/19 parents admit a universal
  strong-profile reduction satisfying the explicitly frozen ATC_any_old contract
root_closed: false
```
