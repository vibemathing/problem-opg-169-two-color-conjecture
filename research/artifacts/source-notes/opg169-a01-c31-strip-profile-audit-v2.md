# C31 supplementary audit: alternating-strip replacement for every exterior

Verdict: candidate_only. Status: proof-drafted.
Candidate audit identity: candidate:opg169-a01-c31-strip-profile-audit-v2.
Problem: problem:opg-169-two-color-conjecture.
Attempt: attempt:web-20260906-opg169-a01.
Route: route:minimal-counterexample-structure-v1.
Graph: graph:opg169-initial-v1.
Target: obligation:opg169-root.
Primary owner: math-proof.
This is a mathematical audit supplement to the existing C31 branch, not a new attempt packet, verifier receipt, or root result. It does not overwrite C30, C29 or PR #37. The branch's recorded starting main was bcffc6fe5ed24d412a3100ec75adb9178e770c9e; this sentence is not a fresh current-main claim.

## 1. Exact disk patch and all exterior quantifiers

For m>=2 define a patch P_m with distinct poles p,q and path vertices x_1,...,x_m. Its COMPLETE arcs are x_i->x_(i+1), for 1<=i<m; q->x_i->p for odd i; and p->x_i->q for even i. There is no pole edge and there are no other patch arcs. Fix the disk boundary B=(p,x_1,q,x_m), with this cyclic order up to simultaneous reversal. Draw the path between x_1,x_m, with the p fan on one side and the q fan on the other. All faces inside the boundary are triangles. Write x=x_1 and y=x_m.

A compatible exterior F has V(F) intersect V(P_m)=B, no edges from F's interior to the patch interior, and a disk embedding on the other side of this boundary. Shared boundary arcs must agree in direction and count once. Additional boundary-to-boundary arcs of the full graph, if any, are retained in F. Thus P_m need not contain every boundary chord of the full graph, but P_m union F contains EVERY original arc; none is omitted from a global induced colour class. All internal path vertices have exactly their two pole neighbours and their two path neighbours in the full graph.

For a valid colouring c of P_m, its state is (sigma,R): sigma is the two-colouring restricted to B, and R is ALL ordered boundary pairs connected by a positive monochromatic directed path in P_m. Paths through other boundary vertices are included. Either colour may be unused. The profile is the set of states of ALL valid colourings, not one selected colouring and not a recolouring component.

Claim: after identifying the four boundary labels,
- all even m>=4 have exactly the same profile, containing 16 states;
- all odd m>=5 have exactly the same profile, containing 18 states.
Consequently, for EVERY compatible exterior and EVERY valid colouring of P_4 union F (even case), or P_5 union F (odd case), there is a valid colouring of P_m union F that agrees on ALL vertices of F.

## 2. Unequal pole colours: all states, not only blocked ones

First let c(p)=0 and c(q)=1 and put t_i=c(x_i) XOR (i mod 2). A monochromatic cycle avoiding both poles is impossible in the directed path. A colour-0 cycle uses only p among the poles, so it has an even-to-later-odd all-zero path segment. Such a segment contains an adjacent even-to-odd 00 pair, which conversely closes a directed triangle through p. A colour-1 cycle analogously corresponds to an adjacent odd-to-even 11 pair through q. For either edge parity, the forbidden pattern is precisely (t_i,t_(i+1))=(0,1).

Thus validity is equivalent to t_1>=...>=t_m. Every valid colouring has t=1^k 0^(m-k), 0<=k<=m. The two constant transformed words and the nonconstant words give exactly three states. Nonconstant words all have the SAME complete state, not just the same blocking entries.

For even m the three states, with boundary order (p,x,q,y), are:
1. k=0: sigma=(0,1,1,0), R={(q,x),(p,y)}.
2. k=m: sigma=(0,0,1,1), R={(x,p),(y,q)}.
3. 0<k<m: sigma=(0,0,1,0), R={(x,p),(p,y),(x,y)}.

