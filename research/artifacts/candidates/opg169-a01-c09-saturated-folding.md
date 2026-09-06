# C09: saturated minimum representatives and planar folding

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c09-saturated-folding
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 869d6a64d909993ab853a16a1b4ca1f98fec68b5
Owner: math-proof.

## 1. Exact choice of counterexample

Assume the frozen root has a counterexample, and let n be its minimum
vertex count over the entire class of finite simple planar orientations.
Among the finitely many such counterexamples on n labelled vertices,
choose T with the largest number of arcs. This secondary maximization
is an explicit choice, not an extra property asserted of every minimum
counterexample.

Adding an orientation of a missing edge cannot make a non-2-colorable
digraph colorable: a valid coloring of the augmented digraph restricts
to one of the original. Any smaller planar orientation is colorable by
the definition of n, whether or not it is a subdigraph of T. Thus T
retains global vertex minimality under this choice.

C01-C03 give strong connectivity, underlying 2-connectivity, and
d+(v),d-(v)>=2. In particular delta(U(T))>=4 and n>=5. No cubic
assumption is made about U(T).

## 2. The chosen underlying graph is a triangulation and 3-connected

Fix a sphere embedding. Since U(T) is 2-connected, each facial boundary
is a simple cycle. Suppose a face has length at least four and choose
four consecutive distinct boundary vertices a,b,c,d. Both ac and bd are
non-boundary diagonals. If both edges existed, their interiors would lie
in the complementary closed disk and their endpoints would alternate
on its boundary. The Jordan separation property forbids two such
disjoint edges. At least one diagonal is absent. Draw it inside the
face and give it either one direction. This preserves simple planarity
and contradicts the arc-maximal choice. All faces are therefore triangles.

The distinct neighbors of any vertex w, in cyclic order, form a cycle:
each consecutive pair is the other edge of its triangular incident face.
Call this cycle the link of w. Here every link has length at least four.

First U(T)-t is connected. In any path between remaining vertices that
passes through t, replace the two-edge passage through t by a path
between those neighbors in the link of t. The resulting walk avoids t.

Now consider distinct s,t and a path in U(T)-t whose endpoints avoid s.
If it passes through s, its entering and leaving neighbors can be joined
in the link of s with t deleted. A cycle with at most one vertex deleted
is connected on its remaining vertices. Replacing the passage gives a
walk avoiding both s and t. Hence U(T)-{s,t} is connected. This proves
3-connectivity of the CHOSEN representative.

Therefore exclusion of all 3-connected planar triangulation
counterexamples suffices for the root. This does NOT prove that an
arbitrary minimum counterexample has no two-cut, nor does it eliminate
C06's rigid two-side configurations in an arbitrary minimum example.
There is no need to assume an unproved boundary-precolor extension
theorem to obtain this representative reduction.

Writing n_j for the degree-j vertex count, Euler's formula gives
m=3n-6 and
2*n_4+n_5 = 12 + sum_{j>=7}(j-6)*n_j.
At least one vertex has degree four or five. This identity is not a
discharging contradiction by itself.

## 3. Folding two neighbors on one semidegree-two side

This reduction applies to ANY global vertex-minimum counterexample G,
not just the saturated representative. Suppose N-(v)={a,b}.
Put F=G-v. We claim F contains a directed two-edge path from a to b
or from b to a.

Suppose no such path exists. Identify a and b to q in F, remove the
loop arising from ab if that edge exists, and retain one copy of each
duplicate arc. Call the result H.

Planarity is checked on the underlying graph: in U(G), remove all edges
at v other than av,bv and contract the path a-v-b. The resulting simple
underlying graph is exactly U(H). No other vertices are identified.
Thus H is planar and has n-2 vertices.

A new opposite-arc pair q<->x could only come from a->x->b or b->x->a,
for x distinct from a,b,v. These are precisely the excluded paths.
Existing arcs already had no opposite pair. The only possible new
loop is internal to {a,b} and is removed. Thus H remains an orientation
of a finite simple planar graph. Notice that a,b need NOT be nonadjacent.

Choose an acyclic 2-coloring of H by global minimum order, and pull it
back to F, giving a,b the color of q. This pullback is valid. Indeed, a
monochromatic directed simple cycle of F cannot be contained in {a,b}.
Its image, after suppressing steps contracted to q, is a positive
monochromatic directed closed walk of H. Every positive closed walk
contains a directed cycle, contradicting the coloring of H.

