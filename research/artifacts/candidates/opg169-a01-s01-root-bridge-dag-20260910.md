# R08 S01 root-bridge integrator checkpoint — typed live proof DAG

Verdict: `candidate_only`. `root_closed=false`. `best_verified_result=none`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Fresh protected `main`: `2d9303e7ae9558d3904bb2fa0bade246ebe9bbde`  
Exact SHA behind the reported `8d5bcb…`: `8d5bcb4955e84468f58a5923bed7f2ec527a6218`.

This is an integration checkpoint, not a new root theorem. It consumes only repository-bound completed material present on fresh `main`. The current 16-slot surge has no later merged mathematical output at this read, so no slot result is inferred from task text, chat consensus, open PRs, or transport state.

## 1. Status vocabulary

`PASS` below means only that an item passes the **S01 import/scope gate**: a repository locator and frozen digest exist and the imported use stays within the artifact's stated scope. It does not mean independent mathematical verification.

`FAIL` means the item fails a named **integration/admission gate** (for example, missing locator or statement-faithfulness), not that the mathematical statement is false.

`UNKNOWN` means no completed, admissible output currently decides the obligation.

All imported proof and computation candidates remain in the `web-candidate-generation` trust domain unless an independent receipt is explicitly present. No such receipt is imported here.

## 2. First genuine root cut

The strongest completed root-wide source cut currently available is C48's low-slack dichotomy, conditional on the candidate C34/C35 double-payment framework.

For any unpaid negative triangular face, some corner `p` has `s(p) <= 5`. Exactly one of:

1. **F26:** `t(p) <= 5`, placing `(s,t,d)` in one of 26 finite arithmetic cells; or
2. **SG:** `t(p) >= 6`, with at least one singleton gap between consecutive marked pair blocks.

For one singleton gap, C48 derives three surviving local alias interfaces and therefore 192 normalized direction parents, conditional on the frozen eight-sector direction catalogue.

Integration status: `PASS(import/scope)`. Mathematical verification: `UNKNOWN`. This cut is not `L_join`, not a realizability theorem for the 26 cells, not a reduction table, and not an AE/M12 shell theorem.

## 3. Mutually exclusive typed research-route DAG

The sparse admitted obligation graph remains unchanged. The following is the live **candidate research-route DAG** used for scheduling and integration.

```text
R0  root conjecture
|
+-- N0  minimum-order / source normal-form framework             [candidate]
     |
     +-- D0  negative DC2 actual unpaid face                     [candidate]
          |
          +-- C48-CUT  F26 arithmetic cell  XOR  SG singleton-gap
                |
                +-- J0  source-faithful generation + UNIQUE L_join
                      |     status: UNKNOWN
                      |     owners: S13-A/B/C/D
                      |
                      +-- STRUCT leaf
                      |     exact structural contradiction
                      |     -> CONTRADICTION
                      |
                      +-- A leaf
                      |     strict source-valid reduction
                      |     -> LIFT-O ordinary arbitrary-exterior lifting
                      |     -> CONTRADICTION
                      |
                      `-- B leaf
                            B-criticality / topology
                            -> well-founded high-port resolution if needed
                            -> finite strict source-valid reduction
                            -> LIFT-O ordinary arbitrary-exterior lifting
                            -> CONTRADICTION
