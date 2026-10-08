# -*- coding: utf-8 -*-
"""
Script to build page-by-page structured digital book archives for Garhwali Language Library.

Processes full text books from data_sources/raw_texts/ and structures them into:
garhwali/culture/data/books/<book_id>.json
and creates garhwali/culture/data/books/index.json.
"""

import os
import sys
import json
import re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw_texts")
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "garhwali", "culture", "data", "books"
)
os.makedirs(OUTPUT_DIR, exist_ok=True)

BOOK_CONFIGS = [
    {
        "id": "grierson_1916_central_pahari",
        "file": "grierson_lsi_vol9_pt4_garhwal_1916.txt",
        "title": "Linguistic Survey of India: Central Pahari / Garhwali",
        "author": "Sir George Abraham Grierson",
        "year": 1916,
        "language": "Garhwali & English",
        "category": "grammar_and_linguistics",
        "description": "Exhaustive linguistic and grammatical survey of Garhwali and Central Pahari dialects with comparative vocabularies, noun declensions, verb matrices, and specimen folk texts.",
        "explicit_page_marker": None
    },
    {
        "id": "upreti_1894_proverbs_folklore",
        "file": "upreti_proverbs_folklore_garhwal_1894.txt",
        "title": "Proverbs & Folklore of Kumaun and Garhwal",
        "author": "Pandit Ganga Datt Upreti",
        "year": 1894,
        "language": "Garhwali, Kumauni & English",
        "category": "folklore_and_proverbs",
        "description": "Extensive collection of authentic Garhwali and Kumauni proverbs, rural riddles, idioms, and cultural folk customs with translations and critical commentaries.",
        "explicit_page_marker": None
    },
    {
        "id": "oakley_gairola_1935_folklore",
        "file": "oakley_gairola_himalayan_folklore_1935.txt",
        "title": "Himalayan Folklore",
        "author": "Rev. E.S. Oakley and Tara Dutt Gairola",
        "year": 1935,
        "language": "Garhwali Folklore in English & Vernacular",
        "category": "folklore_and_epics",
        "description": "Seminal collection of classical Garhwali folk epics, legends of brave warriors (Bhads), deities, and Himalayan ghost tales.",
        "explicit_page_marker": None
    },
    {
        "id": "chatak_1959_garhwali_bhasha",
        "file": "govind_chatak_garhwali_bhasha_1959.txt",
        "title": "Garhwali Bhasha: Ek Bhashashastriya Adhyayan",
        "author": "Dr. Govind Chatak",
        "year": 1959,
        "language": "Garhwali & Hindi",
        "category": "grammar_and_linguistics",
        "description": "Authoritative linguistic, phonetic, and morphological treatise on the structure of the Garhwali language and its dialect variations.",
        "explicit_page_marker": None
    },
    {
        "id": "chatak_1958_lok_gathayen",
        "file": "govind_chatak_gadwali_lok_gathayen_1958.txt",
        "title": "Gadwali Lok Gathayen (Pawada & Jagar Epics)",
        "author": "Dr. Govind Chatak",
        "year": 1958,
        "language": "Garhwali & Hindi",
        "category": "folklore_and_epics",
        "description": "Complete collection of traditional Garhwali oral ballads, warrior epics (Pawadas), and temple Jagar invocations.",
        "explicit_page_marker": None
    },
    {
        "id": "bhatt_1976_garhwali_sahitya",
        "file": "haridatta_bhatt_garhwali_bhasha_aur_sahitya_1976.txt",
        "title": "Garhwali Bhasha Aur Uska Sahitya",
        "author": "Dr. Haridatta Bhatt 'Shailesh'",
        "year": 1976,
        "language": "Garhwali & Hindi",
        "category": "literature_and_history",
        "description": "Comprehensive history of Garhwali literature, canonical authors, folk forms, dialectology, and cultural traditions.",
        "explicit_page_marker": None
    },
    {
        "id": "juyal_1967_madhya_pahadi",
        "file": "gunanand_juyal_madhya_pahadi_bhasha_1967.txt",
        "title": "Madhya Pahadi Bhasha (Garhwali-Kumauni) Ka Anushilan",
        "author": "Dr. Gunanand Juyal",
        "year": 1967,
        "language": "Garhwali & Hindi",
        "category": "grammar_and_linguistics",
        "description": "Comparative scholarly linguistic study of Central Pahari dialects (Garhwali and Kumaoni) and their phonetic relationship with Sanskrit and Prakrit.",
        "explicit_page_marker": None
    },
    {
        "id": "negi_1954_sahitya_bhumika",
        "file": "shyam_chand_negi_gadwali_sahitya_1954.txt",
        "title": "Gadwali Sahitya Ki Bhumika",
        "author": "Shyam Chand Negi",
        "year": 1954,
        "language": "Garhwali & Hindi",
        "category": "literature_and_history",
        "description": "Pioneering critical introduction to classical and modern Garhwali literary traditions, plays, and poetry.",
        "explicit_page_marker": None
    },
    {
        "id": "chaudhary_1994_lokkala",
        "file": "shanti_chaudhary_garhwali_lokkala_1994.txt",
        "title": "Garhwali Lokkala Aur Loksahitya Ka Tulnatmak Anusilan",
        "author": "Shanti Chaudhary",
        "year": 1994,
        "language": "Garhwali & Hindi",
        "category": "culture_and_arts",
        "description": "Comparative research on Garhwali folk arts, Aipan designs, woodcraft, and oral literary traditions.",
        "explicit_page_marker": None
    },
    {
        "id": "uou_cgl_102_garhwali_prose",
        "file": "uou_cgl_102_text.txt",
        "title": "Chayanit Garhwali Gadya (Selected Garhwali Prose)",
        "author": "Uttarakhand Open University",
        "year": 2020,
        "language": "Garhwali & Hindi",
        "category": "open_courseware_and_education",
        "description": "University textbook of selected Garhwali short stories, essays, plays, and autobiographical sketches.",
        "explicit_page_marker": r"---\s*Page\s+(\d+)\s*---"
    },
    {
        "id": "uou_cgl_103_garhwali_poetry",
        "file": "uou_cgl_103_text.txt",
        "title": "Chayanit Garhwali Kavya (Selected Garhwali Poetry)",
        "author": "Uttarakhand Open University",
        "year": 2020,
        "language": "Garhwali & Hindi",
        "category": "open_courseware_and_education",
        "description": "University textbook of canonical and modern Garhwali poetry, songs, and metrical analysis.",
        "explicit_page_marker": r"---\s*Page\s+(\d+)\s*---"
    },
    {
        "id": "uou_cgl_104_grammar",
        "file": "uou_cgl_104_text.txt",
        "title": "Garhwali Bhasha, Vyakaran Evam Lipi (Language, Grammar & Script)",
        "author": "Uttarakhand Open University",
        "year": 2020,
        "language": "Garhwali & Hindi",
        "category": "grammar_and_linguistics",
        "description": "Official university textbook on Garhwali phonetics, grammar rules, cases, tenses, and Devanagari script writing.",
        "explicit_page_marker": r"---\s*Page\s+(\d+)\s*---"
    },
    {
        "id": "uou_aecc_101_general",
        "file": "uou_aecc_g_101_text.txt",
        "title": "Garhwali Bhasha Adhyayan (General Garhwali Studies)",
        "author": "Uttarakhand Open University",
        "year": 2020,
        "language": "Garhwali & Hindi",
        "category": "open_courseware_and_education",
        "description": "Foundation university courseware on Garhwali communication, cultural idioms, and regional literature.",
        "explicit_page_marker": r"---\s*Page\s+(\d+)\s*---"
    }
]


