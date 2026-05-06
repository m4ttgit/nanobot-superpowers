# Nanobot Prompt Engineer#

Prompt engineering patterns, LLM evaluation frameworks, and agentic system design with nanobot.

## Use when#

- User asks to "optimize prompts", "design prompt templates", "evaluate LLM outputs"
- Building agentic systems, implementing RAG, creating few-shot examples
- Analyzing token usage, designing AI workflows, improving model outputs
- Working with nanobot superpowers project on AI/LLM integration
- Need to design structured outputs (JSON, XML) for nanobot agents#

## Core principle#

Effective prompts are clear, specific, and include examples. nanobot helps you analyze, optimize, and validate prompts—but the creative judgment and output quality validation remain with the team.

## The Process#

### 1. Analyze and Optimize Prompts#

Use nanobot to analyze prompt efficiency and generate optimized versions:

```bash
# Analyze a prompt file
python scripts/prompt_optimizer.py prompt.txt --analyze#

# Output:
# Token count: 847
# Estimated cost: $0.0025 (GPT-4)
# Clarity score: 72/100
# Issues found:
#   - Ambiguous instruction at line 3
#   - Missing output format specification
#   - Redundant context (lines 12-15 repeat lines 5-8)
# Suggestions:
#   1. Add explicit output format: "Respond in JSON with keys: ..."
#   2. Remove redundant context to save 89 tokens
#   3. Clarify "analyze" -> "list the top 3 issues with severity ratings"

# Generate optimized version
python scripts/prompt_optimizer.py prompt.txt --optimize --output optimized.txt#

# Count tokens for cost estimation
python scripts/prompt_optimizer.py prompt.txt --tokens --model gpt-4#

# Extract and manage few-shot examples
python scripts/prompt_optimizer.py prompt.txt --extract-examples --output examples.json
```

### 2. Evaluate RAG Quality#

For Retrieval-Augmented Generation systems:

```bash
# Evaluate retrieval quality
python scripts/rag_evaluator.py --contexts retrieved.json --questions eval_set.json#

# Output:
# === RAG Evaluation Report ===
# Questions evaluated: 50
#
# Retrieval Metrics:
#   Context Relevance: 0.78 (target: >0.80)
#   Retrieval Precision@5: 0.72
#   Coverage: 0.85
#
# Generation Metrics:
#   Answer Faithfulness: 0.91
#   Groundedness: 0.88
#
# Issues Found:
#   - 8 questions had no relevant context in top-5
#   - 3 answers contained information not in context
#
# Recommendations:
#   1. Improve chunking strategy for technical documents
#   2. Add metadata filtering for date-sensitive queries

# Evaluate with custom metrics
python scripts/rag_evaluator.py --contexts retrieved.json --questions eval_set.json \
    --metrics relevance,faithfulness,coverage#

# Export detailed results
python scripts/rag_evaluator.py --contexts retrieved.json --questions eval_set.json \
    --output report.json --verbose
```

### 3. Design Agent Workflows#

Visualize and validate agent configurations:

```bash
# Validate agent configuration
python scripts/agent_orchestrator.py agent.yaml --validate#

# Output:
# === Agent Validation Report ===
# Agent: research_assistant
# Pattern: ReAct
#
# Tools (4 registered):
#   [OK] web_search - API key configured
#   [OK] calculator - No config needed
#   [WARN] file_reader - Missing allowed_paths
#   [OK] summarizer - Prompt template valid
#
# Flow Analysis:
#   Max depth: 5 iterations
#   Estimated tokens/run: 2,400-4,800
#   Potential infinite loop: No
#
# Recommendations:
#   1. Add allowed_paths to file_reader for security
#   2. Consider adding early exit condition for simple queries

# Visualize agent workflow (ASCII)
python scripts/agent_orchestrator.py agent.yaml --visualize#

# Export workflow as Mermaid diagram
python scripts/agent_orchestrator.py agent.yaml --visualize --format mermaid
```

### 4. Apply Prompt Engineering Patterns#

#### Prompt Optimization Workflow#

**Step 1: Baseline current prompt**
```bash
python scripts/prompt_optimizer.py current_prompt.txt --analyze --output baseline.json
```

**Step 2: Identify issues**
Review the analysis report for:
- Token waste (redundant instructions, verbose examples)
- Ambiguous instructions (unclear output format, vague verbs)
- Missing constraints (no length limits, no format specification)

**Step 3: Apply optimization patterns**

| Issue | Pattern to Apply |
|-------|------------------|
| Ambiguous output | Add explicit format specification |
| Too verbose | Extract to few-shot examples |
| Inconsistent results | Add role/persona framing |
| Missing edge cases | Add constraint boundaries |

**Step 4: Generate optimized version**
```bash
python scripts/prompt_optimizer.py current_prompt.txt --optimize --output optimized.txt
```

