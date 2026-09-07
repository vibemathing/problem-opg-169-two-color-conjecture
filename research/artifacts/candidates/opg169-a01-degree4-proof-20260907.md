# R08: minimum-counterexample semidegrees and the sharp local degree threshold

Verdict: candidate_only. Status: proof-drafted.
Readiness: RESULT_CANDIDATE_READY / min-degree-four-necessary-condition.
Candidate: candidate:opg169-a01-degree4-proof-20260907
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Admitted target: obligation:opg169-strong-min-degree-three
Base: 8f7fd4ffd8ef3c93fc1cac7bfa1f35456adf791e
Owner: math-proof. No C27 dependency.

## A. Frozen statements and the direction of strengthening

Let C be all orientations of finite simple planar graphs. An orientation
has no loops, repeated arcs or opposite arcs. Set I(v)={x:x->v},
O(v)={x:v->x}. Degrees count distinct neighbors. An acyclic two-coloring
is a function c:V->{0,1} with BOTH full induced color-class digraphs
acyclic. Empty indexed color classes are allowed.

For EVERY G in C assume:
N: no such coloring of G exists.
M: every D in C with fewer vertices than G has such a coloring.

T4: G is nonempty and strongly connected, and every v satisfies
|I(v)|>=2 and |O(v)|>=2, whence degree_U(v)>=4.
T3: G is strongly connected and degree_U(v)>=3 at every v.

T4 implies T3 by numerical weakening, not conversely. The admitted
obligation and its statement digest still designate T3. T4 is a stronger
candidate claim, not a newly registered obligation. The root asks for
colorability for every G and does not follow from either T3 or T4.
Nothing asserts a counterexample exists.

Reachability allows a path of length zero from a vertex to itself.
A directed cycle has positive length; a simple cycle repeats only its
first/last vertex. Strong connectivity here requires nonemptiness.
In C cycles have length at least three. The empty graph has the empty
coloring; a singleton has no loop and permits either color; a two-vertex
orientation has at most one arc. None is a counterexample. Thus N gives
nonemptiness and excludes the singleton convention as an exception.

## B. Heredity and quantified minimality

For any S properly contained in V(G), retain S and all original arcs with
both ends in S. In a planar drawing erase the other vertices and their
incident edges. This introduces neither crossings nor loops, opposite
arcs or repeated edges. The result is G[S], an orientation of U(G)[S],
and remains in C. Finiteness gives |S|<|V(G)|. M supplies its coloring.

If counterexamples exist, their finite orders form a nonempty subset of
N and have a least element. This justifies N and M for every least-order
counterexample. No assertion about same-order arc deletion is used.
All local extension statements below quantify over EVERY valid coloring
of G-v, not a favorably chosen coloring.

## C. SCC condensation and gluing, re-audited

Mutual reachability is an equivalence relation: reflexivity uses the
length-zero convention; symmetry is built in; transitivity follows by
concatenation and removal of repetitions. Let S1,...,St be its nonempty
classes. Since G is finite and nonempty, 1<=t<infinity.

Paths between vertices of one class can be taken inside its induced
digraph. Indeed if x,y are in a class and z is on an x-to-y path, then
x reaches z and z reaches y reaches x, so z is in the same class.

The condensation Q has these classes as vertices and records an arc
Sj->Sk for j!=k exactly when an original arc crosses that way.
Choose representatives for arcs of any hypothetical directed cycle in
Q. Join successive representatives inside their classes using the
internal paths above. Following the cycle gives mutual reachability
between all its classes, contradicting their distinctness. Thus Q is
a DAG. A finite positive closed walk contains a cycle: choose a repeated
pair of vertices of least positive index difference. Its intervening
segment has no further repetition. Consequently Q has no such walk.

If t>=2, every Sj is proper and has a coloring cj by B. Put c(x)=cj(x)
for x in Sj. The two inverse-image sets are disjoint and cover V(G).
Retain ALL original induced arcs, including cross-class arcs.
A monochromatic cycle that crosses classes projects, after suppressing
consecutive equal classes, to a positive closed walk of Q, impossible.
A cycle within one class contradicts cj. Equivalently all vertices of
a directed cycle reach one another along it and must be in one SCC.
Thus the glued coloring is valid, contradicting N.

