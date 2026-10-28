# -*- coding: utf-8 -*-
import json

with open("data_sources/wave3_available.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Get current book IDs in index
with open("garhwali/culture/data/books/index.json", "r", encoding="utf-8") as f:
    existing_books = json.load(f)

existing_ids = {b["id"] for b in existing_books}
print(f"Total existing books: {len(existing_ids)}")
print(f"Total items in wave3_available: {len(items)}")

for it in items:
    print(f"[{it['identifier']}] {it['title'][:55]} | Year: {it['year']} | Size: {it['size_kb']} KB")