**Step 5: Compare results**
```bash
python scripts/prompt_optimizer.py optimized.txt --analyze --compare baseline.json
# Shows: token reduction, clarity improvement, issues resolved
```

#### Few-Shot Example Design#

**Step 1: Define the task clearly**
```
Task: Extract product entities from customer reviews
Input: Review text
Output: JSON with {product_name, sentiment, features_mentioned}
```

**Step 2: Select diverse examples (3-5 recommended)**

| Example Type | Purpose |
|--------------|---------|
| Simple case | Shows basic pattern |
| Edge case | Handles ambiguity |
| Complex case | Multiple entities |
| Negative case | What NOT to extract |

**Step 3: Format consistently**
```
Example 1:
Input: "Love my new iPhone 15, the camera is amazing!"
Output: {"product_name": "iPhone 15", "sentiment": "positive", "features_mentioned": ["camera"]}

Example 2:
Input: "The laptop was okay but battery life is terrible."
Output: {"product_name": "laptop", "sentiment": "mixed", "features_mentioned": ["battery life"]}
```

**Step 4: Validate example quality**
```bash
python scripts/prompt_optimizer.py prompt_with_examples.txt --validate-examples
# Checks: consistency, coverage, format alignment
```

#### Structured Output Design#

**Step 1: Define schema**
```json
{
  "type": "object",
  "properties": {
    "summary": {"type": "string", "maxLength": 200},
    "sentiment": {"enum": ["positive", "negative", "neutral"]},
    "confidence": {"type": "number", "minimum": 0, "maximum": 1}
  },
  "required": ["summary", "sentiment"]
}
```

**Step 2: Include schema in prompt**
```
Respond with JSON matching this schema:
- summary (string, max 200 chars): Brief summary of the content
- sentiment (enum): One of "positive", "negative", "neutral"
- confidence (number 0-1): Your confidence in the sentiment
```

**Step 3: Add format enforcement**
```
IMPORTANT: Respond ONLY with valid JSON. No markdown, no explanation.
Start your response with { and end with }
```

**Step 4: Validate outputs**
```bash
python scripts/prompt_optimizer.py structured_prompt.txt --validate-schema schema.json
```

## Tools Included#

### Prompt Optimizer#
Analyzes prompts for token efficiency, clarity, and structure. Generates optimized versions.

### RAG Evaluator#
Evaluates Retrieval-Augmented Generation quality by measuring context relevance and answer faithfulness.

### Agent Orchestrator#
Parses agent definitions and visualizes execution flows. Validates tool configurations.

## Red Flags#

- **Token waste >30%** → Remove redundant context, consolidate instructions
- **Clarity score <70** → Add explicit output format, clarify verbs
- **Missing examples for complex tasks** → Add 3-5 diverse few-shot examples
- **RAG relevance <0.80** → Improve chunking, add metadata filtering
- **Agent infinite loop risk** → Add early exit conditions, max iteration limits
- **Unvalidated JSON outputs** → Always include schema + format enforcement
- **Over-engineered prompts** → Start simple, add complexity only when validated

## Common Patterns Quick Reference#

| Pattern | When to Use | Example |
|---------|-------------|---------|
| **Zero-shot** | Simple, well-defined tasks | "Classify this email as spam or not spam" |
| **Few-shot** | Complex tasks, consistent format needed | Provide 3-5 examples before the task |
| **Chain-of-Thought** | Reasoning, math, multi-step logic | "Think step by step..." |
| **Role Prompting** | Expertise needed, specific perspective | "You are an expert tax accountant..." |
| **Structured Output** | Need parseable JSON/XML | Include schema + format enforcement |

## Common nanobot Commands#

```bash
# Prompt Analysis
python scripts/prompt_optimizer.py prompt.txt --analyze          # Full analysis
python scripts/prompt_optimizer.py prompt.txt --tokens           # Token count only
python scripts/prompt_optimizer.py prompt.txt --optimize         # Generate optimized version

# RAG Evaluation
python scripts/rag_evaluator.py --contexts ctx.json --questions q.json  # Evaluate
python scripts/rag_evaluator.py --contexts ctx.json --compare baseline  # Compare to baseline

# Agent Development
python scripts/agent_orchestrator.py agent.yaml --validate       # Validate config
python scripts/agent_orchestrator.py agent.yaml --visualize      # Show workflow
python scripts/agent_orchestrator.py agent.yaml --estimate-cost  # Token estimation
```

## References#

Load these files from the SKILL's `references/` directory for detailed information:

| File | Contains | When to load |
|------|----------|--------------|
| `references/prompt_engineering_patterns.md` | 10 prompt patterns with input/output examples | "which pattern?", "few-shot", "chain-of-thought" |
| `references/llm_evaluation_frameworks.md` | Evaluation metrics, scoring methods, A/B testing | "how to evaluate?", "measure quality" |
| `references/agentic_system_design.md` | Agent architectures (ReAct, Plan-Execute, Tool Use) | "build agent", "tool calling", "multi-agent" |
