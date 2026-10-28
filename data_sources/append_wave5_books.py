# -*- coding: utf-8 -*-
"""
Appends Wave 5 book configurations to data_sources/build_book_pages.py.
"""

wave5_configs = """    {
        "id": "mumm_1909_five_months_in_himalaya_garhwal",
        "file": "mumm_five_months_in_himalaya_garhwal_1909.txt",
        "title": "Five Months in the Himalaya: A Record of Mountain Travel in Garhwal",
        "author": "A. L. Mumm",
        "year": 1909,
        "language": "Garhwali & English",
        "category": "travel_and_exploration",
        "description": "First-hand mountaineering and exploration narrative across Garhwal, Trisul, the Rishi Ganga gorge, Nanda Devi sanctuary, Mana pass, and native porter routes.",
        "explicit_page_marker": None
    },
    {
        "id": "up_govt_1919_kumaun_garhwal_local_customs",
        "file": "up_govt_kumaun_garhwal_local_customs_1919.txt",
        "title": "Kumaun and Garhwal: Local Customs and Usages",
        "author": "Government of United Provinces",
        "year": 1919,
        "language": "Garhwali & English",
        "category": "customary_law_and_jurisprudence",
        "description": "Official codification of native customary law in the Himalayan tracts: rights of married daughters, ancestral debts, village water mills, sacred groves, and grazing commons.",
        "explicit_page_marker": None
    },
    {
        "id": "verma_2003_pahari_dictionary_part3",
        "file": "verma_pahari_dictionary_part3_2003.txt",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 3)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "description": "Part 3 of Dr. Siddheshwar Varma's comprehensive Pahari dictionary series, recording comparative root forms, postpositions, and case markers across the Himalayan dialects.",
        "explicit_page_marker": None
    },
    {
        "id": "himalayan_folklore_1920_legends",
        "file": "oakley_himalayan_folklore_legends_1920.txt",
        "title": "Himalayan Folklore: Legends and Traditions of Kumaon and Garhwal",
        "author": "Rev. E. S. Oakley",
        "year": 1920,
        "language": "Garhwali & English",
        "category": "folklore_and_epics",
        "description": "Anthology of heroic legends, chivalric ballads of hill chieftains, supernatural Jagars, and mountain ghost tales of the Central Himalayas.",
        "explicit_page_marker": None
    },
    {
        "id": "dictionary_pahari_1911_dialects",
        "file": "dictionary_pahari_dialects_punjab_himalaya_1911.txt",
        "title": "Dictionary of Pahari Dialects of the Western and Central Himalayas",
        "author": "T. R. Joshi / Government Press",
        "year": 1911,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "description": "Comparative vocabulary of Pahari dialects recording archaic vocables, agricultural implements, and domestic terminology.",
        "explicit_page_marker": None
    },
    {
        "id": "himalayan_letters_1927_pilgrimage",
        "file": "gypsy_davy_himalayan_letters_pilgrimage_1927.txt",
        "title": "The Himalayan Letters of Gypsy Davy and Lady Ba: Pilgrimage in Garhwal",
        "author": "Gypsy Davy and Lady Ba",
        "year": 1927,
        "language": "Garhwali & English",
        "category": "travel_and_pilgrimage",
        "description": "Epistolary narrative documenting journeys along the pilgrim paths of Garhwal (Rishikesh, Devprayag, Srinagar, Rudraprayag, Kedarnath, Badrinath) and encounters with hill folk.",
        "explicit_page_marker": None
    }
]"""

with open("data_sources/build_book_pages.py", "r", encoding="utf-8") as f:
    content = f.read()

marker = "        \"explicit_page_marker\": None\n    }\n]"
if marker in content:
    replacement = "        \"explicit_page_marker\": None\n    },\n" + wave5_configs
    content = content.replace(marker, replacement, 1)
    with open("data_sources/build_book_pages.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully appended Wave 5 book configurations.")
else:
    print("Marker not found in build_book_pages.py")
