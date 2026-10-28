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
        "title": "Garhwal Ancient and Modern",
        "author": "राय पातिराम बहादुर (Rai Pati Ram Bahadur)",
        "year": "1916",
        "genre": "इतिहास, समाजशास्त्र एवं लोकसंस्कृति",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व अंग्रेजी",
        "evidence": "Internet Archive: in.ernet.dli.2015.530003",
        "publisher": "F.W. Prebble, Peshawar",
        "pages": "244",
        "isbn": "",
        "source_url": "https://archive.org/details/in.ernet.dli.2015.530003",
        "confidence": "A — foundational primary source",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 2,
        "title": "British Garhwal: A Gazetteer",
        "author": "एच. जी. वाल्टन (H. G. Walton)",
        "year": "1910",
        "genre": "स्थानिक इतिहास, भूगोल एवं वनस्पति शब्दावली",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व अंग्रेजी",
        "evidence": "District Gazetteers of the United Provinces, Vol. XXXVI",
        "publisher": "Government Press, Allahabad",
        "pages": "347",
        "isbn": "",
        "source_url": "https://archive.org/details/in.ernet.dli.2015.181556",
        "confidence": "A — foundational primary source",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 3,
        "title": "The Languages of the Northern Himalayas",
        "author": "रेवरेंड थॉमस ग्राहम बेली (Rev. Thomas Grahame Bailey)",
        "year": "1908",
        "genre": "तुलनात्मक पहाड़ी भाषाशास्त्र एवं व्याकरण",
        "category": "garhwali_grammar_lexicography",
        "category_label": "Garhwali Grammar, Lexicography & Linguistics",
        "language_status": "गढ़वाली, पहाड़ी व अंग्रेजी",
        "evidence": "Royal Asiatic Society Monographs Vol. XII",
        "publisher": "Royal Asiatic Society, London",
        "pages": "285",
        "isbn": "",
        "source_url": "https://archive.org/details/languagesofnorth00bailrich",
        "confidence": "A — foundational primary source",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 4,
        "title": "Pahari Language: A Linguistic Analysis",
        "author": "डॉ. सिद्धेश्वर वर्मा (Dr. Siddheshwar Verma)",
        "year": "1978",
        "genre": "भाषावैज्ञानिक ध्वनिकी एवं संरचनात्मक विश्लेषण",
        "category": "garhwali_grammar_lexicography",
        "category_label": "Garhwali Grammar, Lexicography & Linguistics",
        "language_status": "पहाड़ी, गढ़वाली व अंग्रेजी",
        "evidence": "Vishveshvaranand Vedic Research Institute",
        "publisher": "V.V.R.I. Press, Hoshiarpur",
        "pages": "97",
        "isbn": "",
        "source_url": "https://archive.org/details/1978-pahari-language-a-linguistic-analysis-verma",
        "confidence": "A — scholarly treatise",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 5,
        "title": "Uttar Pradesh District Gazetteers: Tehri Garhwal",
        "author": "उत्तर प्रदेश शासन (C.P. Sharma et al.)",
        "year": "1971",
        "genre": "गजेटियर, आंचलिक अर्थव्यवस्था व लोकसंस्कृति",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व अंग्रेजी",
        "evidence": "State District Gazetteers Department, Lucknow",
        "publisher": "Government of Uttar Pradesh",
        "pages": "394",
        "isbn": "",
        "source_url": "https://archive.org/details/dli.csl.3107",
        "confidence": "A — official state gazetteer",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★☆"
    },
    {
        "id": max_id + 6,
        "title": "श्री उत्तराखण्ड यात्रा दर्शन",
        "author": "डॉ. शिवप्रसाद डबराल 'चारण'",
        "year": "1961",
        "genre": "यात्रावृत्त, तीर्थ भूगोल एवं लोक परंपराएं",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व हिन्दी",
        "evidence": "Veer Gatha Prakashan, Dogadda, Garhwal",
        "publisher": "वीर गाथा प्रकाशन, दुगड्डा (गढ़वाल)",
        "pages": "510",
        "isbn": "",
        "source_url": "https://archive.org/details/in.ernet.dli.2015.309034",
        "confidence": "A — foundational primary source",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 7,
        "title": "गढ़वाल में कौन कहाँ से",
        "author": "महीधर शर्मा बर्थवाल",
        "year": "1938",
        "genre": "वंशानुक्रम, गोत्र एवं ग्राम बसावट इतिहास",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व हिन्दी",
        "evidence": "Garhwali Press, Dehradun 1938",
        "publisher": "गढ़वाली प्रेस, देहरादून",
        "pages": "111",
        "isbn": "",
        "source_url": "https://archive.org/details/garhwal-me-kon-kahan-se_20250415",
        "confidence": "A — genealogical classic",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 8,
        "title": "उत्तराखण्ड का इतिहास (भाग ३: राजनीतिक तथा सांस्कृतिक इतिहास)",
        "author": "डॉ. शिवप्रसाद डबराल 'चारण'",
        "year": "1971",
        "genre": "मध्यकालीन इतिहास, बावन गढ़ एवं लोकसाहित्य",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व हिन्दी",
        "evidence": "Veer Gatha Prakashan, Dogadda",
        "publisher": "वीर गाथा प्रकाशन, दुगड्डा",
        "pages": "581",
        "isbn": "",
        "source_url": "https://archive.org/details/wnbl_uttarakhand-ka-itihas-bhag-3-rajnaitik-tatha-sanskritik-itihas-by-shiv-pras",
        "confidence": "A — definitive historical monograph",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    },
    {
        "id": max_id + 9,
        "title": "उत्तराखण्ड का इतिहास (भाग १: कत्यूरी युग तक साक्ष्य संकलन)",
        "author": "डॉ. शिवप्रसाद डबराल 'चारण'",
        "year": "1965",
        "genre": "प्राचीन इतिहास, अभिलेख एवं भाषा अवशेष",
        "category": "works_about_garhwali",
        "category_label": "Works About Garhwali Language, Folklore & History",
        "language_status": "गढ़वाली व हिन्दी",
        "evidence": "Veer Gatha Prakashan, Dogadda",
        "publisher": "वीर गाथा प्रकाशन, दुगड्डा",
        "pages": "316",
        "isbn": "",
        "source_url": "https://archive.org/details/ozkb_uttarakhand-ka-itihas-katyuri-yug-tak-bhag-1-sakshya-sankalan-by-shiv-prasa",
        "confidence": "A — foundational epigraphic source",
        "corpus_eligibility": "primary_native_corpus",
        "library_value": "★★★★★"
    }
]

bib.extend(new_entries)

with open(BIB_PATH, "w", encoding="utf-8") as f:
    json.dump(bib, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_entries)} books to bibliography.json. New total books in bibliography: {len(bib)}")

