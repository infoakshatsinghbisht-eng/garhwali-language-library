# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("garhwali/lexicon/data/words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"] for w in words}
print(f"Current lexicon words: {len(words)}")

candidates = [
    "बत्याण", "पछिला", "अघिला", "जुकत", "ओछाण",
    "मोरू", "खर्शू", "कैल", "गट्टा", "घाल", "तार",
    "चैती", "बाजूबंद", "मांगल", "हुरक्या", "झुमेलो", "थड़िया",
    "मोनाळ", "कलीज", "चकोर", "घुरल", "कस्तूरी",
    "तलाओं", "उपराओं", "कातील", "इजराण", "मालगुजार", "पड़त"
]

new_words = []
for c in candidates:
    if c in existing:
        print(f"ALREADY EXISTS: {c}")
    else:
        new_words.append(c)

print(f"\nTotal new verified candidates: {len(new_words)}")
print(new_words)