```

`STRUCT`, `A`, and `B` are required to be a mutually exclusive, source-faithful partition produced by `J0`; no partition theorem has yet been imported. An arithmetic cell does not become a leaf until its actual embedding, rotation, aliases, complete stars, face ownership, and source identity are fixed.

### Ordinary versus anchored type separation

`LIFT-O` is the ordinary all-exterior strong-profile lane: complete valid `Q` colourings, same boundary colours, and both-colour positive-reachability containment.

Anchored contracts form a distinct lane:

```text
ANCHOR source -> anchored reduction -> anchored lifting
```

No anchored result closes an ordinary DAG edge without an explicit, separately proved lane-conversion theorem. In particular S08 `ATC_any_old` remains conditional/anchored and is not promoted to ordinary root coverage; its stronger deleted-only / zero-new-triangle contracts remain failed only in their frozen finite scopes.

## 4. Ancestor precedence and supersession

Candidate precedence rule imported from C48:

> An exact all-exterior strong-profile replacement at a parent source state provisionally dominates descendants that only further restrict its arbitrary exterior, provided the parent rotation, complete stars, arc set, interface, and source identity are unchanged.

Application:

- Exact C37 `d(7)=6`: five source families x 32 directions = 160 parents.
- Merged S06 C5 supplies a parent-preserving rule for all 160 parents.
- Therefore C38/C39/C40 and the C43-C47 / S08 D19 descendants in that **same exact C37 source domain** are inactive for live candidate scheduling.
- This does not cover `d(7)>=7`, a different J orientation, a changed parent, the 26 F26 cells as a class, the 192 SG parents as a class, or the global `L_join`.

Lifecycle imposed for this surge:

- old S05 one-terminal / wrong-region geometry: `retired`; no live DAG edge;
- old S06 exact-sector sessions: `retired` as active work; the merged 160-parent artifact remains an imported candidate ancestor;
- S07/S08/S16: `standby/transport`; no mathematical closure imported;
- S04: `awaiting evidence`;
- C47: retained only as a scoped negative catalogue for the corrected two-hole geometry with deletion `{13,14}` and at most one new nonisolated internal vertex in total. No larger gadget impossibility is inferred.

## 5. Completed-import ledger

| Item | S01 status | Exact imported scope | Trust domain | Supersession / DAG effect | Next obligation |
|---|---|---|---|---|---|
| C48 low-slack cut | PASS | negative unpaid face -> F26 XOR SG; SG has 3 interfaces / 192 normalized directions conditional on 8-sector catalogue | web-candidate-generation | active root cut | source-faithful realizability + unique `L_join` |
| C34 separated donor pairs | PASS | marked-pair packing and source geometry used by C48 | web-candidate-generation | active dependency | independent statement-faithfulness |
| C35 unpaid-face arithmetic | PASS | double-payment sign/arithmetic used by C48 | web-candidate-generation | active dependency | independent statement-faithfulness |
| S06 C5 / exact C37 `d(7)=6` | PASS | exactly five-family 160-parent source | web-candidate-generation | candidate ancestor; descendants inactive only in identical parent domain | independent checker + statement-faithfulness |
| C43 geometry recovery | PASS | corrected geometry / normal-form information only | web-candidate-generation | descendant reductions inactive under exact C37 ancestor; geometry retained as audit reference | S04 if a distinct two-terminal theorem survives |
| C47 corrected two-hole catalogue | PASS | exact corrected holes; delete `{13,14}`; <=1 new nonisolated internal vertex total | web-candidate-generation | scoped failed finite replacement family only | do not extrapolate; await S04 |
| S08 `ATC_any_old` | PASS | conditional anchored contract only | web-candidate-generation | standby; ordinary lane unaffected | independent anchored verification only if reactivated |
| mission-only S12/S14/S05 statements in C48 manifest | FAIL(import gate) | normalized launch statements have no repository-bound proof locator adequate for DAG closure | unbound mission text | no DAG-closing effect | consume only a completed repository-bound successor |

Every PASS in this table is an import/scope PASS, not a theorem-verification PASS.

## 6. 16-slot surge status

No post-C48 completed repository output exists at this fresh read. Hence:

| Slot | Status | Current role / blocker |
|---|---|---|
| S13-A arithmetic | UNKNOWN | refine source arithmetic only; arithmetic cannot prove realizability |
| S13-B geometry | UNKNOWN | actual faces/rotations/aliases for F26/SG source states |
| S13-C unique mapper | UNKNOWN | highest-priority `L_join` existence + uniqueness |
| S13-D red-team atlas | UNKNOWN | unmapped/ambiguous/double-payment falsifiers |
| S12-A blocking paths | UNKNOWN | B-criticality path premises |
| S12-B topology | UNKNOWN | planar contradiction for B-criticality |
| S12-C falsifier | UNKNOWN | adversarial escape from B-criticality |
| S02-A termination rank | UNKNOWN | well-founded high-port rank |
| S02-B infinite-chain attack | UNKNOWN | pumping/cyclic countermodel |
| S09 guard difference | UNKNOWN | exact surviving child set after ancestor precedence |
| S10 clean-room checker | UNKNOWN | independent rule/profile verification |
| S11 lifting theorem | UNKNOWN | theorem-level arbitrary-exterior composition including aliases / repeated boundary visits / zero-length hazards |
| S14 AE/M12 caps | UNKNOWN | source-faithful singleton-cap elimination or realization |
| S15 red team | UNKNOWN | falsify mapper, B-criticality, termination, lifting, caps |
| S04 two-terminal audit | UNKNOWN | determine retire/standby/continue under corrected holes `{8,12}` |
| S01 integrator | PASS | fresh state + typed DAG integrated; no new mathematics promoted |

## 7. Live frontier in priority order

1. **`J0 / L_join` unique source mapper — UNKNOWN.** It must map each source-valid negative DC2 face to exactly one structural/A/B leaf, with actual face sets, rotations, aliases, ownership, and no payer double-spending.
2. **B-criticality — UNKNOWN.** Both blocking-path and topological premises require independent attack.
3. **High-port termination — UNKNOWN.** A genuine well-founded rank or an adversarial infinite-chain construction must decide this before any unbounded degree chase is used.
4. **Finite leaves — UNKNOWN.** F26/SG parents, residual guards, and singleton caps need exact source-valid reductions or structural contradictions.
5. **Arbitrary-exterior lifting — UNKNOWN at verification level.** C48 contains a proof-drafted parent-precedence composition argument, but S11 theoremization and S10 independent checking are not yet completed/imported.
6. **Separating-triangle / composition bridge — UNKNOWN.** C48 leaves separating triangles open; no root closure can bypass this by local enumeration.

## 8. Conflicts and enforced resolutions

1. **Research-route DAG versus sparse formal obligation graph.** Resolution: use this typed DAG for live research scheduling while leaving the admitted formal graph unchanged. Candidate routing does not rewrite truth.
2. **C48 parent dominance versus descendant work.** Resolution: ancestor precedence is applied only under exact source identity. It makes same-parent descendants inactive; it never proves them false and never reaches a different parent.
3. **S08 anchored versus ordinary lifting.** Resolution: contracts are type-separated. `ATC_any_old` is conditional anchored evidence only.
4. **C47 scope inflation.** Resolution: C47 excludes only its frozen corrected-hole, at-most-one-new-internal-vertex family.
5. **Arithmetic versus geometry.** Resolution: F26 and the singleton count are source arithmetic; no realizability or reduction follows without S13-B/C.
6. **Finite census versus unbounded theorem.** Resolution: no fixed-degree census, C47 catalogue, or C48 bounded control is used as a termination theorem.
7. **Transport versus evidence.** Resolution: PR/merge/CI/chat/model review never upgrades any mathematical node.

## 9. Imported digests

Repository-bound SHA-256 values, as frozen by C48's import manifest / packet:

- C48 proof: `5debde2007cf978330c2f88017073ddf587350b7eec17b9860af1e0e9d625bd4`
- C48 low-slack checker: `7da84dab098c887276a4241ca4c7ddce8d301590d3b1b84fcc4474f2ca9a8aca`
- C48 checker output: `2f24e8873f93f185ae0ba46ca5a27bd44fb9ded39e2afcdafd5f34828b86c1a9`
- C48 cross-checker: `f854b9df2fd7de8fc243b99d34ce6a967a9e51385bc085d228151875468e68c8`
- C48 cross-check output: `e17c4ffca2bbcb1d68090e483feeace0c378161e8d1dfa9a17a4d91d155059eb`
- C34 separated-pair proof: `ce5929717bf16c34f59635f4b84d97b1c910809a19e457488e6496c47ed32958`
- C34/nine-donor geometry: `d7a8c647802dd16bf52357a601f415b8fcc33b99413e7b6c4f7abf21da2ffab8`
- C35 unpaid-face proof: `24eaa8c0c284f014b1fe62a572bda92bd149e8c8842a145805bc8a2db125d46a`
- S06 C5 exact C37 coverage: `bd4034e0241aa9370118ec4db6d423215f7b3f97936b78fadf9c68e58da95ebf`
- C43 geometry recovery: `5d9baae3cc2e00f03f6b992613aa0a079146808c7e53d94c34ccf98c04aea1e9`
- C47 corrected two-hole catalogue: `3a6e894c607a8c73f59291c0094efacab9f2bfbaa117ed33907af5d266321339`
- S08 C4 D19 proof: `364c69ffdee1c1cc20f026fbfa5147bd38faa9541778c85dd2491b35ded9d874`

Mission-supplied normalized statement digests remain non-closing: S02_C7 `6125ecfeeb500adebef9a1683a3527f61129f01291f8870ee7e1b40279ec0e4e`; S09_C5 `40841798d17fc6930c9d9036d1225e7a79c00bd81d9aeacbbdd94df1f6e012f0`; S12_C6 `ab003b77f9bc3046f7c5e30481cb0ba66bd956082c5b55919f7ecb49538b5496`; S14_C8 `f21331f5833a1784f0f6e3f6a7ee2f8a09df528db44844e9d63ecb0e44e0b35d`; S05_C5 `55c6278472dacfd9e5b1f60c4bd1ddc9bfcdcfc75b2e50fa7d43dc04cae1ff88`.

## 10. Checkpoint

`fresh_revision=2d9303e7ae9558d3904bb2fa0bade246ebe9bbde`

`reported_8d5bcb_exact=8d5bcb4955e84468f58a5923bed7f2ec527a6218`

`first_genuine_root_cut=C48 low-slack dichotomy: negative unpaid face -> F26 XOR singleton-gap`

`best_verified_result=none`

`root_closed=false`

### Non-claims

This checkpoint does not claim a unique `L_join`; source realizability of all 26 cells; reduction of all 192 singleton-gap parents; B-criticality; high-port termination; a complete finite leaf census; arbitrary-exterior lifting at independent-verifier level; a two-terminal theorem; a singleton-cap theorem; a global separating-triangle composition theorem; an EvidenceLink; a Result; or a Solution.
