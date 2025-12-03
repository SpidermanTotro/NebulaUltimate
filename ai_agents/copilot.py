"""Copilot AI agent for code generation and assistance.

This agent provides code completion, generation, and explanation
capabilities using a local LLM backend.
"""

import requests

REQUEST_TIMEOUT = 30  # seconds


def respond(prompt):
    """Generate a response to a code-related prompt.

    Args:
        prompt (str): The code prompt or question.

    Returns:
        str: The generated response from the LLM.
    """
    # 100% open—NO restrictions!
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "codellama",
                "prompt": prompt
            },
            timeout=REQUEST_TIMEOUT)
        if res.ok:
            return res.json().get("response", "")
        return "LLM did not return a response."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
