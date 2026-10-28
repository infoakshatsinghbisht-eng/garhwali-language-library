# -*- coding: utf-8 -*-
"""
Integrates Wave 11 books into garhwali/culture/data/bibliography.json.
"""

import json

BIBLIO_PATH = "garhwali/culture/data/bibliography.json"

with open(BIBLIO_PATH, "r", encoding="utf-8") as f:
    biblio = json.load(f)

existing_ids = {b.get("id") for b in biblio}

new_records = [
    {
        "id": "ross_1874_settlement_jaunsar_bawar",
        "title": "Settlement of Pargana Jaunsar-Bawar: Customary Law and Land Tenure",
        "author": "H. G. Ross",
        "year": 1874,
        "publisher": "Superintendent, Government Press, North-Western Provinces, Allahabad",
        "pages": 114,
        "language": "Garhwali & English",
        "category": "revenue_and_land_tenure",
        "significance": "Foundational colonial revenue and legal settlement codifying the indigenous Dastur-ul-Amal customary law, khat system, village assemblies (sayana), mountain grazing rights, and water-channel maintenance in the Jaunsar-Bawar tract.",
        "archive_id": "dli.pahar.0789"
    },
    {
        "id": "majumdar_1960_himalayan_polyandry_jaunsar",
        "title": "Himalayan Polyandry: Structure, Functioning and Culture Change in Jaunsar-Bawar",
        "author": "Dr. D. N. Majumdar",
        "year": 1960,
        "publisher": "Asia Publishing House, Bombay & London",
        "pages": 538,
        "language": "Pahari, Garhwali & English",
        "category": "culture_and_ethnology",
        "significance": "Landmark anthropological field monograph documenting the kinship terms, marriage rites, folk festivals (Magh, Bissu), Mahasu Devta worship, agricultural cycles, and vernacular Pahari dialect expressions across Jaunsar-Bawar.",
        "archive_id": "dli.pahar.3163"
    },
    {
        "id": "hearth_1889_deoban_range_jaunsar_forest",
        "title": "Working Plan of the Deoban Range, Jaunsar Forest Division (N.-W. Provinces)",
        "author": "G. F. Hearth / Forest Department",
        "year": 1889,
        "publisher": "Superintendent, Government Press, Allahabad",
        "pages": 391,
        "language": "Garhwali & English",
        "category": "nature_and_forestry",
        "significance": "Silvicultural and topographic survey of the Deoban mountain range in Jaunsar-Garhwal, detailing native Himalayan timber species (Deodar, Moru, Kharsu, Spruce), cattle-lopping rights, timber flumes, and bridle passes.",
        "archive_id": "wbsl.14555"
    },
    {
        "id": "sharma_1955_himtirtha_badrinath",
        "title": "Himtirth Badrinath: The Holy Himalayan Sanctum and Sacred Geography",
        "author": "Pt. Devendranath Sharma",
        "year": 1955,
        "publisher": "Shri Badrinath Kedar Temple Committee, Chamoli / Naval Kishore Press",
        "pages": 39,
        "language": "Hindi & Garhwali",
        "category": "culture_and_pilgrimage",
        "significance": "Comprehensive devotional and geographical treatise on Badrinath Dham, detailing the five sacred Badris (Panch Badri), ancient Rawal sacerdotal traditions, holy confluences along the Alaknanda, and sanctum rituals.",
        "archive_id": "in.ernet.dli.2015.452383"
    },
    {
        "id": "tilman_1937_the_ascent_of_nanda_devi",
        "title": "The Ascent of Nanda Devi: First Historic Ascent of the Sanctuary Peak",
        "author": "H. W. Tilman",
        "year": 1937,
        "publisher": "Cambridge University Press, Cambridge & Macmillan, New York",
        "pages": 232,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Classic mountaineering account chronicling the historic first ascent of Mount Nanda Devi (25,645 ft) by H. W. Tilman and Noel Odell in 1936, documenting the Rishi gorge crossing, Garhwali and Bhotia porter companions, and alpine routes.",
        "archive_id": "in.ernet.dli.2015.79797"
    },
    {
        "id": "languepin_1956_to_kiss_high_heaven_nanda_devi",
        "title": "To Kiss High Heaven: Nanda Devi and Trishul Himalayan Expeditions",
        "author": "J. J. Languepin",
        "year": 1956,
        "publisher": "William Kimber & Co. Ltd., London",
        "pages": 176,
        "language": "English & Garhwali",
        "category": "geography_and_mountaineering",
        "significance": "Expedition narrative detailing French ascents in the Garhwal Himalayas around Nanda Devi, Trishul, and Dunagiri, observing mountain topography, weather conditions, local porter guides, and highland hospitality.",
        "archive_id": "languepin-1956-to-kiss-high-heaven-nanda-devi"
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

