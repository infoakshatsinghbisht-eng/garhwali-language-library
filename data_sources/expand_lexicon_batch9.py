# -*- coding: utf-8 -*-
"""Batch 9: Expand to 3,100+ words."""
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

ADDITIONS = [
    {"garhwali": "तीतर", "hindi": "तीतर पक्षी", "english": "partridge bird", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "बटेर", "hindi": "बटेर पक्षी", "english": "quail bird", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "बगुला", "hindi": "बगुला पक्षी", "english": "heron / egret", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "हंस", "hindi": "हंस पक्षी", "english": "swan", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "चकवा", "hindi": "चकवा पक्षी", "english": "ruddy shelduck", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "कबूतर", "hindi": "कपोत / कबूतर", "english": "pigeon", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "चमगादड़", "hindi": "चमगादड़", "english": "bat", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "जोंक", "hindi": "जलौका / जोंक", "english": "leech", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "केंचुआ", "hindi": "केंचुआ", "english": "earthworm", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "टिड्डी", "hindi": "टिड्डी", "english": "locust / grasshopper", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "भौंरा", "hindi": "भ्रमर / भौंरा", "english": "bumblebee / black hornet", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "जुगनू", "hindi": "खद्योत / जुगनू", "english": "firefly / glowworm", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "खटमल", "hindi": "खटमल", "english": "bedbug", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "पिस्सू", "hindi": "पिस्सू", "english": "flea", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "घोंघा", "hindi": "शंबूक / घोंघा", "english": "snail", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "केकड़ा", "hindi": "कर्कट / केकड़ा", "english": "crab", "pos": "noun", "gender": "M", "category": "fauna"},

    # Culinary Verbs
    {"garhwali": "छीलण", "hindi": "छिलका उतारना", "english": "to peel skin of fruit/vegetable", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "काटण", "hindi": "काटना / टुकड़े करना", "english": "to cut / chop / slice", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "पीसण", "hindi": "सिलबट्टे पर पीसना", "english": "to grind into paste", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "छानण", "hindi": "छानना", "english": "to sieve / filter", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "सेकण", "hindi": "तवे पर सेंकना", "english": "to toast / bake on griddle", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "उबाळण", "hindi": "उबालना / खौलाना", "english": "to boil in water", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "तलण", "hindi": "कड़ाही में तलना", "english": "to deep fry in oil/ghee", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "भूनण", "hindi": "अंगारों पर भूनना", "english": "to roast over embers", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "गूंथण", "hindi": "आटा गूंथना", "english": "to knead dough", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "परोसण", "hindi": "थाली में परोसना", "english": "to serve food onto plates", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "धोण", "hindi": "प्रक्षालन करना / धोना", "english": "to wash / cleanse", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "सुखौण", "hindi": "धूप में सुखाना", "english": "to dry in sunshine", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "निचोड़ण", "hindi": "निचोड़ना", "english": "to wring / squeeze liquid out", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "लपेटण", "hindi": "लपेटना / वेष्टित करना", "english": "to wrap around / roll", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "समेटण", "hindi": "एकत्र करना / समेटना", "english": "to gather together / pack", "pos": "verb", "gender": None, "category": "cooking"},
    {"garhwali": "बांटण", "hindi": "विभाजित करना / बांटना", "english": "to distribute / apportion", "pos": "verb", "gender": None, "category": "cooking"},

    # Qualities and Spatial Terms
    {"garhwali": "भारी", "hindi": "वजनदार / भारी", "english": "heavy / weighty", "pos": "adjective", "gender": None, "category": "descriptors"},
    {"garhwali": "हलको", "hindi": "हल्का / लघुभार", "english": "lightweight", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "चौड़ो", "hindi": "विस्तृत / चौड़ा", "english": "wide / broad", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "संकरो", "hindi": "सकरा / तंग", "english": "narrow / tight passage", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "गाढ़ो", "hindi": "गाढ़ा / सघन", "english": "thick / dense consistency", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "खुरो", "hindi": "खरा / शुद्ध / सच्चा", "english": "pure / genuine / authentic", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "खोट्टो", "hindi": "खोटा / अशुद्ध / कपटी", "english": "counterfeit / impure / false", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "चंचल", "hindi": "नटखट / चंचल", "english": "playful / fickle / restless", "pos": "adjective", "gender": None, "category": "personality"},
    {"garhwali": "सुस्त", "hindi": "धीमा / सुस्त", "english": "sluggish / lethargic", "pos": "adjective", "gender": None, "category": "personality"},
    {"garhwali": "सजग", "hindi": "जागरूक / सतर्क", "english": "alert / mindful / watchful", "pos": "adjective", "gender": None, "category": "personality"},
    {"garhwali": "चौकस", "hindi": "सावधान / चौकन्ना", "english": "vigilant / cautious", "pos": "adjective", "gender": None, "category": "personality"},
    {"garhwali": "नजदीक", "hindi": "पास / निकट", "english": "near / close by", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "दूर", "hindi": "फासले पर / दूर", "english": "far / distant", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "दायें", "hindi": "दाहिनी ओर", "english": "rightward / on the right", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "बायें", "hindi": "बाईं ओर", "english": "leftward / on the left", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "आमने-सामने", "hindi": "एक दूसरे के सम्मुख", "english": "face to face / opposite each other", "pos": "adverb", "gender": None, "category": "spatial"},
    {"garhwali": "आस-पास", "hindi": "इर्द-गिर्द / आस-पास", "english": "around / in vicinity", "pos": "adverb", "gender": None, "category": "spatial"}
]

count = 0
for item in ADDITIONS:
    k = item["garhwali"].strip()
    if k not in existing:
        words.append(item)
        existing.add(k)
        count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Batch 9 added {count} words. Total words in dictionary: {len(words)}")
