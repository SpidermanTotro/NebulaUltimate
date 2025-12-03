import requests

def respond(prompt, chat_history=None, context=None, system_prompt=None):
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
        r = requests.post("http://localhost:11434/api/generate", json=payload)
        if r.ok:
            return r.json().get("response", "")
        return "Local LLM did not return a response."
    except Exception as e:
        return f"ChatGPT agent error: {e}"