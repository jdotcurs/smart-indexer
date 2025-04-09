import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def summarize_code(code):
    prompt = (
    "You are a senior Go developer. Read the following Go function and respond ONLY with a strict JSON object "
    "containing the following fields:\n\n"
    "- function_name: string\n"
    "- purpose: string\n"
    "- inputs: array of strings\n"
    "- output: array of strings\n"
    "- behavior: array of strings\n"
    "- side_effects: array of strings\n"
    "- related_concepts: array of strings\n"
    "- optional_example_usage: string\n\n"
    "DO NOT include any explanation, commentary, or text outside of the JSON object.\n\n"
    "Function:\n\n"
    f"{code}"
    )
    body = {
        "model": "llama3",
        "prompt": prompt,
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