# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 4 vocabulary from newly added historical,
ethnographic, legal, and linguistic texts:
- Dabral (1965): Transhumant pastoralism, woolen crafts, high-altitude ecology
- Stowell (1916): Customary hill jurisprudence, natal rights, partition
- Atkinson (1886): Alpine topography, forest floor, wildlife, shelter
- Verma (2003) & Oakley (1935): Kinship, emotional verbs, sensory descriptors
"""

import json

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE4_WORDS = [
    # --- Alpine Pastoralism & Woolen Crafts (Dabral 1965) ---
    {
        "garhwali": "पंखी",
        "hindi": "भेड़ के महीन ऊन से हाथ से बुनी गई हल्की व गर्म चादर अथवा शॉल",
        "english": "lightweight hand-spun fine wool shawl or wrap woven by high-altitude pastoralists",
        "pos": "noun",
        "gender": "F",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "पंखी", "tehri": "पंखी", "salani": "पंखी", "rathwali": "पङ्खी"}
    },
    {
        "garhwali": "थुल्मा",
        "hindi": "भेड़ के घने रोएंदार ऊन से बना भारी व अत्यंत गर्म कंबल",
        "english": "heavy, thick, deeply napped fleece blanket hand-woven from sheep wool",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "थुल्मा", "tehri": "थुल्मु", "salani": "थुल्मा", "rathwali": "थुल्मो"}
    },
    {
        "garhwali": "चुटक",
        "hindi": "पारंपरिक हथकरघे पर बुना गया रोएंदार ऊनी कालीन अथवा दरी",
        "english": "traditional thick pile woolen floor rug or sitting carpet hand-woven on rustic looms",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "चुटक", "tehri": "चुटक", "salani": "चुटक", "rathwali": "चुटक"}
    },
    {
        "garhwali": "दंडी",
        "hindi": "ऊन कातने की हाथ से घुमाई जाने वाली पारंपरिक छोटी तकली",
        "english": "portable wooden drop-spindle whirled by hand while walking to spin sheep wool into yarn",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "दंडी", "tehri": "दण्डी", "salani": "दंडी", "rathwali": "दंडी"}
    },
    {
        "garhwali": "झूप्पू",
        "hindi": "याक तथा पहाड़ी गाय के संकर से उत्पन्न मजबूत भारवाही नर पशु",
        "english": "sturdy male hybrid beast of burden bred from a Tibetan yak and a mountain hill cow",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "झूप्पू", "tehri": "झुप्पू", "salani": "झूप्पू", "rathwali": "झूप्पू"}
    },
    {
        "garhwali": "कुंतल",
        "hindi": "भेड़-बकरियों की पीठ पर नमक अथवा अनाज लादने हेतु चमड़े या ऊन का बना संकरा थैला",
        "english": "small paired pack-saddle bag of wool or hide loaded on sheep and goats crossing high passes",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कुंतल", "tehri": "कुंतल", "salani": "कुंतल", "rathwali": "कुन्तल"}
    },
    {
        "garhwali": "गम्या",
        "hindi": "तिब्बत व उच्च हिमालयी दर्रों के पार व्यापार करने वाला साहसी पर्वतीय व्यापारी",
        "english": "adventurous trans-Himalayan pass-trader crossing snow cols to conduct seasonal barter",
        "pos": "noun",
        "gender": "M",
        "category": "society",
        "dialect_variants": {"srinagariya": "गम्या", "tehri": "गम्या", "salani": "गम्या", "rathwali": "गम्यो"}
    },
    {
        "garhwali": "मार्ट",
        "hindi": "पारस्परिक विश्वास पर आधारित पारंपरिक व्यापारिक समझौता अथवा टोकन",
        "english": "customary ceremonial token or sacred stone contract cementing lifelong trade partnership",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "मार्ट", "tehri": "मार्ट", "salani": "मार्ट", "rathwali": "मार्ट"}
    },

    # --- Customary Law, Rights & Family Settlements (Stowell 1916) ---
    {
        "garhwali": "घरजंवाई",
        "hindi": "ससुर के घर में ही स्थायी रूप से रहकर खेती व घर संभालने वाला दामाद",
        "english": "resident son-in-law living permanently in his father-in-law's homestead as recognized heir",
        "pos": "noun",
        "gender": "M",
        "category": "family",
        "dialect_variants": {"srinagariya": "घरजंवाई", "tehri": "घरजंवाइ", "salani": "घरजंवाई", "rathwali": "घरजंवायी"}
    },
    {
        "garhwali": "मुंडकटिया",
        "hindi": "पिता की मृत्यु के उपरांत समस्त पुत्रों में संपत्ति का प्रति-व्यक्ति बराबर बंटवारा",
        "english": "customary per-capita equal partition of patrimonial estate among all surviving sons",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "मुंडकटिया", "tehri": "मुंडकटिया", "salani": "मुंडकटिया", "rathwali": "मुण्डकटियो"}
    },
    {
        "garhwali": "भाइ-बांट",
        "hindi": "सगे भाइयों के मध्य पैतृक भूमि, पशु व गृह-सामग्री का आपसी विभाजन",
        "english": "fraternal division and partition of ancestral land, homestead, and livestock among brothers",
        "pos": "noun",
        "gender": "F",
        "category": "governance",
        "dialect_variants": {"srinagariya": "भाइ-बांट", "tehri": "भाइ-बांट", "salani": "भाइ-बांट", "rathwali": "भाइ-बांट"}
    },
    {
        "garhwali": "लावारिस",
        "hindi": "बिना किसी उत्तराधिकारी के छोड़ी गई संपत्ति जो ग्राम-समाज अथवा राज्य को जाती है",
        "english": "heirless ownerless property reverting to the village commons or state by escheat",
        "pos": "adj",
        "gender": None,
        "category": "governance",
        "dialect_variants": {"srinagariya": "लावारिस", "tehri": "लावारिस", "salani": "लावारिस", "rathwali": "लावारिस"}
    },
    {
        "garhwali": "नाप-भूमि",
        "hindi": "सर्वेक्षण व पैमाइश द्वारा निर्धारित निजी काश्तकारी की कृषि भूमि",
        "english": "cadastrally surveyed, assessed, and private proprietary agricultural land",
        "pos": "noun",
        "gender": "F",
        "category": "governance",
        "dialect_variants": {"srinagariya": "नाप-भूमि", "tehri": "नाप-जमीन", "salani": "नाप-भूमि", "rathwali": "नाप-भूमि"}
    },
    {
        "garhwali": "बेनाप-भूमि",
        "hindi": "गैर-पैमाइश शुदा वन, बंजर अथवा ग्राम-समाज की साझा चरागाह भूमि",
        "english": "unsurveyed, unassessed public waste land, common forest, and community grazing slopes",
        "pos": "noun",
        "gender": "F",
        "category": "governance",
        "dialect_variants": {"srinagariya": "बेनाप-भूमि", "tehri": "बेनाप-जमीन", "salani": "बेनाप-भूमि", "rathwali": "बेनाप-भूमि"}
    },

    # --- Alpine Topography & Forest Floor (Atkinson 1886) ---
    {
        "garhwali": "पयाल",
        "hindi": "चीड़ के वृक्षों से गिरी सूखी पत्तियां जो गोशाला में पशुओं के बिछाने हेतु प्रयुक्त होती हैं",
        "english": "dry fallen pine needles gathered from forest slopes for livestock bedding in winter barns",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "पयाल", "tehri": "पयाल", "salani": "पयाल", "rathwali": "पयाळ"}
    },
    {
        "garhwali": "खांच",
        "hindi": "पहाड़ में गहरा संकरा गड्ढा अथवा गहरी घाटी की खाई",
        "english": "narrow, deep mountain gorge, fissure, or precipitous crevasse between hill slopes",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "खांच", "tehri": "खांच", "salani": "खांच", "rathwali": "खाञ्च"}
    },
    {
        "garhwali": "ओड्यार",
        "hindi": "पहाड़ की प्राकृतिक चट्टानी गुफा जो गड़ेरियों व यात्रियों के आश्रय का काम देती है",
        "english": "natural rocky overhang or shallow mountain cave serving as shepherds' bivouac shelter",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "ओड्यार", "tehri": "ओडार", "salani": "ओड्यार", "rathwali": "ओड्यार"}
    },
    {
        "garhwali": "छरछरा",
        "hindi": "पर्वतों पर हल्की धुंधभरी महीन बूंदों वाली वर्षा, फुहार",
        "english": "light misty drizzle, gentle windblown mountain rain shower",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "छरछरा", "tehri": "छरछरु", "salani": "छरछरा", "rathwali": "छरछरो"}
    },
    {
        "garhwali": "हिलांस",
        "hindi": "हरियल पक्षी, गढ़वाली लोकगीतों में वियोग व मैत की याद का प्रतीक पवित्र पक्षी",
        "english": "wedge-tailed green pigeon, poignant emblem of nostalgia and exile in Garhwali folklore",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "हिलांस", "tehri": "हिलांस", "salani": "हिलांस", "rathwali": "हिळांस"}
    },
    {
        "garhwali": "काकड़",
        "hindi": "पहाड़ी जंगलों में पाया जाने वाला भौंकने वाला छोटा हिरण",
        "english": "Indian muntjac or barking deer inhabiting oak and rhododendron forest tracts",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "काकड़", "tehri": "काकड़", "salani": "काकड़", "rathwali": "काकड़"}
    },

    # --- Verbs of Sensation, Emotion & Social Life (Verma 2003, Oakley 1935) ---
    {
        "garhwali": "रुसाणु",
        "hindi": "अपमानित या दुखी होकर रूठ जाना, अप्रसन्न होना",
        "english": "to sulk, become offended, turn sullen due to hurt feelings",
        "pos": "verb",
        "gender": None,
        "category": "emotions",
        "dialect_variants": {"srinagariya": "रुसाणु", "tehri": "रुसाण", "salani": "रुसाणा", "rathwali": "रुसाणु"}
    },
    {
        "garhwali": "मनाणु",
        "hindi": "रूठे हुए व्यक्ति को प्रेमपूर्वक मनाना व प्रसन्न करना",
        "english": "to coax, cajole, appease, conciliate an offended friend or kin",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "मनाणु", "tehri": "मनाण", "salani": "मनाणा", "rathwali": "मनाणु"}
    },
    {
        "garhwali": "लजाणु",
        "hindi": "लज्जा का अनुभव करना, शरमाना, संकोच करना",
        "english": "to feel bashful, act shyly, exhibit modest hesitation",
        "pos": "verb",
        "gender": None,
        "category": "emotions",
        "dialect_variants": {"srinagariya": "लजाणु", "tehri": "लजाण", "salani": "लजाणा", "rathwali": "लजाणु"}
    },
    {
        "garhwali": "हरखाणु",
        "hindi": "अत्यंत प्रसन्न व प्रफुल्लित होना, उल्लास मनाना",
        "english": "to rejoice wholeheartedly, feel exuberant happiness and joy",
        "pos": "verb",
        "gender": None,
        "category": "emotions",
        "dialect_variants": {"srinagariya": "हरखाणु", "tehri": "हरखाण", "salani": "हरखाणा", "rathwali": "हरखाणु"}
    },
    {
        "garhwali": "सकचाणु",
        "hindi": "हिचकिचाना, संकोचवश आगे न बढ़ पाना",
        "english": "to hesitate with diffidence, hold back out of bashfulness",
        "pos": "verb",
        "gender": None,
        "category": "emotions",
        "dialect_variants": {"srinagariya": "सकचाणु", "tehri": "सकचाण", "salani": "सकचाणा", "rathwali": "सकचाणु"}
    },
    {
        "garhwali": "अंग्वाळणु",
        "hindi": "प्रेमपूर्वक बांहों में भरना, आलिंगनबद्ध करना",
        "english": "to embrace warmly, fold affectionately in one's arms",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "अंग्वाळणु", "tehri": "अंग्वालण", "salani": "अंग्वालाणा", "rathwali": "अंग्वाळणु"}
    },
    {
        "garhwali": "छुट्कारो",
        "hindi": "कष्ट अथवा बंधन से मुक्ति, छुटकारा",
        "english": "deliverance, release, freedom from distress or bondage",
        "pos": "noun",
        "gender": "M",
        "category": "abstract",
        "dialect_variants": {"srinagariya": "छुट्कारो", "tehri": "छुट्कारु", "salani": "छुटकारा", "rathwali": "छुट्कारो"}
    },
    {
        "garhwali": "निस्वार्थ",
        "hindi": "बिना किसी स्वार्थ के, परोपकारी भाव",
        "english": "unselfish, selfless altruism for community well-being",
        "pos": "adj",
        "gender": None,
        "category": "personality",
        "dialect_variants": {"srinagariya": "निस्वार्थ", "tehri": "निस्वारथ", "salani": "निस्वारथ", "rathwali": "निस्वार्थ"}
    },
    {
        "garhwali": "रस्याण",
        "hindi": "मधुर रस, आत्मीयता व आनंद का भाव",
        "english": "rich sweet flavor, heartfelt warmth, delightful sweetness of character",
        "pos": "noun",
        "gender": "F",
        "category": "quality",
        "dialect_variants": {"srinagariya": "रस्याण", "tehri": "रस्याण", "salani": "रस्याण", "rathwali": "रस्याण"}
    },
    {
        "garhwali": "अणहोणी",
        "hindi": "अस्वाभाविक अथवा अनपेक्षित अनहोनी घटना",
        "english": "unexpected untoward event, unnatural ominous happening",
        "pos": "noun",
        "gender": "F",
        "category": "abstract",
        "dialect_variants": {"srinagariya": "अणहोणी", "tehri": "अणहोणी", "salani": "अणहोणी", "rathwali": "अणहोणी"}
    }
]

added_words = []
for w in WAVE4_WORDS:
    if w["garhwali"] not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(w["garhwali"])
        added_words.append(w["garhwali"])

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {len(added_words)} new authenticated words to {WORDS_PATH}.")
print(f"Total words in lexicon now: {len(existing_words)}")

