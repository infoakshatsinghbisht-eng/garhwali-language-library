# -*- coding: utf-8 -*-
"""
Downloads Wave 3 Garhwali, Central Pahari, and Himalayan books from Archive.org
with unverified SSL context to handle certificate expiration on Python Windows.
"""

import urllib.request
import urllib.parse
import ssl
import os
import sys

DOWNLOAD_DIR = "data_sources/raw_texts"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

ctx = ssl._create_unverified_context()

WAVE3_BOOKS = [
    {
        "id": "pauw_1896_tenth_settlement_garhwal",
        "title": "Report on the Tenth Settlement of the Garhwal District",
        "author": "E. K. Pauw",
        "year": 1896,
        "identifier": "dli.pahar.1406",
        "file_name": "1896 Report on Tenth Settlement of Garhwal District by Pauw s_djvu.txt",
        "out_file": "pauw_report_tenth_settlement_garhwal_1896.txt"
    },
    {
        "id": "atkinson_1884_himalayan_districts_vol2",
        "title": "The Himalayan Districts of North-Western Provinces of India Vol. 2",
        "author": "Edwin T. Atkinson",
        "year": 1884,
        "identifier": "dli.pahar.1048",
        "file_name": "1884 Himalayan Districts of North-Western Provinces of India by Atkinson Vol 2 s_djvu.txt",
        "out_file": "atkinson_himalayan_districts_vol2_1884.txt"
    },
    {
        "id": "atkinson_1883_notes_history_himalayan",
        "title": "Notes on the History of the Himalayan Districts of the N.W.P. India",
        "author": "Edwin T. Atkinson",
        "year": 1883,
        "identifier": "dli.pahar.1033",
        "file_name": "1883 Notes on the History of the Himalayan Districts of the N.W.P. India by Atkinson s_djvu.txt",
        "out_file": "atkinson_notes_history_himalayan_districts_1883.txt"
    },
    {
        "id": "traill_1828_statistical_sketch_kumaon_garhwal",
        "title": "Statistical Sketch of Kumaon and Garhwal",
        "author": "George William Traill",
        "year": 1828,
        "identifier": "in.ernet.dli.2015.53201",
        "file_name": "2015.53201.Statistical-Sketch-Of-Kumaon_djvu.txt",
        "out_file": "traill_statistical_sketch_kumaon_garhwal_1828.txt"
    },
    {
        "id": "upreti_1900_hill_dialects_kumaun_division",
        "title": "Hill Dialects of the Kumaun Division (Central Pahari)",
        "author": "Pandit Ganga Datt Upreti",
        "year": 1900,
        "identifier": "dli.csl.7734",
        "file_name": "7734_djvu.txt",
        "out_file": "upreti_hill_dialects_kumaun_division_1900.txt"
    },
    {
        "id": "walton_1911_dehra_dun_gazetteer",
        "title": "Dehra Dun: A Gazetteer (District Gazetteers of the United Provinces Vol. 1)",
        "author": "H. G. Walton",
        "year": 1911,
        "identifier": "in.ernet.dli.2015.94182",
        "file_name": "2015.94182.Dehra-Duna-Gazetteervol1_djvu.txt",
        "out_file": "walton_dehra_dun_gazetteer_1911.txt"
    },
    {
        "id": "verma_2004_pahari_dictionary_dialects",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 North-Western Himalayan Dialects",
        "author": "Dr. Siddheshwar Varma",
        "year": 2004,
        "identifier": "bvp-02718",
        "file_name": "BVP02718-PUC-Dr.-Siddheshwar-Varma`s-Pahari-Dictionary-of-27-North-Western-Himalayan-Dialects,-Vol.-II,-Part-Second-(Pahari-Group)_djvu.txt",
        "out_file": "verma_pahari_dictionary_27_dialects_2004.txt"
    },
    {
        "id": "iias_2002_pahari_bhasha_sahitya",
        "title": "Pahari Bhasha Tatha Sahitya",
        "author": "Indian Institute of Advanced Study",
        "year": 2002,
        "identifier": "pahari-bhasha-tatha-sahitya",
        "file_name": "G4376_djvu.txt",
        "out_file": "iias_pahari_bhasha_tatha_sahitya_2002.txt"
    }
]

def download_book(b):
    out_path = os.path.join(DOWNLOAD_DIR, b["out_file"])
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"Already downloaded: {b['title']} ({os.path.getsize(out_path)//1024} KB)")
        return True
    
    url = f"https://archive.org/download/{b['identifier']}/{urllib.parse.quote(b['file_name'])}"
    print(f"Downloading {b['title']} from {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
            with open(out_path, "wb") as f:
                f.write(data)
            print(f"SUCCESS: {b['title']} -> {b['out_file']} ({len(data)//1024} KB)")
            return True
    except Exception as e:
        print(f"ERROR downloading {b['title']}: {e}")
        return False

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(download_book, WAVE3_BOOKS))
    print(f"\nDownloaded {sum(1 for r in results if r)} of {len(WAVE3_BOOKS)} books successfully.")
