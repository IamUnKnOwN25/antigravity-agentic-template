# Antigravity Agentic Starter Template

A clean, production-ready architectural template designed specifically for **Google Antigravity** and modern agentic AI development. 

This repository provides the minimal, unbloated boilerplate required to configure custom **Rules**, **Workflows**, **Skills**, **Subagents**, **MCP connections**, and **Deterministic Python Helpers** for your project.

---

## Architecture Overview

```mermaid
flowchart TD
    User["User Trigger (/task)"] --> Workflows[".agents/workflows/ (Slash Commands)"]
    Workflows --> Rules["GEMINI.md & .agents/rules/ (Always-On Laws)"]
    Rules --> Skills[".agents/skills/ (Progressive On-Demand SOPs)"]
    Skills --> Python["Python Scripts (0-Token Data Pre-Filtering)"]
    Skills --> MCP[".gemini/mcp_config.json (Structured External Data)"]
    Workflows --> Subagents[".agents/agents/ (Context-Isolated Workers)"]
    Subagents --> Done["Verified Implementation"]
```

---

## Directory Structure

```text
.
├── GEMINI.md                                  # 1. ALWAYS-ON RULES (Root guardrails & tech stack)
├── .gitignore                                 # Git ignore rules for node, python, & agent temp files
├── README.md                                  # This documentation
│
├── .gemini/
│   └── mcp_config.json                        # 2. MCP CONFIG (External databases, APIs, GitHub)
│
├── scripts/                                   # 3. GLOBAL DETERMINISTIC UTILITIES
│   └── health_check.py                        #    Fast repository sanity check (0-token cost)
│
└── .agents/
    ├── rules/                                 # 4. MODULAR RULES
    │   └── coding-standards.md                #    Domain-specific coding & architectural standards
    │
    ├── workflows/                             # 5. WORKFLOWS (User-Invoked Slash Commands)
    │   ├── task.md                            #    `/task`       -> Standard plan-build-verify cycle
    │   └── checkpoint.md                      #    `/checkpoint` -> Context rotation & handoff save
    │
    ├── skills/                                # 6. AGENT SKILLS (On-Demand Runbooks & Recipes)
    │   └── sample-skill/
    │       ├── SKILL.md                       #    Procedure definition with YAML frontmatter
    │       └── scripts/
    │           └── helper.py                  #    Executable helper script bundled with skill
    │
    └── agents/                                # 7. CUSTOM SUBAGENTS (Isolated Specialists)
        └── sample-agent.md                    #    Dedicated worker role definition
```

---

## The 5 Core Concepts Explained

| Component | Location | Lifecycle | Purpose |
| :--- | :--- | :--- | :--- |
| **Rules** | `GEMINI.md`, `.agents/rules/` | **Always Active** | The non-negotiable boundaries, coding standards, and forbidden actions. |
| **Workflows** | `.agents/workflows/<name>.md` | **Slash Commands (`/<name>`)** | High-level execution pipelines that automate multi-step tasks. |
| **Skills** | `.agents/skills/<name>/SKILL.md` | **Progressive (On-Demand)** | Modular SOPs and recipes loaded only when their `description` matches the task. |
| **Subagents** | `.agents/agents/<name>.md` | **Spawned by Agent** | Isolated worker threads running specialized roles (`flash` or `pro` model). |
| **MCP** | `.gemini/mcp_config.json` | **Tool Integration** | Clean, structured JSON connections to live databases, GitHub, or remote APIs. |

---

## Built-In Token Optimization

This template is configured out of the box to prevent context bloat and minimize token spend:

1. **Progressive Disclosure**: Detailed skill instructions live inside `SKILL.md` files and are never loaded until explicitly needed.
2. **Context Rotation (`/checkpoint`)**: Prevents "context rot" in long conversations by saving current state to `progress.md` so you can start a fresh, fast chat session without losing progress.
3. **Deterministic Python Helpers**: Heavy tasks (counting rows, checking file trees, formatting data) run on your local CPU via Python scripts rather than burning model tokens.
4. **Context Firewalls (Subagents)**: Trial-and-error debugging runs inside isolated subagents, protecting the primary chat history from bloat.

---

## Quickstart

### 1. Initialize in Your Workspace
Clone or copy this directory into your project root:
```bash
git clone <your-repo-url> my-project
cd my-project
```

### 2. Verify Template Integrity
Run the built-in health check script:
```bash
python scripts/health_check.py
```

### 3. Customize for Your Stack
- Edit `GEMINI.md` to specify your preferred language, framework, and package manager.
- Add your database or GitHub tokens to `.gemini/mcp_config.json` (if using MCP).
- Open the project in **Antigravity**, start a new chat, and try:
  ```text
  /task "Build initial project setup"
  /checkpoint
  ```
