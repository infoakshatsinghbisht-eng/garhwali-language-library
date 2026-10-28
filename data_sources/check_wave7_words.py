# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("garhwali/lexicon/data/words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"] for w in words}
print(f"Existing lemmas: {len(words)}")

candidates = [
    "खरक", "हिमताल", "हिमानी", "भित्ती", "बौण", "झुला",
    "बुझौण", "सुणौण", "दबकण", "टपकण", "छिना",
    "डंडोत", "सदाव्रत", "शंखनाद", "पंडा", "बदरीकाश्रम",
    "कुदाळ", "दाँतुळी", "सूपी", "कनस्तर", "गौचर",
    "कन्दरा", "प्रपात", "गर्त", "पाषाण",
    "नैणा", "दियौण", "घिरौण", "समेत",
    "उखण", "उज्याळ", "अन्धेर", "ओत", "बगौण", "खितौण"
]

new_words = []
for c in candidates:
    if c in existing:
        print(f"ALREADY EXISTS: {c}")
    else:
        new_words.append(c)

print(f"\nTotal new verified candidates: {len(new_words)}")
print(new_words)

