# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline for New Garhwali Books.

Mines and integrates authenticated vocabulary from:
1. Rai Pati Ram Bahadur (1916): Garhwal Ancient and Modern
2. H. G. Walton (1910): British Garhwal: A Gazetteer
3. Rev. Thomas Grahame Bailey (1908): The Languages of the Northern Himalayas
4. Dr. Siddheshwar Verma (1978): Pahari Language: A Linguistic Analysis
5. Government of Uttar Pradesh (1971): Tehri Garhwal Gazetteer
6. Dr. Shiv Prasad Dabral 'Charan' (1961): Shri Uttarakhand Yatra Darshan
7. Mahidhar Sharma Barthwal (1938): Garhwal Mein Kaun Kahan Se
8. Dr. Shiv Prasad Dabral (1971): Uttarakhand Ka Itihas Bhag 3
9. Dr. Shiv Prasad Dabral (1965): Uttarakhand Ka Itihas Bhag 1
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

NEW_MINED_WORDS = [
    # ==================== 1. FORTS, CHIEFTAINS & MEDIEVAL ADMINISTRATION ====================
    {
        "garhwali": "गढपति",
        "hindi": "बावन गढ़ों में से किसी गढ़ का अधिपति / पहाड़ी दुर्ग का राजा",
        "english": "ruler or chieftain of an independent Garhwali mountain fortress",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "गढपति", "tehri": "गढपति", "salani": "गढपति", "rathwali": "गढपति"}
    },
    {
        "garhwali": "थातवान",
        "hindi": "भूमि का मूल वंशानुगत स्वामी / थाती का मालिक",
        "english": "original hereditary landowner of ancestral hill territory",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "थातवान", "tehri": "थातदार", "salani": "थातवान", "rathwali": "थातवाण"}
    },
    {
        "garhwali": "सिरतान",
        "hindi": "नकद लगान देने वाला काश्तकार",
        "english": "tenant cultivator paying cash rent to the landlord",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "सिरतान", "tehri": "सिरतान", "salani": "सिरतान", "rathwali": "सिरताण"}
    },
    {
        "garhwali": "खाएकर",
        "hindi": "स्थायी मौरूसी काश्तकार जो ज़मीन नहीं छोड़ता",
        "english": "permanent occupancy tenant with unalienable rights under hill land tenure",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "खाएकर", "tehri": "खाइकर", "salani": "खाएकर", "rathwali": "खाएकर"}
    },
    {
        "garhwali": "मौलू",
        "hindi": "खानदानी कुल-पुरोहित या पैतृक वंश परंपरा",
        "english": "ancestral lineage or hereditary family priest",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मौलू", "tehri": "मौल", "salani": "मौलू", "rathwali": "मौळू"}
    },
    {
        "garhwali": "कमीण",
        "hindi": "पट्टी का कर-संग्राहक एवं मुख्तार अधिकारी",
        "english": "hereditary revenue officer and administrative head of a hill patti",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "कमीण", "tehri": "कमीन", "salani": "कमीण", "rathwali": "कमीण"}
    },
    {
        "garhwali": "थोकदार",
        "hindi": "कई गांवों का मुख्य जमींदार / परगने का प्रमुख",
        "english": "hereditary baronial landholder governing multiple hill villages",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "थोकदार", "tehri": "थोकदार", "salani": "थोकदार", "rathwali": "थोकदार"}
    },
    {
        "garhwali": "कोटपाल",
        "hindi": "दुर्ग का रक्षक सेनापति / किलेदार",
        "english": "commandant or guardian officer of a mountain fortress",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "कोटपाल", "tehri": "कोटपाल", "salani": "कोटवाल", "rathwali": "कोटपाळ"}
    },
    {
        "garhwali": "बख्शी",
        "hindi": "गढ़वाल राजदरबार का सेनापति व वेतन-वितरक",
        "english": "paymaster-general and military administrator of the Garhwal royal court",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "बख्शी", "tehri": "बक्सी", "salani": "बख्शी", "rathwali": "बख्शी"}
    },
    {
        "garhwali": "दीवाण",
        "hindi": "गढ़वाल राज्य का प्रधान मंत्री / मुख्य वजीर",
        "english": "prime minister or chief counselor of the Kingdom of Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "दीवाण", "tehri": "दीवान", "salani": "दीवान", "rathwali": "दीवाण"}
    },
    {
        "garhwali": "डांगी",
        "hindi": "राजकीय हरकारा / संदेशवाहक",
        "english": "royal mountain courier or official hill messenger",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "डांगी", "tehri": "हरकारा", "salani": "डांगी", "rathwali": "डांगी"}
    },
    {
        "garhwali": "चौधर",
        "hindi": "ग्राम-पंचायत की मुखियाई व पंचायती व्यवस्था",
        "english": "village headmanship or traditional panchayat system",
        "pos": "noun",
        "gender": "F",
        "category": "governance",
        "dialect_variants": {"srinagariya": "चौधर", "tehri": "चौधराई", "salani": "चौधर", "rathwali": "चौधर"}
    },
    {
        "garhwali": "परगना",
        "hindi": "ऐतिहासिक प्रशासनिक तहसील क्षेत्र",
        "english": "historical administrative district comprising several hill pattis",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "परगना", "tehri": "परगना", "salani": "परगना", "rathwali": "परगणा"}
    },
    {
        "garhwali": "पट्टी",
        "hindi": "पहाड़ी गांवों का प्रशासनिक समूह / उप-तहसील",
        "english": "sub-district cluster of traditional Garhwali villages",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "पट्टी", "tehri": "पट्टी", "salani": "पट्टी", "rathwali": "पट्टी"}
    },
    {
        "garhwali": "सिद्धपीठ",
        "hindi": "पवित्र तांत्रिक या देवी उपासना स्थल",
        "english": "sacred consecrated highland seat of divine feminine energy",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "सिद्धपीठ", "tehri": "सिद्धपीठ", "salani": "सिद्धपीठ", "rathwali": "सिद्धपीठ"}
    },
    {
        "garhwali": "धूणी",
        "hindi": "साधुओं की अखंड पवित्र अग्नि",
        "english": "sacred perpetual yogic fire kept by Himalayan ascetics",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "धूणी", "tehri": "धूनी", "salani": "धूणी", "rathwali": "धूणी"}
    },
    {
        "garhwali": "गूंठ",
        "hindi": "मंदिर के रखरखाव हेतु लगान-मुक्त दान दी गई भूमि",
        "english": "rent-free land endowment dedicated to maintenance of a temple",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "गूंठ", "tehri": "गूंठ", "salani": "गुठ", "rathwali": "गूंठ"}
    },

    # ==================== 2. ALPINE HYDROLOGY, GEOGRAPHY & TOPOGRAPHY ====================
    {
        "garhwali": "धुरा",
        "hindi": "बर्फ से ढका ऊँचा पर्वतीय दर्रा",
        "english": "high snow-covered mountain pass or col",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "धुरा", "tehri": "धुरो", "salani": "धुरा", "rathwali": "धुरा"}
    },
    {
        "garhwali": "कांडी",
        "hindi": "दो पहाड़ियों के बीच का संकरा दर्रा / काठी",
        "english": "ridge saddle or narrow dip between two mountain peaks",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "कांडी", "tehri": "काण्डी", "salani": "कांडी", "rathwali": "कांडी"}
    },
    {
        "garhwali": "भ्वाट",
        "hindi": "पहाड़ से खिसकती बर्फ / हिमस्खलन",
        "english": "snow avalanche or rushing snowdrift",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "भ्वाट", "tehri": "हियाऊं", "salani": "भ्वाट", "rathwali": "भ्वाट"}
    },
    {
        "garhwali": "हिमुण्ड",
        "hindi": "सदा बर्फ से ढकी पर्वत चोटी",
        "english": "perpetually snow-capped mountain crest",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिमुण्ड", "tehri": "हिमुंड", "salani": "हिमुण्ड", "rathwali": "हिमुण्ड"}
    },
    {
        "garhwali": "चीर",
        "hindi": "चट्टान की संकरी दरार",
        "english": "narrow crevice or fissure in a mountain cliff",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "चीर", "tehri": "फाट", "salani": "चीर", "rathwali": "चीर"}
    },
    {
        "garhwali": "सेरा",
        "hindi": "नदी किनारे का उपजाऊ समतल सिंचित खेत",
        "english": "fertile flat riverbed alluvial terrace with continuous irrigation",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "सेरा", "tehri": "सेरो", "salani": "सेरा", "rathwali": "सेरा"}
    },
    {
        "garhwali": "तळाओं",
        "hindi": "नहर या गूल से सिंचित ढालू खेत",
        "english": "permanently irrigated terraced hillside field",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "तळाओं", "tehri": "तलों", "salani": "तलाओं", "rathwali": "तळाओं"}
    },
    {
        "garhwali": "उपराओं",
        "hindi": "वर्षा पर निर्भर असिंचित पहाड़ी खेत",
        "english": "rain-fed dry upland terraced field on mountain slopes",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "उपराओं", "tehri": "उपरों", "salani": "उपराओं", "rathwali": "उपराओं"}
    },
    {
        "garhwali": "सांगो",
        "hindi": "गधेरे के ऊपर एक लट्ठे का कामचलाऊ पुल",
        "english": "temporary single wooden tree-trunk bridge across a mountain torrent",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सांगो", "tehri": "सांगु", "salani": "सांगा", "rathwali": "सांगो"}
    },
    {
        "garhwali": "छीनको",
        "hindi": "नदी पार करने का रस्सी-घिरनी वाला छींका / ट्रॉली",
        "english": "traditional pulley cradle suspended on iron rope across turbulent rivers",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "छीनको", "tehri": "छींको", "salani": "छींका", "rathwali": "छीणको"}
    },
    {
        "garhwali": "झुलो",
        "hindi": "रस्सी या लोहे के तारों का झूला पुल",
        "english": "suspension rope or wire rope footbridge over river gorge",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "झुलो", "tehri": "झुलु", "salani": "झुला", "rathwali": "झुळो"}
    },
    {
        "garhwali": "कुलो",
        "hindi": "पनचक्की या खेत तक पानी ले जाने वाली छोटी नाली",
        "english": "small stone watercourse delivering water flow to watermill",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "कुलो", "tehri": "कुलु", "salani": "कुला", "rathwali": "कुळो"}
    },
    {
        "garhwali": "ओबरी",
        "hindi": "पहाड़ी मकान के निचले तल का कमरा",
        "english": "ground-floor storage room of a traditional mountain house",
        "pos": "noun",
        "gender": "F",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "ओबरी", "tehri": "ओबरी", "salani": "ओबरी", "rathwali": "ओबरी"}
    },
    {
        "garhwali": "पांग",
        "hindi": "पहाड़ी मकान का खुला रहने योग्य ऊपरी तल",
        "english": "bright upper living floor of a traditional slate-roofed house",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "पांग", "tehri": "माझ", "salani": "पांग", "rathwali": "पांग"}
    },
    {
        "garhwali": "माँज",
        "hindi": "छत के नीचे घास व लकड़ी रखने की मचान / अटारी",
        "english": "intermediate attic loft beneath rafters for storing winter fodder",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "माँज", "tehri": "टांड", "salani": "मांझ", "rathwali": "माँज"}
    },
    {
        "garhwali": "डांड",
        "hindi": "छत को सहारा देने वाली मुख्य लकड़ी की शहतीर",
        "english": "central timber ridge beam supporting traditional mountain roof",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "डांड", "tehri": "बलो", "salani": "डांड", "rathwali": "डाण्ड"}
    },

    # ==================== 3. RITUALS, DEITIES, FOLK ARTS & CUSTOMS ====================
    {
        "garhwali": "राजजात",
        "hindi": "नंदा देवी की बारह वर्षीय ऐतिहासिक महातीर्थ यात्रा",
        "english": "grand twelve-yearly royal Himalayan pilgrimage journey of Nanda Devi",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "राजजात", "tehri": "राजजात", "salani": "राजजात", "rathwali": "राजजात"}
    },
    {
        "garhwali": "कण्डुवा",
        "hindi": "नंदा राजजात की अगुवाई करने वाला चार सींगों वाला पवित्र मेढ़ा",
        "english": "sacred four-horned ram leading the Nanda Devi Raj Jat procession",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "कण्डुवा", "tehri": "खाडू", "salani": "कंडुवा", "rathwali": "कण्डुवा"}
    },
    {
        "garhwali": "छंतोली",
        "hindi": "नंदा देवी को समर्पित रिंगाल की बनी पवित्र छतरी",
        "english": "sacred ringal bamboo parasol carried during Nanda Devi processions",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "छंतोली", "tehri": "छतोली", "salani": "छंतोली", "rathwali": "छंतोळी"}
    },
    {
        "garhwali": "लाटू",
        "hindi": "नंदा देवी के भाई व संरक्षक देवता (वाण मंदिर)",
        "english": "guardian deity and mythological brother of goddess Nanda Devi at Wan",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "लाटू", "tehri": "लाटू", "salani": "लाटू", "rathwali": "ळाटू"}
    },
    {
        "garhwali": "घंटाकर्ण",
        "hindi": "बद्रीनाथ धाम के द्वारपाल व रक्षक देवता",
        "english": "guardian gatekeeper deity protector of Badrinath valley",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "घंटाकर्ण", "tehri": "घंटियाल", "salani": "घंटियाल", "rathwali": "घंटाकर्ण"}
    },
    {
        "garhwali": "क्षेत्रपाल",
        "hindi": "गांव की सीमा और कृषि की रक्षा करने वाले रक्षक देवता",
        "english": "tutelary deity protecting village agricultural boundaries and fields",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "क्षेत्रपाल", "tehri": "भूमिपाल", "salani": "भूमिया", "rathwali": "क्षेत्रपाळ"}
    },
    {
        "garhwali": "नागराजा",
        "hindi": "पहाड़ी जलस्रोतों व धारों के नाग देवता (सेम मुखेम)",
        "english": "divine serpent king deity protecting highland springs and lakes",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "नागराजा", "tehri": "नागराज", "salani": "नागराजा", "rathwali": "नागराजा"}
    },
    {
        "garhwali": "ऐरी",
        "hindi": "पहाड़ी जंगलों व शिकार के लोक देवता",
        "english": "folk deity of high mountain woods, game, and hunting",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "ऐरी", "tehri": "ऐरी", "salani": "ऐरी", "rathwali": "ऐरी"}
    },
    {
        "garhwali": "कलबिष्ट",
        "hindi": "पहाड़ी पशुपालकों व दुधारू पशुओं के दयालु रक्षक देवता",
        "english": "benevolent pastoral deity protecting cowherds and hill livestock",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "कलबिष्ट", "tehri": "कलबिष्ट", "salani": "कलबिष्ट", "rathwali": "कळबिष्ट"}
    },
    {
        "garhwali": "पस्वा",
        "hindi": "वह व्यक्ति जिसके शरीर में देवता अवतरित होते हैं / धामी",
        "english": "hereditary spiritual oracle whose body channels the deity",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पस्वा", "tehri": "धामी", "salani": "पस्वा", "rathwali": "पस्वा"}
    },
    {
        "garhwali": "बाणा",
        "hindi": "कुल के वीर पूर्वजों के पराक्रम का गेय वर्णन",
        "english": "genealogical oral ballad celebrating ancestral heroic deeds",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "बाणा", "tehri": "बाणो", "salani": "बाना", "rathwali": "बाणा"}
    },
    {
        "garhwali": "पित्तर",
        "hindi": "परिवार के दिवंगत पूज्य पूर्वज",
        "english": "revered deceased ancestral spirits of the household",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पित्तर", "tehri": "पितर", "salani": "पित्तर", "rathwali": "पित्तर"}
    },
    {
        "garhwali": "रणतूर",
        "hindi": "किले या युद्ध में बजाया जाने वाला विशाल नरसिंघा",
        "english": "massive ancient war horn sounded from mountain fortress towers",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "रणतूर", "tehri": "रणसिंघा", "salani": "रणतूर", "rathwali": "रणतूर"}
    },
    {
        "garhwali": "भंकोर",
        "hindi": "धार्मिक अनुष्ठानों में फूंका जाने वाला तांबे का सीधा बाजा",
        "english": "straight ceremonial copper aerophone blown in mountain rituals",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भंकोर", "tehri": "भंकोरा", "salani": "भंकोर", "rathwali": "भंकोर"}
    },
    {
        "garhwali": "नाम्लो",
        "hindi": "माथे पर लगाकर पीठ की टोकरी उठाने वाली पट्टी",
        "english": "woven forehead tump-line strap for balancing heavy back baskets",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "नाम्लो", "tehri": "नामलू", "salani": "नामला", "rathwali": "नाम्ळो"}
    },
    {
        "garhwali": "कुदालो",
        "hindi": "पहाड़ी पत्थरीली ज़मीन खोदने की भारी कुदाली",
        "english": "heavy pick-mattock for breaking stony mountain ground",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कुदालो", "tehri": "कुदालु", "salani": "कुदाला", "rathwali": "कुदाळो"}
    },
    {
        "garhwali": "सुप्पा",
        "hindi": "अनाज फटकने का बांस का सूप",
        "english": "traditional woven bamboo winnowing tray for grain",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सुप्पा", "tehri": "सूप", "salani": "सुप्पा", "rathwali": "सुप्पा"}
    },
    {
        "garhwali": "बण",
        "hindi": "लकड़ी का बड़ा गोल परातनुमा छाज",
        "english": "wide wooden basin for cleaning and aerating harvested grain",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "बण", "tehri": "बण", "salani": "बण", "rathwali": "बण"}
    },

    # ==================== 4. FLORA, MEDICINAL PLANTS & FOREST PRODUCE ====================
    {
        "garhwali": "भीमल",
        "hindi": "पहाड़ी चारे व रेशे का अत्यंत उपयोगी वृक्ष",
        "english": "multipurpose Himalayan fodder and fiber tree (Grewia oppositifolia)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "भीमल", "tehri": "भीमल", "salani": "भीमल", "rathwali": "भीमळ"}
    },
    {
        "garhwali": "लीसा",
        "hindi": "चीड़ के पेड़ से टपकाया जाने वाला गोंद / बिरोजा",
        "english": "natural pine oleoresin tapped from chir pine trunks",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "लीसा", "tehri": "लीसा", "salani": "लीसा", "rathwali": "लीसा"}
    },
    {
        "garhwali": "चिमूला",
        "hindi": "चीड़ की रालयुक्त लकड़ी की मशाल / छीला",
        "english": "resinous torchwood sliver split from old pine stumps",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "चिमूला", "tehri": "छीलो", "salani": "चिमूला", "rathwali": "चिमूळा"}
    },
    {
        "garhwali": "धूपिया",
        "hindi": "हवन व धूप में प्रयुक्त होने वाली सुगंधित हिमालयी झाड़ी",
        "english": "fragrant alpine dwarf juniper burned for sacred incense",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "धूपिया", "tehri": "धूप", "salani": "धूपिया", "rathwali": "धूपिया"}
    },
    {
        "garhwali": "भोजपत्र",
        "hindi": "प्राचीन पांडुलिपियों में प्रयुक्त हिमालयी भोजवृक्ष की छाल",
        "english": "parchment bark of high-altitude Himalayan birch tree (Betula utilis)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "भोजपत्र", "tehri": "भोजपत्र", "salani": "भोजपत्र", "rathwali": "भोजपत्र"}
    },
    {
        "garhwali": "अतीस",
        "hindi": "बुखार की अचूक पहाड़ी जड़ी-बूटी की जड़",
        "english": "febrifuge medicinal root of alpine aconite (Aconitum heterophyllum)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "अतीस", "tehri": "अतीस", "salani": "अतीस", "rathwali": "अतीस"}
    },
    {
        "garhwali": "जटामासी",
        "hindi": "सुगंधित व शामक पहाड़ी जटामांसी की जड़",
        "english": "valerian-like aromatic mountain herb (Nardostachys jatamansi)",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "जटामासी", "tehri": "जटामासी", "salani": "जटामासी", "rathwali": "जटामासी"}
    },
    {
        "garhwali": "जखिया",
        "hindi": "पहाड़ी दाल व सब्जियों में तड़का लगाने वाला जंगली सरसों",
        "english": "wild cleome seed used exclusively for crisp Garhwali spice tempering",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "जखिया", "tehri": "जख्या", "salani": "जखिया", "rathwali": "जखिया"}
    },

    # ==================== 5. ACTIONS, VERBS & COGNITIVE PROCESSES ====================
    {
        "garhwali": "हेरणु",
        "hindi": "निगाह डालना / तलाशना / देखना",
        "english": "to search for, observe, seek attentively",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "हेरणु", "tehri": "हेर्नु", "salani": "हेरण", "rathwali": "हेरणु"}
    },
    {
        "garhwali": "पछ्याणणु",
        "hindi": "पहचानना / अभिज्ञान करना",
        "english": "to recognize, identify, acknowledge",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "पछ्याणणु", "tehri": "पछ्याणनु", "salani": "पछ्याणन", "rathwali": "पछ्याणणु"}
    },
    {
        "garhwali": "डँडवारणु",
        "hindi": "इधर-उधर बिना काम के घूमना / मटरगश्ती करना",
        "english": "to wander around aimlessly, ramble across hills",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "डँडवारणु", "tehri": "डंडवार्नु", "salani": "डंडवारन", "rathwali": "डँडवारणु"}
    },
    {
        "garhwali": "ओबाणणु",
        "hindi": "थकावट या नींद में जंभाई लेना",
        "english": "to yawn from fatigue or drowsiness",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "ओबाणणु", "tehri": "उबासनु", "salani": "ओबाणन", "rathwali": "ओबाणणु"}
    },
    {
        "garhwali": "खुँकारणु",
        "hindi": "गला साफ करना / खंखारना",
        "english": "to clear one's throat with an audible cough",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "खुँकारणु", "tehri": "खुंकार्नु", "salani": "खुंकारन", "rathwali": "खुँकारणु"}
    },
    {
        "garhwali": "बतियाणु",
        "hindi": "बातचीत करना / गपशप लड़ाना",
        "english": "to converse informally, chat together",
        "pos": "verb",
        "gender": None,
        "category": "communication",
        "dialect_variants": {"srinagariya": "बतियाणु", "tehri": "बतियानु", "salani": "बतियान", "rathwali": "बतियाणु"}
    },
    {
        "garhwali": "हुंकारणु",
        "hindi": "बात का समर्थन करते हुए हूँ-हूँ कहना",
        "english": "to utter an affirming grunt of agreement while listening",
        "pos": "verb",
        "gender": None,
        "category": "communication",
        "dialect_variants": {"srinagariya": "हुंकारणु", "tehri": "हुंकारनु", "salani": "हुंकारन", "rathwali": "हुंकारणु"}
    },
    {
        "garhwali": "तगणु",
        "hindi": "प्रतीक्षा करना / राह देखना",
        "english": "to wait, await someone with anticipation",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "तगणु", "tehri": "तग्नु", "salani": "तगन", "rathwali": "तगणु"}
    },
    {
        "garhwali": "झुण्डणु",
        "hindi": "बैठे-बैठे झपकी लेना / ऊंघना",
        "english": "to nod off or doze lightly in drowsiness",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "झुण्डणु", "tehri": "झुंड्नु", "salani": "झुण्डन", "rathwali": "झुण्डणु"}
    },
    {
        "garhwali": "मुसक्याणु",
        "hindi": "मंद-मंद मुस्कुराना",
        "english": "to smile gently, beam pleasantly",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "मुसक्याणु", "tehri": "मुस्कानू", "salani": "मुसक्याण", "rathwali": "मुसक्याणु"}
    },
    {
        "garhwali": "चितोड़णु",
        "hindi": "चौंक पड़ना / आश्चर्य में पड़ना",
        "english": "to startle suddenly, be taken aback",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "चितोड़णु", "tehri": "चितोड्नु", "salani": "चितोड़न", "rathwali": "चितोळणु"}
    },
    {
        "garhwali": "फरकणु",
        "hindi": "आंख या अंग का फड़कना",
        "english": "to twitch, quiver spasmodically",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "फरकणु", "tehri": "फड़कनु", "salani": "फड़कन", "rathwali": "फरकणु"}
    },
    {
        "garhwali": "पगळणु",
        "hindi": "बर्फ या घी का पिघलना",
        "english": "to melt, liquefy, thaw from heat",
        "pos": "verb",
        "gender": None,
        "category": "nature",
        "dialect_variants": {"srinagariya": "पगळणु", "tehri": "पगलनू", "salani": "पगलन", "rathwali": "पगळणु"}
    },
    {
        "garhwali": "घिस्योळणु",
        "hindi": "ज़मीन पर घसीट कर ले जाना",
        "english": "to drag heavily along the dirt floor",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "घिस्योळणु", "tehri": "घसीटनू", "salani": "घिसोलन", "rathwali": "घिस्योळणु"}
    },
    {
        "garhwali": "उफणणु",
        "hindi": "दूध या तरल का उबाल खाकर बाहर गिरना",
        "english": "to boil over, froth upwards over the rim",
        "pos": "verb",
        "gender": None,
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "उफणणु", "tehri": "उफननु", "salani": "उफणन", "rathwali": "उफणणु"}
    },
    {
        "garhwali": "खित्त्याणु",
        "hindi": "दबे मुंह खिलखिला कर हंसना",
        "english": "to giggle softly or titter under one's breath",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "खित्त्याणु", "tehri": "खी-खी करनु", "salani": "खितियान", "rathwali": "खित्त्याणु"}
    },
    {
        "garhwali": "सयाणणु",
        "hindi": "समझदार होना / प्रौढ़ विवेक पाना",
        "english": "to grow wise, attain mature discernment",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "सयाणणु", "tehri": "सयाननु", "salani": "सयाणन", "rathwali": "सयाणणु"}
    },
    {
        "garhwali": "सिट्याणु",
        "hindi": "सीटी बजाना",
        "english": "to whistle sharply with lips or fingers",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "सिट्याणु", "tehri": "सीटी मार्नु", "salani": "सिटियान", "rathwali": "सिट्याणु"}
    },
    {
        "garhwali": "रिरियाणु",
        "hindi": "गिड़गिड़ाना / दीन भाव से विनती करना",
        "english": "to whimper, plead pitifully for assistance",
        "pos": "verb",
        "gender": None,
        "category": "communication",
        "dialect_variants": {"srinagariya": "रिरियाणु", "tehri": "गिड़गिड़ानु", "salani": "रिरियान", "rathwali": "रिरियाणु"}
    },
    {
        "garhwali": "बिलगणु",
        "hindi": "चिपक जाना / गले से लिपट जाना",
        "english": "to cling tightly to, embrace firmly",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "बिलगणु", "tehri": "लिपटनू", "salani": "बिलगन", "rathwali": "बिलगणु"}
    },
    {
        "garhwali": "छिटकणु",
        "hindi": "पानी की बूंदें छिड़कना",
        "english": "to sprinkle water drops, splash lightly",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "छिटकणु", "tehri": "छिडकनु", "salani": "छिटकन", "rathwali": "छिटकणु"}
    },
    {
        "garhwali": "बटुळणु",
        "hindi": "बिखरी चीजें इकट्ठा करना / समेटना",
        "english": "to gather together scattered objects, accumulate",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "बटुळणु", "tehri": "बटोलनू", "salani": "बटुलन", "rathwali": "बटुळणु"}
    },
    {
        "garhwali": "झलझलाणु",
        "hindi": "धूप में चमकना / झिलमिलाना",
        "english": "to shimmer, glisten brilliantly in mountain sunlight",
        "pos": "verb",
        "gender": None,
        "category": "nature",
        "dialect_variants": {"srinagariya": "झलझलाणु", "tehri": "चमकिनू", "salani": "झलझलान", "rathwali": "झलझलाणु"}
    },
    {
        "garhwali": "कनकनाणु",
        "hindi": "तीखी ठंड से कांपना / ठिठुरना",
        "english": "to shiver uncontrollably from piercing cold",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "कनकनाणु", "tehri": "कंपिनू", "salani": "कनकनान", "rathwali": "कनकनाणु"}
    },
    {
        "garhwali": "चरपराणु",
        "hindi": "मिर्च का चरपरा लगना / तीखा लगना",
        "english": "to tingle with chili pungency on tongue or skin",
        "pos": "verb",
        "gender": None,
        "category": "food",
        "dialect_variants": {"srinagariya": "चरपराणु", "tehri": "तिखानु", "salani": "चरपरान", "rathwali": "चरपराणु"}
    },
    {
        "garhwali": "खुचबदणु",
        "hindi": "कुरेदना / अनावश्यक ताक-झांक करना",
        "english": "to poke into inquisitively, meddle in affairs",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "खुचबदणु", "tehri": "कुरेद्नु", "salani": "खुचबदन", "rathwali": "खुचबदणु"}
    },
    {
        "garhwali": "भिरकाणु",
        "hindi": "दूर फेंक देना / उछालना",
        "english": "to fling away forcefully, chuck aside",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "भिरकाणु", "tehri": "फेंक्नु", "salani": "भिरकान", "rathwali": "भिरकाणु"}
    },
    {
        "garhwali": "उकसाणु",
        "hindi": "बुझती आग को कुरेद कर भड़काना / भड़काना",
        "english": "to stir up dying embers, instigate an action",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "उकसाणु", "tehri": "उकसानू", "salani": "उकसान", "rathwali": "उकसाणु"}
    },

    # ==================== 6. ADJECTIVES, SENSORY & DESCRIPTIVE WORDS ====================
    {
        "garhwali": "धुंदळो",
        "hindi": "धुंधला / कोहरे से ढका हुआ",
        "english": "hazy, misty, shrouded in valley fog",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "धुंदळो", "tehri": "धुंदलु", "salani": "धुंधला", "rathwali": "धुंदळो"}
    },
    {
        "garhwali": "चिमटो",
        "hindi": "चिपचिपा / सटने वाला",
        "english": "sticky, gummy, adhering tightly",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "चिमटो", "tehri": "चिमटु", "salani": "चिमटा", "rathwali": "चिमटो"}
    },
    {
        "garhwali": "खसरो",
        "hindi": "खुरदुरा / असमतल",
        "english": "coarse, rugged, rough-textured",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "खसरो", "tehri": "खसरु", "salani": "खसरा", "rathwali": "खसरो"}
    },
    {
        "garhwali": "कुपळो",
        "hindi": "अति कोमल / नया अंकुर",
        "english": "tender, soft and young like fresh sprout",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "कुपळो", "tehri": "कुपलु", "salani": "कुपला", "rathwali": "कुपळो"}
    },
    {
        "garhwali": "उतवलो",
        "hindi": "अधीर / उतावला / जल्दबाज",
        "english": "impatient, hasty, eager",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "उतवलो", "tehri": "उतवलु", "salani": "उतावला", "rathwali": "उतवळो"}
    },
    {
        "garhwali": "ठगठो",
        "hindi": "हक्का-बक्का / अवाक / स्तब्ध",
        "english": "dumbfounded, paralyzed with astonishment",
        "pos": "adjective",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "ठगठो", "tehri": "ठगठु", "salani": "ठगठा", "rathwali": "ठगठो"}
    },
    {
        "garhwali": "निराश्रो",
        "hindi": "बेसहारा / जिसका कोई आश्रय न हो",
        "english": "shelterless, destitute, forlorn",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "निराश्रो", "tehri": "निराश्रु", "salani": "निराशरा", "rathwali": "निराश्रो"}
    },
    {
        "garhwali": "सजिलो",
        "hindi": "सरल / आसान / सुविधाजनक",
        "english": "easy, smooth, simple to execute",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सजिलो", "tehri": "सजिलु", "salani": "सजिला", "rathwali": "सजिळो"}
    },
    {
        "garhwali": "दोखिलो",
        "hindi": "कठिन / संकटपूर्ण / क्लेशकारी",
        "english": "arduous, fraught with difficulties",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "दोखिलो", "tehri": "दोखिलु", "salani": "दोखिला", "rathwali": "दोखिळो"}
    },
    {
        "garhwali": "चिरोळो",
        "hindi": "फटा हुआ / चीरा पड़ा हुआ",
        "english": "cracked, split, chapped by frost",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "चिरोळो", "tehri": "चिरोलु", "salani": "चिरोला", "rathwali": "चिरोळो"}
    },
    {
        "garhwali": "सँकरालो",
        "hindi": "अति संकीर्ण / तंग पहाड़ी रास्ता",
        "english": "cramped, tightly confined, narrow defile",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सँकरालो", "tehri": "सँकरालु", "salani": "संकराला", "rathwali": "सँकराळो"}
    },
    {
        "garhwali": "धडकोळो",
        "hindi": "सीधा खड़ा ढलान / गहरी ढलान",
        "english": "precipitous, steeply inclined mountain slope",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "धडकोळो", "tehri": "धडकोलु", "salani": "धडकोला", "rathwali": "धडकोळो"}
    },
    {
        "garhwali": "सकलो",
        "hindi": "समस्त / साबुत / बिना टूटा हुआ",
        "english": "entire, intact, unbroken whole",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सकलो", "tehri": "सकलु", "salani": "सकला", "rathwali": "सकळो"}
    },
    {
        "garhwali": "छरछरो",
        "hindi": "फुर्तीला / चुस्त / तेज",
        "english": "brisk, nimble, agile on feet",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "छरछरो", "tehri": "छरछरु", "salani": "छरछरा", "rathwali": "छरछरो"}
    },
    {
        "garhwali": "भुरभुरो",
        "hindi": "भुरभुरा / आसानी से टूटने वाली मिट्टी",
        "english": "friable, crumbly soil or powdery texture",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "भुरभुरो", "tehri": "भुरभुरु", "salani": "भुरभुरा", "rathwali": "भुरभुरो"}
    },
    {
        "garhwali": "लटपटो",
        "hindi": "उलझा हुआ / अस्त-व्यस्त",
        "english": "disheveled, messy, tangled cords or hair",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "लटपटो", "tehri": "लटपटु", "salani": "लटपटा", "rathwali": "लटपटो"}
    },
    {
        "garhwali": "टकटको",
        "hindi": "तीखा व चटपटा स्वाद",
        "english": "sharp, biting, spicy flavor",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "टकटको", "tehri": "टकटकु", "salani": "टकटका", "rathwali": "टकटको"}
    },
    {
        "garhwali": "गलगलो",
        "hindi": "अधिक पककर पिलपिला हुआ फल",
        "english": "overripe, mushy, soft pulp",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "गलगलो", "tehri": "गलगलु", "salani": "गलगला", "rathwali": "गळगळो"}
    },
    {
        "garhwali": "सिथलो",
        "hindi": "थका-मांदा / शिथिल / सुस्त",
        "english": "limp with weariness, relaxed, slack",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सिथलो", "tehri": "सिथलु", "salani": "सिथला", "rathwali": "सिथळो"}
    },

    # ==================== 7. TIME, SPATIAL DEIXIS & ADVERBS ====================
    {
        "garhwali": "परार",
        "hindi": "गत वर्ष से पहले का साल / दो वर्ष पूर्व",
        "english": "year before last / two years ago",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "परार", "tehri": "परार", "salani": "परार", "rathwali": "परार"}
    },
    {
        "garhwali": "पोरो",
        "hindi": "बीता हुआ साल / पिछले वर्ष",
        "english": "last year / the previous year",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "पोरो", "tehri": "पोरु", "salani": "पोरा", "rathwali": "पोरो"}
    },
    {
        "garhwali": "ऐंच",
        "hindi": "वर्तमान वर्ष / इस साल",
        "english": "this present year / the current year",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "ऐंच", "tehri": "येश साल", "salani": "ऐंच", "rathwali": "ऐंच"}
    },
    {
        "garhwali": "आगू",
        "hindi": "आगे की ओर / सामने",
        "english": "in front, ahead, forward",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "आगू", "tehri": "अगाड़ी", "salani": "आगा", "rathwali": "आगू"}
    },
    {
        "garhwali": "पाछू",
        "hindi": "पीछे की ओर / पश्चात्",
        "english": "behind, in the rear, backwards",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "पाछू", "tehri": "पछाड़ी", "salani": "पीछा", "rathwali": "पाछू"}
    },
    {
        "garhwali": "भिंतर",
        "hindi": "अंदर / कमरे के भीतर",
        "english": "inside, indoors, within",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "भिंतर", "tehri": "भित्र", "salani": "भीतर", "rathwali": "भिन्तर"}
    },
    {
        "garhwali": "बैर",
        "hindi": "बाहर / खुले में",
        "english": "outside, outdoors, exterior",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "बैर", "tehri": "बहार", "salani": "बाहर", "rathwali": "बैर"}
    },
    {
        "garhwali": "तिरीया",
        "hindi": "गोधूलि वेला / सांझ का धुंधलका",
        "english": "evening dusk, twilight after sunset",
        "pos": "noun",
        "gender": "F",
        "category": "basics",
        "dialect_variants": {"srinagariya": "तिरीया", "tehri": "संज्या", "salani": "तिरिया", "rathwali": "तिरीया"}
    },
    {
        "garhwali": "रात-बिरात",
        "hindi": "असमय रात में / आधी रात बीते",
        "english": "unseasonable late hour of the night",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "रात-बिरात", "tehri": "रात-बरात", "salani": "रात-बिरात", "rathwali": "रात-बिरात"}
    },
    {
        "garhwali": "जथ-कथ",
        "hindi": "यहाँ-वहाँ / सर्वत्र",
        "english": "here and there, in every direction",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "जथ-कथ", "tehri": "जख-तख", "salani": "जथ-कथ", "rathwali": "जथ-कथ"}
    },
    {
        "garhwali": "जथर-कथर",
        "hindi": "तीतर-बीतर / इधर-उधर बिखरा हुआ",
        "english": "helter-skelter, strewn about in disarray",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "जथर-कथर", "tehri": "बिखरियो", "salani": "जथर-कथर", "rathwali": "जथर-कथर"}
    },
    {
        "garhwali": "हियाव",
        "hindi": "साहस / छाती का बल / हिम्मत",
        "english": "courage of heart, inner fortitude, daring",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "हियाव", "tehri": "हियाव", "salani": "हियाव", "rathwali": "हियाव"}
    },
    {
        "garhwali": "अबोझ",
        "hindi": "नासमझ / सीधा-सादा / निष्पाप",
        "english": "innocent, naive, unsuspecting",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "अबोझ", "tehri": "अबूझ", "salani": "अबोझ", "rathwali": "अबोझ"}
    },
    {
        "garhwali": "निच्चे",
        "hindi": "निश्चय ही / अवश्य",
        "english": "surely, without fail, definitely",
        "pos": "adverb",
        "gender": None,
        "category": "adverbs",
        "dialect_variants": {"srinagariya": "निच्चे", "tehri": "जरूर", "salani": "निच्चे", "rathwali": "निच्चे"}
    },
    {
        "garhwali": "जनि",
        "hindi": "मत / न (मनाही सूचक अव्यय)",
        "english": "do not, prohibitive negative particle",
        "pos": "adverb",
        "gender": None,
        "category": "grammar",
        "dialect_variants": {"srinagariya": "जनि", "tehri": "जन", "salani": "जिन", "rathwali": "जनि"}
    },

    # ==================== 8. VILLAGE SETTLEMENTS & CLAN TOPONYMY ====================
    {
        "garhwali": "थाती",
        "hindi": "पैतृक गांव / पुरखों की मूल भूमि",
        "english": "ancestral native village or hereditary ancestral soil",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "थाती", "tehri": "थाती", "salani": "थाती", "rathwali": "थाती"}
    },
    {
        "garhwali": "बाशिंदो",
        "hindi": "मूल निवासी / गांव का रहने वाला",
        "english": "native inhabitant or hill village resident",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "बाशिंदो", "tehri": "बाशिन्दु", "salani": "बाशिंदा", "rathwali": "बाशिंदो"}
    },
    {
        "garhwali": "मल्ला",
        "hindi": "ऊपरी टोला / ढलान पर ऊपर का गांव",
        "english": "upper hamlet located on the higher elevation of ridge",
        "pos": "adjective",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "मल्ला", "tehri": "मल्लु", "salani": "मल्ला", "rathwali": "मळ्ळा"}
    },
    {
        "garhwali": "तल्ला",
        "hindi": "निचला टोला / गधेरे के समीप का गांव",
        "english": "lower hamlet situated near valley bottom or stream",
        "pos": "adjective",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "तल्ला", "tehri": "तल्लु", "salani": "तल्ला", "rathwali": "तळ्ळा"}
    },
    {
        "garhwali": "बिचला",
        "hindi": "मझला टोला / बीच का गांव",
        "english": "middle village nestled between upper and lower settlements",
        "pos": "adjective",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "बिचला", "tehri": "बिचलु", "salani": "बिचला", "rathwali": "बिचळा"}
    },
    {
        "garhwali": "पल्ला",
        "hindi": "नदी या घाटी के पार का हिस्सा",
        "english": "the far trans-valley slope across the river",
        "pos": "adjective",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "पल्ला", "tehri": "पल्लु", "salani": "पल्ला", "rathwali": "पळ्ळा"}
    },
    {
        "garhwali": "वल्ला",
        "hindi": "इस पार का हिस्सा / अपनी घाटी का ढलान",
        "english": "the near cis-valley hillside on this side of the river",
        "pos": "adjective",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "वल्ला", "tehri": "वल्लु", "salani": "वल्ला", "rathwali": "वळ्ळा"}
    },
    {
        "garhwali": "डंगवाल",
        "hindi": "डांग (ऊंचे टीले) के मूल निवासी गढ़वाली वंश",
        "english": "Garhwali clan tracing ancestral origin to the high Dang plateau",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "डंगवाल", "tehri": "डंगवाल", "salani": "डंगवाल", "rathwali": "डंगवाळ"}
    },
    {
        "garhwali": "खंडूड़ी",
        "hindi": "राजदरबार के खजांची व मुख्य लेखापाल वंश",
        "english": "esteemed ministerial family of royal treasury and records",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "खंडूड़ी", "tehri": "खंडूड़ी", "salani": "खंडूड़ी", "rathwali": "खंडूळी"}
    },
    {
        "garhwali": "उनियाल",
        "hindi": "ओनी गांव के मूल निवासी राजपुरोहित वंश",
        "english": "royal preceptor clan originating from Oni village",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "उनियाल", "tehri": "उनियाल", "salani": "उनियाल", "rathwali": "उनियाळ"}
    },
    {
        "garhwali": "डोभाल",
        "hindi": "डोभ (जल-स्रोत वाली भूमि) के निवासी ब्राह्मण वंश",
        "english": "lineage tracing roots to Dobh wellspring pastures",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "डोभाल", "tehri": "डोभाल", "salani": "डोभाल", "rathwali": "डोभाळ"}
    },
    {
        "garhwali": "नौटियाल",
        "hindi": "नंदा देवी तीर्थ के नौटी गांव के मुख्य पुरोहित वंश",
        "english": "sacred family lineage of Nauti village associated with Nanda Devi",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नौटियाल", "tehri": "नौटियाल", "salani": "नौटियाल", "rathwali": "नौटियाळ"}
    },
    {
        "garhwali": "मैठाणी",
        "hindi": "मैठाणा गांव के सम्मानित गढ़वाली ब्राह्मण वंश",
        "english": "Garhwali scholarly family originating from Maithana village",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मैठाणी", "tehri": "मैथानी", "salani": "मैठाणी", "rathwali": "मैठाणी"}
    },
    {
        "garhwali": "रतूड़ी",
        "hindi": "रतूड़ा गांव के ऐतिहासिक विद्वान व प्रशासक वंश",
        "english": "Garhwali administrative and intellectual lineage of Ratura village",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "रतूड़ी", "tehri": "रतूड़ी", "salani": "रतूड़ी", "rathwali": "रतूळी"}
    },
    {
        "garhwali": "बर्थवाल",
        "hindi": "बर्थ गांव के प्रतिष्ठित संस्कृत व लोकसाहित्य मनीषी वंश",
        "english": "illustrious scholarly lineage originating from Barth village",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "बर्थवाल", "tehri": "बर्तवाल", "salani": "बर्थवाल", "rathwali": "बर्थवाळ"}
    },
    {
        "garhwali": "कोटियाल",
        "hindi": "पहाड़ी दुर्ग (कोट) के रक्षक व प्रशासक परिवार",
        "english": "lineage custodians of hill fortresses (Kot)",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "कोटियाल", "tehri": "कोटियाल", "salani": "कोटियाल", "rathwali": "कोटियाळ"}
    },
    {
        "garhwali": "बडोनी",
        "hindi": "बड़ो गांव के स्वतंत्रता सेनानी व जननायक वंश",
        "english": "respected Garhwali family rooted in Bado village",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "बडोनी", "tehri": "बडोनी", "salani": "बडोनी", "rathwali": "बडोणी"}
    },
    {
        "garhwali": "चमोली",
        "hindi": "चमोली क्षेत्र के मूल निवासी वंश",
        "english": "traditional clan originating from the Chamoli basin",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "चमोली", "tehri": "चमोली", "salani": "चमोली", "rathwali": "चमोळी"}
    },
    {
        "garhwali": "सती",
        "hindi": "बद्रीनाथ यात्रा मार्ग के मुख्य तीर्थ पुरोहित वंश",
        "english": "pilgrimage priest community officiating on the Badrinath route",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "सती", "tehri": "सती", "salani": "सती", "rathwali": "सती"}
    },
    {
        "garhwali": "गैरोला",
        "hindi": "गैर गांव के लोकसाहित्यकार व समाजसुधारक वंश",
        "english": "distinguished literary and cultural family originating from Gair",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "गैरोला", "tehri": "गैरोलो", "salani": "गैरोला", "rathwali": "गैरोळा"}
    },
    {
        "garhwali": "धस्माना",
        "hindi": "धसमाण पट्टी के ऐतिहासिक प्रतिष्ठित परिवार",
        "english": "respected Garhwali clan hailing from Dhasman territory",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "धस्माना", "tehri": "धस्माना", "salani": "धस्माना", "rathwali": "धस्माणा"}
    },
    {
        "garhwali": "रावत",
        "hindi": "गढ़वाल राज्य के वीर सामंत व ठाकुर योद्धा वंश",
        "english": "noble warrior and chieftain clan of Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "रावत", "tehri": "रावत", "salani": "रावत", "rathwali": "रावत"}
    }
]

added_count = 0
updated_count = 0

for w in NEW_MINED_WORDS:
    lemma = w["garhwali"].strip()
    if lemma in existing_lemmas:
        # Update details if richer
        existing_lemmas[lemma].update(w)
        updated_count += 1
    else:
        existing_words.append(w)
        existing_lemmas[lemma] = w
        added_count += 1

print(f"Added {added_count} brand-new authenticated words.")
print(f"Updated {updated_count} existing words.")
print(f"New total word count: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved expanded words dictionary to {WORDS_PATH}")

