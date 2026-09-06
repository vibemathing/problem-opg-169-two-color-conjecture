# C13: exact boundary states and a finite low-strip replacement bound

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c13-boundary-automaton
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 1c1283fbb8d873d5015fae7381ca8d55773791e7
Primary owner: math-proof.

## 1. Exact state, not just terminal colors

Let P be a finite digraph with a labelled boundary B. A valid coloring
c:V(P)->{0,1} means both induced color classes are acyclic.
Its boundary state is (sigma,R), where sigma is c restricted to B and
R consists of all ordered pairs (x,y) of boundary vertices joined in
P by a positive-length monochromatic directed path.

Thus R has no diagonal entries, is transitive, and relates only equal
colors. Paths through other boundary vertices are INCLUDED. The empty
path never creates an R entry. The profile S(P,B) is the set of states
of ALL valid colorings, not the state of a selected coloring.
It may be empty. A formally possible state need not be attainable.

## 2. Exact gluing rule

Suppose P and F meet exactly in B and have no arcs between their
disjoint interiors. Shared arcs agree in direction. For colorings
having the same sigma and respective relations R_P,R_F, the union
coloring is valid if and only if the positive transitive closure
(R_P union R_F)^+ has no diagonal entry.

A directed cycle lying entirely in one piece is already excluded.
Any other monochromatic cycle meets B. Cutting it at consecutive
boundary visits splits it into positive monochromatic directed paths
in the pieces. These supply a nonempty cyclic chain in R_P union R_F.

Conversely a nonempty cyclic chain of boundary relation entries can
be expanded into actual monochromatic paths of the pieces. All
vertices in this concatenated closed walk have the same color because
adjacent relation entries share an endpoint. It is a positive directed
closed walk and so contains a directed cycle. This proves both
directions, even if the expanded paths share internal vertices.

The same proof allows arbitrarily many pieces. It handles shared
boundary edges without counting them as missing or reversing them.
Consequently the existence of an acyclic two-coloring of P union F
depends ONLY on their profiles and the boundary identification.

In particular, replacing P by any P' with exactly the same profile
preserves two-colorability for every compatible exterior F. This is
an equivalence in both directions, not a one-sided extension claim.

## 3. Finite introduction and forgetting operations

Suppose a new vertex w is attached only to current boundary vertices.
For each old state and each of the two choices of c(w), add the
same-colored new arcs to R and take positive transitive closure on
B union {w}. Reject the choice if this closure has a diagonal entry.
The remaining relation is precisely the new boundary reachability.

Indeed, a new cycle must pass through w. Segments not using w are old
boundary-to-boundary paths, already recorded in R. The same cutting
and concatenation argument as in Section 2 proves the exact update.
It also proves that every retained state has an actual witness
coloring, provided the old profile had actual witness colorings.

To forget a boundary vertex z, keep z and all its arcs in the graph,
but remove it from the boundary label set. Restrict sigma and the
already transitively closed R to the remaining boundary. Take the
set of these restrictions over the old profile. This is exact because
all paths using z have already been recorded. Forgetting is NOT
deleting z from the graph and must not discard paths through z.

These are finite set operations. They specify an automaton
mathematically; no transition table or solver has been executed.

## 4. Two-terminal check and planar constraints

For two terminals, after a simultaneous color-name exchange, the
actual states are D, E0, E+, E-: different colors, equal with neither
reachability direction, equal with the forward direction, or equal
with the backward direction. The E0 state contributes to both coarse
regimes P and M in C05. Thus this construction recovers the previous
two-terminal rule, including why P and M are not exclusive states.

For a piece in a disk with four boundary vertices a,b,c,d in this
cyclic order, suppose R contains a->c and b->d. If their colors differ,
the two witness paths would be vertex-disjoint paths joining alternating
boundary pairs, impossible in the disk. If their color is the same,
the two paths meet at a vertex w. Concatenating their prefixes and
suffixes then gives a->d and b->c in R. These planar constraints are
necessary. They are not asserted sufficient for profile realizability.

## 5. A uniform bound on the number of four-terminal states

For an unordered pair of equal-colored distinct terminals, an acyclic
relation has at most three choices: neither direction, the first
direction, or the reverse direction. It cannot have both. Pairs of
different colors have only the absent choice.

