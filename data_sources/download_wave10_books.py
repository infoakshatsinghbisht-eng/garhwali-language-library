# -*- coding: utf-8 -*-
"""
Downloads Wave 10 books from Archive.org.
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

WAVE10_PICKS = [
    {
        "id": "prabodhanand_1961_across_gangotri_glaciers",
        "title": "Across Gangotri Glaciers: Explorations in Northern Garhwal",
        "author": "Swami Prabodhanand",
        "year": 1961,
        "identifier": "dli.pahar.3173",
        "file_name": "1961 Across Gangotri Glaciers by Prabodhanand s_djvu.txt",
        "out_file": "prabodhanand_across_gangotri_glaciers_1961.txt"
    },
    {
        "id": "painuli_2000_shri_nandadevi_rajjat",
        "title": "Shri Nanda Devi Raj Jat: The Royal Himalayan Pilgrimage of Garhwal",
        "author": "Shiv Kumar Painuli, Dr. Anusuya Prasad Maikhuri & Dr. Bhagwati Prasad Purohit",
        "year": 2000,
        "identifier": "20260126_20260126_0914",
        "file_name": "श्री नन्दादेवी राजजात 2000_djvu.txt",
        "out_file": "painuli_shri_nandadevi_rajjat_2000.txt"
    },
    {
        "id": "shipton_1936_nanda_devi",
        "title": "Nanda Devi: Exploration of the Great Himalayan Sanctuary",
        "author": "Eric Shipton",
        "year": 1936,
        "identifier": "dli.pahar.2644",
        "file_name": "1936 Nanda Devi by Shipton s_djvu.txt",
        "out_file": "shipton_nanda_devi_1936.txt"
    },
    {
        "id": "shipton_1935_nanda_devi_ganges_watershed",
        "title": "Nanda Devi and the Ganges Watershed: Mountain Topography of Garhwal",
        "author": "Eric Shipton",
        "year": 1935,
        "identifier": "dli.pahar.2609",
        "file_name": "1935 Nanda Devi and Ganges Watershed by Shipton from GJv85 s_djvu.txt",
        "out_file": "shipton_nanda_devi_ganges_watershed_1935.txt"
    },
    {
        "id": "zsi_1997_fauna_nandadevi_biosphere",
        "title": "Fauna of Nanda Devi Biosphere Reserve: Mammals, Birds and Mountain Wildlife",
        "author": "Zoological Survey of India (ZSI)",
        "year": 1997,
        "identifier": "dli.zoological.cas.009",
        "file_name": "index_djvu.txt",
        "out_file": "zsi_fauna_nandadevi_biosphere_1997.txt"
    },
    {
        "id": "negi_gaur_1985_flora_khatling_glacier_tehri",
        "title": "Flora of Khatling Glacier in the Garhwal Himalaya (District Tehri)",
        "author": "K. S. Negi, J. K. Tiwari & R. D. Gaur (HNB Garhwal University)",
        "year": 1985,
        "identifier": "biostor-153424",
        "file_name": "biostor-153424_djvu.txt",
        "out_file": "negi_gaur_flora_khatling_glacier_tehri_1985.txt"
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
    results = list(ex.map(download, WAVE10_PICKS))

print(f"\nDownloaded {sum(1 for r in results if r)} of {len(WAVE10_PICKS)} books successfully.")
