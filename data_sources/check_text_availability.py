# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ids = [
    'in.ernet.dli.2015.530003',
    'in.ernet.dli.2015.181556',
    'languagesofnorth00bailrich',
    '1978-pahari-language-a-linguistic-analysis-verma',
    'dli.csl.3107',
    'in.ernet.dli.2015.309034',
    'garhwal-me-kon-kahan-se_20250415',
    'wnbl_uttarakhand-ka-itihas-bhag-3-rajnaitik-tatha-sanskritik-itihas-by-shiv-pras',
    'ozkb_uttarakhand-ka-itihas-katyuri-yug-tak-bhag-1-sakshya-sankalan-by-shiv-prasa'
]

for i in ids:
    try:
        url = f"https://archive.org/metadata/{i}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            meta = data.get('metadata', {})
            files = data.get('files', [])
            txts = [f for f in files if f.get('name', '').endswith('.txt') and not f.get('name', '').endswith('_meta.txt')]
            print(f"ID: {i}")
            print(f"  Title: {meta.get('title')}")
            print(f"  Creator: {meta.get('creator')}")
            print(f"  Year: {meta.get('year')}")
            for t in txts:
                print(f"    txt: {t.get('name')} ({t.get('size')} bytes)")
    except Exception as e:
        print(f"Error {i}: {e}")

