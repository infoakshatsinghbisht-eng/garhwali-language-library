# -*- coding: utf-8 -*-
"""
Appends Wave 3 book configurations to data_sources/build_book_pages.py.
"""

import re

wave3_configs = """    {
        "id": "pauw_1896_tenth_settlement_garhwal",
        "file": "pauw_report_tenth_settlement_garhwal_1896.txt",
        "title": "Report on the Tenth Settlement of the Garhwal District",
        "author": "E. K. Pauw",
        "year": 1896,
        "language": "Garhwali & English",
        "category": "land_tenure_and_settlement",
        "description": "Authoritative settlement report of British Garhwal containing the definitive survey of land tenure, agricultural vocabulary, village boundaries, water rights, and customary revenue systems.",
        "explicit_page_marker": None
    },
    {
        "id": "atkinson_1884_himalayan_districts_vol2",
        "file": "atkinson_himalayan_districts_vol2_1884.txt",
        "title": "The Himalayan Districts of North-Western Provinces of India Vol. 2",
        "author": "Edwin T. Atkinson",
        "year": 1884,
        "language": "Garhwali & English",
        "category": "history_and_ethnology",
        "description": "Monumental historical and ethnological volume covering the dynastic annals of the Panwars of Garhwal, Katyuri kings, hill forts, religious sects, temple inscriptions, and folk legends.",
        "explicit_page_marker": None
    },
    {
        "id": "atkinson_1883_notes_history_himalayan",
        "file": "atkinson_notes_history_himalayan_districts_1883.txt",
        "title": "Notes on the History of the Himalayan Districts of the N.W.P. India",
        "author": "Edwin T. Atkinson",
        "year": 1883,
        "language": "Garhwali & English",
        "category": "history_and_archaeology",
        "description": "Critical historical study on the epigraphy, copper-plate grants, ruling clans, and political transitions of the Central Himalayas.",
        "explicit_page_marker": None
    },
    {
        "id": "traill_1828_statistical_sketch_kumaon_garhwal",
        "file": "traill_statistical_sketch_kumaon_garhwal_1828.txt",
        "title": "Statistical Sketch of Kumaon and Garhwal",
        "author": "George William Traill",
        "year": 1828,
        "language": "Garhwali & English",
        "category": "early_historical_surveys",
        "description": "The earliest British official account of the Kumaon and Garhwal territories, recording pre-colonial administrative terminology, mountain routes, trade, and native customs.",
        "explicit_page_marker": None
    },
    {
        "id": "upreti_1900_hill_dialects_kumaun_division",
        "file": "upreti_hill_dialects_kumaun_division_1900.txt",
        "title": "Hill Dialects of the Kumaun Division (Central Pahari)",
        "author": "Pandit Ganga Datt Upreti",
        "year": 1900,
        "language": "Garhwali, Kumauni & English",
        "category": "grammar_and_linguistics",
        "description": "Comparative linguistic analysis and grammatical outlines of the spoken dialects across Kumaun, Garhwal, and the borderlands.",
        "explicit_page_marker": None
    },
    {
        "id": "walton_1911_dehra_dun_gazetteer",
        "file": "walton_dehra_dun_gazetteer_1911.txt",
        "title": "Dehra Dun: A Gazetteer (District Gazetteers of the United Provinces Vol. 1)",
        "author": "H. G. Walton",
        "year": 1911,
        "language": "Garhwali & English",
        "category": "gazetteers_and_geography",
        "description": "District gazetteer covering the Dun valley, Jaunsar-Bawar, border Garhwali villages, forest tracts, mountain flora, and tribal communities.",
        "explicit_page_marker": None
    },
    {
        "id": "verma_2004_pahari_dictionary_dialects",
        "file": "verma_pahari_dictionary_27_dialects_2004.txt",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 North-Western Himalayan Dialects",
        "author": "Dr. Siddheshwar Varma",
        "year": 2004,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "description": "Comprehensive comparative dictionary compiled by Dr. Siddheshwar Varma covering 27 dialects of the Pahari group with etymologies and phonetic glosses.",
        "explicit_page_marker": None
    },
    {
        "id": "iias_2002_pahari_bhasha_sahitya",
        "file": "iias_pahari_bhasha_tatha_sahitya_2002.txt",
        "title": "Pahari Bhasha Tatha Sahitya",
        "author": "Indian Institute of Advanced Study",
        "year": 2002,
        "language": "Pahari, Garhwali & Hindi",
        "category": "literature_and_criticism",
        "description": "Scholarly symposium volume on Pahari linguistics, oral literature, jagars, ballads, and dialectal evolution across the Western and Central Himalayas.",
        "explicit_page_marker": None
    }
]"""

with open("data_sources/build_book_pages.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the closing of BOOK_CONFIGS
marker = "        \"explicit_page_marker\": None\n    }\n]"
if marker in content:
    replacement = "        \"explicit_page_marker\": None\n    },\n" + wave3_configs
    content = content.replace(marker, replacement, 1)
    with open("data_sources/build_book_pages.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully appended Wave 3 book configurations.")
else:
    print("Marker not found in build_book_pages.py")
