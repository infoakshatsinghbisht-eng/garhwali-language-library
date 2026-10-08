# -*- coding: utf-8 -*-
import json
import os

p = os.path.join("garhwali", "lexicon", "data", "words.json")
with open(p, "r", encoding="utf-8") as f:
    words = json.load(f)

ext = {x["garhwali"] for x in words}
adds = [
    {"garhwali": "सम्धी", "hindi": "समधी", "english": "co-father-in-law", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "सम्धन", "hindi": "समधन", "english": "co-mother-in-law", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "परदादा", "hindi": "परदादा", "english": "paternal great-grandfather", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "परदादी", "hindi": "परदादी", "english": "paternal great-grandmother", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "परनाना", "hindi": "परनाना", "english": "maternal great-grandfather", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "परनानी", "hindi": "परनानी", "english": "maternal great-grandmother", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "सौतेलो", "hindi": "सौतेला भाई/पुत्र", "english": "step-relation (masc.)", "pos": "adjective", "gender": "M", "category": "kinship"},
    {"garhwali": "सौतेली", "hindi": "सौतेली बहन/पुत्री", "english": "step-relation (fem.)", "pos": "adjective", "gender": "F", "category": "kinship"},
    {"garhwali": "बिरादरी", "hindi": "बिरादरी / सजातीय समुदाय", "english": "community clan fraternity", "pos": "noun", "gender": "F", "category": "society"},
    {"garhwali": "कुटुम्ब", "hindi": "कुटुंब / परिवार", "english": "extended family household", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "खानदान", "hindi": "खानदान / घराना", "english": "pedigree / family lineage", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "वंश", "hindi": "कुल / वंश", "english": "lineage / pedigree", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "गोत्र", "hindi": "ऋषि गोत्र", "english": "ancestral clan lineage gotra", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "पुरखा", "hindi": "पूर्वज / पुरखे", "english": "ancestors / forebears", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "कुलदेवता", "hindi": "कुल के आराध्य देवता", "english": "patron ancestral family deity", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "कुलदेवी", "hindi": "कुल की देवी", "english": "patron family goddess", "pos": "noun", "gender": "F", "category": "religion"},
    {"garhwali": "ग्रामदेवता", "hindi": "गाँव के संरक्षक देवता", "english": "village guardian spirit deity", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "भूमिपाल", "hindi": "भूमि के रक्षक देवता (भूमियाल)", "english": "guardian spirit of village soil", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "चौखट", "hindi": "द्वार शाखा / चौखट", "english": "door frame / threshold", "pos": "noun", "gender": "F", "category": "architecture"},
    {"garhwali": "दहलीज", "hindi": "दहली / प्रवेश देहरी", "english": "entrance threshold step", "pos": "noun", "gender": "F", "category": "architecture"}
]

count = 0
for a in adds:
    if a["garhwali"] not in ext:
        words.append(a)
        ext.add(a["garhwali"])
        count += 1

with open(p, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {count} items. Total words now: {len(words)}")
