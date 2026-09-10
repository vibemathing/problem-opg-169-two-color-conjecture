import Init

/-!
R08 / OPG-169 / S11 Cycle 5
Concrete StrongLift + ExactGlue -> GoodLiftOn bridge.

Candidate source only. NOT kernel-checked at generation time because the
runtime has no Lean toolchain.

Scope is deliberately narrow:
* concrete positive monochromatic boundary reachability `RPlus`;
* canonical typed patch/exterior union, so hidden private-to-private contacts
  are unrepresentable in this model;
* `ExactGlue` is exactly the C13 boundary-automaton iff contract for that union;
* the bridge from all-Q strong profile inclusion to an exterior-fixed whole lift.

Out of scope: proving the C13 ExactGlue criterion from raw walk cutting,
planarity, rotations, reverse guards, source ownership, strict descent,
minimum-counterexample membership, and multi-patch composition.

`B` is the actual boundary type after source-valid alias quotienting.
-/

universe u

namespace OPG169.S11Cycle5

/-- Positive walk: there is deliberately no empty/reflexive constructor. -/
inductive Walk {V : Type u} (R : V → V → Prop) : V → V → Prop where
  | edge {x y : V} : R x y → Walk R x y
  | join {x y z : V} : Walk R x y → Walk R y z → Walk R x z

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

/-- Positive walks are monotone under pointwise relation inclusion. -/
theorem walk_map {V : Type u} {R S : V → V → Prop}
    (h : ∀ {a b : V}, R a b → S a b)
    {x y : V} (p : Walk R x y) : Walk S x y := by
  induction p with
  | edge e =>
      exact Walk.edge (h e)
  | join p q ihp ihq =>
      exact Walk.join ihp ihq

abbrev PieceV (B I : Type u) := Sum B I
abbrev WholeV (B IP IX : Type u) := Sum B (Sum IP IX)

/-- A patch/piece with a canonical boundary summand `B` and private interior `I`. -/
structure Piece (B I : Type u) where
  Arc : PieceV B I → PieceV B I → Prop

/-- Canonical embedding of a patch vertex into a whole patch/exterior union. -/
def patchVertex {B IP IX : Type u} :
    PieceV B IP → WholeV B IP IX
  | Sum.inl b => Sum.inl b
  | Sum.inr p => Sum.inr (Sum.inl p)

/-- Canonical embedding of an exterior vertex into a whole patch/exterior union. -/
def exteriorVertex {B IP IX : Type u} :
    PieceV B IX → WholeV B IP IX
  | Sum.inl b => Sum.inl b
  | Sum.inr x => Sum.inr (Sum.inr x)

/-- Exact typed union relation.  The sum types make the two private interiors
    disjoint and allow contact only through the common `B` summand.
    Shared boundary arcs are simply unioned as propositions. -/
inductive GlueArc {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) :
    WholeV B IP IX → WholeV B IP IX → Prop where
  | patch {a b : PieceV B IP} :
      P.Arc a b →
      GlueArc P X (patchVertex (IX := IX) a) (patchVertex (IX := IX) b)
  | exterior {a b : PieceV B IX} :
      X.Arc a b →
      GlueArc P X (exteriorVertex (IP := IP) a) (exteriorVertex (IP := IP) b)

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

/-- Actual-boundary colour agreement. -/
def BoundaryAgree {B I J : Type u}
    (cP : PieceV B I → Bool) (cQ : PieceV B J → Bool) : Prop :=
  ∀ b : B, cP (Sum.inl b) = cQ (Sum.inl b)

/-- Concrete positive monochromatic boundary reachability.
    Paths may pass through other boundary vertices.  `s != t` prevents
    accidental reflexive/zero-length interface entries. -/
def RPlus {B I : Type u} (P : Piece B I)
    (c : PieceV B I → Bool) (k : Bool) (s t : B) : Prop :=
  s ≠ t ∧
  Walk (Mono P.Arc c k) (Sum.inl s) (Sum.inl t)

/-- All-Q strong lifting profile. -/
def StrongLift {B IP IQ : Type u}
    (P : Piece B IP) (Q : Piece B IQ) : Prop :=
  ∀ d : PieceV B IQ → Bool, Good Q.Arc d →
    ∃ c : PieceV B IP → Bool,
      Good P.Arc c ∧
      BoundaryAgree c d ∧
      (∀ k : Bool, ∀ s t : B,
        RPlus P c k s t → RPlus Q d k s t)

