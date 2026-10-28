# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

queries = [
    'title:(garhwal OR garhwali OR kumaun OR pahari) AND mediatype:texts',
    'creator:(raturi OR bahuguna OR gairola OR dabral OR "govind chatak" OR upreti) AND mediatype:texts',
    'subject:(garhwali OR "central pahari" OR pahari OR garhwal) AND mediatype:texts',
    '"garhwal" AND (folklore OR songs OR grammar OR dialect OR language OR history OR ballads) AND mediatype:texts',
    '"garhwal ka itihas" AND mediatype:texts',
    'title:(himalayan OR uttarakhand) AND (folklore OR language OR dialects OR songs) AND mediatype:texts'
]

seen = set()
for q in queries:
    url = f'https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,downloads,mediatype&sort[]=downloads+desc&rows=40&output=json'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for d in data.get('response', {}).get('docs', []):
                ident = d.get('identifier')
                if ident and ident not in seen:
                    seen.add(ident)
                    print(f"{ident} | {d.get('year', '')} | {str(d.get('creator', ''))[:30]} | {str(d.get('title', ''))[:60]}")
    except Exception as e:
        print(f"Error for {q}: {e}")

print(f"\nTotal unique items: {len(seen)}")

