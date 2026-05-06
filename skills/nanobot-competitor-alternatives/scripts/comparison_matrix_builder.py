PORTING_DOC = """
[Agent Usage Reminder]

You called a search/fetch tool directly without leveraging specialized agents.

RECOMMENDED: Use task with explore/librarian agents for better results:

```\n// Parallel exploration - fire multiple agents simultaneously\ntask(subagent_type=\"explore\", load_skills=[], prompt=\"Find all files matching pattern X\")\ntask(subagent_type=\"explore\", load_skills=[], prompt=\"Search for implementation of Y\")\ntask(subagent_type=\"librarian\", load_skills=[], prompt=\"Lookup documentation for Z\")\n\n// Then continue your work while they run in background\n// System will notify you when each completes\n```\n
WHY:\n+- Agents can perform deeper, more thorough searches\n+- Background tasks run in parallel, saving time\n+- Specialized agents have domain expertise\n+- Reduces context window usage in main session\n
ALWAYS prefer: Multiple parallel task calls > Direct tool calls
"""
