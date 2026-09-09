# C36 incoming fifth neighbour: one deleted vertex with a fixed six-port lift

Verdict: candidate_only. Status: proof-drafted with bounded finite certificates.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: 0ce8698f6fb4c5e7e9e8438cbceca19af39949c3
Owner: math-proof. Existing C36 branch is reused, not replaced.

## 1. Frozen statement and the important retained-colour distinction

All graphs are finite simple planar orientations. A valid two-colouring makes
BOTH complete induced colour classes acyclic; empty classes are allowed. Cycles
and the boundary reachability relation R use positive length, not reflexivity.

The only new domain is the fixed C35 J-direction with d(7)=5 and a genuinely
new fifth neighbour z pointing to7. Label z=1. The other two edges of its actual
outside triangles are to11 and8. They have distinct endpoints: the old six-port
J boundary is (4,5,6,11,7,8), and z is distinct from all its vertices and J.
No equality of these two endpoint edges is compatible with this frozen domain.
The old-port identifications and the outgoing fifth-neighbour case belong to
prior C36 material and are NOT re-enumerated here.

The original controlled interior is I=(0,2,3,7), boundary B=(4,5,6,11,1,8).
Each I vertex has its full underlying degree five and no unlisted neighbour.
The new replacement Q=P-3 retains local interior K=(0,2,7). Its K colours MAY
be reassigned when lifting. Every vertex OUTSIDE I, not merely B, stays fixed.
This is not the false assertion that every colouring of G-3 extends with ALL
retained colours fixed. The certified reassignment is simultaneous; a sequence
of individually legal one-vertex flips is neither needed nor claimed.

The theorem candidate: every graph in the contract containing this saturated
signed plane patch has the property that every valid colouring of G-3 lifts
to a valid colouring of G with all exterior-of-I colours fixed. Consequently
this configuration cannot occur in a vertex-number-minimum counterexample.

## 2. Complete arcs, rotations, and all four remaining directions

Eighteen arcs are fixed:
  0->2,0->4,2->3,2->6,2->11,3->0,3->4,3->7,4->5,
  4->8,5->0,5->6,6->0,7->2,7->8,8->3,11->6,11->7.
The remaining arcs are chosen on endpoints (11,7,8): bit j of w means z points
to that endpoint; an unset bit means the reverse. Exactly w=2,3,6,7 have z->7.
Thus the complete cases are
  w2: 11->z, z->7, 8->z;
  w3: z->11, z->7, 8->z;
  w6: 11->z, z->7, z->8;
  w7: z->11, z->7, z->8.
Each case is a simple orientation of the SAME ten-vertex disk; none is omitted
on the basis of a convenient exterior colouring or an unknown exterior degree.

The full patch rotation is
 0:(2,6,5,4,3); 2:(0,3,7,11,6); 3:(0,4,8,7,2);
 7:(1,11,2,3,8); 1:(7,8,11); 11:(1,6,2,7);
 4:(0,5,8,3); 5:(0,6,4); 6:(0,2,11,5); 8:(1,7,3,4).
It has21 edges,12 inner triangles and one outer hexagon, so10-21+13=2.
Every interior link is the complete degree-five star from the frozen graph.
All additional boundary chords and longer external paths remain in the exterior.

Q removes vertex3 and its FIVE arcs 2->3,3->0,3->4,3->7,8->3. It adds nothing.
Its nine vertices and16 edges have seven triangular faces, the hole
(0,2,7,8,4), and the outer hexagon. These are the actual restricted rotations.
The net order drop is one, the smallest possible positive integer drop; no
minimum-separator or minimum-recolouring theorem among all gadgets is claimed.

## 3. Full-assignment certificate, not a boundary projection

Index a boundary word b by B order, and a replacement interior word k by
K=(0,2,7). The vector index is8*b+k, ranging from0 through511. A hexadecimal
entry encodes the FOUR original interior colours in order I=(0,2,3,7).
A '-' means exactly that the full Q assignment itself is invalid. It does
not mark an unchecked or failed valid assignment. All vectors are retained
uncompressed in incoming-lift-vectors.json and in the full archived certificate.

