# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl

ctx = ssl._create_unverified_context()

tests = [
    {
        "id": "mountains_northern_sikkim_garhwal",
        "ident": "dli.pahar.1942",
        "file": "1936 Mountains of Northern Sikkim and Garhwal from AJ v48 s_djvu.txt",
        "out": "mountains_northern_sikkim_garhwal_1936.txt"
    },
    {
        "id": "chalyaan_suraan_pahari",
        "ident": "HUqe_chalyaan-suraan-pahari-iqbal-nazish",
        "file": "Chalyaan Suraan Pahari - Iqbal Nazish_djvu.txt",
        "out": "chalyaan_suraan_pahari_nazish.txt"
    }
]

for t in tests:
    url = f"https://archive.org/download/{t['ident']}/{urllib.parse.quote(t['file'])}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        print(f"Downloading {t['id']}...")
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
            with open(f"data_sources/raw_texts/{t['out']}", "wb") as f:
                f.write(data)
            print(f"SUCCESS: {t['id']} -> {t['out']} ({len(data)//1024} KB)")
            break
    except Exception as e:
        print(f"ERROR: {t['id']} -> {e}")

