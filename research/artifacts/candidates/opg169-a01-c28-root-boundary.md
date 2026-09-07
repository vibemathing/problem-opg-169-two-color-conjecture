# C28: an SCC-exchange reduction, exact low-degree interfaces, and a two-step obstruction

Verdict: candidate_only. Status: proof-drafted with bounded generator self-tests.
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Current packet target: obligation:opg169-root
Base: 16b9fbcf379719f4fad59a364151ff36f1bbb772
Primary owner: math-proof. No C27 dependency or extension.

## 1. Scope and the actual discharging gap

Keep finite simple planar orientations, full induced acyclic color classes,
and colors 0,1 with unused colors permitted. T3 is the admitted necessary
condition (strong connectivity and underlying minimum degree three).
T4 is the separately identified degree-four/semidegree-two candidate.
Neither is an admitted verifier conclusion. The root remains the universal
existence of an acyclic two-coloring, not a structural necessary condition.

Conditional on a vertex-minimum counterexample and T4's supplied proof,
write n_j for the number of vertices of underlying degree j. The simple
planar inequality m<=3n-6 gives
  2*n_4+n_5 >= 12 + sum_{j>=7}(j-6)*n_j.
Thus at least one degree-four or degree-five vertex exists. This does NOT
say a fixed deletion coloring extends there. C04 already records this
charge calculation and its octahedral equality example; it is reused,
not presented as a new contradiction or an unexamined discharging rule.

Deletion of v preserves the whole frozen class and strictly lowers its
finite order. Recoloring never changes the graph, its rotation system,
or its induced arc sets. No contraction is used in the reduction below.
The empty and singleton cases and SCC condensation proof are in T3/T4;
we use nonempty strong connectivity only where expressly stated.

## 2. Actual degree-four blocking and planar separation

Let H=G-v and let c be ANY valid coloring of H. If giving v color k fails,
a new monochromatic simple directed cycle must contain v. Its predecessor
is an incoming neighbor i_k and its successor an outgoing neighbor o_k.
Removing v gives a k-colored positive directed path o_k to i_k in H.
Conversely such a path, with the two indicated incident arcs, completes a
monochromatic cycle. No loops or opposite arcs means i_k,o_k,v are distinct.
A path through v, a reverse path or an internally mixed-color path does not
qualify. Mere same-color neighbors are not a sufficient obstruction.

If degree(v)=4 and both colors fail, its semidegrees are two, each color
occurs once on each side, and the two colored return paths are disjoint.
Adding their incident arcs gives two simple cycles meeting only at v.
The ends of these cycles cannot alternate in the rotation at v: one is a
Jordan curve, while the other minus v is connected and disjoint from it.
Its two ends cannot lie on opposite sides. This is C03's separation fact,
with the actual paths, not imagined edges, as its witnesses.

For an I,I,O,O cyclic rotation there is exactly one noncrossing in/out
matching; for I,O,I,O there are two. A simultaneous block requires one
of those matchings, and still requires both genuine return paths.

## 3. New reduction R4-SCC: at most one full-SCC palette exchange

Claim: in a plane orientation, let v have degree four and let H=G-v have a
valid coloring c. If the four neighbors of v are not all in one SCC of H,
then c extends after interchanging 0 and 1 on at most ONE SCC of H.
SCC here means an SCC of the entire uncolored digraph H, NOT of a color
class. The latter is already acyclic and has singleton SCCs.

First, a full-SCC palette exchange preserves validity of H: every directed
cycle lies entirely in an SCC. On that SCC either no color changes or every
color changes, so a formerly nonmonochromatic cycle cannot become monochromatic.
Cross-SCC induced arcs are retained; no directed cycle uses them cyclically.

If the original coloring already extends, do nothing. Otherwise use the
four witnesses of Section 2. If the two incoming neighbors lie in different
SCCs, flip the SCC of one of them. Their colors become equal, so the other
color has no incoming neighbor and is safe at v. This proves the claim in
that case. If the outgoing neighbors lie in different SCCs, the corresponding
flip makes them equal, and the color absent on the outgoing side is safe.

It remains that the incoming pair lies in an SCC A and the outgoing pair
in an SCC B. Under the claim's hypothesis A and B are distinct. Connect the
two incoming neighbors by a simple underlying path inside A and the two
outgoing neighbors by one inside B. These paths are disjoint. Adding v and
their respective incident edges gives two underlying Jordan cycles meeting
only at v. Hence the I/O rotation cannot alternate; it is I,I,O,O.

