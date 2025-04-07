import json
from openai_client import summarize_code

with open("../output/summaries.json", "r") as f:
    summaries = json.load(f)

for fn_id, info in summaries.items():
    if not info["summary"]:
        with open(f"../output/code_chunks/{info['hash']}.txt") as code_file:
            code = code_file.read()
        summaries[fn_id]["summary"] = summarize_code(code)
        print(f"Summarized: {fn_id}")

with open("../output/summaries.json", "w") as f:
    json.dump(summaries, f, indent=2)