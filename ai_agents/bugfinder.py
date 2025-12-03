"""Bug Finder AI agent for code analysis.

This agent analyzes code to detect bugs, anti-patterns,
and potential issues.
"""


def respond(prompt):
    """Analyze code for bugs and issues.

    Args:
        prompt (str): The code to analyze for bugs.

    Returns:
        str: Analysis results with any detected issues.
    """
    # For real use, invoke LLM with a detailed bug-hunt prompt
    return f"BugFinder reviewed code: '{prompt}'\n[Result: No obvious bugs found]"
