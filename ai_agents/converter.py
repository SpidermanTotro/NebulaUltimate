"""Code Converter AI agent for language translation.

This agent converts code between different programming languages
using an ensemble of AI services.
"""

import requests

REQUEST_TIMEOUT = 30  # seconds


def respond(prompt, from_lang="python", to_lang="rust"):
    """Convert code from one programming language to another.

    Args:
        prompt (str): The source code to convert.
        from_lang (str): The source programming language. Defaults to "python".
        to_lang (str): The target programming language. Defaults to "rust".

    Returns:
        str: The converted code or an error message.
    """
    # Call your own API, or use an ensemble of AIs for better translation
    url = "http://localhost:5000/convert"
    try:
        res = requests.post(url, json={
            "input": prompt,
            "from": from_lang,
            "to": to_lang
        }, timeout=REQUEST_TIMEOUT)
        if res.ok:
            return res.json()["output"]
        return "Conversion error: check server."
    except requests.exceptions.RequestException as e:
        return f"Converter error: {e}"
