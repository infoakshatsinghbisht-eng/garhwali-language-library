# -*- coding: utf-8 -*-
"""
Search for Wave 3 Garhwali, Central Pahari, and Himalayan books on Archive.org.
"""

import urllib.request
import urllib.parse
import json
import sys

queries = [
    'title:(himalayan districts) AND creator:(atkinson) AND mediatype:texts',
    'title:(uttarakhand ka itihas) AND mediatype:texts',
    'title:(garhwal OR garhwali) AND (gazetteer OR report OR history OR folklore OR songs OR bhasha) AND mediatype:texts',
    'title:(statistical sketch) AND (kumaon OR garhwal) AND mediatype:texts',
    'title:(kumaun garhwal OR "kumaon and garhwal") AND mediatype:texts',
    'creator:(dabral) AND (uttarakhand OR garhwal) AND mediatype:texts',
    'title:(pahari) AND (grammar OR dictionary OR bhasha OR shabdkosh) AND mediatype:texts',
    'title:(dehra dun) AND creator:(walton) AND mediatype:texts'
]

results = {}
for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,mediatype,publicdate&rows=20&page=1&output=json"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
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
        print(f"Error for query {q[:30]}: {e}")

print(f"Total candidate identifiers found: {len(results)}")
with open("data_sources/wave3_candidates.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to data_sources/wave3_candidates.json")

