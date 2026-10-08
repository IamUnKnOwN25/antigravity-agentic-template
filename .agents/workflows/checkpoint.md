---
description: Save project progress to a durable file on disk and prepare for a fresh, rot-free chat context.
---

# /checkpoint Workflow

Execute this workflow when a conversation becomes long (15+ turns) or when ending a work session:

## 1. Inspect State
- Run `git status` and `git diff --stat` to review recent modifications.

## 2. Update `progress.md`
Write or update `progress.md` at the project root with:
- **Current Milestone**: What was being worked on.
- **Completed Changes**: Bullet points of finished work.
- **Known Issues / Blockers**: Broken tests or unresolved questions.
- **Next Steps**: Exact instruction for the next conversation to pick up.

## 3. Completion Message
Notify the user:
> *"State saved to `progress.md`. You can now open a fresh chat tab and type: 'Read progress.md and continue.'"*
