# -*- coding: utf-8 -*-
"""
Download new primary source books from Internet Archive for Garhwali digital corpus.
"""
import os
import sys
import json
import urllib.request
import ssl

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

DEST_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")
os.makedirs(DEST_DIR, exist_ok=True)

NEW_BOOKS = [
    {
        "id": "in.ernet.dli.2015.530003",
        "filename": "2015.530003.garhwal-ancient_djvu.txt",
        "save_name": "pati_ram_garhwal_ancient_and_modern_1916.txt",
        "title": "Garhwal Ancient and Modern",
        "author": "Rai Pati Ram Bahadur",
        "year": 1916
    },
    {
        "id": "in.ernet.dli.2015.181556",
        "filename": "2015.181556.British-Garhwal---A-Gazetteer_djvu.txt",
        "save_name": "walton_british_garhwal_gazetteer_1910.txt",
        "title": "British Garhwal: A Gazetteer",
        "author": "H. G. Walton",
        "year": 1910
    },
    {
        "id": "languagesofnorth00bailrich",
        "filename": "languagesofnorth00bailrich_djvu.txt",
        "save_name": "bailey_languages_of_northern_himalayas_1908.txt",
        "title": "The Languages of the Northern Himalayas",
        "author": "Rev. Thomas Grahame Bailey",
        "year": 1908
    },
    {
        "id": "1978-pahari-language-a-linguistic-analysis-verma",
        "filename": "Pahari Language- A Linguistics Analysis_djvu.txt",
        "save_name": "verma_pahari_language_linguistic_analysis_1978.txt",
        "title": "Pahari Language: A Linguistic Analysis",
        "author": "Dr. Siddheshwar Verma",
        "year": 1978
    },
    {
        "id": "dli.csl.3107",
        "filename": "3107_djvu.txt",
        "save_name": "up_gazetteer_tehri_garhwal_1971.txt",
        "title": "Uttar Pradesh District Gazetteers: Tehri Garhwal",
        "author": "Government of Uttar Pradesh (C.P. Sharma et al.)",
        "year": 1971
    },
    {
        "id": "in.ernet.dli.2015.309034",
        "filename": "2015.309034.Shri-Uttarakhand_djvu.txt",
        "save_name": "dabral_shri_uttarakhand_yatra_darshan.txt",
        "title": "Shri Uttarakhand Yatra Darshan",
        "author": "Dr. Shiv Prasad Dabral 'Charan'",
        "year": 1961
    },
    {
        "id": "garhwal-me-kon-kahan-se_20250415",
        "filename": "garhwal me kon kahan se_djvu.txt",
        "save_name": "barthwal_garhwal_me_kon_kahan_se_1938.txt",
        "title": "Garhwal Mein Kaun Kahan Se",
        "author": "Mahidhar Sharma Barthwal",
        "year": 1938
    },
    {
        "id": "wnbl_uttarakhand-ka-itihas-bhag-3-rajnaitik-tatha-sanskritik-itihas-by-shiv-pras",
        "filename": "Uttarakhand Ka Itihas Bhag 3 Rajnaitik Tatha Sanskritik Itihas By Shiv Prasad Dabral Charan Hindi History Illustrated Dogadda Garhwal 2026 - Veer Gatha Prakashan_djvu.txt",
        "save_name": "dabral_uttarakhand_ka_itihas_bhag3.txt",
        "title": "Uttarakhand Ka Itihas Bhag 3: Rajnaitik Tatha Sanskritik Itihas",
        "author": "Dr. Shiv Prasad Dabral 'Charan'",
        "year": 1971
    },
    {
        "id": "ozkb_uttarakhand-ka-itihas-katyuri-yug-tak-bhag-1-sakshya-sankalan-by-shiv-prasa",
        "filename": "Uttarakhand Ka Itihas Katyuri Yug Tak Bhag 1 Sakshya Sankalan By Shiv Prasad Dabral Charan Hindi History Dogadda Garhwal 1965 - Veer Gatha Prakashan_djvu.txt",
        "save_name": "dabral_uttarakhand_ka_itihas_bhag1.txt",
        "title": "Uttarakhand Ka Itihas Bhag 1: Katyuri Yug Tak Sakshya Sankalan",
        "author": "Dr. Shiv Prasad Dabral 'Charan'",
        "year": 1965
    }
]

# Disable SSL verification for archive.org downloads if needed
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for b in NEW_BOOKS:
    save_path = os.path.join(DEST_DIR, b["save_name"])
    if os.path.exists(save_path) and os.path.getsize(save_path) > 1000:
        print(f"Already downloaded: {b['save_name']} ({os.path.getsize(save_path)} bytes)")
        continue
    
    url = f"https://archive.org/download/{b['id']}/{urllib.parse.quote(b['filename'])}"
    print(f"Downloading {b['title']} from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp, open(save_path, "wb") as out:
            data = resp.read()
            out.write(data)
        print(f"Downloaded: {b['save_name']} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed to download {b['id']}: {e}")

print("Download script finished.")

