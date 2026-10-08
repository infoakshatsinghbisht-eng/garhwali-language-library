# -*- coding: utf-8 -*-
"""
Batch 8: Traditional Kitchen Vessels, Architecture, Agrarian Operations, Interjections.
Brings the dictionary to over 3,100 words.
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
    # Traditional Metal & Wooden Kitchen Vessels
    {"garhwali": "भड्डू", "hindi": "भड्डू (दाल पकाने का भारी कांसे/पीतल का पात्र)", "english": "heavy brass-bell metal pot for slow-cooking mountain dals", "pos": "noun", "gender": "M", "category": "crockery"},
    {"garhwali": "गागर", "hindi": "पानी भरने की बड़ी गागर / गगरी", "english": "large brass or copper water jar", "pos": "noun", "gender": "F", "category": "crockery"},
    {"garhwali": "तौली", "hindi": "तौली (पीतल की छोटी पतीली)", "english": "small brass cooking vessel", "pos": "noun", "gender": "F", "category": "crockery"},
    {"garhwali": "बटलोई", "hindi": "संकरे मुंह का पीतल का भात पकाने का पात्र", "english": "narrow-necked brass rice cooking pot", "pos": "noun", "gender": "F", "category": "crockery"},
    {"garhwali": "कलछी", "hindi": "कलछी (दाल-सब्जी परोसने की)", "english": "long-handled serving ladle", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "मथणी", "hindi": "मथानी (दही बिलोने की लकड़ी की रई)", "english": "wooden hand-churn for separating butter from curd", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "ठेकी", "hindi": "ठेकी (दही-मक्खन रखने का लकड़ी का पारंपरिक पात्र)", "english": "traditional hollowed-wood vessel for storing curd and butter", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "नेती", "hindi": "नेती (मथानी घुमाने की रस्सी)", "english": "churning cord wrapped around wooden churn", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "कनस्तर", "hindi": "तेल-घी का टीन का पीपा", "english": "tin storage canister", "pos": "noun", "gender": "M", "category": "kitchen"},
    {"garhwali": "डब्बा", "hindi": "डिब्बा / पेटी", "english": "small box / container", "pos": "noun", "gender": "M", "category": "kitchen"},
    {"garhwali": "हंडिया", "hindi": "मिट्टी की हांडी", "english": "earthen clay stewing pot", "pos": "noun", "gender": "F", "category": "kitchen"},

    # Architecture & Homestead Anatomy
    {"garhwali": "पौळी", "hindi": "प्रवेश द्वार का मुख्य बरामदा / ड्योढ़ी", "english": "traditional entrance portico of stone house", "pos": "noun", "gender": "F", "category": "architecture"},
    {"garhwali": "खम्भा", "hindi": "लकड़ी का नक्काशीदार खंभा / थंभ", "english": "carved wooden pillar", "pos": "noun", "gender": "M", "category": "architecture"},
    {"garhwali": "छज्जा", "hindi": "छज्जा (छत का आगे निकला भाग)", "english": "projecting roof eave", "pos": "noun", "gender": "M", "category": "architecture"},
    {"garhwali": "धारो", "hindi": "पानी की टोंटी / प्राकृतिक जलधारा", "english": "stone water spout conduit", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "बगड़", "hindi": "नदी तट का कंकड़-पत्थर वाला मैदान", "english": "pebbled boulder floodplain bank of river", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "सेरा", "hindi": "नदी किनारे का उपजाऊ सिंचित समतल खेत", "english": "richly irrigated alluvial riverside valley terrace", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "पांणा", "hindi": "सीढ़ीदार खेत की एक पट्टी", "english": "single strip of contoured terraced field", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "क्यारी", "hindi": "सब्जी की छोटी क्यारी", "english": "small square vegetable garden bed", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "बाड़ी", "hindi": "घर के पीछे का शाक-वाटिका / बाड़ा", "english": "homestead kitchen garden / fenced orchard", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "बाड़", "hindi": "घेरा / बाड़", "english": "protective hedge fence around crops", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "मचान", "hindi": "फसल की रखवाली का ऊंचा मंच", "english": "elevated wooden watchtower platform to guard crops", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "खेत-खलिहान", "hindi": "कृषि भूमि एवं फसल का आंगन", "english": "fields and threshing grounds", "pos": "noun", "gender": "M", "category": "agriculture"},

    # Seasonal Agricultural Operations
    {"garhwali": "रूणि", "hindi": "पहली निराई (फसल से खरपतवार निकालना)", "english": "first weeding cycle in crops", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "दौणि", "hindi": "दूसरी निराई-गुड़ाई", "english": "second weeding and hoeing cycle", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "असोजि", "hindi": "आश्विन मास की खरीफ कटाई", "english": "autumn kharif harvest season", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "चैति", "hindi": "चैत्र मास की रबी कटाई / वसंत बुवाई", "english": "spring rabi harvesting and sowing season", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "बीज", "hindi": "अनाज का दाना / बीज", "english": "seed / grain seed", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "खाद", "hindi": "गोबर की जैविक खाद", "english": "organic farmyard cow-dung compost manure", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "फसल", "hindi": "खेती की उपज / फसल", "english": "crop yield / harvest", "pos": "noun", "gender": "F", "category": "agriculture"},

    # Interjections & Conversational Expressions
    {"garhwali": "वाह-वाह", "hindi": "वाह-वाह / अति सुंदर", "english": "splendid! / bravo!", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "शाबाश", "hindi": "बहुत बढ़िया / शाबाश", "english": "well done! / kudos!", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "हाय-दइ", "hindi": "हाय रे विधाता / हाय राम", "english": "alas! / woe is me!", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "अरे-रे", "hindi": "अरे रे (दुख या आश्चर्य का भाव)", "english": "oh dear! / alas!", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "धिक्कार", "hindi": "लानत / धिक्कार", "english": "shame on you! / fie!", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "राम-राम", "hindi": "पारंपरिक अभिवादन / नमस्कार", "english": "traditional hill greeting / salutation", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "पैलाग", "hindi": "पैर छूकर प्रणाम (पैलाग)", "english": "traditional respectful foot-touching greeting", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "जी रया", "hindi": "दीर्घायु होओ (बुजुर्गों का आशीर्वाद)", "english": "may you live long! (elders blessing)", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "खुश रया", "hindi": "प्रसन्न रहो", "english": "stay blessed and happy!", "pos": "interjection", "gender": None, "category": "conversation"},
    {"garhwali": "जय बदरी", "hindi": "भगवान बदरीनाथ की जय", "english": "victory to Lord Badrinath!", "pos": "interjection", "gender": None, "category": "religion"},
    {"garhwali": "जय केदार", "hindi": "भगवान केदारनाथ की जय", "english": "victory to Lord Kedarnath!", "pos": "interjection", "gender": None, "category": "religion"}
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

print(f"Batch 8 added {count} words. Total words in dictionary: {len(words)}")
