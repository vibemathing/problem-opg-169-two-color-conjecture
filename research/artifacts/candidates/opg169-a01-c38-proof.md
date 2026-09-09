# C38: releasing a forced port of D/19, with quantified residuals

Verdict: candidate_only. Status: proof-drafted with reproducible finite controls.
Repository: vibemathing/problem-opg-169-two-color-conjecture
Problem: problem:opg-169-two-color-conjecture
Attempt: attempt:web-20260906-opg169-a01
Route: route:minimal-counterexample-structure-v1
Graph: graph:opg169-initial-v1
Target: obligation:opg169-root
Base: 81882fe9d01f0a13600bdceb175394a584f4e285 (merged C37).
Primary owner: math-proof. No truth-ledger or Result authority is claimed.

## 1. Frozen domain, expert handoff, and what is reused

Graphs are finite simple planar orientations. Both FULL induced colour classes
must be acyclic; unused colours are allowed. R means all positive monochromatic
paths between the explicitly listed retained ports. Only the selected minimum-
order counterexample representative is assumed triangulated. Smaller graphs
need only belong to the full original contract, not its critical subclass.

Only local D/10 = remote C37 D/19 is studied. Our x=12 is next to11 and y=13
next to8; exchange names12/13 to obtain C37's remote coordinates. The new arcs
are exactly11->x,y->x,y->8,x->7,7->y. In particular7->y->x->7 is retained.
The controlled old set is I0=(0,2,3,7); degrees0,2,3 are5 and degree7 is6.
Its complete rotation is7:(x,11,2,3,8,y), up to cyclic shift. The old five
ports B0=(4,5,6,8,11) are distinct from x,y and I0.

The user named J_mono_old_boundary_unique_lift and a six-family ledger gap.
An exact-name main search and a search of all Issue3 comments did not locate
an original expert report. No external report or trusted review is invented.
The following precise five-port lemma is reconstructed from the frozen arcs:
if B0 is uniformly coloured a, the ONLY valid colouring of the 18-arc old core
on I0 is (1-a,a,1-a,1-a). Cycles0->4->5->0 and3->4->8->3 force0,3 to1-a;
0->2->3->0 forces2=a; 2->11->7->2 forces7=1-a. The assignment itself is valid:
the1-a class has only3->0 and3->7 among its nontrivial arcs; the a class has
arcs from2 and4 through11/5 to6/8, with no return. Thus existence as well as
uniqueness is checked. Fixing x=y=1-a makes the retained outer triangle fail.

This statement uses FIVE ports. If one instead includes7 in a uniformly a
six-port old J boundary, there is no extension, not a unique extension. The
boundary set must not be silently changed when reusing the named lemma.
This forcing observation is reused to choose a port to release, not advertised
as a new root theorem. No old delete3/recolour-I0 table is expanded here.

C35 already proves the exact arithmetic domain d>=max(3t,2t+4) and six symbolic
L/N/P sign families. It explicitly does NOT prove planar realizability or an
unavoidable reducible set. That coverage gap is retained without duplicating
its enumeration. In particular C38 will not relabel all arithmetic families
as handled after eliminating one signed subconfiguration.

## 2. Minimal nonzero port release and all degree-four identifications

To permit x's colour to change, include its COMPLETE star in the controlled
region. It has known neighbours11,7,y. If d(x)=4, its remaining neighbour z
is forced by the actual outside faces(x,11,z),(y,x,z). Since11->x,y->x and
x->7 are fixed, semidegrees>=2 force x->z. The two other edge directions
z--11 and z--y are NOT assumed. Similarly, if d(y)=4, its actual outside
faces are(y,x,z),(8,y,z), and semidegrees force z->y.

This frees ONE original port, the smallest positive number of freed ports.
It is not a claim of minimum separator size among every conceivable gadget.
The surviving controlled vertices may be reassigned simultaneously; all other
vertices, including every retained port and all distant exterior vertices,
remain fixed. We do not assert a sequence of single-vertex recolourings.

The new neighbour cannot be a repeated neighbour or the released vertex
itself, by simplicity. It cannot be0,2,3 because their complete degree-five
stars would acquire an extra neighbour. For x, the remaining possibilities
are z new,4,5,6,8. The case z=8 closes the three-neighbour link of y=13,
contradicting minimum degree4. For y the possibilities are new,4,5,6,11;
z=11 similarly closes the three-neighbour link of x=12. These exclusions use
actual facial sectors, not the degree in an arbitrarily truncated subgraph.