| w | all Q assignments | valid with full P lifts | invalid | equal R | strict R containment |
|---|---:|---:|---:|---:|---:|
|2|512|162|350|151|11|
|3|512|160|352|151|9|
|6|512|216|296|205|11|
|7|512|216|296|200|16|
|total|2048|754|1294|707|47|

For every valid index the certificate proves sigma_P=sigma_Q, acyclicity of
both FULL induced P colour classes, and R_P subseteq R_Q. R records every
positive monochromatic boundary path, including paths through other boundary
vertices. Here equality is NOT automatic because K may be reassigned:47 maps
strictly decrease R.620 maps leave K fixed,100 change one K vertex,34 change
two. No selected map changes all three or changes any boundary vertex.

The finite procedure terminates: four fixed arc sets,64 boundary words,eight
Q interior words,and at most16 P interior words. Invalid Q words are checked
explicitly, not discarded by an assumed characterisation. This finite table is
the entire proof certificate for this fixed local domain, not a sampled claim
about arbitrary graph order. The generator uses positive closure/Kahn deletion;
a separately coded consumer reconstructs the arcs and uses DFS/BFS. Both share
a generator trust domain. A matching trusted receipt remains absent.

## 4. Every exterior lifts, and class preservation is literal deletion

Let G contain this exact saturated patch P, and put G'=G-3. The restriction of
any valid G' colouring to Q is one of the valid table indices. Take its P lift,
keep EVERY vertex outside I fixed, and replace only the controlled I colours.
All arcs at K and3 belong to P, because their complete original stars were
specified. Hence no unaccounted K-to-exterior arc is affected by reassignment.

Let F contain all other vertices/arcs, including additional boundary chords.
P and F meet only at B, allowing shared boundary arcs to count once. If a new
monochromatic cycle lies inside P or F, it contradicts the respective validity.
Otherwise cut it at successive B visits. Replace each positive P segment by
the same-colour Q path guaranteed by R_P subseteq R_Q, keeping F segments.
The resulting positive closed walk is in the original valid colouring of G'.
It contains a directed cycle: choose equal positions with least positive
separation. This contradiction proves the lift for ALL exteriors, including
arbitrarily long paths, not just the direct chords tested by the checker.

G' is an induced subgraph: finite, simple, planar and oriented, with one fewer
vertex. There is no added arc, contraction, port identification, inverse-arc
guard, or assumption that exterior chords are absent. Its degree/semidegree
bounds need not match those derived for minimum counterexamples. Minimality
applies to the entire original contract class. It supplies a valid colouring
of G', whose lift contradicts a minimum counterexample containing P.

This closes the four incoming d5 cases as a proof/certificate candidate. In
combination with the separately preserved earlier C36 degree4, outgoing-d5 and
old-port cases, a minimum counterexample with this J-direction must have d(7)>=6.
That combined conclusion retains those earlier dependencies; their controls
were not rerun or relabelled as a new execution. Other J exteriors and root
remain open. No result admission is inferred from a candidate or CI.

## 5. Real plane extensions and all actual external colours

Each of the four core directions is realized by a complete12-vertex simple
plane orientation of the frozen underlying map, with every degree5 and both
semidegrees at least2. Complete arc sets are in the certificate; only the nine
edges outside this core were oriented to achieve the bounds. These graphs are
explicitly colourable controls, not minimum counterexamples.
The complete G-3 colourings number338,338,446,440 for w2,w3,w6,w7. All1562 lift,
with all EIGHT vertices outside I unchanged. This does not fix the old failing
nine-vertex exterior from a different direction graph and pretend it is still
the same input. Selected maps also pass full-arc reversal checks.

