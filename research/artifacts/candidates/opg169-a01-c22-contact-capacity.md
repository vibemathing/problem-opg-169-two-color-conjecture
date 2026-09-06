# C22: low-patch contacts reduce exceptional-vertex support capacity

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c22-contact-capacity
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 492be21c6237f0ab33e62dbf4d97aaf2374dc285
Primary owner: math-proof.

## 1. Frozen objects and the overlap convention

Use the selected minimum-order triangulation T of C09 and the support
map of C21. An exceptional vertex is a degree-five vertex with exactly
one directed incident face. Each has a unique support; q(h) counts
exceptional vertices supported by h. A marked neighbor of h has its
predecessor and successor in the cyclic link oriented the same way
as itself at h, and distinct marks are nonconsecutive, by C21.

Call h qualified when it is either the distinguished majority pole
of a low-edge component from C17, or a boundary vertex of a low-triangle
component from C11. Qualification is a property of a VERTEX, not of
an incidence. If several patches qualify the same vertex, it is counted
only once below. No assumption that these patches have disjoint
neighbor blocks is needed.

The claims are additional structural candidates for this selected T;
they do not modify either admitted obligation.

## 2. Every qualified vertex has a four-position block and is heavy

For a low-edge majority pole, C17 gives four distinct consecutive
link vertices r,u,v,s, where u,v are the two low vertices, and both
faces hru and hvs are directed. Hence the spoke pairs hr,hu and
hv,hs have opposite directions. C17 also gives
  d^-(h)>=3, d^+(h)>=3.

For a low-triangle boundary vertex the same block occurs by C11's
octahedral disk geometry. To verify the directions and degree bound,
take outer triangle h,r,s and the low triangle with u,v the two
neighbors of h. Its two corner faces hru and hvs are directed.
Again each of {r,u} and {v,s} contributes one incoming and one
outgoing neighbor of h.

Delete the three low vertices and fix a valid coloring of the exterior.
C11 says that h,r,s all have color A in EVERY such coloring. Recolor h
alone to B. If the new exterior coloring were valid, its nonconstant
boundary triangle would extend across the low patch by C11 and glue
along the entire tournament boundary, giving a coloring of T.

It follows that the flip creates an actual B-colored directed cycle
through h. Its predecessor and successor are outside {r,u,v,s}:
r,s still have color A, and u,v are deleted. They are distinct in an
orientation. They give a third incoming and a third outgoing neighbor.
Thus every qualified h is heavy, meaning BOTH semidegrees at least
three; in particular degree(h)>=6. This is not inferred merely from
degree(h)>=6.

## 3. The four-position block contains no support mark

The low vertices u,v have degree four, so they are not exceptional
degree-five vertices and cannot be marked. A mark at r would require
hr and hu to have the same direction, contrary to the directed face
hru. A mark at s would likewise contradict the directed face hvs.
Thus all four positions r,u,v,s are unmarked.

Every mark lies on the complementary link path of N=d-4 vertices,
where d=degree(h). The marks are pairwise nonconsecutive on that
path, so their number is at most ceil(N/2).

We will improve the odd-path equality case using the same-direction
three-spoke condition and heaviness. No cycle or path is inferred
from neighbor colors in this combinatorial capacity argument.

## 4. Degree six and the odd-degree equality obstruction

If d=6, the complementary path has two vertices z1,z2. A mark at z1
would force s,z1,z2 all to have the same spoke direction. Because
hr,hu are opposite and hv,hs are opposite, exactly two of all six
spokes would then have the other direction. This contradicts the
three-and-three semidegree requirement. A mark at z2 instead forces
z1,z2,r to agree, with the same contradiction. Therefore q(h)=0
for every qualified degree-six vertex.

Now let d>=7 be odd, so N=d-4 is odd. A set of ceil(N/2) nonconsecutive
positions on a path with N vertices is uniquely the set of odd positions
1,3,...,N. One direct proof is to order the chosen positions
j1<...<jt, where t=(N+1)/2. The bounds j1>=1,
j_(k+1)>=j_k+2, and jt<=N force equality throughout.

If all these positions were marks, their overlapping same-direction
triples would force all complementary vertices together with r and s
to have the same spoke direction. The directed corner faces then force
u,v to have the opposite direction. Exactly two spokes have that other
direction, again contradicting heaviness. Hence
  q(h)<=floor((d-4)/2)  for odd d>=7.

For even d>=8 this bound already follows from the N-vertex path bound.
Consequently every qualified vertex satisfies
  q(h)=0                         if d=6;
  q(h)<=floor((d-4)/2)            if d>=7.

These improve C21's general capacity floor((d-2)/2) by two at degree
six, and by one at every degree at least seven. No further improvement
per additional patch is asserted.

## 5. Distinct-vertex counting and Euler refinement

Let p_d be the number of DISTINCT qualified degree-d vertices. Let B
count exceptional degree-five vertices and let G_5 count the remaining
degree-five vertices, as in C21; write n_d for all degree-d vertices.
Qualified vertices have degree at least six. C21 and Section 4 give
  B <= G_5 + sum_(d>=6) floor((d-2)/2)*n_d
            -2*p_6 - sum_(d>=7) p_d.                         (1)

Combining this with
  2*n_4+B+G_5 = 12+sum_(d>=6)(d-6)*n_d
and moving negative high-degree coefficients to the right yields
  2*n_4 + 2*G_5 + 2*(n_6-p_6) + n_7 + n_8
    >= 12 + sum_(d>=7) p_d
          + sum_(d>=11)(ceil(d/2)-5)*n_d.                   (2)

Every penalty is attached to a single qualified vertex and a single
chosen block at that vertex. This prevents double counting when a
vertex is both a majority pole and a boundary of one or more low
triangles. The inequality is necessary; it does not prove that a
two-coloring exists or that the displayed counts are contradictory.

## 6. Attack and dependency audit

Dependencies: C09 selected triangulation and minimum order; C11 exact
low-triangle disk, forced corner directions, and tournament gluing;
C17 unique majority pole and its heavy-degree argument; C21 marked
neighbor semantics and nonconsecutive capacity.

The low-triangle heaviness argument counts a real new-cycle predecessor
and successor, not merely vertices of a different color. The four-position
block has distinct vertices and is consecutive by the respective patch
geometry. The odd-path maximum is proved explicitly. The degree-six
case is treated separately, since its strengthened bound is zero rather
than the generic floor((d-4)/2)=1.

No non-overlap of different patches or of different recoloring paths is
assumed. Additional contact incidences are not automatically additive.
All argument counts are symbolic; no solver or mathematical program
has been run, and no external theorem is newly imported.

## 7. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c22-contact-capacity
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; prior local exclusions retained.
next_obligation: obligation:opg169-strong-min-degree-three
next_action: combine the high-core size inequality with the exact domain
of the located published order-26 exclusion. Preserve its computational
source dependency and do not describe it as a local replay.
No verifier receipt, EvidenceLink or root admission is asserted.
