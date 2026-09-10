# R08 S02-B — adversarial high-port chain audit

**Verdict:** `candidate_only`  
**Root:** `root_closed=false`  
**Fresh protected main at final source read:** `d3d43d517596934ea16c906c9f335e8cf6ba4884`  
**Exact reported ancestor:** `8d5bcb4955e84468f58a5923bed7f2ec527a6218`

## 1. Outcome

A literal unbounded **source-expansion family** exists in the C37 J-sector: degree,
fresh-port count, fan-sector count, and raw controlled-region size can all grow
without violating plane embedding, simplicity, the fixed core rotation, or the
minimum-semidegree footprint.

I did **not** obtain an infinite **unresolved reduction-child** chain. The
strongest self-similar pump found is blocked once its tail is enclosed by a fixed
four-port interface: the full strong boundary profile is finite, so an infinite
tail has two prefix patches with identical profiles; the later prefix then has a
strict source-valid profile-preserving replacement by the earlier one.

Thus this lane kills degree-chase termination, but does not kill every possible
well-founded high-port strategy. It isolates the missing premise: interface
growth / separator escape must itself carry a strictly decreasing rank.

## 2. Source separation

The merged C37 coverage applies exactly to `d(7)=6`; it is not used as a
classification of `d(7)>=7`.

C45/C46 are a different descendant source. C45 treats a complete degree-four
endpoint in one C44 residual; C46 treats only the guard-failure subcase
`d(z)=4` and leaves `d(z)>=5` open. Current S01 ancestor precedence makes those
same-C37-`d(7)=6` descendants inactive for live scheduling. No repository-bound
map sends a C37 `d(7)>=7` source state into the C45 high-degree state.

The mission-supplied S14/AE-M12 high-degree shell statement remains unbound
(`S14_C8`, SHA-256
`f21331f5833a1784f0f6e3f6a7ee2f8a09df528db44844e9d63ecb0e44e0b35d`);
current S01 gives it no DAG-closing effect. It is used neither as a pump nor as a
termination theorem here.

## 3. Exact high-port expansion family

Use the frozen C37 whole D,w3 triangulation only for its explicit core and
embedding. In that embedding the edge `12-13` has the two actual facial sides
with third vertices `7` and `5`.

For `n>=1`, define fresh distinct vertices `z_1,...,z_n`, delete the edge
`12-13`, and replace it by

```
12 -> z_1 -> z_2 -> ... -> z_n -> 13.
```

For each `i` independently choose one of the two spoke signs

```
bit 1: 7 -> z_i -> 5,
bit 0: 5 -> z_i -> 7.
```

All other C37 whole-witness arcs are unchanged.

The rotations are obtained by repeated edge splitting:

```
rot_7  = (2,3,8,12,z_1,...,z_n,13,11),
rot_5  = (0,6,13,z_n,...,z_1,12,8,4),

rot_12 = (5,z_1,7,8),
rot_13 = (5,6,11,7,z_n),

rot_z_i = (7,p_{i-1},5,p_{i+1}),
p_0=12, p_{n+1}=13.
```

Hence every face stays triangular. For every spoke word:

```
|V(G_n)| = 11+n,
|E(G_n)| = 27+3n = 3|V|-6,
|F(G_n)| = 18+2n,
d(7)     = 6+n.
```

Every `z_i` has complete degree four. The directed path gives one incoming and
one outgoing path arc at `z_i`; either spoke sign gives one additional incoming
and one additional outgoing arc. Thus

```
d^-(z_i)=d^+(z_i)=2.
```

Old vertices lose no semidegree: `12` and `13` replace the old `12->13`
incidence by the directed path endpoints, while `7` and `5` only gain incident
arcs. The source semidegree lower bound is preserved.

The exact expansion transition `T_i` splits the terminal path edge
`p_i->13`. It removes that arc, inserts a fresh `z_{i+1}`, and adds

```
p_i -> z_{i+1} -> 13
```

