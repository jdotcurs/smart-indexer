import json
import os
from openai_client import summarize_code

summaries_path = "../output/summaries.json"
chunks_path = "../output/code_chunks/"
debug_path = "../output/_debug_summaries.json"

# Load summaries
with open(summaries_path, "r") as f:
    summaries = json.load(f)

# Ensure debug file starts fresh
if not os.path.exists(debug_path):
    with open(debug_path, "w") as f:
        json.dump({}, f)

# Load or create debug summaries
with open(debug_path, "r") as f:
    debug_summaries = json.load(f)

# Save function to write to debug file after each summary
def save_debug():
    try:
        with open(debug_path, "w") as f:
            json.dump(debug_summaries, f, indent=2)
        print(f"💾 Saved to {debug_path}")
    except Exception as e:
        print(f"❌ Failed to write to debug file: {e}")

# Main summarization loop
for fn_id, entry in summaries.items():
    if fn_id in debug_summaries and debug_summaries[fn_id].get("summary"):
        continue  # Skip already summarized

    try:
        code_file_path = os.path.join(chunks_path, f"{entry['hash']}.txt")
        with open(code_file_path, "r") as code_file:
            code = code_file.read()

        summary = summarize_code(code).strip()

        # Print result
        print(f"\n🧠 Summary for {fn_id}:\n{summary}\n")

        # Store in debug file
        debug_summaries[fn_id] = {
            "summary": summary,
            "hash": entry["hash"],
            "file": entry.get("path", "[unknown file]")
        }

        save_debug()

    except Exception as e:
        print(f"❌ Error for {fn_id}: {e}")