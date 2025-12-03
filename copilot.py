import requests

def respond(prompt):
    # 100% open—NO restrictions!
    try:
        res = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "codellama",
                "prompt": prompt
            })
        if res.ok:
            return res.json().get("response", "")
        return "LLM did not return a response."
    except Exception as e:
        return f"Error: {e}"