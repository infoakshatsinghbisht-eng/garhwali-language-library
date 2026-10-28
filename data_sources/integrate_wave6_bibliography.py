# -*- coding: utf-8 -*-
"""
Integrates Wave 6 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "sherring_1906_western_tibet_british_borderland",
        "title": "Western Tibet and the British Borderland: Garhwal and Bhotia Customs",
        "author": "Charles A. Sherring",
        "year": 1906,
        "publisher": "Edward Arnold, London",
        "pages": 376,
        "language": "Garhwali, Tibetan & English",
        "category": "ethnography_and_borderland_customs",
        "significance": "Authoritative ethnographic survey of the Garhwal borderland, trans-Himalayan trade routes through Mana and Niti passes, Bhotia customs, village administration, and mountain pastoralism.",
        "archive_id": "westerntibetbrit00sher"
    },
    {
        "id": "batten_1851_official_reports_kumaon_garhwal",
        "title": "Official Reports on the Province of Kumaon and Garhwal",
        "author": "J. H. Batten",
        "year": 1851,
        "publisher": "Agra Government Press, Agra",
        "pages": 472,
        "language": "Garhwali & English",
        "category": "revenue_and_land_tenure",
        "significance": "Early colonial settlement and administrative reports detailing land tenure (Thatwan, Khaikar, Sirtan), revenue assessments, village boundaries, and customary rights in British Garhwal.",
        "archive_id": "dli.pahar.0412"
    },
    {
        "id": "bisht_1994_tourism_garhwal_himalaya",
        "title": "Tourism in Garhwal Himalaya: Pilgrimage, Culture and Economy",
        "author": "Dr. Harshwanti Bisht",
        "year": 1994,
        "publisher": "Indus Publishing Company, New Delhi",
        "pages": 232,
        "language": "Garhwali & English",
        "category": "travel_and_pilgrimage",
        "significance": "Comprehensive study of pilgrimage routes, sacred geography (Char Dham, Panch Kedar, Panch Prayag), trekking trails, hill economy, and cultural ecology of Garhwal.",
        "archive_id": "tourism-in-garhwal-himalaya-by-harshwanti-bisht-to"
    },
    {
        "id": "khanduri_1986_peaks_passes_garhwal",
        "title": "Peaks and Passes of the Garhwal Himalaya",
        "author": "Garhwal Exploration Society",
        "year": 1986,
        "publisher": "Garhwal Exploration Society / Himalayan Club",
        "pages": 188,
        "language": "Garhwali & English",
        "category": "geography_and_mountaineering",
        "significance": "Exhaustive geographical and topographical documentation of Garhwal's high-altitude passes (Dharas, Khalas, Dhuras), peaks, glacial basins, and traditional shepherds' trails.",
        "archive_id": "dli.pahar.3635"
    },
    {
        "id": "bhatt_1992_garhwal_himalaya_nature_culture",
        "title": "Garhwal Himalaya: Nature, Culture and Society",
        "author": "H. P. Bhatt et al.",
        "year": 1992,
        "publisher": "Transmedia Publication, Srinagar Garhwal",
        "pages": 204,
        "language": "Garhwali & English",
        "category": "culture_and_geography",
        "significance": "Interdisciplinary exploration of Garhwali society, folk culture, settlement patterns, forest conservation traditions, and mountain agro-pastoral life.",
        "archive_id": "GarhwalHimalaya"
    },
    {
        "id": "verma_2003_pahari_dictionary_part2",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 2)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "publisher": "Vishveshvaranand Vishva Bandhu Institute, Panjab University, Hoshiarpur",
        "pages": 180,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "significance": "Part 2 of Dr. Siddheshwar Varma's landmark comparative Pahari dictionary, analyzing phonetic correspondences, verbal roots, and dialectological isoglosses.",
        "archive_id": "bvp-03865"
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