together with either `7->z_{i+1}->5` or `5->z_{i+1}->7`.
The operation adds one vertex and three net edges. It is performed in the union
of the two actual faces on the old terminal edge; no cross-lobe edge or alias
digon is introduced.

This proves an arbitrarily long source-valid high-port family. Every finite
degree cutoff `D` misses `G_n` for `n>D-6`.

## 4. Measures killed by the family

Along `T_i`:

| candidate quantity | transition |
|---|---|
| `d(7)` | `+1` |
| number of fresh fan ports | `+1` |
| number of fan sectors/faces | `+1` |
| local vertex count | `+1` |
| local edge count | `+3` |
| old-alias count | constant `0` |
| separator depth in this strip | constant |

So none of these quantities, alone or in a lexicographic tuple whose earlier
coordinates are constant here, is a decreasing termination measure.

The construction uses no old-port alias at all. This avoids the invalid move of
reusing an old star entry: in a simple graph the neighbours of `7` are distinct,
so any one old port can appear at most once in the star. An infinite alias-only
pump is impossible; the all-fresh tail is the real adversary.

## 5. Why the natural self-similar pump still dies

Let `P_w` be the strip patch for a spoke word `w`, with fixed boundary

```
B=(7,5,12,13).
```

All inserted `z_i` are internal and have complete stars, so this patch has no
unrecorded exterior contacts.

For a complete valid two-colouring of `P_w`, record:
1. the four boundary colours; and
2. for each colour, the positive directed reachability relation on `B`.

Let `Phi(P_w)` be, for each of the 16 boundary colour words, the set of all such
reachability relations realised by valid complete colourings.

Because `|B|=4`, `Phi` takes values in a finite set. A crude explicit bound is
enough: for one boundary colouring there are at most `2^12` directed
reachability bitsets on ordered boundary pairs, hence at most `2^4096` realised
relation sets; over 16 boundary colourings there are at most `2^65536` full
profiles.

Now fix any infinite spoke sequence and its finite prefixes
`w_0,w_1,w_2,...`. Two prefixes `w_i,w_j`, `i<j`, have the same full profile.

Inside `G_j`, delete the suffix `z_{i+1},...,z_j`. If `i>0`, add the cofacial
arc `z_i->13`; if `i=0`, add `12->13`. This reconstructs the shorter prefix
patch.

The reverse-edge guard is source-valid in this family:
- for `i>0`, `z_i` had complete degree four in `G_j` and was not adjacent to
  `13`;
- for `i=0`, the construction explicitly removed the unique underlying edge
  `12-13`.

The shortcut lies in the actual deletion disk. Equality
`Phi(P_{w_i})=Phi(P_{w_j})` says that every complete valid colouring of the
smaller prefix has a colouring of the larger prefix with the same boundary
colours and the same positive boundary reachability. Therefore the standard
arbitrary-exterior segment-replacement argument lifts every valid colouring of
the smaller whole graph to the larger one.

Consequently, in a minimum-order counterexample, a repeated fixed-interface
profile is impossible. The closed four-port edge-split family cannot yield an
infinite unresolved-child chain.

This is the first structural blocker found.

## 6. Bounded adversarial search

A dual-implementation checker was written from scratch for this lane.

Command:

```bash
python3 research/artifacts/candidates/opg169-a01-s02b-high-port-checker.py \
  --structural-max 64 \
  --profile-max 12 \
  --word-max 8 \
  > research/artifacts/candidates/opg169-a01-s02b-high-port-checker-output.json
```

Runtime: CPython 3.13.5.

Checker SHA-256:

```
549239acee6ed91e57ab941c0d2c0635fc5f9ded2471b2b4cdf881ea9ff9033d
```

Output SHA-256:

```
b3f74273204459ace40cbbde20021c314f8abe9e76f726d92d503717b3171835
```

The two internal implementations use:
- Kahn deletion + DFS reachability;
- Floyd-Warshall closure for both cycle detection and reachability.

