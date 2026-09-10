# R08 S02-B Cycle 2 — growing-interface / separator-escape rank attack

**Verdict:** `candidate_only`  
**Root:** `root_closed=false`  
**Fresh main at start of Cycle 2:** `b742c72f1d50849bd074f1f7f7f6e2ed019870c4`  
**Fresh main observed during Cycle 2:** `598d2c887a119fbb762ce51f9d6dc4af9431aff9`

Cycle 2 attacks only the S01 `ESCAPE-RANK` side gate:
interface release, complete-star absorption, separator crossing, and changing
exterior contact sets. It does not reopen the completed `d(7)=6` C37 table and
does not claim GSRC/JMAP.

## 1. Decision

A history-free escape rank is impossible for the natural raw transition
relation.

There is an exact C37-derived alternating high-port strip in which every
interior fresh degree-four port is a universal same-boundary obstruction. If
the source-resolution state remembers only the current active wheel, absorbing
the complete star of the right boundary port moves to the next obstructed wheel,
while absorbing the left port moves back. Hence the raw active-window release
relation contains literal two-cycles.

Separately, a repeated directed octahedral shell can be inserted into an actual
directed triangular face of the same high-port strip to arbitrary depth. The
old C37-derived rotation is preserved and every intermediate inner triangle is
a genuine separating triangle. All shell layers are locally isomorphic. Thus a
separator rank depending only on the current separator and bounded local
geometry cannot see the remaining depth.

The attack does **not** refute a history-aware rank. Finiteness of the fixed
original source graph blocks the pump once the transition state is required to
remember monotonically:
- exposed original vertex identities,
- which exposed vertices have had their complete stars frozen, and
- which rooted separator sides have already been traversed.

That rank proves source-discovery well-foundedness only. It does not prove that
the terminal source is reducible, or that GSRC/JMAP succeeds.

## 2. Exact alternating-wheel obstruction

Take the Cycle-1 S02-B edge-split family

```text
12 -> z1 -> z2 -> ... -> zn -> 13
```

with poles `7,5`. For each fresh port use one of the spoke signs

```text
1: 7 -> zi -> 5
0: 5 -> zi -> 7.
```

Choose the alternating word

```text
101010...101
```

of odd length. Every interior `z_i` has complete cyclic star

```text
(7, z_{i-1}, 5, z_{i+1})
```

and degree four.

For an interior wheel, write its boundary in the order

```text
(U,L,D,R)=(7,z_{i-1},5,z_{i+1})
```

and center `x=z_i`. The chain edges are `L->x->R`.

Only two local triples occur.

### Type 010

The arcs are

```text
L -> x -> R
U -> x -> D
D -> L -> U
D -> R -> U.
```

Boundary colouring

```text
(U,L,D,R) = (0,1,1,0)
```

has no extension:
- `x=0` makes `U->x->R->U` monochromatic;
- `x=1` makes `x->D->L->x` monochromatic.

The complementary boundary word `1001` also fails.

### Type 101

The arcs are

```text
L -> x -> R
D -> x -> U
U -> L -> D
U -> R -> D.
```

Boundary colouring

```text
(U,L,D,R) = (0,0,1,1)
```

has no extension:
- `x=0` makes `L->x->U->L` monochromatic;
- `x=1` makes `x->R->D->x` monochromatic.

The complementary word `1100` also fails.

Each bad boundary word uses two vertices of each colour. Any strictly smaller
replacement preserving all four boundary vertices has no internal vertex.
In a simple orientation, a colour class on at most two vertices cannot contain
a directed cycle. Therefore the displayed boundary word is valid for **every**
same-boundary strictly smaller simple oriented replacement, while it is invalid
for the original wheel.

So each alternating interior wheel has a universal ordinary all-Q
same-boundary obstruction. This is stronger than failure of one chosen shortcut
or one reachability table.

## 3. Raw complete-star release relation contains two-cycles

Let `W_i` be the active wheel centered at an interior `z_i`.

Because the same-boundary route is impossible, a local strategy that continues
by releasing a boundary port may absorb the complete star of `z_{i+1}` and move
to `W_{i+1}`. But `z_i` is a boundary port of `W_{i+1}`, and its complete star is
also source-valid. If the active state forgets exposure history, the reverse
move is equally legal:

