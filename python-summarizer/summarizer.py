import json
import os
from openai_client import summarize_code

# Define paths
summaries_path = "../output/summaries.json"
chunks_path = "../output/code_chunks/"
debug_path = "../output/_debug_summaries.json"

# Ensure all output directories exist
os.makedirs(os.path.dirname(summaries_path), exist_ok=True)
os.makedirs(chunks_path, exist_ok=True)

def ensure_json_file(filepath, default_content=None):
    """Ensure a JSON file exists and contains valid JSON."""
    if default_content is None:
        default_content = {}
    
    try:
        if not os.path.exists(filepath):
            print(f"⚠️ No file found at {filepath}, creating empty one")
            with open(filepath, "w") as f:
                json.dump(default_content, f, indent=2)
            return default_content

        with open(filepath, "r") as f:
            content = json.load(f)
            return content
    except json.JSONDecodeError:
        print(f"⚠️ Invalid JSON in {filepath}, starting fresh")
        with open(filepath, "w") as f:
            json.dump(default_content, f, indent=2)
        return default_content
    except Exception as e:
        print(f"❌ Error handling {filepath}: {e}")
        return default_content

# Load or initialize files
summaries = ensure_json_file(summaries_path)
debug_summaries = ensure_json_file(debug_path)

# Save function to write to debug file after each summary
def save_debug():
    try:
        with open(debug_path, "w") as f:
            json.dump(debug_summaries, f, indent=2)
        print(f"💾 Saved to {debug_path}")
    except Exception as e:
        print(f"❌ Failed to write to debug file: {e}")

# Main summarization loop
print(f"📚 Found {len(summaries)} functions to process")

for fn_id, entry in summaries.items():
    if fn_id in debug_summaries and debug_summaries[fn_id].get("summary"):
        print(f"⏭️  Skipping {fn_id} (already summarized)")
        continue

    try:
        code_file_path = os.path.join(chunks_path, f"{entry['hash']}.txt")
        print(f"🔍 Processing {fn_id} from {code_file_path}")
        
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

print("\n✅ Done processing all functions!")