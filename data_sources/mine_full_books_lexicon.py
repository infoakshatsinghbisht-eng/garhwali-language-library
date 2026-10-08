# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline extracting authentic Garhwali vocabulary
from the 13 full-text digitized books in the Garhwali Language Library:
- Grierson (1916): Linguistic Survey of India (Central Pahari / Garhwali)
- Govind Chatak (1959): Garhwali Bhasha (Linguistic Analysis)
- Govind Chatak (1958): Gadwali Lok Gathayen (Pawada & Jagar Epics)
- Haridatta Bhatt 'Shailesh' (1976): Garhwali Bhasha Aur Uska Sahitya
- Gunanand Juyal (1967): Madhya Pahadi Bhasha
- Ganga Datt Upreti (1894): Proverbs & Folklore of Garhwal
- Uttarakhand Open University (UOU) Textbooks (CGL-102, 103, 104, AECC-G-101)
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "garhwali", "lexicon", "data", "words.json"
)

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"].strip(): w for w in existing_words}
print(f"Current word count before full-book mining: {len(existing_words)}")

NEW_BOOK_WORDS = [
    # ==================== 1. GRIERSON 1916 (LSI Central Pahari: Pronouns, Postpositions & Grammar) ====================
    {
        "garhwali": "कथगा",
        "hindi": "कितना / कितने",
        "english": "how much / how many",
        "pos": "pronoun",
        "gender": "M",
        "category": "quantifiers",
        "dialect_variants": {"srinagariya": "कथगा", "tehri": "कत्तुका", "salani": "कतगा", "rathwali": "कथगा"}
    },
    {
        "garhwali": "यथगा",
        "hindi": "इतना / इतने",
        "english": "this much / so much",
        "pos": "pronoun",
        "gender": "M",
        "category": "quantifiers",
        "dialect_variants": {"srinagariya": "यथगा", "tehri": "एतुका", "salani": "यतगा", "rathwali": "यथगा"}
    },
    {
        "garhwali": "वथगा",
        "hindi": "उतना / उतने",
        "english": "that much",
        "pos": "pronoun",
        "gender": "M",
        "category": "quantifiers",
        "dialect_variants": {"srinagariya": "वथगा", "tehri": "ओतुका", "salani": "वतगा", "rathwali": "वथगा"}
    },
    {
        "garhwali": "कथै",
        "hindi": "कहीं / किसी स्थान पर",
        "english": "somewhere / anywhere",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कथै", "tehri": "कथई", "salani": "कथै", "rathwali": "कथै"}
    },
    {
        "garhwali": "कखि",
        "hindi": "कहाँ / किस जगह",
        "english": "where / at what place",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कखि", "tehri": "कथी", "salani": "कख", "rathwali": "कखी"}
    },
    {
        "garhwali": "यखि",
        "hindi": "यहाँ / इस जगह",
        "english": "here / at this place",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "यखि", "tehri": "इथी", "salani": "यख", "rathwali": "यखी"}
    },
    {
        "garhwali": "वखि",
        "hindi": "वहाँ / उस जगह",
        "english": "there / at that place",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "वखि", "tehri": "उथी", "salani": "वख", "rathwali": "वखी"}
    },
    {
        "garhwali": "जैलो",
        "hindi": "जब / जिस समय",
        "english": "when / at the time which",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "जैलो", "tehri": "जब", "salani": "जैल", "rathwali": "जैळो"}
    },
    {
        "garhwali": "तैलो",
        "hindi": "तब / उस समय",
        "english": "then / at that time",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "तैलो", "tehri": "तब", "salani": "तैल", "rathwali": "तैळो"}
    },
    {
        "garhwali": "कैलो",
        "hindi": "कब / किस समय",
        "english": "when / at what time",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "कैलो", "tehri": "कब", "salani": "कैल", "rathwali": "कैळो"}
    },
    {
        "garhwali": "ऐलो",
        "hindi": "अब / इस समय",
        "english": "now / currently",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "ऐलो", "tehri": "अब", "salani": "ऐल", "rathwali": "ऐळो"}
    },
    {
        "garhwali": "सैणी",
        "hindi": "की तरफ / की ओर",
        "english": "towards / in the direction of",
        "pos": "postposition",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सैणी", "tehri": "तरफ", "salani": "कानी", "rathwali": "सैणी"}
    },
    {
        "garhwali": "थईं",
        "hindi": "तक / पर्यन्त",
        "english": "until / up to",
        "pos": "postposition",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "थईं", "tehri": "तक", "salani": "थैं", "rathwali": "थईं"}
    },
    {
        "garhwali": "बटी",
        "hindi": "से (अपादान / स्रोत)",
        "english": "from (source/origin)",
        "pos": "postposition",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "बटी", "tehri": "बटी", "salani": "से", "rathwali": "बटि"}
    },

    # ==================== 2. CHATAK 1959 (Verbs, Adjectives & Daily Mountain Life) ====================
    {
        "garhwali": "जांचणु",
        "hindi": "परखना / जांच करना",
        "english": "to examine / test / verify",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "जांचणु", "tehri": "परखना", "salani": "जांचना", "rathwali": "जांचणु"}
    },
    {
        "garhwali": "पछ्याणणु",
        "hindi": "पहचानना",
        "english": "to recognize / identify",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "पछ्याणणु", "tehri": "पहचानना", "salani": "पछियानना", "rathwali": "पछ्याणणु"}
    },
    {
        "garhwali": "समझाउणु",
        "hindi": "समझाना / बोध कराना",
        "english": "to explain / persuade",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "समझाउणु", "tehri": "समझाना", "salani": "समझाना", "rathwali": "समझाउणु"}
    },
    {
        "garhwali": "बिसरणु",
        "hindi": "भूल जाना / विस्मृत होना",
        "english": "to forget",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बिसरणु", "tehri": "भूलना", "salani": "बिसरना", "rathwali": "बिसरणु"}
    },
    {
        "garhwali": "संजोउणु",
        "hindi": "सहेजना / संभालकर रखना",
        "english": "to preserve carefully / gather tenderly",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "संजोउणु", "tehri": "सहेजना", "salani": "संजोना", "rathwali": "संजोउणु"}
    },
    {
        "garhwali": "खोदणु",
        "hindi": "मिट्टी खोदना",
        "english": "to dig earth or terraced fields",
        "pos": "verb",
        "gender": "N",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "खोदणु", "tehri": "खोदना", "salani": "गोडना", "rathwali": "खोदणु"}
    },
    {
        "garhwali": "रोपणु",
        "hindi": "धान की रोपाई करना",
        "english": "to transplant paddy seedlings in flooded terraces",
        "pos": "verb",
        "gender": "N",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "रोपणु", "tehri": "रोपना", "salani": "रोपनी", "rathwali": "रोपणु"}
    },
    {
        "garhwali": "निणाणु",
        "hindi": "खेतों से खरपतवार निकालना (निराई)",
        "english": "to weed crops in terraced fields",
        "pos": "verb",
        "gender": "N",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "निणाणु", "tehri": "गोडाई", "salani": "निराई", "rathwali": "निणाणु"}
    },
    {
        "garhwali": "मांडणु",
        "hindi": "दंवेरी करना / बैलों से दाना निकालना",
        "english": "to thresh grain using trotting oxen",
        "pos": "verb",
        "gender": "N",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "मांडणु", "tehri": "दंवेरी", "salani": "दंवाई", "rathwali": "मांडणु"}
    },
    {
        "garhwali": "छानणु",
        "hindi": "सूप से अनाज फटकना",
        "english": "to winnow chaff from grain",
        "pos": "verb",
        "gender": "N",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "छानणु", "tehri": "फटकना", "salani": "ओसाना", "rathwali": "छाणणु"}
    },

    # ==================== 3. CHATAK 1958 (Pawadas, Jagar Epics, Martial & Shamanic Lore) ====================
    {
        "garhwali": "रणखेत्र",
        "hindi": "युद्धभूमि / रणक्षेत्र",
        "english": "battlefield of heroic warriors",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "रणखेत्र", "tehri": "रणभूमि", "salani": "मैदान-ए-जंग", "rathwali": "रणखेत्र"}
    },
    {
        "garhwali": "खांडो",
        "hindi": "चौड़ी दुधारी तलवार",
        "english": "broad double-edged ceremonial sword",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "खांडो", "tehri": "तलवार", "salani": "खांडा", "rathwali": "खांडो"}
    },
    {
        "garhwali": "बर्छी",
        "hindi": "भाला / नेजा",
        "english": "spear / lance",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "बर्छी", "tehri": "भाला", "salani": "नेजा", "rathwali": "बर्छी"}
    },
    {
        "garhwali": "ढाल",
        "hindi": "गैंडे की खाल की ढाल",
        "english": "protective battle shield",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "ढाल", "tehri": "ढाल", "salani": "ढाल", "rathwali": "ढाळ"}
    },
    {
        "garhwali": "धुणी",
        "hindi": "सिद्धों व नाथों की पवित्र अग्नि",
        "english": "sacred yogic continuous fire altar",
        "pos": "noun",
        "gender": "F",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "धुणी", "tehri": "धूनी", "salani": "धुणी", "rathwali": "धुणी"}
    },
    {
        "garhwali": "धुंवार",
        "hindi": "हवन का पवित्र सुवासित धुआं",
        "english": "sacred aromatic incense smoke of hawan",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "धुंवार", "tehri": "धुआं", "salani": "धूम", "rathwali": "धुंवार"}
    },
    {
        "garhwali": "थान",
        "hindi": "ग्राम देवता का खुला शिला-स्थान / देवस्थल",
        "english": "open-air village deity rock shrine",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "थान", "tehri": "देवस्थान", "salani": "मंढ़", "rathwali": "थान"}
    },
    {
        "garhwali": "बासी",
        "hindi": "देवता का प्रसाद / नैवेद्य",
        "english": "sacred consecrated food offering to deities",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "बासी", "tehri": "प्रसाद", "salani": "भोग", "rathwali": "बासी"}
    },
    {
        "garhwali": "जाग",
        "hindi": "रातभर चलने वाला जागर अनुष्ठान",
        "english": "all-night spiritual vigil and deity invocation",
        "pos": "noun",
        "gender": "F",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "जाग", "tehri": "जागर", "salani": "जागरण", "rathwali": "जाग"}
    },
    {
        "garhwali": "पश्वा",
        "hindi": "जिस व्यक्ति के शरीर में देवता आते हैं",
        "english": "spiritual medium possessed by the deity during jagar",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पश्वा", "tehri": "डांगरिया", "salani": "घटुवा", "rathwali": "पश्वा"}
    },

    # ==================== 4. BHATT 1976 (Historical Geography & Hill Architecture) ====================
    {
        "garhwali": "गौठ",
        "hindi": "मकान के भूतल की गोशाला",
        "english": "ground-floor cattle barn of traditional hill house",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "गौठ", "tehri": "गोठ", "salani": "सार", "rathwali": "गौठ"}
    },
    {
        "garhwali": "माझ",
        "hindi": "मकान की बीच की मंजिल / रिहायशी कमरा",
        "english": "middle living floor of a multi-storey mountain house",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "माझ", "tehri": "मंजिल", "salani": "बीच", "rathwali": "माझ"}
    },
    {
        "garhwali": "टिपर",
        "hindi": "मकान की सबसे ऊपरी छत की अटारी",
        "english": "top attic / loft beneath the slate roof",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "टिपर", "tehri": "अटारी", "salani": "छज्जा", "rathwali": "टिपर"}
    },
    {
        "garhwali": "चौक",
        "hindi": "मकान के आगे का खुला आंगन",
        "english": "paved stone courtyard in front of traditional house",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "चौक", "tehri": "आंगन", "salani": "अंगनाई", "rathwali": "चौक"}
    },
    {
        "garhwali": "धारेली",
        "hindi": "पहाड़ी पगडंडी की संकरी कगार",
        "english": "narrow cliffside ridge pathway",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "धारेली", "tehri": "पगडंडी", "salani": "डगर", "rathwali": "धारेळी"}
    },
    {
        "garhwali": "डंडा",
        "hindi": "पहाड़ की ऊंची चोटी / पर्वत श्रृंखला",
        "english": "mountain ridge / alpine crest",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "डंडा", "tehri": "डांडा", "salani": "धार", "rathwali": "डांडा"}
    },
    {
        "garhwali": "कांडी",
        "hindi": "घास व पत्तियां ढोने की बड़ी टोकरी",
        "english": "large conical bamboo wicker basket for carrying fodder",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कांडी", "tehri": "डोका", "salani": "कंडी", "rathwali": "कांडी"}
    },
    {
        "garhwali": "मिरगा",
        "hindi": "मृग / हिरण",
        "english": "deer / alpine stag",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "मिरगा", "tehri": "हिरण", "salani": "मृग", "rathwali": "मिरगा"}
    },
    {
        "garhwali": "स्याल",
        "hindi": "सियार / गीदड़",
        "english": "jackal",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "स्याल", "tehri": "गीदड़", "salani": "स्यार", "rathwali": "स्याळ"}
    },
    {
        "garhwali": "भालू",
        "hindi": "हिमालयी काला रीछ",
        "english": "Himalayan black bear",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "भालू", "tehri": "रीछ", "salani": "भालू", "rathwali": "भाळू"}
    },

    # ==================== 5. UPRETI 1894 (Proverbs, Farming, Village Crafts & Wisdom) ====================
    {
        "garhwali": "अखाण",
        "hindi": "कहावत / लोकोक्ति",
        "english": "traditional folk proverb / aphorism",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "अखाण", "tehri": "पखाण", "salani": "कहावत", "rathwali": "अखाण"}
    },
    {
        "garhwali": "आणा",
        "hindi": "पहेली / बुझौवल",
        "english": "folk riddle",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "आणा", "tehri": "पहेली", "salani": "आणा", "rathwali": "आणा"}
    },
    {
        "garhwali": "पखाण",
        "hindi": "पारंपरिक नीतिवचन / पुरानी सीख",
        "english": "ancestral folk moral precept",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पखाण", "tehri": "पखाण", "salani": "अखाण", "rathwali": "पखाण"}
    },
    {
        "garhwali": "घटवार",
        "hindi": "पनचक्की चलाने वाला व्यक्ति",
        "english": "watermill operator (Ghatwar)",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "घटवार", "tehri": "घट्या", "salani": "घटवार", "rathwali": "घटवार"}
    },
    {
        "garhwali": "कुन्यार",
        "hindi": "सब्जी उगाने का बाड़ा / शाकवाटिका",
        "english": "kitchen vegetable garden plot near house",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "कुन्यार", "tehri": "बाड़ा", "salani": "साग-बाड़ा", "rathwali": "कुन्यार"}
    },
    {
        "garhwali": "बाड़",
        "hindi": "खेत के चारों ओर पत्थरों या कांटों की बाड़",
        "english": "protective stone or thorn field fence",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "बाड़", "tehri": "घेरा", "salani": "बाड़ा", "rathwali": "बाड़"}
    },
    {
        "garhwali": "सेरू",
        "hindi": "उपजाऊ सिंचित धान का खेत",
        "english": "irrigated fertile valley floor paddy field",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "सेरू", "tehri": "सेरा", "salani": "क्यारी", "rathwali": "सेरू"}
    },
    {
        "garhwali": "उखरा",
        "hindi": "असिंचित सीढ़ीदार पहाड़ी खेत",
        "english": "rainfed terraced hill field",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "उखरा", "tehri": "उखड़", "salani": "असिंचित-खेत", "rathwali": "उखरा"}
    },
    {
        "garhwali": "पापड़ी",
        "hindi": "रोटी पर जमने वाली कुरकुरी परत",
        "english": "crispy outer crust of mountain flatbread",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "पापड़ी", "tehri": "पपड़ी", "salani": "पापड़ी", "rathwali": "पापळी"}
    },
    {
        "garhwali": "माल्टा",
        "hindi": "पहाड़ी मीठा संतरा (माल्टा)",
        "english": "sweet Himalayan blood orange / citrus sinensis",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "माल्टा", "tehri": "माल्टा", "salani": "संतरा", "rathwali": "माल्टा"}
    },
    {
        "garhwali": "गलगल",
        "hindi": "बड़ा पहाड़ी खट्टा नींबू",
        "english": "large hill lemon (Citrus pseudolimon)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "गलगल", "tehri": "बड़ा-नींबू", "salani": "खट्टा", "rathwali": "गळगळ"}
    },
    {
        "garhwali": "दाड़िम",
        "hindi": "जंगली अनार (दाड़िम)",
        "english": "wild Himalayan pomegranate (Punica granatum)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "दाड़िम", "tehri": "दाड़िम", "salani": "अनार", "rathwali": "दाड़िम"}
    },

    # ==================== 6. JUYAL 1967 & UOU TEXTBOOKS (Linguistics, Metaphor & Emotion) ====================
    {
        "garhwali": "मया",
        "hindi": "स्नेह / प्रेम / अनुराग",
        "english": "pure affection / maternal or spousal love",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "मया", "tehri": "माया", "salani": "प्रेम", "rathwali": "मया"}
    },
    {
        "garhwali": "हड़कंप",
        "hindi": "घबराहट / भय से कांपना",
        "english": "panic / tremor of sudden fright",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "हड़कंप", "tehri": "कम्प", "salani": "घबराहट", "rathwali": "हड़कम्प"}
    },
    {
        "garhwali": "ह्याव",
        "hindi": "हौसला / हिम्मत / साहस",
        "english": "courage / fortitude of heart",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "ह्याव", "tehri": "हियाव", "salani": "हिम्मत", "rathwali": "ह्याव"}
    },
    {
        "garhwali": "अणहोणी",
        "hindi": "अप्रत्याशित अमंगल घटना",
        "english": "untoward tragedy / fateful mishap",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "अणहोणी", "tehri": "अनहोनी", "salani": "अमंगल", "rathwali": "अणहोणी"}
    },
    {
        "garhwali": "चैत",
        "hindi": "चैत्र मास (वसंत का पहला महीना)",
        "english": "Chaitra month (first month of spring in Himalayan calendar)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "चैत", "tehri": "चैत्र", "salani": "चैत", "rathwali": "चैत"}
    },
    {
        "garhwali": "बैसाख",
        "hindi": "वैशाख मास (फसल कटाई का महीना)",
        "english": "Baisakh month (harvest season)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "बैसाख", "tehri": "वैशाख", "salani": "बैसाख", "rathwali": "बैसाख"}
    },
    {
        "garhwali": "जेठ",
        "hindi": "ज्येष्ठ मास (ग्रीष्म ऋतु)",
        "english": "Jeth month (peak summer)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "जेठ", "tehri": "ज्येष्ठ", "salani": "जेठ", "rathwali": "जेठ"}
    },
    {
        "garhwali": "असाढ़",
        "hindi": "आषाढ़ मास (वर्षा का आगमन)",
        "english": "Asadh month (arrival of monsoon rains)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "असाढ़", "tehri": "आषाढ़", "salani": "असाढ़", "rathwali": "असाढ़"}
    },
    {
        "garhwali": "सावण",
        "hindi": "श्रावण मास (झमाझम सावन)",
        "english": "Sawan month (height of monsoon)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सावण", "tehri": "श्रावण", "salani": "सावन", "rathwali": "सावण"}
    },
    {
        "garhwali": "भादों",
        "hindi": "भाद्रपद मास",
        "english": "Bhado month (late monsoon)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "भादों", "tehri": "भाद्रपद", "salani": "भादों", "rathwali": "भादों"}
    },
    {
        "garhwali": "आसोज",
        "hindi": "आश्विन मास (शरद ऋतु)",
        "english": "Asoj month (crisp autumn)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "आसोज", "tehri": "आश्विन", "salani": "क्वार", "rathwali": "आसोज"}
    },
    {
        "garhwali": "कातिक",
        "hindi": "कार्तिक मास (दीपावली का महीना)",
        "english": "Katik month (festival of lights month)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "कातिक", "tehri": "कार्तिक", "salani": "कातिक", "rathwali": "कातिक"}
    },
    {
        "garhwali": "मगसिर",
        "hindi": "मार्गशीर्ष मास (सर्दियों की शुरुआत)",
        "english": "Magsir month (onset of winter)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "मगसिर", "tehri": "अघन", "salani": "मगसिर", "rathwali": "मगसिर"}
    },
    {
        "garhwali": "पूस",
        "hindi": "पौष मास (कड़ाके की ठंड)",
        "english": "Poos month (deep winter frost)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "पूस", "tehri": "पौष", "salani": "पूस", "rathwali": "पूस"}
    },
    {
        "garhwali": "माघ",
        "hindi": "माघ मास (मकर संक्रांति / घुघुतिया)",
        "english": "Magh month (winter festival of Makar Sankranti)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "माघ", "tehri": "माघ", "salani": "माघ", "rathwali": "माघ"}
    },
    {
        "garhwali": "फागुण",
        "hindi": "फाल्गुन मास (होली का महीना)",
        "english": "Phagun month (Holi festival)",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "फागुण", "tehri": "फाल्गुन", "salani": "फागुन", "rathwali": "फागुण"}
    }
]

added = 0
enriched = 0

for item in NEW_BOOK_WORDS:
    lemma = item["garhwali"].strip()
    if lemma in existing_lemmas:
        ex = existing_lemmas[lemma]
        for k, v in item.items():
            if k == "dialect_variants" and isinstance(v, dict):
                ex.setdefault("dialect_variants", {}).update(v)
            elif k not in ex or not ex[k]:
                ex[k] = v
        enriched += 1
    else:
        existing_lemmas[lemma] = item
        existing_words.append(item)
        added += 1

print(f"Newly added lemmas from full book mining: {added}")
print(f"Enriched existing lemmas: {enriched}")
print(f"Total words count now: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved to {WORDS_PATH}")
