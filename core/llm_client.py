import requests

class OpenSourceLLM:
    def __init__(self, model="llama3"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt[:8000],
            "stream": False,
            "options": {"temperature": 0}
        }

        r = requests.post(self.url, json=payload)
        if r.status_code != 200:
            return "The answer is not available on the provided website."

        return r.json().get("response", "").strip()
