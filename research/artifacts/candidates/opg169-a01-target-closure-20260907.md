# R08: standalone proof of the admitted necessary condition

Verdict: candidate_only. Mathematical document status: proof-drafted.
Readiness: RESULT_CANDIDATE_READY (natural-language candidate only).
Candidate: candidate:opg169-a01-target-closure-20260907
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Target statement SHA-256: e5d7b7d2903018956d3e5c66f61cd5d33ef699e068931d2e97a13a1fbaeda4da
ProblemContract SHA-256: 719230edd088c52a5468eed8090579e5eef1bf85d8a56e633350063108f345ec
Base: 2aaa043b59c90d7c50f456ce9c11bd85d978c8ce
Primary owner: math-proof.

## 1. Exact claim, quantifiers, and conventions

Let C be the class of orientations of finite simple planar graphs. Write
U(D) for the underlying simple graph of D. Each unordered edge receives
exactly one direction. There are no loops, opposite arcs, or parallel arcs.
A valid coloring is a function c:V(D)->{0,1} for which each full induced
digraph D[c^{-1}(k)] has no directed cycle. Either color class may be empty.
A partition here is the two indexed, disjoint color classes covering V(D);
it is not a requirement to use both colors, nor a proper graph coloring.

The claim is: for EVERY G in C satisfying
  (N) G has no valid coloring, and
  (M) for EVERY D in C with |V(D)|<|V(G)|, D has a valid coloring,
G is nonempty, strongly connected, and delta(U(G))>=3.
This quantifies over all least-order counterexamples, not just an
edge-maximal representative, a particular embedding, or one selected G.
No existence of a counterexample is asserted.

If any counterexample exists, its finite orders form a nonempty subset
of the natural numbers. The well-ordering principle gives a least order,
and a graph of that order satisfies (N),(M). No arc-minimality is inferred.
The exact negation of the necessary condition would be a G satisfying
(N),(M) that is empty, not strongly connected, or has a vertex of degree
0, 1, or 2. The proof below excludes these possibilities separately.

A directed path is a finite directed vertex sequence with no repetition;
a length-zero path from x to x is permitted for reachability. A directed
cycle has positive length and distinct vertices except for the repeated
endpoint. In C its length is at least three. Strong connectivity means
nonempty vertex set and mutual reachability of every ordered pair,
using this length-zero convention. A loopless singleton is therefore
strongly connected but acyclic. It will not satisfy (N).

Allowed background: finite-digraph-basic, planar-graph-basic,
finite-combinatorics, as in the frozen contract.

## 2. Deletion, minimality, and empty objects

For every S subset V(G), the underlying graph of G[S] is exactly U(G)[S].
Retain a planar drawing of U(G), erase vertices outside S and all incident
edges, and keep the other drawn edges with their old directions.
No crossing, repeated edge, loop, or opposite arc is introduced.
Thus G[S] is again in C. If S is proper, finiteness gives |S|<|V(G)|;
(M) then supplies a valid coloring of this full induced digraph.

For V(G)=empty, the unique empty coloring is valid, contradicting (N).
For a singleton {v}, there is no loop and the coloring X0={v}, X1=empty
is valid. A graph on two vertices in C has at most one arc and is also
acyclic. In particular G is nonempty, and there is no singleton-convention
exception to the theorem.

For each v, H=G[V(G) minus {v}] is the ordinary vertex-deleted digraph,
not an arc-deleted same-order graph. Fix ANY valid coloring c of H
provided by (M). All extension arguments below work for each such c;
they do not select a specially favorable coloring.

## 3. Strongly connected components and their condensation

Reachability is reflexive because of length-zero paths and transitive
because concatenated paths are walks from which repeated segments can
be removed. Define x~y by reachability in BOTH directions. Reflexivity,
symmetry and transitivity show that ~ is an equivalence relation.
Let its nonempty classes be S1,...,St. Since G is finite and nonempty,
1<=t<=|V(G)|.

The induced graph on each Sj is strongly connected. To check that a path
does not have to leave the component, take x,y in Sj and any path x to y.
If z is on that path, x reaches z and z reaches y, while y reaches x.
Thus z reaches x and x reaches z, so z lies in Sj. Hence that path stays
in G[Sj]. This justifies every use of an internal component path below.

The condensation Q has vertices S1,...,St. It has an arc Sj->Sk, j!=k,
exactly when G has an arc from a vertex of Sj to a vertex of Sk.
Internal arcs are omitted and repeated component arcs are represented once.

Suppose Q has a directed cycle of distinct components
Si1->Si2->...->Sir->Si1, r>=2.
Choose an original arc for each displayed component arc. Within each
component, join the endpoint of the preceding chosen arc to the start
of the following one by an internal directed path, allowing length zero.
Following these paths and arcs around the cycle shows that every vertex
in any of these components reaches every vertex in any other, in both
directions. They must be one equivalence class, contradicting distinctness.
Therefore Q has no directed cycle: Q is a DAG.

