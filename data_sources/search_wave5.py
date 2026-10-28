# -*- coding: utf-8 -*-
"""
Search for Wave 5 Garhwali and Central Pahari books on Archive.org.
"""

import urllib.request
import urllib.parse
import json
import ssl
from concurrent.futures import ThreadPoolExecutor

ctx = ssl._create_unverified_context()

queries = [
    'title:(batten) AND (kumaon OR garhwal) AND mediatype:texts',
    'title:(beckett) AND (garhwal OR settlement) AND mediatype:texts',
    'title:(pahari) AND (grammar OR dictionary OR folklore) AND mediatype:texts',
    'creator:(dabral) AND mediatype:texts',
    'title:(himalayan) AND (districts OR gazetteer OR folklore) AND mediatype:texts',
    'title:(garhwal) AND (songs OR tales OR travel OR pilgrims) AND mediatype:texts',
    'title:(kumaun) AND (folklore OR traditions OR tales) AND mediatype:texts'
]

results = {}
for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,mediatype&rows=25&page=1&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            docs = data.get("response", {}).get("docs", [])
            for d in docs:
                ident = d.get("identifier")
                if ident and ident not in results:
                    results[ident] = {
                        "title": d.get("title"),
                        "creator": d.get("creator"),
                        "year": d.get("year"),
                    }
    except Exception as e:
        print(f"Error {q[:30]}: {e}")

print(f"Discovered {len(results)} candidate identifiers.")

# Check for djvu.txt
available = []
def check(item):
    ident, meta = item
    url = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt")]
            if txts:
                sz = int(txts[0].get("size", 0))
                if sz > 50000:
                    return {
                        "identifier": ident,
                        "title": meta.get("title"),
                        "creator": meta.get("creator"),
                        "year": meta.get("year"),
                        "file_name": txts[0].get("name"),
                        "size_bytes": sz,
                        "size_kb": sz // 1024
                    }
    except Exception:
        pass
    return None

with ThreadPoolExecutor(max_workers=10) as ex:
    for r in ex.map(check, results.items()):
        if r:
            print(f"FOUND: [{r['identifier']}] {r['title'][:55]} | {r['size_kb']} KB")
            available.append(r)

with open("data_sources/wave5_available.json", "w", encoding="utf-8") as f:
    json.dump(available, f, ensure_ascii=False, indent=2)

print(f"Saved {len(available)} available texts to data_sources/wave5_available.json")

