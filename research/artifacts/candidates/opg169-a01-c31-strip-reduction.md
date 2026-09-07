# C31 companion: an actual all-exterior alternating-strip replacement

Verdict: candidate_only. Status: proof-drafted with finite generator controls.
Candidate: candidate:opg169-a01-c31-strip-reduction
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Packet target: obligation:opg169-root
Base: bcffc6fe5ed24d412a3100ec75adb9178e770c9e
Primary owner: math-proof. No C27 dependency.

## 1. Exact patch and the replacement claim

Let k>=3. Take distinct poles p,q and distinct path vertices
z0=a,z1,...,z_(k-1)=b, with the two sets disjoint. Put every path arc
z_i->z_(i+1). Label path vertices alternately A,B, starting with either
type. At type A put p->z_i->q; at type B put q->z_i->p. These are all
patch arcs. In particular pq and ab are not patch edges. Denote the
oriented patch by P(k,T), where T is the first type.

It is embedded in a disk whose cyclic boundary is B=(p,a,q,b). A complete
rotation, with the disk exterior distinguished, is
 p: (z0,z1,...,z_(k-1)); q: (z_(k-1),...,z1,z0);
 z0: (p,q,z1); z_(k-1): (p,z_(k-2),q);
 z_i: (p,z_(i-1),q,z_(i+1)) for 0<i<k-1.
Draw a simple a-to-b path across the disk, p-spokes in one resulting
half-disk and q-spokes in the other. This gives the rotation directly.
There are k+2 vertices, 3k-1 edges, 2k-2 interior triangular faces, and
one quadrilateral exterior face. All vertices are distinct and every
edge has exactly its listed direction.

Theorem (static profile equality): with boundary labels, cyclic order,
and endpoint spoke directions preserved,
  profile(P(k,T)) = profile(P(4,T)) for every even k>=4;
  profile(P(k,T)) = profile(P(5,T)) for every odd k>=5.
The profile consists of states of ALL valid acyclic binary colourings,
not merely of a selected threshold colouring. Each state gives boundary
colours sigma and the COMPLETE positive monochromatic boundary relation R.
Empty colour classes are allowed; the relation never includes empty paths.

Consequently, if a graph in the frozen planar-orientation class contains
this disk patch with NO other edges incident to its interior vertices,
an even strip with k>=6 can be replaced by k=4, and an odd strip with
k>=7 by k=5. Every effective colouring of the smaller whole graph lifts
to the original, keeping the exterior colouring exactly unchanged.
The graph loses at least two vertices. This is an actual conditional
reducible configuration, not a claim that every low-degree vertex lies
in one. Global minimum-counterexample exclusion is in Section 5.

## 2. Unequal pole colours: an exact three-case endpoint rule

Fix c(p)!=c(q). Complement all colour names if necessary to normalize
c(p)=0,c(q)=1. Write type A as 0 and type B as 1, and put
  s_i=c(z_i) XOR type(z_i).
A monochromatic cycle must use a pole, because the graph without poles
is a directed path. It cannot use both poles, whose colours differ.

A colour-0 cycle through p starts at an A vertex, follows a nonempty
forward monochromatic ring-path segment, and ends at a later B vertex.
Such a segment contains an adjacent A-to-B pair coloured 00. Conversely
any such adjacent pair closes a directed triangle with p. Thus colour-0
acyclicity is exactly the exclusion of 00 at A-to-B edges. The analogous
colour-1 condition excludes 11 at B-to-A edges, by the triangle through q.
At either edge parity the forbidden pair is exactly (s_i,s_(i+1))=(0,1).
Therefore validity is equivalent to
  s_0>=s_1>=...>=s_(k-1), or s=1^t 0^(k-t), 0<=t<=k.

For specified boundary colours, let sa=c(a) XOR c(p) XOR type(a) and
sb=c(b) XOR c(p) XOR type(b); this formula also covers the unnormalized
pole assignment. The boundary colouring is attainable iff sa>=sb.
The three cases 00,10,11 are all attainable at every k>=3: choose all
zeros, an interior threshold, or all ones. This proves existence, not
just a necessary endpoint condition.

