# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

tests = [
    {
        "id": "shrestha_grammar_of_pahari",
        "ident": "AGrammarOfPahariPhDDissertationByOmkareshworShrestha",
        "file": "A Grammar of Pahari, PhD Dissertation by Omkareshwor Shrestha_djvu.txt",
        "out": "shrestha_grammar_of_pahari_phd.txt"
    },
    {
        "id": "thakur_1975_pahari_bhasha",
        "ident": "hpaul58808",
        "file": "(1975) Pahari Bhasha--Kului ke Vishesh Sandrabh Mein_djvu.txt",
        "out": "thakur_pahari_bhasha_kullui_1975.txt"
    },
    {
        "id": "roch_1947_garhwal_himalaya",
        "ident": "dli.pahar.2868",
        "file": "1947 Garhwal Himalaya by Roch_djvu.txt",
        "out": "roch_garhwal_himalaya_1947.txt"
    }
]

for t in tests:
    url = f"https://archive.org/download/{t['ident']}/{urllib.parse.quote(t['file'])}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        print(f"Testing {t['id']} from {url}...")
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
            with open(f"data_sources/raw_texts/{t['out']}", "wb") as f:
                f.write(data)
            print(f"SUCCESS: {t['id']} -> {t['out']} ({len(data)//1024} KB)")
    except Exception as e:
        print(f"ERROR: {t['id']} -> {e}")

