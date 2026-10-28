# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("data_sources/wave10_confirmed.json", "r", encoding="utf-8") as f:
    confirmed = json.load(f)

with open("garhwali/culture/data/bibliography.json", "r", encoding="utf-8") as f:
    biblio = json.load(f)
existing_archive_ids = {b.get("archive_id") for b in biblio if b.get("archive_id")}

unused = [c for c in confirmed if c["identifier"] not in existing_archive_ids]
print(f"Total confirmed in wave10: {len(confirmed)}")
print(f"Unused in wave10: {len(unused)}")
for u in unused[:20]:
    sz = u["size_bytes"] // 1024
    print(f"[{u['identifier']}] {u['title']} | Creator: {u.get('creator')} | File: {u['file_name']} ({sz} KB)")

