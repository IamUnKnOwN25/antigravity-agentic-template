---
name: sample-skill
description: Template skill showing how to define on-demand procedural instructions and executable helper scripts.
---

# Sample Skill: Standard Operating Procedure (SOP)

<!-- 
Skills are loaded ON-DEMAND via Progressive Disclosure.
The main prompt only sees the `name` and `description` above until this skill is needed.
-->

## When to Use
Use this skill whenever performing [insert specialized task, e.g., adding an API route, creating a database migration, deploying to staging].

## Step-by-Step Procedure

1. **Pre-Check**:
   Run the local verification script to check prerequisites:
   ```bash
   python .agents/skills/sample-skill/scripts/helper.py
   ```

2. **Execute Core Task**:
   Follow the standard implementation pattern:
   - Create or update the target files following project standards.
   - Ensure proper validation and typing.

3. **Validation**:
   Execute test commands to confirm the procedure completed successfully.
