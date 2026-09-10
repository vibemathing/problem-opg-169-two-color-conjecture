# R08 S02-B Cycle 3 — attack TERMINAL-USEFULNESS, not well-foundedness

**Verdict:** `candidate_only`  
**Root:** `root_closed=false`  
**Fresh protected main at final source read:** `6b34ce7f7ce83b238bebd85babd7aaff6f40a3d0`  
**Cycle-2 S02-B merge:** `3bec7e8d2c4fec368707f3f86cccfc7af8120472`  
**Latest S01 integration consumed:** `a2a9973d2f995de71095a6bea814cbe882cb7718`

## 1. Cycle-3 decision

Cycle 2 left a history-aware exposure rank alive:

```text
unseen original vertices
incomplete exposed complete stars
unprocessed rooted separator sides.
```

Cycle 3 does not attack its well-foundedness. It attacks the missing implication

```text
rank decreases  ==>  a useful local terminal appears early.
```

That implication is false in a strong bounded-locality sense.

There is an explicit arbitrarily large high-port root-class family `T_N`,
for every even `N>=6`, with all of the following properties:

1. `T_N` is a simple plane triangulation.
2. Every vertex has indegree and outdegree at least `2`.
3. The two poles have degree `N`.
4. Every 3-cycle is facial, so there is no separating triangle anywhere.
5. A monotone complete-star sweep around one ring exposes all but one vertex
   after `N-1` steps.
6. The controlled interface of the first `t` consecutive exposed stars has
   exact size

   ```text
   |B_t| = t+4,  1 <= t <= N-2,
   ```

   so the interface genuinely grows and fixed-boundary profile recurrence does
   not apply.
7. Every consecutive block of `1`, `2`, or `3` exposed stars has **no strict
   same-boundary ordinary extension replacement at all**.
   Therefore it also has no strong-profile replacement.

Thus a history-aware rank may decrease for an arbitrarily long source-discovery
schedule while all separator exits and every local reduction using at most three
consecutive exposed stars remain unavailable.

This is not a full falsifier of `TERMINAL-USEFULNESS`: a block of size `>=4`,
a nonlocal reduction, or source-specific GSRC/JMAP information may still become
useful. The exact consequence is a lower bound:

```text
any universal bounded-cluster usefulness theorem in this root-class model
must use radius/block-size at least 4.
```

The next live adversarial question is whether this lower bound can be pumped to
arbitrary `r`.

## 2. The double-ring family T_N

For even `N>=6`, use vertices

```text
U, D,
A_0,...,A_{N-1},
B_0,...,B_{N-1},
```

with subscripts modulo `N`.

Underlying edges are

```text
A_i A_{i+1},
B_i B_{i+1},
U A_i,
D B_i,
A_i B_i,
A_i B_{i-1}.
```

Hence

```text
|V(T_N)| = 2N+2,
|E(T_N)| = 6N = 3|V|-6,
|F(T_N)| = 4N.
```

A rotation system is

```text
rot(U)   = (A_0,A_1,...,A_{N-1}),
rot(D)   = (B_{N-1},...,B_1,B_0),

rot(A_i) = (U,A_{i-1},B_{i-1},B_i,A_{i+1}),
rot(B_i) = (D,B_{i+1},A_{i+1},A_i,B_{i-1}).
```

All traced faces are triangles.

The orientation used in the adversarial family is period two.

### Ring and pole arcs

For the `A` ring,

```text
i even: A_{i+1} -> A_i,
i odd : A_i -> A_{i+1}.
```

Thus even `A_i` receive both ring arcs and odd `A_i` send both ring arcs.

For the `B` ring,

```text
B_{i+1} -> B_i
```

for every `i`.

Pole spokes alternate:

```text
i even: A_i -> U,
i odd : U -> A_i,

i even: B_i -> D,
i odd : D -> B_i.
```

Cross arcs are

```text
A_i -> B_i,
B_{i-1} -> A_i.
```

Therefore the semidegrees are exactly

```text
A_i even: indegree 3, outdegree 2,
A_i odd : indegree 2, outdegree 3,

B_i even: indegree 2, outdegree 3,
B_i odd : indegree 3, outdegree 2,

U,D: indegree N/2, outdegree N/2.
```

So the minimum semidegree is `2`, and `d(U)=d(D)=N` is unbounded.

## 3. No separator exit

The only 3-cycles in the underlying triangulation are

```text
U A_i A_{i+1},
A_i A_{i+1} B_i,
A_i B_{i-1} B_i,
D B_i B_{i+1}.
```

They are exactly the `4N` facial triangles.

So `T_N` has no nonfacial 3-cycle and hence no separating triangle.
The Cycle-2 "rooted separator side" coordinate has nothing to process in this
family.

The executable control checked this directly for every even

```text
6 <= N <= 64.
```

At `N=64`:

