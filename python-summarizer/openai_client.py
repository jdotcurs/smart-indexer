import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_code(code):
    body = {
        "model": "llama3",
        "prompt": (
            "You are a senior Go developer. Summarize the following Go function in a strict structured format with no intro, no conclusion, no explanation, and no extra commentary. "
            "Only return the following sections:\n\n"
            "DO NOT include any other text or commentary such as 'Here is the summary of the function' or 'Here is the function' or 'Here is the function in a strict structured format' or anything like that. \n\n"
            "1. **Function Name**\n"
            "2. **Purpose**\n"
            "3. **Inputs**\n"
            "4. **Output**\n"
            "5. **Behavior**\n"
            "6. **Side Effects**\n"
            "7. **Related Concepts**\n"
            "8. **Optional Example Usage**\n\n"
            "Function:\n\n"
            f"{code}"
        ),
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