# -*- coding: utf-8 -*-
import urllib.request
import ssl

ctx = ssl._create_unverified_context()
url = "https://archive.org/download/dli.pahar.2868/1947%20Garhwal%20Himalaya%20by%20Roch_djvu.txt"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        print("Status:", resp.status)
        head = resp.read(200)
        print("Head:", len(head))
except Exception as e:
    print("Error:", e)