There are two all-equal labeled colorings of four terminals, eight
colorings with a three-to-one split, and six with a two-to-two split.
The numbers of same-colored unordered pairs are respectively 6,3,2.
Thus the number of states is at most
2*3^6 + 8*3^3 + 6*3^2 = 1728.
This deliberately overcounts nontransitive or nonplanar relations.
Hence there are at most K=2^1728 distinct four-terminal profiles.
The bound counts sets of actual states; it does not assert every
subset is realizable by a planar piece.

## 6. Prefix automaton for the low strip

Use C12's disk with poles p,q, end terminals r,s, and low path
v1,...,vk, k>=2. Its boundary is p-r-q-s-p and its interior chain is
r,v1,...,vk,s. All arcs at an interior vertex belong to the disk.

For i=1,...,k let P_i contain p,q,r,v1,...,vi, with all the strip arcs
on these vertices, and label its boundary (p,q,r,front), front=vi.
The initial piece consists of edges pr,qr,pv1,qv1,rv1 with their
actual directions. Any exterior diagonals are omitted from all P_i.

To pass from i to i+1, introduce w=vi+1 using its edges to p,q,vi,
then forget vi and rename w as front. The directions of these three
edges give one of eight transition labels. Section 3 proves that
the new profile is a deterministic function of the old profile and
this label. The eventual final step introduces s with its edges to
p,q,vk, then forgets vk, leaving boundary (p,q,r,s).

There are no forgotten neighbors of a newly introduced vertex: C12
lists every arc incident with the low path. Thus no adjacency or
possible monochromatic cycle is silently omitted from the update.

## 7. Repeated prefixes produce a smaller planar counterexample

Suppose k>K. The k profiles of P_1,...,P_k cannot all differ, so there
are i<j with the same profile after the canonical front relabelling.

Remove v_{i+1},...,v_j from the strip. If j<k, reconnect vi to v_{j+1}
with the direction formerly used between v_j and v_{j+1}; if j=k,
reconnect vi to s with the direction formerly used between v_k and s.
All pole spokes and remaining chain edges retain their directions.

The prefix up to vi has exactly the same boundary profile as the old
prefix up to vj. Feeding the identical suffix transition labels and
the identical final step through the deterministic updates gives the
same final four-terminal profile as before.

The new underlying piece is again two cones over a shorter simple
chain, embedded in the same quadrilateral disk. At least one interior
vertex remains since i>=1. The four boundary vertices remain distinct.
The new edge joins previously nonadjacent chain vertices, or the final
interior vertex to s. It therefore causes no parallel edge, loop or
opposite-arc conflict. The exterior and all boundary arcs are unchanged.

Gluing the replacement into T preserves non-two-colorability by
Section 2, while decreasing the vertex count by j-i>0. The result is
still an orientation of a finite simple planar graph. It need not
preserve semidegrees or the secondary extremal choice: the global
vertex-minimum premise applies to the whole frozen class.
This contradicts minimality.

We conclude that every low path component of the selected T has at
most 2^1728 vertices. Isolated low vertices satisfy this automatically.
This extremely coarse bound is a finite parameter reduction, not a
practical enumeration result or an upper bound on |V(T)|.

## 8. Falsifier checks and scope limits

Color agreement without R is insufficient: two directed terminal
paths in opposite directions may form a cycle only after gluing.
Reflexive reachability would wrongly reject every nonempty boundary;
only positive paths are recorded. A neighbor witness without a
return path does not contribute an R entry.

Keeping just one favorable coloring instead of the entire profile
would invalidate deterministic replacement. Restricting R before
closing under intermediate boundary vertices would lose paths through
forgotten vertices. Introducing a new vertex adjacent to an already
forgotten interior vertex would violate the stated update contract.
None of these operations occurs in Sections 6-7.

The state bound and pigeonhole argument are exact finite reasoning.
There is no claim that 1728 states have been enumerated, that the
bound is sharp, or that all planar exterior profiles are classified.
Degree-five and higher vertices, and the all-equal triangular
exterior of C11, remain unresolved. No root closure follows.

Proof dependencies: C05's two-terminal comparison, C12's disk
geometry, and elementary finite directed-path and planar separation
facts. No new external theorem beyond those basics is imported.

## Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c13-boundary-automaton
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: combine exact patch profiles with constraints on vertices
having both semidegrees at least three; audit any use of a global
Brooks bound separately from fixed-boundary extension.
No mathematical execution, SAT certificate, Lean receipt or admission.
