# R08 S09 Cycle 9 — conditional COMPACT-NONJ-CLOSE from C35 six-hole profiles

`verdict=candidate_only`; `best_verified_result=none`; `root_closed=false`.

Fresh protected main: `88af1f947ecbdbac4562d57e4b4f195250319eb4`.

This checkpoint is a **row-level conditional closure theorem**.  S01 Cycle 10 now extracts a content-derived `RawSourceRow` from every FECT exposure and proves `RawSourceRow -> SameMinCEJREL`; this theorem begins only after that exact same-MinCE raw row exists.  It does not
turn the C35 controls into FECT occurrence or totality.

## 1. Compact source key

For an exact compact row `r`, retain the ordered six-boundary
`B=(b0,...,b5)`, the actual source patch `P`, its nonempty source interior `I`,
all actual boundary/exterior contacts, aliases, payer/source identities, and a
complete ownership partition.

The closure-relevant invariant is:

1. `B` with its cyclic order and actual rim directions;
2. the **exact P extension set** `Ext_P(beta)` for each of the 64 complete
   boundary colourings `beta`: every exact pair `(R_P,0^+,R_P,1^+)` realized
   by a valid complete P colouring extending `beta`;
3. the forbidden non-rim boundary pairs already occupied in either actual
   direction, with their directions and owners;
4. complete stars for every vertex in `I`, so there is no hidden
   `I`-to-exterior contact;
5. explicit source/exterior/shared-boundary ownership; and
6. the unchanged payer ledger.

No equality with a C35 profile hash is part of the theorem.

## 2. Weakest C35-library acceptance predicate

Let `L20` be the 20 canonical minimum zero-internal C35 chord systems from
Cycle 8, closed under the 12 dihedral relabellings of a six-cycle.  The 20
labels collapse to 19 distinct directed systems and their dihedral closure has
85 distinct systems.

For `T in L20`, write `Q_T` for the actual rim of `r` plus the directed chords
of `T`.  Define `SAFE_r(T)` by:

- every T chord is a noncrossing chord in the replacement disk;
- for every required directed chord `u->v`, either the underlying pair is
  absent and the chord may be inserted, or the actual same-direction edge
  `u->v` is already present and the ownership record explicitly permits it to
  be retained/reused as a boundary/shared arc;
- an actual reverse edge `v->u` is forbidden, as is any same-direction edge
  whose ownership/contact status prevents consistent reuse;
- ownership of every retained/shared boundary arc is direction-consistent;
- all contacts of the deleted interior are already in P.

Define `PROFILE_r(T)` by:

- `Q_T` has at least one valid complete colouring; and
- for every valid complete boundary colouring `beta` of `Q_T`, there is some
  `(rho0,rho1) in Ext_P(beta)` with
  `rho0 subseteq R^+_Q_T,0(beta)` and
  `rho1 subseteq R^+_Q_T,1(beta)`.

Then

```text
COMPACT20(r) := exists T in L20, SAFE_r(T) and PROFILE_r(T).
```

This is weaker than matching an entire C35 control signature.  Relative to the
fixed C35 chord library and the listed source-key fields, it is the direct
acceptance condition actually needed by the lifting theorem.

## 3. Conditional COMPACT-NONJ-CLOSE theorem

Assume `RawSourceRow_G(f,a,j)`, `SameMinCEJREL_G(f,a,j)`, `RowTag(j)=COMPACT_NONJ`, and `COMPACT20(j)`.
Choose a witnessing T.  Delete all vertices of I and insert the T chords.
Because I is nonempty the order drops strictly.  `SAFE_r(T)` gives a simple
plane orientation: required absent chords are inserted, compatible same-direction
boundary chords are reused, and every reverse/ownership conflict is forbidden; complete stars and
ownership ensure that the exterior meets the changed patch only through the
declared boundary interface.

`PROFILE_r(T)` is exactly the complete-Q, same-boundary, two-colour positive
reachability hypothesis of the generic ordinary arbitrary-exterior lifting
lemma.  Hence every valid colouring of the smaller graph lifts while the whole
exterior stays fixed.  Therefore this exact row is `ClosureEligible` by a
strict ordinary L_A replacement.