The old two blocking cycles use its unique noncrossing in/out matching.
Flip every color in B, leaving A unchanged. The coloring of H stays valid.
Both outgoing neighbor colors reverse while both incoming colors stay put.
Consequently the same-color in/out matching switches to the OTHER matching.
If both colors still blocked, their disjoint colored return paths would
realize that alternating matching, contradicting planar separation.
So at least one color now extends to v. This proves R4-SCC for every order.

Corollary for a hypothetical vertex-minimum counterexample: deleting ANY
of its degree-four vertices leaves a strongly connected digraph.
Indeed a valid coloring of H exists by minimality. R4-SCC forces all four
neighbors into one SCC S. Since G is strongly connected, any x in H lies
on an H-walk from some outgoing neighbor to x and then to some incoming
neighbor: take simple v-to-x and x-to-v paths and delete their occurrences
of v. Thus S reaches x and x reaches S, so x belongs to S. All of H is S.

This closes a genuine reducible subclass. It does not prove a minimum
counterexample contains such a subclass: H may be strongly connected at
all its degree-four vertices, or the available low vertex may have degree five.

## 4. A seven-vertex obstruction to ONE-step recoloring

Here is a complete oriented planar graph on vertices 0,...,6. Its arcs are
  0->4, 0->6, 1->2, 1->3, 1->5, 2->0, 2->6, 3->0,
  3->2, 4->1, 4->3, 5->0, 5->4, 6->1, 6->5.
It is the pentagonal bipyramid, with poles 0,1 and ring 2,3,4,5,6.
A sphere rotation system, listing all neighbors in order, is
  0: 2,3,4,5,6       1: 2,6,5,4,3
  2: 0,6,1,3         3: 0,2,1,4
  4: 0,3,1,5         5: 0,4,1,6         6: 0,5,1,2.
The dart permutation (a,b)->(b,next_b(a)) has ten triangular faces;
7-15+10=2. The checked rotations and every facial walk are in the output.
Equivalently draw the ring on the sphere and place the poles in opposite
hemispheres. Each edge has precisely the one direction listed above.
Every ring vertex has in=out=2; pole 0 has (in,out)=(3,2), and pole 1 has
(2,3). Thus delta=4 and average degree 30/7<6. The directed ring and both
poles' access to it also show strong connectivity.

Delete v=5. Use X_1={1,2,4}, X_0={0,3,6}; the two full induced digraphs
are the paths 4->1->2 and 3->0->6. Giving 5 color 0 creates
0->6->5->0, and giving it color 1 creates 1->5->4->1.
Here 5 has rotation O,O,I,I and the correct noncrossing blocking pairs.

All SIX single-vertex recolorings of H are audited below. A cycle in H
means that proposed move is not legal; an otherwise valid move still
leaves both displayed cycles through 5.

| Flipped vertex | Consequence |
|---|---|
| 0 | Invalid: monochromatic 0->4->1->2->0 |
| 1 | Invalid: monochromatic 0->6->1->3->0 |
| 2 | Valid on H, but both cycles through 5 remain |
| 3 | Valid on H, but both cycles through 5 remain |
| 4 | Invalid: monochromatic 0->4->3->0 |
| 6 | Invalid: monochromatic 1->2->6->1 |

Nevertheless TWO moves work: flip 2, then 0, and give 5 color 0.
The color-one masks are 22 -> 18 -> 19 (bit x is the color of vertex x).
The final full partition is X_1={0,1,4}, X_0={2,3,5,6}, whose induced
paths are 0->4->1 and 3->2->6->5. Each intermediate H-coloring is valid.
Thus the graph is NOT a root counterexample and NOT an obstruction to
arbitrary-length recoloring. It exactly defeats the claim that at most
one legal single-vertex change always suffices at a degree-four vertex.

The whole H is one SCC: 0->4->1->2->0 is a directed cycle, 3 is joined
by 1->3 and 3->0, and 6 by 0->6 and 6->1. Its full-SCC palette orbit has
only the original coloring and its complement, both blocked at 5.
Repeated SCC-only exchanges cannot escape this orbit. Flipping vertices
inside that SCC is a different operation, as the successful two-step
sequence demonstrates.

