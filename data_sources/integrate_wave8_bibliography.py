# -*- coding: utf-8 -*-
"""
Integrates Wave 8 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "grierson_1916_lsi_pahari_gujuri_ignca",
        "title": "Linguistic Survey of India: The Pahari Languages and Gujuri (IGNCA Archival Edition)",
        "author": "Sir George Abraham Grierson",
        "year": 1916,
        "publisher": "Indira Gandhi National Centre for the Arts / Superintendent of Government Printing, Calcutta",
        "pages": 770,
        "language": "Pahari, Garhwali & English",
        "category": "grammar_and_linguistics",
        "significance": "Comprehensive comparative linguistic treatise on the Pahari group (Eastern, Central/Garhwali-Kumauni, and Western Pahari) detailing phonetic shifts, ergative constructions, verb matrices, and comparative folk specimens.",
        "archive_id": "in.gov.ignca.23438"
    },
    {
        "id": "tehri_garhwal_1897_leased_forests_plan",
        "title": "Working Plan of the Tehri-Garhwal Leased Forests",
        "author": "Forest Department, North-Western Provinces",
        "year": 1897,
        "publisher": "Superintendent, Government Press, North-Western Provinces, Allahabad",
        "pages": 186,
        "language": "Garhwali & English",
        "category": "culture_and_geography",
        "significance": "Detailed administrative and botanical survey of Tehri Garhwal forests, recording native Himalayan timber species (Deodar, Kail, Chir, Banj), timber floating down the Bhagirathi, pasture rights, and water access.",
        "archive_id": "wbsl.13950"
    },
    {
        "id": "nazish_chalyaan_suraan_pahari_poetry",
        "title": "Chalyaan Suraan: Pahari Rhythms, Songs and Verses",
        "author": "Iqbal Nazish",
        "year": 1995,
        "publisher": "Pahari Cultural Academy, Srinagar",
        "pages": 57,
        "language": "Pahari & Garhwali",
        "category": "folklore_and_epics",
        "significance": "Anthology of mountain songs, Pahari folk meters, lyrical verses, and cultural idioms expressing rural pastoral sentiment and Himalayan seasonal celebrations.",
        "archive_id": "HUqe_chalyaan-suraan-pahari-iqbal-nazish"
    },
    {
        "id": "bhandari_1946_snow_balls_of_garhwal",
        "title": "Snow Balls of Garhwal: Folk Songs, Ballads and Life in the Hills",
        "author": "N. S. Bhandari et al.",
        "year": 1946,
        "publisher": "Universal Publishers, Lucknow",
        "pages": 50,
        "language": "Garhwali & English",
        "category": "folklore_and_epics",
        "significance": "Anthology of authentic Garhwali folk ballads, seasonal Chaiti and Bajuband songs, heroic legends, village love songs, and mountain life narratives.",
        "archive_id": "in.ernet.dli.2015.85090"
    },
    {
        "id": "himalayan_society_1969_birds_lower_garhwal",
        "title": "Birds and Natural History of Lower Garhwal Himalayas",
        "author": "Himalayan Natural History Society",
        "year": 1969,
        "publisher": "Journal of the Bombay Natural History Society / Biostor",
        "pages": 38,
        "language": "Garhwali & English",
        "category": "nature_and_wildlife",
        "significance": "Faunal and ornithological documentation of the Garhwal valley foothills, Doon valley, and sub-Himalayan ridges, recording vernacular bird names, migratory patterns, and forest habitats.",
        "archive_id": "biostor-250867"
    },
    {
        "id": "ibbotson_1933_eleventh_settlement_garhwal",
        "title": "Final Report on the Eleventh Revenue Settlement of Garhwal District",
        "author": "A. W. Ibbotson",
        "year": 1933,
        "publisher": "Superintendent, Printing and Stationery, United Provinces, Allahabad",
        "pages": 26,
        "language": "Garhwali & English",
        "category": "revenue_and_land_tenure",
        "significance": "Twentieth-century colonial settlement report detailing land classification (Talaon, Upraon, Katil, Ijran), village water mill assessments, customary rights, and agrarian changes in British Garhwal.",
        "archive_id": "dli.pahar.2527"
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

