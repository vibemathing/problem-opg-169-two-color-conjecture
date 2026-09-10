# R08 S02-B Cycle 3 source note — TERMINAL-USEFULNESS

Status: `candidate_only`; `root_closed=false`.

Fresh protected main used for the final mathematical source read:
`6b34ce7f7ce83b238bebd85babd7aaff6f40a3d0`.

Transport was subsequently rebased onto protected main
`ea8148a64703c6d29831d07c83001a4988ab80c1` after concurrent S01 Cycle 5 landed.
That S01 commit explicitly imports no S02-A theorem and leaves the live
termination gates as normalized source resolution plus mathematical progress;
it does not supersede the frozen Cycle-3 stress result.

Repository-bound predecessors consumed:

- S02-B Cycle 2 merge `3bec7e8d2c4fec368707f3f86cccfc7af8120472`, which leaves history-aware discovery well-foundedness alive but explicitly does not prove terminal reducibility.
- S01 Cycle 4 integration `a2a9973d2f995de71095a6bea814cbe882cb7718`, which imports that separation and keeps GSRC/JMAP unknown.
- S01 Cycle 5 `ea8148a64703c6d29831d07c83001a4988ab80c1`, which renames the unresolved termination gates `TNORM` and `TPROG`; discovery termination alone remains insufficient.
- C37 exact `d(7)=6` material is not extrapolated to this family.

Cycle-3 construction `T_N` is a new root-class stress family. It is proved/checked only as a finite simple plane triangulation orientation with minimum semidegree at least two, actual rotations/faces, unbounded pole degree, no separating triangle, a growing A-star sweep interface, and same-boundary ordinary-extension irreducibility for consecutive A-star blocks of sizes 1, 2 and 3.

It is **not** repository-bound as an exact C37 higher-degree descendant, LSRC realization, GSRC occurrence, JMAP/`L_join` child, C45/C46 descendant, or S14/AE/M12 cap. Any future source theorem may exclude it; that exclusion would itself be source-specific TERMINAL-USEFULNESS information.

Frozen candidate identities:

- proof/report SHA-256: `9d586e7ae6abb04a823b9165462d0799c68bc931e49ee2dff7bc71030f1d2bbd`
- checker SHA-256: `ccfaf917f11df1d146ca28f99d314601a5bc76643d9faddc2d178514b0a88fcc`
- checker output SHA-256: `f66a8f3c51a6b9571d6ca51eda0a57a883ca57af056566808650a48103f6d504`

Exact bounded computation:

- structural canary: every even `N=6,8,...,64`;
- `N=64`: 130 vertices, 384 edges, 256 faces, pole degree 64, minimum semidegree 2, zero nonfacial 3-cycles;
- exact A-sweep formula checked through `t=N-2`: `|B_t|=t+4`;
- strict same-boundary oriented replacement candidates exhausted over both parity classes:
  - one-star: `40` total;
  - two-star: `10,976` total;
  - three-star: `9,547,584` total;
  - grand total: `9,558,600`;
- successful ordinary-extension replacements: `0`.

Trust boundary: the checker, topology generator, embedding/face tracer and colouring test are all same-principal candidate-generation code. This is exhaustive finite control in the stated search space, not a registered independent verifier receipt. No EvidenceLink, Result, Solution or root closure is claimed.

Live consequence: history-aware well-foundedness does not imply local usefulness at block size at most 3 in this root-class model. The next adversarial target is to pump the local-hardness radius to arbitrary `r`; the positive alternative is a source-faithful uniform usefulness lemma at some finite `r>=4`.
