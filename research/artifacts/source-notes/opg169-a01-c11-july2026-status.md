# C11 source-status note: July 2026 feedback-vertex-set result

Verdict: candidate_only. Source discovery and scope comparison only.
Problem: problem:opg-169-two-color-conjecture
Base: 8689bd5701f791cb2e3bada7e85c23e49bf4a8d9
Retrieved: 2026-09-06.

Primary source: Simon Dreyer, Feedback vertex sets in oriented graphs,
arXiv:2607.13895v1.
https://arxiv.org/abs/2607.13895
https://arxiv.org/html/2607.13895v1

The introduction states the planar two-acyclic-set partition as
Conjecture 3 and describes it as open. Corollary 9 concerns a feedback
vertex set of size at most (2n+m)/9, and hence (5n-6)/9 for planar
orientations with n>=3. This is not an acyclic bipartition: the theorem
does not require the removed feedback vertex set itself to be acyclic.
The paper is a recent primary research source, not an admission receipt
for either its theorem or this repository's root.

The bounded searches in this continuation found no primary-source full
solution to the frozen root. This is a search-coverage statement, not a
proof that no later or unindexed solution exists. It does not change
the frozen contract, stop the research, or claim novelty.

Other sources used in the mathematical cycle: the cited Steiner paper
in C11 and the low-vertex color-transfer source in C10. The 2026 list
Erdos-Neumann-Lara paper recorded by C09 has different quantifiers and
does not supply the planar two-color theorem. No claim is made that
a local SAT enumeration or a mathematical verifier was executed.

Next source check: compare any claimed stronger extension theorem
against its root-conjecture assumptions before using it to eliminate
the all-equal exterior profile.