For completeness, a finite positive closed directed walk always contains
a directed cycle. In its vertex sequence choose equal entries with
smallest positive index difference. Their intervening segment has no
repeated internal vertex, or a still smaller difference would exist.
This is a cycle. A finite DAG therefore has no positive closed walk.

## 4. Gluing the component partitions, including the single-SCC case

Assume t>=2. Each Sj is then a proper subset of V(G), so Section 2 supplies
a valid coloring cj of G[Sj]. Choose these for the finite list of classes.
For k in {0,1} define
  Xk = union over j of {x in Sj : cj(x)=k}.
The two sets cover V(G) and are disjoint, since the Sj are disjoint and
each cj is a function. Some local or global color classes may be empty.

Form G[Xk] with ALL original arcs whose endpoints lie in Xk, including
arcs between components. Suppose it has a directed cycle Z.
If Z crossed components, project its cyclic vertex sequence to Q and
suppress consecutive occurrences of the same component. The crossing
arcs give a positive closed directed walk in Q. Section 3 forbids it.
Equivalently, all vertices of Z mutually reach one another along Z,
so they must lie in a single Sj. In that Sj the cycle is monochromatic
under cj, contradicting the validity of cj. Thus G[Xk] is acyclic for
both k, and the glued coloring contradicts (N).

It follows that t=1. This case is NOT colored by applying (M) to G itself.
Instead Section 3 already says the sole component induces a strongly
connected digraph; that sole component is V(G). This proves the required
strong connectivity. The t=0 case was excluded by nonemptiness.

## 5. Exact obstruction to extending a deleted-vertex coloring

Let c color H=G-v validly. For k in {0,1}, let ck equal c on H and assign
color k to v. The other color class is unchanged. The k-class acquires
v and exactly those incident arcs having the other endpoint colored k.
Call k blocked when ck is not valid.

Every cycle that makes ck invalid must use v: otherwise it was already
a monochromatic cycle in the unchanged full induced digraph of H.
Such a cycle has color k. Let i precede v and o follow v on the cycle.
Then i->v and v->o are arcs, both neighbors have old color k, and removing
v from the simple cycle leaves a simple directed path o to i entirely
inside H[c^{-1}(k)]. The endpoints are distinct: equality would give an
opposite-arc pair at v, which an orientation cannot have.

Conversely, suppose i->v, v->o, c(i)=c(o)=k and there is such a simple
monochromatic path o to i in H. Its vertices are distinct and avoid v.
Append i->v->o to get a monochromatic directed cycle. Thus, for the
fixed coloring c, blockedness is EQUIVALENT to the existence of this
return path and the two specified incident arcs, with both endpoints
colored k. Mere presence of same-color in- and out-neighbors is only
necessary and is not sufficient.

In particular, at a degree-two vertex with a->v->b,
  k is blocked
  iff c(a)=c(b)=k AND H[c^{-1}(k)] contains a directed path b to a.   (*)
The path in (*) has positive length since a!=b. It may have more than
one edge; it must not run through v or through a vertex of the other color.

## 6. Exhaustive degree-0, degree-1, and degree-2 extensions

Degree zero: no incident arc exists, so a cycle cannot enter and leave v.
Both choices for ck are valid; the other induced color class is unchanged.

Degree one: if the sole edge is a->v there is no outgoing arc at v;
if it is v->a there is no incoming arc. Either fact prevents any directed
cycle through v. Thus BOTH colors are safe in either orientation.

Degree two has distinct neighbors a,b and exactly four labeled patterns:
  a->v and b->v;          v->a and v->b;
  a->v and v->b;          b->v and v->a.
In the first pattern there is no outgoing arc; in the second there is
no incoming arc. Both colors are safe, regardless of the neighbors'
colors or of any exterior path.

For a->v->b, if c(a)!=c(b), neither color satisfies the endpoint condition
in (*), so both are safe. If c(a)=c(b)=k, choose 1-k at v. Neither neighbor
has that color, so it is safe. Color k itself is blocked exactly when
the k-colored b-to-a path exists; its existence is NOT inferred from
the endpoint colors. For b->v->a the same explicit criterion has a-to-b
in place of b-to-a. The identical color choices follow from its two
endpoint colors. This is just exchanging the labels a and b.

Two colors cannot both be blocked in either mixed pattern: blocking
color 0 requires c(a)=c(b)=0, whereas blocking color 1 requires
c(a)=c(b)=1. A fixed coloring cannot satisfy both requirements.
Each pattern therefore extends c to all of G without recoloring H.

If G had a vertex of degree at most two, this construction, using (M),
would contradict (N). Consequently every vertex has degree at least three.
Together with Section 4 this proves exactly the admitted necessary
condition, without any premise or theorem from C27.

