#!/usr/bin/env python3
"""
Antigravity Agentic Harness Adopter
Safely installs the Antigravity agentic structure into an existing project.
Usage:
    python scripts/adopt.py [optional_path_to_existing_project]
"""
import sys
import os
import shutil
from pathlib import Path

# Fix Windows console encoding for Unicode/Emojis
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def detect_stack(project_root: Path) -> dict:
    stack = {
        "runtime": "Not detected (Specify in GEMINI.md)",
        "package_manager": "Not detected",
        "framework": "Not detected",
        "test_runner": "Not detected"
    }

    # Node / JS / TS detection
    pkg_json = project_root / "package.json"
    if pkg_json.exists():
        stack["runtime"] = "Node.js (TypeScript)" if (project_root / "tsconfig.json").exists() else "Node.js (JavaScript)"
        if (project_root / "pnpm-lock.yaml").exists():
            stack["package_manager"] = "pnpm"
        elif (project_root / "yarn.lock").exists():
            stack["package_manager"] = "yarn"
        elif (project_root / "bun.lockb").exists() or (project_root / "bun.lock").exists():
            stack["package_manager"] = "bun"
        else:
            stack["package_manager"] = "npm"

        try:
            content = pkg_json.read_text(encoding="utf-8")
            if "next" in content:
                stack["framework"] = "Next.js"
            elif "react" in content:
                stack["framework"] = "React"
            elif "fastify" in content:
                stack["framework"] = "Fastify"
            elif "express" in content:
                stack["framework"] = "Express"

            if "vitest" in content:
                stack["test_runner"] = "vitest"
            elif "jest" in content:
                stack["test_runner"] = "jest"
        except Exception:
            pass

    # Python detection
    if (project_root / "pyproject.toml").exists() or (project_root / "requirements.txt").exists():
        stack["runtime"] = "Python 3.x"
        stack["package_manager"] = "poetry" if (project_root / "poetry.lock").exists() else "pip"
        stack["test_runner"] = "pytest"

    # Go detection
    if (project_root / "go.mod").exists():
        stack["runtime"] = "Go"
        stack["package_manager"] = "go modules"
        stack["test_runner"] = "go test"

    # Rust detection
    if (project_root / "Cargo.toml").exists():
        stack["runtime"] = "Rust"
        stack["package_manager"] = "cargo"
        stack["test_runner"] = "cargo test"

    return stack

def adopt(target_dir: str):
    target = Path(target_dir).resolve()
    template_root = Path(__file__).resolve().parent.parent

    print(f"\n🚀 Adopting Antigravity Agentic Harness into: {target}")

    if not target.exists():
        print(f"❌ Error: Target directory '{target}' does not exist.")
        sys.exit(1)

    # 1. Detect Stack
    stack = detect_stack(target)
    print("\n📦 Detected Stack:")
    for k, v in stack.items():
        print(f"   • {k}: {v}")

    # 2. Copy .agents structure safely
    agents_src = template_root / ".agents"
    agents_dest = target / ".agents"

    dirs_to_make = [
        agents_dest / "rules",
        agents_dest / "workflows",
        agents_dest / "skills",
        agents_dest / "agents",
        target / ".gemini",
        target / "scripts"
    ]
    for d in dirs_to_make:
        d.mkdir(parents=True, exist_ok=True)

    # Copy files if not already present
    files_to_copy = [
        (template_root / ".agents" / "rules" / "coding-standards.md", agents_dest / "rules" / "coding-standards.md"),
        (template_root / ".agents" / "workflows" / "task.md", agents_dest / "workflows" / "task.md"),
        (template_root / ".agents" / "workflows" / "checkpoint.md", agents_dest / "workflows" / "checkpoint.md"),
        (template_root / ".agents" / "agents" / "sample-agent.md", agents_dest / "agents" / "sample-agent.md"),
        (template_root / ".gemini" / "mcp_config.json", target / ".gemini" / "mcp_config.json"),
        (template_root / "scripts" / "health_check.py", target / "scripts" / "health_check.py"),
    ]

    # Copy sample-skill directory
    sample_skill_src = template_root / ".agents" / "skills" / "sample-skill"
    sample_skill_dest = agents_dest / "skills" / "sample-skill"
    if sample_skill_src.exists() and not sample_skill_dest.exists():
        shutil.copytree(sample_skill_src, sample_skill_dest)
        print("   ✔ Copied .agents/skills/sample-skill/")

    for src, dest in files_to_copy:
        if src.exists() and not dest.exists():
            shutil.copy2(src, dest)
            print(f"   ✔ Created {dest.relative_to(target)}")
        elif dest.exists():
            print(f"   ⏩ Kept existing {dest.relative_to(target)} (not overwritten)")

    # 3. Create or Update GEMINI.md
    gemini_file = target / "GEMINI.md"
    if not gemini_file.exists():
        gemini_content = f"""# Project Rules & Guidelines

## 1. Tech Stack & Environment
- **Runtime**: {stack['runtime']}
- **Package Manager**: {stack['package_manager']}
- **Core Framework**: {stack['framework']}
- **Test Runner**: {stack['test_runner']}

## 2. Coding Standards
- Write clean, maintainable, and type-safe code.
- Avoid loose typings and unhandled error cases.
- Keep individual source files under 200 lines; extract modular components/utilities when exceeded.

## 3. Autonomous Execution & Verification
- Always run the relevant test suite ({stack['test_runner']}) before marking a task complete.
- Never write dummy mock implementations into production code paths.
- If a command fails in terminal, diagnose the error and self-heal before asking for user intervention.

## 4. Token & Output Optimization
- Respond directly without conversational filler (no "Certainly!", no pleasantries).
- For code modifications, use targeted diffs (`replace_file_content`) instead of regenerating entire files.
- Deliver concise bullet-point summaries rather than lengthy conversational recaps.

## 5. Security Guardrails
- Never inspect, log, or commit secret keys or `.env` files.
- Never run destructive git commands (e.g., `git reset --hard`, `git push --force`) without explicit confirmation.
"""
        gemini_file.write_text(gemini_content, encoding="utf-8")
        print("   ✔ Generated tailored GEMINI.md with your detected stack!")
    else:
        print("   ⏩ Kept existing GEMINI.md (preserves your custom rules)")

    print("\n✅ Antigravity Harness successfully configured in your project!")
    print("\nNext Steps:")
    print("1. Review GEMINI.md and adjust any stack rules.")
    print("2. Open your project in Antigravity.")
    print("3. Try running '/task' or '/checkpoint' in chat.\n")

if __name__ == "__main__":
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."
    adopt(target_path)
