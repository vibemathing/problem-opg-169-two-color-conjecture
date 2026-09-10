import Init

/-!
R08 / OPG-169 / S11 Cycle 7
Raw C13 exact-glue proof plus the existing StrongLift -> GoodLiftOn bridge.

Candidate source only. This file is intentionally self-contained (`import Init`).
No Lean toolchain was available in the generation runtime, so no compilation or
kernel receipt is claimed here.

Formal boundary model:
* `B` is the actual boundary type AFTER source-valid alias quotienting;
* patch-private and exterior-private vertices are disjoint sum summands;
* the only shared vertices are the single canonical `B` summand;
* on a same-direction boundary arc present in both pieces, the exterior owns the
  whole-arc occurrence (exterior precedence); the underlying relation still has
  that arc exactly once;
* an opposite patch/exterior boundary pair is exposed as
  `ReverseArcGuardFailure`; it is a class-preservation failure for orientations.

The raw C13 theorem proved below is graph-theoretic and in fact still describes
acyclic colourings if a reverse conflict is present.  The source-class wrapper
`GlueContract` requires the reverse guard to be safe before the result is used as
an ordinary orientation replacement.
-/

universe u

namespace OPG169.S11Cycle7

/-- Positive walk. There is deliberately no empty/reflexive constructor. -/
inductive Walk {V : Type u} (R : V → V → Prop) : V → V → Prop where
  | edge {x y : V} : R x y → Walk R x y
  | cons {x y z : V} : R x y → Walk R y z → Walk R x z

/-- Concatenate two positive walks. -/
theorem walk_join {V : Type u} {R : V → V → Prop}
    {x y z : V} (p : Walk R x y) (q : Walk R y z) : Walk R x z := by
  induction p with
  | edge e => exact Walk.cons e q
  | cons e p ih => exact Walk.cons e ih

/-- Map every edge of a positive walk. -/
theorem walk_map {V : Type u} {R S : V → V → Prop}
    (h : ∀ {a b : V}, R a b → S a b)
    {x y : V} (p : Walk R x y) : Walk S x y := by
  induction p with
  | edge e => exact Walk.edge (h e)
  | cons e p ih => exact Walk.cons (h e) ih

/-- Replace each edge by a nonempty walk and flatten. -/
theorem walk_bind {V : Type u} {R S : V → V → Prop}
    (h : ∀ {a b : V}, R a b → Walk S a b)
    {x y : V} (p : Walk R x y) : Walk S x y := by
  induction p with
  | edge e => exact h e
  | cons e p ih => exact walk_join (h e) ih

/-- A relation has no positive directed closed walk. -/
def Acyclic {V : Type u} (R : V → V → Prop) : Prop :=
  ∀ x : V, Not (Walk R x x)

/-- Full induced relation of one colour. -/
def Mono {V : Type u} (R : V → V → Prop)
    (c : V → Bool) (k : Bool) (x y : V) : Prop :=
  R x y ∧ c x = k ∧ c y = k

/-- Both complete induced colour classes are acyclic. -/
def Good {V : Type u} (R : V → V → Prop) (c : V → Bool) : Prop :=
  ∀ k : Bool, Acyclic (Mono R c k)

abbrev PieceV (B I : Type u) := Sum B I
abbrev WholeV (B IP IX : Type u) := Sum B (Sum IP IX)

structure Piece (B I : Type u) where
  Arc : PieceV B I → PieceV B I → Prop

/-- Canonical patch embedding. -/
def patchVertex {B IP IX : Type u} : PieceV B IP → WholeV B IP IX
  | Sum.inl b => Sum.inl b
  | Sum.inr p => Sum.inr (Sum.inl p)

/-- Canonical exterior embedding. -/
def exteriorVertex {B IP IX : Type u} : PieceV B IX → WholeV B IP IX
  | Sum.inl b => Sum.inl b
  | Sum.inr x => Sum.inr (Sum.inr x)

/-- The canonical typed model has one actual shared boundary and disjoint private
    summands.  Source aliases must already have been quotiented before choosing
    the type `B`; there is no second formal copy of a boundary vertex. -/
def AliasNormalizedActualBoundary {B IP IX : Type u} : Prop :=
  (∀ b : B,
      patchVertex (IP := IP) (IX := IX) (Sum.inl b) =
      exteriorVertex (IP := IP) (IX := IX) (Sum.inl b)) ∧
  (∀ p : IP, ∀ x : IX,
      patchVertex (IX := IX) (Sum.inr p) ≠
      exteriorVertex (IP := IP) (Sum.inr x)) ∧
  (∀ b : B, ∀ p : IP,
      patchVertex (IP := IP) (IX := IX) (Sum.inl b) ≠
      patchVertex (IX := IX) (Sum.inr p)) ∧
  (∀ b : B, ∀ x : IX,
      exteriorVertex (IP := IP) (IX := IX) (Sum.inl b) ≠
      exteriorVertex (IP := IP) (Sum.inr x))

theorem canonical_alias_normalized_actual_boundary {B IP IX : Type u} :
    AliasNormalizedActualBoundary (B := B) (IP := IP) (IX := IX) := by
  constructor
  · intro b
    rfl
  · constructor
    · intro p x h
      cases h
    · constructor
      · intro b p h
        cases h
      · intro b x h
        cases h

/-- Whole relation with exterior precedence on shared same-direction boundary
    arcs.  The boundary-boundary case says: use the exterior occurrence when it
    exists; otherwise use the patch occurrence.  Mixed private/private contacts
    across pieces are unrepresentable and therefore false. -/
