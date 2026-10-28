# -*- coding: utf-8 -*-
"""
Integrates Wave 3 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "pauw_1896_tenth_settlement_garhwal",
        "title": "Report on the Tenth Settlement of the Garhwal District",
        "author": "E. K. Pauw",
        "year": 1896,
        "publisher": "Government Press, North-Western Provinces and Oudh, Allahabad",
        "pages": 439,
        "language": "Garhwali & English",
        "category": "land_tenure_and_settlement",
        "significance": "Foundational colonial settlement report of British Garhwal containing the definitive survey of land tenure, agricultural vocabulary, village boundaries, water rights, and customary revenue systems.",
        "archive_id": "dli.pahar.1406"
    },
    {
        "id": "atkinson_1884_himalayan_districts_vol2",
        "title": "The Himalayan Districts of North-Western Provinces of India Vol. 2",
        "author": "Edwin T. Atkinson",
        "year": 1884,
        "publisher": "North-Western Provinces and Oudh Government Press, Allahabad",
        "pages": 1389,
        "language": "Garhwali & English",
        "category": "history_and_ethnology",
        "significance": "Monumental historical and ethnological volume covering the dynastic annals of the Panwars of Garhwal, Katyuri kings, hill forts, religious sects, temple inscriptions, and folk legends.",
        "archive_id": "dli.pahar.1048"
    },
    {
        "id": "atkinson_1883_notes_history_himalayan",
        "title": "Notes on the History of the Himalayan Districts of the N.W.P. India",
        "author": "Edwin T. Atkinson",
        "year": 1883,
        "publisher": "Government Press, Allahabad",
        "pages": 684,
        "language": "Garhwali & English",
        "category": "history_and_archaeology",
        "significance": "Critical historical study on the epigraphy, copper-plate grants, ruling clans, and political transitions of the Central Himalayas.",
        "archive_id": "dli.pahar.1033"
    },
    {
        "id": "traill_1828_statistical_sketch_kumaon_garhwal",
        "title": "Statistical Sketch of Kumaon and Garhwal",
        "author": "George William Traill",
        "year": 1828,
        "publisher": "Asiatic Researches, Vol. XVI, Calcutta",
        "pages": 680,
        "language": "Garhwali & English",
        "category": "early_historical_surveys",
        "significance": "The earliest British official account of the Kumaon and Garhwal territories, recording pre-colonial administrative terminology, mountain routes, trade, and native customs.",
        "archive_id": "in.ernet.dli.2015.53201"
    },
    {
        "id": "upreti_1900_hill_dialects_kumaun_division",
        "title": "Hill Dialects of the Kumaun Division (Central Pahari)",
        "author": "Pandit Ganga Datt Upreti",
        "year": 1900,
        "publisher": "Government Press, Allahabad",
        "pages": 119,
        "language": "Garhwali, Kumauni & English",
        "category": "grammar_and_linguistics",
        "significance": "Comparative linguistic analysis and grammatical outlines of the spoken dialects across Kumaun, Garhwal, and the borderlands.",
        "archive_id": "dli.csl.7734"
    },
    {
        "id": "walton_1911_dehra_dun_gazetteer",
        "title": "Dehra Dun: A Gazetteer (District Gazetteers of the United Provinces Vol. 1)",
        "author": "H. G. Walton",
        "year": 1911,
        "publisher": "Government Press, United Provinces, Allahabad",
        "pages": 441,
        "language": "Garhwali & English",
        "category": "gazetteers_and_geography",
        "significance": "District gazetteer covering the Dun valley, Jaunsar-Bawar, border Garhwali villages, forest tracts, mountain flora, and tribal communities.",
        "archive_id": "in.ernet.dli.2015.94182"
    },
    {
        "id": "verma_2004_pahari_dictionary_dialects",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 North-Western Himalayan Dialects",
        "author": "Dr. Siddheshwar Varma",
        "year": 2004,
        "publisher": "Vishveshvaranand Vishva Bandhu Institute, Panjab University, Hoshiarpur",
        "pages": 395,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "significance": "Comprehensive comparative dictionary compiled by Dr. Siddheshwar Varma covering 27 dialects of the Pahari group with etymologies and phonetic glosses.",
        "archive_id": "bvp-02718"
    },
    {
        "id": "iias_2002_pahari_bhasha_sahitya",
        "title": "Pahari Bhasha Tatha Sahitya",
        "author": "Indian Institute of Advanced Study",
        "year": 2002,
        "publisher": "IIAS, Rashtrapati Nivas, Shimla",
        "pages": 210,
        "language": "Pahari, Garhwali & Hindi",
        "category": "literature_and_criticism",
        "significance": "Scholarly symposium volume on Pahari linguistics, oral literature, jagars, ballads, and dialectal evolution across the Western and Central Himalayas.",
        "archive_id": "pahari-bhasha-tatha-sahitya"
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
