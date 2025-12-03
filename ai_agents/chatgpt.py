"""ChatGPT-style AI agent for Nebula Ultimate.

This agent provides conversational AI capabilities using a local
LLM server for natural language interactions.
"""

import requests

REQUEST_TIMEOUT = 30  # seconds


def respond(prompt, chat_history=None, system_prompt=None):
    """Generate a conversational response to a prompt.

    Args:
        prompt (str): The user's message or question.
        chat_history (list, optional): Previous conversation history.
        system_prompt (str, optional): System prompt for context.

    Returns:
        str: The generated response from the LLM.
    """
    # Calls your local LLM server (e.g., ollama, GPT4All, etc)
    try:
        payload = {
            "model": "llama3",  # or "codellama", "ggml", etc.
            "prompt": prompt
        }
        if system_prompt:
            payload["system"] = system_prompt
        if chat_history:
            payload["chat_history"] = chat_history
        res = requests.post(
            "http://localhost:11434/api/generate",
            json=payload,
            timeout=REQUEST_TIMEOUT
        )
        if res.ok:
            return res.json().get("response", "")
        return "Local LLM did not return a response."
    except requests.exceptions.RequestException as e:
        return f"ChatGPT agent error: {e}"
