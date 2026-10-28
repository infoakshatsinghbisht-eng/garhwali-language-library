# -*- coding: utf-8 -*-
"""
Find 3 open access books on Garhwal / Pahari from Archive.org (dli.pahar.* or public domain).
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
    'dli.pahar Garhwal mediatype:texts',
    'dli.pahar Pahari mediatype:texts',
    'dli.pahar Kumaon mediatype:texts',
    'dli.pahar Himalaya mediatype:texts',
    'collection:(pahar-in-library) Garhwal'
]

open_candidates = []

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,mediatype&rows=50&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for doc in data.get("response", {}).get("docs", []):
                ident = doc.get("identifier")
                if ident and ident not in existing_archive_ids:
                    open_candidates.append(doc)
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"Found {len(open_candidates)} candidates.")

# Test actual downloadability of _djvu.txt without 401
def test_direct_download(ident):
    url_meta = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url_meta, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt") and int(f.get("size", 0)) > 60000]
            if not txts:
                return None
            best = sorted(txts, key=lambda x: int(x.get("size", 0)), reverse=True)[0]
            fname = best["name"]
            sz = int(best["size"])
            
            # Test 1-byte read from download URL to ensure NO 401
            dl_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(fname)}"
            dl_req = urllib.request.Request(dl_url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-100"})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=6) as dl_resp:
                if dl_resp.status in (200, 206):
                    return fname, sz
    except Exception:
        pass
    return None

confirmed = []
for c in open_candidates:
    res = test_direct_download(c["identifier"])
    if res:
        fname, sz = res
        confirmed.append({
            "identifier": c["identifier"],
            "title": c.get("title"),
            "creator": c.get("creator"),
            "year": c.get("year"),
            "file_name": fname,
            "size_bytes": sz
        })
        print(f"CONFIRMED OPEN: [{c['identifier']}] {c.get('title')} ({sz//1024} KB) -> {fname}")
        if len(confirmed) >= 10:
            break

with open("data_sources/wave7_open_confirmed.json", "w", encoding="utf-8") as f:
    json.dump(confirmed, f, ensure_ascii=False, indent=2)

print(f"Saved {len(confirmed)} confirmed open access books.")

