# -*- coding: utf-8 -*-
"""
Download Wave 2 primary source books from Internet Archive for Garhwali digital corpus.
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

WAVE2_BOOKS = [
    {
        "id": "dli.csl.3036",
        "filename": "3036_djvu.txt",
        "save_name": "up_gazetteer_garhwal_1989.txt",
        "title": "Uttar Pradesh District Gazetteers: Garhwal",
        "author": "Government of Uttar Pradesh (Swami Prasad Singh et al.)",
        "year": 1989
    },
    {
        "id": "GarhwalPainting",
        "filename": "Garhwal-Painting_djvu.txt",
        "save_name": "mukandi_lal_garhwal_painting_1968.txt",
        "title": "Garhwal Painting",
        "author": "Mukandi Lal",
        "year": 1968
    },
    {
        "id": "dli.pahar.2397",
        "filename": "1929 Khasa Family Law in the Himalayan Districts of United Provinces India by Joshi s_djvu.txt",
        "save_name": "joshi_khasa_family_law_himalayan_districts_1929.txt",
        "title": "Khasa Family Law in the Himalayan Districts",
        "author": "L. D. Joshi",
        "year": 1929
    },
    {
        "id": "linguisticstudie00bailrich",
        "filename": "linguisticstudie00bailrich_djvu.txt",
        "save_name": "bailey_linguistic_studies_from_the_himalayas_1915.txt",
        "title": "Linguistic Studies from the Himalayas",
        "author": "Rev. Thomas Grahame Bailey",
        "year": 1915
    },
    {
        "id": "in.ernet.dli.2015.223292",
        "filename": "2015.223292.A-Dictionary_djvu.txt",
        "save_name": "dictionary_of_pahari_dialects_1909.txt",
        "title": "A Dictionary of Pahari Dialects",
        "author": "Himachal Academy of Arts, Culture and Languages",
        "year": 1909
    },
    {
        "id": "1989-pahari-hindi-shabdkosh-by-haacl_202108",
        "filename": "Pahari-Hindi Shabdkosh_djvu.txt",
        "save_name": "pahari_hindi_shabdkosh_1989.txt",
        "title": "Pahari-Hindi Shabdkosh",
        "author": "Himachal Academy of Arts, Culture and Languages",
        "year": 1989
    },
    {
        "id": "in.ernet.dli.2015.46900",
        "filename": "2015.46900.The-Himalayan-Districts--Vol-1_djvu.txt",
        "save_name": "atkinson_himalayan_districts_vol1_1882.txt",
        "title": "The Himalayan Districts of the North-Western Provinces Vol. 1",
        "author": "Edwin T. Atkinson",
        "year": 1882
    }
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for b in WAVE2_BOOKS:
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

print("Wave 2 download script finished.")

