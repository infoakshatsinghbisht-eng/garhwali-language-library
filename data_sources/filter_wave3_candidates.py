# -*- coding: utf-8 -*-
import json
import urllib.request

with open("data_sources/wave3_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

print(f"Checking {len(candidates)} candidates for djvu.txt files...")

available = []
for ident, meta in candidates.items():
    title = str(meta.get("title", ""))
    creator = str(meta.get("creator", ""))
    year = meta.get("year", "")
    
    # We want works related to Garhwal, Pahari, Himalayan districts, gazetteers, history, linguistics
    # Skip items already in our 29 books
    url = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            files_data = json.loads(resp.read().decode("utf-8")).get("result", [])
            txt_files = [f for f in files_data if f.get("name", "").endswith("_djvu.txt")]
            if txt_files:
                txt_info = txt_files[0]
                size = int(txt_info.get("size", 0))
                if size > 50000: # at least 50KB text
                    print(f"FOUND: [{ident}] {title[:60]} | {creator[:30]} | {year} | Size: {size//1024} KB")
                    available.append({
                        "identifier": ident,
                        "title": title,
                        "creator": creator,
                        "year": year,
                        "file_name": txt_info.get("name"),
                        "size_bytes": size,
                        "size_kb": size // 1024
                    })
    except Exception as e:
        continue

print(f"\nTotal available with full djvu.txt: {len(available)}")
with open("data_sources/wave3_available.json", "w", encoding="utf-8") as f:
    json.dump(available, f, ensure_ascii=False, indent=2)

