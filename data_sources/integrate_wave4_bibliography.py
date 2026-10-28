# -*- coding: utf-8 -*-
"""
Integrates Wave 4 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "dabral_1965_bhotantik_alaknanda",
        "title": "Uttarakhand Ke Bhotantik: Alaknanda Upatyaka Mein Pravas (Bhag 2)",
        "author": "Dr. Shiv Prasad Dabral 'Charan'",
        "year": 1965,
        "publisher": "Veer Gatha Prakashan, Dogadda, Garhwal",
        "pages": 177,
        "language": "Garhwali & Hindi",
        "category": "ethnography_and_culture",
        "significance": "Comprehensive ethnographical study by Dr. S.P. Dabral documenting the transhumant pastoralists, Marchha and Tolchha clans of upper Garhwal, alpine migration routes, and border trade terms.",
        "archive_id": "xhed_uttarakhand-ke-bhotantik-alaknanda-upatyaka-mein-pravas-bhag-2-by-shivapras"
    },
    {
        "id": "atkinson_1886_himalayan_districts_vol3",
        "title": "The Himalayan Districts of the North-Western Provinces Vol. 3",
        "author": "Edwin T. Atkinson",
        "year": 1886,
        "publisher": "Government Press, Allahabad",
        "pages": 899,
        "language": "Garhwali & English",
        "category": "gazetteers_and_geography",
        "significance": "The concluding gazetteer volume of Atkinson's Himalayan series, providing detailed place-by-place descriptions of Garhwali tahsils, pattis, rivers, forts, and indigenous economic products.",
        "archive_id": "wbsl.19297"
    },
    {
        "id": "stowell_1916_kumaun_garhwali_customary_rulings",
        "title": "Kumaun Rulings for Civil Courts (Customary Law of Kumaun and Garhwal)",
        "author": "V. A. Stowell",
        "year": 1916,
        "publisher": "Government Press, United Provinces, Allahabad",
        "pages": 185,
        "language": "Garhwali & English",
        "category": "customary_law_and_jurisprudence",
        "significance": "Official legal rulings and precedents on Garhwali and Kumauni customary law, succession, village commons, irrigation disputes, and lineage property rights.",
        "archive_id": "kqqg-kumaun-rulings-for-civil-courts-by-v-a-stowell-law"
    },
    {
        "id": "british_records_1842_historical_papers_garhwal",
        "title": "Historical Papers Relating to Kumaun and Garhwal 1809-1842",
        "author": "Government of North-Western Provinces",
        "year": 1842,
        "publisher": "Government Central Record Office, Allahabad",
        "pages": 307,
        "language": "Garhwali & English",
        "category": "historical_records_and_archives",
        "significance": "Primary colonial correspondence, treaties, and administrative records regarding the liberation of Garhwal from Gorkha rule, early settlement agreements, and native institutions.",
        "archive_id": "bcxu_historical-papers-relating-to-kumaun-1809-1842-selections-from-english-reco"
    },
    {
        "id": "oakley_1935_himalayan_folklore_extended",
        "title": "Himalayan Folklore (Extended Archival Edition)",
        "author": "Rev. E. S. Oakley and Tara Dutt Gairola",
        "year": 1935,
        "publisher": "Government Press, Allahabad",
        "pages": 313,
        "language": "Garhwali & English",
        "category": "folklore_and_epics",
        "significance": "Unabridged archival edition of Central Himalayan legends, ballads of warrior heroes (Bhads), demon tales, and sacred mythological cycles.",
        "archive_id": "in.ernet.dli.2015.532407"
    },
    {
        "id": "verma_2003_pahari_dictionary_vol1",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 North-Western Himalayan Dialects (Vol. 1)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "publisher": "Vishveshvaranand Vishva Bandhu Institute, Panjab University, Hoshiarpur",
        "pages": 372,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "significance": "Volume 1 of Dr. Siddheshwar Varma's monumental comparative Pahari lexicon, documenting phonetic transcriptions, nominal declensions, and cognates across the Himalayan belt.",
        "archive_id": "bvp-03866"
    },
    {
        "id": "imperial_gazetteer_1905_kumaun_garhwal",
        "title": "Imperial Gazetteer of India: Kumaun Division (Garhwal)",
        "author": "Imperial Gazetteer of India",
        "year": 1905,
        "publisher": "Superintendent of Government Printing, Calcutta",
        "pages": 69,
        "language": "Garhwali & English",
        "category": "gazetteers_and_geography",
        "significance": "Provincial gazetteer series volume summarizing the administrative history, agriculture, trade routes, and demographic statistics of British Garhwal.",
        "archive_id": "in.ernet.dli.2015.35356"
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

