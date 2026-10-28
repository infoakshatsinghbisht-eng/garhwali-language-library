# -*- coding: utf-8 -*-
import json
import urllib.request
import ssl
import os

ctx = ssl._create_unverified_context()

WAVE4_CANDIDATES = [
    {
        "id": "dabral_1965_bhotantik_alaknanda",
        "title": "Uttarakhand Ke Bhotantik: Alaknanda Upatyaka Mein Pravas (Bhag 2)",
        "author": "Dr. Shiv Prasad Dabral 'Charan'",
        "year": 1965,
        "identifier": "xhed_uttarakhand-ke-bhotantik-alaknanda-upatyaka-mein-pravas-bhag-2-by-shivapras",
        "out_file": "dabral_uttarakhand_ke_bhotantik_alaknanda_1965.txt"
    },
    {
        "id": "atkinson_1886_himalayan_districts_vol3",
        "title": "The Himalayan Districts of the North-Western Provinces Vol. 3",
        "author": "Edwin T. Atkinson",
        "year": 1886,
        "identifier": "wbsl.19297",
        "out_file": "atkinson_himalayan_districts_vol3_1886.txt"
    },
    {
        "id": "stowell_1916_kumaun_garhwali_customary_rulings",
        "title": "Kumaun Rulings for Civil Courts (Customary Law of Kumaun and Garhwal)",
        "author": "V. A. Stowell",
        "year": 1916,
        "identifier": "kqqg-kumaun-rulings-for-civil-courts-by-v-a-stowell-law",
        "out_file": "stowell_kumaun_garhwali_customary_rulings_1916.txt"
    },
    {
        "id": "british_records_1842_historical_papers_garhwal",
        "title": "Historical Papers Relating to Kumaun and Garhwal 1809-1842",
        "author": "Government of North-Western Provinces",
        "year": 1842,
        "identifier": "bcxu_historical-papers-relating-to-kumaun-1809-1842-selections-from-english-reco",
        "out_file": "british_records_historical_papers_garhwal_1842.txt"
    },
    {
        "id": "shrestha_2004_grammar_of_pahari",
        "title": "A Grammar of Pahari: Phonology, Morphology and Syntax",
        "author": "Dr. Omkareshwor Shrestha",
        "year": 2004,
        "identifier": "AGrammarOfPahariPhDDissertationByOmkareshworShrestha",
        "out_file": "shrestha_grammar_of_pahari_2004.txt"
    },
    {
        "id": "oakley_1935_himalayan_folklore_west_himalayas",
        "title": "Himalayan Folklore: Legends and Epics of Kumaon and Garhwal",
        "author": "Rev. E. S. Oakley and Tara Dutt Gairola",
        "year": 1935,
        "identifier": "in.ernet.dli.2015.532407",
        "out_file": "oakley_gairola_himalayan_folklore_extended_1935.txt"
    },
    {
        "id": "verma_2003_pahari_dictionary_vol1",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 North-Western Himalayan Dialects (Vol. 1)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "identifier": "bvp-03866",
        "out_file": "verma_pahari_dictionary_vol1_2003.txt"
    }
]

# Find file names for each
for c in WAVE4_CANDIDATES:
    url = f"https://archive.org/metadata/{c['identifier']}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt")]
            if txts:
                c["file_name"] = txts[0].get("name")
                c["size_bytes"] = int(txts[0].get("size", 0))
                print(f"Verified {c['id']}: {c['file_name']} ({c['size_bytes']//1024} KB)")
    except Exception as e:
        print(f"Error checking {c['id']}: {e}")

with open("data_sources/wave4_verified.json", "w", encoding="utf-8") as f:
    json.dump(WAVE4_CANDIDATES, f, ensure_ascii=False, indent=2)
print("Saved to data_sources/wave4_verified.json")

