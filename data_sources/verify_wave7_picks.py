# -*- coding: utf-8 -*-
import json
import urllib.request
import ssl
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ctx = ssl._create_unverified_context()

WAVE7_PICKS = [
    {
        "id": "fiol_2017_recasting_folk_himalayas",
        "title": "Recasting Folk in the Himalayas: Indian Music, Media, and Social Mobility",
        "author": "Stefan Patrick Fiol",
        "year": 2017,
        "identifier": "recastingfolkinh0000fiol",
        "file_name": "recastingfolkinh0000fiol_djvu.txt",
        "out_file": "fiol_recasting_folk_himalayas_2017.txt"
    },
    {
        "id": "alter_2000_knowing_dil_das_hunter",
        "title": "Knowing Dil Das: Stories of a Himalayan Hunter",
        "author": "Joseph S. Alter",
        "year": 2000,
        "identifier": "knowingdildassto0000alte",
        "file_name": "knowingdildassto0000alte_djvu.txt",
        "out_file": "alter_knowing_dil_das_himalayan_hunter_2000.txt"
    },
    {
        "id": "lewis_1995_himalayas_history_religion",
        "title": "The Himalayas: A Syllabus of the Region's History, Anthropology, and Religion",
        "author": "Todd Lewis",
        "year": 1995,
        "identifier": "dli.pahar.3680",
        "file_name": "3680 The Himalayas Todd Lewis s_djvu.txt",
        "out_file": "lewis_himalayas_history_anthropology_religion_1995.txt"
    },
    {
        "id": "singh_2002_trekking_in_himalaya",
        "title": "Trekking in the Himalaya: Garhwal Trails and High Passes",
        "author": "Hashmat Singh",
        "year": 2002,
        "identifier": "trekkinginhimala0000sing",
        "file_name": "trekkinginhimala0000sing_djvu.txt",
        "out_file": "singh_trekking_in_himalaya_2002.txt"
    },
    {
        "id": "lsi_2023_himachal_pahari_survey",
        "title": "Linguistic Survey of India: Pahari Dialects of the Western and Central Himalayas",
        "author": "Language Division, Office of the Registrar General, Government of India",
        "year": 2023,
        "identifier": "PARI.linguistic-survey-of-india---himachal-pradesh",
        "file_name": "linguistic-survey-of-india---himachal-pradesh_djvu.txt",
        "out_file": "lsi_himachal_pahari_language_survey_2023.txt"
    },
    {
        "id": "himachal_shabdawali_kangari_pahari",
        "title": "Himachali and Pahari Shabdawali: Comparative Himalayan Vocabulary",
        "author": "BVP Research Collection / Linguistic Cell",
        "year": 1998,
        "identifier": "bvp-05997-md-himachali-kangari-shabdawali",
        "file_name": "BVP05997-MD-Himachali-Kangani-Shabdawali_djvu.txt",
        "out_file": "himachali_kangari_pahari_shabdawali.txt"
    }
]

print("Verifying Wave 7 picks on Archive.org...")
for p in WAVE7_PICKS:
    url = f"https://archive.org/metadata/{p['identifier']}/files"
    req = urllib.request.Request(url, headers={"User-Agent": "GarhwaliLibraryBot/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            files = json.loads(resp.read().decode("utf-8")).get("result", [])
            matches = [f for f in files if f.get("name") == p["file_name"]]
            if matches:
                p["size_bytes"] = int(matches[0].get("size", 0))
                print(f"VERIFIED: {p['id']} -> {p['file_name']} ({p['size_bytes']//1024} KB)")
            else:
                txts = [f for f in files if f.get("name", "").endswith("_djvu.txt")]
                if txts:
                    p["file_name"] = txts[0].get("name")
                    p["size_bytes"] = int(txts[0].get("size", 0))
                    print(f"UPDATED: {p['id']} -> {p['file_name']} ({p['size_bytes']//1024} KB)")
                else:
                    print(f"MISSING TXT: {p['id']}")
    except Exception as e:
        print(f"ERROR: {p['id']} -> {e}")

with open("data_sources/wave7_verified.json", "w", encoding="utf-8") as f:
    json.dump(WAVE7_PICKS, f, ensure_ascii=False, indent=2)
print("Saved to data_sources/wave7_verified.json")

