# -*- coding: utf-8 -*-
"""
Search Archive.org for additional Garhwali and Himalayan books.
"""

import urllib.request
import urllib.parse
import json

queries = [
    'title:(stowell) AND (kumaun OR garhwal) AND mediatype:texts',
    'title:(almanac OR panchang OR bhasha) AND (garhwal OR kumaun) AND mediatype:texts',
    'title:(himalayan) AND (folklore OR songs OR ballads) AND mediatype:texts',
    'title:(uttarakhand) AND (bhag OR itihas OR sanskriti) AND mediatype:texts',
    'creator:("tara datt gairola" OR "bhagirath" OR "mola ram") AND mediatype:texts'
]

results = {}
for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,mediatype&rows=20&page=1&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
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
        print(f"Error {e}")

print(f"Discovered {len(results)} additional candidates.")

# Check for djvu.txt
from concurrent.futures import ThreadPoolExecutor

available = []
def check(item):
    ident, meta = item
    url = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
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
                        "size_kb": sz // 1024
                    }
    except Exception:
        pass
    return None

with ThreadPoolExecutor(max_workers=8) as ex:
    for r in ex.map(check, results.items()):
        if r:
            print(f"AVAILABLE: [{r['identifier']}] {r['title'][:50]} | {r['size_kb']} KB")
            available.append(r)

with open("data_sources/wave4_extra_available.json", "w", encoding="utf-8") as f:
    json.dump(available, f, ensure_ascii=False, indent=2)

print(f"Saved {len(available)} extra available texts.")

