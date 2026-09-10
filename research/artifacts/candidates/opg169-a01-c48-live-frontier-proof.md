# C48: live-frontier integration and the low-slack source-state cut

Verdict: `candidate_only`.  Status: proof-drafted with bounded exact controls.

Repository: `vibemathing/problem-opg-169-two-color-conjecture`  
Problem: `problem:opg-169-two-color-conjecture`  
Attempt: `attempt:web-20260906-opg169-a01`  
Route: `route:minimal-counterexample-structure-v1`  
Graph: `graph:opg169-initial-v1`  
Target: `obligation:opg169-root`  
Base revision: `8d5bcb4955e84468f58a5923bed7f2ec527a6218`

No EvidenceLink, Result, Solution, trusted verification, or root closure is claimed.

## 1. Scope freeze and source precedence

All graphs are orientations of finite simple planar graphs.  A valid binary
colouring makes both full induced colour classes acyclic.  Directed cycles and
the boundary relation \(R^+\) have positive length.  Empty colour classes are
allowed.

This candidate performs two logically separate operations.

1. It applies an explicit parent-precedence lemma to the newly merged exact
   C37 \(d(7)=6\) 160-parent profile catalogue.  This changes the *candidate
   live frontier* but does not turn any candidate into admitted evidence.
2. It derives a new source-state cut from the C34/C35 double-payment ledger:
   every unpaid negative triangle has either a corner in one of 26 finite
   low-\(t\) integer cells, or a high-\(t\) corner with a singleton separator
   between two marked pair blocks.  The singleton branch has an exact
   three-interface plane geometry before directions are treated.

The source manifest distinguishes repository-bound artifacts from mission text
for which no repository locator was found.  An unbound specialist statement
does not close a node.

## 2. Parent precedence for all-exterior profile reductions

### Lemma 2.1 — source-parent dominance

Let \(\mathcal S\) be a family of exact embedded parent patches.  Suppose that
for every \(P\in\mathcal S\) there is a replacement \(Q_P\) such that:

1. \(Q_P\) is a finite simple planar orientation with strictly fewer vertices
   than \(P\), embedded in the same controlled region;
2. every controlled star declared complete in \(P\) is complete in the source
   graph, and every other arc is retained in the exterior;
3. for every valid complete colouring \(d\) of \(Q_P\), there is a valid
   complete colouring \(c\) of \(P\) with the same boundary colours and
   \(R_P^+(c)\subseteq R_{Q_P}^+(d)\).

Then no vertex-minimum counterexample contains a member of \(\mathcal S\).
Moreover, any child configuration obtained only by fixing additional exterior
vertices, arcs, aliases, directions, or guard outcomes while retaining the
same exact parent patch is logically dominated by its parent rule.

**Proof.**  Apply minimum order to the whole graph with \(P\) replaced by
\(Q_P\).  Fix any valid colouring of that smaller graph and choose the
certified local lift.  If the lifted colouring created a monochromatic cycle
crossing the interface, cut it at successive boundary visits.  Replace each
positive \(P\)-segment by the same-colour \(Q_P\)-path guaranteed by relation
containment.  Together with the unchanged exterior segments this gives a
positive monochromatic closed walk in the smaller graph, hence a directed
cycle, a contradiction.  A child only restricts the arbitrary exterior
already quantified in the parent statement, so the same rule applies. \(\square\)

The last sentence requires exact source identity.  It does not apply if a
child changes a complete star, the parent rotation, the interface, or the
orientation of a parent arc.

### Application to the current source chain

The merged S06 Cycle-5 candidate states that the exact C37 \(d(7)=6\) domain
contains five labelled embedding families and 32 directions per family, hence
160 parents, and supplies a selected unconditional parent-preserving rule for
each: 156 merged-\(\{0,2\}\) rules and four prior bare delete-3 rules.  Its
packet states that all 21,732 valid complete smaller colourings lift, with
16,536 equal and 5,196 strict relation decreases.

Subject to statement-faithfulness and independent verification still absent,
Lemma 2.1 therefore removes the following from the *active candidate frontier*:

- C38 and C39 refinements of the exact C37 \(d(7)=6\) source;
- C40's 10/24/22/14 local catalogue and its guard-failure descendants in that
  same source domain;
- the C43--C47 D/19/guard-face/two-hole descendants;
- S08's parent-10--14 D/19 descendants.

These artifacts remain useful historical pressure tests.  They are not
declared false, deleted, or mathematically admitted.  The dominance statement
does not cover \(d(7)\ge7\), another J orientation, a source state not in the
five exact C37 families, or the global negative-face join.

## 3. The first genuine root cut from an unpaid negative face

Retain the C34/C35 candidate framework.  For a marked-pair donor \(p\), let

\[
d=d(p),\qquad t=t(p),\qquad
\gamma(d,t)=\frac{d-4-2t}{d}.
\]

C34 proves, in its exact marked-pair convention, that every pair occupies two
consecutive degree-four neighbour positions and distinct pairs are separated
by at least one unmarked high endpoint.  It obtains

