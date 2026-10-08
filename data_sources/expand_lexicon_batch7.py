# -*- coding: utf-8 -*-
"""
Batch 7: Numbers, Ordinals, Fractions, Colors, Textures, and Landscape Morphology.
Reaches 3,050+ words in garhwali/lexicon/data/words.json.
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

BATCH_WORDS = [
    # Numbers
    {"garhwali": "इक्कीस", "hindi": "इक्कीस (२१)", "english": "twenty-one (21)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "बाईस", "hindi": "बाईस (२२)", "english": "twenty-two (22)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "तेईस", "hindi": "तेईस (२३)", "english": "twenty-three (23)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "चौबीस", "hindi": "चौबीस (२४)", "english": "twenty-four (24)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "छब्बीस", "hindi": "छब्बीस (२६)", "english": "twenty-six (26)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "सत्ताईस", "hindi": "सत्ताईस (२७)", "english": "twenty-seven (27)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "अट्ठाईस", "hindi": "अट्ठाईस (२८)", "english": "twenty-eight (28)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "उनतीस", "hindi": "उनतीस (२९)", "english": "twenty-nine (29)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "इकतीस", "hindi": "इकतीस (३१)", "english": "thirty-one (31)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "बत्तीस", "hindi": "बत्तीस (३२)", "english": "thirty-two (32)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "तैंतीस", "hindi": "तैंतीस (३३)", "english": "thirty-three (33)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "चौंतीस", "hindi": "चौंतीस (३४)", "english": "thirty-four (34)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "पैंतीस", "hindi": "पैंतीस (३५)", "english": "thirty-five (35)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "छत्तीस", "hindi": "छत्तीस (३६)", "english": "thirty-six (36)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "सैंतीस", "hindi": "सैंतीस (३७)", "english": "thirty-seven (37)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "अड़तीस", "hindi": "अड़तीस (३८)", "english": "thirty-eight (38)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "उनतालीस", "hindi": "उनतालीस (३९)", "english": "thirty-nine (39)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "इकतालीस", "hindi": "इकतालीस (४१)", "english": "forty-one (41)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "बयालीस", "hindi": "बयालीस (४२)", "english": "forty-two (42)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "तैंतालीस", "hindi": "तैंतालीस (४३)", "english": "forty-three (43)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "चवालीस", "hindi": "चवालीस (४४)", "english": "forty-four (44)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "पैंतालीस", "hindi": "पैंतालीस (४५)", "english": "forty-five (45)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "छियालीस", "hindi": "छियालीस (४६)", "english": "forty-six (46)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "सैंतालीस", "hindi": "सैंतालीस (४७)", "english": "forty-seven (47)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "अड़तालीस", "hindi": "अड़तालीस (४८)", "english": "forty-eight (48)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "उनचास", "hindi": "उनचास (४९)", "english": "forty-nine (49)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "पचास", "hindi": "पचास (५०)", "english": "fifty (50)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "साठ", "hindi": "साठ (६०)", "english": "sixty (60)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "सत्तर", "hindi": "सत्तर (७०)", "english": "seventy (70)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "अस्सी", "hindi": "अस्सी (८०)", "english": "eighty (80)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "नब्बे", "hindi": "नब्बे (९०)", "english": "ninety (90)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "हजार", "hindi": "हजार (१०००)", "english": "thousand (1000)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "लाख", "hindi": "एक लाख", "english": "one hundred thousand (lakh)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "करोड़", "hindi": "एक करोड़", "english": "ten million (crore)", "pos": "numeral", "gender": None, "category": "quantity"},

    # Ordinals
    {"garhwali": "पहिलो", "hindi": "प्रथम / पहला", "english": "first (1st)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "पहिलि", "hindi": "पहली (स्त्री.)", "english": "first (fem.)", "pos": "adjective", "gender": "F", "category": "quantity"},
    {"garhwali": "दूसरो", "hindi": "द्वितीय / दूसरा", "english": "second (2nd)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "तीसरो", "hindi": "तृतीय / तीसरा", "english": "third (3rd)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "चौथो", "hindi": "चतुर्थ / चौथा", "english": "fourth (4th)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "पांचवों", "hindi": "पंचम / पांचवां", "english": "fifth (5th)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "छठवों", "hindi": "षष्ठ / छठा", "english": "sixth (6th)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "सातवों", "hindi": "सप्तम / सातवां", "english": "seventh (7th)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "आठवों", "hindi": "अष्टम / आठवां", "english": "eighth (8th)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "नौवों", "hindi": "नवम / नौवां", "english": "ninth (9th)", "pos": "adjective", "gender": "M", "category": "quantity"},
    {"garhwali": "दसवों", "hindi": "दशम / दसवां", "english": "tenth (10th)", "pos": "adjective", "gender": "M", "category": "quantity"},

    # Fractions & Proportions
    {"garhwali": "पौणा", "hindi": "पौने (०.७५)", "english": "three-quarters (0.75)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "सवा", "hindi": "सवा (१.२५)", "english": "one and a quarter (1.25)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "डेढ़", "hindi": "डेढ़ (१.५)", "english": "one and a half (1.5)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "अढाई", "hindi": "ढाई (२.५)", "english": "two and a half (2.5)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "आधा", "hindi": "अर्ध / आधा (०.५)", "english": "half (0.5)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "तिहाई", "hindi": "एक तिहाई (१/३)", "english": "one-third (1/3)", "pos": "numeral", "gender": None, "category": "quantity"},
    {"garhwali": "चौथाई", "hindi": "एक चौथाई (१/४)", "english": "one-quarter (1/4)", "pos": "numeral", "gender": None, "category": "quantity"},

    # Colors and Appearance
    {"garhwali": "चटक", "hindi": "चमकीला / चटक", "english": "vivid / brilliant color", "pos": "adjective", "gender": None, "category": "descriptors"},
    {"garhwali": "मटमैलो", "hindi": "मिट्टी के रंग का / धूसर", "english": "earthy mud-colored / dusty grey", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "गुलाबी", "hindi": "गुलाबी रंग", "english": "pink / roseate", "pos": "adjective", "gender": None, "category": "descriptors"},
    {"garhwali": "बैंगनी", "hindi": "बैंगनी रंग", "english": "violet / purple", "pos": "adjective", "gender": None, "category": "descriptors"},
    {"garhwali": "सलेटी", "hindi": "स्लेटी / पाषाण वर्ण", "english": "slate grey", "pos": "adjective", "gender": None, "category": "descriptors"},
    {"garhwali": "गेरुआ", "hindi": "गेरुआ / भगवा", "english": "ochre / saffron ascetic color", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "सुनहलो", "hindi": "स्वर्णिम / सुनहरा", "english": "golden", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "रूपहलो", "hindi": "रुपहला / चांदी जैसा", "english": "silvery", "pos": "adjective", "gender": "M", "category": "descriptors"},

    # Tastes, Sensations & Textures
    {"garhwali": "अलूणो", "hindi": "बिना नमक का / फीका", "english": "salt-less / bland", "pos": "adjective", "gender": "M", "category": "taste"},
    {"garhwali": "सड़ांध", "hindi": "दुर्गंध / बदबू", "english": "foul stench / decay odor", "pos": "noun", "gender": "F", "category": "sense"},
    {"garhwali": "सुवास", "hindi": "सुगंध / महक", "english": "sweet fragrance / aroma", "pos": "noun", "gender": "F", "category": "sense"},
    {"garhwali": "खुरदुरा", "hindi": "रूखा / खुरदुरा", "english": "rough / abrasive surface", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "लिजलिजो", "hindi": "लसलसा / चिपचिपा", "english": "slimy / viscous", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "चिकणो", "hindi": "मुलायम / चिकना", "english": "smooth / slick / polished", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "भुरभुरा", "hindi": "दानेदार / भुरभुरा", "english": "crumbly / friable", "pos": "adjective", "gender": "M", "category": "descriptors"},

    # Landscape & Mountain Terrain Topography
    {"garhwali": "ठाड़ो", "hindi": "सीधी चढ़ाई वाला", "english": "steep uphill gradient", "pos": "adjective", "gender": "M", "category": "spatial"},
    {"garhwali": "ऊंधार", "hindi": "तीव्र ढलान / उतराई", "english": "steep downward descent", "pos": "noun", "gender": "M", "category": "spatial"},
    {"garhwali": "सीम", "hindi": "ग्राम सीमा / सरहद", "english": "village cadastral boundary line", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "मेढ़", "hindi": "खेत की मेड़ / डोल", "english": "raised earthen terrace boundary", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "डोल", "hindi": "खेतों के बीच की संकरी मेड़", "english": "narrow terrace dividing ridge", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "आगो-पाछो", "hindi": "आगे-पीछे / चारों ओर", "english": "ahead and behind / all around", "pos": "adverb", "gender": None, "category": "spatial"},
    {"garhwali": "ओर-छोर", "hindi": "आर-पार / दोनों किनारे", "english": "both ends / across boundaries", "pos": "noun", "gender": "M", "category": "spatial"}
]

count = 0
for item in BATCH_WORDS:
    k = item["garhwali"].strip()
    if k not in existing:
        words.append(item)
        existing.add(k)
        count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Batch 7 added {count} words. Total words in dictionary: {len(words)}")
