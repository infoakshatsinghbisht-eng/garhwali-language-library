# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

search_queries = [
    'title:(garhwali OR garhwal OR pahari) AND (shabdkosh OR kosh OR dictionary OR vyakaran OR grammar)',
    'creator:("bahuguna" OR "dabral" OR "chatak" OR "raturi" OR "gairola" OR "bartwal" OR "atkinson") AND mediatype:texts',
    'title:(meghdoot OR gita OR geeta OR ramayana OR mahabharata) AND (garhwali OR pahari OR garhwal)',
    'title:("central pahari" OR "pahari dialects" OR "himalayan dialects" OR "garhwal gazetteer")',
    'subject:("garhwali" OR "central pahari" OR "pahari language") AND mediatype:texts',
    'title:("himalayan folklore" OR "himalayan districts" OR "garhwal painting")'
]

found = {}
for q in search_queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,downloads&sort[]=downloads+desc&rows=30&output=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for doc in data.get('response', {}).get('docs', []):
                ident = doc.get('identifier')
                if ident and ident not in found:
                    found[ident] = doc
                    print(f"{ident} | {doc.get('year')} | {str(doc.get('creator'))[:25]} | {str(doc.get('title'))[:55]}")
    except Exception as e:
        print(f"Error {q}: {e}")

print(f"\nTotal new items found: {len(found)}")