Retain every other identification, including z=6 for x and z=4 for y, where
another retained vertex has a closed degree-four star. Depending on the alias,
the exterior has a pentagonal boundary or two complementary regions sharing a
retained port. A retained vertex with no exterior incidence is allowed in B.
The face/rotation records do NOT declare complementary regions empty in G.

Each single-star case has four choices on endpoints(a,b): a=11,b=y for x,
a=x,b=8 for y. Bit0 of w chooses a->z, otherwise z->a; bit1 chooses b->z,
otherwise z->b. Existing directions are retained, so z=6 at x forces w odd
(11->6 already exists); z=4 at y forces w<2 (4->8 already exists).

When BOTH x,y have degree4, the unique actual face on the other side of xy
forces their fourth neighbour to be the SAME z. Distinct fourth neighbours
are incompatible with that facial third vertex. The new faces are
(x,11,z),(y,x,z),(8,y,z); the forced arcs are x->z and z->y. The remaining
z is new,4,5,6; the old complete stars and distinct degree-four neighbours
exclude all others. For this case the two w bits are on endpoints11,8.
All old-port cases are kept, with actual duplicate-edge directions enforced.

Complete allocation: 40 single-star direction slots plus16 double-star slots.
Eight slots are excluded by the two closed degree-three identifications;
eight further slots contradict an already present arc. Forty oriented plane
cores remain. Full arcs, actual triangles, complete rotations and all retained
port orders are in the certificate. This is the complete allocation for the
stated degree-four expansions, NOT for arbitrary degrees of x or y.

## 3. Twenty-eight strictly smaller all-exterior rules

The selected rule is particularly simple:

| Expanded controlled region | Condition | Smaller graph | Signed cases | Full selected lifts |
|---|---|---|---:|---:|
| I0 plus x | d(x)=4 and11->z | delete0 | 8 | 2872 |
| I0 plus y | d(y)=4 and z->8 | delete3 | 8 | 2956 |
| I0 plus both x,y | d(x)=d(y)=4 | delete0 | 12 | 3436 |

Thus28 cases have9264 complete Q-input lifts. The first two releases preserve
seven distinct ports when z is new (six retained vertices when aliased). The
last retains six when z is new (five when aliased). These counts concern fixed
retained sets, not an assertion that every retained vertex is on one rim cycle.

The Q operation is a literal induced vertex deletion; no arc is added, reversed
or contracted in these positive rules. There is therefore no external inverse-
arc guard. All positive rules decrease the whole graph order by exactly one.
Some local controlled vertices survive in Q and MAY change colour in the lift.
No unlisted adjacency of a recoloured vertex is allowed: all its actual face
corners are accounted for by its full degree.

Every row covers ALL binary assignments to Q, not just boundary projections.
The order is B followed by Q_internal, with the first vertex at the lowest bit.
A selected alphabet character gives the entire original interior word I; '-'
means no selected lift. The separate status string distinguishes invalid Q
inputs ('-'), complete contained lifts ('L'), no original colouring with that
boundary ('N'), and ordinary extensions that all add a positive relation ('R').
Every L entry has sigma_P=sigma_Q and R_P subseteq R_Q. Two distinct code
implementations validate actual arcs, complete induced acyclicity, the entire
relation, all original face corners, and every valid full Q word.

Quantified composition: let G contain a recorded saturated core P and let F
contain all other vertices/arcs, including all exterior chords. P and F meet
only in B; no unaccounted interior-to-exterior edge exists. For ANY valid whole
colouring of the strictly smaller G', select its Q entry, recolour only I,
and keep EVERY exterior vertex colour fixed. Any new monochromatic cycle
crossing the interface splits into positive P/F boundary paths. Replace each
P portion by its same-colour Q path from R_P subseteq R_Q. Together with the
unchanged F portions, these form a positive closed walk in the original valid
G' colouring, hence a directed cycle, contradiction. Cycles wholly in either
piece were excluded separately. The proof works for multiple complementary
regions and redundant retained ports, not just a simple disk boundary.

Induced deletion preserves finite/simple/planar/oriented, independently of
whether the smaller graph has any critical-degree bound. Minimum order in the
FULL contract supplies its colouring, so each listed signed core is excluded
from a minimum counterexample. No finite path-length cutoff is used.

Consequences for precisely D/19 in that minimum-counterexample setting:
1. x,y cannot both have degree4.
2. If x has degree4, then d(y)>=5, z is new or4 or5, and z->11. Thus
   x->z->11->x is a SECOND directed triangle. The direction on zy remains open.
