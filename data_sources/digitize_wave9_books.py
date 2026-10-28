# -*- coding: utf-8 -*-
"""
Digitizes Wave 9 books into garhwali/culture/data/books/<id>.json
and updates master index.json.
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

WAVE9_CONFIGS = [
    {
        "id": "smythe_1932_kamet_conquered",
        "file": "smythe_kamet_conquered_1932.txt",
        "title": "Kamet Conquered: Exploration in the Garhwal Himalaya and the Valley of Flowers",
        "author": "Frank S. Smythe",
        "year": 1932,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Acclaimed mountaineering account documenting the expedition to Mount Kamet (25,447 ft) in Garhwal, noting local Bhotia and Garhwali porters, pass routes, alpine flora of the Bhyundar valley (Valley of Flowers), mountain glaciers, and Pahari topography."
    },
    {
        "id": "badrinath_kedarnath_yatra_guide",
        "file": "badrinath_kedarnath_yatra_guide_1938.txt",
        "title": "Badrinath-Kedarnath Yatra: Holy Pilgrimage in the Garhwal Himalayas",
        "author": "Pt. Hariram Sharma",
        "year": 1938,
        "language": "Hindi & Garhwali",
        "category": "culture_and_pilgrimage",
        "description": "Comprehensive pilgrim guide detailing the sacred traditional routes across Garhwal: Hardwar, Devprayag, Rudraprayag, Kedarnath, Chamoli, Joshimath, and Badrinath, recording local Garhwali river confluences (Prayags), kunds, chattis (halts), dharamsalas, local shrines, and mountain customs."
    },
    {
        "id": "smythe_1932_explorations_around_kamet",
        "file": "smythe_explorations_around_kamet_1932.txt",
        "title": "Explorations in Garhwal around Kamet",
        "author": "Frank S. Smythe",
        "year": 1932,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Geographical exploration paper published in the Geographical Journal describing the terrain, river gorges, glaciers (Arwa, Kamet), high passes, and local Garhwali guides and porter terminology in northern Garhwal."
    },
    {
        "id": "history_shrinagar_socio_cultural",
        "file": "khan_history_of_srinagar_himalayas_1978.txt",
        "title": "History of Srinagar: A Study in Socio-Cultural Change in the Central and Northern Himalayas",
        "author": "Dr. Mohammad Ishaq Khan",
        "year": 1978,
        "language": "English, Urdu & Pahari",
        "category": "history_and_society",
        "description": "In-depth historical study of socio-cultural developments, mountain trade routes, urban growth, traditional crafts, bazaar economies, and Pahari linguistic interactions in historical Himalayan administrative and cultural capitals."
    },
    {
        "id": "parbaton_ki_khushbu_pahari_afsanon",
        "file": "maanoos_parbaton_ki_khushbu_pahari_2020.txt",
        "title": "Parbaton Ki Khushbu: Selected Pahari Mountain Tales, Folklore and Idioms",
        "author": "Parvez Maanoos",
        "year": 2020,
        "language": "Pahari & Urdu",
        "category": "folklore_and_literature",
        "description": "Selected Pahari mountain tales, folklore, proverbs, idioms, and oral narratives reflecting everyday Himalayan life, pastoral migration, village festivals, and highland humor."
    },
    {
        "id": "sivananda_1966_himalayan_forest_academy",
        "file": "sivananda_himalayan_forest_academy_garhwal_1966.txt",
        "title": "Himalayan Forest Hermitage: Health, Nature and Sacred Living in Garhwal",
        "author": "Swami Sivananda",
        "year": 1966,
        "language": "English & Hindi",
        "category": "philosophy_and_nature",
        "description": "Writings from the Yoga-Vedanta Forest Academy at Muni-ki-Reti, Tehri Garhwal, describing natural herbal remedies, the restorative atmosphere of the Garhwal Himalayas, Himalayan solitude, Ganges bank life, and spiritual discipline in the hill forests."
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

print("=== Digitizing Wave 9 Books ===")
for cfg in WAVE9_CONFIGS:
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

print(f"Master index.json updated: {len(books_index)} books, {total_pages_all:,} total pages.")
