# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

candidates = [
    'dli.csl.3036', # UP District Gazetteers: Garhwal (1989)
    'GarhwalPainting', # Garhwal Painting by Mukandi Lal (1968)
    'dli.pahar.2397', # Khasa Family Law in the Himalayan Districts (1929) - L.D. Joshi
    'linguisticstudie00bailrich', # Linguistic Studies from the Himalayas (1915) - T. Grahame Bailey
    'in.ernet.dli.2015.223292', # A Dictionary of Pahari Dialects (1909)
    '1989-pahari-hindi-shabdkosh-by-haacl_202108', # Pahari-Hindi Shabdkosh (1989)
    'in.ernet.dli.2015.46900', # Himalayan Districts Vol 1 - Atkinson (1882)
]

for c in candidates:
    url = f"https://archive.org/metadata/{c}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            meta = data.get('metadata', {})
            files = data.get('files', [])
            txts = [f for f in files if f.get('name', '').endswith('.txt') and not f.get('name', '').endswith('_meta.txt')]
            print(f"ID: {c}")
            print(f"  Title: {meta.get('title')}")
            print(f"  Creator: {meta.get('creator')}")
            print(f"  Year: {meta.get('year')}")
            for t in txts:
                print(f"    txt: {t.get('name')} ({t.get('size')} bytes)")
    except Exception as e:
        print(f"Error {c}: {e}")

