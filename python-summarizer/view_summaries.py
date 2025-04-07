import json

with open("../output/summaries.json", "r") as f:
    summaries = json.load(f)

for fn_hash, entry in summaries.items():
    summary = entry.get("summary", "").strip()
    if not summary:
        continue  # skip empty ones
    file = entry.get("file", "[unknown file]")
    print(f"\n🔹 {fn_hash} ({file})\n➡️  {summary}\n")