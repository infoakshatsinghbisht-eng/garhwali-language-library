import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    'garhwali AND mediatype:texts',
    'गढ़वाली AND mediatype:texts',
    'title:(garhwali) AND mediatype:texts',
    'title:(garhwal) AND subject:(language OR folklore OR dialect OR proverbs OR poetry) AND mediatype:texts',
    'subject:(garhwali) AND mediatype:texts',
    'Govind Chatak AND mediatype:texts',
    'Tara Dutt Gairola AND mediatype:texts',
    'Ganga Datt Upreti AND mediatype:texts',
]

seen_ids = set()
results = []

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year,description,downloads&sort[]=downloads+desc&rows=50&output=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            docs = data.get('response', {}).get('docs', [])
            for doc in docs:
                ident = doc.get('identifier')
                if ident and ident not in seen_ids:
                    seen_ids.add(ident)
                    results.append(doc)
    except Exception as e:
        print(f"Error for query '{q}': {e}", file=sys.stderr)

print(f"Total unique books found: {len(results)}")
for r in results[:40]:
    title = str(r.get('title', ''))[:60]
    creator = str(r.get('creator', ''))[:30]
    year = str(r.get('year', ''))
    print(f"{r.get('identifier')} | {year} | {creator} | {title}")
