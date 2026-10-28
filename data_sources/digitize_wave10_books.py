# -*- coding: utf-8 -*-
"""
Digitizes Wave 10 books into garhwali/culture/data/books/<id>.json
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

WAVE10_CONFIGS = [
    {
        "id": "prabodhanand_1961_across_gangotri_glaciers",
        "file": "prabodhanand_across_gangotri_glaciers_1961.txt",
        "title": "Across Gangotri Glaciers: Explorations in Northern Garhwal",
        "author": "Swami Prabodhanand",
        "year": 1961,
        "language": "Hindi & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Exploration chronicle detailing the high-altitude pilgrimage and mountaineering traversal of the Gangotri glacier system, Gaumukh source of Bhagirathi, Meru, Shivling peaks, high ice cols, and local porter routes."
    },
    {
        "id": "painuli_2000_shri_nandadevi_rajjat",
        "file": "painuli_shri_nandadevi_rajjat_2000.txt",
        "title": "Shri Nanda Devi Raj Jat: The Royal Himalayan Pilgrimage of Garhwal",
        "author": "Shiv Kumar Painuli, Dr. Anusuya Prasad Maikhuri & Dr. Bhagwati Prasad Purohit",
        "year": 2000,
        "language": "Garhwali & Hindi",
        "category": "culture_and_folklore",
        "description": "Definitive cultural, ethnographic, and linguistic monograph on the sacred 280-km, 12-yearly royal pilgrimage of Goddess Nanda Devi in Chamoli Garhwal: detailing the four-horned ram (Chausinghya Khadu), ringal parasols (Chhantoli), Nauti to Homkund halts, Jagars, and mountain traditions."
    },
    {
        "id": "shipton_1936_nanda_devi",
        "file": "shipton_nanda_devi_1936.txt",
        "title": "Nanda Devi: Exploration of the Great Himalayan Sanctuary",
        "author": "Eric Shipton",
        "year": 1936,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Historic mountaineering narrative chronicling the pioneering exploration of the Rishi Ganga gorge and penetration of the inner Nanda Devi mountain sanctuary, recording Garhwali and Bhotia porter lore, glacial passes, and alpine navigation."
    },
    {
        "id": "shipton_1935_nanda_devi_ganges_watershed",
        "file": "shipton_nanda_devi_ganges_watershed_1935.txt",
        "title": "Nanda Devi and the Ganges Watershed: Mountain Topography of Garhwal",
        "author": "Eric Shipton",
        "year": 1935,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Geographical paper from the Royal Geographical Society documenting the hydrographic divide, high cols, gorges of the Alaknanda, Dhauli, and Rishi Ganga basins, and local Pahari toponymy."
    },
    {
        "id": "zsi_1997_fauna_nandadevi_biosphere",
        "file": "zsi_fauna_nandadevi_biosphere_1997.txt",
        "title": "Fauna of Nanda Devi Biosphere Reserve: Mammals, Birds and Mountain Wildlife",
        "author": "Zoological Survey of India (ZSI)",
        "year": 1997,
        "language": "English & Garhwali",
        "category": "nature_and_wildlife",
        "description": "Comprehensive biological documentation of high Garhwal fauna across Nanda Devi Biosphere Reserve: Blue sheep (Bharal), Himalayan tahr, musk deer (Kastura), snow leopard, Monal pheasant, and native vernacular wildlife terminology."
    },
    {
        "id": "negi_gaur_1985_flora_khatling_glacier_tehri",
        "file": "negi_gaur_flora_khatling_glacier_tehri_1985.txt",
        "title": "Flora of Khatling Glacier in the Garhwal Himalaya (District Tehri)",
        "author": "K. S. Negi, J. K. Tiwari & R. D. Gaur (HNB Garhwal University)",
        "year": 1985,
        "language": "English & Garhwali",
        "category": "flora_and_ethnobotany",
        "description": "Botanical and ethnopharmacological survey conducted by Garhwal University researchers in the Bhilangna valley and Khatling glacier of Tehri Garhwal, recording indigenous Garhwali plant names, folk remedies, and alpine distribution."
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

print("=== Digitizing Wave 10 Books ===")
for cfg in WAVE10_CONFIGS:
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
