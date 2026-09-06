import Init

/- C08: unexecuted positive-walk and vertex-extension source candidate.
   Verdict: candidate_only.
   Target binding: obligation:opg169-strong-min-degree-three.
   Walk has no empty constructor. No Lean execution is reported. -/

universe u

namespace OPG169.C08

inductive Walk {V : Type u} (R : V → V → Prop) : V → V → Prop where
  | edge {x y : V} : R x y → Walk R x y
  | join {x y z : V} : Walk R x y → Walk R y z → Walk R x z

def Acyclic {V : Type u} (R : V → V → Prop) : Prop :=
  ∀ x, Not (Walk R x x)

def Delete {V : Type u} (R : V → V → Prop) (v x y : V) : Prop :=
  R x y ∧ x ≠ v ∧ y ≠ v

def Mono {V : Type u} (R : V → V → Prop)
    (c : V → Bool) (b : Bool) (x y : V) : Prop :=
  R x y ∧ c x = b ∧ c y = b

def Good {V : Type u} (R : V → V → Prop) (c : V → Bool) : Prop :=
  ∀ b : Bool, Acyclic (Mono R c b)

def Bad {V : Type u} (R : V → V → Prop) (c : V → Bool) : Prop :=
  ∃ b : Bool, ∃ x : V, Walk (Mono R c b) x x

def Recolour {V : Type u} [DecidableEq V]
    (c : V → Bool) (v : V) (b : Bool) (x : V) : Bool :=
  if x = v then b else c x

def Oriented {V : Type u} (R : V → V → Prop) : Prop :=
  ∀ x y, R x y → Not (R y x)

def Neighbour {V : Type u} (R : V → V → Prop) (v w : V) : Prop :=
  R v w ∨ R w v

def BothNeighbourColours {V : Type u}
    (R : V → V → Prop) (c : V → Bool) (v : V) : Prop :=
  ∀ b : Bool, ∃ i o : V, R i v ∧ R v o ∧ c i = b ∧ c o = b

def FourDistinctNeighbours {V : Type u}
    (R : V → V → Prop) (v : V) : Prop :=
  ∃ a b c d : V,
    Neighbour R v a ∧ Neighbour R v b ∧
    Neighbour R v c ∧ Neighbour R v d ∧
    a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d

theorem walk_map {V : Type u} {R S : V → V → Prop}
    (h : ∀ {a b : V}, R a b → S a b)
    {x y : V} (p : Walk R x y) : Walk S x y := by
  induction p with
  | edge e => exact Walk.edge (h e)
  | join p q ihp ihq => exact Walk.join ihp ihq

theorem first_edge {V : Type u} {R : V → V → Prop}
    {x y : V} (p : Walk R x y) : ∃ o : V, R x o := by
  induction p with
  | edge e => exact ⟨_, e⟩
  | join p q ihp ihq => exact ihp

theorem last_edge {V : Type u} {R : V → V → Prop}
    {x y : V} (p : Walk R x y) : ∃ i : V, R i y := by
  induction p with
  | edge e => exact ⟨_, e⟩
  | join p q ihp ihq => exact ihq

