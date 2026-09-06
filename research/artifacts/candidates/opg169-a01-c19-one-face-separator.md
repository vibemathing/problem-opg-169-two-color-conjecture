# C19: one-directed-face degree-five vertices force large directed separators

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c19-one-face-separator
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 8262e58b186da0c729ea9328fe33fc2966b60570
Primary owner: math-proof.

## 1. Exact hypotheses and notation

Let T be the maximum-size representative among globally minimum-order
counterexamples chosen in C09. It is a simple plane triangulation and
every vertex has both semidegrees at least two. This choice is not
asserted for every vertex-minimum counterexample.

Suppose a vertex v has degree five, with cyclic neighbors a,b,c,d,e,
and exactly ONE of its five incident faces is directed. Relabel so
that this face is vde. Put F=T-v. It has a valid acyclic two-coloring
by global vertex minimality, and none of its valid colorings extends.

The proof concerns this special local configuration. It does not
assume absence of separating triangles or a triangle-precoloring
extension theorem. The original admitted target remains unchanged.

## 2. Specializing the exact wheel table

For ANY five-wheel with vde its unique directed incident face, and
ANY compatible acyclicly colored exterior F, C18 gives:
failure to extend is equivalent to
  phi(a)=phi(c), phi(d)=phi(e), phi(a)!=phi(d), R_phi(a,c)=1.
There is no additional condition on phi(b).

For completeness, if the twice-used color is on adjacent rim vertices,
its facial triangle must be directed. The unique possibility is the
pair d,e; then a,b,c share the other color, and the only remaining
obstruction is R_phi(a,c), as the faces vab and vbc are transitive.
If the twice-used color occupies nonadjacent positions, C18 requires
the adjacent majority pair to support a directed face. That pair must
be d,e, so the minority pair is a,c and the leftover majority vertex
is b. Its return obstruction is again R_phi(a,c). The automatic
multiplicity cases cannot fail. Both displayed patterns conversely
block one color at vde and the other at the a,c return path.

Applying this to every valid coloring of T-v shows that the two
equalities and their inequality are rigid in F, up to global color
exchange, and the indicated return path exists for EVERY such coloring.
No assertion is made that both choices of phi(b) actually occur.

Since R_phi(a,c)=1, the two spokes have opposite directions. Write
i for the in-neighbor and o for the out-neighbor of v among {a,c}.
Thus i->v->o, and each valid coloring of F has a same-color o-to-i path.

## 3. A safe diagonal insertion forces a separating directed triangle

If ac were absent, insert the single arc i->o in the pentagonal face
left by v. Its endpoints are distinct, and no edge between them was
present, so the augmented graph H=F+(i->o) is a smaller finite simple
planar orientation in the frozen class. Minimum order supplies a
valid two-coloring of H.

Restrict this coloring to F. Section 2 forces i and o to have one
color and supplies a monochromatic o-to-i path already in F.
The new arc i->o closes it into a directed monochromatic cycle in H,
a contradiction. Therefore ac is an existing edge.

Its direction cannot be i->o: the same return path would make F
itself monochromatically cyclic in each of its valid colorings.
Consequently its direction is o->i, and
  i->v->o->i
is a directed triangle in T.

This triangle is separating. The half-edge vb lies between va and vc
on one side, whereas vd and ve lie in the other cyclic interval.
Because ac is drawn outside the five-wheel disk, the Jordan triangle
vac has b on one side and d,e on the other. These are actual distinct
vertices, so both sides are nonempty.

Thus any degree-five vertex with exactly one directed incident face
also belongs to a directed separating triangle. The facial triangle
vde and the separating triangle vac intersect only at v.

Only insertion of a previously absent arc was used. No existing arc
was reversed, and no two opposite arcs were inserted simultaneously.

## 4. Every directed separating triangle has at least four vertices on each side

This separate lemma applies to any directed separating triangle S in T,
not just the triangle constructed above. Fix a side and let k>0 be its
number of vertices strictly inside. Take the closed disk patch consisting
of S and all these vertices. All its non-outer faces are triangles.
Write m_I for the number of edges between the k interior vertices.

