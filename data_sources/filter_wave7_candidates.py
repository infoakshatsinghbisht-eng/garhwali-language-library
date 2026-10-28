# -*- coding: utf-8 -*-
"""
Filter and rank Wave 7 candidate books.
"""

import json
import urllib.request
import ssl
import sys
from concurrent.futures import ThreadPoolExecutor

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

with open("data_sources/wave7_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

def str_val(val):
    if isinstance(val, list):
        return " ".join(str(v) for v in val)
    return str(val) if val else ""

# Priority keywords: garhwal, pahari, kumaun, himalaya, folklore, history, dialect, bhasha
def score_candidate(c):
    text = (str_val(c.get("title")) + " " + str_val(c.get("creator")) + " " + str_val(c.get("description"))).lower()
    score = 0
    if "garhwal" in text:
        score += 10
    if "pahari" in text:
        score += 8
    if "folklore" in text or "folk" in text:
        score += 5
    if "dialect" in text or "language" in text or "bhasha" in text:
        score += 7
    if "gazetteer" in text or "settlement" in text or "history" in text or "itihas" in text:
        score += 6
    if "kumaun" in text or "himalaya" in text:
        score += 3
    if "yatra" in text or "pilgrimage" in text or "travel" in text:
        score += 4
    return score

ranked = sorted(candidates, key=score_candidate, reverse=True)

print(f"Top 30 candidate titles:")
for idx, c in enumerate(ranked[:30], 1):
    print(f"{idx}. [{c['identifier']}] ({c.get('year')}) {c.get('title')} - by {c.get('creator')}")

# Now verify text file availability for top 25 candidates
def check_text(c):
    url = f"https://archive.org/metadata/{c['identifier']}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=6) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt") or (f.get("name", "").endswith(".txt") and int(f.get("size", 0)) > 50000)]
            if txts:
                best = sorted(txts, key=lambda x: int(x.get("size", 0)), reverse=True)[0]
                return {
                    "identifier": c["identifier"],
                    "title": c.get("title"),
                    "creator": c.get("creator"),
                    "year": c.get("year"),
                    "file_name": best.get("name"),
                    "size_bytes": int(best.get("size", 0))
                }
    except Exception:
        pass
    return None

print("\nChecking full-text availability in parallel...")
with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(check_text, ranked[:35]))

verified = [r for r in results if r]
print(f"Verified {len(verified)} candidates with available full text:")
for v in verified:
    print(f"  - [{v['identifier']}] {v['title']} ({v['size_bytes']//1024} KB) -> {v['file_name']}")

with open("data_sources/wave7_verified_candidates.json", "w", encoding="utf-8") as f:
    json.dump(verified, f, ensure_ascii=False, indent=2)

print("\nSaved to data_sources/wave7_verified_candidates.json")
