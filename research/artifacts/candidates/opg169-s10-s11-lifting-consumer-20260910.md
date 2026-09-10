# S10 Cycle 2 — theorem-content consumer for ordinary arbitrary-exterior lifting

Verdict: `candidate_only`. `root_closed=false`.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`
Problem: `problem:opg-169-two-color-conjecture`
Attempt: `attempt:web-20260906-opg169-a01`
Route: `route:minimal-counterexample-structure-v1`
Graph: `graph:opg169-initial-v1`
Target: `obligation:opg169-root`
Frozen source base: `b742c72f1d50849bd074f1f7f7f6e2ed019870c4`

This is an S10 consumer audit. It does not claim a repository-bound S11 artifact exists, and it does not rename older producer arguments as independent S11 verification.

## 1. Fresh source/admission result

At the frozen base there is no branch, pull request, candidate file, packet, or Issue-bound locator carrying an S11 lifting theorem. S01 Cycle 3 explicitly records that no S11 lifting theorem has been imported and keeps `LIFT-O` UNKNOWN.

Therefore:

```text
S11_ARTIFACT_BINDING = NOT_VERIFIABLE_MISSING_SOURCE
LIFT_O_THEOREM_CONTENT = PASS(candidate, repository-derived)
LIFT_O_TRUSTED_VERIFICATION = UNKNOWN
```

The theorem-content PASS below is a clean statement/proof audit against already repository-bound sources. It is not a claim that the absent S11 producer output has been consumed by identity.

## 2. Smallest ordinary Replacement Lifting Lemma

Let `P,Q,F` be finite digraphs and let `B` be a finite boundary set. Assume:

1. `V(P) ∩ V(F) = B = V(Q) ∩ V(F)`.
2. There are no arcs between `V(P)\B` and `V(F)\B`, and no arcs between `V(Q)\B` and `V(F)\B`. Equivalently, every exterior contact of either patch is represented through a vertex of `B`.
3. Shared boundary arcs are owned consistently: if the same arc is present in two pieces its direction agrees and the union counts it once. `P∪F` and `Q∪F` are actual digraph unions; an opposite boundary arc is a class-preservation failure, not a lifting case.
4. Boundary aliases have already been quotiented, so `B` is the actual vertex set after all source-valid identifications.
5. A valid colouring means that each full induced colour class is acyclic. For a valid patch colouring `c`, let
   `R_X^+(c)` be the set of ordered pairs `(u,v)` of boundary vertices joined in `X` by a positive-length monochromatic directed path. Empty paths are excluded.
6. For every valid complete colouring `d` of `Q`, there exists a valid complete colouring `c` of `P` such that
   `c|B=d|B` and, for both colours,
   `R_P^+(c) ⊆ R_Q^+(d)`.

Then every valid colouring of `Q∪F` has a valid colouring lift to `P∪F` which keeps every vertex of `F` fixed.

### Proof

Take a valid colouring `D` of `Q∪F`. Its restrictions `d=D|Q` and `f=D|F` are valid. By hypothesis choose a valid `P` colouring `c` with the same boundary colours and `R_P^+(c)⊆R_Q^+(d)`. Glue `c` to `f`.

C13's exact gluing criterion says that, for a fixed colour and two pieces meeting exactly in `B`, the union is valid iff the positive transitive closure of the union of the two boundary-reachability relations has no diagonal entry. Since `Q∪F` is valid,

```text
tc+(R_Q^+(d) ∪ R_F^+(f))
```

has no diagonal. If `P∪F` were invalid, then

```text
tc+(R_P^+(c) ∪ R_F^+(f))
```

would have a diagonal. Monotonicity under `R_P^+(c)⊆R_Q^+(d)` would give the same diagonal in the first closure, contradiction.

Thus the lifted union is valid. No topology of `B` was used.

## 3. Edge-case audit

The proof covers the S11 mission edge cases as follows.

- **Repeated boundary visits.** C13 cuts a crossing cycle at successive boundary visits, producing a nonempty cyclic chain of positive relation entries. No simplicity of the visit sequence is assumed.
- **Boundary-owned edges.** A boundary arc is itself a positive path. It may be owned by one piece or shared consistently. The relation records it; no edge is silently discarded.
- **Zero-length hazards.** `R+` excludes empty paths. Every relation segment has positive length. A positive closed walk, not an empty walk, is produced.
- **Disconnected patches.** Connectivity is unused. Missing connections merely produce missing relation entries.
- **Pinched/two-terminal/multi-region interfaces.** `B` is an arbitrary set, not a simple boundary cycle. The C34 alias cases with two complementary regions sharing a port are within the theorem.
- **Aliases.** They must be normalized before `B`, ownership, and `R+` are computed. Treating two aliases as distinct terminals changes the theorem instance and is invalid.
- **Reused vertices/edges.** Expanded relation chains may reuse paths. A finite positive directed closed walk still contains a directed cycle.
- **All exterior contacts.** The theorem is inapplicable if an internal patch vertex has an unrecorded arc to an exterior-only vertex. Complete-star/saturation claims in source rows are ownership certificates for this condition.

## 4. Theorem versus minimal-counterexample corollary

Strict order decrease, planarity, simplicity, orientation, and reverse-arc guards are not logical hypotheses of the colouring-lifting implication itself. They are required to invoke minimum-order counterexample minimality.

Corollary: if `Q∪F` is an orientation of a finite simple planar graph with strictly fewer vertices than `P∪F`, then minimum-order noncolourability of `P∪F` is contradicted by the lemma.

For consumer-table acceptance S10 additionally retains `valid_Q_count>0`. This is a nonvacuity guard on certificates. In a genuine minimality application, existence of a valid whole `Q∪F` colouring follows from strict smaller-order membership in the frozen root class.

## 5. Complete tournament / triangle specialization

Ordinary same-boundary extension is sufficient only under an exact common tournament interface.

Assume the same tournament `K` on `B` is contained with identical arc directions in both `P` and `Q`. Fix a valid colouring of either patch. Within one colour, the same-coloured boundary vertices induce an acyclic tournament, hence a transitive tournament. For any same-coloured distinct `u,v`, the direct tournament arc supplies exactly the forward reachability direction; a positive path in the reverse direction would close a directed cycle with that arc. Therefore the full positive boundary relation is determined solely by the boundary colours and the common tournament orientation.

Consequently any valid ordinary same-boundary lift from `Q` to `P` automatically has
`R_P^+=R_Q^+`. This is the replacement specialization behind the tournament-gluing lemma used in C11.

This shortcut is invalid when the common interface is not complete, when `P` and `Q` do not retain the same tournament orientation, or when aliases change the actual boundary vertex set. In particular, ordinary extension is not sufficient on a generic two-terminal interface: a `u→v` return in `P` missing from `Q` can combine with an exterior `v→u` return to create a new monochromatic cycle.

## 6. Repository source and ownership chain

The theorem content is repository-derived through the following chain.

1. **C13 boundary automaton** — `research/artifacts/candidates/opg169-a01-c13-boundary-automaton.md`.
   It defines positive `R`, requires pieces to meet exactly in `B`, forbids arcs between disjoint interiors, requires shared-arc direction agreement, and proves the exact gluing iff criterion. This is the primary generic theorem source.
2. **C31 strip reduction** — `research/artifacts/candidates/opg169-a01-c31-strip-reduction.md`.
   It turns profile inclusion into a one-sided smaller-patch lift, makes boundary-edge ownership explicit, permits exterior boundary edges, and separates reverse-arc/class-preservation guards from the lifting proof.
3. **C34 nine-donor proof** — `research/artifacts/candidates/opg169-a01-nine-donor-proof-20260908.md`.
   It states `G=P∪F`, includes all remaining vertices/arcs in `F`, counts shared boundary arcs once, uses saturated internal stars to exclude hidden cross-interior contacts, and explicitly proves the theorem on a pinched two-region interface.
4. **S06/C37 universal fan backtrace** — `research/artifacts/candidates/opg169-a01-s06-c05-universal-fan-backtrace.md`.
   It instantiates exact-boundary ownership using complete stars and all exterior arcs, and quantifies over every complete valid `Q` colouring with `R_P^+⊆R_Q^+`.
5. **C48 parent dominance** — `research/artifacts/candidates/opg169-a01-c48-live-frontier-proof.md`.
   It packages the same implication as exact-parent precedence. Its phrase “same controlled region” is not, by itself, a sufficient standalone ownership contract; the C13/C31/C34 ownership conditions must be inherited.
6. **S10 clean-room receipt** — `research/artifacts/source-notes/opg169-s10-cleanroom-consumer-receipt.md`.
   It independently reconstructs the finite C37/S08 table semantics and kills mutations removing complete-Q, `R+`, embedding, reverse guards, complete stars, aliases, nonvacuity, or strictness.
7. **S01 Cycle 3** — `research/artifacts/candidates/opg169-a01-s01-cycle3-source-cut-repair-20260910.md`.
   It correctly leaves `LIFT-O` UNKNOWN at theorem/verification level and requires S11+S10.

External prior art is narrower. Steiner's Lemma 1 states that two acyclicly coloured digraphs intersecting in a tournament glue acyclicly when their colours agree on the tournament, and attributes the lemma to Li and Mohar (2017). That supports the complete-tournament specialization, not the generic arbitrary-boundary `R+` replacement theorem.

## 7. Ownership admission checklist for any row

S10 may consume a proposed reduction through this theorem only after all of the following are source-bound:

```text
actual alias quotient
actual boundary vertex set B
P-internal vertices
Q-internal vertices
all exterior-contact vertices
all arcs owned by P / Q / exterior / shared boundary
shared-arc orientation agreement
no unrecorded internal-to-exterior arc
complete valid-Q quantifier
same-boundary valid-P lift
both-colour positive R+ inclusion
class-preservation guards
strict order decrease for minimality
```

A missing item yields `UNKNOWN` or `NOT_VERIFIABLE_MISSING_SOURCE`, never PASS.

## 8. Consumer disposition

```text
S11_ARTIFACT_BINDING: NOT_VERIFIABLE_MISSING_SOURCE
LIFT_O_THEOREM_CONTENT: PASS(candidate)
OWNERSHIP_CONTRACT: PASS(candidate, conditional on row source)
TOURNAMENT_SPECIALIZATION: PASS(candidate)
GENERIC_ORDINARY_ONLY_SHORTCUT: FAIL
TRUSTED_VERIFIER_RECEIPT: absent
EvidenceLink: absent
Result: absent
root_closed: false
```

This changes no global join, GSRC/JMAP, B-criticality, termination, S09 source registry, two-terminal structural theorem, anchored-lane conversion, or root status.
