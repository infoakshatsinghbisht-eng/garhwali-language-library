# -*- coding: utf-8 -*-
"""
Downloads Wave 8 books from Archive.org.
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

WAVE8_PICKS = [
    {
        "id": "lsi_pahari_ignca_vol9_pt4",
        "title": "Linguistic Survey of India: The Pahari Languages and Gujuri (Vol. 9, Pt. 4)",
        "author": "Sir George A. Grierson / IGNCA Edition",
        "year": 1916,
        "identifier": "in.gov.ignca.23438",
        "file_name": "23438_djvu.txt",
        "out_file": "lsi_pahari_languages_gujuri_ignca_1916.txt"
    },
    {
        "id": "tehri_garhwal_leased_forests_1897",
        "title": "Working Plan of the Tehri-Garhwal Leased Forests",
        "author": "Forest Department, North-Western Provinces",
        "year": 1897,
        "identifier": "wbsl.13950",
        "file_name": "13950_djvu.txt",
        "out_file": "tehri_garhwal_leased_forests_1897.txt"
    },
    {
        "id": "snow_balls_of_garhwal_1946",
        "title": "Snow Balls of Garhwal: Folk Songs, Ballads and Life in the Hills",
        "author": "N. S. Bhandari et al.",
        "year": 1946,
        "identifier": "in.ernet.dli.2015.85090",
        "file_name": "2015.85090.Snow-Balls-Of-Garhwal_djvu.txt",
        "out_file": "snow_balls_of_garhwal_1946.txt"
    },
    {
        "id": "strachey_1851_physical_geography_garhwal",
        "title": "On the Physical Geography of Kumáon and Garhwál in the Himálaya Mountains",
        "author": "Captain Richard Strachey",
        "year": 1851,
        "identifier": "jstor-1798183",
        "file_name": "jstor-1798183_djvu.txt",
        "out_file": "strachey_physical_geography_kumaon_garhwal_1851.txt"
    },
    {
        "id": "garhwal_eleventh_settlement_report_1933",
        "title": "Final Report on the Eleventh Revenue Settlement of Garhwal District",
        "author": "A. W. Ibbotson",
        "year": 1933,
        "identifier": "dli.pahar.2527",
        "file_name": "1933 Final Report on 11th Revenue Settlement of Garhwal District by Ibbotson s_djvu.txt",
        "out_file": "ibbotson_eleventh_settlement_garhwal_1933.txt"
    },
    {
        "id": "birds_lower_garhwal_himalayas",
        "title": "Birds and Natural History of Lower Garhwal Himalayas",
        "author": "Himalayan Natural History Society",
        "year": 1969,
        "identifier": "biostor-250867",
        "file_name": "biostor-250867_djvu.txt",
        "out_file": "birds_natural_history_lower_garhwal_1969.txt"
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
    results = list(ex.map(download, WAVE8_PICKS))

print(f"\nDownloaded {sum(1 for r in results if r)} of {len(WAVE8_PICKS)} books successfully.")

