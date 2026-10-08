# Modular Rule: Code Quality & Architecture

<!-- 
Rules placed in .agents/rules/ are discovered and merged automatically.
Use this folder to split complex domain rules into dedicated files.
-->

1. **Single Responsibility**: Every module or component should have a single clear purpose.
2. **Error Handling**: Use structured try/catch blocks with typed or identifiable error classes. Never silently swallow exceptions.
3. **Immutability**: Prefer immutable data structures and pure functions where possible.
4. **Naming Conventions**: Use descriptive names that clearly convey intent (avoid single-letter abbreviations outside loops).
