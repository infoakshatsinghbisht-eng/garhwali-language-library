# -*- coding: utf-8 -*-
"""
Integrates Wave 5 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "mumm_1909_five_months_in_himalaya_garhwal",
        "title": "Five Months in the Himalaya: A Record of Mountain Travel in Garhwal",
        "author": "A. L. Mumm",
        "year": 1909,
        "publisher": "Edward Arnold, London",
        "pages": 211,
        "language": "Garhwali & English",
        "category": "travel_and_exploration",
        "significance": "First-hand mountaineering and exploration narrative across Garhwal, Trisul, the Rishi Ganga gorge, Nanda Devi sanctuary, Mana pass, and native porter routes.",
        "archive_id": "india.history.resource.91859"
    },
    {
        "id": "up_govt_1919_kumaun_garhwal_local_customs",
        "title": "Kumaun and Garhwal: Local Customs and Usages",
        "author": "Government of United Provinces",
        "year": 1919,
        "publisher": "Superintendent, Government Press, United Provinces, Allahabad",
        "pages": 105,
        "language": "Garhwali & English",
        "category": "customary_law_and_jurisprudence",
        "significance": "Official codification of native customary law in the Himalayan tracts: rights of married daughters, ancestral debts, village water mills, sacred groves, and grazing commons.",
        "archive_id": "india.history.resource.88082"
    },
    {
        "id": "verma_2003_pahari_dictionary_part3",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 3)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "publisher": "Vishveshvaranand Vishva Bandhu Institute, Panjab University, Hoshiarpur",
        "pages": 270,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "significance": "Part 3 of Dr. Siddheshwar Varma's comprehensive Pahari dictionary series, recording comparative root forms, postpositions, and case markers across the Himalayan dialects.",
        "archive_id": "bvp-03883"
    },
    {
        "id": "himalayan_folklore_1920_legends",
        "title": "Himalayan Folklore: Legends and Traditions of Kumaon and Garhwal",
        "author": "Rev. E. S. Oakley",
        "year": 1920,
        "publisher": "Government Press, Allahabad",
        "pages": 269,
        "language": "Garhwali & English",
        "category": "folklore_and_epics",
        "significance": "Anthology of heroic legends, chivalric ballads of hill chieftains, supernatural Jagars, and mountain ghost tales of the Central Himalayas.",
        "archive_id": "in.ernet.dli.2015.108282"
    },
    {
        "id": "dictionary_pahari_1911_dialects",
        "title": "Dictionary of Pahari Dialects of the Western and Central Himalayas",
        "author": "T. R. Joshi / Government Press",
        "year": 1911,
        "publisher": "Baptist Mission Press, Calcutta / Asiatic Society",
        "pages": 154,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "significance": "Comparative vocabulary of Pahari dialects recording archaic vocables, agricultural implements, and domestic terminology.",
        "archive_id": "dli.pahar.1894"
    },
    {
        "id": "himalayan_letters_1927_pilgrimage",
        "title": "The Himalayan Letters of Gypsy Davy and Lady Ba: Pilgrimage in Garhwal",
        "author": "Gypsy Davy and Lady Ba",
        "year": 1927,
        "publisher": "W. Heffer & Sons Ltd., Cambridge",
        "pages": 319,
        "language": "Garhwali & English",
        "category": "travel_and_pilgrimage",
        "significance": "Epistolary narrative documenting journeys along the pilgrim paths of Garhwal (Rishikesh, Devprayag, Srinagar, Rudraprayag, Kedarnath, Badrinath) and encounters with hill folk.",
        "archive_id": "the-himalayan-letters-of-gypsy-davy-and-lady-ba-written-on-pilgrimage-to-the-hig"
    }
]

added = 0
for r in new_records:
    if r["id"] not in existing_ids:
        biblio.append(r)
        added += 1

with open(BIBLIO_PATH, "w", encoding="utf-8") as f:
    json.dump(biblio, f, ensure_ascii=False, indent=2)

print(f"Added {added} records to bibliography. Total records: {len(biblio)}")
