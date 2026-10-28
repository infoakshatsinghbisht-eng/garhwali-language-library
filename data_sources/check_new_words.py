# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("garhwali/lexicon/data/words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"] for w in words}
print(f"Total existing words: {len(words)}")

candidates = [
    "हूँण", "हूँणिया", "झब्बू", "गंगवाल", "गठ्वाळ", "करचा", "भांफ",
    "थात", "थातवान", "खैकर", "सिरतान", "कमीण", "स्याणा", "सवाजी",
    "पैयाँ", "गधेरा", "कण्डार", "धुरा", "ग्वाठ", "तिबारी",
    "झंगोरा", "कोदा", "कौणी", "भट्ट", "गहत", "तोर", "रिंगाल",
    "बांज", "बुरांश", "काफल", "बिसरौण", "सिकलौण", "हौंकण", "उमटण", "घुरकण"
]

for c in candidates:
    if c in existing:
        print(f"ALREADY EXISTS: {c}")
    else:
        print(f"NEW: {c}")
