import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def summarize_code(code):
    body = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [
            {"role": "system", "content": "You are a senior Go developer."},
            {"role": "user", "content": f"Summarize this Go function:\n\n{code}"}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    try:
        json_response = response.json()
        if "choices" not in json_response:
            print("❌ API error:", json_response)
            return "[ERROR: No summary received]"
        return json_response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print("❌ Failed to parse response:", response.text)
        return f"[ERROR: {str(e)}]"