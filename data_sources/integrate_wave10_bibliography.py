# -*- coding: utf-8 -*-
"""
Integrates Wave 10 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "prabodhanand_1961_across_gangotri_glaciers",
        "title": "Across Gangotri Glaciers: Explorations in Northern Garhwal",
        "author": "Swami Prabodhanand",
        "year": 1961,
        "publisher": "Shri Badrinath-Kedarnath Samiti / Gyanendra Press, Rishikesh",
        "pages": 50,
        "language": "Hindi & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Exploration chronicle detailing the high-altitude pilgrimage and mountaineering traversal of the Gangotri glacier system, Gaumukh source of Bhagirathi, Meru, Shivling peaks, high ice cols, and local porter routes.",
        "archive_id": "dli.pahar.3173"
    },
    {
        "id": "painuli_2000_shri_nandadevi_rajjat",
        "title": "Shri Nanda Devi Raj Jat: The Royal Himalayan Pilgrimage of Garhwal",
        "author": "Shiv Kumar Painuli, Dr. Anusuya Prasad Maikhuri & Dr. Bhagwati Prasad Purohit",
        "year": 2000,
        "publisher": "Nanda Devi Raj Jat Samiti / Navprabhat Press, Chamoli Garhwal",
        "pages": 23,
        "language": "Garhwali & Hindi",
        "category": "culture_and_folklore",
        "significance": "Definitive cultural, ethnographic, and linguistic monograph on the sacred 280-km, 12-yearly royal pilgrimage of Goddess Nanda Devi in Chamoli Garhwal: detailing the four-horned ram (Chausinghya Khadu), ringal parasols (Chhantoli), Nauti to Homkund halts, Jagars, and mountain traditions.",
        "archive_id": "20260126_20260126_0914"
    },
    {
        "id": "shipton_1936_nanda_devi",
        "title": "Nanda Devi: Exploration of the Great Himalayan Sanctuary",
        "author": "Eric Shipton",
        "year": 1936,
        "publisher": "Hodder and Stoughton, London",
        "pages": 235,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Historic mountaineering narrative chronicling the pioneering exploration of the Rishi Ganga gorge and penetration of the inner Nanda Devi mountain sanctuary, recording Garhwali and Bhotia porter lore, glacial passes, and alpine navigation.",
        "archive_id": "dli.pahar.2644"
    },
    {
        "id": "shipton_1935_nanda_devi_ganges_watershed",
        "title": "Nanda Devi and the Ganges Watershed: Mountain Topography of Garhwal",
        "author": "Eric Shipton",
        "year": 1935,
        "publisher": "The Geographical Journal (Royal Geographical Society, Vol. 85, No. 4), London",
        "pages": 33,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Geographical paper from the Royal Geographical Society documenting the hydrographic divide, high cols, gorges of the Alaknanda, Dhauli, and Rishi Ganga basins, and local Pahari toponymy.",
        "archive_id": "dli.pahar.2609"
    },
    {
        "id": "zsi_1997_fauna_nandadevi_biosphere",
        "title": "Fauna of Nanda Devi Biosphere Reserve: Mammals, Birds and Mountain Wildlife",
        "author": "Zoological Survey of India (ZSI)",
        "year": 1997,
        "publisher": "Zoological Survey of India, Fauna of Conservation Areas Series, Dehradun & Calcutta",
        "pages": 116,
        "language": "English & Garhwali",
        "category": "nature_and_wildlife",
        "significance": "Comprehensive biological documentation of high Garhwal fauna across Nanda Devi Biosphere Reserve: Blue sheep (Bharal), Himalayan tahr, musk deer (Kastura), snow leopard, Monal pheasant, and native vernacular wildlife terminology.",
        "archive_id": "dli.zoological.cas.009"
    },
    {
        "id": "negi_gaur_1985_flora_khatling_glacier_tehri",
        "title": "Flora of Khatling Glacier in the Garhwal Himalaya (District Tehri)",
        "author": "K. S. Negi, J. K. Tiwari & R. D. Gaur (HNB Garhwal University)",
        "year": 1985,
        "publisher": "Journal of the Bombay Natural History Society / HNB Garhwal University Srinagar",
        "pages": 19,
        "language": "English & Garhwali",
        "category": "flora_and_ethnobotany",
        "significance": "Botanical and ethnopharmacological survey conducted by Garhwal University researchers in the Bhilangna valley and Khatling glacier of Tehri Garhwal, recording indigenous Garhwali plant names, folk remedies, and alpine distribution.",
        "archive_id": "biostor-153424"
    }
]

added = 0
for r in new_records:
    if r["id"] not in existing_ids:
        biblio.append(r)
        existing_ids.add(r["id"])
        added += 1

with open(BIBLIO_PATH, "w", encoding="utf-8") as f:
    json.dump(biblio, f, ensure_ascii=False, indent=2)

print(f"Added {added} records to bibliography.json. Total canonical records: {len(biblio)}.")