For each word all215 absent/directed noncrossing direct exterior chord sets
were retained. The valid chorded Q assignments total29128,26636,38432,37926,
respectively,132122 altogether. The same actual chords are present before and
after every check. These bounded controls test the quantified argument in4;
they do not replace that argument or claim all full planar graphs enumerated.

## 6. Complete double-payment bookkeeping, with no new money

No charge rule is changed. On the original selected minimum-counterexample
model retain DC2: gamma(v)=(d(v)-4-2t(v))/d(v), each marked pair gets one unit
on EACH incident face, and every vertex pays gamma at each of its d corners.
Its debit is2t+d*gamma=d-4, final0. Every face uses length-4+sum gamma+h.
The smaller graph is a minimality device, not a source of new charge in G.

Although only3 is deleted,0,2,7 can change colour, so ALL12 original triangular
faces meeting I are accounted. Interior vertices have degree5,t0,gamma1/5.
Writing g_v for each actual boundary gamma, the per-face values are
 (0,2,3): -2/5; (2,7,3): -2/5;
 (0,3,4): -3/5+g4; (0,6,2): -3/5+g6;
 (2,11,7): -3/5+g11; (3,7,8): -3/5+g8;
 (0,4,5): -4/5+g4+g5+h045;
 (0,5,6): -4/5+g5+g6+h056;
 (1,7,11): -4/5+g1+g11+h1711;
 (1,8,7): -4/5+g1+g8+h187;
 (2,6,11): -4/5+g6+g11+h2611;
 (3,8,4): -4/5+g8+g4+h384.
Faces with fewer than two boundary vertices cannot contain a marked degree-four
edge, so their h is zero. The other h values are NOT assumed zero in a general
exterior: every actual unit payment is retained once.

The sum is -8+2g1+3g4+2g5+3g6+3g8+3g11+sum(h).
Relative to the OLD single-payment rule the change over these faces is exactly
 extra unit receipts -2t1/d1-3t4/d4-2t5/d5-3t6/d6-3t8/d8-3t11/d11.
These are all16 boundary corner losses; the20 interior corners have t=0.
Every other face keeps the same per-corner DC2 formula. No old positive-face
list is silently reused after a gamma decrease.

In each complete degree-five realization, ALL vertices have t0 and ALL faces
h0. Each of12 vertices starts1, sends1/5 at five corners and ends0. The12
controlled faces total-24/5 and the other8 faces total-16/5, each face-2/5,
all20 total-8. A configuration exclusion does not relabel its numeric charge
as positive. No all-nonnegative ledger, root colouring proof or root witness
is obtained.

## 7. Reproduction, provenance and remaining obligation

The exact existing c36-input.json bytes are unchanged. Replay the new incoming
check and incoming audit through incoming-replay.py, or assemble the archived
certificate before consuming it. The new programs enumerate only words2,3,6,7;
no outgoing case, old nine-degree table, old J direct-restoration assertion or
uniform dynamic-width route is reopened. Existing older C36 source files remain
historical, not this turn's executable input or a trusted receipt.

Actual CPython3.13.5 generator and consumer exited0 with no timeout/stderr,
under one CPU,512MiB address space,CPU30s/wall35s/parent38s,1MiB file caps and
seccomp denial of socket/socketpair/connect. Their exact hashes, times and
outputs are separate records. Lean/elan lookup found no entry; elaboration
not_run, axiom_report null. No verifier identity, EvidenceLink, Result or
Solution is self-signed. A scoped trusted review request remains necessary.

Dependency chain: fixed complete stars/plane rotation -> four direction sets
-> all valid Q assignments and full R-contained P lifts -> arbitrary exterior
path composition -> one-vertex size drop -> conditional local exclusion.
The charge formulas are a separate unchanged-accounting chain, not proof of
unavoidability. Probability and asymptotic heuristics are not used.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
incoming_d5_remaining_cases: [] at proof/certificate scope
first_open_configuration: same J-direction with d(7)>=6; other unpaid signed
triangles and exterior constraints not covered by this patch remain open
next_obligation: obligation:opg169-root
root_closed: false