3. If y has degree4, then d(x)>=5, z is new or5 or6, and8->z. Thus
   y->8->z->y is a SECOND directed triangle. The direction on zx remains open.
4. If both x,y have degree>=5, C38 makes no exclusion.
These are necessary alternatives with their exact hypotheses, not a uniform
minimum-degree-five theorem or exclusion of every D/19 occurrence.

## 4. A complete failure object and the first lost quantifier

Twelve allocated single-star rows still fail the selected bare-deletion
profile criterion. No impossibility of every other gadget is inferred.
For a stronger pressure test freeze the fresh-z, x-degree-four case with
z=14, z->11, y->z, x->z. Add the actual exterior chords
8->5,5->13,6->13,14->6. The resulting WHOLE twelve-vertex simple plane
triangulation has all semidegrees>=2. Its full30 arcs and rotation are in the
input; this is not an unspecified boundary projection.

Controlled I=(0,2,3,7,12); retained B=(4,5,6,8,11,13,14). The graph has202
full valid colourings attaining exactly66 of128 boundary words. All valid
colourings and all attainments are retained, so an unattained word is never
confused with a claim that every boundary word fails. For example full ones
{2,4,8,11,13} is valid. It is NOT a root counterexample.

Allocated alternatives: delete any one of the five controlled vertices, or
contract any controlled-controlled edge in the underlying plane graph, remove
loops and choose each possible inherited direction when opposite parallel
arcs arise. Exterior vertices/arcs stay unchanged. This gives exactly25
specified alternatives (five deletions and20 oriented quotient choices).
Every one of their51200 complete assignments is classified:
46132 invalid,4720 safe contained lifts,142 valid with no ordinary extension,
and206 valid with ordinary extensions but none containing the full relation.
Each alternative has its own failed quantified input and all32 original
interior assignments are certified by a cycle or an explicit extra pair.

All five induced deletions have actual nonextendable whole-graph colourings.
Their valid / ordinary-failure / extra-relation-only counts are
 delete0:232/8/2; delete2:252/8/2; delete3:254/2/2;
 delete7:288/8/38; delete12:196/6/28.
For example after delete3, ones={4,5,6,7,8,11,14} is valid but no assignment
to all five original controlled vertices restores the original graph with
its seven exterior colours fixed. Every one of32 restorations has a saved
monochromatic cycle. This is failure of the enlarged-control attempt, not a
rerun of the earlier three-point restoration claim.

Important distinction: only24 of25 alternatives have an ordinary nonextension.
The remaining quotient contracts3 with7 and uses3->2 and8->3 at the two
conflicting pairs. All168 valid quotient colourings DO have an ordinary full
extension. Ten nevertheless fail R containment. This quotient is a negative
for the requested universal profile contract, NOT for ordinary colourability.
For the allocated family the exact failed quantifier is
 for each Q, there exists a valid complete d on Q such that every valid
 P-colouring with boundary d|B either does not exist or has R_P not subset R_Q(d).
No conclusion about a Q outside the allocated family follows.

Minimality is restricted and explicit. A fresh-z x-release has twelve forced
distinct vertices, and this full graph uses exactly those twelve. For negative
old-z single-star cases there are eleven vertices. Their complementary regions
are a triangle and a quadrilateral; with no extra vertex, only two diagonals
and two directions are possible. All32 completions of the eight such negative
cases have a recorded semidegree shortage. Positive old-z cases already have
a universal deletion rule. This supplies the stated lower-order control within
the allocated degree-four port-release class, NOT among all D/19 instances or
all separators/gadgets (where different degree hypotheses are possible).

## 5. Full double-payment ledger, including a real nonzero donor

There is NO new payment rule. Always use ORIGINAL degrees and marks:
 gamma(v)=(d(v)-4-2t(v))/d(v),
 mu(f)=length(f)-4+sum_corners gamma+h(f).
Each marked residual low-low pair receives one unit on BOTH incident faces;
its donor's debit is2t+d*gamma=d-4, final0. Relative to the single-payment
rule every face changes by its extra actual unit receipts minus sum(t/d)
over ALL its corners. No t value from a hypothetical replacement is substituted.

