"""
Workspace Health Check Utility
Performs a quick local check of repository structure and configuration.
Usage: python scripts/health_check.py
"""
import sys
import json
from pathlib import Path

def check_structure():
    root = Path.cwd()
    checks = {
        "gemini_rules": (root / "GEMINI.md").exists(),
        "agents_dir": (root / ".agents").exists(),
        "workflows_dir": (root / ".agents" / "workflows").exists(),
        "skills_dir": (root / ".agents" / "skills").exists(),
        "agents_subdir": (root / ".agents" / "agents").exists(),
        "mcp_config": (root / ".gemini" / "mcp_config.json").exists(),
    }
    
    all_ok = all(checks.values())
    status = {
        "status": "PASS" if all_ok else "INCOMPLETE",
        "checks": checks
    }
    print(json.dumps(status, indent=2))
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(check_structure())
