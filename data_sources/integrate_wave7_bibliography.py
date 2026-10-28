# -*- coding: utf-8 -*-
"""
Integrates Wave 7 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "lsi_2023_himachal_pahari_survey",
        "title": "Linguistic Survey of India: Pahari Dialects of the Western and Central Himalayas",
        "author": "Language Division, Office of the Registrar General, Government of India",
        "year": 2023,
        "publisher": "Government of India Press, New Delhi",
        "pages": 596,
        "language": "Pahari, Garhwali & English",
        "category": "grammar_and_linguistics",
        "significance": "Comprehensive modern linguistic survey documenting the Pahari dialect continuum, comparative nominal inflections, ergative case markers, and verbal morphology.",
        "archive_id": "PARI.linguistic-survey-of-india---himachal-pradesh"
    },
    {
        "id": "shrestha_2000_grammar_of_pahari",
        "title": "A Grammar of Pahari: Phonology, Morphology and Syntax",
        "author": "Dr. Omkareshwor Shrestha",
        "year": 2000,
        "publisher": "Tribhuvan University / Linguistic Society of Nepal",
        "pages": 217,
        "language": "Pahari, Garhwali & English",
        "category": "grammar_and_linguistics",
        "significance": "Scholarly grammatical treatise detailing Pahari phonetics, noun declension classes, split-ergative case alignment, compound verb stems, and modal auxiliaries.",
        "archive_id": "AGrammarOfPahariPhDDissertationByOmkareshworShrestha"
    },
    {
        "id": "lewis_1995_himalayas_history_religion",
        "title": "The Himalayas: A Syllabus of the Region's History, Anthropology, and Religion",
        "author": "Todd Lewis",
        "year": 1995,
        "publisher": "Association for Asian Studies / Pahar Publications",
        "pages": 140,
        "language": "Garhwali & English",
        "category": "culture_and_geography",
        "significance": "Comprehensive academic survey of Central Himalayan history, sacred topography of Garhwal and Kumaon shrines, Shaivite/Shakta ritual centers, and mountain anthropology.",
        "archive_id": "dli.pahar.3680"
    },
    {
        "id": "roch_1947_garhwal_himalaya",
        "title": "Garhwal Himalaya: Mountain Expeditions and High Passes",
        "author": "André Roch",
        "year": 1947,
        "publisher": "Swiss Foundation for Alpine Research / Pahar Publications",
        "pages": 131,
        "language": "Garhwali & English",
        "category": "travel_and_exploration",
        "significance": "First-hand expedition narrative documenting ascents of Garhwal peaks (Chaukhamba, Satopanth, Bhagirathi), high glacial passes, alpine flora, and encounters with local Bhotia porters.",
        "archive_id": "dli.pahar.2868"
    },
    {
        "id": "himachal_shabdawali_kangari_pahari",
        "title": "Himachali and Pahari Shabdawali: Comparative Himalayan Vocabulary",
        "author": "BVP Research Collection / Linguistic Cell",
        "year": 1998,
        "publisher": "BVP Research Collection, Hoshiarpur",
        "pages": 25,
        "language": "Pahari, Garhwali & Hindi",
        "category": "lexicography_and_dictionary",
        "significance": "Lexicographic compilation of native agricultural tools, mountain livestock terminology, seasonal festivals, kinship terms, and verbal roots across Pahari dialects.",
        "archive_id": "bvp-05997-md-himachali-kangari-shabdawali"
    },
    {
        "id": "auden_1936_structure_himalaya_garhwal",
        "title": "The Structure of the Himalaya in Garhwal",
        "author": "J. B. Auden",
        "year": 1936,
        "publisher": "Geological Survey of India Records, Vol. 71, Calcutta",
        "pages": 38,
        "language": "Garhwali & English",
        "category": "geography_and_mountaineering",
        "significance": "Landmark geological and topographical survey of the Garhwal Himalaya, the Bhagirathi and Alaknanda gorges, river terraces, mountain thrusts, and rock formations.",
        "archive_id": "dli.pahar.2649"
    }
]

added = 0
for r in new_records:
    if r["id"] not in existing_ids:
        biblio.append(r)
        added += 1

with open(BIBLIO_PATH, "w", encoding="utf-8") as f:
    json.dump(biblio, f, ensure_ascii=False, indent=2)

print(f"Added {added} records to bibliography. Total records: {len(biblio)}")

