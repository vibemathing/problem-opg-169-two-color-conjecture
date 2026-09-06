import «opg169-a01-c08-cycle-localization»

/- Unexecuted C08 companion, revision 2; verdict: candidate_only.
   This replaces the proposed c08-scc-bridge.lean as the selected companion.
   Static correction: the Good hypothesis in good_of_cut takes the coloring
   inside the binder; the earlier text contained one extra closing parenthesis.
   No compiler was run. Replay requires the exact C08 imported source to be
   built first and its directory added to the module search path.
   Main scope is proper-induced criticality, not the root conjecture. -/

universe u

namespace OPG169.C08Cut

open OPG169.C08

def Restrict {V : Type u} (R : V → V → Prop)
    (S : V → Prop) (x y : V) : Prop :=
  R x y ∧ S x ∧ S y

def Reach {V : Type u} (R : V → V → Prop) (x y : V) : Prop :=
  x = y ∨ Walk R x y

def Mix {V : Type u} (S : V → Prop) [DecidablePred S]
    (a b : V → Bool) (x : V) : Bool :=
  if S x then a x else b x

def ProperColorings {V : Type u} (R : V → V → Prop) : Prop :=
  ∀ S : V → Prop, (∃ x : V, Not (S x)) →
    ∃ c : V → Bool, Good (Restrict R S) c

theorem walk_restrict_forward {V : Type u}
    {R : V → V → Prop} {S : V → Prop}
    (h : ∀ {a b : V}, R a b → S a → S b)
    {x y : V} (p : Walk R x y) :
    S x → S y ∧ Walk (Restrict R S) x y := by
  induction p with
  | edge e =>
    intro hx
    have hy := h e hx
    exact ⟨hy, Walk.edge ⟨e, hx, hy⟩⟩
  | join p q ihp ihq =>
    intro hx
    have hp := ihp hx
    have hq := ihq hp.1
    exact ⟨hq.1, Walk.join hp.2 hq.2⟩

theorem walk_restrict_backward {V : Type u}
    {R : V → V → Prop} {S : V → Prop}
    (h : ∀ {a b : V}, R a b → S b → S a)
    {x y : V} (p : Walk R x y) :
    S y → S x ∧ Walk (Restrict R S) x y := by
  induction p with
  | edge e =>
    intro hy
    have hx := h e hy
    exact ⟨hx, Walk.edge ⟨e, hx, hy⟩⟩
  | join p q ihp ihq =>
    intro hy
    have hq := ihq hy
    have hp := ihp hq.1
    exact ⟨hp.1, Walk.join hp.2 hq.2⟩

theorem acyclic_of_cut {V : Type u}
    {R : V → V → Prop} {S : V → Prop} [DecidablePred S]
    (hc : ∀ {a b : V}, R a b → S a → S b)
    (ha : Acyclic (Restrict R S))
    (hb : Acyclic (Restrict R (fun x => Not (S x)))) : Acyclic R := by
  intro x p
  by_cases hx : S x
  · exact ha x ((walk_restrict_forward hc p) hx).2
  · have hback : ∀ {a b : V}, R a b → Not (S b) → Not (S a) :=
      fun e hn hs => hn (hc e hs)
    exact hb x ((walk_restrict_backward hback p) hx).2

theorem mix_on {V : Type u} (S : V → Prop) [DecidablePred S]
    (a b : V → Bool) {x : V} (hx : S x) : Mix S a b x = a x := by
  unfold Mix
  exact if_pos hx

theorem mix_off {V : Type u} (S : V → Prop) [DecidablePred S]
    (a b : V → Bool) {x : V} (hx : Not (S x)) : Mix S a b x = b x := by
  unfold Mix
  exact if_neg hx

theorem mono_on_map {V : Type u}
    {R : V → V → Prop} {S : V → Prop} [DecidablePred S]
    {a b : V → Bool} {k : Bool} {x y : V}
    (h : Restrict (Mono R (Mix S a b) k) S x y) :
    Mono (Restrict R S) a k x y := by
  exact ⟨⟨h.1.1, h.2.1, h.2.2⟩,
    Eq.trans (Eq.symm (mix_on S a b h.2.1)) h.1.2.1,
    Eq.trans (Eq.symm (mix_on S a b h.2.2)) h.1.2.2⟩