The patch has k+3 vertices and 3k+3 edges. Its three boundary edges,
its interior-interior edges, and its crossing-to-boundary edges give
  sum of the full T-degrees of the interior vertices = 3k + m_I.
Those vertices have no neighbors outside the closed disk. By the
minimum-degree-four bound this sum is at least 4k, so m_I>=k.

For k=1 or 2 this contradicts m_I<=k(k-1)/2.
For k=3, equality forces m_I=3 and all three interior vertices
have degree exactly four in T. They form a facial triangle: its inner
disk has no further vertex, and the boundary S is outside it.

Here is the required six-vertex geometry. For each edge of the inner
triangle let its other facial third vertex be on S. These three third
vertices are distinct. If two consecutive inner edges had the same
third vertex z, the link of their common degree-four inner vertex
would contain a three-cycle, contradicting that its link is a simple
four-cycle. Thus the third vertices exhaust S. The remaining link
edges force the three corner triangles. The patch is the octahedron
with one triangular face chosen as its outer boundary.

Every nonconstant precoloring of that outer triangle extends to an
acyclic two-coloring of ANY orientation of this patch, by C11's explicit
two-path construction. In the notation of C11, for outer x=y=A,z=B,
put inner a=A,b=c=B. The two induced underlying color classes are
paths. Rotation of the labels and color exchange covers all six
nonconstant boundary assignments.

Delete the k interior vertices from T and color the remaining graph
by minimum order. Since S is directed, its coloring cannot be constant.
Extend across the octahedral patch using the preceding construction.
The two colored pieces share the entire tournament on S. C11's
tournament-gluing proof then prevents cross-piece monochromatic cycles:
within each color, every path between shared vertices respects the
common tournament order. The union would color T, impossible.

Hence k=3 is impossible as well. Each side therefore has at least four
vertices, and a T containing any directed separating triangle has
at least 3+4+4=11 vertices. This conditional bound is not asserted to
be an optimal or new published order bound.

## 5. Consequences and boundaries

The one-directed-face degree-five configuration is impossible unless
the graph has a directed separating triangle with at least four
vertices on each side.

In a selected representative having NO directed separating triangle,
every degree-five vertex has at least TWO directed incident faces:
zero faces is excluded by C18, and exactly one by Section 3.
In particular this applies conditionally when the underlying graph
is 4-connected. We have NOT shown that a representative with either
additional property can always be chosen.

The C18 six-vertex bad-extension example has only one directed incident
face and its opposite diagonal, but it is itself colorable and its
triangle vac has small sides. It tests the fixed-color extension
rule; it does not contradict these global minimality consequences.

The opposite pair a,c being forced to one color is not an assertion
that F itself is uncolorable. An already present diagonal o->i is
compatible with that monochromatic class. Deleting or reversing it
would change the family of available colorings, so the old rigidity
could no longer be assumed.

## 6. Dependency and source audit

Direct proof-draft dependencies, all read at or before the base:
C09 selected triangulation and link geometry;
C11 octahedral precoloring and tournament gluing;
C18 exact degree-five interface.
The canonical contract supplies global minimum order over the entire
orientation class, not just over induced subgraphs.

No additional literature theorem or computational output is imported.
The small-side classification uses the displayed degree count and link
argument, not an enumerator. No unrestricted boundary-precoloring
theorem, digirth-preserving contraction, or absent-separator hypothesis
is smuggled into the argument. C18's source note already distinguishes
the digirth-restricted coloring theorems from this local question.

## 7. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c19-one-face-separator
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; prior C18 face-only shortcut
remains excluded; this cycle does not abandon the admitted route.
next_obligation: obligation:opg169-strong-min-degree-three
next_action: analyze the exact coloring-profile conflict across the
forced directed separating triangle, or sharpen its interior-size
restriction. Do not infer that existence of the separator already
contradicts minimality.
No mathematical execution, verifier receipt, or root admission is claimed.
