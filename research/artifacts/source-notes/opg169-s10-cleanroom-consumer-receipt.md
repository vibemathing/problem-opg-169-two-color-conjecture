# S10 clean-room consumer receipt for S01/S11

`verdict=candidate_only`; `root_closed=false`.

## Base
- fresh protected `main`: `2d9303e7ae9558d3904bb2fa0bade246ebe9bbde`
- direct parent: `8d5bcb4955e84468f58a5923bed7f2ec527a6218`
- ProblemContract SHA-256: `719230edd088c52a5468eed8090579e5eef1bf85d8a56e633350063108f345ec`

## Consumer result
- C37 exact `d(7)=6`: **160/160 PASS**.
  - 156 merged `delete {0,2}` rules.
  - four independently rediscovered merged-search residuals `Y4/0,4,16,20`, all closed by bare `delete 3`.
  - all complete valid Q colourings: **21,732**.
  - equal R+ lifts: **16,536**; strict R+ lifts: **5,196**; failures: **0**.
- S08 P10--P14 under the frozen `ATC_any_old` lane: **5/5 PASS**.
  - profile rows: `144/140/4`, `144/140/4`, `420/330/90`, `396/250/146`, `396/250/146`.
  - possible new directed triangles over the permitted exterior superdomain: `3,3,3,5,5`; all anchored by retained edges on actual directed parent faces.
  - `strict_zero_new`: strong-profile / zero-new / intersection = `6/101/0`, `6/101/0`, `3/113/0`, `3/113/0`, `3/113/0`.
  - P12 `ATC_deleted_only` witness: `V/E/F=13/30/19`, strong-profile `3`, deleted-anchor `140`, intersection `0`.
- S09 remaining guard-child set: **NOT_VERIFIABLE_MISSING_SOURCE**.
  Current main supplies no repository-bound exact remaining S09 registry, row set, or per-row source digests. The only S09 item in C48 is unbound `S09_C5` with digest `40841798d17fc6930c9d9036d1225e7a79c00bd81d9aeacbbdd94df1f6e012f0`, corroborating C37 160/160 rather than identifying the requested remaining child set.

## Required checks
Alias normalization precedes geometry. Faces and deletion holes are derived from rotation. Controlled complete stars are checked. Every accepted rule is strictly smaller and a simple planar orientation; reverse-arc conditions are discharged only by an actual parent edge, a declared complete star, or the exact source-noncofaciality interface where permitted. `valid_Q_count>0`; every complete valid Q colouring is enumerated; each receives a same-boundary valid P lift; both-colour positive reachability satisfies `R_P^+ ⊆ R_Q^+`.

The arbitrary-exterior theorem interface is the full R+ condition. In addition, the frozen run executed 1,800 bounded cofacial return-path gluing canaries; none produced a counterexample.

## Mutation receipt
All 8 required mutants were killed: dropping complete-Q, R+, embedding, reverse guards, complete stars, alias handling, nonvacuity, or strictness admits its dedicated invalid canary.

## Reproduction and frozen run digests
```bash
python3 s10_cleanroom_checker.py --out s10-cleanroom-results.json --glue-cap 100
```

- checker SHA-256 `72300ee37f7f5df7ba28244577ab27c781876f9a2f642223065a30be8e2959a2`
- results-file SHA-256 `e26ddb5b66afc1479e2f5f8634d666a81c5b783471271d054fbacf7e836c3f21`
- semantic result digest `f3dc810615fd1ee01c779e2f5f763c7c62309eea61dbd7e42fe4390e9fd86a20`
- row-status CSV SHA-256 `935fa6f49cd26b9525c96c2fec5b117cf36e79626f0a7f2e4bb954fca8390a6c`

## Trust boundary
Clean-room consumer implementation in this S10 run; no producer checker, producer lift vector, or producer helper was imported. This is not a registered trusted verifier, EvidenceLink, Result, or root closure.

This receipt is consumable by S01/S11 only as candidate-level clean-room corroboration. It does **not** assert a global negative-face join or root closure.
