# Nanobot Code Reviewer#

Automated code review tools for analyzing pull requests, detecting code quality issues, and generating review reports with nanobot.

## Use when#

- Reviewing pull requests, analyzing code quality, identifying issues
- Generating review checklists, automating code review processes
- Working with TypeScript, JavaScript, Python, Go, Swift, Kotlin codebases
- Need to detect complexity, security issues, or SOLID violations
- Integrating automated review into nanobot superpowers workflows#

## Core principle#

Code review is about catching issues early and sharing knowledge—not blame. nanobot automates the mechanical checks (complexity, style, common bugs) so humans can focus on design, logic, and intent.

## The Process#

### 1. Analyze Pull Requests#

Use nanobot to assess review complexity and identify risks:

```bash
# Analyze current branch against main
python scripts/pr_analyzer.py /path/to/repo#

# Compare specific branches
python scripts/pr_analyzer.py . --base main --head feature-branch#

# JSON output for integration
python scripts/pr_analyzer.py /path/to/repo --json
```

**What nanobot detects:**
- Hardcoded secrets (passwords, API keys, tokens)
- SQL injection patterns (string concatenation in queries)
- Debug statements (debugger, console.log)
- ESLint rule disabling
- TypeScript `any` types
- TODO/FIXME comments#

**Output includes:**
- Complexity score (1-10)
- Risk categorization (critical, high, medium, low)
- File prioritization for review order
- Commit message validation#

### 2. Check Code Quality#

Analyze source code for structural issues and code smells:

```bash
# Analyze a directory
python scripts/code_quality_checker.py /path/to/code#

# Analyze specific language
python scripts/code_quality_checker.py . --language python#

# JSON output
python scripts/code_quality_checker.py /path/to/code --json
```

**What nanobot detects:**
- Long functions (>50 lines)
- Large files (>500 lines)
- God classes (>20 methods)
- Deep nesting (>4 levels)
- Too many parameters (>5)
- High cyclomatic complexity
- Missing error handling
- Unused imports
- Magic numbers#

**Thresholds:**

| Issue | Threshold |
|-------|-----------|
| Long function | >50 lines |
| Large file | >500 lines |
| God class | >20 methods |
| Too many params | >5 |
| Deep nesting | >4 levels |
| High complexity | >10 branches |#

### 3. Generate Review Reports#

Combine PR analysis and code quality findings into structured reports:

```bash
# Generate report for current repo
python scripts/review_report_generator.py /path/to/repo#

# Markdown output
python scripts/review_report_generator.py . --format markdown --output review.md#

# Use pre-computed analyses
python scripts/review_report_generator.py . \
  --pr-analysis pr_results.json \
  --quality-analysis quality_results.json
```

**Report includes:**
- Review verdict (approve, request changes, block)
- Score (0-100)
- Prioritized action items
- Issue summary by severity
- Suggested review order#

**Verdicts:**

| Score | Verdict |
|-------|---------|
| 90+ with no high issues | Approve |
| 75+ with ≤2 high issues | Approve with suggestions |
| 50-74 | Request changes |
| <50 or critical issues | Block |

## Tools Included#

### PR Analyzer#
Analyzes git diff between branches to assess review complexity and identify risks.

### Code Quality Checker#
Analyzes source code for structural issues, code smells, and SOLID violations.

### Review Report Generator#
Combines PR analysis and code quality findings into structured review reports.

## Red Flags#

- **Hardcoded secrets** (passwords, API keys) → Block review immediately
- **SQL injection patterns** → Block, rewrite with parameterized queries
- **Complexity score >8** → Require refactoring before approve
- **God classes (>20 methods)** → Split into focused classes
- **Deep nesting (>4 levels)** → Simplify logic, extract methods
- **Missing error handling** → Add try/catch or error propagation
- **TypeScript `any` types** → Add proper type annotations
- **Unused imports** → Remove to keep code clean
- **Magic numbers** → Extract to named constants#

## Languages Supported#

| Language | Extensions |
|----------|------------|
| Python | `.py` |
| TypeScript | `.ts`, `.tsx` |
| JavaScript | `.js`, `.jsx`, `.mjs` |
| Go | `.go` |
| Swift | `.swift` |
| Kotlin | `.kt`, `.kts` |

## Reference Guides#

Load these files from the SKILL's `references/` directory for detailed information:

### Code Review Checklist#
`references/code_review_checklist.md`#

Systematic checklists covering:
- Pre-review checks (build, tests, PR hygiene)
- Correctness (logic, data handling, error handling)
- Security (input validation, injection prevention)
- Performance (efficiency, caching, scalability)
- Maintainability (code quality, naming, structure)
- Testing (coverage, quality, mocking)
- Language-specific checks#

### Coding Standards#
`references/coding_standards.md`#

Language-specific standards for:
- TypeScript (type annotations, null safety, async/await)
- JavaScript (declarations, patterns, modules)
- Python (type hints, exceptions, class design)
- Go (error handling, structs, concurrency)
- Swift (optionals, protocols, errors)
- Kotlin (null safety, data classes, coroutines)#

### Common Antipatterns#
`references/common_antipatterns.md`#

Antipattern catalog with examples and fixes:
- Structural (god class, long method, deep nesting)
- Logic (boolean blindness, stringly typed code)
- Security (SQL injection, hardcoded credentials)
- Performance (N+1 queries, unbounded collections)
- Testing (duplication, testing implementation)
- Async (floating promises, callback hell)#

## Common nanobot Commands#

```bash
# PR Analysis
python scripts/pr_analyzer.py .                    # Analyze current branch
python scripts/pr_analyzer.py . --json              # JSON output
python scripts/pr_analyzer.py . --base main       # Compare against main#

# Code Quality
python scripts/code_quality_checker.py .                     # Analyze current directory
python scripts/code_quality_checker.py . --language python  # Specific language
python scripts/code_quality_checker.py . --json               # JSON output#

# Review Reports
python scripts/review_report_generator.py .                          # Generate report
python scripts/review_report_generator.py . --format markdown    # Markdown output
python scripts/review_report_generator.py . --output review.md      # Save to file
```

## Integration with nanobot Superpowers#

To use with your nanobot workflow:

1. **Pre-commit hook**: Run `pr_analyzer.py` before allowing commits
2. **CI/CD integration**: Add quality checks to your pipeline
3. **PR template**: Include review report in pull request description
4. **Local development**: Run `code_quality_checker.py` before pushing

```bash
# Example: Pre-commit check
python scripts/code_quality_checker.py . --json | grep -q '"score": [0-7]' && echo "FAIL: Code quality too low" && exit 1
```