Hence t=1 and G is strongly connected. In this branch M is NOT applied
to G itself. The t=0 branch was excluded by N. Local empty color classes
and singleton SCCs cause no difficulty; the empty induced class is acyclic.

## D. Exact obstruction lemma, with actual return paths

Fix v and any valid coloring c of H=G-v. For k in {0,1} let c_k extend
c by giving v color k. Other colors and all arcs not incident with v
are unchanged. The other color-class digraph is exactly unchanged.

Let B_k mean c_k is invalid. Then
B_k iff there exist i in I(v), o in O(v) with c(i)=c(o)=k
and a directed path o-to-i contained in H[c^{-1}(k)].                 (1)

Necessity: a new monochromatic cycle must contain v, since c is valid
on the full induced deletion. Its color is k. Remove v from a simple
such cycle; its successor o and predecessor i give the stated path.
They are different: i=o would give both i->v and v->i. They also differ
from v because loops are excluded. The path has positive length.
Sufficiency: a simple path of the stated kind avoids v. Append i->v->o;
the resulting simple directed cycle has color k. If a walk was initially
given, repeated subwalks can be removed to obtain a simple path.

Thus mere same-color in/out neighbors are necessary, not sufficient.
Neither a path using v, a reverse-direction path, nor a path with a
wrong-color internal vertex witnesses (1).

## E. All small-semidegree extensions, without a bound on the other side

If I(v) is empty, (1) fails for both colors, so B_0=B_1=false.
If I(v)={a}, put h=c(a). For k=1-h the required incoming neighbor in (1)
cannot exist. For k=h the exact condition is
B_h iff some o in O(v) has color h and an h-colored path o-to-a in H. (2)
This describes both choices, not just a color-selection prescription.
In particular B_0 and B_1 cannot both hold: their incoming witnesses
would both have to be a, forcing c(a)=0 and c(a)=1.

If O(v) is empty, again neither color is blocked.
If O(v)={a}, put h=c(a). The exact alternative is
B_h iff some i in I(v) has color h and an h-colored path a-to-i in H,  (3)
whereas B_(1-h)=false. Two blocked colors would force the unique outgoing
neighbor a to have both colors. These cases cover arbitrary sizes of the
opposite side, including zero; that side has not silently been bounded.

Equivalently, assume both colors fail. Choose witnesses (i0,o0) and
(i1,o1) from the two actual cycles using (1). Different colors imply
i0!=i1 and o0!=o1. Therefore both semidegrees are at least two.
Cross-side distinctness is NOT needed for this semidegree step.

For each v of G, B supplies a valid c on H. N says that neither c_0 nor
c_1 can be valid. The preceding argument forces |I(v)|>=2, |O(v)|>=2
for that arbitrary v. This establishes the semidegree part of T4.

## F. Complete finite low-degree case table

The rows below range over all labeled directions and every coloring
of the neighbor set. h is the color of the unique neighbor on the small
side. R denotes the precise Boolean return-path test in the last column.
When a row uses R, the blocked set is {h} if R is true and empty otherwise;
color 1-h is always safe, and h is safe exactly when R is false.

| Total degree | (in,out) | Labeled patterns | Blocked set | Exact test R |
|---|---|---:|---|---|
| 0 | (0,0) | 1 | empty | none |
| 1 | (1,0) | 1 | empty | none |
| 1 | (0,1) | 1 | empty | none |
| 2 | (2,0) | 1 | empty | none |
| 2 | (0,2) | 1 | empty | none |
| 2 | (1,1) | 2 | {h} iff R | unique in a, out b: c(b)=h and b-to-a path in color h |
| 3 | (3,0) | 1 | empty | none |
| 3 | (0,3) | 1 | empty | none |
| 3 | (1,2) | 3 | {h} iff R | (2), disjunction over the two outgoing neighbors |
| 3 | (2,1) | 3 | {h} iff R | (3), disjunction over the two incoming neighbors |