theorem mono_off_map {V : Type u}
    {R : V → V → Prop} {S : V → Prop} [DecidablePred S]
    {a b : V → Bool} {k : Bool} {x y : V}
    (h : Restrict (Mono R (Mix S a b) k) (fun z => Not (S z)) x y) :
    Mono (Restrict R (fun z => Not (S z))) b k x y := by
  exact ⟨⟨h.1.1, h.2.1, h.2.2⟩,
    Eq.trans (Eq.symm (mix_off S a b h.2.1)) h.1.2.1,
    Eq.trans (Eq.symm (mix_off S a b h.2.2)) h.1.2.2⟩

theorem good_of_cut {V : Type u}
    {R : V → V → Prop} {S : V → Prop} [DecidablePred S]
    {a b : V → Bool}
    (hc : ∀ {x y : V}, R x y → S x → S y)
    (ha : Good (Restrict R S) a)
    (hb : Good (Restrict R (fun x => Not (S x))) b) :
    Good R (Mix S a b) := by
  intro k
  apply acyclic_of_cut (S := S)
  · exact fun h hx => hc h.1 hx
  · intro x p
    exact ha k x (walk_map (fun h => mono_on_map h) p)
  · intro x p
    exact hb k x (walk_map (fun h => mono_off_map h) p)

theorem strong_of_proper_colorings {V : Type u}
    {R : V → V → Prop}
    (hbad : Not (∃ c : V → Bool, Good R c))
    (hp : ProperColorings R) : ∀ u v : V, Reach R u v := by
  classical
  intro u v
  apply Classical.byContradiction
  intro hn
  let S : V → Prop := Reach R u
  have hc : ∀ {x y : V}, R x y → S x → S y := by
    intro x y e hx
    change u = x ∨ Walk R u x at hx
    cases hx with
    | inl he =>
      subst x
      exact Or.inr (Walk.edge e)
    | inr p => exact Or.inr (Walk.join p (Walk.edge e))
  cases hp S ⟨v, hn⟩ with
  | intro a ha =>
    have hu : S u := Or.inl rfl
    cases hp (fun x => Not (S x)) ⟨u, fun h => h hu⟩ with
    | intro b hb =>
      exact hbad ⟨Mix S a b, good_of_cut hc ha hb⟩

theorem four_of_proper_colorings {V : Type u}
    {R : V → V → Prop}
    (hO : Oriented R)
    (hbad : Not (∃ c : V → Bool, Good R c))
    (hp : ProperColorings R) : ∀ v : V, FourDistinctNeighbours R v := by
  classical
  intro v
  cases hp (fun x => x ≠ v) ⟨v, fun h => h rfl⟩ with
  | intro c hg =>
    have hd : Good (Delete R v) c := hg
    have hf : ∀ b : Bool, Not (Good R (Recolour c v b)) :=
      fun b h => hbad ⟨Recolour c v b, h⟩
    exact fourDistinct_of_bothColours hO
      (bothNeighbours_of_no_good_extension hO hd hf)

theorem critical_structure {V : Type u}
    {R : V → V → Prop}
    (hO : Oriented R)
    (hbad : Not (∃ c : V → Bool, Good R c))
    (hp : ProperColorings R) :
    (∀ u v : V, Reach R u v) ∧
    (∀ v : V, FourDistinctNeighbours R v) :=
  ⟨strong_of_proper_colorings hbad hp,
    four_of_proper_colorings hO hbad hp⟩

end OPG169.C08Cut

#print axioms OPG169.C08Cut.acyclic_of_cut
#print axioms OPG169.C08Cut.good_of_cut
#print axioms OPG169.C08Cut.strong_of_proper_colorings
#print axioms OPG169.C08Cut.four_of_proper_colorings
#print axioms OPG169.C08Cut.critical_structure
