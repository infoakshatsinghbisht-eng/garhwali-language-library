# -*- coding: utf-8 -*-
"""
Downloads Wave 11 books from Archive.org.
"""

import json
import urllib.request
import urllib.parse
import ssl
import os
import sys
from concurrent.futures import ThreadPoolExecutor

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()
DOWNLOAD_DIR = "data_sources/raw_texts"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

WAVE11_PICKS = [
    {
        "id": "ross_1874_settlement_jaunsar_bawar",
        "title": "Settlement of Pargana Jaunsar-Bawar: Customary Law and Land Tenure",
        "author": "H. G. Ross",
        "year": 1874,
        "identifier": "dli.pahar.0789",
        "file_name": "1874 Settlement of Pargana Jaunsar Bawar by Ross s_djvu.txt",
        "out_file": "ross_settlement_jaunsar_bawar_1874.txt"
    },
    {
        "id": "majumdar_1960_himalayan_polyandry_jaunsar",
        "title": "Himalayan Polyandry: Structure, Functioning and Culture Change in Jaunsar-Bawar",
        "author": "Dr. D. N. Majumdar",
        "year": 1960,
        "identifier": "dli.pahar.3163",
        "file_name": "1960 Himalayan Polyandry--structure functioning and culture change--a field-study of Jaunsar-Bawar by Majumdar s_djvu.txt",
        "out_file": "majumdar_himalayan_polyandry_jaunsar_1960.txt"
    },
    {
        "id": "hearth_1889_deoban_range_jaunsar_forest",
        "title": "Working Plan of the Deoban Range, Jaunsar Forest Division (N.-W. Provinces)",
        "author": "G. F. Hearth / Forest Department",
        "year": 1889,
        "identifier": "wbsl.14555",
        "file_name": "14555_djvu.txt",
        "out_file": "hearth_deoban_range_jaunsar_forest_1889.txt"
    },
    {
        "id": "sharma_1955_himtirtha_badrinath",
        "title": "Himtirth Badrinath: The Holy Himalayan Sanctum and Sacred Geography",
        "author": "Pt. Devendranath Sharma",
        "year": 1955,
        "identifier": "in.ernet.dli.2015.452383",
        "file_name": "2015.452383.Himtirtha-Badrinath-Ed-1st_djvu.txt",
        "out_file": "sharma_himtirtha_badrinath_1955.txt"
    },
    {
        "id": "tilman_1937_the_ascent_of_nanda_devi",
        "title": "The Ascent of Nanda Devi: First Historic Ascent of the Sanctuary Peak",
        "author": "H. W. Tilman",
        "year": 1937,
        "identifier": "in.ernet.dli.2015.79797",
        "file_name": "2015.79797.The-Ascent-Of-Nanda-Devi_djvu.txt",
        "out_file": "tilman_ascent_of_nanda_devi_1937.txt"
    },
    {
        "id": "languepin_1956_to_kiss_high_heaven_nanda_devi",
        "title": "To Kiss High Heaven: Nanda Devi and Trishul Himalayan Expeditions",
        "author": "J. J. Languepin",
        "year": 1956,
        "identifier": "languepin-1956-to-kiss-high-heaven-nanda-devi",
        "file_name": "Languepin 1956 To Kiss High Heaven Nanda Devi_djvu.txt",
        "out_file": "languepin_to_kiss_high_heaven_nanda_devi_1956.txt"
    }
]

def download(b):
    out_path = os.path.join(DOWNLOAD_DIR, b["out_file"])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"Already downloaded: {b['title']} ({os.path.getsize(out_path)//1024} KB)")
        return True

    url = f"https://archive.org/download/{b['identifier']}/{urllib.parse.quote(b['file_name'])}"
    print(f"Downloading {b['title']} from {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
            data = resp.read()
            with open(out_path, "wb") as f:
                f.write(data)
            print(f"SUCCESS: {b['title']} -> {b['out_file']} ({len(data)//1024} KB)")
            return True
    except Exception as e:
        print(f"ERROR downloading {b['title']}: {e}")
        return False

with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(download, WAVE11_PICKS))

print(f"\nDownloaded {sum(1 for r in results if r)} of {len(WAVE11_PICKS)} books successfully.")