Minimality is restricted to graphs satisfying the global necessary bounds
(delta>=4 and both semidegrees>=2). For n<6, 4n<=2m<=6n-12 is impossible.
At n=6 every degree is four, and the complement of the underlying graph
is a perfect matching; hence the underlying graph is the octahedron.
The exact checker visits all 4096 orientations of that labeled octahedron,
including all 38 with semidegrees two, all six deletions and 4104 valid
deletion colorings. Every blocked coloring there has a one-step escape.
Together with the displayed seven-vertex witness, this gives a replayable
finite minimality certificate in that restricted class, not an independently
admitted classification or a claim about arbitrary planar patches.

The same run visits all 32768 orientations of the pentagonal bipyramid;
180 meet the semidegree bounds. Among their degree-four deletions, 2680
valid colorings are blocked and 40 require two moves. All escape within
two moves in this finite test. No general two-move theorem is inferred.

## 5. Exact finite boundary states for double blocking

Cut out a disk neighborhood of the embedded star at v, with its distinct
neighbors on the boundary in their actual cyclic order. All other arcs
are in the complementary disk on the sphere. For a valid coloring of
that exterior, record its boundary colors sigma and, separately for each
color, the positive directed reachability relation R on boundary vertices.
R is irreflexive and transitive. Empty paths do not contribute diagonal
entries. This is a state of one coloring, not the profile of all colorings.

If two comparable pairs of DIFFERENT colors have alternating endpoints,
their disjoint paths would cross in the disk. Such a state is impossible.
For four boundary vertices with a two/two color split, this condition is
also sufficient for realizability: each color pair has no path, a forward
path or a backward path, and the required pairs can be drawn as noncrossing
chords with the recorded directions. There are four nonalternating color
words contributing 9 states each and two alternating words contributing
5 each. Thus there are exactly 46 exterior states. With the six balanced
I/O assignments there are 276 signed states, of which exactly 16 block
both extensions. The entire 276-row table is saved, including arc direction.
Color splits zero/four or one/three cannot block both colors and need no
new reduction. For I,I,O,O there are 2 blocked color-named states; for
I,O,I,O there are 4, for each fixed labeled I/O word.

For five boundary vertices only a two/three color split can block both.
A strict partial order on three labeled points has 19 possibilities, and
on two points it has 3. The cover graph of a three-point order has at most
two edges, sharing an endpoint when there are two. Therefore cover arcs
of each color can be drawn as chords; different-color interlacing is the
only obstruction in these particular two/three splits.

There are ten color words whose minority pair is adjacent on the boundary;
all 19*3=57 states are possible for each. There are ten whose minority pair
is nonadjacent. If that pair is incomparable, all 19 orders on the majority
triple are allowed. If it is comparable, its chord separates the remaining
vertices into a singleton and a pair. The singleton must be incomparable
with that pair, leaving 3 orders on the pair and 2 minority directions.
Thus each such word has 19+2*3=25 states. The total is
  10*57+10*25 = 820.
This sufficiency construction is special to color groups of size at most
three; no such sufficiency is asserted for general boundary sizes.

There are twenty direction assignments with in/out sizes two/three or
three/two. All 16400 signed states were tested by explicit Hasse-arc
realizers, their sphere rotations, and direct induced-cycle checking.
Exactly 1160 block both colors. At the unique two-neighbor side the colors
must differ; for each color at least one opposite-side neighbor must have
a directed return path to its matching small-side neighbor. This includes
the disjunction over two possible same-color neighbors on the larger side.
The five-boundary rows are streamed into a reproducible SHA-256 digest;
no separately saved full table is claimed. The source specifies their order.

## 6. Composition and why a static state is not a recoloring algorithm

Reuse C13's exact composition rule. Pieces P and F meet exactly at their
labeled boundary and have no interior-to-interior arcs. With matching
boundary colors, their full induced union is acyclic exactly when
(R_P union R_F)^+ has no diagonal. A cycle crossing pieces cuts into
positive boundary paths. Conversely a cyclic relation chain expands
into a positive monochromatic closed walk and hence a directed cycle.
This proves both directions even when expanded paths share internal vertices.
The checker tests 374 matching four-boundary state pairs, subdividing each
piece's arcs with its own fresh vertices so opposite relations never create
an illicit boundary digon in the underlying orientation. Of these unions,
136 are cyclic, precisely as the relation test predicts.

Uncolored SCC information is extra data: optionally record positive
uncolored boundary reachability U, including its possible diagonal.
Under composition U is updated by positive transitive closure of the
union, with equality allowed separately for SCC membership. Colored R
must still reject diagonal entries. This keeps reflexive reachability
and cycle detection distinct.

