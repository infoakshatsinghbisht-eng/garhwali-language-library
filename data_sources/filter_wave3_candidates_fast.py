# -*- coding: utf-8 -*-
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

with open("data_sources/wave3_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Skip identifiers we already have in books index
with open("garhwali/culture/data/books/index.json", "r", encoding="utf-8") as f:
    existing_books = json.load(f)

existing_ids = set()
for b in existing_books:
    existing_ids.add(b.get("id"))

print(f"Total candidates to check: {len(candidates)}")

available = []

def check_item(ident_meta):
    ident, meta = ident_meta
    title = str(meta.get("title", ""))
    creator = str(meta.get("creator", ""))
    year = meta.get("year", "")
    
    url = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            files_data = json.loads(resp.read().decode("utf-8")).get("result", [])
            txt_files = [f for f in files_data if f.get("name", "").endswith("_djvu.txt")]
            if txt_files:
                txt_info = txt_files[0]
                size = int(txt_info.get("size", 0))
                if size > 60000: # at least 60KB
                    return {
                        "identifier": ident,
                        "title": title,
                        "creator": creator,
                        "year": year,
                        "file_name": txt_info.get("name"),
                        "size_bytes": size,
                        "size_kb": size // 1024
                    }
    except Exception:
        pass
    return None

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(check_item, item) for item in candidates.items()]
    for fut in as_completed(futures):
        res = fut.result()
        if res:
            print(f"FOUND: [{res['identifier']}] {res['title'][:50]} | {res['size_kb']} KB")
            available.append(res)

print(f"\nTotal available with full djvu.txt: {len(available)}")
with open("data_sources/wave3_available.json", "w", encoding="utf-8") as f:
    json.dump(available, f, ensure_ascii=False, indent=2)
print("Saved to data_sources/wave3_available.json")
