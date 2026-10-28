# -*- coding: utf-8 -*-
"""
Search Archive.org for candidate Wave 7 books on Garhwal / Pahari / Uttarakhand.
"""

import urllib.request
import urllib.parse
import json
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

queries = [
    'Garhwal mediatype:texts',
    'Garhwali mediatype:texts',
    'Pahari language mediatype:texts',
    'Tehri Garhwal mediatype:texts',
    'Himalayan folklore mediatype:texts',
    'Kumaun Garhwal mediatype:texts',
    'Uttarakhand history mediatype:texts',
    'Central Pahari mediatype:texts',
    'Himalaya mountaineering Garhwal mediatype:texts',
    'Badrinath Kedarnath travel mediatype:texts'
]

with open("garhwali/culture/data/bibliography.json", "r", encoding="utf-8") as f:
    biblio = json.load(f)
existing_archive_ids = {b.get("archive_id") for b in biblio if b.get("archive_id")}

with open("garhwali/culture/data/books/index.json", "r", encoding="utf-8") as f:
    books = json.load(f)
existing_book_ids = {b["id"] for b in books}

print(f"Existing catalogued archive IDs: {len(existing_archive_ids)}")
print(f"Existing digital books in corpus: {len(existing_book_ids)}")

found_candidates = {}

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,description,mediatype&rows=50&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            docs = data.get("response", {}).get("docs", [])
            for d in docs:
                ident = d.get("identifier")
                title = d.get("title", "")
                if ident and ident not in existing_archive_ids and ident not in found_candidates:
                    found_candidates[ident] = {
                        "identifier": ident,
                        "title": title,
                        "creator": d.get("creator", "Unknown"),
                        "year": d.get("year", "Unknown"),
                        "description": (d.get("description", "") or "")[:200]
                    }
    except Exception as e:
        print(f"Error querying {q}: {e}")

print(f"Found {len(found_candidates)} candidate works on Archive.org.")

with open("data_sources/wave7_candidates.json", "w", encoding="utf-8") as f:
    json.dump(list(found_candidates.values()), f, ensure_ascii=False, indent=2)

print("Saved to data_sources/wave7_candidates.json")

