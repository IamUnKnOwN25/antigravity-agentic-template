# Project Rules & Guidelines

<!-- 
This file is ALWAYS loaded into the AI agent's context for every message.
Keep it concise, actionable, and under 80 lines to prevent token bloat.
-->

## 1. Tech Stack & Environment
- **Runtime**: [e.g., Node.js 20+ / Python 3.11+ / Go 1.22]
- **Package Manager**: [e.g., pnpm / poetry / bun]
- **Core Frameworks**: [e.g., Next.js 15, FastAPI, Tailwind CSS]

## 2. Coding Standards
- Write clean, maintainable, and type-safe code.
- Avoid loose typings (e.g., no `any` in TypeScript, use strict type annotations in Python).
- Keep individual source files under 200 lines; extract modular functions and utilities when exceeded.

## 3. Autonomous Execution & Verification
- Always run the relevant test or build command (e.g., `pnpm test`, `pytest`) before marking a task complete.
- Never write dummy mock implementations into production code paths.
- If a command fails, diagnose the terminal error and self-heal before asking for user intervention.

## 4. Token & Output Optimization
- Respond directly without conversational filler (no "Certainly!", no pleasantries).
- For code modifications, use targeted diffs (`replace_file_content`) instead of regenerating entire files.
- Deliver concise bullet-point summaries rather than lengthy conversational recaps.

## 5. Security Guardrails
- Never inspect, log, or commit secret keys or `.env` files.
- Never run destructive git commands (e.g., `git reset --hard`, `git push --force`) without explicit confirmation.
