# -*- coding: utf-8 -*-
"""
Batch 6: Final push to 3,100+ Garhwali words covering:
- Traditional measurements (Patha, Bitta, Kos)
- Time intervals and diurnal cycle
- Body anatomy parts in detail
- Psychological traits, temperament, and character
- Weather, precipitation, and seasonal elements
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(ROOT_DIR, "garhwali", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"].strip() for w in words}

NEW_WORDS = [
    # Traditional Pahari Measurements
    {"garhwali": "पाथा", "hindi": "पाथा (लकड़ी का अनाज मापक पात्र, लगभग 2 किग्रा)", "english": "traditional wooden grain measurement vessel (~2 kg)", "pos": "noun", "gender": "M", "category": "measurement"},
    {"garhwali": "कुड़ी", "hindi": "कुड़ी (पाथा का चौथाई भाग, लगभग 500 ग्राम)", "english": "one-quarter of a patha volume measure", "pos": "noun", "gender": "F", "category": "measurement"},
    {"garhwali": "तामी", "hindi": "तामी (तांबे का अनाज मापक पात्र)", "english": "copper standard grain vessel", "pos": "noun", "gender": "F", "category": "measurement"},
    {"garhwali": "ढाकर", "hindi": "पीठ पर लादकर ले जाने वाला भारी बोझ", "english": "heavy mountain back-load carried with tump-line", "pos": "noun", "gender": "M", "category": "measurement"},
    {"garhwali": "मुट्ठी", "hindi": "मुट्ठी भर परिमाण", "english": "fistful measure", "pos": "noun", "gender": "F", "category": "measurement"},
    {"garhwali": "अंजलि", "hindi": "ओक / दोनों हाथों की अंजलि", "english": "cupped hands volume measure", "pos": "noun", "gender": "F", "category": "measurement"},
    {"garhwali": "बित्ता", "hindi": "बालिश्त / बित्ता (अंगूठे से कनिष्ठिका तक)", "english": "span measure from thumb to little finger", "pos": "noun", "gender": "M", "category": "measurement"},
    {"garhwali": "कदम", "hindi": "पग / डग / कदम", "english": "walking pace distance", "pos": "noun", "gender": "M", "category": "measurement"},
    {"garhwali": "कोस", "hindi": "कोस (लगभग 3 किलोमीटर)", "english": "mountain league distance (~3 km)", "pos": "noun", "gender": "M", "category": "measurement"},
    {"garhwali": "नाली", "hindi": "नाली (पहाड़ी भूमि का मापक, लगभग 240 वर्ग गज)", "english": "traditional Himalayan land area unit (240 sq yards)", "pos": "noun", "gender": "F", "category": "measurement"},
    {"garhwali": "बीघा", "hindi": "बीघा (भूमि मापक, 20 नाली)", "english": "traditional land bigha (20 nalis)", "pos": "noun", "gender": "M", "category": "measurement"},

    # Diurnal Time & Calendar
    {"garhwali": "भोर", "hindi": "तड़का / उषाकाल", "english": "first light before dawn", "pos": "noun", "gender": "F", "category": "time"},
    {"garhwali": "दुपहरिया", "hindi": "मध्याह्न / दोपहर", "english": "midday / noon heat", "pos": "noun", "gender": "F", "category": "time"},
    {"garhwali": "गोधूलि", "hindi": "गोधूलि वेला / संध्‍या", "english": "twilight cow-dust hour at dusk", "pos": "noun", "gender": "F", "category": "time"},
    {"garhwali": "अर्धरात्रि", "hindi": "आधी रात / निशीथ", "english": "midnight", "pos": "noun", "gender": "F", "category": "time"},
    {"garhwali": "पहर", "hindi": "प्रहर (तीन घंटे का समय)", "english": "three-hour watch of day or night", "pos": "noun", "gender": "M", "category": "time"},
    {"garhwali": "घड़ी", "hindi": "घड़ी / २४ मिनट का समय", "english": "traditional 24-minute time unit / clock", "pos": "noun", "gender": "F", "category": "time"},
    {"garhwali": "पल", "hindi": "क्षण / पल", "english": "instant / moment", "pos": "noun", "gender": "M", "category": "time"},
    {"garhwali": "पखवाड़ा", "hindi": "पक्ष / पंद्रह दिन", "english": "fortnight (waxing/waning phase)", "pos": "noun", "gender": "M", "category": "time"},
    {"garhwali": "संवत", "hindi": "विक्रम संवत / वर्ष", "english": "era / calendar year", "pos": "noun", "gender": "M", "category": "time"},

    # Detailed Anatomy
    {"garhwali": "मस्तक", "hindi": "माथा / ललाट", "english": "forehead / brow", "pos": "noun", "gender": "M", "category": "anatomy"},
    {"garhwali": "भवें", "hindi": "भौंहें", "english": "eyebrows", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "पलक", "hindi": "बरौनी / पलक", "english": "eyelid / eyelashes", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "पुतली", "hindi": "आंख की पुतली", "english": "pupil of eye", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "ठुड्डी", "hindi": "चिबुक / ठोड़ी", "english": "chin", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "मूंछ", "hindi": "मूंछ", "english": "mustache", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "दाढ़ी", "hindi": "कूर्मि / दाढ़ी", "english": "beard", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "कंधा", "hindi": "स्कंध / कंधा", "english": "shoulder", "pos": "noun", "gender": "M", "category": "anatomy"},
    {"garhwali": "कोहनी", "hindi": "कूर्पर / कोहनी", "english": "elbow", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "कलाई", "hindi": "मणिबंध / कलाई", "english": "wrist", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "हथेली", "hindi": "करतल / हथेली", "english": "palm of hand", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "नाखून", "hindi": "नख / नाखून", "english": "fingernail / claw", "pos": "noun", "gender": "M", "category": "anatomy"},
    {"garhwali": "पेट", "hindi": "उदर / पेट", "english": "belly / abdomen", "pos": "noun", "gender": "M", "category": "anatomy"},
    {"garhwali": "नाभि", "hindi": "टुंडी / नाभि", "english": "navel / belly button", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "पीठ", "hindi": "पृष्ठ / पीठ", "english": "back of torso", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "जांघ", "hindi": "ऊरु / जांघ", "english": "thigh", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "घुटना", "hindi": "जानु / घुटना", "english": "knee", "pos": "noun", "gender": "M", "category": "anatomy"},
    {"garhwali": "पिंडली", "hindi": "जंघा / पिंडली", "english": "calf of leg", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "टखना", "hindi": "गुल्फ / टखना", "english": "ankle", "pos": "noun", "gender": "M", "category": "anatomy"},
    {"garhwali": "एड़ी", "hindi": "पाणि / एड़ी", "english": "heel", "pos": "noun", "gender": "F", "category": "anatomy"},
    {"garhwali": "तलवा", "hindi": "पगथली / तलवा", "english": "sole of foot", "pos": "noun", "gender": "M", "category": "anatomy"},

    # Personality, Mind & Character Traits
    {"garhwali": "धैर्य", "hindi": "धीरज / सब्र", "english": "patience / forbearance", "pos": "noun", "gender": "M", "category": "personality"},
    {"garhwali": "उतावला", "hindi": "व्यग्र / अधीर / जल्दबाज", "english": "impatient / hasty", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "चतुर", "hindi": "होशियार / चालाक", "english": "clever / astute", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "सयाना", "hindi": "बुद्धिमान / प्रौढ़", "english": "wise / mature", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "भोला", "hindi": "सरल / निष्कपट", "english": "innocent / naive / guileless", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "कपटी", "hindi": "छली / धोखेबाज", "english": "deceitful / treacherous", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "लोभी", "hindi": "लालची / तृष्णालु", "english": "greedy / covetous", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "दानी", "hindi": "उदार / दानवीर", "english": "generous / philanthropic", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "कंजूस", "hindi": "कृपण / कंजूस", "english": "miserly / stingy", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "निडर", "hindi": "साहसी / निर्भय", "english": "fearless / bold", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "डरपोक", "hindi": "भीरु / कायर", "english": "timid / cowardly", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "मेहनती", "hindi": "कर्मठ / परिश्रमी", "english": "hardworking / diligent", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "आलसी", "hindi": "सुस्त / प्रमादी", "english": "lazy / indolent", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "झगड़ालू", "hindi": "लड़ाकू / कलहप्रिय", "english": "quarrelsome / contentious", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "मिलनसार", "hindi": "सामाजिक / सौहार्दपूर्ण", "english": "amiable / sociable", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "हसमुख", "hindi": "प्रसन्नचित्त / विनोदी", "english": "cheerful / jovial", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "गंभीर", "hindi": "शांत / धीर-गंभीर", "english": "solemn / dignified / reserved", "pos": "adjective", "gender": "M", "category": "personality"},

    # Mountain Weather Elements
    {"garhwali": "ह्युं", "hindi": "बर्फ / हिम", "english": "high alpine snow", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "झकोरा", "hindi": "हवा का झोंका", "english": "sudden wind gust across gorge", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "फुहार", "hindi": "धीमी फुहार / रिमझिम", "english": "gentle mountain drizzle", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "ओला", "hindi": "करापात / ओला", "english": "hailstone", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "गड़गड़ाहट", "hindi": "मेघगर्जन", "english": "rumble of thunder", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "झड़ी", "hindi": "लगातार बारिश की झड़ी", "english": "continuous days of non-stop monsoon rain", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "बौछार", "hindi": "तेज हवा संग बौछार", "english": "slanting wind-blown rain shower", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "पाला", "hindi": "तुषारपात / पाला", "english": "frost blanket killing vegetation", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "उमस", "hindi": "गर्मी की घुटन / उमस", "english": "muggy monsoon humidity", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "शीतल", "hindi": "ठंडी / सुखद शीतल", "english": "pleasantly cooling", "pos": "adjective", "gender": None, "category": "weather"}
]

count = 0
for item in NEW_WORDS:
    k = item["garhwali"].strip()
    if k not in existing:
        words.append(item)
        existing.add(k)
        count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Batch 6 added {count} words. Total words in dictionary: {len(words)}")