They agreed on every enumerated complete colouring. This is algorithmic
differential control by one research principal, **not** an independent verifier
receipt.

Exact bounded scope/results:

- structural all-1 family checked through `n=64`, reaching
  `d(7)=70`, `|V|=75`, `|E|=219`, `|F|=146`, minimum in/outdegree `2`;
- natural all-1 profile checked through `n=12`;
- all `2^n` spoke words for every `1<=n<=8`: `510` source-valid words total;
- for `n=1`, word `1` has no shorter-prefix replacement;
- for every enumerated word with `2<=n<=8`, at least one shorter prefix is a
  strong-profile replacement;
- direct collapse to the `n=0` edge fails only on
  `1`, `101`, `10101`, `1010101` in the tested range;
- the longer alternating failures still collapse to the one-port prefix;
- for the natural word `1^n`, the `n=1` direct collapse fails exactly on
  boundary words `0110` and `1001`, while every `2<=n<=12` direct collapse
  succeeds.

No finite row above is promoted to a global high-port theorem.

## 7. C45 and AE/M12 pump audit

### C45

C45's proved same-boundary obstruction is real: when its reverse guard is
present, a successful next step must release at least one boundary port and
absorb a complete star. Raw interface size can therefore increase.

That makes C45 useful as an adversarial warning against a measure such as
"number of ports". It does not supply a C37 high-port recursive transition:
C45 is a different, currently ancestor-dominated `d(7)=6` descendant, and its
higher-degree endpoint normal form is not repository-bound.

### AE/M12

Current C48/S01 material explicitly says that a singleton gap does not imply an
AE/M12 or octahedral-cap profile. The mission-only S14 statement has no
repository-bound proof locator/exact-hypothesis match. No source-valid
C37-high-port -> AE/M12 transition is therefore available to pump.

## 8. Termination premise S02-A actually needs

The edge-split attack shows that **degree cannot be the rank**. The fixed
four-port obstruction shows what can replace it, but only after an additional
interface-control premise.

A sufficient termination architecture is:

**Bounded-interface / escape-rank premise.**
There exist a finite interface bound `b` and a well-founded rank `rho` on
interface-changing source states such that every unresolved high-port
transition is exactly one of:

1. **closed step:** it stays inside a disk with at most `b` boundary ports,
   every internal star has no exterior contacts, and all reverse-edge guards
   needed for profile compression are source-checked; or
2. **escape step:** it enlarges/releases the interface, crosses a separating
   triangle, or absorbs a new complete star, and strictly decreases `rho`.

For fixed `rho`, closed steps have finitely many full strong profiles. A repeated
profile gives a strict smaller replacement, so the admissible profile-transition
graph has no cycle. Its finite DAG height is a natural-number rank `h`. Then

```
(rho, h)
```

with lexicographic order is well founded and strictly decreases on every
admissible transition.

What remains unproved is exactly the escape clause: arbitrary exterior,
separating triangles, and complete-star release must be shown to decrease some
source-faithful `rho`. Without that clause the high-port termination argument is
not complete.

## 9. Next obligation

Construct or refute a **growing-interface pump**:

> a source-valid `d(7)>=7` family in which each forced complete-star release or
> separator crossing exposes genuinely new exterior ports, no fixed-size disk
> captures the tail, and the candidate escape rank fails to decrease.

This should be attacked before further degree enumeration. If no such family
survives, its first forced separator/profile compression is the missing lemma
for S02-A.

## 10. Non-claims

- No global infinite unresolved-child chain was found.
- No global no-pump theorem was proved.
- The unbounded family refutes finite degree cutoff as a termination strategy,
  not the Two Color Conjecture.
- C37 `160/160` remains exact `d(7)=6` candidate coverage only.
- C45 high-degree and AE/M12 mission statements were not imported as theorems.
- The bounded checker is not independent mathematical verification.
- `L_join`, B-criticality, separating-triangle composition, independent
  arbitrary-exterior lifting verification, and the root remain open.
