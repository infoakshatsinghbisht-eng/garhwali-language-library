# -*- coding: utf-8 -*-
import json
import urllib.request
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

picks = [
    ("dli.pahar.0789", "Settlement of Pargana Jaunsar Bawar"),
    ("dli.pahar.3163", "Himalayan Polyandry Jaunsar Bawar"),
    ("wbsl.14555", "Working Plan Deoban Range Jaunsar Forest Division 1889"),
    ("in.ernet.dli.2015.452383", "Himtirth Badrinath"),
    ("in.ernet.dli.2015.79797", "The Ascent of Nanda Devi Tilman 1937"),
    ("languepin-1956-to-kiss-high-heaven-nanda-devi", "To Kiss High Heaven Nanda Devi 1956")
]

for ident, title in picks:
    url = f"https://archive.org/metadata/{ident}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt") or f.get("name", "").endswith(".txt")]
            print(f"=== {ident} ({title}) ===")
            for t in txts:
                print("  TXT:", t.get("name"), t.get("size"))
    except Exception as e:
        print(f"ERR {ident}: {e}")

