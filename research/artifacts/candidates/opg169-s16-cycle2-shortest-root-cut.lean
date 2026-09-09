import Init

set_option autoImplicit false

/-!
S16 Cycle 2: the shortest logical cut from the current route to OPG-169.

Frozen repository main: dc6ee891ed7614602e88d48a57314416082dd022.
Target toolchain: leanprover/lean4:v4.33.0.
This source is candidate_only and was not elaborated in the current host.

`Plane` is deliberately a parameter: this file proves the well-founded
root shell independently of the eventual concrete plane-embedding library.
The one open mathematical proposition is `ShortestRootCut Plane`.
-/

universe u

namespace OPG169.S16.Cycle2

inductive PosWalk {α : Type u} (R : α → α → Prop) : α → α → Prop where
  | edge {u v : α} : R u v → PosWalk R u v
  | join {u v w : α} : PosWalk R u v → PosWalk R v w → PosWalk R u w

def Acyclic {α : Type u} (R : α → α → Prop) : Prop :=
  ∀ v, ¬ PosWalk R v v

variable (Plane : {n : Nat} → (Fin n → Fin n → Prop) → Prop)

structure PlaneOrientation (n : Nat) where
  arc : Fin n → Fin n → Prop
  loopless : ∀ v, ¬ arc v v
  noAntiparallel : ∀ {u v}, arc u v → ¬ arc v u
  planar : Plane (fun u v => arc u v ∨ arc v u)

def MonoArc {n : Nat} (G : PlaneOrientation Plane n)
    (colour : Fin n → Bool) (k : Bool) : Fin n → Fin n → Prop :=
  fun u v => G.arc u v ∧ colour u = k ∧ colour v = k

def Good {n : Nat} (G : PlaneOrientation Plane n)
    (colour : Fin n → Bool) : Prop :=
  ∀ k : Bool, Acyclic (MonoArc Plane G colour k)

def TwoColorable {n : Nat} (G : PlaneOrientation Plane n) : Prop :=
  ∃ colour : Fin n → Bool, Good Plane G colour

def Root : Prop :=
  ∀ n (G : PlaneOrientation Plane n), TwoColorable Plane G

/--
The sole root cut. Under the induction hypothesis that every smaller
contract object is two-colourable, the current object is two-colourable.
-/
def ShortestRootCut : Prop :=
  ∀ n (G : PlaneOrientation Plane n),
    (∀ m, m < n → ∀ H : PlaneOrientation Plane m, TwoColorable Plane H) →
    TwoColorable Plane G

/-- The cut closes the root by strong induction on the vertex count. -/
theorem root_of_shortestRootCut
    (hcut : ShortestRootCut Plane) : Root Plane := by
  intro n
  exact Nat.strongRecOn
    (motive := fun n => ∀ G : PlaneOrientation Plane n, TwoColorable Plane G)
    n
    (fun n ih G => hcut n G (fun m hm H => ih m hm H))

/-- A proved root trivially supplies the induction step. -/
theorem shortestRootCut_of_root
    (hroot : Root Plane) : ShortestRootCut Plane := by
  intro n G _
  exact hroot n G

/-- The single cut is logically equivalent to the root statement. -/
theorem root_iff_shortestRootCut :
    Root Plane ↔ ShortestRootCut Plane := by
  constructor
  · exact shortestRootCut_of_root Plane
  · exact root_of_shortestRootCut Plane

#print axioms OPG169.S16.Cycle2.root_of_shortestRootCut
#print axioms OPG169.S16.Cycle2.root_iff_shortestRootCut

end OPG169.S16.Cycle2
