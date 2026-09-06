# C01 source and statement-faithfulness note

Verdict: candidate_only. Retrieved: 2026-09-06.
Binding: attempt:web-20260906-opg169-a01 /
route:minimal-counterexample-structure-v1 /
obligation:opg169-strong-min-degree-three.

## Primary sources and comparison

1. Bojan Mohar, Eigenvalues and colorings of digraphs, preprint dated
May 18, 2009, Section 2, printed page 3 (PDF page index 3).
https://www.sfu.ca/~mohar/Reprints/Inprint/BM09_LAA09_Mohar_EigenvaluesandColorings.pdf
The PDF text and page rendering were inspected. Lemma 2.1 gives the
SCC maximum rule for dichromatic number. Lemma 2.2 gives both semidegree
bounds k-1 at a critical vertex. Relation: stronger general setting.
The source permits digons; our contract does not. The candidate does not
silently equate vertex-minimality with arc-minimality. To use k=3 one must
also justify that coloring G-v and giving v a third color implies chi(G)=3.
C01 avoids relying on that extra bridge by giving direct two-color proofs.
No source PDF digest or formal-library certification is claimed.

2. Zhentao Li and Bojan Mohar, Planar digraphs of digirth four are
2-colourable, arXiv:1606.06114, abstract inspected.
https://arxiv.org/abs/1606.06114
The result assumes digirth at least four. Our contract permits directed
triangles. Relation: weaker than the root domain; not used to close it.
This distinction must not be replaced by the assertion that planarity
alone excludes the possible return paths through a restored vertex.

## Search scope and source hygiene

Bounded web searches targeted planar two-coloring, critical digraphs,
SCCs and semidegree. Unrelated search hits were discarded. The repository
knowledge-source and operator registries were read. Formal-package entries
are constrained or design-only; no formal package was imported or built.
Only locators and short paraphrases are retained, not copied papers.
The claims in C01 are elementary derivations under the frozen axioms,
with no appeal to an unexamined theorem or presumed current problem status.

## Contract audit

A color class must induce a digraph containing all arcs with both endpoints
in it; this is not a selected acyclic spanning subdigraph. Unused colors
are allowed in the coloring convention. A directed cycle is not an
undirected cycle. Deletion never changes the direction of a retained arc.
Minimality is over vertex counts in the full frozen planar-orientation
class, not over a fixed drawing or an arbitrary restricted subclass.

Snapshot and ProblemContract digests used for transport are manifest
declarations. Candidate-content hashes are separate transport metadata.
No mathematical command runtime, kernel replay or semantic-verifier
receipt is asserted. The profile's historical pending-smoke strings are
not edited; live main protection and the existing successful transport
run were read instead. Neither observation is mathematical evidence.
