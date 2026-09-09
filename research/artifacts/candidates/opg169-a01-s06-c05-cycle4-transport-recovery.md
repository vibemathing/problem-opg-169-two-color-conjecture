# S06 Cycle 5: transport recovery for the Cycle 4 merged-{0,2} catalogue

Verdict: `candidate_only`. Review status: pending.  
Candidate: `candidate:opg169-a01-s06-c05-cycle4-transport-recovery`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Protected base used by the recovered computation: `dc6ee891ed7614602e88d48a57314416082dd022`.

## 1. Recovery scope

This packet transports the bounded S06 Cycle 4 candidate previously produced outside the repository. It does not rerun mathematical research in GitHub, does not create a verifier receipt, and does not alter any truth ledger. The transported statement is restricted to the exact C37 degree-six J sector and its C38/C39 descendants.

The local recovery archive was recorded as:

```text
s06-r08-cycle4-backtrace-c39-c38-c37.tar.gz
SHA-256 a2ea17f4794d5746f100bd0088e152f9909b4f4dcbf5047bb92366a47d62fca4
```

Before transport, the local replay reported that its 18 frozen source/output files matched the archive manifest and that the C37/C38/C39 summaries were reproduced. This is generator-domain execution metadata, not independent evidence.

## 2. Exact replacement and interface

For the frozen C37 patch let the controlled set be

```text
I = {0,2,3,7}
```

and keep every vertex outside `I`, including vertex 4, fixed in a lift. The complete rotations at the two deleted adjacent vertices are

```text
rot(0) = (2,6,5,4,3)
rot(2) = (0,3,7,11,6).
```

Deleting `{0,2}` merges their two closed-star disks into the actual six-sided hole

```text
H = (3,4,5,6,11,7).
```

The principal rule is

```text
Q = P - {0,2} + {5->7, 6->7, 7->4}.
```

The three added edges form a noncrossing fan in `H`, with cells

```text
(7,3,4), (7,4,5), (7,5,6), (7,6,11).
```

In the C37 D family, the complete star of 7 is `{2,3,8,11,12,13}`; hence all three added underlying edges are fresh and no hidden exterior reverse arc exists. The replacement is finite, simple, planar, oriented, and has two fewer vertices.

For every valid complete colouring of a selected smaller patch, the frozen computation required a same-boundary colouring of the original patch satisfying

```text
R_P^+ subseteq R_Q^+,
```

where `R^+` is all positive monochromatic reachability on the retained interface. The arbitrary-exterior gluing argument replaces every original-patch segment of a hypothetical crossing monochromatic cycle by a smaller-patch path with the same colour and endpoints. This would create a positive monochromatic closed walk, hence a directed cycle, in the valid smaller graph.

## 3. Backtrace through C39 and C38

C39 adds the hypothesis `d(4)=6` and expands

```text
rot(4) = (0,5,q,r,8,3)
```

into 70 compatible signed parents. Keeping 4 on the interface gives a stronger contract than the original C39 search. The recovered audit reports:

```text
parents                         70
valid complete Q colourings  17408
equal reachability lifts       8458
strict reachability decreases  8950
failed valid inputs                0
```

Thus the full C39 70-parent layer is absorbed without using `d(4)=6` in the replacement itself.

C38's D/19 notation swaps C37's role labels 12 and 13. Under `12 <-> 13`, its five added arcs become C37 family `D`, word `19`. The recovered direct audit reports 168 valid smaller colourings: 72 equal-relation lifts, 96 strict decreases, and no failure. The frozen twelve-vertex C38 whole-graph obstruction also admits the same two-vertex replacement, with 90 valid smaller colourings, 64 equal lifts, 26 strict decreases, and no failure. This does not invalidate C38's old negative result, whose allocated family contained only specified one-point deletions and contractions.

## 4. Complete C37 degree-six signed layer

C37 has five surviving equality families `D,X5,X6,Y4,Y5`, each with 32 words: 160 signed parents. The direct universal fan is source-valid for 96 parents. For the other 64, one desired fan edge is opposite an already present arc; those are class-preservation conflicts, not profile failures.

The recovered merged-hole catalogue enumerated every noncrossing oriented diagonal set of the six-sided hole. There are 215 abstract sets and 24,928 parent-specific class-valid candidates. Its recorded totals are:

```text
successful candidates             11147
valid complete Q colourings      3549510
equal relation lifts             2008336
strict relation lifts            1422566
failed valid inputs               118608
ordinary failures                  36272
relation-only failures              82336
vacuous-Q candidates                    0
```

Candidate-level failures are retained as negative rows. Parent coverage before geometric guard elimination was `146 unguarded + 14 guarded-only + 0 residual`.

Ten nominal guards are impossible in the actual frozen embeddings because their endpoints are not cofacial in any complementary region. After that geometric audit, 156 parents have unconditional merged-`{0,2}` rules. The remaining four parents `Y4/0, Y4/4, Y4/16, Y4/20` reuse C37's independently checked bare `delete 3` rules. Their valid-colouring counts are respectively 124, 150, 134 and 162, all with zero failure.

The final selected menu therefore has

```text
156 merged-{0,2} rules
  4 bare delete-3 rules
160 unconditional signed parents
  0 guarded-only parents
  0 residual parents.
```

Across the selected menu, the recovered audit reports 21,732 valid complete smaller colourings, 16,536 equal-relation lifts, 5,196 strict decreases, and no ordinary or relation failure.

## 5. Prior obstruction and failed-route scope

C37's eleven-vertex `D/3` whole-graph obstruction defeated 308 alternatives of the form “delete one controlled vertex and add diagonals only in that one-point hole.” The new replacement deletes two adjacent vertices and uses the union of their closed-star disks. It lies outside that failed family. On the frozen whole graph, the recovered two-vertex audit reports 72 valid smaller colourings, 30 equal lifts, 42 strict decreases and no failure.

No claim is made that arbitrary two-vertex replacements work, that every C35 arithmetic family is covered, or that the local C37 sector is unavoidable in every minimum counterexample.

## 6. Reproducibility and trust boundary

The original local execution recorded CPython 3.13.5, NetworkX 3.6.1 and g++ 14.2.0. Its two C++ catalogue outputs were recorded as byte-identical with SHA-256

```text
dd215e43d05e9cbe529d86afcf903f94b96eac879be85fdd7fd5ccf4da98fc8c
```

The full catalogue exceeded the repository's one-file Web limit. This recovery does not silently replace it with incomplete data. The repository receives a readable statement, compact frozen totals, provenance note and a static consistency replay. The complete local archive remains identified only by its digest above; it is not represented as independently reviewed or as a repository verifier receipt.

## 7. Candidate conclusions and open boundary

Within the exact prior candidate dependencies, the Cycle 4 computation supports these candidate statements:

1. C38 D/19 and all 70 C39 descendants admit the stronger merged-`{0,2}` profile replacement while keeping vertex 4 fixed.
2. The full frozen C37 `d(7)=6` 160-parent signed layer has an unconditional selected replacement menu.
3. The old one-point-hole failed route remains valid at its stated scope.

This transport does not address `d(7)>=7`, other C35 direction families, the global negative-face join, DC2 completeness, the root conjecture, or trusted admission.

```text
checkpoint_state: NONTERMINAL_CHECKPOINT
best_verified_result: none
best_verified_candidate: none
requested_verification: statement_faithfulness, independent_replay, geometry_and_guard_audit
next_obligation: obligation:opg169-root
root_closed: false
```