def GlueArc {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) :
    WholeV B IP IX → WholeV B IP IX → Prop
  | Sum.inl s, Sum.inl t =>
      X.Arc (Sum.inl s) (Sum.inl t) ∨
      (P.Arc (Sum.inl s) (Sum.inl t) ∧
       Not (X.Arc (Sum.inl s) (Sum.inl t)))
  | Sum.inl s, Sum.inr (Sum.inl p) =>
      P.Arc (Sum.inl s) (Sum.inr p)
  | Sum.inl s, Sum.inr (Sum.inr x) =>
      X.Arc (Sum.inl s) (Sum.inr x)
  | Sum.inr (Sum.inl p), Sum.inl t =>
      P.Arc (Sum.inr p) (Sum.inl t)
  | Sum.inr (Sum.inl p), Sum.inr (Sum.inl q) =>
      P.Arc (Sum.inr p) (Sum.inr q)
  | Sum.inr (Sum.inl _), Sum.inr (Sum.inr _) => False
  | Sum.inr (Sum.inr x), Sum.inl t =>
      X.Arc (Sum.inr x) (Sum.inl t)
  | Sum.inr (Sum.inr x), Sum.inr (Sum.inl _) => False
  | Sum.inr (Sum.inr x), Sum.inr (Sum.inr y) =>
      X.Arc (Sum.inr x) (Sum.inr y)

/-- A source/class guard failure: the patch contributes one boundary direction
    while the exterior contributes its reverse. -/
