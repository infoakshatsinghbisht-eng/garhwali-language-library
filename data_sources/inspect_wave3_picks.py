# -*- coding: utf-8 -*-
import json

with open("data_sources/wave3_available.json", "r", encoding="utf-8") as f:
    items = json.load(f)

selected_ids = [
    "dli.pahar.1406",        # Pauw's Tenth Settlement of Garhwal District (1896)
    "in.ernet.dli.2015.53201", # Traill's Statistical Sketch of Kumaon (1828)
    "dli.pahar.1033",        # Atkinson's History of Himalayan Districts (1884)
    "dli.pahar.1048",        # Atkinson's Himalayan Districts Vol 2 (1884)
    "in.ernet.dli.2015.94182", # Walton's Dehra Dun Gazetteer (1911)
    "dli.csl.7734",          # Upreti's Hill Dialects of Kumaun Division (1900)
    "bvp-02718",             # Siddheshwar Varma's Pahari Dictionary (1989)
    "pahari-bhasha-tatha-sahitya" # Pahari Bhasha Tatha Sahitya
]

print("Selected candidates details:")
for it in items:
    if it["identifier"] in selected_ids:
        print(f"\nID: {it['identifier']}")
        print(f"Title: {it['title']}")
        print(f"Creator: {it['creator']}")
        print(f"Year: {it['year']}")
        print(f"File: {it['file_name']}")
        print(f"Size: {it['size_kb']} KB")
