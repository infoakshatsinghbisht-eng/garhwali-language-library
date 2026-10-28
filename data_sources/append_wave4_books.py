# -*- coding: utf-8 -*-
"""
Appends Wave 4 book configurations to data_sources/build_book_pages.py.
"""

wave4_configs = """    {
        "id": "dabral_1965_bhotantik_alaknanda",
        "file": "dabral_uttarakhand_ke_bhotantik_alaknanda_1965.txt",
        "title": "Uttarakhand Ke Bhotantik: Alaknanda Upatyaka Mein Pravas (Bhag 2)",
        "author": "Dr. Shiv Prasad Dabral 'Charan'",
        "year": 1965,
        "language": "Garhwali & Hindi",
        "category": "ethnography_and_culture",
        "description": "Comprehensive ethnographical study by Dr. S.P. Dabral documenting the transhumant pastoralists, Marchha and Tolchha clans of upper Garhwal, alpine migration routes, and border trade terms.",
        "explicit_page_marker": None
    },
    {
        "id": "atkinson_1886_himalayan_districts_vol3",
        "file": "atkinson_himalayan_districts_vol3_1886.txt",
        "title": "The Himalayan Districts of the North-Western Provinces Vol. 3",
        "author": "Edwin T. Atkinson",
        "year": 1886,
        "language": "Garhwali & English",
        "category": "gazetteers_and_geography",
        "description": "The concluding gazetteer volume of Atkinson's Himalayan series, providing detailed place-by-place descriptions of Garhwali tahsils, pattis, rivers, forts, and indigenous economic products.",
        "explicit_page_marker": None
    },
    {
        "id": "stowell_1916_kumaun_garhwali_customary_rulings",
        "file": "stowell_kumaun_garhwali_customary_rulings_1916.txt",
        "title": "Kumaun Rulings for Civil Courts (Customary Law of Kumaun and Garhwal)",
        "author": "V. A. Stowell",
        "year": 1916,
        "language": "Garhwali & English",
        "category": "customary_law_and_jurisprudence",
        "description": "Official legal rulings and precedents on Garhwali and Kumauni customary law, succession, village commons, irrigation disputes, and lineage property rights.",
        "explicit_page_marker": None
    },
    {
        "id": "british_records_1842_historical_papers_garhwal",
        "file": "british_records_historical_papers_garhwal_1842.txt",
        "title": "Historical Papers Relating to Kumaun and Garhwal 1809-1842",
        "author": "Government of North-Western Provinces",
        "year": 1842,
        "language": "Garhwali & English",
        "category": "historical_records_and_archives",
        "description": "Primary colonial correspondence, treaties, and administrative records regarding the liberation of Garhwal from Gorkha rule, early settlement agreements, and native institutions.",
        "explicit_page_marker": None
    },
    {
        "id": "oakley_1935_himalayan_folklore_extended",
        "file": "oakley_gairola_himalayan_folklore_extended_1935.txt",
        "title": "Himalayan Folklore (Extended Archival Edition)",
        "author": "Rev. E. S. Oakley and Tara Dutt Gairola",
        "year": 1935,
        "language": "Garhwali & English",
        "category": "folklore_and_epics",
        "description": "Unabridged archival edition of Central Himalayan legends, ballads of warrior heroes (Bhads), demon tales, and sacred mythological cycles.",
        "explicit_page_marker": None
    },
    {
        "id": "verma_2003_pahari_dictionary_vol1",
        "file": "verma_pahari_dictionary_vol1_2003.txt",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 North-Western Himalayan Dialects (Vol. 1)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "description": "Volume 1 of Dr. Siddheshwar Varma's monumental comparative Pahari lexicon, documenting phonetic transcriptions, nominal declensions, and cognates across the Himalayan belt.",
        "explicit_page_marker": None
    },
    {
        "id": "imperial_gazetteer_1905_kumaun_garhwal",
        "file": "imperial_gazetteer_kumaun_garhwal_1905.txt",
        "title": "Imperial Gazetteer of India: Kumaun Division (Garhwal)",
        "author": "Imperial Gazetteer of India",
        "year": 1905,
        "language": "Garhwali & English",
        "category": "gazetteers_and_geography",
        "description": "Provincial gazetteer series volume summarizing the administrative history, agriculture, trade routes, and demographic statistics of British Garhwal.",
        "explicit_page_marker": None
    }
]"""

with open("data_sources/build_book_pages.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the closing of BOOK_CONFIGS
marker = "        \"explicit_page_marker\": None\n    }\n]"
if marker in content:
    replacement = "        \"explicit_page_marker\": None\n    },\n" + wave4_configs
    content = content.replace(marker, replacement, 1)
    with open("data_sources/build_book_pages.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully appended Wave 4 book configurations.")
else:
    print("Marker not found in build_book_pages.py")