```text
W_i -> W_{i+1} -> W_i.
```

Thus no map from the raw active-wheel state space to any well-founded order can
strictly decrease on **every** such release transition.

This is not merely a large finite cutoff failure. It is a literal directed
cycle in the unnormalized transition relation.

The executed `n=31` C37-derived strip has

```text
d(7)=37,
29 obstructed interior wheels,
28 adjacent raw release two-cycles.
```

Therefore any S02-A transition system that permits "release any source-valid
boundary complete star" without a no-backtracking history condition is not
well founded.

## 4. Generic cyclic stress test: alternating bipyramids

There is an even cleaner root-class countermodel to a purely local release rank.

For any even `N>=8`, take the `N`-gonal bipyramid with poles `U,D` and rim

```text
v0,v1,...,v_{N-1}.
```

Orient the rim cyclically

```text
v_i -> v_{i+1}.
```

Use alternating spokes:

```text
i even: U -> v_i -> D
i odd : D -> v_i -> U.
```

The underlying graph is a simple plane triangulation:

```text
|V| = N+2,
|E| = 3N = 3|V|-6,
|F| = 2N.
```

Every rim vertex has indegree/outdegree `2/2`; each pole has
indegree/outdegree `N/2,N/2`.

Every rim wheel is exactly type `010` or `101`, hence has the universal
same-boundary obstruction above. A locally canonical rule "release the next
rim port in the directed rim order" gives

```text
W_0 -> W_1 -> ... -> W_{N-1} -> W_0.
```

So even a locally oriented successor convention does not rescue a history-free
rank.

This bipyramid family is a **root-class stress test**, not claimed to be an
exact C37 descendant or an LSRC output of the current DC2 source generator.
It shows what GSRC/JMAP would have to exclude before a universal local escape
rank could be stated.

## 5. Exact separator-depth stress test inside the C37 high-port source

Take the odd alternating strip and its final bit `1`. The actual face

```text
T0=(7,z_n,13)
```

is a directed triangle

```text
7 -> z_n -> 13 -> 7.
```

Inside this face insert one directed octahedral shell. If the outer directed
triangle is

```text
A -> B -> C -> A,
```

create an inner triangle

```text
a -> b -> c -> a
```

and orient the six cross edges as

```text
A -> b -> C -> a -> B -> c -> A.
```

Every vertex in one isolated shell has two incoming and two outgoing arcs.
Repeat the same operation inside the inner face.

For depth `m`, each new layer adds exactly three vertices and nine edges.
Intermediate triangle vertices have indegree/outdegree `3/3`; the terminal
inner triangle has `2/2`. The construction is a maximal planar orientation.

The checker spliced depth `32` into the exact `n=31` C37-derived strip:

```text
|V| = 138,
|E| = 408 = 3|V|-6,
minimum indegree = minimum outdegree = 2.
```

NetworkX planarity plus an explicit rotation restriction audit recovered the
old C37-derived cyclic order **unchanged** on every pre-splice vertex.

There are 31 intermediate genuine separating triangles. Deleting each one
separates the graph into a nonempty outer and inner component.

Every shell uses the same directed local geometry. Therefore:
- boundary size stays `3`;
- active shell size stays constant;
- local direction/profile type is periodic with period `1`;
- "level counted from the original outer face" increases under inward crossing.

An arbitrarily deep family defeats every escape rank that factors only through
the active separator and a fixed-radius local neighborhood.

This is still not an infinite unresolved chain: the whole shell stack lies
inside the fixed outer triangle `T0`, so a global fixed-interface profile
compression may eventually compress it. The result attacks **local separator
ranking**, not the bounded-interface theorem.

## 6. First unavoidable structural blocker

The surviving rank must be history-aware.

Fix the actual finite original source graph `G`. A normalized source-resolution
state should retain at least:

```text
K = exposed original vertex identities,
C = exposed vertices whose complete stars are frozen,
P = rooted separator sides already traversed/processed.
```

Require monotonicity:

```text
K' superset K,
C' superset C,
P' superset P.
```

Every genuine escape step must do at least one of:

