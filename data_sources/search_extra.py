# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

extra_queries = [
    'title:(garhwal OR kumaon) AND (itihas OR kosh OR shabdkosh OR vyakaran OR geet OR bhasha)',
    'creator:(dabral OR raturi OR pokhriyal OR bartwal OR "satya prasad" OR nautiyal) AND mediatype:texts',
    'title:("garhwal ka itihas" OR "uttarakhand ka itihas") AND mediatype:texts',
    'title:(himalayan) AND (folklore OR songs OR ballads OR proverbs) AND mediatype:texts',
]

seen = set()
for q in extra_queries:
    url = f'https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year&rows=25&output=json'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for d in data.get('response', {}).get('docs', []):
                ident = d.get('identifier')
                if ident and ident not in seen:
                    seen.add(ident)
                    print(f"{ident} | {d.get('year')} | {str(d.get('creator'))[:25]} | {str(d.get('title'))[:50]}")
    except Exception as e:
        print(f"Error {q}: {e}")