def paginate_by_paragraphs(text: str, target_chars_per_page: int = 2200) -> list:
    """Split text into logical book pages respecting paragraphs."""
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


def paginate_explicit(text: str, marker_pattern: str) -> list:
    """Split text using explicit page markers like '--- Page N ---'."""
    parts = re.split(marker_pattern, text)
    pages = []
    # parts: [preamble, page_num1, text1, page_num2, text2, ...]
    if len(parts) >= 3:
        i = 1
        while i < len(parts):
            try:
                p_num = int(parts[i])
            except ValueError:
                p_num = len(pages) + 1
            p_text = parts[i + 1].strip() if i + 1 < len(parts) else ""
            if p_text:
                pages.append({"page_number": p_num, "text": p_text})
            i += 2
    else:
        # Fallback to paragraph pagination
        raw_pages = paginate_by_paragraphs(text)
        for idx, pt in enumerate(raw_pages, 1):
            pages.append({"page_number": idx, "text": pt})
    return pages


def build_all_books():
    books_index = []
    print(f"Building page-by-page book corpus in {OUTPUT_DIR}...")

    for cfg in BOOK_CONFIGS:
        file_path = os.path.join(RAW_DIR, cfg["file"])
        if not os.path.exists(file_path):
            print(f"WARNING: File not found: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if cfg["explicit_page_marker"]:
            structured_pages = paginate_explicit(content, cfg["explicit_page_marker"])
        else:
            raw_pages = paginate_by_paragraphs(content, target_chars_per_page=2200)
            structured_pages = [
                {"page_number": idx, "text": text}
                for idx, text in enumerate(raw_pages, 1)
            ]

        # Extract sample chapters/sections
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

        books_index.append({
            "id": cfg["id"],
            "title": cfg["title"],
            "author": cfg["author"],
            "year": cfg["year"],
            "language": cfg["language"],
            "category": cfg["category"],
            "description": cfg["description"],
            "total_pages": len(structured_pages),
            "json_file": f"{cfg['id']}.json"
        })

    index_file = os.path.join(OUTPUT_DIR, "index.json")
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(books_index, f, ensure_ascii=False, indent=2)

    print(f"\nAll books built successfully! Total books in corpus: {len(books_index)}")
    print(f"Index created at {index_file}")


if __name__ == "__main__":
    build_all_books()