1. expose a previously unseen original vertex: `K' > K`;
2. with no new vertex, freeze a previously incomplete exposed star: `C' > C`;
3. with neither, cross a previously unprocessed rooted separator side:
   `P' > P`.

Then the lexicographic natural-number rank

```text
rho =
(
  |V(G)\K|,
  |V(G)\C|,
  N_sep(G)-|P|
)
```

strictly decreases.

Aliases do not break the argument. If completing a star discovers only aliases
to already exposed vertices, the first coordinate stays fixed but the second
decreases. A separator crossing that reveals no new star decreases the third.

The raw two-cycle disappears because after

```text
W_i -> W_{i+1}
```

the complete star of `z_{i+1}` is now in `C`; returning to `W_i` by "releasing"
the already completed `z_i` is not a new escape step.

Similarly, separator traversal must be rooted/no-backtracking. An unrooted
relation that allows crossing the same separator both ways cannot admit a
strict rank.

## 7. Why this does not solve S02-A

The history rank proves only:

> a normalized process that monotonically accumulates true source information
> cannot query fresh source information forever in a finite graph.

It does **not** prove:
- that a bounded number of local source types suffices;
- that the process terminates before exposing essentially all of `G`;
- that the terminal state has a strict profile reduction;
- that the terminal state maps uniquely through GSRC/JMAP;
- that separating-triangle composition is sound;
- that `L_join` or B-criticality closes.

So "unseen vertices" is a valid well-foundedness coordinate but can be
mathematically vacuous for the local-reduction program unless S02-A supplies a
terminal theorem.

The next positive obligation is not another degree bound. It is:

```text
TERMINAL-USEFULNESS:
show that before the monotone exposure rank reaches its trivial terminal state,
one obtains either
  (a) a fixed-interface repeated profile reduction,
  (b) a source-valid structural contradiction,
  (c) a rooted separator decomposition with sound composition, or
  (d) an exact GSRC/JMAP leaf.
```

The next adversarial obligation is to construct a family where the normalized
history rank decreases correctly but every intermediate state remains locally
irreducible until the whole graph is exposed. That would show the rank is
termination-only and useless as a local theorem.

## 8. Exact bounded checker

Command:

```bash
python3 s02b_cycle2_escape_checker.py \
  --strip-n 31 \
  --bipyramid-max 64 \
  --separator-depth 32 \
  > s02b_cycle2_escape_output.json
```

Environment:

```text
CPython 3.13.5
NetworkX 3.6.1
```

Checker SHA-256:

```text
aaacfaaa24229919fdcacc79ce00532480fab45d068504542b8b275bb0b77b6b
```

Output SHA-256:

```text
c6587703d780e1ad0d695bad5fc7924543b006837ca8e0a36299b53a6a85093d
```

The colouring obstruction is cross-checked with:
- Kahn topological deletion;
- a separate Floyd-Warshall transitive-closure implementation.

The plane tests use explicit rotations for the strip and bipyramid; the
separator splice is additionally checked by NetworkX planarity and by
restriction of the returned maximal-planar rotation to all old C37-derived
vertices.

All implementations belong to this generator trust domain. They are not an
independent verifier receipt.

## 9. Failed measures

Cycle 1 already killed:

```text
d(7),
fresh-port count,
fan-sector count,
raw local V/E size.
```

Cycle 2 additionally kills, on the raw/history-free escape relation:

```text
active boundary size,
active wheel size,
active local isomorphism/profile type,
number of released ports,
separator local type,
separator level measured from the outer root,
any rank required to decrease on both directions of an unrooted
complete-star release or separator-crossing relation.
```

A locally canonical successor direction is also insufficient: the alternating
bipyramid closes it into a cycle.

## 10. Non-claims

- No infinite normalized history-aware source-resolution chain was found.
- No global termination theorem is claimed.
- No statement here promotes the generic bipyramid to a C37 descendant.
- No claim is made that the nested octahedral shell is an AE/M12/S14 cap.
- C37 `d(7)=6` remains a separate exact candidate library.
- The Cycle-2 constructions do not prove GSRC, JMAP, L_join, B-criticality or
  arbitrary-exterior separator composition.
- A finite decreasing exposure rank is not by itself a proof that the local
  reduction strategy succeeds.
- No EvidenceLink, Result, trusted verification or root closure follows.
