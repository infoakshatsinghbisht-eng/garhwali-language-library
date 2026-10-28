# -*- coding: utf-8 -*-
"""
Digitizes Wave 7 books into garhwali/culture/data/books/<id>.json
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

WAVE7_CONFIGS = [
    {
        "id": "lsi_2023_himachal_pahari_survey",
        "file": "lsi_himachal_pahari_language_survey_2023.txt",
        "title": "Linguistic Survey of India: Pahari Dialects of the Western and Central Himalayas",
        "author": "Language Division, Office of the Registrar General, Government of India",
        "year": 2023,
        "language": "Pahari, Garhwali & English",
        "category": "grammar_and_linguistics",
        "description": "Comprehensive modern linguistic survey documenting the Pahari dialect continuum, comparative nominal inflections, ergative case markers, and verbal morphology."
    },
    {
        "id": "shrestha_2000_grammar_of_pahari",
        "file": "shrestha_grammar_of_pahari_phd.txt",
        "title": "A Grammar of Pahari: Phonology, Morphology and Syntax",
        "author": "Dr. Omkareshwor Shrestha",
        "year": 2000,
        "language": "Pahari, Garhwali & English",
        "category": "grammar_and_linguistics",
        "description": "Scholarly grammatical treatise detailing Pahari phonetics, noun declension classes, split-ergative case alignment, compound verb stems, and modal auxiliaries."
    },
    {
        "id": "lewis_1995_himalayas_history_religion",
        "file": "lewis_himalayas_history_anthropology_religion_1995.txt",
        "title": "The Himalayas: A Syllabus of the Region's History, Anthropology, and Religion",
        "author": "Todd Lewis",
        "year": 1995,
        "language": "Garhwali & English",
        "category": "culture_and_geography",
        "description": "Comprehensive academic survey of Central Himalayan history, sacred topography of Garhwal and Kumaon shrines, Shaivite/Shakta ritual centers, and mountain anthropology."
    },
    {
        "id": "roch_1947_garhwal_himalaya",
        "file": "roch_garhwal_himalaya_1947.txt",
        "title": "Garhwal Himalaya: Mountain Expeditions and High Passes",
        "author": "André Roch",
        "year": 1947,
        "language": "Garhwali & English",
        "category": "travel_and_exploration",
        "description": "First-hand expedition narrative documenting ascents of Garhwal peaks (Chaukhamba, Satopanth, Bhagirathi), high glacial passes, alpine flora, and encounters with local Bhotia porters."
    },
    {
        "id": "himachal_shabdawali_kangari_pahari",
        "file": "himachali_kangari_pahari_shabdawali.txt",
        "title": "Himachali and Pahari Shabdawali: Comparative Himalayan Vocabulary",
        "author": "BVP Research Collection / Linguistic Cell",
        "year": 1998,
        "language": "Pahari, Garhwali & Hindi",
        "category": "lexicography_and_dictionary",
        "description": "Lexicographic compilation of native agricultural tools, mountain livestock terminology, seasonal festivals, kinship terms, and verbal roots across Pahari dialects."
    },
    {
        "id": "auden_1936_structure_himalaya_garhwal",
        "file": "auden_structure_himalaya_garhwal_1936.txt",
        "title": "The Structure of the Himalaya in Garhwal",
        "author": "J. B. Auden",
        "year": 1936,
        "language": "Garhwali & English",
        "category": "geography_and_mountaineering",
        "description": "Landmark geological and topographical survey of the Garhwal Himalaya, the Bhagirathi and Alaknanda gorges, river terraces, mountain thrusts, and rock formations."
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

print("=== Digitizing Wave 7 Books ===")
for cfg in WAVE7_CONFIGS:
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

