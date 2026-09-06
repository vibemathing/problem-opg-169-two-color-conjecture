# Web Research Context Bundle

This file is generated from repository truth and bounded for the web channel. It is navigation context, not a Result, EvidenceLink, verifier receipt, or permission grant.

## Mandatory order

1. Read `AGENTS.md`, `governance/harness/PROJECT_AGENTS.md`, and `WEB_BOOTSTRAP.md`.
2. Check the exact ProblemContract and its SHA-256 below.
3. Select exactly one pre-admitted Attempt/Route/ObligationGraph/Obligation.
4. Search registered mathematical knowledge sources before inventing a new theorem.
5. After repository admission, autonomously complete Issue, candidate branch/file edits, commit, PR review, checks/rerun, merge, and checkpoint within the profile.
6. Write only candidate files under the profile allowlist and one `WEB_ATTEMPT_PACKET`; do not wait for project-added routine human approvals.
7. Never claim that Issue, PR, AI review, merge, Actions status, package build, search hit, test success, or this context closes mathematics.

## Compiled repository truth

```json
{
  "active_skills": [
    {
      "entry": ".codex/skills/math-computation/SKILL.md",
      "entry_sha256": "80c447221725ec198bee4b104d43ca28425110a7dac17afa9cad56ec69b57f48",
      "skill_id": "math-computation",
      "version": "0.6.0",
      "web_status": "constrained"
    },
    {
      "entry": ".codex/skills/math-derivation/SKILL.md",
      "entry_sha256": "3f3b567729f1e5dd24f87e832fdac702577f4add14b8cf6be12d538e1fe787c1",
      "skill_id": "math-derivation",
      "version": "0.4.0",
      "web_status": "active"
    },
    {
      "entry": ".codex/skills/math-discovery/SKILL.md",
      "entry_sha256": "ceb54d773cd970ca42d0243fb1a39b109cab3ffdbe2dd87b98b43539f988d471",
      "skill_id": "math-discovery",
      "version": "0.4.0",
      "web_status": "active"
    },
    {
      "entry": ".codex/skills/math-formalization/SKILL.md",
      "entry_sha256": "8ade921dacd277f425f424064a6002806c057f160555081dbdb4ec05c1f5ea05",
      "skill_id": "math-formalization",
      "version": "0.5.0",
      "web_status": "constrained"
    },
    {
      "entry": ".codex/skills/math-proof/SKILL.md",
      "entry_sha256": "61006c732ad69e73f56be126acb6fa9e25c866e18733ce1f0f3863c1f8eea80f",
      "skill_id": "math-proof",
      "version": "0.5.0",
      "web_status": "active"
    },
    {
      "entry": ".codex/skills/math-toolchain/SKILL.md",
      "entry_sha256": "f6514e01358aa2e40f8b7e3bb9221fd9abca6b7ff37ec6920f2c2cf537533f7b",
      "skill_id": "math-toolchain",
      "version": "0.2.0",
      "web_status": "constrained"
    },
    {
      "entry": ".codex/skills/solve/SKILL.md",
      "entry_sha256": "ff557dc3fc2fa10df4b21e8bef251a37928f5572ccf0092c79f0d9ab90a00ec0",
      "skill_id": "solve",
      "version": "0.3.0",
      "web_status": "active"
    },
    {
      "entry": ".codex/skills/vibe-mathing-router/SKILL.md",
      "entry_sha256": "65f6b25fe152a4cc2fa9ecb03626dad6e3b70473fc256ac9acbabd0ef7cb9e8e",
      "skill_id": "vibe-mathing-router",
      "version": "0.4.0",
      "web_status": "active"
    }
  ],
  "attempts": [
    {
      "artifacts": [],
      "attempt_id": "attempt:web-20260906-opg169-a01",
      "claims": [],
      "completed_at": null,
      "generator": "chatgpt-web-github",
      "inputs": [
        "problem-library/records/canonical-problems.jsonl",
        "research/records/failed-routes.jsonl"
      ],
      "lifecycle": "running",
      "method": "proof",
      "objective": "严格证明：若 Two Color Conjecture 存在按顶点数最小的反例 G，则 G 强连通，且其 underlying graph 的最小度至少为 3。",
      "obligation_graph_id": "graph:opg169-initial-v1",
      "problem_contract_sha256": "719230edd088c52a5468eed8090579e5eef1bf85d8a56e633350063108f345ec",
      "problem_id": "problem:opg-169-two-color-conjecture",
      "route_id": "route:minimal-counterexample-structure-v1",
      "started_at": "2026-09-06T05:03:30Z"
    }
  ],
  "failed_routes": [],
  "knowledge_operators": [
    {
      "evidence_ceiling": "discovery_only",
      "external_effect": "none",
      "operator_id": "op:identify-mathematical-object",
      "owner_skill": "math-discovery"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "read_local",
      "operator_id": "op:search-formal-theorem",
      "owner_skill": "math-discovery"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "read_network",
      "operator_id": "op:search-mathematical-database",
      "owner_skill": "math-discovery"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "read_local",
      "operator_id": "op:resolve-formal-package",
      "owner_skill": "math-formalization"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "none",
      "operator_id": "op:compare-statements",
      "owner_skill": "math-proof"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "none",
      "operator_id": "op:compose-reuse-plan",
      "owner_skill": "math-proof"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "none",
      "operator_id": "op:prove-reuse-gap",
      "owner_skill": "math-proof"
    },
    {
      "evidence_ceiling": "candidate_only",
      "external_effect": "bounded_candidate_build",
      "operator_id": "op:build-formal-candidate",
      "owner_skill": "math-formalization"
    },
    {
      "evidence_ceiling": "verifier_receipt",
      "external_effect": "bounded_candidate_build",
      "operator_id": "op:verify-formal-candidate",
      "owner_skill": "math-formalization"
    },
    {
      "evidence_ceiling": "verifier_receipt",
      "external_effect": "none",
      "operator_id": "op:review-reuse-semantics",
      "owner_skill": "math-proof"
    }
  ],
  "knowledge_sources": [
    {
      "evidence_ceiling": "verifier_input",
      "maturity": "installed",
      "operational_status": "quarantined",
      "source_class": "formal_library_index",
      "source_id": "lean-mathlib-local"
    },
    {
      "evidence_ceiling": "candidate_only",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "formal_package_registry",
      "source_id": "lean-reservoir"
    },
    {
      "evidence_ceiling": "candidate_only",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "formal_library_index",
      "source_id": "mathlib-docs-search"
    },
    {
      "evidence_ceiling": "verifier_input",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "proof_archive",
      "source_id": "isabelle-afp"
    },
    {
      "evidence_ceiling": "verifier_input",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "formal_package_registry",
      "source_id": "rocq-mathcomp"
    },
    {
      "evidence_ceiling": "candidate_only",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "mathematical_object_database",
      "source_id": "oeis"
    },
    {
      "evidence_ceiling": "candidate_only",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "mathematical_object_database",
      "source_id": "lmfdb"
    },
    {
      "evidence_ceiling": "candidate_only",
      "maturity": "surveyed",
      "operational_status": "available",
      "source_class": "formula_reference",
      "source_id": "nist-dlmf"
    },
    {
      "evidence_ceiling": "computation_evidence",
      "maturity": "surveyed",
      "operational_status": "design_only",
      "source_class": "algorithm_distribution",
      "source_id": "sagemath"
    }
  ],
  "obligation_graphs": [
    {
      "attempt_id": "attempt:web-20260906-opg169-a01",
      "graph_id": "graph:opg169-initial-v1",
      "obligations": [
        {
          "dependencies": [
            "obligation:opg169-strong-min-degree-three"
          ],
          "kind": "root_claim",
          "obligation_id": "obligation:opg169-root",
          "statement": {
            "formal_declaration": null,
            "language": "en",
            "text": "For every orientation G of a finite simple planar graph, can V(G) be partitioned into X₁ and X₂ so that each induced digraph G[Xᵢ] is acyclic?"
          },
          "statement_sha256": "384e13c90c28fc7af0281753a421a641625fb4024165358eb4bd0a799a664756"
        },
        {
          "dependencies": [],
          "kind": "lemma",
          "obligation_id": "obligation:opg169-strong-min-degree-three",
          "statement": {
            "formal_declaration": null,
            "language": "zh",
            "text": "严格证明：若 Two Color Conjecture 存在按顶点数最小的反例 G，则 G 强连通，且其 underlying graph 的最小度至少为 3。"
          },
          "statement_sha256": "e5d7b7d2903018956d3e5c66f61cd5d33ef699e068931d2e97a13a1fbaeda4da"
        }
      ],
      "root_obligation_id": "obligation:opg169-root",
      "route_id": "route:minimal-counterexample-structure-v1"
    }
  ],
  "problem_contract": {
    "acceptance": {
      "policy": "solution-admission-v1"
    },
    "aliases": [
      "Open Problem Garden OPG-169"
    ],
    "allowed_axioms": [
      "finite-digraph-basic",
      "planar-graph-basic",
      "finite-combinatorics"
    ],
    "assumptions": [
      "All graphs and digraphs are finite and simple unless the statement explicitly says otherwise."
    ],
    "constraints": {
      "allowed_adapters": [
        "planar-digraph-enumerator-v1",
        "acyclic-two-color-sat-v1",
        "lean-obligation-v1"
      ],
      "allowed_methods": [
        "discovery",
        "derivation",
        "computation",
        "proof",
        "formalization"
      ],
      "max_attempts": 20,
      "runtime": {
        "max_output_bytes": 5242880,
        "max_retries": 3,
        "max_transitions": 300,
        "timeout_seconds": 1800
      }
    },
    "created_at": "2026-09-06T03:30:00Z",
    "definitions": [
      {
        "definition": "A digraph obtained by assigning one direction to every edge of a simple graph.",
        "term": "orientation"
      },
      {
        "definition": "A directed graph containing no directed cycle.",
        "term": "acyclic digraph"
      },
      {
        "definition": "The digraph on X containing every arc of G whose endpoints both lie in X.",
        "term": "induced digraph G[X]"
      }
    ],
    "domain": {
      "description": "Orientations of finite simple planar graphs.",
      "objects": [
        "planar digraph",
        "vertex 2-coloring",
        "acyclic induced digraph"
      ]
    },
    "lifecycle": "active",
    "msc": [
      "05C20",
      "05C15"
    ],
    "problem_id": "problem:opg-169-two-color-conjecture",
    "quantifiers": [
      {
        "domain": "orientations of finite simple planar graphs",
        "kind": "forall",
        "variables": [
          "G"
        ]
      },
      {
        "domain": "partitions V(G)=X₁⊔X₂",
        "kind": "exists",
        "variables": [
          "X₁",
          "X₂"
        ]
      }
    ],
    "schema_version": "1.0.0",
    "sources": [
      {
        "retrieved_at": "2026-09-02T00:06:43Z",
        "source": "UnsolvedMath",
        "source_record_id": "unsolvedmath-opg-169-203611002f24",
        "url": "https://www.unsolvedmath.com/problems/OPG-169"
      }
    ],
    "statement": {
      "language": "en",
      "text": "For every orientation G of a finite simple planar graph, can V(G) be partitioned into X₁ and X₂ so that each induced digraph G[Xᵢ] is acyclic?",
      "version": 1
    },
    "title": "The Two Color Conjecture for planar digraphs",
    "updated_at": "2026-09-06T03:30:00Z"
  },
  "problem_contract_sha256": "719230edd088c52a5468eed8090579e5eef1bf85d8a56e633350063108f345ec"
}
```