This implication is conditional on the already extracted same-MinCE raw row and `COMPACT20`; it is not an occurrence theorem.

## 4. Maximal-completion monotonicity, including nonvacuity

Let Q be any source-safe plane replacement satisfying the profile predicate and
having a valid complete colouring `chi`.  Triangulate its nontriangular disk
faces by adding only source-safe edges and no vertices.

For each colour c, the c-induced subgraph of Q under chi is a DAG.  Fix a
topological order of it.  Orient every newly added edge whose endpoints both
have colour c forward in that order; orient bichromatic added edges arbitrarily.
Then neither monochromatic class gains a directed cycle, so chi remains valid.
Thus the completion Q' is nonvacuous.

Every Q' colouring is also a Q colouring, and adding edges can only enlarge
positive monochromatic reachability:
`R_Q,c^+ subseteq R_Q',c^+`.  The P lift already supplied for that Q colouring
therefore still satisfies `R_P,c^+ subseteq R_Q',c^+` for c=0,1.  Hence the
profile property is monotone under **source-safe** maximal completion.

The adjective source-safe is essential.  A completion edge may be newly
inserted only when its underlying pair is absent; an already present
same-direction boundary edge may instead be reused when ownership is compatible.
A reverse actual edge, or a same-direction edge with incompatible ownership,
blocks that completion edge.

## 5. What the twenty controls cover

Fresh reconstruction from the raw C35 arcs/rotation gives 20 actual negative
six-hole controls.  Their exact P extension profiles are all distinct even
after quotienting by D6 boundary symmetry and global colour swap.

All 20 C35 controls have empty actual non-rim boundary-chord forbidden sets.
Consequently they realize 20 concrete full invariant signatures, not a proof
that arbitrary FECT `COMPACT_NONJ` rows have one of those signatures.

The full local machine payload records all 20 exact extension sets and their
hashes.  The repository signature artifact stores the hashes and compact row
data; the Cycle-9 checker reconstructs the exact extension sets directly from
the repository-bound C35 raw arcs/rotation before checking them.

## 6. Minimal exterior-direction counterrow

Use the exact C35 source patch for physical face `(0,3,4)`.  Its six-boundary is

```text
B = (2,7,8,9,5,6).
```

Among **all 215** zero-internal directed noncrossing chord states on this B,
exactly one satisfies the local complete-Q/full-R+ profile for this P:

```text
local chords: 0->2, 3->0, 0->4
actual arcs:  2->8, 9->2, 2->5.
```

Now leave P, its rotations, exact extension set, complete deleted stars and
empty payer ledger unchanged, but put the single exterior-owned arc

```text
8->2
```

on the exterior side of B.  This is the reverse of the required `2->8`.
It is planar as a single outer-disk chord.

The unique locally profile-valid C35 zero-internal state now fails its reverse
guard.  Every other one of the 215 states already fails the P/Q profile before
the exterior is considered.  Hence every C35 zero-internal chord template is
invalidated for this compact interface.

The blocker number is minimal for this fixed P profile: with no exterior
blocker the unique state is source-safe; one reverse chord suffices.

This is a compact plane source-interface countermodel, **not** a claimed FECT
or minimum-counterexample occurrence.

## 7. S01 insertion point

S01 Cycle 10 may consume exactly:

```text
RawSourceRow_G(f,a,j)
and SameMinCEJREL_G(f,a,j)
and RowTag(j)=COMPACT_NONJ
and COMPACT20(j)
    -> ClosureEligible_G(j) by L_A.                 [candidate]
```

`RawSourceRow` is the occurrence identity produced by Cycle 10 from the actual FECT record; no named C35 catalogue membership is required. What remains open is whether every actual raw COMPACT_NONJ row satisfies `COMPACT20`, or needs additional compact templates/classes.

No C35/MinCE inversion, no FECT totality, no B46 IDs, no registry inversion,
and no root closure are claimed.