/-- C13 crossing-safety condition for one patch and one exterior.
    A bad witness is a nonempty closed boundary walk alternating arbitrarily
    among positive relation entries supplied by the two pieces. -/
def CrossSafe {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX)
    (cP : PieceV B IP → Bool) (cX : PieceV B IX → Bool) : Prop :=
  ∀ k : Bool, ∀ b : B,
    Not (Walk
      (fun s t : B => RPlus P cP k s t ∨ RPlus X cX k s t)
      b b)

/-- `ExactGlue` is exactly the C13 boundary-automaton iff contract for the
    canonical typed union above.  Cycle 5 consumes this criterion; it does not
    re-prove C13's cycle-cutting theorem. -/
def ExactGlue {B IP IX : Type u}
    (P : Piece B IP) (X : Piece B IX) : Prop :=
  ∀ w : WholeV B IP IX → Bool,
    Good (GlueArc P X) w ↔
      Good P.Arc (restrictPatch w) ∧
      Good X.Arc (restrictExterior w) ∧
      CrossSafe P X (restrictPatch w) (restrictExterior w)

/-- Glue two local colourings, taking the exterior copy on the common boundary.
    A separate `BoundaryAgree` hypothesis makes the patch restriction equal to
    the requested patch colouring. -/
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
  | inl b =>
      exact Eq.symm (h b)
  | inr p =>
      rfl

theorem restrictExterior_glueColor {B IP IX : Type u}
    (cP : PieceV B IP → Bool) (cX : PieceV B IX → Bool) :
    restrictExterior (glueColor cP cX) = cX := by
  funext v
  cases v with
  | inl b => rfl
  | inr x => rfl

/-- Monotonicity of the C13 boundary safety test in the patch relation. -/
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
  | inl hP =>
      exact Or.inl (hIncl k s t hP)
  | inr hX =>
      exact Or.inr hX

/-- Minimal state wrapper used only to state `GoodLiftOn`. -/
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

/-- Every valid colouring of `H` lifts to a valid colouring of `G` while
    preserving the full named core `A`. -/
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
        | inl b =>
            cases h
            rfl
        | inr b =>
            cases h
    | inr a =>
        cases b with
        | inl b =>
            cases h
        | inr b =>
            cases h
            rfl

/-- Cycle-5 target theorem.

    Every valid colouring of the smaller exact union `Q ∪ X` restricts to a
    valid complete `Q` colouring.  StrongLift supplies a valid `P` colouring
    with the same actual boundary colours and `RPlus_P ⊆ RPlus_Q` for both
    colours.  C13 crossing safety is monotone under that inclusion, so the
    glued `P ∪ X` colouring is valid.  Every exterior vertex, including every
    boundary vertex, keeps exactly its original colour. -/
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
  | intro cP hcP =>
      have hPX : BoundaryAgree cP (restrictExterior d) := by
        intro b
        exact hcP.2.1 b
      let c : WholeV B IP IX → Bool :=
        glueColor cP (restrictExterior d)
      have hRestrP : restrictPatch c = cP := by
        exact restrictPatch_glueColor hPX
      have hRestrX : restrictExterior c = restrictExterior d := by
        exact restrictExterior_glueColor cP (restrictExterior d)
      have hSafeP : CrossSafe P X cP (restrictExterior d) :=
        crossSafe_mono hcP.2.2 hQparts.2.2
      have hGood : Good (GlueArc P X) c := by
        apply (hExactP c).mpr
        constructor
        · rw [hRestrP]
          exact hcP.1
        · constructor
          · rw [hRestrX]
            exact hQparts.2.1
          · rw [hRestrP, hRestrX]
            exact hSafeP
      refine ⟨c, hGood, ?_⟩
      intro x
      cases x with
      | inl b => rfl
      | inr z => rfl

end OPG169.S11Cycle5

#print axioms OPG169.S11Cycle5.walk_map
#print axioms OPG169.S11Cycle5.crossSafe_mono
#print axioms OPG169.S11Cycle5.strongLift_exactGlue_to_goodLiftOn
