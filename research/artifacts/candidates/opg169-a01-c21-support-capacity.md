# C21: support capacity for one-face degree-five vertices

Verdict: candidate_only. Status: proof-drafted.
Candidate: candidate:opg169-a01-c21-support-capacity
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-strong-min-degree-three
Base: 4c536f43179370c159a496237e217dc5d1140059
Primary owner: math-proof.

## 1. Exact objects

Let T be C09's selected minimum-order counterexample triangulation.
Call a degree-five vertex exceptional if it has exactly one directed
incident face. C18 excludes zero directed faces at a degree-five vertex.

For an exceptional v, label its cyclic neighbors a,b,c,d,e so that vde
is the unique directed face. C19 supplies the separating directed triangle
vac. The vertex b is the unique neighbor of v strictly on one side of vac;
d,e lie on the other side. Define f(v)=b, called its support vertex.
The unique directed face and the cyclic link determine b uniquely.
This is a combinatorial association, not an edge contraction performed
on the actual repository graph.

Every claim below concerns this selected T. The two admitted obligations
remain open. No assumption of four-connectivity is made.

## 2. Safe contraction forces a uniform three-spoke block

Orient the notation so that a->v->c and c->a form the directed triangle.
Planarity implies that b has no edge to d or e: b is strictly on one
side of vac, d,e strictly on the other. Thus the only possible common
neighbors of b and v are a and c, and both actually are common neighbors.

If b->v, the transitive face vbc forces b->c. Suppose a->b as well.
Then a points to both b,v, and both b,v point to c. Contract bv to w,
remove its resulting loop, and retain one copy of each duplicate arc.
The only duplicates involve a,c, and each pair has the same direction.
There is no digon. The result is a finite simple planar orientation on
one fewer vertex.

Color this smaller orientation by global minimum order and pull the
coloring back, giving b and v the color of w. A monochromatic directed
cycle in T cannot be contained in {b,v}, since an orientation has no
loop or digon. Its contracted image, after suppressing the bv step if
present, is therefore a positive monochromatic directed closed walk.
Such a walk contains a directed cycle in the smaller graph, impossible.
The pullback would color T. Thus a->b is impossible, and b->a.
We have b->a, b->v, b->c.

If v->b, the transitive face vab forces a->b. Were b->c present, the
same contraction would again have only same-direction duplicates.
It is impossible for the same reason. Therefore c->b, and all three
a,v,c point to b.

In either case b is uniformly directed toward or away from {a,v,c}.
Its other semidegree is at least two, so degree(b)>=5. Moreover the
two facial triangles bav and bvc show that a,v,c are three consecutive
vertices in the cyclic link of b, with v in the middle. Their three
spokes have the same direction at b.

The contraction argument does NOT assert that any edge not on a directed
triangle is contractible. A transitive two-edge path between its endpoints
also creates a digon when they are identified; both possible conflicts
were explicitly excluded here.

## 3. A degree-five support vertex is not exceptional

Suppose degree(b)=5. Write its cyclic link as a,v,c,x,y.
The vertices x,y lie strictly on b's side of vac. They differ from
a,b,c,v,d,e, and neither vx nor vy is an edge, since v's only neighbor
strictly on this side is b.

If b points to a,v,c, its other two spokes are x->b and y->b, by the
two-sided minimum-semidegree bound. Reverse all arcs for the other
uniform case. The faces bav, bvc and bxy are transitive, so the only
possible directed faces at b are bcx and bya.

At least one is directed by C18. If only bcx were directed, C19,
applied now at b with cyclic link y,a,v,c,x, would force the edge yv.
If only bya were directed, the cyclic link v,c,x,y,a would force vx.
Both edges have just been excluded by the separating triangle vac.
Therefore BOTH bcx and bya are directed. A degree-five support vertex
has exactly two directed incident faces and is not exceptional.

## 4. Supports cannot receive consecutive exceptional neighbors

Fix any support vertex b. Mark the neighbors v with f(v)=b in its
cyclic link. If r_i is marked, Section 1 and the two faces at br_i
force the edge r_(i-1)r_(i+1): it closes the directed triangle supplied
by C19 for r_i. All indices are cyclic.

