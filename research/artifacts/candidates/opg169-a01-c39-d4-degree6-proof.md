# C39: first D/19 degree-six port-4 layer

Verdict: candidate_only. Status: proof-drafted with bounded exact controls.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Target: obligation:opg169-root
Base: a7821429de61e4e8aa397838e5bb42e3eeaeb2a4 (merged C38/PR46).

## 1. Frozen scope and reused distinctions

Only the local D/19 orientation from C38 is used. In C38 notation x=12 is next to 11 and y=13 is next to 8, with
11->12, 13->12, 13->8, 12->7, 7->13,
so 7->13->12->7 is retained. The old controlled vertices are 0,2,3,7; this turn additionally controls vertex 4 and assumes d(4)=6. Vertices 0,2,3 have complete degree-five stars and 7 has its complete degree-six star. All exterior colours outside the explicitly controlled set stay fixed in every lift.

The named S02/S11/S03 handoffs were searched by exact labels in current main/Issue state but no separately citable original expert artifact was found. No expert approval is invented. The following content is absorbed only where it is independently rechecked from frozen arcs:
- the five-old-port forcing observation already reconstructed in C38;
- the distinction between strong profile failure, ordinary nonextension, and relation-only failure;
- the fact that C35's six L/N/P arithmetic families do not constitute a geometric coverage theorem.

No C36 d(7)=5 table, nine-donor table, old three-point direct restoration, uniform-width recolouring route, or C38 degree-four x/y release is rerun here.

## 2. Actual degree-six star of 4 and all allowed identities

The old rotation at 4 is (0,5,8,3). For d(4)=6 write the two ordered additional neighbours q,r, so the complete rotation is
(0,5,q,r,8,3).
The actual added faces are
(5,4,q), (q,4,r), (r,4,8).
This turn fixes the first face direction
4->5->q->4.
Thus 5->q and q->4 are fixed. The remaining direction word has three bits:
bit0: q->r (else r->q);
bit1: r->8 (else 8->r);
bit2: r->4 (else 4->r).

The star entries q,r are distinct. They cannot be 0,2,3,4,5,7,8 because of simplicity or already complete controlled stars. Before geometry checks, each is therefore one of 6,11,12,13 or a genuinely new vertex; there are 21 ordered identity patterns.

Exact facial-link and edge-count checks remove ten patterns:
- q=6 in four choices closes the actual link at vertex 5 with degree three;
- (11,6), (12,11), (13,12) conflict in stipulated facial successors;
- (12,6), (13,6), (13,11) leave 11 vertices and 28 different underlying edges, exceeding the simple planar bound 27.
Exactly eleven identity types remain:
(11,12),(11,13),(11,new),(12,13),(12,new),(13,new),(new,6),(new,11),(new,12),(new,13),(new,new).
Existing directed edges reject some of the eight words. Exactly 70 compatible labelled direction types remain.

This classification is for the stated complete d(4)=6 star only. A `new` vertex may have arbitrary further exterior neighbours; they are not silently discarded.

## 3. Tested replacement family and six complete reductions

For each of the 70 compatible types let
I={0,2,3,4,7}
and let B be every local vertex outside I. For each v in I the tested smaller graph is the literal induced deletion Q=P-v. No arc is added, reversed, contracted or identified. Surviving vertices in I may be recoloured simultaneously; every B colour, and hence every exterior colour, stays fixed.

For every valid COMPLETE colouring of Q the checker asks for a complete colouring of P with the same B colours and
R_P subseteq R_Q,
where R is the full positive monochromatic reachability relation on B. This is the strong profile condition required for arbitrary-exterior composition.

Exactly six of the 70 direction types have a successful deletion:

| q | r | word | one successful deletion | scope |
|---|---|---:|---|---|
|11|12|1|delete 4|all 212 valid Q colourings lift, R equal|
|11|13|3|delete 4|all 240 lift; 238 equal R, 2 strict decreases|
|new|6|4|delete 3|all 360 lift; 356 equal, 4 strict|
|new|6|5|delete 3|same counts|
|new|6|6|delete 3|all 468 lift; 452 equal, 16 strict|
|new|6|7|delete 3|all 468 lift; 452 equal, 16 strict|

Other deletions also work for some of these rows; the table lists only one minimal literal deletion. Every successful operation decreases the graph order by exactly one and preserves finite/simple/planar/oriented by induced deletion.

