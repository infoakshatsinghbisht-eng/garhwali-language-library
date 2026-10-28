# -*- coding: utf-8 -*-

wave6_snippet = """    {
        "id": "sherring_1906_western_tibet_british_borderland",
        "file": "sherring_western_tibet_british_borderland_1906.txt",
        "title": "Western Tibet and the British Borderland: Garhwal and Bhotia Customs",
        "author": "Charles A. Sherring",
        "year": 1906,
        "language": "Garhwali, Tibetan & English",
        "category": "ethnography_and_borderland_customs",
        "description": "Authoritative ethnographic survey of the Garhwal borderland, trans-Himalayan trade routes through Mana and Niti passes, Bhotia customs, village administration, and mountain pastoralism.",
        "explicit_page_marker": None
    },
    {
        "id": "batten_1851_official_reports_kumaon_garhwal",
        "file": "batten_official_reports_kumaon_garhwal_1851.txt",
        "title": "Official Reports on the Province of Kumaon and Garhwal",
        "author": "J. H. Batten",
        "year": 1851,
        "language": "Garhwali & English",
        "category": "revenue_and_land_tenure",
        "description": "Early colonial settlement and administrative reports detailing land tenure (Thatwan, Khaikar, Sirtan), revenue assessments, village boundaries, and customary rights in British Garhwal.",
        "explicit_page_marker": None
    },
    {
        "id": "bisht_1994_tourism_garhwal_himalaya",
        "file": "bisht_tourism_in_garhwal_himalaya_1994.txt",
        "title": "Tourism in Garhwal Himalaya: Pilgrimage, Culture and Economy",
        "author": "Dr. Harshwanti Bisht",
        "year": 1994,
        "language": "Garhwali & English",
        "category": "travel_and_pilgrimage",
        "description": "Comprehensive study of pilgrimage routes, sacred geography (Char Dham, Panch Kedar, Panch Prayag), trekking trails, hill economy, and cultural ecology of Garhwal.",
        "explicit_page_marker": None
    },
    {
        "id": "khanduri_1986_peaks_passes_garhwal",
        "file": "khanduri_peaks_and_passes_garhwal_1986.txt",
        "title": "Peaks and Passes of the Garhwal Himalaya",
        "author": "Garhwal Exploration Society",
        "year": 1986,
        "language": "Garhwali & English",
        "category": "geography_and_mountaineering",
        "description": "Exhaustive geographical and topographical documentation of Garhwal's high-altitude passes (Dharas, Khalas, Dhuras), peaks, glacial basins, and traditional shepherds' trails.",
        "explicit_page_marker": None
    },
    {
        "id": "bhatt_1992_garhwal_himalaya_nature_culture",
        "file": "bhatt_garhwal_himalaya_nature_culture_1992.txt",
        "title": "Garhwal Himalaya: Nature, Culture and Society",
        "author": "H. P. Bhatt et al.",
        "year": 1992,
        "language": "Garhwali & English",
        "category": "culture_and_geography",
        "description": "Interdisciplinary exploration of Garhwali society, folk culture, settlement patterns, forest conservation traditions, and mountain agro-pastoral life.",
        "explicit_page_marker": None
    },
    {
        "id": "verma_2003_pahari_dictionary_part2",
        "file": "verma_pahari_dictionary_part2_2003.txt",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 2)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "description": "Part 2 of Dr. Siddheshwar Varma's landmark comparative Pahari dictionary, analyzing phonetic correspondences, verbal roots, and dialectological isoglosses.",
        "explicit_page_marker": None
    }
]"""

with open("data_sources/build_book_pages.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the closing of himalayan_letters_1927_pilgrimage and BOOK_CONFIGS
old_end = """        "explicit_page_marker": None
    }
]"""

if old_end not in content:
    old_end = old_end.replace("\n", "\r\n")

new_end = """        "explicit_page_marker": None
    },
""" + wave6_snippet

content_updated = content.replace(old_end, new_end)

with open("data_sources/build_book_pages.py", "w", encoding="utf-8") as f:
    f.write(content_updated)

print("Updated data_sources/build_book_pages.py successfully!")
