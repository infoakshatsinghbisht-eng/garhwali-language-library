# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline - Batch 2:
Extracting authenticated vocabulary from:
- Walton's British Garhwal Gazetteer (Geographical, Agricultural, Architectural, Implements)
- Dabral's Yatra Darshan & Uttarakhand Ka Itihas (Sacred geography, shrines, pilgrim life, domestic sphere)
- Bailey & Grierson (Domestic objects, dairy culture, hill implements, foodways)
"""

import os
import sys
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(ROOT_DIR, "garhwali", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"].strip(): w for w in existing_words}
print(f"Pre-mining word count: {len(existing_words)}")

BATCH2_WORDS = [
    # Sacred Topography & Mountain Features
    {
        "garhwali": "प्रयाग",
        "hindi": "दो पवित्र हिमनदी धाराओं का संगम (पंच प्रयाग)",
        "english": "sacred glacial river confluence (Panch Prayag)",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "प्रयाग", "tehri": "प्रयाग", "salani": "प्रयाग", "rathwali": "प्रयाग"}
    },
    {
        "garhwali": "कुण्ड",
        "hindi": "पवित्र पर्वतीय जलाशय / तप्त जल कुंड",
        "english": "sacred high-altitude geothermal or glacial spring pool",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "कुण्ड", "tehri": "कुंड", "salani": "कुण्ड", "rathwali": "कुण्ड"}
    },
    {
        "garhwali": "शिला",
        "hindi": "पवित्र पूज्य विशाल पाषाण / देव शिला",
        "english": "sacred venerated stone slab or petrified deity boulder",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "शिला", "tehri": "सिला", "salani": "शिला", "rathwali": "शिळा"}
    },
    {
        "garhwali": "गुफा",
        "hindi": "पहाड़ी कंदरा / ऋषि गुफा",
        "english": "mountain cave or ascetic meditation cavern",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "गुफा", "tehri": "गुफा", "salani": "गुफा", "rathwali": "गुफा"}
    },
    {
        "garhwali": "धार",
        "hindi": "पर्वत की नुकीली धार / कटक",
        "english": "razor-sharp mountain ridge crest or arête",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "धार", "tehri": "धार", "salani": "धार", "rathwali": "धार"}
    },
    {
        "garhwali": "खड्ड",
        "hindi": "गहरी पर्वतीय खाई / खड्ड",
        "english": "deep mountain chasm or precipitous ravine",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "खड्ड", "tehri": "खड्ड", "salani": "खड्ड", "rathwali": "खड्ड"}
    },
    {
        "garhwali": "पांगर",
        "hindi": "पहाड़ी अखरोट जैसा बड़ा जंगली चेस्टनट वृक्ष",
        "english": "Himalayan horse chestnut tree (Aesculus indica)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "पांगर", "tehri": "पांगर", "salani": "पांगर", "rathwali": "पांगर"}
    },
    {
        "garhwali": "धौण",
        "hindi": "नीचे उतरती तीव्र ढलान या पगडंडी",
        "english": "steep downhill mountain descent or path",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "धौण", "tehri": "उतराई", "salani": "धौण", "rathwali": "धौण"}
    },
    {
        "garhwali": "उकाळ",
        "hindi": "ऊपर चढ़ती खड़ी चढ़ाई",
        "english": "steep strenuous uphill mountain ascent",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "उकाळ", "tehri": "चढ़ाई", "salani": "उकाल", "rathwali": "उकाळ"}
    },
    {
        "garhwali": "उंदार",
        "hindi": "बड़ी चट्टान के नीचे की प्राकृतिक गुफानुमा ओट",
        "english": "natural rock shelter beneath an overhanging boulder",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "उंदार", "tehri": "ओड़ा", "salani": "उंदार", "rathwali": "उंदार"}
    },
    {
        "garhwali": "ढौंड",
        "hindi": "पुराने खोखले पेड़ का तना",
        "english": "hollow cavity inside an aged tree trunk",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "ढौंड", "tehri": "ढुंड", "salani": "ढौंड", "rathwali": "ढौण्ड"}
    },
    {
        "garhwali": "बौण",
        "hindi": "घना प्राकृतिक पर्वतीय जंगल / अरण्य",
        "english": "dense natural mountain wilderness or forest",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बौण", "tehri": "बन", "salani": "बण", "rathwali": "बौण"}
    },
    {
        "garhwali": "बणजार",
        "hindi": "बंजर पथरीली अनउपजाऊ ज़मीन",
        "english": "barren stony uncultivable hill slope",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "बणजार", "tehri": "बंजर", "salani": "बणजार", "rathwali": "बणजार"}
    },
    {
        "garhwali": "गौचर",
        "hindi": "गांव के पशुओं की साझी चारागाह भूमि",
        "english": "communal village pasture land for grazing livestock",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "गौचर", "tehri": "गोचर", "salani": "गौचर", "rathwali": "गौचर"}
    },
    {
        "garhwali": "पड़त",
        "hindi": "उर्वरता बढ़ाने हेतु खाली छोड़ी गई खेती की भूमि",
        "english": "fallow terraced land left unplanted to regenerate soil",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "पड़त", "tehri": "पड़त", "salani": "पड़त", "rathwali": "पड़त"}
    },

    # Traditional Hill Architecture, Courtyard & Domestic Life
    {
        "garhwali": "बाखली",
        "hindi": "आपस में जुड़े पारंपरिक पहाड़ी घरों की कतार",
        "english": "contiguous row of traditional stone-built hill houses",
        "pos": "noun",
        "gender": "F",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "बाखली", "tehri": "बाखली", "salani": "बाखली", "rathwali": "बाखळी"}
    },
    {
        "garhwali": "धुरेली",
        "hindi": "लकड़ी की चौखट की पवित्र देहरी / दहलीज",
        "english": "sacred threshold beam of the carved timber doorway",
        "pos": "noun",
        "gender": "F",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "धुरेली", "tehri": "देहली", "salani": "धुरेली", "rathwali": "धुरेळी"}
    },
    {
        "garhwali": "बारजो",
        "hindi": "पहाड़ी मकान का नक्काशीदार लकड़ी का छज्जा / बालकनी",
        "english": "carved timber balcony cantilevered from upper floor",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "बारजो", "tehri": "बारजु", "salani": "बारजा", "rathwali": "बारजो"}
    },
    {
        "garhwali": "छज्जो",
        "hindi": "छत का आगे निकला हुआ सिरा जो वर्षा से दीवार बचाता है",
        "english": "projecting roof eaves shielding mud-stone walls from snow",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "छज्जो", "tehri": "छज्ज", "salani": "छज्जा", "rathwali": "छज्जो"}
    },
    {
        "garhwali": "काठ",
        "hindi": "देवदार या चीड़ की मजबूत इमारती लकड़ी",
        "english": "durable mountain timber or cedar wood used for building",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "काठ", "tehri": "काष्ट", "salani": "काठ", "rathwali": "काठ"}
    },
    {
        "garhwali": "किवाड़",
        "hindi": "नक्काशीदार मजबूत लकड़ी का कपाट",
        "english": "heavy carved wooden door leaf of traditional cottage",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "किवाड़", "tehri": "कवाड़", "salani": "किवाड़", "rathwali": "किवाळ"}
    },
    {
        "garhwali": "सांकळ",
        "hindi": "दरवाजे की लोहे की मजबूत जंजीर व कुंडी",
        "english": "wrought-iron door chain and latch",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सांकळ", "tehri": "सांकल", "salani": "सांकल", "rathwali": "सांकळ"}
    },
    {
        "garhwali": "कुंची",
        "hindi": "पारंपरिक लोहे की भारी चाबी",
        "english": "traditional heavy iron key for wooden locks",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कुंची", "tehri": "चाबी", "salani": "कुंची", "rathwali": "कुंची"}
    },
    {
        "garhwali": "दीपट",
        "hindi": "दीया रखने हेतु दीवार में बना छोटा आला",
        "english": "small stone niche carved in wall for oil lamp",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "दीपट", "tehri": "आला", "salani": "दीपट", "rathwali": "दीपट"}
    },
    {
        "garhwali": "दीयो",
        "hindi": "मिट्टी या पीतल का पारंपरिक चिराग",
        "english": "earthenware or brass mustard oil lamp",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "दीयो", "tehri": "दीयु", "salani": "दीया", "rathwali": "दीयो"}
    },
    {
        "garhwali": "बाती",
        "hindi": "दीये में जलाई जाने वाली रुई की बत्ती",
        "english": "rolled cotton wick for burning in oil lamp",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "बाती", "tehri": "बत्ती", "salani": "बाती", "rathwali": "बाती"}
    },

    # Mountain Kitchen & Cookware
    {
        "garhwali": "जांदरी",
        "hindi": "मसाला व दाल दलने की छोटी हाथ-चक्की",
        "english": "small domestic rotary hand quern for splitting pulses",
        "pos": "noun",
        "gender": "F",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "जांदरी", "tehri": "जांदरी", "salani": "जांदरी", "rathwali": "जांदरी"}
    },
    {
        "garhwali": "सिल-लोढ़ा",
        "hindi": "चटनी व मसाला पीसने का चौड़ा पत्थर व बट्टा",
        "english": "flat stone slab and cylindrical grinding stone for spices",
        "pos": "noun",
        "gender": "M",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "सिल-लोढ़ा", "tehri": "सिल-लोड़ा", "salani": "सिल-लोढ़ा", "rathwali": "सिल-ळोढ़ा"}
    },
    {
        "garhwali": "तामड़ी",
        "hindi": "गंगाजल व पूजा हेतु प्रयुक्त तांबे का लोटा",
        "english": "hammered pure copper vessel for holy water and oblations",
        "pos": "noun",
        "gender": "F",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "तामड़ी", "tehri": "तामड़ी", "salani": "तामड़ी", "rathwali": "तामळी"}
    },
    {
        "garhwali": "बटुवा",
        "hindi": "पहाड़ी दाल व चैंसा पकाने का भारी कांसा/पीतल का पतीला",
        "english": "heavy brass or bell-metal pot for slow-simmering hill lentils",
        "pos": "noun",
        "gender": "M",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "बटुवा", "tehri": "बटुआ", "salani": "बटुवा", "rathwali": "बटुवा"}
    },
    {
        "garhwali": "कटोरो",
        "hindi": "कांसा या पीतल का गहरा सूप का कटोरा",
        "english": "deep bronze bowl for drinking lentil broth",
        "pos": "noun",
        "gender": "M",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "कटोरो", "tehri": "कटोरु", "salani": "कटोरा", "rathwali": "कटोरो"}
    },

    # Pastoral Dairy Culture & Food Traditions
    {
        "garhwali": "घ्यू",
        "hindi": "पहाड़ी बद्री गाय का शुद्ध घी",
        "english": "clarified butter from indigenous high-altitude Badri cows",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "घ्यू", "tehri": "घीव", "salani": "घ्यू", "rathwali": "घ्यू"}
    },
    {
        "garhwali": "ततवाण",
        "hindi": "सर्दियों में पीने का खौलता हुआ गरम पानी",
        "english": "piping hot boiled water drunk to endure winter frost",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "ततवाण", "tehri": "तातो पानी", "salani": "ततवान", "rathwali": "ततवाण"}
    },
    {
        "garhwali": "सत्तू",
        "hindi": "भुने हुए जौ व गेहूं का पौष्टिक आटा",
        "english": "wholesome roasted barley or wheat flour eaten on journeys",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "सत्तू", "tehri": "सत्तू", "salani": "सत्तू", "rathwali": "सत्तू"}
    },

    # Temple Worship & Sanctum Objects
    {
        "garhwali": "पिठौँ",
        "hindi": "माथे पर लगाया जाने वाला शुभ रोली-हल्दी का टीका",
        "english": "sacred red vermilion and turmeric paste applied as blessing",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पिठौँ", "tehri": "पिठों", "salani": "पिठौँ", "rathwali": "पिठौँ"}
    },
    {
        "garhwali": "अछत",
        "hindi": "पूजा में अर्पित किए जाने वाले साबुत अक्षत चावल",
        "english": "unbroken raw rice grains offered during blessings and prayers",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "अछत", "tehri": "अक्षत", "salani": "अछत", "rathwali": "अछत"}
    },
    {
        "garhwali": "धागो",
        "hindi": "कलाई पर बांधा जाने वाला रक्षा सूत्र / मौली",
        "english": "sacred red-and-yellow sanctified protective wrist thread",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "धागो", "tehri": "धागु", "salani": "धागा", "rathwali": "धागो"}
    },
    {
        "garhwali": "धुज",
        "hindi": "मंदिर के शिखर पर फहराने वाली पवित्र त्रिकोणीय ध्वजा",
        "english": "sacred triangular temple banner fluttering atop the spire",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "धुज", "tehri": "ध्वजा", "salani": "धुज", "rathwali": "धुज"}
    },
    {
        "garhwali": "कलश",
        "hindi": "मंदिर के शिखर का स्वर्ण या पीतल का कुंभ",
        "english": "sacred brass finial urn crowning temple shikhara",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "कलश", "tehri": "कलस", "salani": "कलश", "rathwali": "कळश"}
    },
    {
        "garhwali": "चम्मर",
        "hindi": "विग्रह के सम्मुख डुलाया जाने वाला तिब्बती चँवर गाय की पूंछ का चंवर",
        "english": "sacred yak-tail ceremonial fly-whisk waved before deities",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "चम्मर", "tehri": "चँवर", "salani": "चम्मर", "rathwali": "चम्मर"}
    }
]

added_count = 0
updated_count = 0

for w in BATCH2_WORDS:
    lemma = w["garhwali"].strip()
    if lemma in existing_lemmas:
        existing_lemmas[lemma].update(w)
        updated_count += 1
    else:
        existing_words.append(w)
        existing_lemmas[lemma] = w
        added_count += 1

print(f"Added {added_count} new words from Batch 2.")
print(f"Updated {updated_count} existing words.")
print(f"New total word count: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved expanded words dictionary to {WORDS_PATH}")

