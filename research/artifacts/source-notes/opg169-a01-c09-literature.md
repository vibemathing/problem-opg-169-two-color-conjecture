# C09 source audit: planar dichromatic number and scope boundaries

Verdict: candidate_only. Retrieval date: 2026-09-06.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Base: 869d6a64d909993ab853a16a1b4ca1f98fec68b5

## S1. Conditional precoloring is not an unconditional reduction

Raphael Steiner, A Note on Graphs of Dichromatic Number 2.
DMTCS 22:4, article 11; published 2021-01-05.
DOI: 10.23638/DMTCS-22-4-11; HAL hal-02178422v3.
https://dmtcs.episciences.org/7040
https://dmtcs.episciences.org/7040/pdf

Published Proposition 1, page 2, compares the planar conjecture with
stronger triangle-precoloring formulations. Corollary 1, page 5, assumes
the conjecture before asserting extension of an edge precoloring or
a non-monochromatic triangle precoloring. These statements cannot be
imported as unconditional lemmas to close our two-cut argument.
Lemma 1 on page 2 concerns gluing acyclic colorings along a common
tournament; unlike the precoloring assertion, its gluing rule is usable
without assuming the conjecture. C10 will supply its own direct proof.
Relation: prior_art and explicit conditional scope comparison.

## S2. Low-vertex color shifting

J. Bang-Jensen, T. Bellitto, M. Stiebitz and T. Schweser,
Hajos and Ore constructions for digraphs, arXiv:1908.04096v1,
submitted 2019-08-12.
https://arxiv.org/abs/1908.04096
https://arxiv.org/pdf/1908.04096

Proposition 13, printed page 13, records one occurrence of each color
on each directed side of a missing low vertex, and transfer of a
neighbor's color to that vertex. Theorem 11 gives a broader low-block
classification for k-critical digraphs. The paper's criticality tests
ALL proper subdigraphs. Our saturated representative need not be
arc-critical, so that premise must not be silently inherited.
The next candidate instead proves the needed two-color transfer,
triangle and diamond arguments directly from vertex minimality.
Relation: prior_art; no unproved criticality bridge imported.

## S3. Digirth-four result is a special class

Zhentao Li and Bojan Mohar, Planar Digraphs of Digirth Four are
2-Colorable, SIAM Journal on Discrete Mathematics 31 (2017), 2201-2205.
DOI: 10.1137/16M108080X.
https://epubs.siam.org/doi/10.1137/16M108080X

This proves acyclic two-colorability when directed triangles are absent.
Our frozen class allows those triangles. Folding and shortcut operations
must not be claimed to preserve this stronger digirth hypothesis.
Relation: special-class result, not root closure.

## S4. Published finite bound, not a run of this agent

Kolja Knauer and Petru Valicov, Cuts in matchings of 3-connected
cubic graphs, arXiv:1712.06143v3, revised 2018-09-07.
https://arxiv.org/abs/1712.06143

The abstract reports the conjecture for all planar graphs on at most
26 vertices. This is a published source claim, not a SAT certificate
replayed or generated here. This audit does not assert that 26 is the
best current bound. No local enumeration bound is recorded.
Relation: prior_art, finite scope only.

## S5. The 2026 similarly named conjecture is different

Ararat Harutyunyan, Lucas Picasarri-Arrieta and Gil Puig i Surroca,
On the list version of a conjecture of Erdos and Neumann-Lara,
arXiv:2603.01020v2; submitted 2026-03-01, revised 2026-04-14.
https://arxiv.org/abs/2603.01020

Its conclusion chooses an orientation with large list dichromatic
number when the underlying list chromatic number is large.
That existential orientation statement is not our universal planar
two-color bound. It supplies no root proof or planar counterexample.
Relation: different statement; not applicable for closure.

## Coverage and limitations

Bounded searches covered the conjecture name, planar dichromatic
number, 2026 resolution claims, minimal counterexamples, precoloring,
low-degree shifting and finite bounds. No retrieved primary source
supplied a full proof or counterexample for the frozen root. This is
not an exhaustive claim about all literature.

Parsed text and exact proposition locations were read. PDF screenshot
requests for the Steiner corollary page and the Hajos/Ore color-shifting
page returned tool errors. No figure-dependent edge list or diagram
interpretation is claimed. Only bounded paraphrases and locators are
retained. External search, this audit and transport CI are not Evidence.