At (1,1) the labeled patterns a->v->b and b->v->a respectively require
b-to-a and a-to-b paths. Unequal endpoint colors make R false. Equal
endpoint colors k leave k blocked precisely when the indicated
monochromatic return path exists. The other color never blocks.
At (1,2), if neither outgoing neighbor has color h, R is false; if one
does, test its path; if both do, take the OR of the two path tests.
At (2,1) apply the same 0/1/2 qualifying-neighbor split on the incoming
side with path direction from the unique outgoing neighbor.
All-in/all-out rows cannot contain a directed cycle through v.

For total degree d, there are 2^d labeled direction patterns and 2^d
neighbor color assignments. For d=0,1,2,3 this table covers all
1+4+16+64=85 local direction/color assignments symbolically. The R
split handles arbitrarily large exteriors; 85 is not an enumeration
claim for graphs or for all possible return paths.

## G. From semidegree two to underlying degree four

In a simple orientation I(v) and O(v) are disjoint: a vertex in both
would give an opposite-arc pair. Neither contains v. Every underlying
neighbor belongs to exactly one, so
degree_U(v)=|I(v) disjoint-union O(v)|=|I(v)|+|O(v)|>=4.
Alternatively all four cycle witnesses above are distinct: same-color
cross-side coincidences are excluded by no opposite arcs, and all
different-color coincidences by the fact c is a function.
Together with C this proves T4 and hence the weaker admitted T3.

Without the no-digon hypothesis the correct identity is
degree_U(v)=|I(v)|+|O(v)|-|I(v) intersection O(v)|.
The minimum loopless control is the bidirected triangle on {0,1,2}:
include both arcs for each unordered pair. Every vertex has in=out=2
but underlying degree 2. Any two-coloring repeats a color on a pair,
whose digon is monochromatic. All assignments with c(0)=0 are
000,001,010,011, blocked respectively by pairs 01,01,02,12;
color complementation covers the other four. Every loopless digraph on
at most two vertices is colored by giving its vertices different colors.
Thus this is a minimum-order counterexample only in the ENLARGED
loopless digon-permitting domain. It is not in C and does not oppose T4.

## H. Sharpness of the local threshold, not a new root bound

On five vertices v,a,b,c,d take exactly
v->a,a->b,b->v,v->c,c->d,d->v.
Draw the two directed triangles on opposite sides of v; the graph is a
simple planar orientation. In H=G-v color a,b with 0 and c,d with 1.
Both full color classes are single directed edges, yet either color
at v closes its corresponding triangle. The whole graph is colorable:
v has color 0 and a,b,c,d have color 1, with two disjoint directed edges.
This is a fixed-color extension obstruction, not a root counterexample.
Four other vertices are necessary for two blocked colors in an
orientation by D/E/G, so five vertices are minimum for this LOCAL
obstruction. C02's six-vertex octahedral example remains unchanged.
We do not infer that a hypothetical least-order counterexample has a
degree-four vertex, or that no further global necessary conditions exist.

## I. Dependencies and honest closure boundaries

Direct chain: N,M and finite/simple/planar heredity -> proper colorings;
reachability -> SCC DAG -> gluing -> strong connectivity;
valid deletion -> actual cycle/return-path iff -> two distinct witnesses
on each side -> semidegree two; no opposite arcs -> disjoint union -> T4;
T4 -> T3 by weakening. No converse, arc-criticality or C27 is used.

C01/C02 and the merged target-closure contain correct direct reductions;
this version makes T4 primary and supplies exact directional case tests,
an executable-design oracle and a separate verifier/admission request.
There is no mathematical correction to their degree-three proof.

Invariants: old colors and every induced arc away from v. Well-founded
measures: finite vertex count at every use of M, finite walk length in
walk shortening. No probabilistic or asymptotic step applies. Color
complement and relabeling are bijections; zero/singleton cases are explicit.
Finite tests are not induction and cannot establish the universal claim.

natural_language_remaining_cases: []
enumerator_execution: pending/unverified
Lean_elaboration_and_axiom_report: not_run
best_verified_candidate: none
best_verified_result: none
admission: request_only
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_obligation: obligation:opg169-strong-min-degree-three
The strong T4 claim is kept separately identified for faithful trusted
review; no new admitted ID, EvidenceLink, Result or Solution is created.