For odd m>=3 they are:
1. k=0: sigma=(0,1,1,1), R={(q,x),(q,y)}.
2. k=m: sigma=(0,0,1,0), R={(x,p),(y,p)}.
3. 0<k<m: sigma=(0,0,1,1), R={(x,p),(q,y)}.

To see the lists are complete, away from the one threshold edge all successive path vertices have different colours. At the threshold the single same-colour path arc points in the direction already represented through that colour's pole. Prefix odd vertices point to p, suffix even vertices receive arcs from p; prefix even vertices point to q, suffix odd vertices receive arcs from q. There is no monochromatic return from a later layer. This proves all displayed positive pairs and excludes the others. Global colour complementation supplies the three states with c(p)=1,c(q)=0, without reversing any arc. There are therefore six unequal-pole states for each relevant parity.

## 3. Equal pole colours: the additional states needed for a valid replacement

Let c(p)=c(q)=s and S={i:c(x_i)=s}. If S contains an even e and an odd o, then p->x_e->q->x_o->p is a monochromatic directed 4-cycle, irrespective of the order of e,o along the path. Hence S must be empty or contained entirely in one parity. Conversely, this condition suffices: when S is even-only the pole-colour part has layers p->selected even vertices->q; when S is odd-only it has layers q->selected odd vertices->p. The other colour is an induced subgraph of the directed path. Both are acyclic.

If S is empty, x and y have colour 1-s and the complete boundary relation is {(x,y)}, because the entire path has that colour. The poles have no monochromatic connection.

If S is nonempty and even-only, the pole-colour boundary relation is the transitive closure of p->q and p->z->q for each selected endpoint z in {x,y}. If S is nonempty and odd-only, replace that description by q->p and q->z->p. No relation between opposite-colour endpoints survives when S is nonempty and both endpoints are unselected: every path from x to y is interrupted by a selected internal vertex, and both poles have the wrong colour for such a path. There are no other same-colour boundary vertices to consider. This characterizes the COMPLETE relation.

For even m>=4, x is odd and y is even. A nonempty even-only S gives two endpoint patterns, according as y is selected or not; if not, an internal even vertex exists. A nonempty odd-only S similarly gives two patterns according as x is selected or not; an internal odd vertex exists when x is not selected. Together with S empty, this is five states for each fixed s. Combining both s values with the six unequal-pole states gives 2*5+6=16 states.

For odd m>=5 both endpoints are odd. A nonempty even-only S gives one endpoint pattern and is realized at an internal even vertex. A nonempty odd-only S gives all four choices of selected endpoints; when neither is selected an internal odd vertex exists. Together with the empty S case this is six states for each s, giving 2*6+6=18 states.

The availability thresholds matter. P_2 has no internal even or odd vertex and does not have the even stabilized profile. P_3 has no internal odd vertex and does not have the odd stabilized profile. For example the equal-pole colouring with both endpoints opposite to the poles and relation q->p requires a selected internal odd vertex, absent in P_3 but present in P_5. This is minimality only of these target lengths WITHIN this parity-preserving patch family, not among all possible planar replacement gadgets.

## 4. Constructive state lifting and positive-relation composition

For unequal poles, the endpoint colours identify which of the three states is required. Use the corresponding constant transformed word, or any nonconstant threshold word (for example k=1), in the longer patch. This preserves the boundary colours and exact R.

For equal poles, the state identifies whether S is empty, even-only or odd-only, and which endpoints are selected. Preserve the selected endpoints. If a nonempty S is required but neither endpoint is selected, choose one internal vertex of the required parity; the size thresholds guarantee it exists. Put all other path vertices in the opposite colour. The classification proves that this constructs exactly the requested state. These recipes work for every state of the shorter patch and are independent of the exterior colouring.