All actual faces and corner coefficients are saved per expanded row. Starting
with C37's13 triangles, an x or y release adds2, a double release adds3.
For distinct z the complete affected totals are, writing g_v=gamma(v):
 x-release: -12+6g7+4gx+3g4+2g5+3g6+3g8+4g11+3gy+2gz+sum h;
 y-release: -12+6g7+4gy+3g4+2g5+3g6+4g8+3g11+3gx+2gz+sum h;
 both:      -13+6g7+4gx+4gy+3g4+2g5+3g6+4g8+4g11+3gz+sum h.
For a released degree-four port g=0, but its incident faces may receive h
from an actual marked low-low edge; h is NOT silently zeroed. For aliases
sum the repeated vertex coefficients and keep distinct face payments distinct.
Every individual face is still -1+its THREE actual g terms+its actual h.
These formulas cover45,45,48 face corners respectively, including all six
corners at7. The loss relative to single payment is obtained by replacing
EVERY coefficient*g_v by coefficient*t(v)/d(v) with a minus sign, together
with the actual new unit credits. It is not restricted to newly attached faces.

In the complete failure graph degree-four vertices are4,12,14, with only the
edge12--14 between them. It is precisely residual C32(3,43) after full reversal
and the bijection(0,1,2,3,4,5)->(11,7,13,6,12,14). Its donor is13. Therefore
ACTUAL t(13)=1, all other t=0; h=1 on faces(11,12,14),(12,13,14), zero elsewhere.
In particular g13=0 rather than1/3. The20 face charges are:
 -2/5 once; -4/15 six times; -3/5 five times; -7/15 four times;
 -2/3 twice; +1/5 once; 0 once. Sum=-8.
Fifteen controlled faces total-26/5; the other five total-14/5.
The additional payment on(12,13,14) is accompanied by six separate1/6 losses
at donor13's corners: three inside the controlled faces, three outside.
Every one of20 faces and12 vertices has its explicit debit/credit row.
This is a nonzero-t audit, not another donor-free example set to t=h=0.

After the new exclusions the central face(7,x,y) has h=0 because x,y cannot
both be degree4. Its exact residual charge is
  -(2+t7)/3 + gamma(x)+gamma(y), t7 in{0,1}.
If x is4 and y has degree d with t marks, this is always negative when t7=1;
when t7=0 it is negative exactly when d<12+6t, zero at equality. The mirrored
case is identical. When both ports are high the displayed gamma sum is the
remaining criterion. No C35 six-family geometric coverage gap has disappeared.
The whole sum remains-8; no global no-negative-face or root contradiction exists.

## 6. Replay, provenance, and next obligation

The replay capsule losslessly stores the complete raw certificate, source,
input, bounded wrapper and selected execution records. Use c38-unpack.py to
extract into its dedicated candidate-only replay directory, then run the
relative wrapper with check or audit. The generator uses positive bitset
closure; the separate consumer uses DFS/BFS and imports none of its predicates.
Both really ran on CPython3.13.5 under one CPU,512MiB,CPU35/hard36 seconds,
alarm40,parent43 seconds,1MiB files, and denied socket/socketpair/connect.
Both implementations belong to ONE generator trust domain. They do not sign
Evidence. Lean elaboration and axiom reports were not run. A matching trusted
statement-faithfulness and closure receipt is still required.

The selected scope is40 direction rows,28 successful rules,9264 complete
positive lifts, a25-alternative full-object audit, and32 smallest-completion
controls. Full output includes rejected and successful inputs; no failed type
is represented by only one sampled boundary word. All positive, ordinary-
negative and relation-negative claims keep distinct scopes.

Dependencies: frozen D19 arcs/actual rotations + semidegree conditions ->
complete degree-four aliases; all full-Q lift entries + saturated stars ->
arbitrary-exterior composition + strict induced deletion -> three conditional
reductions. Whole finite object -> scoped failed family. Full original marks
and corners -> conserved ledger. No arrow claims unavoidability from arithmetic.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_result: none
first_open_configuration: D19 with both x,y>=5; or exactly one degree4 port
 satisfying the new second-directed-triangle condition, e.g. x4,new z,z->11,
 y->z, with y>=5 and full external constraints. Twelve allocated single-star
 bare-deletion types remain, and no classification for higher-degree ports
 or all smaller gadgets is asserted.
next_obligation: obligation:opg169-root
next_action: enlarge the second directed triangle at z, or use a different
 replacement that resolves the ordinary-vs-relation gap; retain every outside
 arc and every double-payment debit. Do not retry the25 tested alternatives
 without an explicitly changed interface or premise.
root_closed: false
