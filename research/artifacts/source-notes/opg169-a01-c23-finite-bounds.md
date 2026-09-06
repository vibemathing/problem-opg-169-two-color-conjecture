# C23 source-faithfulness note: two distinct finite bounds

Verdict: candidate_only. Retrieval: current C23 research cycle.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Target: obligation:opg169-strong-min-degree-three
Base: 47e284ea38aa1fa0afb9deb721d1e542dffae850

## A. Directed coloring through order 26

Kolja Knauer and Petru Valicov, Cuts in matchings of 3-connected cubic
graphs, European Journal of Combinatorics 76 (2019), 27-36.
DOI: 10.1016/j.ejc.2018.09.004.
arXiv:1712.06143v3, revised 7 September 2018.
https://arxiv.org/abs/1712.06143
https://arxiv.org/pdf/1712.06143

Conjecture 4 has the frozen planar-orientation quantifiers.
Proposition 4, printed page 10 (PDF index 9), asserts it through 26
vertices. That page was read as a screenshot. Section 4 describes
a Sage-based computation and a duality reduction from cubic order 48.
This is a published finite theorem, not our executed certificate.
The nearby 27- and 39-vertex statements have additional connectivity
and degree hypotheses and are not used.

## B. Undirected Hamiltonicity through cubic order 36

D. A. Holton and B. D. McKay, The smallest non-Hamiltonian 3-connected
cubic planar graphs have 38 vertices, J. Combinatorial Theory B 45(3)
(1988), 305-319. DOI: 10.1016/0095-8956(88)90075-5.
https://www.sciencedirect.com/science/article/pii/0095895688900755
Author-hosted scan with appended erratum:
https://users.cecs.anu.edu.au/~bdm/papers/HoltonCubic38.pdf

The primary publisher abstract states Hamiltonicity for all
3-connected cubic planar graphs of order at most 36.
The appended 1989 erratum, JCTB 47, 248,
DOI 10.1016/0095-8956(89)90025-7, adds a case to the 38/40/42-vertex
classification. Its parsed text was read. No classification beyond
the 36-vertex threshold is used here.

## C. Access and verification limits

The Knauer-Valicov Proposition 4 screenshot was obtained. Rendering
its later table and the Holton-McKay scan did not succeed. The latter
bound is sourced to the primary publisher's indexed abstract, not to
an asserted full reading of the scanned proof. The author-hosted
erratum was accessible as parsed text. A bounded local reference
download also failed; no PDF-byte digest is claimed.

No source program, graph catalog, dependency environment or computation
was replayed. No mathematical certificate or EvidenceLink was produced.
A future source-admission review must assess both cited finite theorems,
their proofs/computations, and the exact planar-dual bridge in C23.
The following proof candidate explicitly depends on these two source
statements. This note does not claim that they are newly proved here.

The statements have different roles: the first bounds the size of an
oriented counterexample; the second, via a separately supplied argument,
bounds a planar graph not partitionable into two induced forests.
Neither statement by itself settles the unbounded root.
