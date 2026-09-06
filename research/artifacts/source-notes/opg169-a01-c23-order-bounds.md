# C23 source-faithfulness note: two bounded-order inputs

Verdict: candidate_only. No published computation was replayed.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Base: 47e284ea38aa1fa0afb9deb721d1e542dffae850

## KV26

Kolja Knauer and Petru Valicov, Cuts in matchings of 3-connected cubic
graphs. arXiv:1712.06143v3, submitted version dated 7 September 2018;
the manuscript title page is dated 10 September 2018.
https://arxiv.org/abs/1712.06143
https://arxiv.org/pdf/1712.06143v3

Conjecture 4 is the planar-orientation two-acyclic-partition statement.
Proposition 4, printed page 10, asserts it through order26. Section4.3
describes testing orientations via perfect matchings and cuts in
non-Hamiltonian planar cubic graphs through order48, then planar duality
and edge deletion transfer the bound to all planar orientations.
The program uses SageMath; supplementary code is described as available
from the publisher or authors. The proof candidate uses the published
bound, not a newly checked dataset or execution receipt.

The PDF text, Proposition4 and surrounding computation discussion were
read on 2026-09-06; pages indexed8 and9 were rendered. Later rendering
requests for Table1 at index10 failed with cache-miss responses. No
table image or graph data was reconstructed or used as an executed check.
The restricted order27/order39 corollaries do not apply unconditionally.

## HM36

D. A. Holton and B. D. McKay, The smallest non-Hamiltonian 3-connected
cubic planar graphs have 38 vertices. JCTB45(3), 305-319 (1988).
DOI: 10.1016/0095-8956(88)90075-5.
https://www.sciencedirect.com/science/article/pii/0095895688900755

The primary publisher abstract states Hamiltonicity through order36
for cubic 3-connected planar graphs. The same minimum38 bound is
explicitly cited in the introduction of Knauer--Valicov v3.
The 1989 erratum entry, DOI10.1016/0095-8956(89)90025-7, was located;
its text was not obtained. We do not claim a full original-proof or
erratum audit. HM36 is the precise published premise used in C23.

McKay's primary plane-graph page was also opened:
https://users.cecs.anu.edu.au/~bdm/data/planegraphs.html
Its non-Hamiltonian section lists six order38 graphs with no triangular
faces, in planar-code format. No binary graph list was decoded and no
enumeration completeness or Hamiltonicity certificate was replayed.

## Relation to the root

HM36 is an undirected Hamiltonicity theorem, not the root. C23 supplies
the Jordan-curve bridge to bounded-order induced forests. That is a
stronger sufficient coloring property. KV26 is a bounded special case
of the root, not a general resolution. Both remain explicit sources,
not EvidenceLinks or admitted results in this repository.
