# S02-B source / scope / trust note

`candidate_only`; `root_closed=false`.

## Frozen repository state

- Repository: `vibemathing/problem-opg-169-two-color-conjecture`.
- Exact SHA behind the mission-reported `8d5bcb…`: `8d5bcb4955e84468f58a5923bed7f2ec527a6218`.
- Main at the beginning of the mathematical search: `2d9303e7ae9558d3904bb2fa0bade246ebe9bbde` (merged C48).
- Fresh protected main at the final source read / branch point: `d3d43d517596934ea16c906c9f335e8cf6ba4884` (S01 typed root-bridge integration), whose parent is C48.
- ProblemContract SHA-256: `719230edd088c52a5468eed8090579e5eef1bf85d8a56e633350063108f345ec`.
- Harness snapshot SHA-256: `7a2742cba5465b04c12b939e43143ddaff67bbd355eaacb5c7cab9ed674ff47c`.

S01 explicitly keeps S02-B/high-port termination `UNKNOWN`; this lane therefore adds candidate research, not an imported conclusion.

## Repository-bound source separation

1. `research/artifacts/candidates/opg169-a01-c37-input.json` supplies the exact C37 whole-witness embedding used as the base plane triangulation. Its Git blob on current main is `a452f67995e1b563e364382593b887bf0ec1f63d`.
2. The merged S06/C37 parent theorem candidate applies exactly to `d(7)=6` (five source families, 160 signed parents). It is not used to classify the new `d(7)>=7` family.
3. `research/artifacts/candidates/opg169-a01-c45-endpoint-proof.md` and C46 are a different descendant source. C45's same-boundary obstruction is used only as a warning that interface release can increase raw port count; no C37-high-port -> C45 source bridge is assumed.
4. C48/S01 record the mission-supplied S14/AE-M12 shell statement (`S14_C8`, SHA-256 `f21331f5833a1784f0f6e3f6a7ee2f8a09df528db44844e9d63ecb0e44e0b35d`) as repository-unbound. It has no DAG-closing effect here and is not used in the construction or finite-profile argument.
5. C43's obsolete one-terminal infinite-pinch extrapolation remains quarantined; the S02-B construction uses only the actual two facial sides of the edge `12-13` and introduces no cross-lobe edge.

## Candidate artifacts and exact digests

- Proof / audit: `research/artifacts/candidates/opg169-a01-s02b-high-port-chain-20260910.md`; SHA-256 `e003bbaeb1dfbe513d42fbf61e479c3173ed490e9c1072713b2373fff3e57900`.
- Executed checker: `research/artifacts/candidates/opg169-a01-s02b-high-port-checker.py`; SHA-256 `549239acee6ed91e57ab941c0d2c0635fc5f9ded2471b2b4cdf881ea9ff9033d`.
- Executed output: `research/artifacts/candidates/opg169-a01-s02b-high-port-checker-output.json`; SHA-256 `b3f74273204459ace40cbbde20021c314f8abe9e76f726d92d503717b3171835`.

The repository checker bytes were explicitly rebound to the executed scratch bytes; its Git blob is `9e41787db9a3189608c0ceac773961071ae0a128`.

## Executed bounded control

```bash
python3 research/artifacts/candidates/opg169-a01-s02b-high-port-checker.py \
  --structural-max 64 \
  --profile-max 12 \
  --word-max 8 \
  > research/artifacts/candidates/opg169-a01-s02b-high-port-checker-output.json
```

The run used CPython 3.13.5 before repository transport. The checker contains two separately implemented algorithms: Kahn deletion plus DFS reachability, and Floyd-Warshall closure for cycle/reachability checks. They agreed on all enumerated complete colorings. Both implementations and the mathematical analysis are from the same research principal, so this is differential candidate control, **not** an independent verifier receipt.

## Scope boundary

The parametric edge-split construction is a proof-drafted unbounded source family. The enumeration is bounded to structural `n<=64`, natural all-one profiles `n<=12`, and all spoke words `n<=8`. No finite row is used as induction or as a global no-pump theorem.

The finite-profile repetition argument applies only when a tail is enclosed by a fixed four-port disk, all internal stars have no exterior contacts, and the needed shortcut/reverse-edge guards are source-valid. Growing interfaces, separating-triangle escape, and repeated complete-star release remain open.

## Failed-route proposal

Route fingerprint `15e82f71ad0336ea4cb82fbd2fc31ae657d5b846e4f2ac4845751c5c601ed4ef` denotes: **finite degree cutoff / raw high-port complexity as a termination strategy**. The parametric family has `d(7)=6+n` and preserves the source geometry and semidegree footprint for every `n`, so every finite degree cutoff misses a child. This blocks that termination strategy; it does not refute the root conjecture or every well-founded high-port measure.

Next research obligation: construct or rule out a source-faithful **growing-interface pump** in which each complete-star release or separator crossing exposes genuinely new exterior ports and evades fixed-interface profile compression.