def ReverseArcGuardFailure {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : Prop :=
  ∃ s t : B, s ≠ t ∧
    P.Arc (Sum.inl s) (Sum.inl t) ∧
    X.Arc (Sum.inl t) (Sum.inl s)

def ReverseArcGuardSafe {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : Prop :=
  Not (ReverseArcGuardFailure P X)

/-- Source-facing contract. Alias normalization/private disjointness are enforced
    by the canonical types; the remaining class-preservation gate here is the
    cross-piece reverse-arc guard. -/
def GlueContract {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : Prop :=
  ReverseArcGuardSafe P X

/-- Restrict a whole colouring to the patch. -/
def restrictPatch {B IP IX : Type u}
    (w : WholeV B IP IX → Bool) : PieceV B IP → Bool
  | Sum.inl b => w (Sum.inl b)
  | Sum.inr p => w (Sum.inr (Sum.inl p))

/-- Restrict a whole colouring to the exterior. -/
def restrictExterior {B IP IX : Type u}
    (w : WholeV B IP IX → Bool) : PieceV B IX → Bool
  | Sum.inl b => w (Sum.inl b)
  | Sum.inr x => w (Sum.inr (Sum.inr x))

/-- Positive monochromatic boundary reachability.  Positive means a genuine
    `Walk`; no empty path is available.  Under `Good`, diagonal entries are
    automatically impossible. -/
def RPlus {B I : Type u} (P : Piece B I)
    (c : PieceV B I → Bool) (k : Bool) (s t : B) : Prop :=
  Walk (Mono P.Arc c k) (Sum.inl s) (Sum.inl t)

/-- The relation whose positive transitive closure is audited by C13. -/
def BoundaryUnion {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX)
    (cP : PieceV B IP → Bool) (cX : PieceV B IX → Bool)
    (k : Bool) (s t : B) : Prop :=
  RPlus P cP k s t ∨ RPlus X cX k s t

/-- No nonempty cyclic chain of patch/exterior positive boundary returns. -/
def CrossSafe {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX)
    (cP : PieceV B IP → Bool) (cX : PieceV B IX → Bool) : Prop :=
  ∀ k : Bool, ∀ b : B,
    Not (Walk (BoundaryUnion P X cP cX k) b b)

/-- Valid patch colourings have no diagonal positive boundary reachability. -/
theorem rplus_irrefl_of_good {B I : Type u}
    {P : Piece B I} {c : PieceV B I → Bool}
    (hGood : Good P.Arc c) (k : Bool) (b : B) :
    Not (RPlus P c k b b) := by
  intro h
  exact hGood k (Sum.inl b) h

/-- Every patch arc embeds into the exterior-precedence whole relation.  On a
    shared same-direction boundary arc, the proof uses the exterior-owned branch. -/
theorem patchArc_to_glue {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {a b : PieceV B IP} (h : P.Arc a b) :
    GlueArc P X (patchVertex (IX := IX) a) (patchVertex (IX := IX) b) := by
  classical
  cases a with
  | inl s =>
      cases b with
      | inl t =>
          change X.Arc (Sum.inl s) (Sum.inl t) ∨
            (P.Arc (Sum.inl s) (Sum.inl t) ∧
             Not (X.Arc (Sum.inl s) (Sum.inl t)))
          by_cases hx : X.Arc (Sum.inl s) (Sum.inl t)
          · exact Or.inl hx
          · exact Or.inr ⟨h, hx⟩
      | inr p =>
          change P.Arc (Sum.inl s) (Sum.inr p)
          exact h
  | inr p =>
      cases b with
      | inl t =>
          change P.Arc (Sum.inr p) (Sum.inl t)
          exact h
      | inr q =>
          change P.Arc (Sum.inr p) (Sum.inr q)
          exact h

/-- Every exterior arc embeds into the whole relation. -/
theorem exteriorArc_to_glue {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {a b : PieceV B IX} (h : X.Arc a b) :
    GlueArc P X (exteriorVertex (IP := IP) a) (exteriorVertex (IP := IP) b) := by
  cases a with
  | inl s =>
      cases b with
      | inl t =>
          change X.Arc (Sum.inl s) (Sum.inl t) ∨
            (P.Arc (Sum.inl s) (Sum.inl t) ∧
             Not (X.Arc (Sum.inl s) (Sum.inl t)))
          exact Or.inl h
      | inr x =>
          change X.Arc (Sum.inl s) (Sum.inr x)
          exact h
  | inr x =>
      cases b with
      | inl t =>
          change X.Arc (Sum.inr x) (Sum.inl t)
          exact h
      | inr y =>
          change X.Arc (Sum.inr x) (Sum.inr y)
          exact h

/-- A cross-piece reverse guard failure produces both directions in the whole
    relation, hence cannot represent an orientation of a simple graph. -/
theorem reverseGuardFailure_gives_digon {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    (h : ReverseArcGuardFailure P X) :
    ∃ s t : B, s ≠ t ∧
      GlueArc P X (Sum.inl s) (Sum.inl t) ∧
      GlueArc P X (Sum.inl t) (Sum.inl s) := by
  cases h with
  | intro s hs =>
    cases hs with
    | intro t ht =>
      have hne := ht.1
      have hp := ht.2.1
      have hx := ht.2.2
      refine ⟨s, t, hne, ?_, ?_⟩
      · exact patchArc_to_glue (P := P) (X := X) hp
      · exact exteriorArc_to_glue (P := P) (X := X) hx

/-- Local patch monochromatic edges embed in the whole monochromatic relation. -/
theorem patchMono_to_whole {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {a b : PieceV B IP}
    (h : Mono P.Arc (restrictPatch w) k a b) :
    Mono (GlueArc P X) w k
      (patchVertex (IX := IX) a) (patchVertex (IX := IX) b) := by
  refine ⟨patchArc_to_glue (P := P) (X := X) h.1, ?_, ?_⟩
  · cases a <;> exact h.2.1
  · cases b <;> exact h.2.2

/-- Local exterior monochromatic edges embed in the whole monochromatic relation. -/
theorem exteriorMono_to_whole {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {a b : PieceV B IX}
    (h : Mono X.Arc (restrictExterior w) k a b) :
    Mono (GlueArc P X) w k
      (exteriorVertex (IP := IP) a) (exteriorVertex (IP := IP) b) := by
  refine ⟨exteriorArc_to_glue (P := P) (X := X) h.1, ?_, ?_⟩
  · cases a <;> exact h.2.1
  · cases b <;> exact h.2.2

theorem patchWalk_to_whole {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {a b : PieceV B IP}
    (p : Walk (Mono P.Arc (restrictPatch w) k) a b) :
    Walk (Mono (GlueArc P X) w k)
      (patchVertex (IX := IX) a) (patchVertex (IX := IX) b) :=
  walk_map (fun h => patchMono_to_whole (P := P) (X := X) h) p

theorem exteriorWalk_to_whole {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {a b : PieceV B IX}
    (p : Walk (Mono X.Arc (restrictExterior w) k) a b) :
    Walk (Mono (GlueArc P X) w k)
      (exteriorVertex (IP := IP) a) (exteriorVertex (IP := IP) b) :=
  walk_map (fun h => exteriorMono_to_whole (P := P) (X := X) h) p

/-- Extract a patch monochromatic edge from a whole edge whose endpoints force
    patch ownership. -/
theorem wholeMono_patch_boundary_private {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {s : B} {p : IP}
    (h : Mono (GlueArc P X) w k
      (Sum.inl s) (Sum.inr (Sum.inl p))) :
    Mono P.Arc (restrictPatch w) k (Sum.inl s) (Sum.inr p) := by
  exact h

theorem wholeMono_patch_private_boundary {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {p : IP} {t : B}
    (h : Mono (GlueArc P X) w k
      (Sum.inr (Sum.inl p)) (Sum.inl t)) :
    Mono P.Arc (restrictPatch w) k (Sum.inr p) (Sum.inl t) := by
  exact h

theorem wholeMono_patch_private_private {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {p q : IP}
    (h : Mono (GlueArc P X) w k
      (Sum.inr (Sum.inl p)) (Sum.inr (Sum.inl q))) :
    Mono P.Arc (restrictPatch w) k (Sum.inr p) (Sum.inr q) := by
  exact h

theorem wholeMono_exterior_boundary_private {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {s : B} {x : IX}
    (h : Mono (GlueArc P X) w k
      (Sum.inl s) (Sum.inr (Sum.inr x))) :
    Mono X.Arc (restrictExterior w) k (Sum.inl s) (Sum.inr x) := by
  exact h

theorem wholeMono_exterior_private_boundary {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {x : IX} {t : B}
    (h : Mono (GlueArc P X) w k
      (Sum.inr (Sum.inr x)) (Sum.inl t)) :
    Mono X.Arc (restrictExterior w) k (Sum.inr x) (Sum.inl t) := by
  exact h

theorem wholeMono_exterior_private_private {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {x y : IX}
    (h : Mono (GlueArc P X) w k
      (Sum.inr (Sum.inr x)) (Sum.inr (Sum.inr y))) :
    Mono X.Arc (restrictExterior w) k (Sum.inr x) (Sum.inr y) := by
  exact h

/-- A monochromatic whole boundary edge is one positive boundary-relation edge,
    with exterior precedence deciding ownership in the shared-edge case. -/
theorem wholeMono_boundary_edge_to_union {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {s t : B}
    (h : Mono (GlueArc P X) w k (Sum.inl s) (Sum.inl t)) :
    BoundaryUnion P X (restrictPatch w) (restrictExterior w) k s t := by
  have ha := h.1
  change X.Arc (Sum.inl s) (Sum.inl t) ∨
    (P.Arc (Sum.inl s) (Sum.inl t) ∧
     Not (X.Arc (Sum.inl s) (Sum.inl t))) at ha
  cases ha with
  | inl hx =>
      exact Or.inr (Walk.edge ⟨hx, h.2.1, h.2.2⟩)
  | inr hp =>
      exact Or.inl (Walk.edge ⟨hp.1, h.2.1, h.2.2⟩)

/-- Normal form of a positive whole walk ending on the boundary.  A private
    start either reaches the final boundary wholly inside its own piece, or
    reaches an earlier boundary inside that piece and then continues as a
    boundary-relation chain. -/
def ToBoundaryNF {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX)
    (w : WholeV B IP IX → Bool) (k : Bool)
    (v : WholeV B IP IX) (t : B) : Prop :=
  match v with
  | Sum.inl s =>
      Walk (BoundaryUnion P X (restrictPatch w) (restrictExterior w) k) s t
  | Sum.inr (Sum.inl p) =>
      Walk (Mono P.Arc (restrictPatch w) k) (Sum.inr p) (Sum.inl t) ∨
      ∃ b : B,
        Walk (Mono P.Arc (restrictPatch w) k) (Sum.inr p) (Sum.inl b) ∧
        Walk (BoundaryUnion P X (restrictPatch w) (restrictExterior w) k) b t
  | Sum.inr (Sum.inr x) =>
      Walk (Mono X.Arc (restrictExterior w) k) (Sum.inr x) (Sum.inl t) ∨
      ∃ b : B,
        Walk (Mono X.Arc (restrictExterior w) k) (Sum.inr x) (Sum.inl b) ∧
        Walk (BoundaryUnion P X (restrictPatch w) (restrictExterior w) k) b t

/-- Raw C13 cutting lemma, proved directly by induction over the positive whole
    walk. -/
theorem wholeWalk_to_boundaryNF {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {v : WholeV B IP IX} {t : B}
    (p : Walk (Mono (GlueArc P X) w k) v (Sum.inl t)) :
    ToBoundaryNF P X w k v t := by
  induction p with
  | edge e =>
      cases v with
      | inl s =>
          exact Walk.edge (wholeMono_boundary_edge_to_union e)
      | inr v =>
          cases v with
          | inl q =>
              exact Or.inl (Walk.edge (wholeMono_patch_private_boundary e))
          | inr y =>
              exact Or.inl (Walk.edge (wholeMono_exterior_private_boundary e))
  | @cons x y z e rest ih =>
      cases x with
      | inl s =>
          cases y with
          | inl b =>
              have hEdge := wholeMono_boundary_edge_to_union e
              exact Walk.cons hEdge ih
          | inr y =>
              cases y with
              | inl q =>
                  have hEdge := wholeMono_patch_boundary_private e
                  change
                    (Walk (Mono P.Arc (restrictPatch w) k)
                        (Sum.inr q) (Sum.inl t) ∨
                     ∃ b : B,
                       Walk (Mono P.Arc (restrictPatch w) k)
                         (Sum.inr q) (Sum.inl b) ∧
                       Walk (BoundaryUnion P X
                         (restrictPatch w) (restrictExterior w) k) b t) at ih
                  cases ih with
                  | inl hLocal =>
                      exact Walk.edge (Or.inl (Walk.cons hEdge hLocal))
                  | inr hSplit =>
                      cases hSplit with
                      | intro b hb =>
                          exact Walk.cons (Or.inl (Walk.cons hEdge hb.1)) hb.2
              | inr y =>
                  have hEdge := wholeMono_exterior_boundary_private e
                  change
                    (Walk (Mono X.Arc (restrictExterior w) k)
                        (Sum.inr y) (Sum.inl t) ∨
                     ∃ b : B,
                       Walk (Mono X.Arc (restrictExterior w) k)
                         (Sum.inr y) (Sum.inl b) ∧
                       Walk (BoundaryUnion P X
                         (restrictPatch w) (restrictExterior w) k) b t) at ih
                  cases ih with
                  | inl hLocal =>
                      exact Walk.edge (Or.inr (Walk.cons hEdge hLocal))
                  | inr hSplit =>
                      cases hSplit with
                      | intro b hb =>
                          exact Walk.cons (Or.inr (Walk.cons hEdge hb.1)) hb.2
      | inr x =>
          cases x with
          | inl p0 =>
              change
                (Walk (Mono P.Arc (restrictPatch w) k)
                    (Sum.inr p0) (Sum.inl t) ∨
                 ∃ b : B,
                   Walk (Mono P.Arc (restrictPatch w) k)
                     (Sum.inr p0) (Sum.inl b) ∧
                   Walk (BoundaryUnion P X
                     (restrictPatch w) (restrictExterior w) k) b t)
              cases y with
              | inl b =>
                  have hEdge := wholeMono_patch_private_boundary e
                  change
                    Walk (BoundaryUnion P X
                      (restrictPatch w) (restrictExterior w) k) b t at ih
                  exact Or.inr ⟨b, Walk.edge hEdge, ih⟩
              | inr y =>
                  cases y with
                  | inl q =>
                      have hEdge := wholeMono_patch_private_private e
                      change
                        (Walk (Mono P.Arc (restrictPatch w) k)
                            (Sum.inr q) (Sum.inl t) ∨
                         ∃ b : B,
                           Walk (Mono P.Arc (restrictPatch w) k)
                             (Sum.inr q) (Sum.inl b) ∧
                           Walk (BoundaryUnion P X
                             (restrictPatch w) (restrictExterior w) k) b t) at ih
                      cases ih with
                      | inl hLocal =>
                          exact Or.inl (Walk.cons hEdge hLocal)
                      | inr hSplit =>
                          cases hSplit with
                          | intro b hb =>
                              exact Or.inr ⟨b, Walk.cons hEdge hb.1, hb.2⟩
                  | inr q =>
                      have hf := e.1
                      change False at hf
                      exact False.elim hf
          | inr x0 =>
              change
                (Walk (Mono X.Arc (restrictExterior w) k)
                    (Sum.inr x0) (Sum.inl t) ∨
                 ∃ b : B,
                   Walk (Mono X.Arc (restrictExterior w) k)
                     (Sum.inr x0) (Sum.inl b) ∧
                   Walk (BoundaryUnion P X
                     (restrictPatch w) (restrictExterior w) k) b t)
              cases y with
              | inl b =>
                  have hEdge := wholeMono_exterior_private_boundary e
                  change
                    Walk (BoundaryUnion P X
                      (restrictPatch w) (restrictExterior w) k) b t at ih
                  exact Or.inr ⟨b, Walk.edge hEdge, ih⟩
              | inr y =>
                  cases y with
                  | inl q =>
                      have hf := e.1
                      change False at hf
                      exact False.elim hf
                  | inr y0 =>
                      have hEdge := wholeMono_exterior_private_private e
                      change
                        (Walk (Mono X.Arc (restrictExterior w) k)
                            (Sum.inr y0) (Sum.inl t) ∨
                         ∃ b : B,
                           Walk (Mono X.Arc (restrictExterior w) k)
                             (Sum.inr y0) (Sum.inl b) ∧
                           Walk (BoundaryUnion P X
                             (restrictPatch w) (restrictExterior w) k) b t) at ih
                      cases ih with
                      | inl hLocal =>
                          exact Or.inl (Walk.cons hEdge hLocal)
                      | inr hSplit =>
                          cases hSplit with
                          | intro b hb =>
                              exact Or.inr ⟨b, Walk.cons hEdge hb.1, hb.2⟩

/-- Normal form used only when a closed walk is based at a patch-private vertex. -/
def ToPatchPrivateNF {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX)
    (w : WholeV B IP IX → Bool) (k : Bool)
    (v : WholeV B IP IX) (target : IP) : Prop :=
  match v with
  | Sum.inr (Sum.inl p) =>
      Walk (Mono P.Arc (restrictPatch w) k) (Sum.inr p) (Sum.inr target) ∨
      ∃ b : B,
        Walk (Mono P.Arc (restrictPatch w) k) (Sum.inr p) (Sum.inl b) ∧
        Walk (Mono (GlueArc P X) w k) (Sum.inl b)
          (Sum.inr (Sum.inl target))
  | _ => True

theorem wholeWalk_to_patchPrivateNF {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {v : WholeV B IP IX} {target : IP}
    (p : Walk (Mono (GlueArc P X) w k) v
      (Sum.inr (Sum.inl target))) :
    ToPatchPrivateNF P X w k v target := by
  induction p with
  | edge e =>
      cases v with
      | inl _ => exact True.intro
      | inr v =>
          cases v with
          | inl q =>
              exact Or.inl (Walk.edge (wholeMono_patch_private_private e))
          | inr _ => exact True.intro
  | @cons x y z e rest ih =>
      cases x with
      | inl _ => exact True.intro
      | inr x =>
          cases x with
          | inl p0 =>
              change
                (Walk (Mono P.Arc (restrictPatch w) k)
                    (Sum.inr p0) (Sum.inr target) ∨
                 ∃ b : B,
                   Walk (Mono P.Arc (restrictPatch w) k)
                     (Sum.inr p0) (Sum.inl b) ∧
                   Walk (Mono (GlueArc P X) w k) (Sum.inl b)
                     (Sum.inr (Sum.inl target)))
              cases y with
              | inl b =>
                  have hEdge := wholeMono_patch_private_boundary e
                  exact Or.inr ⟨b, Walk.edge hEdge, rest⟩
              | inr y =>
                  cases y with
                  | inl q =>
                      have hEdge := wholeMono_patch_private_private e
                      change
                        (Walk (Mono P.Arc (restrictPatch w) k)
                            (Sum.inr q) (Sum.inr target) ∨
                         ∃ b : B,
                           Walk (Mono P.Arc (restrictPatch w) k)
                             (Sum.inr q) (Sum.inl b) ∧
                           Walk (Mono (GlueArc P X) w k) (Sum.inl b)
                             (Sum.inr (Sum.inl target))) at ih
                      cases ih with
                      | inl hLocal =>
                          exact Or.inl (Walk.cons hEdge hLocal)
                      | inr hSplit =>
                          cases hSplit with
                          | intro b hb =>
                              exact Or.inr ⟨b, Walk.cons hEdge hb.1, hb.2⟩
                  | inr _ =>
                      have hf := e.1
                      change False at hf
                      exact False.elim hf
          | inr _ => exact True.intro

/-- Symmetric normal form for a closed walk based at an exterior-private vertex. -/
def ToExteriorPrivateNF {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX)
    (w : WholeV B IP IX → Bool) (k : Bool)
    (v : WholeV B IP IX) (target : IX) : Prop :=
  match v with
  | Sum.inr (Sum.inr x) =>
      Walk (Mono X.Arc (restrictExterior w) k) (Sum.inr x) (Sum.inr target) ∨
      ∃ b : B,
        Walk (Mono X.Arc (restrictExterior w) k) (Sum.inr x) (Sum.inl b) ∧
        Walk (Mono (GlueArc P X) w k) (Sum.inl b)
          (Sum.inr (Sum.inr target))
  | _ => True

theorem wholeWalk_to_exteriorPrivateNF {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool}
    {v : WholeV B IP IX} {target : IX}
    (p : Walk (Mono (GlueArc P X) w k) v
      (Sum.inr (Sum.inr target))) :
    ToExteriorPrivateNF P X w k v target := by
  induction p with
  | edge e =>
      cases v with
      | inl _ => exact True.intro
      | inr v =>
          cases v with
          | inl _ => exact True.intro
          | inr y =>
              exact Or.inl (Walk.edge (wholeMono_exterior_private_private e))
  | @cons x y z e rest ih =>
      cases x with
      | inl _ => exact True.intro
      | inr x =>
          cases x with
          | inl _ => exact True.intro
          | inr x0 =>
              change
                (Walk (Mono X.Arc (restrictExterior w) k)
                    (Sum.inr x0) (Sum.inr target) ∨
                 ∃ b : B,
                   Walk (Mono X.Arc (restrictExterior w) k)
                     (Sum.inr x0) (Sum.inl b) ∧
                   Walk (Mono (GlueArc P X) w k) (Sum.inl b)
                     (Sum.inr (Sum.inr target)))
              cases y with
              | inl b =>
                  have hEdge := wholeMono_exterior_private_boundary e
                  exact Or.inr ⟨b, Walk.edge hEdge, rest⟩
              | inr y =>
                  cases y with
                  | inl _ =>
                      have hf := e.1
                      change False at hf
                      exact False.elim hf
                  | inr y0 =>
                      have hEdge := wholeMono_exterior_private_private e
                      change
                        (Walk (Mono X.Arc (restrictExterior w) k)
                            (Sum.inr y0) (Sum.inr target) ∨
                         ∃ b : B,
                           Walk (Mono X.Arc (restrictExterior w) k)
                             (Sum.inr y0) (Sum.inl b) ∧
                           Walk (Mono (GlueArc P X) w k) (Sum.inl b)
                             (Sum.inr (Sum.inr target))) at ih
                      cases ih with
                      | inl hLocal =>
                          exact Or.inl (Walk.cons hEdge hLocal)
                      | inr hSplit =>
                          cases hSplit with
                          | intro b hb =>
                              exact Or.inr ⟨b, Walk.cons hEdge hb.1, hb.2⟩

/-- Expand a cyclic chain of boundary-reachability entries to an actual positive
    monochromatic whole walk. -/
theorem boundaryUnionWalk_to_whole {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    {w : WholeV B IP IX → Bool} {k : Bool} {s t : B}
    (p : Walk (BoundaryUnion P X
      (restrictPatch w) (restrictExterior w) k) s t) :
    Walk (Mono (GlueArc P X) w k) (Sum.inl s) (Sum.inl t) := by
  apply walk_bind (p := p)
  intro a b h
  cases h with
  | inl hp =>
      exact patchWalk_to_whole (P := P) (X := X) hp
  | inr hx =>
      exact exteriorWalk_to_whole (P := P) (X := X) hx

/-- The raw C13 exact-glue theorem for the canonical typed union. -/
theorem exactGlue_raw {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    (w : WholeV B IP IX → Bool) :
    Good (GlueArc P X) w ↔
      Good P.Arc (restrictPatch w) ∧
      Good X.Arc (restrictExterior w) ∧
      CrossSafe P X (restrictPatch w) (restrictExterior w) := by
  constructor
  · intro hWhole
    constructor
    · intro k a hClosed
      exact hWhole k (patchVertex (IX := IX) a)
        (patchWalk_to_whole (P := P) (X := X) hClosed)
    · constructor
      · intro k a hClosed
        exact hWhole k (exteriorVertex (IP := IP) a)
          (exteriorWalk_to_whole (P := P) (X := X) hClosed)
      · intro k b hBoundaryClosed
        exact hWhole k (Sum.inl b)
          (boundaryUnionWalk_to_whole (P := P) (X := X) hBoundaryClosed)
  · intro hParts
    have hP := hParts.1
    have hX := hParts.2.1
    have hSafe := hParts.2.2
    intro k v hClosed
    cases v with
    | inl b =>
        have hNF := wholeWalk_to_boundaryNF
          (P := P) (X := X) (w := w) (k := k) (t := b) hClosed
        change Walk (BoundaryUnion P X
          (restrictPatch w) (restrictExterior w) k) b b at hNF
        exact hSafe k b hNF
    | inr v =>
        cases v with
        | inl p0 =>
            have hNF := wholeWalk_to_patchPrivateNF
              (P := P) (X := X) (w := w) (k := k)
              (target := p0) hClosed
            change
              (Walk (Mono P.Arc (restrictPatch w) k)
                  (Sum.inr p0) (Sum.inr p0) ∨
               ∃ b : B,
                 Walk (Mono P.Arc (restrictPatch w) k)
                   (Sum.inr p0) (Sum.inl b) ∧
                 Walk (Mono (GlueArc P X) w k) (Sum.inl b)
                   (Sum.inr (Sum.inl p0))) at hNF
            cases hNF with
            | inl hLocal =>
                exact hP k (Sum.inr p0) hLocal
            | inr hSplit =>
                cases hSplit with
                | intro b hb =>
                    have hPrefixWhole :=
                      patchWalk_to_whole (P := P) (X := X) hb.1
                    have hRotated :
                        Walk (Mono (GlueArc P X) w k) (Sum.inl b) (Sum.inl b) :=
                      walk_join hb.2 hPrefixWhole
                    have hBoundary := wholeWalk_to_boundaryNF
                      (P := P) (X := X) (w := w) (k := k)
                      (t := b) hRotated
                    change Walk (BoundaryUnion P X
                      (restrictPatch w) (restrictExterior w) k) b b at hBoundary
                    exact hSafe k b hBoundary
        | inr x0 =>
            have hNF := wholeWalk_to_exteriorPrivateNF
              (P := P) (X := X) (w := w) (k := k)
              (target := x0) hClosed
            change
              (Walk (Mono X.Arc (restrictExterior w) k)
                  (Sum.inr x0) (Sum.inr x0) ∨
               ∃ b : B,
                 Walk (Mono X.Arc (restrictExterior w) k)
                   (Sum.inr x0) (Sum.inl b) ∧
                 Walk (Mono (GlueArc P X) w k) (Sum.inl b)
                   (Sum.inr (Sum.inr x0))) at hNF
            cases hNF with
            | inl hLocal =>
                exact hX k (Sum.inr x0) hLocal
            | inr hSplit =>
                cases hSplit with
                | intro b hb =>
                    have hPrefixWhole :=
                      exteriorWalk_to_whole (P := P) (X := X) hb.1
                    have hRotated :
                        Walk (Mono (GlueArc P X) w k) (Sum.inl b) (Sum.inl b) :=
                      walk_join hb.2 hPrefixWhole
                    have hBoundary := wholeWalk_to_boundaryNF
                      (P := P) (X := X) (w := w) (k := k)
                      (t := b) hRotated
                    change Walk (BoundaryUnion P X
                      (restrictPatch w) (restrictExterior w) k) b b at hBoundary
                    exact hSafe k b hBoundary

/-- ExactGlue is no longer an assumption: it is the proved raw C13 criterion. -/
def ExactGlue {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : Prop :=
  ∀ w : WholeV B IP IX → Bool,
    Good (GlueArc P X) w ↔
      Good P.Arc (restrictPatch w) ∧
      Good X.Arc (restrictExterior w) ∧
      CrossSafe P X (restrictPatch w) (restrictExterior w)

theorem exactGlue_proved {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : ExactGlue P X := by
  intro w
  exact exactGlue_raw (P := P) (X := X) w

/-- Source-facing version: the raw theorem plus an explicit reverse-guard
    applicability contract. -/
theorem exactGlue_of_contract {B IP IX : Type u}
    {P : Piece B IP} {X : Piece B IX}
    (_hContract : GlueContract P X) : ExactGlue P X :=
  exactGlue_proved P X

/-- Same-boundary colouring agreement. -/
def BoundaryAgree {B I J : Type u}
    (cP : PieceV B I → Bool) (cQ : PieceV B J → Bool) : Prop :=
  ∀ b : B, cP (Sum.inl b) = cQ (Sum.inl b)

/-- All-valid-Q strong profile lifting. -/
def StrongLift {B IP IQ : Type u}
    (P : Piece B IP) (Q : Piece B IQ) : Prop :=
  ∀ d : PieceV B IQ → Bool, Good Q.Arc d →
    ∃ c : PieceV B IP → Bool,
      Good P.Arc c ∧
      BoundaryAgree c d ∧
      (∀ k : Bool, ∀ s t : B,
        RPlus P c k s t → RPlus Q d k s t)

/-- Monotonicity of C13 cross-safety under the strong-profile relation. -/
theorem crossSafe_mono {B IP IQ IX : Type u}
    {P : Piece B IP} {Q : Piece B IQ} {X : Piece B IX}
    {cP : PieceV B IP → Bool}
    {cQ : PieceV B IQ → Bool}
    {cX : PieceV B IX → Bool}
    (hIncl : ∀ k : Bool, ∀ s t : B,
      RPlus P cP k s t → RPlus Q cQ k s t)
    (hSafe : CrossSafe Q X cQ cX) :
    CrossSafe P X cP cX := by
  intro k b hClosed
  apply hSafe k b
  apply walk_map (p := hClosed)
  intro s t hst
  cases hst with
  | inl hP => exact Or.inl (hIncl k s t hP)
  | inr hX => exact Or.inr hX

/-- Glue local colourings, taking the exterior colour on the shared boundary. -/
def glueColor {B IP IX : Type u}
    (cP : PieceV B IP → Bool) (cX : PieceV B IX → Bool) :
    WholeV B IP IX → Bool
  | Sum.inl b => cX (Sum.inl b)
  | Sum.inr (Sum.inl p) => cP (Sum.inr p)
  | Sum.inr (Sum.inr x) => cX (Sum.inr x)

theorem restrictPatch_glueColor {B IP IX : Type u}
    {cP : PieceV B IP → Bool} {cX : PieceV B IX → Bool}
    (h : BoundaryAgree cP cX) :
    restrictPatch (glueColor cP cX) = cP := by
  funext v
  cases v with
  | inl b => exact Eq.symm (h b)
  | inr p => rfl

theorem restrictExterior_glueColor {B IP IX : Type u}
    (cP : PieceV B IP → Bool) (cX : PieceV B IX → Bool) :
    restrictExterior (glueColor cP cX) = cX := by
  funext v
  cases v <;> rfl

structure State where
  V : Type u
  Good : (V → Bool) → Prop

structure Embedding (A : Type u) (G : State.{u}) where
  toFun : A → G.V
  injective : Function.Injective toFun

def AgreeOn {A : Type u} {G H : State.{u}}
    (iG : Embedding A G) (iH : Embedding A H)
    (cG : G.V → Bool) (cH : H.V → Bool) : Prop :=
  ∀ a : A, cG (iG.toFun a) = cH (iH.toFun a)

def GoodLiftOn {A : Type u} (G H : State.{u})
    (iG : Embedding A G) (iH : Embedding A H) : Prop :=
  ∀ d : H.V → Bool, H.Good d →
    ∃ c : G.V → Bool, G.Good c ∧ AgreeOn iG iH c d

def GlueState {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : State.{u} where
  V := WholeV B IP IX
  Good := fun c => Good (GlueArc P X) c

def exteriorEmbedding {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) :
    Embedding (PieceV B IX) (GlueState P X) where
  toFun := exteriorVertex (IP := IP)
  injective := by
    intro a b h
    cases a with
    | inl a =>
        cases b with
        | inl b => cases h; rfl
        | inr _ => cases h
    | inr a =>
        cases b with
        | inl _ => cases h
        | inr b => cases h; rfl

/-- Cycle-5 theorem retained verbatim at the logical level, but ExactGlue can now
    be discharged by `exactGlue_proved` rather than supplied as an external
    dependency. -/
theorem strongLift_exactGlue_to_goodLiftOn
    {B IP IQ IX : Type u}
    {P : Piece B IP} {Q : Piece B IQ} {X : Piece B IX}
    (hLift : StrongLift P Q)
    (hExactP : ExactGlue P X)
    (hExactQ : ExactGlue Q X) :
    GoodLiftOn
      (GlueState P X) (GlueState Q X)
      (exteriorEmbedding P X) (exteriorEmbedding Q X) := by
  intro d hd
  have hQparts :
      Good Q.Arc (restrictPatch d) ∧
      Good X.Arc (restrictExterior d) ∧
      CrossSafe Q X (restrictPatch d) (restrictExterior d) :=
    (hExactQ d).mp hd
  cases hLift (restrictPatch d) hQparts.1 with
  | intro cP hc =>
      have hcP := hc.1
      have hB := hc.2.1
      have hIncl := hc.2.2
      have hPX : BoundaryAgree cP (restrictExterior d) := by
        intro b
        exact hB b
      let c : WholeV B IP IX → Bool := glueColor cP (restrictExterior d)
      have hRestrP : restrictPatch c = cP :=
        restrictPatch_glueColor hPX
      have hRestrX : restrictExterior c = restrictExterior d :=
        restrictExterior_glueColor cP (restrictExterior d)
      have hSafeP : CrossSafe P X cP (restrictExterior d) :=
        crossSafe_mono hIncl hQparts.2.2
      have hGood : Good (GlueArc P X) c := by
        apply (hExactP c).mpr
        constructor
        · rw [hRestrP]
          exact hcP
        · constructor
          · rw [hRestrX]
            exact hQparts.2.1
          · rw [hRestrP, hRestrX]
            exact hSafeP
      refine ⟨c, hGood, ?_⟩
      intro x
      cases x <;> rfl

/-- Cycle-7 closed bridge: raw C13 exact glue is proved internally.  The guard
    hypotheses are retained as source/class applicability gates, not as hidden
    proof axioms. -/
theorem strongLift_concreteGlue_to_goodLiftOn
    {B IP IQ IX : Type u}
    {P : Piece B IP} {Q : Piece B IQ} {X : Piece B IX}
    (hLift : StrongLift P Q)
    (hContractP : GlueContract P X)
    (hContractQ : GlueContract Q X) :
    GoodLiftOn
      (GlueState P X) (GlueState Q X)
      (exteriorEmbedding P X) (exteriorEmbedding Q X) :=
  strongLift_exactGlue_to_goodLiftOn hLift
    (exactGlue_of_contract hContractP)
    (exactGlue_of_contract hContractQ)

end OPG169.S11Cycle7

#print axioms OPG169.S11Cycle7.walk_join
#print axioms OPG169.S11Cycle7.walk_bind
#print axioms OPG169.S11Cycle7.reverseGuardFailure_gives_digon
#print axioms OPG169.S11Cycle7.wholeWalk_to_boundaryNF
#print axioms OPG169.S11Cycle7.exactGlue_raw
#print axioms OPG169.S11Cycle7.exactGlue_proved
#print axioms OPG169.S11Cycle7.strongLift_exactGlue_to_goodLiftOn
#print axioms OPG169.S11Cycle7.strongLift_concreteGlue_to_goodLiftOn