For each such colouring, R is exactly the transitive closure of the
monochromatic BOUNDARY spokes. To prove there is no omitted relation,
consider a positive monochromatic boundary path. If it uses its colour's
pole, any detour from a same-coloured endpoint back to that pole in the
opposite direction to their direct spoke would create a cycle. The same
argument applies to leaving the pole toward an endpoint. Hence the pole
part of any such boundary path is represented by the direct matching
spokes. A path avoiding both poles lies in the directed a-to-b path.
For it to join a to b all k vertices would have to be monochromatic.
As k>=3 and types alternate, the path contains both an A-to-B and a
B-to-A edge, so the preceding forbidden-pair rule excludes either
monochromatic choice. A reverse b-to-a path avoiding poles is impossible.
This exhausts all pairs and proves the asserted full relation.

Thus the unequal-pole part of the profile depends only on the endpoint
types and colours, not on the internal length. It has exactly three
states for each of the two ordered pole colourings, six in total.

## 3. Equal pole colours: exact occupancy regimes and returns

Let c(p)=c(q)=h. Write A_h and B_h for the path vertices of type A and
B coloured h. If both sets are nonempty, any x in A_h and y in B_h give
the monochromatic directed cycle p->x->q->y->p. Conversely, if at most
one set is nonempty, the h-class has only the form p->A_h->q or q->B_h->p,
or two isolated poles. There are no same-h path edges because adjacent
types differ. The other colour has no poles and induces a subgraph of
the directed path. Thus validity is equivalent to at least one of
A_h,B_h being empty.

The three exact regimes are:
 E: neither is occupied; every path vertex is 1-h;
 A: A_h nonempty and B_h empty;
 B: B_h nonempty and A_h empty.
For E the endpoints must both be 1-h, and R={(a,b)}.
For A take the monochromatic boundary spokes and add p->q, then take
positive transitive closure. This is EXACTLY R: the h-class is the
stated two-level graph, and the other colour cannot travel from a to b
because an h-vertex interrupts the only possible path. Regime B is the
same with q->p. No positive diagonal occurs.

Availability is also exact. An h-coloured endpoint forces its own type
to be the occupied type. Endpoints of both different types coloured h
exclude every regime. If neither endpoint has colour h, E is available;
regime A is available precisely when there is an internal A vertex,
and B precisely when there is an internal B vertex. If an endpoint
already supplies the required occupied type, no additional interior
vertex is needed. To realize a permitted regime, colour the forced
endpoints h, choose one additional vertex of that type if necessary,
and colour every other path vertex 1-h. This constructs every listed state.

For even k>=4 there is an internal vertex of each type and the endpoint
types differ. For each h, the four endpoint colour patterns yield
3,1,1,0 regimes (neither, first, last, both endpoints coloured h).
Therefore equal poles yield ten states and the full profile has 16.
For odd k>=5 there is again an internal vertex of each type but endpoint
types agree; the regime counts are 3,1,1,1, giving twelve equal-pole states
and 18 full states. Relations and availability use only the same endpoint
types and the two internal-type existence flags. This proves Section 1
for EVERY permitted k and both starting types. The finite checker is
not used as induction or as a substitute for these classifications.

## 4. Why an odd strip cannot automatically be shortened to three vertices

For k=3 starting A the sole internal vertex has type B. Consider boundary
colours (p,a,q,b)=(0,1,0,1). In P(5,A), colour the middle A vertex z2 with
0 and every other path vertex with 1. The full boundary relation is
R={(p,q)}; there is no same-coloured a-to-b path. This is a valid state.
In P(3,A), giving the sole internal B vertex colour 1 instead yields
R={(a,b)}, and giving it 0 yields R={(q,p)}. Neither choice gives {(p,q)}.
Thus these two profiles genuinely differ. For k=3 there are only 16
states, versus 18 for odd k>=5.
This rules out that particular three-path-vertex substitute. It does not
prove P(5,A) has minimum size among ALL conceivable replacement patches.

## 5. All-exterior lifting and preservation of the frozen graph class

Suppose G=P(k,T) union F, where the two pieces meet exactly in the four
labelled boundary vertices. No edge connects their disjoint interiors.
All shared boundary arcs agree, and ALL graph arcs belong to this union.
F may contain additional boundary edges, such as pq or ab. They remain
in F, with their original directions. The replacement adds neither edge.

