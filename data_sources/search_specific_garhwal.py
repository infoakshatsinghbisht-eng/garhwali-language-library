# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

queries = [
    'title:(Garhwal) mediatype:texts',
    'title:(Himalaya) AND description:(Garhwal) mediatype:texts',
    'title:(Uttarakhand) mediatype:texts',
    'title:(Nanda Devi) mediatype:texts',
    'title:(Badrinath) mediatype:texts',
    'title:(Kedarnath) mediatype:texts',
    'description:(Tehri Garhwal) mediatype:texts',
    'title:(Pahari) AND mediatype:texts'
]

with open("garhwali/culture/data/books/index.json", "r", encoding="utf-8") as f:
    books = json.load(f)
existing_ids = {b["id"] for b in books}

results = {}

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,downloads,description&rows=50&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            docs = data.get("response", {}).get("docs", [])
            for d in docs:
                ident = d.get("identifier")
                if ident and ident not in results:
                    results[ident] = d
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(results)} additional items.")

# Verify which have _djvu.txt text
def check_item(ident):
    url = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt") and int(f.get("size", 0)) > 60000]
            if txts:
                best = sorted(txts, key=lambda x: int(x.get("size", 0)), reverse=True)[0]
                return best.get("name"), int(best.get("size", 0))
    except Exception:
        pass
    return None, 0

verified_items = []
for ident, meta in list(results.items()):
    fname, sz = check_item(ident)
    if fname:
        verified_items.append({
            "identifier": ident,
            "title": meta.get("title"),
            "creator": meta.get("creator"),
            "year": meta.get("year"),
            "file_name": fname,
            "size_bytes": sz
        })
        print(f"VERIFIED: [{ident}] {meta.get('title')} ({sz//1024} KB) -> {fname}")
        if len(verified_items) >= 20:
            break

with open("data_sources/wave7_specific_verified.json", "w", encoding="utf-8") as f:
    json.dump(verified_items, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(verified_items)} verified books to data_sources/wave7_specific_verified.json")

