import openai

openai.api_key = "your-api-key"

def summarize_code(code: str) -> str:
    prompt = f"Summarize this Go function:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message["content"].strip()