Let k0=4 for even k>=6, and k0=5 for odd k>=7. Embed P(k0,T) in the SAME
disk and retain p,a,q,b as distinct vertices in the same cyclic order.
Its first and last types match the old ones because k-k0 is even, so
its four boundary spoke directions agree with the original. Use fresh
internal vertices, or delete the surplus and re-embed the retained ones
inside the disk; their only new edges are the listed path/spoke edges.
No interior vertex has an exterior neighbour by hypothesis. Hence no
new loop, repeated endpoint pair or reverse arc is introduced. Shared
boundary edges are retained once with their single consistent direction.
The outside drawing is unchanged, the inside drawing is planar, and the
replacement has strictly fewer vertices by k-k0>=2. Thus G' is again
an orientation of a finite simple planar graph. This is not an unrestricted
directed contraction, and no boundary vertices are identified.

Take ANY valid colouring of G'. Restrict it to F and P(k0,T). Profile
equality supplies a valid colouring of P(k,T) with EXACTLY the same sigma
and R as that small-patch restriction. Keep every exterior colour fixed.
The resulting colouring of G is valid: if a monochromatic cycle used
both pieces, split it at boundary visits into positive boundary paths.
These give a cyclic chain in the union of their boundary relations.
The identical relations in G' would expand to a positive monochromatic
closed walk, hence a directed cycle, contradicting its validity. Cycles
lying wholly in either piece were already excluded. This proves lifting
for every exterior, not just for the source star or sampled exteriors.

For a hypothetical minimum-order counterexample containing this patch,
G' has fewer vertices and lies in the FULL contract class, so it has a
valid colouring. The lift contradicts that G is a counterexample.
Therefore no such isolated long alternating strip occurs in a minimum
counterexample. This is a genuine colouring-liftable subclass. Euler's
low-degree inequality still has not been shown to force this subclass:
nonuniform strips, isolated degree-four cores, and degree-five patterns
without this interior geometry remain open.

The dynamic classes of long strips may remain large (C31 core-family
proof). That does not obstruct this argument: minimum-counterexample
replacement needs existence of a full lifted colouring, not a sequence
of legal moves from an arbitrary preselected old colouring. This explicit
example separates those two quantifiers constructively.

## 6. Actual controls, provenance and independent obligations

The companion checker enumerates ALL binary colourings for path sizes
k=3,...,9, both initial types, with poles included. It uses direct Kahn
acyclicity and positive transitive closure as two cycle tests, and compares
the actual full profile to the symbolic classification. It checks every
rotation neighbour, the complete face permutation, quadrilateral boundary
order and triangular interior faces. All 14 cases and eight long/short
comparisons passed in the selected bounded CPython 3.13.5 execution.
There are 8128 complete colour assignments in this finite allocation.
The k=3 missing-state control is retained. The complete profiles for
k=3,4,5 and both initial types are saved in the actual output.

The selected source enforces one-CPU affinity, 512 MiB address space,
CPU20s, wall alarm25s, per-output-file65536 bytes, and seccomp denial of
socket/socketpair/connect. The parent also enforced a30s timeout. Actual
exit code0, no timeout and no stderr are recorded separately with hashes.
No external math library, Lean declaration or source theorem is treated
as an executed verifier. Lean/elan were not found by the current probe;
no elaboration/axiom report or trusted admission is claimed.

Dependencies are: explicit patch -> exact two-pole cycle classification
-> all-boundary profile equality -> same-disk smaller graph -> all-exterior
colouring lift -> minimal-counterexample exclusion. C13/C30 supply prior
context for composition, but the needed path argument is supplied here.
The C31 core-family proof gives separate dynamic-width and safe-policy
results; its statement that the controller is not a graph replacement
remains true. THIS companion adds a graph replacement for the narrower
isolated, uniformly alternating strip configuration.

T3, T4, C30 dynamics, C31 width/policy, this strip reduction, and root have
separate review scopes. No new admitted obligation record is invented.
Primary remaining root work is an unavoidable family covering the other
strong-deletion degree-four configurations and both degree-five signs.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
first_open_configuration: degree4 (2,2) common-SCC double block outside an
  isolated long uniformly alternating strip; degree5 (2,3)/(3,2) without
  a forced safe-policy invariant or an all-exterior smaller patch
next_obligation: obligation:opg169-root
next_action: test nonuniform strip orientations and local orientation defects;
  prove the required all-exterior lift and an unavoidability bridge rather
  than extrapolating these 14 finite controls
root_closed: false
