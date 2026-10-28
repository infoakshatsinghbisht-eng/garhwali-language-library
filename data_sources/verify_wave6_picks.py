# -*- coding: utf-8 -*-
import json
import urllib.request
import ssl

ctx = ssl._create_unverified_context()

WAVE6_PICKS = [
    {
        "id": "sherring_1906_western_tibet_british_borderland",
        "title": "Western Tibet and the British Borderland: Garhwal and Bhotia Customs",
        "author": "Charles A. Sherring",
        "year": 1906,
        "identifier": "westerntibetbrit00sher",
        "out_file": "sherring_western_tibet_british_borderland_1906.txt"
    },
    {
        "id": "batten_1851_official_reports_kumaon_garhwal",
        "title": "Official Reports on the Province of Kumaon and Garhwal",
        "author": "J. H. Batten",
        "year": 1851,
        "identifier": "dli.pahar.0412",
        "out_file": "batten_official_reports_kumaon_garhwal_1851.txt"
    },
    {
        "id": "bisht_1994_tourism_garhwal_himalaya",
        "title": "Tourism in Garhwal Himalaya: Pilgrimage, Culture and Economy",
        "author": "Dr. Harshwanti Bisht",
        "year": 1994,
        "identifier": "tourism-in-garhwal-himalaya-by-harshwanti-bisht-to",
        "out_file": "bisht_tourism_in_garhwal_himalaya_1994.txt"
    },
    {
        "id": "khanduri_1986_peaks_passes_garhwal",
        "title": "Peaks and Passes of the Garhwal Himalaya",
        "author": "Garhwal Exploration Society",
        "year": 1986,
        "identifier": "dli.pahar.3635",
        "out_file": "khanduri_peaks_and_passes_garhwal_1986.txt"
    },
    {
        "id": "bhatt_1992_garhwal_himalaya_nature_culture",
        "title": "Garhwal Himalaya: Nature, Culture and Society",
        "author": "H. P. Bhatt et al.",
        "year": 1992,
        "identifier": "GarhwalHimalaya",
        "out_file": "bhatt_garhwal_himalaya_nature_culture_1992.txt"
    },
    {
        "id": "verma_2003_pahari_dictionary_part2",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 2)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "identifier": "bvp-03865",
        "out_file": "verma_pahari_dictionary_part2_2003.txt"
    }
]

for p in WAVE6_PICKS:
    url = f"https://archive.org/metadata/{p['identifier']}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            txts = [f for f in files if f.get("name", "").endswith("_djvu.txt")]
            if txts:
                p["file_name"] = txts[0].get("name")
                p["size_bytes"] = int(txts[0].get("size", 0))
                print(f"VERIFIED: {p['id']} -> {p['file_name']} ({p['size_bytes']//1024} KB)")
    except Exception as e:
        print(f"ERROR: {p['id']} -> {e}")

with open("data_sources/wave6_verified.json", "w", encoding="utf-8") as f:
    json.dump(WAVE6_PICKS, f, ensure_ascii=False, indent=2)
print("Saved to data_sources/wave6_verified.json")
