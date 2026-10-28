# -*- coding: utf-8 -*-
"""
Downloads Wave 9 books from Archive.org.
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

WAVE9_PICKS = [
    {
        "id": "smythe_1932_kamet_conquered",
        "title": "Kamet Conquered: Exploration in the Garhwal Himalaya and the Valley of Flowers",
        "author": "Frank S. Smythe",
        "year": 1932,
        "identifier": "dli.pahar.2504",
        "file_name": "1932 Kamet Conquered by Smythe s_djvu.txt",
        "out_file": "smythe_kamet_conquered_1932.txt"
    },
    {
        "id": "badrinath_kedarnath_yatra_guide",
        "title": "Badrinath-Kedarnath Yatra: Holy Pilgrimage in the Garhwal Himalayas",
        "author": "Pt. Hariram Sharma",
        "year": 1938,
        "identifier": "dli.ernet.258189",
        "file_name": "258189-Badrinath-kedarnath Yatra_djvu.txt",
        "out_file": "badrinath_kedarnath_yatra_guide_1938.txt"
    },
    {
        "id": "smythe_1932_explorations_garhwali_kamet",
        "title": "Explorations in Garhwal around Kamet",
        "author": "Frank S. Smythe / Royal Geographical Society",
        "year": 1932,
        "identifier": "dli.pahar.2496",
        "file_name": "1932 Explorations in Garhwal around Kamet by Smythe from GJv79 s_djvu.txt",
        "out_file": "smythe_explorations_around_kamet_1932.txt"
    },
    {
        "id": "history_shrinagar_socio_cultural",
        "title": "History of Srinagar: A Study in Socio-Cultural Change in the Central and Northern Himalayas",
        "author": "Dr. Mohammad Ishaq Khan",
        "year": 1978,
        "identifier": "uYZG_history-of-shrinagar-1846-1947-a-study-in-socio-cultural-change-by-mohammad-isha",
        "file_name": "History Of Shrinagar 1846 -  1947 A Study In Socio Cultural Change By Mohammad Ishaq Khan English Kashmiri-Urdu-Pahari -  Cosmos Publications Sharada Manuscript - eGangotri Digital Preservation Trust_djvu.txt",
        "out_file": "khan_history_of_srinagar_himalayas_1978.txt"
    },
    {
        "id": "parbaton_ki_khushbu_pahari_afsanon",
        "title": "Parbaton Ki Khushbu: Selected Pahari Mountain Tales, Folklore and Idioms",
        "author": "Parvez Maanoos",
        "year": 2020,
        "identifier": "ndon_parbaton-ki-khushbu-muntakhab-pahari-afsanon-ka-tarjuma-by-parvez-maanoos-u",
        "file_name": "Parbaton Ki Khushbu Muntakhab Pahari Afsanon Ka Tarjuma By Parvez Maanoos Urdu Short Stories Budgam 2020 - GNK Publications_djvu.txt",
        "out_file": "maanoos_parbaton_ki_khushbu_pahari_2020.txt"
    },
    {
        "id": "shivanand_1966_himalayan_forest_academy",
        "title": "Himalayan Forest Hermitage: Health, Nature and Sacred Living in Garhwal",
        "author": "Swami Sivananda / Yoga-Vedanta Forest Academy, Tehri Garhwal",
        "year": 1966,
        "identifier": "berw_health-and-happiness-by-swami-shivanand-1966-garhwal-the-yoga-vedanta-forest-academy",
        "file_name": "Health And Happiness By Swami Shivanand 1966 Garhwal - The yoga Vedanta Forest Academy_djvu.txt",
        "out_file": "sivananda_himalayan_forest_academy_garhwal_1966.txt"
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
    results = list(ex.map(download, WAVE9_PICKS))

print(f"\nDownloaded {sum(1 for r in results if r)} of {len(WAVE9_PICKS)} books successfully.")