For an arbitrary exterior F, take any valid colouring of the smaller whole graph. Its Q restriction is a valid table input. Choose the certified P colouring and keep F fixed. Any new crossing monochromatic directed cycle splits into positive P/F boundary paths. Replacing every P segment by its certified Q path creates a positive monochromatic closed walk in the originally valid smaller graph, hence a directed cycle, contradiction. Thus these six signed local configurations cannot occur in a vertex-number-minimum counterexample, conditional on the separately scoped prior structural candidates.

This is a six-type exclusion, not elimination of all d(4)=6 or all D/19 configurations.

## 4. Strong versus ordinary failure: the coverage matrix

The five literal deletions were audited with two separate failure notions.
For a valid Q colouring:
- `ordinary_nonextension` means there is no acyclic P colouring with the same boundary colours at all;
- `relation_only` means an ordinary same-boundary P colouring exists, but every such colouring adds some positive boundary reachability, so no R_P subseteq R_Q lift is available.

Across the 70 compatible direction types, classifying a type by its best tested deletion gives:
- 6 `strong_profile`: at least one deletion has no failed valid Q input;
- 48 `ordinary_only`: at least one deletion has ordinary extensions for every valid Q input, but every tested deletion has at least one relation-only failure;
- 16 `ordinary_failure`: every tested deletion has at least one valid Q input with no ordinary same-boundary extension.

This is the explicit coverage matrix for THIS deletion family. It does not classify other gadgets, expanded separators, or contractions.

The lexicographically first still-open profile type is (q,r,word)=(11,12,3), i.e.
5->11, 11->4, 11->12, 12->8, 4->12.
For deletions 0,2,3,4,7 respectively, the numbers of valid Q inputs are 240,300,276,240,296. Their profile failures are 2,2,2,2,32, and EVERY ONE of these failures is relation-only: ordinary same-boundary extension exists for all valid Q inputs. Thus the first lost quantifier here is positive-reachability containment, not ordinary colourability.

That observation selects the next route: change the interface/replacement so that boundary reachability is controlled more tightly. Repeating the same five literal deletions cannot close this row.

## 5. Complete DC2 accounting for the expanded star

No transfer rule changes. On the ORIGINAL graph,
gamma(v)=(d(v)-4-2t(v))/d(v),
mu(f)=length(f)-4+sum_corners gamma+h(f),
and each marked residual pair receives one unit on each incident face. Every vertex sends 2t+d*gamma=d-4.

Here g0=g2=g3=1/5. Because d(4)=d(7)=6,
g4=(1-t4)/3 and g7=(1-t7)/3,
with the earlier d=6 donor restriction giving t4,t7 in {0,1} when applicable. Neither is silently replaced by the old degree-five value 1/5.

The controlled region contains the old ten J faces, the three D/19 faces at 7, and the three new faces at 4: sixteen triangles total. Counting every corner gives the exact aggregate
-13 + 6g7 + 6g4 + 3g5 + 3g6 + 3g11 + 4g8 + 2g12 + 2g13 + 2gq + 2gr + sum(actual h).
If identities coincide, repeated coefficients for that actual vertex are aggregated, but distinct face payments remain distinct.

Relative to the old single-face payment ledger, the complete corner deduction over these sixteen faces is
 t7+t4
 +3t5/d5+3t6/d6+3t11/d11+4t8/d8
 +2t12/d12+2t13/d13+2tq/dq+2tr/dr,
plus every actual additional unit receipt. This includes all six corners at 4 and all six at 7; no local face is subsidised by omitting losses elsewhere.

The fixed target face has
mu(4,5,q)=-1+g4+g5+gq+h(4,5,q).
When h=0 it is negative exactly when g5+gq < (2+t4)/3. This is a residual signed-face condition, not a global contradiction and not a new classification of all C35 arithmetic families.

## 6. Bounded control and nonterminal state

The selected checker was actually run with CPython 3.13.5 and exited 0. It exhausts the 21 initial identity patterns, all compatible direction words, all complete colourings for the five literal deletions, and distinguishes ordinary from relation-only failure. Finite enumeration verifies only this local allocation; Sections 2,3 and 5 supply the general geometry, arbitrary-exterior composition and ledger arguments.

No Lean elaboration, axiom report, trusted statement-faithfulness acknowledgement, EvidenceLink or Result is supplied.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
current_atomic_progress: 6 of 70 compatible d(4)=6 signed types have complete induced-deletion profile reductions in the tested family
first_open_configuration: (q,r,word)=(11,12,3), whose tested deletion failures are relation-only
next_action: enlarge/change the interface for this first relation-only row, preserving all exterior arcs and DC2 costs; do not infer the other 63 open rows from it
next_obligation: obligation:opg169-root
root_closed: false
