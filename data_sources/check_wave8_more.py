# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("garhwali/lexicon/data/words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"] for w in words}

more_candidates = [
    "बत्याण", "पछिला", "अघिला", "जुकत", "ओछाण",
    "मोरू", "खर्शू", "कैल", "गट्टा", "घाल", "तार",
    "चैती", "हुरक्या", "कलीज", "चकोर", "तलाओं", "कातील", "इजराण",
    "घुघुती", "लस्या", "डालो", "गाडर", "छानी",
    "बुज्याण", "चितकण", "तपक्क", "झमक्क", "कनपट",
    "पिंडालू", "गेठी", "तरूड़", "झिंझोड़ण", "भकोसण", "सरकण", "खुरपी",
    "झोल", "पल्लो", "वल्लो", "गौंत"
]

new_words = []
for c in more_candidates:
    if c not in existing:
        new_words.append(c)
    else:
        print(f"Exists: {c}")

print(f"\nTotal new verified candidates: {len(new_words)}")
print(new_words)