\[
3t\le d.
\]

The double-payment budget also gives \(2t\le d-4\).  C35 writes

\[
s=d-3t\ge0
\]
and hence
\[
d=3t+s,\qquad t+s\ge4,\qquad
\gamma=\frac{t+s-4}{3t+s}
       =\frac13+\frac{2(s-6)}{3d}.
\]

For an unpaid triangular face \(f=xyz\), \(h(f)=0\), so
\[
\mu(f)=-1+\gamma_x+\gamma_y+\gamma_z.
\]

### Theorem 3.1 — low-slack dichotomy

If \(\mu(f)<0\), then some corner \(p\in V(f)\) has \(s(p)\le5\).  For such a
corner exactly one of the following mutually exclusive alternatives holds.

**Finite branch.** \(0\le t(p)\le5\), and \((s,t,d)\) is one of the following
26 cells:

| \(s\) | allowed \(t\le5\) | corresponding \(d=3t+s\) |
|---:|---|---|
| 0 | 4,5 | 12,15 |
| 1 | 3,4,5 | 10,13,16 |
| 2 | 2,3,4,5 | 8,11,14,17 |
| 3 | 1,2,3,4,5 | 6,9,12,15,18 |
| 4 | 0,1,2,3,4,5 | 4,7,10,13,16,19 |
| 5 | 0,1,2,3,4,5 | 5,8,11,14,17,20 |

**Singleton-gap branch.** \(t(p)\ge6\), and in the cyclic order at \(p\) two
consecutive marked pair blocks are separated by exactly one unmarked high
neighbour.  More precisely, if \(g_1,\ldots,g_t\ge1\) are the numbers of
unmarked positions in the cyclic gaps after the \(t\) two-position blocks,
then
\[
\sum_i g_i=d-2t=t+s,\qquad
\sum_i(g_i-1)=s,
\]
so the number of singleton gaps \(g_i=1\) is at least
\[
t-s\ge1.
\]

**Proof.**  If every face corner had \(s\ge6\), the displayed formula would
give \(\gamma\ge1/3\) at each corner, hence \(\mu(f)\ge0\), contradiction.
Choose a corner with \(s\le5\).  The integer domain \(t+s\ge4\) gives
\(t\ge\max(0,4-s)\).  Intersecting this with \(t\le5\) yields exactly the
listed 26 cells.  If \(t\ge6\), the separated pair blocks define the positive
cyclic gaps.  At most \(s\) gaps can have size at least two because each such
gap consumes at least one unit of \(\sum(g_i-1)=s\).  Thus at least \(t-s\)
gaps are singleton. \(\square\)

This is an exact source-state cut.  It is not yet a negative-face-to-reducible-
parent join theorem.  In particular it neither says that the 26 cells are all
reducible nor that a singleton gap automatically has an octahedral-shell or
AE/M12 cap profile.

### Sharpness pressure tests

The lower bound cannot be strengthened uniformly to two singleton gaps:
at \(t=6,s=5\), the cyclic gap sequence
\[
(1,2,2,2,2,2)
\]
has exactly one singleton gap.  The finite branch cannot be shortened by
discarding \(t=0\): cells \((s,t,d)=(4,0,4)\) and \((5,0,5)\) are allowed by
the arithmetic domain.  Conversely, arithmetic admissibility alone does not
establish planar realizability or minimum-counterexample occurrence.

## 4. Exact plane source state of one singleton gap

Choose two marked pair blocks consecutive around a donor \(p\), separated by
one high endpoint \(H\).  In the rotation at \(p\), write

\[
H_0,u_0,v_0,H,u_1,v_1,H_2.
\]

The four low vertices have degree four.  Let \(q_i\) be the other facial third
vertex of the edge \(u_iv_i\).  The actual faces of sector \(i\) are

\[
(p,u_i,H_i),\ (p,v_i,u_i),\ (p,H_{i+1},v_i),
\]
\[
(H_i,u_i,q_i),\ (q_i,v_i,H_{i+1}),\ (q_i,u_i,v_i).
\]

With no aliases the two sectors form a ten-vertex, 21-edge triangulated disk
whose outer boundary is
\[
(p,H_0,q_0,H,q_1,H_2).
\]
Every low star is saturated at degree four.

### Lemma 4.1 — complete local alias trichotomy

Up to exchanging the two sectors, exactly three local interface types survive:

1. \(q_0,q_1,H_0,H,H_2,p\) are all distinct;
2. \(q_0=H_2\), while \(q_1\) is distinct from the other local vertices;
3. \(q_1=H_0\), while \(q_0\) is distinct from the other local vertices.

In the two alias cases the complement consists of two triangular boundary
regions sharing the identified port; neither region may be assumed empty.

**Proof.**  A facial third vertex is distinct from the three vertices of its
incident face.  It cannot be a low vertex of the other block: that degree-four
vertex already has three distinct neighbours \(p\), its mate and an endpoint,
and becoming adjacent to both vertices of the first block would give at least
five neighbours.  Thus the only local high-endpoint aliases are
\(q_0=H_2\) and \(q_1=H_0\).