```text
|V|=130,
|E|=384,
|F|=256,
d(U)=d(D)=64,
minimum semidegree=2,
nonfacial 3-cycles=0.
```

The formulas above are parametric; the finite sweep is a canary, not the proof
of the formulas.

## 4. A monotone history rank can run almost to full exposure

Expose the complete stars

```text
A_0, A_1, ..., A_{N-2}
```

in order.

For `1<=t<=N-2`, the union of the first `t` closed stars has the boundary

```text
U,
A_{-1}, A_t,
B_{-1}, B_0, ..., B_{t-1},
```

so

```text
|B_t|=t+4.
```

The exposed vertex set has size

```text
|K_t|=2t+4.
```

At `t=N-1`, all `A` and `B` vertices plus `U` have been exposed. The only
unseen vertex is `D`.

Therefore the history coordinate

```text
|V(T_N) \ K_t|
```

strictly decreases for an arbitrarily long sweep and can reach `1` before this
family is forced into any separator exit.

This is exactly the distinction Cycle 3 needs:

```text
well-founded discovery != early useful terminal.
```

## 5. Exact same-boundary obstruction model

For a plane patch `P` with boundary `B`, define

```text
Ext(P)
```

to be the set of boundary two-colourings that extend to a complete colouring of
`P` with no monochromatic directed cycle.

A same-boundary ordinary replacement `Q` for `P` must satisfy at least

```text
Ext(Q) subseteq Ext(P).
```

The strong arbitrary-exterior condition is stricter, because it additionally
requires positive-reachability containment. Hence

```text
no ordinary extension replacement
   => no strong-profile replacement.
```

For a block of `k` consecutive `A` stars, the original patch has exactly `k`
internal vertices and boundary size `k+4`.

A strict same-boundary replacement has at most `k-1` internal vertices.

The checker permits **every** orientation of every maximal triangulated disk
with that boundary and fewer internal vertices. No source guard, semidegree
condition, or special reduction catalogue is imposed on `Q`. This is a
deliberate superset of source-valid reductions.

Nonmaximal `Q` cannot escape the test. If a nonmaximal oriented disk satisfied

```text
Ext(Q) subseteq Ext(P),
```

add arbitrary oriented diagonals until it is maximally triangulated. Adding
edges only removes valid `Q` colourings, so every such completion `Q'` still
satisfies

```text
Ext(Q') subseteq Ext(Q) subseteq Ext(P).
```

Since no maximal completion works, no nonmaximal patch works either.

## 6. Complete topology enumeration

The checker does not use a finite hand list of replacement topologies.

It recursively generates every triangulated disk by the face incident to a
distinguished closing boundary edge.

For a disk with cyclic boundary `B` and interior set `I`, let `x` be the third
vertex of the unique inner triangular face on the closing edge.

There are exactly two cases.

### Boundary third vertex

If `x` is another boundary vertex, that face splits the disk into two smaller
disks, and `I` partitions between the two sides.

### Interior third vertex

If `x` is interior, remove the root face. Then `x` becomes an additional
boundary vertex of the remaining disk, and recursion continues with
`I-{x}`.

Every triangulated disk follows one of these two cases at its root edge, so an
induction on

```text
|B| + |I|
```

generates every topology.

Degenerate unions created by coincident recursive edges are discarded by the
Euler edge-count identity

```text
|E| = 3(|B|+|I|) - 3 - |B|.
```

The exact topology-count canaries are

```text
boundary 5, internal 0:    5
boundary 6, internal 0:   14
boundary 6, internal 1:   84
boundary 7, internal 0:   42
boundary 7, internal 1:  330
boundary 7, internal 2: 4620.
```

The `q=0` counts agree with the Catalan polygon-triangulation counts.

## 7. One-star blocks are useless

For either parity, a single `A_i` star has

```text
boundary size 5,
internal vertices 1,
|Ext(P)|=24,
invalid boundary words=8.
```

A strict same-boundary replacement has zero internal vertices.

There are

```text
5 triangulations of the pentagon
x 4 orientations of their two diagonals
= 20
```

complete candidate `Q` orientations per parity.

None satisfies

```text
Ext(Q) subseteq Ext(P).
```

Thus every active `A_i` complete star is ordinary-extension irreducible.

## 8. Two-star blocks are still useless

For either parity, two consecutive stars have

```text
boundary size 6,
internal vertices 2,
|Ext(P)|=46,
invalid boundary words=18.
```

Every strict same-boundary replacement has zero or one internal vertex.

Per parity the exhaustive candidate universe is

```text
q=0:
  14 topologies * 2^3 orientations = 112

q=1:
  84 topologies * 2^6 orientations = 5376

total = 5488.
```

No candidate satisfies

```text
Ext(Q) subseteq Ext(P).
```

So aggregation of two adjacent exposed stars is still insufficient.

## 9. Three-star blocks are still useless

For either parity, three consecutive stars have

