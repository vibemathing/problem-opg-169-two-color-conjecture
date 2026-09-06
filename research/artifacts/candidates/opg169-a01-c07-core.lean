import Init

/- Unexecuted source input for ToolPlan C07.
   Verdict: candidate_only. This file does not formalize the whole graph theorem.
   The predicate BothNeighbourColours records only necessary local witnesses
   of two blocked colors, not a definition of an actual monochromatic cycle. -/

universe u

namespace OPG169.C07

def Oriented {V : Type u} (arc : V → V → Prop) : Prop :=
  ∀ x y, arc x y → Not (arc y x)

def Neighbour {V : Type u} (arc : V → V → Prop) (v w : V) : Prop :=
  arc v w ∨ arc w v

def BothNeighbourColours {V : Type u}
    (arc : V → V → Prop) (colour : V → Bool) (v : V) : Prop :=
  ∀ b : Bool, ∃ i o : V,
    arc i v ∧ arc v o ∧ colour i = b ∧ colour o = b

def FourDistinctNeighbours {V : Type u}
    (arc : V → V → Prop) (v : V) : Prop :=
  ∃ a b c d : V,
    Neighbour arc v a ∧ Neighbour arc v b ∧
    Neighbour arc v c ∧ Neighbour arc v d ∧
    a ≠ b ∧ a ≠ c ∧ a ≠ d ∧
    b ≠ c ∧ b ≠ d ∧ c ≠ d

theorem differentColours_ne {V : Type u} {colour : V → Bool}
    {x y : V} (hx : colour x = false) (hy : colour y = true) :
    x ≠ y := by
  intro e
  have impossible : false = true :=
    Eq.trans (Eq.symm hx) (Eq.trans (congrArg colour e) hy)
  cases impossible

theorem inOut_ne {V : Type u} {arc : V → V → Prop}
    {v i o : V} (hO : Oriented arc)
    (hi : arc i v) (ho : arc v o) : i ≠ o := by
  intro e
  subst o
  exact hO i v hi ho

theorem neighbour_ne_centre {V : Type u} {arc : V → V → Prop}
    {v w : V} (hO : Oriented arc) (hw : Neighbour arc v w) :
    w ≠ v := by
  intro e
  subst w
  cases hw with
  | inl h => exact hO v v h h
  | inr h => exact hO v v h h

theorem twoInTwoOut_of_bothColours {V : Type u}
    {arc : V → V → Prop} {colour : V → Bool} {v : V}
    (hb : BothNeighbourColours arc colour v) :
    ∃ i0 i1 o0 o1 : V,
      arc i0 v ∧ arc i1 v ∧ arc v o0 ∧ arc v o1 ∧
      i0 ≠ i1 ∧ o0 ≠ o1 :=
  match hb false, hb true with
  | ⟨i0, o0, hi0, ho0, ci0, co0⟩,
    ⟨i1, o1, hi1, ho1, ci1, co1⟩ =>
    ⟨i0, i1, o0, o1, hi0, hi1, ho0, ho1,
      differentColours_ne (colour := colour) ci0 ci1, differentColours_ne (colour := colour) co0 co1⟩

theorem fourDistinct_of_bothColours {V : Type u}
    {arc : V → V → Prop} {colour : V → Bool} {v : V}
    (hO : Oriented arc) (hb : BothNeighbourColours arc colour v) :
    FourDistinctNeighbours arc v :=
  match hb false, hb true with
  | ⟨i0, o0, hi0, ho0, ci0, co0⟩,
    ⟨i1, o1, hi1, ho1, ci1, co1⟩ =>
    ⟨i0, o0, i1, o1, Or.inr hi0, Or.inl ho0, Or.inr hi1, Or.inl ho1,
      inOut_ne hO hi0 ho0,
      differentColours_ne (colour := colour) ci0 ci1, differentColours_ne (colour := colour) ci0 co1,
      differentColours_ne (colour := colour) co0 ci1, differentColours_ne (colour := colour) co0 co1,
      inOut_ne hO hi1 ho1⟩

theorem not_bothColours_of_no_four {V : Type u}
    {arc : V → V → Prop} {colour : V → Bool} {v : V}
    (hO : Oriented arc) (hn : Not (FourDistinctNeighbours arc v)) :
    Not (BothNeighbourColours arc colour v) :=
  fun hb => hn (fourDistinct_of_bothColours hO hb)

end OPG169.C07

#print axioms OPG169.C07.differentColours_ne
#print axioms OPG169.C07.inOut_ne
#print axioms OPG169.C07.neighbour_ne_centre
#print axioms OPG169.C07.twoInTwoOut_of_bothColours
#print axioms OPG169.C07.fourDistinct_of_bothColours
#print axioms OPG169.C07.not_bothColours_of_no_four