If \(q_0=q_1=q\), four actual wedges close the neighbour cycle
\[
p,v_0,q,u_1,p
\]
at \(H\), forcing \(d(H)=4\), contrary to the inherited endpoint bound
\(d(H)\ge5\).  If both opposite-endpoint aliases occur, the quotient has
eight vertices and 20 distinct edges, exceeding the simple planar bound
\(3\cdot8-6=18\).  Either single alias alone has nine vertices and 21 edges,
meeting the maximal planar bound and is therefore not excluded by counting.
\(\square\)

The frozen C32/C34 residual-sector catalogue has eight complete direction
types at a fixed donor sign.  Consequently this exact source state has
\(3\cdot8^2=192\) normalized direction parents before full arc reversal.
This multiplication imports the upstream eight-sector catalogue; the new
checker independently audits only the geometry and alias count.

This 192-parent singleton-gap atlas is the earliest finite geometric target
on the high-\(t\) branch.  No replacement table for it is asserted here.

## 5. Mutually exclusive candidate proof DAG

```text
root: every finite simple planar orientation is two-colourable
|
+-- N: select a minimum-order, maximum-edge counterexample
|     +-- maximal planar / 3-connected candidate normal form
|     `-- separating triangles remain open
|
+-- D: double-payment charge ledger
|     +-- all vertices finish at zero
|     +-- length >= 4 faces are nonnegative
|     `-- some unpaid triangle has sum(gamma) < 1
|
+-- J48: Theorem 3.1 at a low-slack corner of that triangle
      |
      +-- F: one of 26 finite (s,t,d) cells, t <= 5
      |     `-- OPEN: exact rotation/direction/alias -> parent generation
      |
      `-- S: t >= 6 and at least one singleton pair gap
            +-- Lemma 4.1: three local interfaces, 192 normalized directions
            +-- OPEN: complete source-faithful profile reductions
            `-- unbound S14 AE/M12 shell/cap statement may refine this
                branch only after a repository locator and hypotheses match
```

A separately scoped exact parent leaf is now candidate-covered:

```text
exact C37 d(7)=6 source (5 families x 32 = 160)
  -> merged S06 parent-preserving rule menu (160/160)
  -> C38/C39/C40/C43--C47 and S08 D/19 descendants
     are provisionally dominated in the active candidate frontier
```

That leaf does not close either branch F or S unless the missing generation
theorem maps the selected negative face to the exact C37 source.

## 6. Imported specialist statements and status discipline

The import manifest records SHA-256 values for repository-bound candidates.
For specialist statements supplied only in the launch text, it records the
SHA-256 of a normalized statement and status `mission_supplied_unbound`.
Those statements are not treated as independent verification.

- S02 C7 and S09 C5 corroborate the exact C37 160/160 claim, but the merged S06
  artifact is the sole repository-bound representative used in the DAG.
- S12 C6 is a bounded \(n\le12\), 4-connected bad-pivot reduction claim.  It
  cannot imply a root lower bound and remains inactive without its exact
  graph/profile schema.
- S14 C8 is a high-degree shell/cap normalization claim.  The new singleton-gap
  atlas identifies a possible attachment point, but the statement cannot close
  it without a source locator, exact hypotheses, and a profile-lifting proof.
- S05 C5's wrong-region quarantine agrees with the C43--C47 correction chain.
  No old one-vertex-pinch or wrong two-lobe catalogue is restored.

## 7. Bounded exact execution

`opg169-a01-c48-low-slack-check.py` was run with CPython 3.13.5.  It:

- enumerates the 26 finite cells;
- checks 18,556 positive cyclic gap compositions for \(1\le t\le12\),
  \(0\le s\le5\), including sharp singleton counts;
- checks 682,640 bounded unordered corner triples, of which 336,161 are
  negative, and confirms each has a corner with \(s\le5\);
- reconstructs the ten-vertex/twenty-one-edge two-sector disk and checks the
  critical alias quotients.

The run exited zero.  It is a same-principal bounded pressure test.  The
universal statements are the proofs in Sections 3--4, not an extrapolation
from the finite range.

## 8. Remaining root obligations

Priority order:

1. **L_join / parent generation.**  For each actual unpaid negative face,
   generate an exact source-valid parent from branch F or S, with rotations,
   aliases, directions, complete stars and payer identity.  Arithmetic coverage
   alone is insufficient.
2. **Finite branch F.**  Refine the 26 cells by actual incidence and direction,
   then map every realizable state to a strong-profile reduction or a smaller
   structural leaf.
3. **Singleton branch S.**  Freeze the 192 direction parents and search
   source-faithful replacements.  Validate the mission-supplied AE/M12
   octahedral-shell claim before using it.
4. **Separating triangles.**  The 3-connected maximal-planar normal form does
   not eliminate separating 3-cycles; composition across them remains open.
5. **Verification.**  Obtain independent replay, statement-faithfulness and
   the required trusted closure receipts.

`best_verified_result=none`; `root_closed=false`.