## 7. Finite case table

The table is a hand-derived exhaustive symbolic table, not a program log.
I means a neighbor-to-v arc and O means a v-to-neighbor arc. For the
mixed rows, i is the unique incoming neighbor, o the unique outgoing
neighbor; r_k means existence of an o-to-i path in H[c^{-1}(k)].

| Degree | Pattern | Old endpoint colors | Return path | Blocked colors | Safe colors |
|---|---|---|---|---|---|
| 0 | no arcs | none | irrelevant | none | 0,1 |
| 1 | I | either | irrelevant | none | 0,1 |
| 1 | O | either | irrelevant | none | 0,1 |
| 2 | II | any | irrelevant | none | 0,1 |
| 2 | OO | any | irrelevant | none | 0,1 |
| 2 | IO: a=i,b=o | 0,0 | r_0 false | none | 0,1 |
| 2 | IO: a=i,b=o | 0,0 | r_0 true | 0 | 1 |
| 2 | IO: a=i,b=o | 1,1 | r_1 false | none | 0,1 |
| 2 | IO: a=i,b=o | 1,1 | r_1 true | 1 | 0 |
| 2 | IO: a=i,b=o | 0,1 or 1,0 | irrelevant | none | 0,1 |
| 2 | OI: a=o,b=i | 0,0 | r_0 false | none | 0,1 |
| 2 | OI: a=o,b=i | 0,0 | r_0 true | 0 | 1 |
| 2 | OI: a=o,b=i | 1,1 | r_1 false | none | 0,1 |
| 2 | OI: a=o,b=i | 1,1 | r_1 true | 1 | 0 |
| 2 | OI: a=o,b=i | 0,1 or 1,0 | irrelevant | none | 0,1 |

For degree two, the four direction patterns each account for all four
labeled endpoint colorings. Same-color mixed cases are further split
by the single relevant path predicate. Unrestricted exterior size and
path length are handled by (*) itself, not by a finite sample inference.

## 8. Degree-three boundary check; explicitly stronger, not needed above

For three distinct neighbors the direction patterns are:

| (in-degree,out-degree) | Number of labeled patterns | Guaranteed safe choice |
|---|---:|---|
| (3,0) | 1 | either color |
| (0,3) | 1 | either color |
| (1,2) | 3 | opposite to the unique in-neighbor's color |
| (2,1) | 3 | opposite to the unique out-neighbor's color |

A blocked color must occur on both sides of v, by Section 5. The displayed
choice is absent on one side, so it is safe. This covers all eight
orientations and every coloring of the three neighbors.

More generally, if in-degree or out-degree is at most one, choose a
color absent on that side. Thus (N),(M) imply both semidegrees at least
two. Since opposite arcs are forbidden, the in/out neighbor sets are
disjoint and their cardinalities sum to the underlying degree. This
recovers C02's stronger delta>=4, but Section 6 already proved delta>=3.

## 9. Dependencies, applicability, and readiness

Local dependency chain:
definitions -> deletion/minimality (Section 2);
reachability -> component-internal paths -> condensation DAG (Section 3);
Sections 2,3 -> SCC gluing -> strong connectivity (Section 4);
valid deleted coloring -> exact return-path obstruction (Section 5);
Sections 2,5 -> all degree-0/1/2 cases -> degree>=3 (Section 6).
There are no new admitted obligation IDs and no dependency on C03-C27.

The extremal measure is the finite vertex count; every use of minimality
strictly reduces that count. No induction from small examples is claimed.
The only subsidiary walk-shortening step strictly decreases finite walk
length. Unchanged colors/arcs away from v and the full induced-arc
predicate are the extension invariants. Label exchange a<->b and global
color exchange are actual bijections; the table also displays both mixed
direction patterns. No probability, asymptotics, numerical limit, dual
construction, or iterative coloring algorithm is used.

The companion mutation audit provides explicit 0-3-neighbor fixtures,
including out-of-domain loops/digons and invalid-input controls. Such
fixtures test the lemmas and their semantics; they are not counterexamples
to the frozen root and do not replace this all-orders argument.

All logical cases requested for this natural-language theorem are supplied.
RESULT_CANDIDATE_READY means ready for external review as a proof of a
necessary condition / local result. It does NOT record a verifier verdict,
a formal elaboration, a trusted admission, or a resolution of the root.

best_verified_candidate: none
best_verified_result: none
natural_language_remaining_cases: []
route_status: open (pending the required mathematical verification)
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
next_action: review this exact direct proof and mutation audit; complete
the trusted formal/axiom/faithfulness gates separately without expanding
the conditional C27 machinery.
No mathematical executable was run for this document.

Repository sources at the base: canonical ProblemContract, C01 direct
proof, C02 semidegree proof. The companion audit records their precise
relationship, the C07/C08 source status, and the C27 scope separation.
