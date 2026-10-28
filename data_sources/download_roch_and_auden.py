# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

items = [
    {
        "id": "roch_1947_garhwal_himalaya",
        "ident": "dli.pahar.2868",
        "file": "1947 Garhwal Himalaya by Roch_djvu.txt",
        "out": "roch_garhwal_himalaya_1947.txt"
    },
    {
        "id": "auden_1936_structure_himalaya_garhwal",
        "ident": "dli.pahar.2649",
        "file": "1936 Structure of the Himalaya in Garhwal by Auden from Records GSI v71 s_djvu.txt",
        "out": "auden_structure_himalaya_garhwal_1936.txt"
    }
]

for it in items:
    url = f"https://archive.org/download/{it['ident']}/{urllib.parse.quote(it['file'])}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        print(f"Downloading {it['id']} from {url}...")
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
            with open(f"data_sources/raw_texts/{it['out']}", "wb") as f:
                f.write(data)
            print(f"SUCCESS: {it['id']} -> {it['out']} ({len(data)//1024} KB)")
    except Exception as e:
        print(f"ERROR: {it['id']} -> {e}")