The C02 octahedral deletion has a boundary state with two directed same-color
pairs, just like a four-vertex matching realizer of that state. The matching
has singleton SCCs while the octahedral deletion is strongly connected.
Consequently equal (sigma,R) does not determine the palette-exchange orbit.
Even augmented static states must not be treated as freely composable
recoloring moves: every move requires a lift to the SAME current coloring.
Profiles of all states preserve static colorability, not automatically
reconfiguration connectivity or a bounded number of moves.

A legitimate replacement criterion is one-sided: if every state of a
smaller patch P' has a state of P with the same boundary colors and
R_P contained in R_P', any coloring of P' glued to F lifts to a coloring
of P glued to F. Any smaller reachability union remains acyclic. The
actual lifted coloring witnesses the chosen P-state; none is assumed.
To apply minimality also require P' in the same disk with the same cyclic
boundary identification, no new opposite boundary arcs, coincident shared
arcs kept once, distinct boundary vertices, and strictly fewer interior
vertices. Then simplicity, orientation and planarity are preserved.
No such dominating smaller patch is claimed for the remaining strongly
connected degree-four exterior or for all degree-five states.

## 7. Execution, provenance, and remaining obligations

The original frozen degree-four enumerator and 21-fixture input were
reconstructed from fresh connector text and matched to BOTH original
Git blob identities and SHA-256 hashes before execution. The actual
0..4 run finished: 761 orientations, 23665 deletion assignments, 23233
valid and 432 invalid deletion assignments, 46466 tested extensions;
all 21 fixtures and five deliberately wrong-semantic controls passed.
The invalid assignments are rejected inputs, not theorem counterexamples.

Actual runtime: CPython 3.13.5, not the earlier proposed 3.12.10 pin.
Each selected run has a 120-second external wall cap, 105 CPU seconds,
512 MiB address-space cap, one CPU affinity, 65536-byte stdout/stderr file
caps, and network socket-family syscalls denied by seccomp. Both selected
runs exited zero. These are generator self-tests under this turn's explicit
bounded-execution request, not GitHub Actions mathematical execution or
registered verifier receipts. The profile and all trust policies remain
unchanged. Actual metadata and compact outputs are retained separately.

Lean and elan were not found in the current executable search. No Lean
elaboration or axiom/escape report occurred; C07/C08 remain unelaborated.
The existing verifier request remains pending trusted scope, the correct
runtime pin, full-target formal bridges and real receipts. Local Python
runs do not discharge its kernel, axiom or semantic gates.

Logical dependency/status separation:
- T3: existing admitted obligation; proof candidate unchanged, admission open.
- T4: existing stronger candidate; bounded replay now performed, admission open.
- R4-SCC: new proof candidate above; implies the strongly connected deletion
  restriction conditionally on T4 and minimality; no new ledger object.
- R4-one-step: precisely failed shortcut, with the seven-vertex witness;
  not a failure of T3, T4, arbitrary recoloring, or the root route.
- R4-core: open configuration, degree four with H strongly connected and
  a noncrossing two-return-path state. A globally valid multistep escape
  or a strictly smaller liftable replacement is not supplied.
- R5: open configuration, semidegrees two/three and one of the 1160
  double-blocked signed states. No unavoidable reducible subfamily proved.

Root candidate progress consists of R4-SCC, the exact interfaces, executed
checks and precise shortcut obstructions. It does NOT include a planar
contradiction or a universal two-coloring. Packet/checks/merge cannot
close these gaps. No EvidenceLink, Result or Solution is signed or edited.

Sources at the base: planar root contract; T4 proof/enumerator/mutations;
C03 for rotation separation; C04 for the charge identity; C13 for static
composition; C02 for the six-vertex benchmark; C07/C08 and their semantic
notes only for formal status. Prior candidates are dependencies to review,
not mathematical Evidence. The abstract of Bousquet et al., Digraph
redicolouring, arXiv:2301.03417, was consulted for context: single-vertex
redicoloring has its own nontrivial reachability problem. No theorem from
that paper is an unproved premise here, and no novelty claim is made.

Checkpoint state: NONTERMINAL_CHECKPOINT.
Best verified/admitted result: none.
First open configuration: R4-core above; R5 remains separate.
Next action: preserve actual rotation and state witnesses while seeking a
multi-step recoloring/lifting invariant on R4-core, then a degree-five
reducible family; request trusted replay and statement-faithfulness in parallel
as coordination only, with no claim of background execution.
