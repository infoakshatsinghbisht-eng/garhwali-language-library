# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline extracting vocabulary from:
- Uttarakhand Open University (UOU) Textbooks (CGL-102, CGL-103, CGL-104, AECC-G-101)
- Ganga Datt Upreti (1894): Proverbs & Folklore of Kumaun and Garhwal
- Oakley & Gairola (1935): Himalayan Folklore
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
print(f"Pre-mining word count: {len(existing_words)}")

UOU_FOLKLORE_WORDS = [
    # ==================== 1. GRAMMAR, CONNECTIVES & PARTICLES (UOU CGL-104) ====================
    {
        "garhwali": "अर",
        "hindi": "और / तथा",
        "english": "and",
        "pos": "conjunction",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "अर", "tehri": "और", "salani": "अर", "rathwali": "अर"}
    },
    {
        "garhwali": "तौभी",
        "hindi": "तथापि / फिर भी",
        "english": "even then / still / nevertheless",
        "pos": "conjunction",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "तौभी", "tehri": "तब-भी", "salani": "तौभी", "rathwali": "तौभी"}
    },
    {
        "garhwali": "हत्तेरी",
        "hindi": "अरे रे! (विस्मय या निराशा का भाव)",
        "english": "alas! / oh no! (exclamation of dismay)",
        "pos": "interjection",
        "gender": "N",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "हत्तेरी", "tehri": "धत्तेरी", "salani": "हत्तेरी", "rathwali": "हत्तेरी"}
    },
    {
        "garhwali": "ईशानी",
        "hindi": "हे भगवान! (स्त्री विस्मय बोधक)",
        "english": "good heavens! (traditional women's exclamation)",
        "pos": "interjection",
        "gender": "N",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "ईशानी", "tehri": "ईसाणी", "salani": "हे-राम", "rathwali": "ईशानी"}
    },
    {
        "garhwali": "यो",
        "hindi": "यह (निकटवर्ती निश्चयवाचक)",
        "english": "this (proximate demonstrative)",
        "pos": "pronoun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "यो", "tehri": "यह", "salani": "यो", "rathwali": "यो"}
    },
    {
        "garhwali": "वो",
        "hindi": "वह (दूरवर्ती निश्चयवाचक)",
        "english": "that (remote demonstrative)",
        "pos": "pronoun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "वो", "tehri": "वह", "salani": "वो", "rathwali": "वो"}
    },
    {
        "garhwali": "आधो",
        "hindi": "आधा",
        "english": "half",
        "pos": "adjective",
        "gender": "M",
        "category": "quantifiers",
        "dialect_variants": {"srinagariya": "आधो", "tehri": "आधा", "salani": "आधा", "rathwali": "आधो"}
    },
    {
        "garhwali": "पौणो",
        "hindi": "पौना (तीन चौथाई)",
        "english": "three quarters",
        "pos": "adjective",
        "gender": "M",
        "category": "quantifiers",
        "dialect_variants": {"srinagariya": "पौणो", "tehri": "पौना", "salani": "पौना", "rathwali": "पौणो"}
    },
    {
        "garhwali": "दुगूणो",
        "hindi": "दोगुना",
        "english": "double / twice as much",
        "pos": "adjective",
        "gender": "M",
        "category": "quantifiers",
        "dialect_variants": {"srinagariya": "दुगूणो", "tehri": "दुगुना", "salani": "दोगुना", "rathwali": "दुगूणो"}
    },

    # ==================== 2. LITERARY PROSE & EMOTIONAL STATES (UOU CGL-102 & 103) ====================
    {
        "garhwali": "निसोह",
        "hindi": "निराधार / असहाय / लाचार",
        "english": "helpless / destitute / without support",
        "pos": "adjective",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "निसोह", "tehri": "लाचार", "salani": "बेबस", "rathwali": "निसोह"}
    },
    {
        "garhwali": "हिया-फूटणु",
        "hindi": "हृदय विदीर्ण होना / अत्यधिक दुःख होना",
        "english": "to have one's heart broken by intense grief",
        "pos": "verb",
        "gender": "N",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "हिया-फूटणु", "tehri": "दिल-टूटना", "salani": "छाती-फटना", "rathwali": "हिया-फूटणु"}
    },
    {
        "garhwali": "अंसुवा",
        "hindi": "आंसू / अश्रु",
        "english": "teardrops",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "अंसुवा", "tehri": "आंसू", "salani": "आंसू", "rathwali": "अंसुवा"}
    },
    {
        "garhwali": "मुसक्याण",
        "hindi": "मंद मुस्कान",
        "english": "gentle smile",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "मुसक्याण", "tehri": "मुस्कान", "salani": "हंसी", "rathwali": "मुसक्याण"}
    },
    {
        "garhwali": "झुरणु",
        "hindi": "चिंता में घुलना / विरह में सूखना",
        "english": "to pine away in sorrow or separation",
        "pos": "verb",
        "gender": "N",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "झुरणु", "tehri": "घुलना", "salani": "झुरना", "rathwali": "झुरणु"}
    },
    {
        "garhwali": "बिलाप",
        "hindi": "विलाप / रोना-धोना",
        "english": "lamentation / mourning wail",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "बिलाप", "tehri": "विलाप", "salani": "मातम", "rathwali": "बिलाप"}
    },
    {
        "garhwali": "कसकस",
        "hindi": "मन की कसक / टीस",
        "english": "pang of longing / lingering heartache",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "कसकस", "tehri": "कसक", "salani": "टीस", "rathwali": "कसकस"}
    },
    {
        "garhwali": "उमंग",
        "hindi": "हर्षोल्लास / उत्साह",
        "english": "joyous enthusiasm / festive zeal",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "उमंग", "tehri": "उत्साह", "salani": "उमंग", "rathwali": "उमंग"}
    },
    {
        "garhwali": "रंग-बिरंगो",
        "hindi": "रंग-बिरंगा / बहुरंगी",
        "english": "multi-colored / colorful",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "रंग-बिरंगो", "tehri": "रंगीला", "salani": "रंग-बिरंगा", "rathwali": "रंग-बिरंगो"}
    },
    {
        "garhwali": "सपिनो",
        "hindi": "स्वप्न / सपना",
        "english": "dream",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "सपिनो", "tehri": "सपना", "salani": "सपना", "rathwali": "सपिणो"}
    },
    {
        "garhwali": "जागणु",
        "hindi": "नींद से जागना",
        "english": "to wake up / awaken",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "जागणु", "tehri": "जागना", "salani": "जागना", "rathwali": "जागणु"}
    },

    # ==================== 3. HIMALAYAN TOPOGRAPHY & NATURE (UOU & Upreti 1894) ====================
    {
        "garhwali": "घाम",
        "hindi": "तेज धूप",
        "english": "bright mountain sunshine / sunny weather",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "घाम", "tehri": "धूप", "salani": "घाम", "rathwali": "घाम"}
    },
    {
        "garhwali": "कुहाड़",
        "hindi": "पहाड़ों में छाने वाला घना कोहरा",
        "english": "dense mountain fog / valley mist",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कुहाड़", "tehri": "कुहासा", "salani": "धुंध", "rathwali": "कुहाड़"}
    },
    {
        "garhwali": "पाळो",
        "hindi": "सर्दियों का पाला / तुषार",
        "english": "winter ground frost / rime ice",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "पाळो", "tehri": "पाला", "salani": "पाला", "rathwali": "पाळो"}
    },
    {
        "garhwali": "हिंवल-गौंत",
        "hindi": "पवित्र हिमनदी का ठंडा जल",
        "english": "sacred glacial meltwater stream",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिंवल-गौंत", "tehri": "बर्फानी-पानी", "salani": "ठंडा-पानी", "rathwali": "हिंवल-गौंत"}
    },
    {
        "garhwali": "डांडी-कांडी",
        "hindi": "ऊंचे पहाड़ की चोटियां और जंगल",
        "english": "high mountain ridges and forested crests",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "डांडी-कांडी", "tehri": "पहाड़-जंगल", "salani": "धार-जंगल", "rathwali": "डांडी-कांडी"}
    },
    {
        "garhwali": "सैंण",
        "hindi": "पहाड़ के बीच समतल चौरस मैदान",
        "english": "flat alpine meadow plateau / plain in the hills",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "सैंण", "tehri": "मैदान", "salani": "सैंण", "rathwali": "सैंण"}
    },
    {
        "garhwali": "बगड़",
        "hindi": "पहाड़ी नदी का रेतीला व पथरीला किनारा",
        "english": "sandy or pebbly riverbank beach in mountain valley",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बगड़", "tehri": "रेत", "salani": "किनारा", "rathwali": "बगड़"}
    },
    {
        "garhwali": "घाट",
        "hindi": "नदी का स्नान-स्थल / घाट",
        "english": "river bathing steps / sacred river ghat",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "घाट", "tehri": "घाट", "salani": "पत्तण", "rathwali": "घाट"}
    },
    {
        "garhwali": "बटौही",
        "hindi": "पहाड़ी राही / मुसाफिर / पथिक",
        "english": "mountain traveler / wayfarer on hill trails",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "बटौही", "tehri": "राही", "salani": "बटोही", "rathwali": "बटौही"}
    },
    {
        "garhwali": "डगर",
        "hindi": "पहाड़ी रास्ता / पगडंडी",
        "english": "mountain pathway / walking track",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "डगर", "tehri": "रास्ता", "salani": "डगर", "rathwali": "डगर"}
    },

    # ==================== 4. FOLK CUSTOMS & RITUAL OBJECTS (Oakley-Gairola 1935) ====================
    {
        "garhwali": "औल्या",
        "hindi": "मौसम व ओलों की भविष्यवाणी करने वाला पारंपरिक ज्ञानी",
        "english": "traditional village weather forecaster who predicts hailstorms",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "औल्या", "tehri": "ज्ञानी", "salani": "पंडित", "rathwali": "औल्या"}
    },
    {
        "garhwali": "पंचामृत",
        "hindi": "दूध, दही, घी, शहद व शर्करा का पवित्र मिश्रण",
        "english": "five sacred nectars mixture for deity libation",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "पंचामृत", "tehri": "पंचामृत", "salani": "चरणामृत", "rathwali": "पंचामृत"}
    },
    {
        "garhwali": "बटलोही",
        "hindi": "दाल व भात पकाने का पारंपरिक पीतल का गोल पात्र",
        "english": "traditional spherical brass cooking cauldron",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "बटलोही", "tehri": "बटोही", "salani": "पतीली", "rathwali": "बटलोही"}
    },
    {
        "garhwali": "कनस्तर",
        "hindi": "घी व तेल रखने का टीन का बड़ा पीपा",
        "english": "large tin canister for storing clarified butter (ghee)",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "कनस्तर", "tehri": "टीन", "salani": "कनस्तर", "rathwali": "कनस्तर"}
    },
    {
        "garhwali": "डबलो",
        "hindi": "मसाले रखने का छोटा गोल डिब्बा",
        "english": "small round spice box",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "डबलो", "tehri": "डब्बी", "salani": "डिबिया", "rathwali": "डबळो"}
    },
    {
        "garhwali": "दिवाली",
        "hindi": "मिट्टी का छोटा दीपक (दीया)",
        "english": "small clay oil lamp",
        "pos": "noun",
        "gender": "F",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "दिवाली", "tehri": "दीया", "salani": "दीपक", "rathwali": "दिवाळी"}
    },
    {
        "garhwali": "धियाण",
        "hindi": "मायके आई हुई विवाहित बेटी / बहन",
        "english": "married daughter visiting her maternal home (Mait)",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "धियाण", "tehri": "ध्याणी", "salani": "बेटी", "rathwali": "धियाण"}
    },
    {
        "garhwali": "रौंत्याल",
        "hindi": "हर्षोल्लास से भरा / उत्सवप्रिय व्यक्ति",
        "english": "cheerful / merry-making / celebratory person",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "रौंत्याल", "tehri": "रंगीला", "salani": "हंसमुख", "rathwali": "रौंत्याळ"}
    },
    {
        "garhwali": "भंकोरी",
        "hindi": "मंदिरों में बजने वाला लंबा पीतल का तुरही बाजा",
        "english": "long brass ceremonial temple trumpet (Bhankora)",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भंकोरी", "tehri": "भंकोरा", "salani": "तुरही", "rathwali": "भंकोरी"}
    },
    {
        "garhwali": "घंडियाल",
        "hindi": "मंदिर का बड़ा पीतल का घंटा",
        "english": "large bronze temple bell / gong",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "घंडियाल", "tehri": "घंटा", "salani": "घंट", "rathwali": "घंडियाळ"}
    },
    {
        "garhwali": "पिठाई",
        "hindi": "माथे पर लगाया जाने वाला अक्षत व रोली का तिलक",
        "english": "sacred red vermilion and unbroken rice forehead mark (Pithya)",
        "pos": "noun",
        "gender": "F",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "पिठाई", "tehri": "पिठ्या", "salani": "रोली", "rathwali": "पिठाई"}
    },
    {
        "garhwali": "अछरी",
        "hindi": "हिमालयी बुग्यालों में विचरने वाली दिव्य अप्सराएं (आंछरी)",
        "english": "ethereal celestial fairies of the high alpine bugyals",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "अछरी", "tehri": "आंछरी", "salani": "अप्सरा", "rathwali": "अछरी"}
    },
    {
        "garhwali": "मंडाण",
        "hindi": "पांडव नृत्य व ढोल-दमाऊं का सामूहिक गोलाकार नृत्य",
        "english": "circular sacred trance dance accompanied by folk drums",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "मंडाण", "tehri": "मंडाण", "salani": "घेर", "rathwali": "मंडाण"}
    },
    {
        "garhwali": "थड्या",
        "hindi": "वसंत ऋतु में आंगन में गाया जाने वाला सामूहिक थड़िया गीत",
        "english": "traditional spring courtyard standing circle song",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "थड्या", "tehri": "थड़िया", "salani": "गीत", "rathwali": "थड्या"}
    },
    {
        "garhwali": "चौंफुला",
        "hindi": "स्त्री-पुरुषों का प्रसिद्ध श्रृंगारिक सवाल-जवाब लोकनृत्य",
        "english": "romantic four-stanza conversational folk dance of Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "चौंफुला", "tehri": "चौंफुला", "salani": "झुमैलो", "rathwali": "चौंफुळा"}
    },
    {
        "garhwali": "बांद",
        "hindi": "पहाड़ी सुंदर युवती / रूपवती कन्या",
        "english": "graceful young mountain village maiden",
        "pos": "noun",
        "gender": "F",
        "category": "people",
        "dialect_variants": {"srinagariya": "बांद", "tehri": "कलेऊ", "salani": "कन्या", "rathwali": "बांद"}
    },
    {
        "garhwali": "छैला",
        "hindi": "बांका पहाड़ी नौजवान / प्रियतम",
        "english": "handsome, dashing hill youth / beloved",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "छैला", "tehri": "छैल", "salani": "छैला", "rathwali": "छैळा"}
    },
    {
        "garhwali": "गौंंत्यार",
        "hindi": "ग्रामवासी / एक ही गांव का निवासी",
        "english": "fellow villager from the same ancestral hamlet",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "गौंंत्यार", "tehri": "गांववासी", "salani": "पड़ोसी", "rathwali": "गौंंत्यार"}
    },
    {
        "garhwali": "सयाणा",
        "hindi": "गांव का प्रतिष्ठित वयोवृद्ध मुखिया / पंच",
        "english": "respected village elder / traditional council arbiter",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "सयाणा", "tehri": "सयाना", "salani": "मुखिया", "rathwali": "सयाणा"}
    },
    {
        "garhwali": "पाहुणा",
        "hindi": "घर आया हुआ अतिथि / मेहमान",
        "english": "honored household guest / visitor",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "पाहुणा", "tehri": "मेहमान", "salani": "पाहुना", "rathwali": "पाहुणा"}
    },
    {
        "garhwali": "मैत",
        "hindi": "विवाहित स्त्री का मायका (माता-पिता का घर)",
        "english": "married woman's maternal parental village and home",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मैत", "tehri": "मायका", "salani": "मैत", "rathwali": "मैत"}
    },
    {
        "garhwali": "सौरास",
        "hindi": "ससुराल / पति का घर",
        "english": "in-laws' house / marital home of bride",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "सौरास", "tehri": "ससुराल", "salani": "सौरास", "rathwali": "सौरास"}
    },
    {
        "garhwali": "नथुली",
        "hindi": "गढ़वाल की प्रसिद्ध बड़ी सोने की नथ (टिहरी नथ)",
        "english": "traditional large circular gold nose ring of Garhwal",
        "pos": "noun",
        "gender": "F",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "नथुली", "tehri": "नथ", "salani": "नथुली", "rathwali": "नथुळी"}
    },
    {
        "garhwali": "गुलोबंद",
        "hindi": "गले में सटकर पहना जाने वाला सोने का चौकोर हार",
        "english": "traditional velvet-backed gold choker necklace",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "गुलोबंद", "tehri": "गुलूबंद", "salani": "कंठी", "rathwali": "गुळोबंद"}
    },
    {
        "garhwali": "पिछौड़ा",
        "hindi": "विवाह व मांगलिक कार्यों में पहना जाने वाला पीला-लाल उत्तरीय",
        "english": "ceremonial auspicious saffron-red dyed veil worn at weddings",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "पिछौड़ा", "tehri": "रंग्वाली", "salani": "दुपट्टा", "rathwali": "पिछौड़ा"}
    },
    {
        "garhwali": "हंसुली",
        "hindi": "चांदी का भारी ठोस हंसियानुमा कण्ठहार",
        "english": "heavy solid silver torque collar necklace",
        "pos": "noun",
        "gender": "F",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "हंसुली", "tehri": "हँसुली", "salani": "हंसुली", "rathwali": "हंसुळी"}
    },
    {
        "garhwali": "धगुला",
        "hindi": "चांदी के भारी नक्काशीदार कड़े",
        "english": "heavy engraved silver wrist bracelets",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "धगुला", "tehri": "धगुले", "salani": "कड़ा", "rathwali": "धगुळा"}
    },
    {
        "garhwali": "पिस्यूं-लूण",
        "hindi": "सिलबट्टे पर पिसा हुआ पहाड़ी हरा नमक (जीरा, लहसुन, धनिया युक्त)",
        "english": "traditional rock salt stone-ground with roasted cumin, garlic, and mint",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "पिस्यूं-लूण", "tehri": "पिसा-नमक", "salani": "लूण", "rathwali": "पिस्यूं-ळूण"}
    },
    {
        "garhwali": "जख्या",
        "hindi": "पहाड़ी तड़के का प्रसिद्ध जंगली बीज (क्लियोम विस्कोसा)",
        "english": "wild crunchy Himalayan tempering seed (Cleome viscosa)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "जख्या", "tehri": "जख्या", "salani": "जख्या", "rathwali": "जख्या"}
    },
    {
        "garhwali": "गंधरायण",
        "hindi": "दाल छौंकने की सुगंधित जंगली जड़ी (एंजेलिका)",
        "english": "high-altitude aromatic digestive herb root (Angelica glauca)",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "गंधरायण", "tehri": "गंधरायण", "salani": "गंधरायण", "rathwali": "गंधरायण"}
    },
    {
        "garhwali": "भंगजीरा",
        "hindi": "चटनी में प्रयुक्त होने वाले सुवासित बीज (पेरिला)",
        "english": "wild Himalayan perilla seeds used in roasted chutney",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "भंगजीरा", "tehri": "भंगजीरा", "salani": "भंगजीरा", "rathwali": "भंगजीरा"}
    },
    {
        "garhwali": "काफ़ुली",
        "hindi": "पालक व मेथी को चावल के आलन के साथ पकाया गया गाढ़ा साग",
        "english": "signature Garhwali thick spinach and fenugreek green gravy",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "काफ़ुली", "tehri": "काफली", "salani": "साग", "rathwali": "काफ़ुळी"}
    },
    {
        "garhwali": "चैनसूं",
        "hindi": "काले भट्ट को भूनकर और सिलबट्टे पर पीसकर बनी गाढ़ी दाल",
        "english": "traditional aromatic roasted black soybean gravy",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "चैनसूं", "tehri": "चैंसु", "salani": "चैनसूं", "rathwali": "चैनसूं"}
    },
    {
        "garhwali": "थटवाणी",
        "hindi": "विभिन्न दालों को लोहे की कड़ाही में धीमी आंच पर पकाकर बना सूप",
        "english": "iron-pot slow-simmered mixed lentil stew",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "थटवाणी", "tehri": "फाबा", "salani": "दाल-रस", "rathwali": "थटवाणी"}
    },
    {
        "garhwali": "झोली",
        "hindi": "मट्ठे और छाछ में पकाई गई स्वादिष्ट पहाड़ी कढ़ी",
        "english": "curd and buttermilk curry with turmeric and fenugreek",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "झोली", "tehri": "कढ़ी", "salani": "झोली", "rathwali": "झोळी"}
    },
    {
        "garhwali": "बाड़ी",
        "hindi": "मंडुवे (कोदा) के आटे को खौलते पानी में मथकर बनाया गया व्यंजन",
        "english": "finger millet cooked polenta paste served with hot ghee",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "बाड़ी", "tehri": "बाड़ी", "salani": "बाड़ी", "rathwali": "बाळी"}
    },
    {
        "garhwali": "सिंगोरी",
        "hindi": "मालू के पत्ते में लपेटी गई खोया की प्रसिद्ध मिठाई",
        "english": "cone-shaped sweet confection wrapped in aromatic malu oak leaves",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "सिंगोरी", "tehri": "सिंगोड़ी", "salani": "मिठाई", "rathwali": "सिंगोरी"}
    },
    {
        "garhwali": "अरसा",
        "hindi": "भीगे चावल के आटे और गुड़ की चाशनी से बना विवाह का मांगलिक पकवान",
        "english": "ceremonial wedding sweet cake made from rice flour and jaggery syrup",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "अरसा", "tehri": "अरसे", "salani": "अनरसा", "rathwali": "अरसा"}
    },
    {
        "garhwali": "रोट",
        "hindi": "देवी-देवताओं को चढ़ाई जाने वाली मोटी मीठी रोट",
        "english": "thick sweet ceremonial sacred bread offered to deities",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "रोट", "tehri": "रोट", "salani": "रोटा", "rathwali": "रोट"}
    }
]

added = 0
enriched = 0

for item in UOU_FOLKLORE_WORDS:
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

print(f"UOU & Folklore mining added: {added}")
print(f"Enriched: {enriched}")
print(f"Total word count now: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved words to {WORDS_PATH}")
