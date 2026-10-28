# -*- coding: utf-8 -*-
import json
import urllib.request
import ssl

ctx = ssl._create_unverified_context()

WAVE5_PICKS = [
    {
        "id": "mumm_1909_five_months_in_himalaya_garhwal",
        "title": "Five Months in the Himalaya: A Record of Mountain Travel in Garhwal",
        "author": "A. L. Mumm",
        "year": 1909,
        "identifier": "india.history.resource.91859",
        "out_file": "mumm_five_months_in_himalaya_garhwal_1909.txt"
    },
    {
        "id": "up_govt_1919_kumaun_garhwal_local_customs",
        "title": "Kumaun and Garhwal: Local Customs and Usages",
        "author": "Government of United Provinces",
        "year": 1919,
        "identifier": "india.history.resource.88082",
        "out_file": "up_govt_kumaun_garhwal_local_customs_1919.txt"
    },
    {
        "id": "verma_2003_pahari_dictionary_part3",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 3)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "identifier": "bvp-03883",
        "out_file": "verma_pahari_dictionary_part3_2003.txt"
    },
    {
        "id": "himalayan_folklore_1920_legends",
        "title": "Himalayan Folklore: Legends and Traditions of Kumaon and Garhwal",
        "author": "Rev. E. S. Oakley",
        "year": 1920,
        "identifier": "in.ernet.dli.2015.108282",
        "out_file": "oakley_himalayan_folklore_legends_1920.txt"
    },
    {
        "id": "dictionary_pahari_1911_dialects",
        "title": "Dictionary of Pahari Dialects of the Western and Central Himalayas",
        "author": "Government Press, Punjab & United Provinces",
        "year": 1911,
        "identifier": "dli.pahar.1894",
        "out_file": "dictionary_pahari_dialects_punjab_himalaya_1911.txt"
    },
    {
        "id": "himalayan_letters_1927_pilgrimage",
        "title": "The Himalayan Letters of Gypsy Davy and Lady Ba: Pilgrimage in Garhwal",
        "author": "Gypsy Davy and Lady Ba",
        "year": 1927,
        "identifier": "the-himalayan-letters-of-gypsy-davy-and-lady-ba-written-on-pilgrimage-to-the-hig",
        "out_file": "gypsy_davy_himalayan_letters_pilgrimage_1927.txt"
    }
]

for p in WAVE5_PICKS:
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

with open("data_sources/wave5_verified.json", "w", encoding="utf-8") as f:
    json.dump(WAVE5_PICKS, f, ensure_ascii=False, indent=2)
print("Saved to data_sources/wave5_verified.json")