```text
boundary size 7,
internal vertices 3,
|Ext(P)|=86,
invalid boundary words=42.
```

Every strict replacement has `q=0,1,2` internal vertices.

Per parity:

```text
q=0:
   42 topologies * 2^4  =       672

q=1:
  330 topologies * 2^7  =    42,240

q=2:
 4620 topologies * 2^10 = 4,730,880
-----------------------------------
total                         4,773,792.
```

For both parity classes this is

```text
9,547,584
```

fully oriented smaller disks.

The candidate count satisfying

```text
Ext(Q) subseteq Ext(P)
```

is exactly

```text
0
```

for both parities.

Across the one-, two-, and three-star tests, the checker consumes

```text
2 * (20 + 5488 + 4,773,792)
= 9,558,600
```

strictly smaller oriented replacement candidates.

No finite row is promoted beyond the exact scopes stated here.

## 10. What this kills

Cycle 2 already killed history-free release and purely local separator ranks.

Cycle 3 kills the stronger inference

```text
a monotone history-aware discovery rank
plus local reductions of radius <=3
plus separating-triangle decomposition
must produce an early useful terminal.
```

It does not.

In `T_N`, for arbitrary `N`:

- the history rank can keep decreasing;
- the active interface grows rather than repeats;
- there is no separating triangle;
- every one-star patch is irreducible;
- every adjacent two-star patch is irreducible;
- every adjacent three-star patch is irreducible;
- after `N-1` A-star exposures only one vertex remains unseen.

Thus the surviving termination story needs genuinely more mathematics than
well-foundedness.

## 11. New live obligation

The next positive statement should be separated into two claims.

### WF-DISCOVERY

A history-aware source-resolution process is well founded.

Cycle 3 does not attack this.

### UNIFORM-USEFULNESS

There exists a source-faithful constant or structural trigger such that before
exposure becomes global, one obtains at least one of:

```text
(a) a strict same-boundary reduction on a bounded cluster,
(b) a source-valid structural contradiction,
(c) a sound separator composition,
(d) an exact GSRC/JMAP leaf.
```

The generic root-class lower bound established here is

```text
bounded-cluster constant >= 4.
```

The next S02-B adversarial target is therefore:

```text
for each r, build a high-port source-valid family whose every consecutive
exposed block of size <=r is same-boundary irreducible while the interface
continues to grow.
```

If such a family exists, no uniform local cluster theorem can terminate the
route.

If it fails, the first uniform `r` at which a reduction is forced is the
usefulness lemma S02-A actually needs.

## 12. Source separation

`T_N` is an exact simple plane orientation satisfying the global root-class
structural footprint used in this lane:

```text
plane triangulation,
simple orientation,
minimum semidegree >=2,
unbounded high degree,
actual rotations,
actual faces,
complete stars,
arbitrary size.
```

It is **not** claimed to be:

- an exact C37 `d(7)>=7` descendant;
- an LSRC realization of an A48 witness;
- a GSRC-generated negative-face state;
- a JMAP / unique-`L_join` child;
- a C45/C46 descendant;
- an AE/M12 or S14 cap state;
- a counterexample to the root conjecture.

Therefore a future GSRC/JMAP theorem may exclude this family. If so, that
exclusion itself is source-specific terminal-usefulness information and must be
proved; it cannot be supplied by the history rank.

## 13. Exact execution

Command:

```bash
g++ -O3 -std=c++17 s02b_cycle3_terminal_checker.cpp \
  -o s02b_cycle3_terminal_checker

./s02b_cycle3_terminal_checker 64 \
  > s02b_cycle3_terminal_output.json
```

Compiler:

```text
g++ (Debian 14.2.0-19) 14.2.0
```

Checker SHA-256:

```text
ccfaf917f11df1d146ca28f99d314601a5bc76643d9faddc2d178514b0a88fcc
```

Output SHA-256:

```text
f66a8f3c51a6b9571d6ca51eda0a57a883ca57af056566808650a48103f6d504
```

The topology generator, graph builder, embedding/face tracer, colouring test and
replacement enumeration are all in the same checker and same research trust
domain. This is exhaustive candidate control, not independent trusted
verification.

## 14. Non-claims

- No infinite normalized history-aware chain is claimed.
- History-aware well-foundedness is not refuted.
- No block of size `>=4` was classified.
- No nonlocal replacement theorem is refuted.
- No source-specific GSRC/JMAP terminal theorem is refuted.
- No exact C37 higher-degree source bridge is supplied.
- No separating-triangle composition theorem is proved; this family simply has
  no separating triangle.
- No EvidenceLink, Result, trusted verification, or root closure follows.

**Cycle-3 disposition:** keep S02-B active. The live target is no longer
well-foundedness; it is whether the local-hardness radius can be pumped from
`3` to arbitrary `r`, or whether a uniform source-faithful usefulness lemma
appears at some finite radius `r>=4`.
