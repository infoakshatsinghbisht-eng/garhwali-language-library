# -*- coding: utf-8 -*-
"""
Search Archive.org for Wave 8 candidate books on Garhwal / Pahari / Uttarakhand.
"""

import urllib.request
import urllib.parse
import json
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

with open("garhwali/culture/data/bibliography.json", "r", encoding="utf-8") as f:
    biblio = json.load(f)
existing_archive_ids = {b.get("archive_id") for b in biblio if b.get("archive_id")}

queries = [
    'title:(Garhwal) mediatype:texts',
    'title:(Pahari) mediatype:texts',
    'title:(Himalaya) AND description:(Garhwal) mediatype:texts',
    'description:(Tehri Garhwal) mediatype:texts',
    'description:(Alaknanda) mediatype:texts',
    'title:(Kumaun) AND description:(Garhwal) mediatype:texts',
    'title:(Badrinath) mediatype:texts',
    'dli.pahar Garhwal'
]

candidates = {}

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,description&rows=50&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for doc in data.get("response", {}).get("docs", []):
                ident = doc.get("identifier")
                if ident and ident not in existing_archive_ids and ident not in candidates:
                    candidates[ident] = doc
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(candidates)} candidate items.")

def test_candidate(ident, meta):
    url_meta = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url_meta, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt") and int(f.get("size", 0)) > 50000]
            if not txts:
                return None
            best = sorted(txts, key=lambda x: int(x.get("size", 0)), reverse=True)[0]
            fname = best["name"]
            sz = int(best["size"])

            # Test 100 bytes download to verify NO 401 Unauthorized
            dl_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(fname)}"
            dl_req = urllib.request.Request(dl_url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-100"})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=6) as dl_resp:
                if dl_resp.status in (200, 206):
                    return {
                        "identifier": ident,
                        "title": meta.get("title"),
                        "creator": meta.get("creator"),
                        "year": meta.get("year"),
                        "file_name": fname,
                        "size_bytes": sz
                    }
    except Exception:
        pass
    return None

confirmed = []
for ident, meta in list(candidates.items())[:60]:
    res = test_candidate(ident, meta)
    if res:
        confirmed.append(res)
        print(f"CONFIRMED: [{res['identifier']}] {res['title']} ({res['size_bytes']//1024} KB) -> {res['file_name']}", flush=True)
        if len(confirmed) >= 12:
            break

with open("data_sources/wave8_confirmed.json", "w", encoding="utf-8") as f:
    json.dump(confirmed, f, ensure_ascii=False, indent=2)

print(f"\nSaved {len(confirmed)} confirmed open access books to data_sources/wave8_confirmed.json")

