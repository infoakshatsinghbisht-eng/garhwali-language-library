# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("data_sources/wave7_verified_candidates.json", "r", encoding="utf-8") as f:
    items = json.load(f)

for i, it in enumerate(items, 1):
    print(f"{i}. [{it['identifier']}] {it['title']} ({it['size_bytes']//1024} KB)")