For coloured patches P,F with compatible sigma, a monochromatic directed cycle in their union either lies in one patch or cuts at boundary visits into a positive cyclic chain in R_P union R_F. Conversely any positive cyclic chain expands into a positive monochromatic closed walk and hence contains a directed cycle. Therefore their union colouring is valid exactly when (R_P union R_F)^+ has no diagonal entry.

Now fix ANY valid colouring of P_4 union F or P_5 union F. Its patch restriction has a state in the appropriate stabilized profile. The constructive recipe supplies a colouring of P_m with that identical state, leaving every exterior vertex unchanged. Since the positive relation union is identical, the new full colouring is valid. This proves the all-exterior lift, not merely existence of one favourable boundary assignment. No legal sequence of single-vertex recolourings is required or claimed.

## 5. A genuine smaller graph reduction

Suppose a full graph in the root contract contains the clean disk patch P_m with the stipulated lack of extra internal/exterior adjacencies. For even m>=6 replace it by P_4; for odd m>=7 replace it by P_5. Keep p,q,x,y and all exterior vertices/arcs fixed, and use fresh internal labels for the shorter path.

The same parity of m and the target length preserves the directions of all four boundary edges. The replacement introduces no pole edge and no direct x-y edge. Every new edge has a fresh internal endpoint, except the unchanged boundary edges; no new loop, repeated edge or opposite arc is introduced. Any consistently shared boundary edge is retained once, and every exterior boundary chord is left unchanged. The two-fan construction embeds in the same quadrilateral disk with the same boundary cyclic order. Hence the new graph is finite, simple, planar and oriented. Its order decreases by m-4 or m-5, at least two.

In a hypothetical vertex-number-minimum root counterexample, the smaller graph is colourable by minimality in the FULL contract class. Section 4 lifts that colouring to the original graph, a contradiction. Therefore such a minimum counterexample contains no clean patch of this particular alternating orientation with m>=6 even or m>=7 odd. In this configuration family at most five path vertices remain.

The reduced graph need not retain the semidegree bounds or strong-deletion property: those are necessary consequences of being a minimum counterexample, not restrictions on graphs to which its global minimality can be applied. No unrestricted directed contraction is used.

## 6. Scope, provenance and remaining root obligations

This is a configuration-specific reduction with all-colourings lifting. It does not show that Euler's degree-four/degree-five count forces this alternating two-fan patch. Degree-four vertices with strongly connected deletions and other rotations/path orientations remain open; general degree-five (2,3)/(3,2) configurations also remain open.

C30's exact dynamic model may have arbitrarily many classes as the interior grows. That does not prevent this STATIC profile equality from supporting a graph replacement: existential colouring lifting and representative-wise recolouring are distinct requirements. C31's explicit colourable width families are not asserted to be minimum counterexamples; the clean-strip reduction can exclude long members from an actual minimum counterexample without contradicting their existence.

The present audit is a direct all-orders proof draft. No current execution output, tool version, checksum, PR number, merge SHA or verifier receipt is inferred from a previous progress message. Exact-byte hashing, the existing branch's finite-control files, the sole packet and final-head required checks must be read back before transport completion is reported. There is no new Lean elaboration or axiom report.

Local claim chain: exact mono-cycle classification -> complete parity-stable profile -> constructive state lifting -> positive-path composition -> class-preserving strict-size replacement -> exclusion in a minimum counterexample. No implication uses finite sample agreement as induction.

checkpoint_state: NONTERMINAL_CHECKPOINT
verdict: candidate_only
best_verified_candidate: none
root_closed: false
first_open_configuration: degree-four (2,2) with strongly connected deletion not forced to contain the clean alternating strip; general degree-five (2,3)/(3,2)
next_obligation: obligation:opg169-root
next_action: audit and transport the existing C31 family/strip files with one packet, then prove applicability or unavoidability of additional all-exterior-liftable reductions. Preserve the separate T3, T4, dynamic-interface and root statement scopes.
