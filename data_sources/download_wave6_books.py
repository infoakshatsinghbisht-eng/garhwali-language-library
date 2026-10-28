# -*- coding: utf-8 -*-
"""
Downloads Wave 6 books from Archive.org.
"""

import json
import urllib.request
import urllib.parse
import ssl
import os
from concurrent.futures import ThreadPoolExecutor

ctx = ssl._create_unverified_context()
DOWNLOAD_DIR = "data_sources/raw_texts"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

with open("data_sources/wave6_verified.json", "r", encoding="utf-8") as f:
    books = json.load(f)

def download(b):
    out_path = os.path.join(DOWNLOAD_DIR, b["out_file"])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"Already downloaded: {b['title']} ({os.path.getsize(out_path)//1024} KB)")
        return True
    
    url = f"https://archive.org/download/{b['identifier']}/{urllib.parse.quote(b['file_name'])}"
    print(f"Downloading {b['title']} from {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            data = resp.read()
            with open(out_path, "wb") as f:
                f.write(data)
            print(f"SUCCESS: {b['title']} -> {b['out_file']} ({len(data)//1024} KB)")
            return True
    except Exception as e:
        print(f"ERROR downloading {b['title']}: {e}")
        return False

with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(download, books))

print(f"\nDownloaded {sum(1 for r in results if r)} of {len(books)} books successfully.")