Give v the color opposite to q. It has no same-colored in-neighbor,
so no new monochromatic cycle through v is possible. This colors G,
a contradiction. The claimed directed two-edge path must exist.
Reversing all arcs proves the same claim for an out-neighbor pair.

This is not an unrestricted directed-contraction rule. The no-digon
condition, duplicate suppression, contracted internal edge and
positive-walk pullback are separate parts of the argument. Merely
having an undirected path between the two neighbors is insufficient.

## 4. Degree-four directed facial triangles

At a degree-four vertex of T, C04 gives two directed triangles meeting
only at the vertex and using all four distinct neighbors. Their four
incident half-edges cannot alternate: the first triangle is a Jordan
curve and the second, otherwise disjoint, cannot connect opposite sides.

A nonalternating partition of four cyclically ordered ports into two
pairs consists of two adjacent pairs. Since every incident face of T
is triangular, each of these neighbor pairs forms a facial triangle
with the center. Thus each degree-four vertex of T is incident with
two directed FACIAL triangles meeting only there.

For cyclic directions I,I,O,O, these are the two I/O transition corners.
For I,O,I,O, they are one of the two opposite-corner matchings.
Faciality uses the triangulation choice. C04 alone did not supply it.

## 5. A four-port reachability constraint and the degree-five 2+3 case

Remove a small open disk about v. The incident edges meet its boundary
in distinct ports in their cyclic order. The remaining sphere is a disk.
A path in G-v between neighbors may be extended to the corresponding
ports along the retained edge stubs.

For four distinct ports a,b,c,d in this order, paths from a to c and
from b to d must intersect. With different monochromatic colors they
cannot intersect, so those two differently colored reachabilities
cannot coexist. With the SAME color, choose an intersection vertex z.
Concatenating the first path's prefix to z with the second's suffix
gives a same-colored a-to-d walk, and the other two portions give
b-to-c. Deleting repeated segments gives directed paths since the
endpoints are distinct. Thus same-color crossing reachabilities force
both cross-rerouted reachabilities.

Now let deg(v)=5 and fix a valid coloring of G-v that blocks both colors.
One color, say red, occurs on exactly two neighbors x,y; the other
occurs on three. The red neighbors must supply one incoming and one
outgoing arc and a real red return path. Its closed cycle through v
separates the two open cyclic intervals between the x,y ports.

A blue blocking cycle is disjoint from that red cycle except at v.
Consequently its two ports must lie in the SAME interval. If x,y
are nonadjacent around v, the other ports split as 1+2; the blue cycle
must use the two ports in the size-two interval. Those two incident arcs
must have opposite directions. In particular, a coloring with all blue
in-neighbors in one interval and all blue out-neighbors in the other
always has a safe blue extension and cannot occur as an obstruction.
If x,y are adjacent, the split is 0+3 and this particular test adds no
restriction. This is a necessary local test, not a realizability or
recoloring theorem for all boundary states.

The first failed color always arises from an actual new directed cycle.
Distinct same-color incoming/outgoing witnesses use the absence of
opposite arcs; distinct cross-color witnesses use their different colors.
No mere-neighbor predicate is substituted for a return path.

## 6. Attacks, source scope and checkpoint

The oriented octahedron of C02 still passes the degree/facial tests and
is explicitly colorable. It also has the directed two-edge paths required
by the folding test. Hence the tests are not asserted jointly sufficient
for a contradiction. Choosing a saturated representative does not imply
4-connectivity, absence of separating triangles, or arc-criticality.
The folding graph is smaller but need not preserve a digirth restriction.

Proof dependencies: frozen canonical contract; C01-C04 at the base;
basic finite graph facts, sphere Jordan separation and planar minor
closure. All new implications are proved here. The companion literature
note identifies conditional source results that must not be used
circularly, and distinguishes published finite bounds from local runs.

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c09-saturated-folding
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
next_action: use reversible color transfer into an uncolored degree-four
vertex to constrain the induced graph of all degree-four vertices of T.
Keep arbitrary two-cut elimination distinct from the representative choice.
No mathematical program, verifier receipt or root admission is claimed.
