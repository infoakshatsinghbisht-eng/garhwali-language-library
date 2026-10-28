# -*- coding: utf-8 -*-
import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB_PATH = os.path.join(ROOT_DIR, "garhwali", "culture", "data", "bibliography.json")

with open(BIB_PATH, "r", encoding="utf-8") as f:
    bib = json.load(f)

max_id = max(b["id"] for b in bib) if bib else 0

new_entries = [
    {
        "id": max_id + 1,
        "title": "Uttar Pradesh District Gazetteers: Garhwal",
        "author": "उत्तर प्रदेश शासन (Swami Prasad Singh et al.)",
        "year": "1989",
        "genre": "गजेटियर, प्रशासनिक एवं आंचलिक शब्दावली",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व अंग्रेजी",
        "evidence": "State District Gazetteers Department, Lucknow",
        "publisher": "Government of Uttar Pradesh",
        "pages": "288",
        "isbn": "",
        "source_url": "https://archive.org/details/dli.csl.3036",
        "confidence": "A — official state gazetteer",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★☆"
    },
    {
        "id": max_id + 2,
        "title": "Garhwal Painting",
        "author": "मुकुन्दी लाल (Mukandi Lal)",
        "year": "1968",
        "genre": "कला इतिहास, मौलाराम की कविताएं एवं दरबारी संस्कृति",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व अंग्रेजी",
        "evidence": "Publications Division, Ministry of Information and Broadcasting",
        "publisher": "Publications Division, New Delhi",
        "pages": "52",
        "isbn": "",
        "source_url": "https://archive.org/details/GarhwalPainting",
        "confidence": "A — classic art treatise",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 3,
        "title": "Khasa Family Law in the Himalayan Districts",
        "author": "एल. डी. जोशी (L. D. Joshi)",
        "year": "1929",
        "genre": "खस प्रथागत विधि, विवाह, उत्तराधिकार एवं गोत्र व्यवस्था",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली, कुमाऊंनी व अंग्रेजी",
        "evidence": "Government Press, Allahabad",
        "publisher": "Superintendent, Government Press, United Provinces",
        "pages": "346",
        "isbn": "",
        "source_url": "https://archive.org/details/dli.pahar.2397",
        "confidence": "A — foundational customary legal monograph",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 4,
        "title": "Linguistic Studies from the Himalayas",
        "author": "रेवरेंड थॉमस ग्राहम बेली (Rev. Thomas Grahame Bailey)",
        "year": "1915",
        "genre": "पहाड़ी बोलियों का तुलनात्मक भाषाशास्त्रीय अध्ययन",
        "category": "garhwali_grammar_lexicography",
        "category_label": "Garhwali Grammar, Lexicography & Linguistics",
        "language_status": "गढ़वाली, पहाड़ी व अंग्रेजी",
        "evidence": "Royal Asiatic Society Monographs Vol. XV",
        "publisher": "Royal Asiatic Society, London",
        "pages": "214",
        "isbn": "",
        "source_url": "https://archive.org/details/linguisticstudie00bailrich",
        "confidence": "A — foundational linguistic source",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 5,
        "title": "A Dictionary of Pahari Dialects",
        "author": "हिमाचल कला संस्कृति भाषा अकादमी",
        "year": "1909",
        "genre": "पहाड़ी भाषा कोश एवं धातु-संग्रह",
        "category": "garhwali_grammar_lexicography",
        "category_label": "Garhwali Grammar, Lexicography & Linguistics",
        "language_status": "पहाड़ी, गढ़वाली व अंग्रेजी",
        "evidence": "Himachal Academy Archives",
        "publisher": "Himachal Academy of Arts, Culture and Languages",
        "pages": "258",
        "isbn": "",
        "source_url": "https://archive.org/details/in.ernet.dli.2015.223292",
        "confidence": "A — historical dialect dictionary",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★☆"
    },
    {
        "id": max_id + 6,
        "title": "Pahari-Hindi Shabdkosh",
        "author": "हिमाचल कला संस्कृति भाषा अकादमी",
        "year": "1989",
        "genre": "वृहद पहाड़ी-हिन्दी शब्दकोश",
        "category": "garhwali_grammar_lexicography",
        "category_label": "Garhwali Grammar, Lexicography & Linguistics",
        "language_status": "पहाड़ी, गढ़वाली व हिन्दी",
        "evidence": "Himachal Academy of Arts, Culture and Languages, Shimla",
        "publisher": "हिमाचल कला संस्कृति भाषा अकादमी, शिमला",
        "pages": "981",
        "isbn": "",
        "source_url": "https://archive.org/details/1989-pahari-hindi-shabdkosh-by-haacl_202108",
        "confidence": "A — comprehensive lexicon",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 7,
        "title": "The Himalayan Districts of the North-Western Provinces Vol. 1",
        "author": "एडविन टी. एटकिंसन (Edwin T. Atkinson)",
        "year": "1882",
        "genre": "हिमालयी गजेटियर, भूगोल, वनस्पति एवं खनिज",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व अंग्रेजी",
        "evidence": "North-Western Provinces Gazetteer Vol. X",
        "publisher": "North-Western Provinces and Oudh Government Press, Allahabad",
        "pages": "955",
        "isbn": "",
        "source_url": "https://archive.org/details/in.ernet.dli.2015.46900",
        "confidence": "A — monumental Himalayan survey",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    }
]

bib.extend(new_entries)

with open(BIB_PATH, "w", encoding="utf-8") as f:
    json.dump(bib, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_entries)} Wave 2 books to bibliography.json. New total books: {len(bib)}")

