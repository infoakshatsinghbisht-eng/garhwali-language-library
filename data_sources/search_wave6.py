# -*- coding: utf-8 -*-
"""
Search for Wave 6 Garhwali, Central Pahari, and Himalayan books on Archive.org.
"""

import urllib.request
import urllib.parse
import json
import ssl
from concurrent.futures import ThreadPoolExecutor

ctx = ssl._create_unverified_context()

queries = [
    'title:("holy himalaya") AND creator:(oakley) AND mediatype:texts',
    'title:("western tibet and the british borderland") AND creator:(sherring) AND mediatype:texts',
    'title:("bhotia") AND (kumaon OR garhwal) AND mediatype:texts',
    'title:("official reports") AND creator:(batten) AND mediatype:texts',
    'title:(garhwal) AND (pilgrimage OR temple OR himalaya) AND mediatype:texts',
    'title:(pahari) AND (grammar OR dictionary OR dialect) AND mediatype:texts'
]

results = {}
for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,mediatype&rows=20&page=1&output=json"
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

with ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(check, results.items()):
        if r:
            print(f"FOUND: [{r['identifier']}] {r['title'][:55]} | {r['size_kb']} KB")
            available.append(r)

with open("data_sources/wave6_available.json", "w", encoding="utf-8") as f:
    json.dump(available, f, ensure_ascii=False, indent=2)

print(f"Saved {len(available)} available texts to data_sources/wave6_available.json")

