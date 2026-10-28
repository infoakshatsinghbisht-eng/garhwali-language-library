# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("data_sources/wave10_confirmed.json", "r", encoding="utf-8") as f:
    confirmed = json.load(f)

for c in confirmed:
    title = c.get("title", "")
    ident = c.get("identifier", "")
    creator = c.get("creator", "")
    fname = c.get("file_name", "")
    sz = c.get("size_bytes", 0) // 1024
    if any(k in title.lower() for k in ["gangotri", "nanda", "khatling", "fauna", "pilgrimage", "heaven"]):
        print(f"[{ident}] {title} | Creator: {creator} | File: {fname} ({sz} KB)")