If two consecutive positions r_i and r_(i+1) were marked, the two
forced edges would be
  r_(i-1)r_(i+1),  r_i r_(i+2).
Their four endpoints are distinct since degree(b)>=5, and alternate
on the link cycle. Neither edge can pass through the disk formed by
the incident faces at b. Both must be drawn in its complementary disk.
Two disjoint edges joining alternating boundary endpoints cannot be
drawn there. This contradicts planarity.

Consequently marked positions are pairwise nonconsecutive in the
cyclic link. Only the required chord edges were used in this argument;
there is no assumption that different recoloring paths are disjoint.

## 5. A local capacity bound

Write I/O on the spokes at b according as they enter or leave b.
Let ell_1,...,ell_r be the lengths of its maximal cyclic constant-direction
runs. Both directions occur, so r>=2.

By Section 2, a marked position is an interior position of a run:
its predecessor and successor have the same spoke direction.
A run of length ell has at most max(ell-2,0) eligible positions.
By Section 4, no two marked positions are consecutive, hence it has
at most floor((ell-1)/2) marks. This formula also gives zero for ell=1.

If q(b) is the number of exceptional vertices supported by b, then
  q(b) <= sum_j floor((ell_j-1)/2)
       <= floor((degree(b)-r)/2)
       <= floor((degree(b)-2)/2).

Degree-four vertices receive no mark by Section 2.
Degree-five vertices receive at most one; if they receive one, Section 3
places them in the nonexceptional degree-five class.

## 6. Combining capacity with Euler's identity

Let n_d count vertices of degree d, B the number of exceptional
degree-five vertices, and G_5 the number of degree-five vertices with
at least two directed incident faces. C18 gives n_5=B+G_5.

Every exceptional vertex sends exactly one mark to its support. Summing
Section 5 and using Section 3 yields
  B <= G_5 + sum_{d>=6} floor((d-2)/2) n_d.                 (1)

Euler's identity for a simple triangulation of minimum degree four is
  2 n_4 + B + G_5 = 12 + sum_{d>=6} (d-6) n_d.          (2)

Substitute (1) into (2) and use
floor((d-2)/2)-(d-6)=5-ceil(d/2). This gives the necessary constraint
  2 n_4 + 2 G_5 + 2 n_6 + n_7 + n_8
    >= 12 + sum_{d>=11} (ceil(d/2)-5) n_d.               (3)

The degree-nine and degree-ten coefficients vanish. In particular at
least six vertices are outside the exceptional degree-five class,
because the left side of (3) is at most twice their total number.

This is a necessary counting inequality, not a discharging contradiction.
Degree-four vertices and nonexceptional degree-five vertices remain,
and degree-six vertices may still support exceptional neighbors.

## 7. Audit and limits

Proof-draft dependencies: C09 selected triangulation and global minimum
order; C18 directed-face existence at degree five; C19 forced directed
separator. The proof is not conditional on accepting the root conjecture.
All contractions used for contradiction retain a smaller graph in its
frozen class and explicitly audit loops, opposite arcs, and cycle images.

Potential pitfalls tested: an existing arc is not reversed; the support
vertex need not itself have degree five; the run bound treats runs of
length one and two; different support triangles can have intersecting
or overlapping complementary regions. No nesting or disjoint-interior
claim is used. The nonconsecutive obstruction uses four distinct chord
endpoints, not unverified recoloring paths.

The count does not say that the support association is injective at
higher degrees. The capacity, not injectivity, is what is proved.
No program, enumeration, proof-assistant replay, or new external theorem
is used. All computations displayed are algebraic counts within the proof.

## 8. Checkpoint

best_verified_result: none
best_verified_candidate: none
best_candidate: candidate:opg169-a01-c21-support-capacity
route_status: open
open_obligations: obligation:opg169-strong-min-degree-three; obligation:opg169-root
failed_routes: authoritative ledger empty; prior local exclusions retained.
next_obligation: obligation:opg169-strong-min-degree-three
next_action: combine support capacity with C17's heavy majority poles
and C11's low-triangle boundary vertices. Their low-neighbor blocks may
consume positions otherwise available for exceptional degree-five support;
audit overlaps before adding contributions.
No mathematical EvidenceLink or Result is claimed.
