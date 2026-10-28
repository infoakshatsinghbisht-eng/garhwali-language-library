# -*- coding: utf-8 -*-
"""
Fast parallel search & verification of Wave 11 candidate books from Archive.org.
Focusing on:
- Jaunsar-Bawar / Rawalti (Western Garhwali dialect & culture)
- Tehri State & Bhagirathi Valley
- First Ascent of Nanda Devi (Tilman 1937)
- Himalayan Mountaineering in Garhwal (Languepin 1956)
- Badrinath & Kedarnath holy itineraries
"""

import urllib.request
import urllib.parse
import json
import ssl
import sys
from concurrent.futures import ThreadPoolExecutor

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

with open("garhwali/culture/data/bibliography.json", "r", encoding="utf-8") as f:
    biblio = json.load(f)
existing_archive_ids = {b.get("archive_id") for b in biblio if b.get("archive_id")}

queries = [
    'title:(Jaunsar) mediatype:texts',
    'title:(Jaunsari) mediatype:texts',
    'title:(Rawain) mediatype:texts',
    'title:(Tehri) mediatype:texts',
    'title:(Bhilangna) mediatype:texts',
    'title:(Badrinath) AND mediatype:texts',
    'title:(Kedarnath) AND mediatype:texts',
    'title:(Pahari) AND title:(Folk) mediatype:texts',
    'title:(Pahari) AND title:(Grammar) mediatype:texts',
    'dli.pahar Jaunsar',
    'dli.pahar Tehri',
    'dli.pahar Badrinath'
]

candidates = {}

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,description&rows=40&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/3.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for doc in data.get("response", {}).get("docs", []):
                ident = doc.get("identifier")
                if ident and ident not in existing_archive_ids and ident not in candidates:
                    candidates[ident] = doc
    except Exception as e:
        print(f"Error {q}: {e}", flush=True)

print(f"Discovered {len(candidates)} candidates.", flush=True)

def test_candidate(item):
    ident, meta = item
    url_meta = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url_meta, headers={"User-Agent": "GarhwaliLibraryBot/3.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [
                f for f in files 
                if (f.get("name", "").endswith("_djvu.txt") or f.get("name", "").endswith(".txt")) 
                and int(f.get("size", 0)) > 30000
            ]
            if not txts:
                return None
            best = sorted(txts, key=lambda x: int(x.get("size", 0)), reverse=True)[0]
            fname = best["name"]
            sz = int(best["size"])

            dl_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(fname)}"
            dl_req = urllib.request.Request(dl_url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-50"})
            with urllib.request.urlopen(dl_req, context=ctx, timeout=6) as dl_resp:
                if dl_resp.status in (200, 206):
                    res = {
                        "identifier": ident,
                        "title": meta.get("title"),
                        "creator": meta.get("creator"),
                        "year": meta.get("year"),
                        "file_name": fname,
                        "size_bytes": sz
                    }
                    print(f"CONFIRMED: [{ident}] {meta.get('title')} ({sz//1024} KB)", flush=True)
                    return res
    except Exception:
        pass
    return None

with ThreadPoolExecutor(max_workers=12) as ex:
    results = list(ex.map(test_candidate, list(candidates.items())[:120]))

confirmed = [r for r in results if r]
print(f"\nTotal confirmed open-access works: {len(confirmed)}", flush=True)

with open("data_sources/wave11_confirmed.json", "w", encoding="utf-8") as f:
    json.dump(confirmed, f, ensure_ascii=False, indent=2)

print("Saved to data_sources/wave11_confirmed.json", flush=True)

