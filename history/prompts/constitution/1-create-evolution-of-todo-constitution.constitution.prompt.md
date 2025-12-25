---
id: 1
title: Create-evolution-of-todo-constitution
stage: constitution
date: 2025-01-01
surface: agent
model: gpt-4o
feature: evolution-of-todo
branch: main
user: user
command: /sp.constitution
labels: [constitution, spec-driven-development, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - null
---

## Prompt

```
/sp.constitution Create a single global constitution for the entire "Evolution of Todo" project covering Phase I through Phase V[cite: 17]. This constitution must define: 1. Spec-Driven Development as mandatory (No agent may write code without approved specs/tasks)[cite: 19, 20]. 2. Agent Behavior: No manual coding by humans, no feature invention, and no deviation from approved specs[cite: 23, 24, 25]. 3. Phase Governance: Future-phase features must never leak into earlier phases[cite: 31]. 4. Technology Constraints: Python for backend, Next.js for frontend, FastAPI, SQLModel, Neon DB, and MCP[cite: 34, 35, 36, 37]. This constitution acts as the supreme governing document.
```

## Response snapshot

Created a comprehensive constitution for the "Evolution of Todo" project with six core principles:
1. Spec-Driven Development (NON-NEGOTIABLE)
2. Agent-Centric Development
3. Phase Governance (NON-NEGOTIABLE)
4. Technology Stack Compliance
5. Quality Assurance Standards
6. Documentation and Traceability

The constitution includes sections on Technology Constraints, Development Governance, and Phase Governance. I also updated the dependent templates (plan, spec, and tasks) to align with the new constitution by adding constitutional compliance checks.

## Outcome

- ✅ Impact: Established foundational governance document for the entire project lifecycle
- 🧪 Tests: No tests required for this governance task
- 📁 Files: Updated constitution and 3 dependent templates to align with new principles
- 🔁 Next prompts: Users can now create specs based on this constitution
- 🧠 Reflection: The constitution establishes clear boundaries and requirements for the project

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A