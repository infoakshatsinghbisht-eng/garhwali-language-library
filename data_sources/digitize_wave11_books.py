# -*- coding: utf-8 -*-
"""
Digitizes Wave 11 books into garhwali/culture/data/books/<id>.json
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

WAVE11_CONFIGS = [
    {
        "id": "ross_1874_settlement_jaunsar_bawar",
        "file": "ross_settlement_jaunsar_bawar_1874.txt",
        "title": "Settlement of Pargana Jaunsar-Bawar: Customary Law and Land Tenure",
        "author": "H. G. Ross",
        "year": 1874,
        "language": "Garhwali & English",
        "category": "revenue_and_land_tenure",
        "description": "Foundational colonial revenue and legal settlement codifying the indigenous Dastur-ul-Amal customary law, khat system, village assemblies (sayana), mountain grazing rights, and water-channel maintenance in the Jaunsar-Bawar tract."
    },
    {
        "id": "majumdar_1960_himalayan_polyandry_jaunsar",
        "file": "majumdar_himalayan_polyandry_jaunsar_1960.txt",
        "title": "Himalayan Polyandry: Structure, Functioning and Culture Change in Jaunsar-Bawar",
        "author": "Dr. D. N. Majumdar",
        "year": 1960,
        "language": "Pahari, Garhwali & English",
        "category": "culture_and_ethnology",
        "description": "Landmark anthropological field monograph documenting the kinship terms, marriage rites, folk festivals (Magh, Bissu), Mahasu Devta worship, agricultural cycles, and vernacular Pahari dialect expressions across Jaunsar-Bawar."
    },
    {
        "id": "hearth_1889_deoban_range_jaunsar_forest",
        "file": "hearth_deoban_range_jaunsar_forest_1889.txt",
        "title": "Working Plan of the Deoban Range, Jaunsar Forest Division (N.-W. Provinces)",
        "author": "G. F. Hearth / Forest Department",
        "year": 1889,
        "language": "Garhwali & English",
        "category": "nature_and_forestry",
        "description": "Silvicultural and topographic survey of the Deoban mountain range in Jaunsar-Garhwal, detailing native Himalayan timber species (Deodar, Moru, Kharsu, Spruce), cattle-lopping rights, timber flumes, and bridle passes."
    },
    {
        "id": "sharma_1955_himtirtha_badrinath",
        "file": "sharma_himtirtha_badrinath_1955.txt",
        "title": "Himtirth Badrinath: The Holy Himalayan Sanctum and Sacred Geography",
        "author": "Pt. Devendranath Sharma",
        "year": 1955,
        "language": "Hindi & Garhwali",
        "category": "culture_and_pilgrimage",
        "description": "Comprehensive devotional and geographical treatise on Badrinath Dham, detailing the five sacred Badris (Panch Badri), ancient Rawal sacerdotal traditions, holy confluences along the Alaknanda, and sanctum rituals."
    },
    {
        "id": "tilman_1937_the_ascent_of_nanda_devi",
        "file": "tilman_ascent_of_nanda_devi_1937.txt",
        "title": "The Ascent of Nanda Devi: First Historic Ascent of the Sanctuary Peak",
        "author": "H. W. Tilman",
        "year": 1937,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Classic mountaineering account chronicling the historic first ascent of Mount Nanda Devi (25,645 ft) by H. W. Tilman and Noel Odell in 1936, documenting the Rishi gorge crossing, Garhwali and Bhotia porter companions, and alpine routes."
    },
    {
        "id": "languepin_1956_to_kiss_high_heaven_nanda_devi",
        "file": "languepin_to_kiss_high_heaven_nanda_devi_1956.txt",
        "title": "To Kiss High Heaven: Nanda Devi and Trishul Himalayan Expeditions",
        "author": "J. J. Languepin",
        "year": 1956,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "description": "Expedition narrative detailing French ascents in the Garhwal Himalayas around Nanda Devi, Trishul, and Dunagiri, observing mountain topography, weather conditions, local porter guides, and highland hospitality."
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

print("=== Digitizing Wave 11 Books ===")
for cfg in WAVE11_CONFIGS:
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

