# -*- coding: utf-8 -*-
"""
Digitizes Wave 6 books into garhwali/culture/data/books/<id>.json
and rebuilds index.json for all books in the library.
"""

import os
import sys
import json
import glob
import re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "garhwali", "culture", "data", "books"
)

WAVE6_CONFIGS = [
    {
        "id": "sherring_1906_western_tibet_british_borderland",
        "file": "sherring_western_tibet_british_borderland_1906.txt",
        "title": "Western Tibet and the British Borderland: Garhwal and Bhotia Customs",
        "author": "Charles A. Sherring",
        "year": 1906,
        "language": "Garhwali, Tibetan & English",
        "category": "ethnography_and_borderland_customs",
        "description": "Authoritative ethnographic survey of the Garhwal borderland, trans-Himalayan trade routes through Mana and Niti passes, Bhotia customs, village administration, and mountain pastoralism."
    },
    {
        "id": "batten_1851_official_reports_kumaon_garhwal",
        "file": "batten_official_reports_kumaon_garhwal_1851.txt",
        "title": "Official Reports on the Province of Kumaon and Garhwal",
        "author": "J. H. Batten",
        "year": 1851,
        "language": "Garhwali & English",
        "category": "revenue_and_land_tenure",
        "description": "Early colonial settlement and administrative reports detailing land tenure (Thatwan, Khaikar, Sirtan), revenue assessments, village boundaries, and customary rights in British Garhwal."
    },
    {
        "id": "bisht_1994_tourism_garhwal_himalaya",
        "file": "bisht_tourism_in_garhwal_himalaya_1994.txt",
        "title": "Tourism in Garhwal Himalaya: Pilgrimage, Culture and Economy",
        "author": "Dr. Harshwanti Bisht",
        "year": 1994,
        "language": "Garhwali & English",
        "category": "travel_and_pilgrimage",
        "description": "Comprehensive study of pilgrimage routes, sacred geography (Char Dham, Panch Kedar, Panch Prayag), trekking trails, hill economy, and cultural ecology of Garhwal."
    },
    {
        "id": "khanduri_1986_peaks_passes_garhwal",
        "file": "khanduri_peaks_and_passes_garhwal_1986.txt",
        "title": "Peaks and Passes of the Garhwal Himalaya",
        "author": "Garhwal Exploration Society",
        "year": 1986,
        "language": "Garhwali & English",
        "category": "geography_and_mountaineering",
        "description": "Exhaustive geographical and topographical documentation of Garhwal's high-altitude passes (Dharas, Khalas, Dhuras), peaks, glacial basins, and traditional shepherds' trails."
    },
    {
        "id": "bhatt_1992_garhwal_himalaya_nature_culture",
        "file": "bhatt_garhwal_himalaya_nature_culture_1992.txt",
        "title": "Garhwal Himalaya: Nature, Culture and Society",
        "author": "H. P. Bhatt et al.",
        "year": 1992,
        "language": "Garhwali & English",
        "category": "culture_and_geography",
        "description": "Interdisciplinary exploration of Garhwali society, folk culture, settlement patterns, forest conservation traditions, and mountain agro-pastoral life."
    },
    {
        "id": "verma_2003_pahari_dictionary_part2",
        "file": "verma_pahari_dictionary_part2_2003.txt",
        "title": "Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 2)",
        "author": "Dr. Siddheshwar Varma",
        "year": 2003,
        "language": "Pahari, Garhwali & English",
        "category": "lexicography_and_dictionary",
        "description": "Part 2 of Dr. Siddheshwar Varma's landmark comparative Pahari dictionary, analyzing phonetic correspondences, verbal roots, and dialectological isoglosses."
    }
]

def paginate_by_paragraphs(text: str, target_chars_per_page: int = 2200) -> list:
    paragraphs = re.split(r"\n\s*\n+", text.strip())
    pages = []
    current_page = []
    current_len = 0

    for p in paragraphs:
        p_clean = p.strip()
        if not p_clean:
            continue
        p_len = len(p_clean)

        if current_len + p_len > target_chars_per_page and current_page:
            pages.append("\n\n".join(current_page))
            current_page = [p_clean]
            current_len = p_len
        else:
            current_page.append(p_clean)
            current_len += p_len + 2

    if current_page:
        pages.append("\n\n".join(current_page))

    return pages

print("=== Digitizing Wave 6 Books ===")
for cfg in WAVE6_CONFIGS:
    file_path = os.path.join(RAW_DIR, cfg["file"])
    if not os.path.exists(file_path):
        print(f"ERROR: Raw text not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    raw_pages = paginate_by_paragraphs(content, target_chars_per_page=2200)
    structured_pages = [
        {"page_number": idx, "text": text}
        for idx, text in enumerate(raw_pages, 1)
    ]

    sample_chapters = []
    for p in structured_pages:
        first_lines = [l.strip() for l in p["text"].splitlines() if l.strip()][:3]
        for l in first_lines:
            if len(l) < 60 and any(keyword in l.lower() for keyword in ["अध्याय", "भाग", "खण्ड", "प्रकरण", "chapter", "section", "part"]):
                if l not in sample_chapters:
                    sample_chapters.append(l)

    book_payload = {
        "id": cfg["id"],
        "title": cfg["title"],
        "author": cfg["author"],
        "year": cfg["year"],
        "language": cfg["language"],
        "category": cfg["category"],
        "description": cfg["description"],
        "source_file": cfg["file"],
        "total_pages": len(structured_pages),
        "chapters_detected": sample_chapters[:15],
        "pages": structured_pages
    }

    out_file = os.path.join(OUTPUT_DIR, f"{cfg['id']}.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(book_payload, f, ensure_ascii=False, indent=2)

    print(f"Created {cfg['id']}.json -> {len(structured_pages)} pages ({os.path.getsize(out_file):,} bytes)")

print("\n=== Rebuilding Master index.json ===")
all_book_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "*.json")))
books_index = []
total_pages_all = 0

for bf in all_book_files:
    if bf.endswith("index.json"):
        continue
    with open(bf, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    entry = {
        "id": data.get("id"),
        "title": data.get("title"),
        "author": data.get("author"),
        "year": data.get("year"),
        "language": data.get("language"),
        "category": data.get("category"),
        "description": data.get("description"),
        "total_pages": data.get("total_pages", len(data.get("pages", []))),
        "json_file": f"{data.get('id')}.json"
    }
    books_index.append(entry)
    total_pages_all += entry["total_pages"]

index_file = os.path.join(OUTPUT_DIR, "index.json")
with open(index_file, "w", encoding="utf-8") as f:
    json.dump(books_index, f, ensure_ascii=False, indent=2)

print(f"Master index.json successfully updated!")
print(f"Total digitized books: {len(books_index)}")
print(f"Total digitized pages: {total_pages_all:,}")
