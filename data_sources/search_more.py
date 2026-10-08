import urllib.request
import urllib.parse
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    'title:("Garhwal Ka Itihas") AND mediatype:texts',
    'creator:("Govind Chatak") AND mediatype:texts',
    'creator:("Hari Krishna Raturi") AND mediatype:texts',
    'title:("Garhwali Lokgeet") AND mediatype:texts',
    'title:("Garhwali") AND mediatype:texts',
]

for q in queries:
    url = f"https://archive.org/advancedsearch.php?q={urllib.parse.quote(q)}&fl[]=identifier,title,creator,year&rows=10&output=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for d in data.get('response', {}).get('docs', []):
                print(f"{d.get('identifier')} | {d.get('year')} | {d.get('creator')} | {d.get('title')}")
    except Exception as e:
        print(f"Error {q}: {e}")