theorem avoid_or_visit {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {v x y : V} (p : Walk R x y) :
    x ≠ v → y ≠ v →
    Walk (Delete R v) x y ∨ (Walk R x v ∧ Walk R v y) := by
  induction p with
  | edge e =>
    intro hx hy
    exact Or.inl (Walk.edge ⟨e, hx, hy⟩)
  | @join x m y p q ihp ihq =>
    intro hx hy
    by_cases hm : m = v
    · subst m
      exact Or.inr ⟨p, q⟩
    · cases ihp hx hm with
      | inr hv =>
        exact Or.inr ⟨hv.1, Walk.join hv.2 q⟩
      | inl ha =>
        cases ihq hm hy with
        | inl hb => exact Or.inl (Walk.join ha hb)
        | inr hv => exact Or.inr ⟨Walk.join p hv.1, hv.2⟩

theorem localize_closed_walk {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {v x : V}
    (hd : Acyclic (Delete R v)) (p : Walk R x x) : Walk R v v := by
  by_cases hx : x = v
  · subst x
    exact p
  · cases avoid_or_visit p hx hx with
    | inl hp => exact False.elim (hd x hp)
    | inr hp => exact Walk.join hp.2 hp.1

theorem recolour_on {V : Type u} [DecidableEq V]
    (c : V → Bool) (v : V) (b : Bool) :
    Recolour c v b v = b := by
  unfold Recolour
  exact if_pos rfl

theorem recolour_off {V : Type u} [DecidableEq V]
    (c : V → Bool) (v : V) (b : Bool) {x : V} (hx : x ≠ v) :
    Recolour c v b x = c x := by
  unfold Recolour
  exact if_neg hx

theorem deleted_mono_map {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {c : V → Bool} {v : V} {b k : Bool}
    {x y : V} (h : Delete (Mono R (Recolour c v b) k) v x y) :
    Mono (Delete R v) c k x y := by
  exact ⟨⟨h.1.1, h.2.1, h.2.2⟩,
    Eq.trans (Eq.symm (recolour_off c v b h.2.1)) h.1.2.1,
    Eq.trans (Eq.symm (recolour_off c v b h.2.2)) h.1.2.2⟩

theorem acyclic_recoloured_deleted {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {c : V → Bool} {v : V} {b k : Bool}
    (hg : Good (Delete R v) c) :
    Acyclic (Delete (Mono R (Recolour c v b) k) v) := by
  intro x p
  exact hg k x (walk_map (fun h => deleted_mono_map h) p)

theorem neighbours_of_failed_extension {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {c : V → Bool} {v : V} {b : Bool}
    (hO : Oriented R) (hg : Good (Delete R v) c)
    (hb : Bad R (Recolour c v b)) :
    ∃ i o : V, R i v ∧ R v o ∧ c i = b ∧ c o = b := by
  cases hb with
  | intro k hk =>
    cases hk with
    | intro x p =>
      have q : Walk (Mono R (Recolour c v b) k) v v :=
        localize_closed_walk (acyclic_recoloured_deleted hg) p
      cases first_edge q with
      | intro o ho =>
        cases last_edge q with
        | intro i hi =>
          have hkb : k = b :=
            Eq.trans (Eq.symm ho.2.1) (recolour_on c v b)
          have hiv : i ≠ v := by
            intro e
            have loop : R v v := e ▸ hi.1
            exact hO v v loop loop
          have hov : o ≠ v := by
            intro e
            have loop : R v v := e ▸ ho.1
            exact hO v v loop loop
          exact ⟨i, o, hi.1, ho.1,
            Eq.trans (Eq.symm (recolour_off c v b hiv))
              (Eq.trans hi.2.1 hkb),
            Eq.trans (Eq.symm (recolour_off c v b hov))
              (Eq.trans ho.2.2 hkb)⟩

theorem witness_of_not_good {V : Type u}
    {R : V → V → Prop} {c : V → Bool} (h : Not (Good R c)) :
    Bad R c := by
  apply Classical.byContradiction
  intro hn
  apply h
  intro b x hw
  exact hn ⟨b, x, hw⟩

theorem bothNeighbours_of_no_good_extension {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {c : V → Bool} {v : V}
    (hO : Oriented R) (hg : Good (Delete R v) c)
    (hf : ∀ b : Bool, Not (Good R (Recolour c v b))) :
    BothNeighbourColours R c v := by
  intro b
  exact neighbours_of_failed_extension hO hg (witness_of_not_good (hf b))

theorem differentColours_ne {V : Type u} {c : V → Bool}
    {x y : V} (hx : c x = false) (hy : c y = true) : x ≠ y := by
  intro e
  have impossible : false = true :=
    Eq.trans (Eq.symm hx) (Eq.trans (congrArg c e) hy)
  cases impossible

theorem inOut_ne {V : Type u} {R : V → V → Prop}
    {v i o : V} (hO : Oriented R) (hi : R i v) (ho : R v o) :
    i ≠ o := by
  intro e
  subst o
  exact hO i v hi ho

theorem fourDistinct_of_bothColours {V : Type u}
    {R : V → V → Prop} {c : V → Bool} {v : V}
    (hO : Oriented R) (hb : BothNeighbourColours R c v) :
    FourDistinctNeighbours R v :=
  match hb false, hb true with
  | ⟨i0, o0, hi0, ho0, ci0, co0⟩,
    ⟨i1, o1, hi1, ho1, ci1, co1⟩ =>
    ⟨i0, o0, i1, o1, Or.inr hi0, Or.inl ho0, Or.inr hi1, Or.inl ho1,
      inOut_ne hO hi0 ho0,
      differentColours_ne (c := c) ci0 ci1,
      differentColours_ne (c := c) ci0 co1,
      differentColours_ne (c := c) co0 ci1,
      differentColours_ne (c := c) co0 co1,
      inOut_ne hO hi1 ho1⟩

theorem goodExtension_of_no_four {V : Type u} [DecidableEq V]
    {R : V → V → Prop} {c : V → Bool} {v : V}
    (hO : Oriented R) (hg : Good (Delete R v) c)
    (hn : Not (FourDistinctNeighbours R v)) :
    ∃ b : Bool, Good R (Recolour c v b) := by
  apply Classical.byContradiction
  intro hf
  have hb : BothNeighbourColours R c v :=
    bothNeighbours_of_no_good_extension hO hg (fun b h => hf ⟨b, h⟩)
  exact hn (fourDistinct_of_bothColours hO hb)

end OPG169.C08

#print axioms OPG169.C08.avoid_or_visit
#print axioms OPG169.C08.localize_closed_walk
#print axioms OPG169.C08.neighbours_of_failed_extension
#print axioms OPG169.C08.witness_of_not_good
#print axioms OPG169.C08.bothNeighbours_of_no_good_extension
#print axioms OPG169.C08.goodExtension_of_no_four
