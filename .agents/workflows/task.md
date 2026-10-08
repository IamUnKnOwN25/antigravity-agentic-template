---
description: Standard development workflow for implementing a task with planning, execution, and verification.
---

# /task Workflow

Execute this workflow when developing a new feature or solving an issue:

## 1. Plan & Scope
- Inspect project requirements and affected files.
- If relevant skills exist in `.agents/skills/`, review their `SKILL.md` instructions.
- Provide a brief 3-bullet execution plan.

## 2. Implement
- Apply modifications adhering to `GEMINI.md` and `.agents/rules/`.
- Use targeted diff edits rather than full-file rewrites.

## 3. Verify
- Run project test/build commands to ensure zero regressions.
- If tests fail, diagnose and fix them immediately.

## 4. Summary
- Present a concise summary of modified files and verification results.
