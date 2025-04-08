import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_code(code):
    body = {
        "model": "llama3",
        "prompt": f"Summarize this Go function:\n\n{code}",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=body)
        response.raise_for_status()
        json_response = response.json()

        if "response" not in json_response:
            print("❌ API error:", json_response)
            return "[ERROR: No summary received]"

        return json_response["response"].strip()

    except Exception as e:
        print("❌ Failed to parse response:", str(e))
        return f"[ERROR: {str(e)}]"