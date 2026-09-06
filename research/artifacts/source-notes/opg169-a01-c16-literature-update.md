# C16 source-faithfulness update, 2026-09-06

Verdict: candidate_only. Source discovery and statement comparison only.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: d90ba0a2be0dc58ae8fe2cd70c788f8290f7ab12

## 1. New July 2026 primary source

Simon Dreyer, Feedback vertex sets in oriented graphs.
arXiv:2607.13895v1; submitted 2026-07-15.
https://arxiv.org/abs/2607.13895
https://arxiv.org/html/2607.13895v1

The primary abstract and HTML introduction were read on 2026-09-06.
Conjecture 3 states the same planar-orientation two-acyclic-partition
question and the following paragraph says that it remains open in general.
Corollary 9 gives a planar feedback-vertex-set bound (2n+m)/9,
and hence (5n-6)/9 when the simple-planar edge bound applies (n>=3).

Statement relation to root: weaker/different optimization target, not a
proof of two-colorability. A feedback vertex set has acyclic complement;
the set itself is not required to induce an acyclic digraph. The paper
therefore does not supply the second acyclic part demanded by the contract.
No claim that its proof was mechanically or separately verified is made.
The degree-5/6 elimination headings refer to its own extremal problem,
not automatically to minimum counterexamples to our root.

No PDF figure was analyzed or copied for this note.

## 2. A similarly named April 2026 result has different quantifiers

A. Harutyunyan, L. Picasarri-Arrieta, G. Puig i Surroca,
On the list version of a conjecture of Erdos and Neumann-Lara.
arXiv:2603.01020v2; revised 2026-04-14.
https://arxiv.org/abs/2603.01020

The primary abstract proves a list-coloring version of a different
conjecture: a sufficiently large list chromatic number guarantees the
EXISTENCE of an orientation with large list dichromatic number.
This does not prove that EVERY orientation of EVERY simple planar graph
has ordinary dichromatic number at most two. Neither the quantifier
direction nor the coloring notion matches. Relation: different statement.

The version read is v2, not just the earlier March 2026 submission.

## 3. The global semidegree theorem used in C14

Lucas Picasarri-Arrieta, Strengthening the Directed Brooks' Theorem for
oriented graphs and consequences on digraph redicolouring.
arXiv:2301.04881v2; revised 2023-05-25.
https://arxiv.org/abs/2301.04881

The primary abstract defines Delta_min as max_v min(d+(v),d-(v)),
and asserts dichromatic number at most Delta_min for oriented graphs
when Delta_min>=2. C14 uses this as a source-reuse statement: if every
vertex has one semidegree at most two, a non-two-colorable orientation
cannot occur (the case Delta_min<=1 has the elementary deletion proof).
Thus a counterexample must contain a vertex with both semidegrees >=3.

This is a GLOBAL maximum parameter. It does not allow extension at any
specified degree-5 vertex and is not a substitute for a boundary table.
No theorem replay or new mathematical receipt is supplied.

## 4. Special classes and equivalent formulations

S. Cambie, F. Dross, K. Knauer, H. La, P. Valicov,
Partitions of planar (oriented) graphs into a connected acyclic and
an independent set, arXiv:2412.11774v2; revised 2025-10-29.
https://arxiv.org/abs/2412.11774
The abstract gives CAI partitions for specific bipartite subcubic and
series-parallel settings. It also gives an obstruction to a stronger
Eulerian-triangulation approach. These domains/partition conditions do
not directly settle the full frozen root. Relation: special-class results.

Raphael Steiner, A Note on Graphs of Dichromatic Number 2.
DMTCS 22:4, paper 11, published 2021-01-05.
https://dmtcs.episciences.org/7040
DOI: 10.23638/DMTCS-22-4-11.
The journal abstract gives equivalence with the corresponding assertion
for oriented K5-minor-free graphs. An equivalent assertion is not an
unconditional theorem asserting the root. C11's specific gluing arguments
are audited separately and are not replaced by an assumed precoloring theorem.

## 5. Search scope and limitation

Bounded search queries included Neumann-Lara/planar/2026,
Neumann-Lara/planar/2025/solved, and planar digraphs/two-colour/2026.
An AI-reviewed problem mirror and unrelated search hits were not used
as mathematical authorities. Primary arXiv and journal records above
were opened to compare dates, statements, and quantifiers.

No matching complete solution was located in this bounded search.
This is not a proof that no later source exists and does not justify
stopping the proof effort. The new local tables in C16 are direct
candidate derivations, not claims inferred from bibliographic status.

best_verified_result: none
next_action: continue the constrained plane-core coloring proof while
preserving both acyclicity requirements and all terminal quantifiers.
