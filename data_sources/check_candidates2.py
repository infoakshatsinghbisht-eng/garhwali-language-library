# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("garhwali/lexicon/data/words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"] for w in words}

more_candidates = [
    "हूँण", "हूँणिया", "झब्बू", "गंगवाल", "गठ्वाळ", "करचा", "भांफ",
    "थात", "खैकर", "स्याणा", "सवाजी", "पैयाँ", "कण्डार", "ग्वाठ",
    "बिसरौण", "सिकलौण", "हौंकण", "उमटण", "घुरकण",
    "पश्म", "खलचा", "करबन्दी", "डाँफ", "लंगूर", "जुवाळ", "पाता", "गुजी",
    "गाँवठ", "खसमिया", "मुआफी", "कूंट", "बिसाती", "पैमाइस", "पत्तीदार", "हकदार",
    "खरास", "काण्डी", "थला", "नागफनी", "छत्तर", "चैंणा", "गुल",
    "अगास", "उधौण", "किकरण", "चिटकण", "निफूट", "पछ्याण", "बिहाण", "रुंगण", "लिलौण", "हिकौण"
]

new_words = []
for c in more_candidates:
    if c not in existing:
        new_words.append(c)
    else:
        print(f"Exists: {c}")

print(f"\nTotal new words found: {len(new_words)}")
print(new_words)
