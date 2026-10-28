# -*- coding: utf-8 -*-
"""
Integrates Wave 9 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "smythe_1932_kamet_conquered",
        "title": "Kamet Conquered: Exploration in the Garhwal Himalaya and the Valley of Flowers",
        "author": "Frank S. Smythe",
        "year": 1932,
        "publisher": "Victor Gollancz Ltd., London / E. P. Dutton & Co., New York",
        "pages": 378,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Acclaimed mountaineering account documenting the expedition to Mount Kamet (25,447 ft) in Garhwal, noting local Bhotia and Garhwali porters, pass routes, alpine flora of the Bhyundar valley (Valley of Flowers), mountain glaciers, and Pahari topography.",
        "archive_id": "dli.pahar.2504"
    },
    {
        "id": "badrinath_kedarnath_yatra_guide",
        "title": "Badrinath-Kedarnath Yatra: Holy Pilgrimage in the Garhwal Himalayas",
        "author": "Pt. Hariram Sharma",
        "year": 1938,
        "publisher": "Shri Badrinath-Kedarnath Temple Committee / Naval Kishore Press, Lucknow",
        "pages": 91,
        "language": "Hindi & Garhwali",
        "category": "culture_and_pilgrimage",
        "significance": "Comprehensive pilgrim guide detailing the sacred traditional routes across Garhwal: Hardwar, Devprayag, Rudraprayag, Kedarnath, Chamoli, Joshimath, and Badrinath, recording local Garhwali river confluences (Prayags), kunds, chattis (halts), dharamsalas, local shrines, and mountain customs.",
        "archive_id": "dli.ernet.258189"
    },
    {
        "id": "smythe_1932_explorations_around_kamet",
        "title": "Explorations in Garhwal around Kamet",
        "author": "Frank S. Smythe",
        "year": 1932,
        "publisher": "The Geographical Journal, Royal Geographical Society, London (Vol. 79, No. 1)",
        "pages": 31,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Geographical exploration paper published in the Geographical Journal describing the terrain, river gorges, glaciers (Arwa, Kamet), high passes, and local Garhwali guides and porter terminology in northern Garhwal.",
        "archive_id": "dli.pahar.2496"
    },
    {
        "id": "history_shrinagar_socio_cultural",
        "title": "History of Srinagar: A Study in Socio-Cultural Change in the Central and Northern Himalayas",
        "author": "Dr. Mohammad Ishaq Khan",
        "year": 1978,
        "publisher": "Cosmos Publications, New Delhi / Sharada Manuscript & eGangotri Digital Trust",
        "pages": 319,
        "language": "English, Urdu & Pahari",
        "category": "history_and_society",
        "significance": "In-depth historical study of socio-cultural developments, mountain trade routes, urban growth, traditional crafts, bazaar economies, and Pahari linguistic interactions in historical Himalayan administrative and cultural capitals.",
        "archive_id": "uYZG_history-of-shrinagar-1846-1947-a-study-in-socio-cultural-change-by-mohammad-isha"
    },
    {
        "id": "parbaton_ki_khushbu_pahari_afsanon",
        "title": "Parbaton Ki Khushbu: Selected Pahari Mountain Tales, Folklore and Idioms",
        "author": "Parvez Maanoos",
        "year": 2020,
        "publisher": "GNK Publications, Budgam",
        "pages": 57,
        "language": "Pahari & Urdu",
        "category": "folklore_and_literature",
        "significance": "Selected Pahari mountain tales, folklore, proverbs, idioms, and oral narratives reflecting everyday Himalayan life, pastoral migration, village festivals, and highland humor.",
        "archive_id": "ndon_parbaton-ki-khushbu-muntakhab-pahari-afsanon-ka-tarjuma-by-parvez-maanoos-u"
    },
    {
        "id": "sivananda_1966_himalayan_forest_academy",
        "title": "Himalayan Forest Hermitage: Health, Nature and Sacred Living in Garhwal",
        "author": "Swami Sivananda",
        "year": 1966,
        "publisher": "The Yoga-Vedanta Forest Academy, Divine Life Society, Muni-ki-Reti, Tehri Garhwal",
        "pages": 183,
        "language": "English & Hindi",
        "category": "philosophy_and_nature",
        "significance": "Writings from the Yoga-Vedanta Forest Academy at Muni-ki-Reti, Tehri Garhwal, describing natural herbal remedies, the restorative atmosphere of the Garhwal Himalayas, Himalayan solitude, Ganges bank life, and spiritual discipline in the hill forests.",
        "archive_id": "berw_health-and-happiness-by-swami-shivanand-1966-garhwal-the-yoga-vedanta-forest-academy"
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

