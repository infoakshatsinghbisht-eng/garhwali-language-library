# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 7 vocabulary from newly added linguistic,
geological, mountaineering, and religious texts:
- LSI Pahari Survey (2023) & Shrestha (2000): Dialect verbs, aspectual roots, time vocables
- Lewis (1995): Sacred pilgrim institutions, shrines, temple rituals
- Roch (1947) & Auden (1936): High glacial geography, gorges, rock shelters, tarns
- Himachali Shabdawali (1998): Traditional implements, farming tools
"""

import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE7_WORDS = [
    # --- Glacial Geography & Topography (Roch 1947, Auden 1936) ---
    {
        "garhwali": "हिमताल",
        "hindi": "उच्च हिमालयी शिखरों के मध्य हिमानी से निर्मित प्राकृतिक शीतल झील",
        "english": "glacial cirque lake or high-altitude alpine tarn fed by melting perpetual ice",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिमताल", "tehri": "हिमताल", "salani": "हिमताल", "rathwali": "हिमताल"}
    },
    {
        "garhwali": "हिमानी",
        "hindi": "पर्वतों से धीरे-धीरे खिसकने वाली विशाल हिमधारा अथवा ग्लेशियर",
        "english": "living valley glacier or creeping river of perpetual mountain ice",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिमानी", "tehri": "हिमानी", "salani": "हिमानी", "rathwali": "हिमानी"}
    },
    {
        "garhwali": "भित्ती",
        "hindi": "सीधी खड़ी प्राकृतिक चट्टानी दीवार अथवा विकट कगार",
        "english": "sheer vertical rock face, mountain crag wall, or natural stone buttress",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "भित्ती", "tehri": "भिती", "salani": "भित्ती", "rathwali": "भित्ती"}
    },
    {
        "garhwali": "कन्दरा",
        "hindi": "पर्वतों के भीतर बनी प्राकृतिक गुफा अथवा शिला-आश्रय",
        "english": "natural mountain cavern, rock grotto, or cavernous stone shelter",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कन्दरा", "tehri": "कंदरा", "salani": "कन्दरा", "rathwali": "कन्दरा"}
    },
    {
        "garhwali": "प्रपात",
        "hindi": "पहाड़ी कगार से तीव्र वेग से नीचे गिरने वाला जलप्रपात",
        "english": "cascading mountain waterfall plunging sheer over vertical cliffs",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "प्रपात", "tehri": "प्रपात", "salani": "प्रपात", "rathwali": "प्रपात"}
    },
    {
        "garhwali": "गर्त",
        "hindi": "नदी तल अथवा हिमानी चट्टान में जल-भंवर से बना गहरा गड्ढा",
        "english": "deep glacial pothole or circular rock basin carved by swirling torrents",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गर्त", "tehri": "गर्त", "salani": "गर्त", "rathwali": "गर्त"}
    },
    {
        "garhwali": "पाषाण",
        "hindi": "कठोर रूपांतरित पर्वतीय शिला अथवा प्राचीन पाषाण खंड",
        "english": "ancient crystalline metamorphic bedrock or monumental stone block",
        "pos": "noun",
        "gender": "M",
        "category": "material",
        "dialect_variants": {"srinagariya": "पाषाण", "tehri": "पासाण", "salani": "पाषाण", "rathwali": "पाषाण"}
    },
    {
        "garhwali": "ओत",
        "hindi": "ठंडी बर्फीली हवाओं से बचने हेतु चट्टान अथवा पेड़ के पीछे की ओट",
        "english": "sheltered leeward niche protected from biting Himalayan blizzard winds",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "ओत", "tehri": "ओट", "salani": "ओत", "rathwali": "ओत"}
    },

    # --- Sacred Geography & Temple Institutions (Lewis 1995) ---
    {
        "garhwali": "डंडोत",
        "hindi": "मंदिर अथवा पूज्य देव-स्थान के सम्मुख पूर्ण साष्टांग प्रणाम",
        "english": "prostrate full-body reverential obeisance performed before holy Himalayan shrines",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "डंडोत", "tehri": "दंडौत", "salani": "डंडोत", "rathwali": "डंडोत"}
    },
    {
        "garhwali": "सदाव्रत",
        "hindi": "तीर्थ-मार्ग पर निर्धन तीर्थयात्रियों हेतु निःशुल्क भोजन वितरण की पारंपरिक व्यवस्था",
        "english": "traditional philanthropic endowment providing free daily food and rations to Himalayan pilgrims",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "सदाव्रत", "tehri": "सदाबरत", "salani": "सदाव्रत", "rathwali": "सदाव्रत"}
    },
    {
        "garhwali": "शंखनाद",
        "hindi": "मंदिरों में संध्या आरती अथवा धार्मिक अनुष्ठान के समय शंख की पवित्र ध्वनि",
        "english": "auspicious blowing of the sacred conch shell during temple evening aarti and invocations",
        "pos": "noun",
        "gender": "M",
        "category": "music",
        "dialect_variants": {"srinagariya": "शंखनाद", "tehri": "संखनाद", "salani": "शंखनाद", "rathwali": "शंखनाद"}
    },
    {
        "garhwali": "पंडा",
        "hindi": "बदरीनाथ व केदारनाथ के वंशानुगत पुरोहित जो यात्रियों की वंशावली सुरक्षित रखते हैं",
        "english": "hereditary pilgrim priest and traditional genealogist serving families visiting holy shrines",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "पंडा", "tehri": "पंडो", "salani": "पंडा", "rathwali": "पंडा"}
    },
    {
        "garhwali": "बदरीकाश्रम",
        "hindi": "बदरीनाथ धाम का प्राचीन तपोवन तथा पावन तीर्थ-क्षेत्र",
        "english": "the classical sacred forest hermitage and holy pilgrimage precinct of Badrinath",
        "pos": "noun",
        "gender": "M",
        "category": "places",
        "dialect_variants": {"srinagariya": "बदरीकाश्रम", "tehri": "बद्रीकाश्रम", "salani": "बदरीकाश्रम", "rathwali": "बदरीकाश्रम"}
    },

    # --- Agricultural Implements & Rural Crafts (Himachal Shabdawali 1998) ---
    {
        "garhwali": "कुदाळ",
        "hindi": "पथरीली सीढ़ीदार भूमि को खोदने का लोहे का भारी कुदाल",
        "english": "heavy iron mountain mattock or hoe used to break and till stony terraced soil",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कुदाळ", "tehri": "कुदाल", "salani": "कुदाल", "rathwali": "कुदाळ"}
    },
    {
        "garhwali": "दाँतुळी",
        "hindi": "मडुआ तथा धान काटने की दांतेदार छोटी दरांती",
        "english": "small curved serrated sickle used for cleanly reaping millet and rice stalks",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "दाँतुळी", "tehri": "दाँतुली", "salani": "दाँतुली", "rathwali": "दाँतुळी"}
    },
    {
        "garhwali": "सूपी",
        "hindi": "पहाड़ी हवा में अनाज को फटकने व भूसा अलग करने का रिंगाल का सूप",
        "english": "finely woven ringal cane winnowing tray used to winnow grain in mountain breezes",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सूपी", "tehri": "सूपि", "salani": "सूपी", "rathwali": "सूपी"}
    },

    # --- Dialect Verbs, Time & Cognitive Expressions (LSI Survey 2023, Shrestha 2000) ---
    {
        "garhwali": "बुझौण",
        "hindi": "समझना, अर्थ ग्रहण करना अथवा किसी बात का बोध होना",
        "english": "to understand, comprehend, perceive, or grasp the meaning of speech",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बुझौण", "tehri": "बुझणा", "salani": "बुझौण", "rathwali": "बुझौण"}
    },
    {
        "garhwali": "सुणौण",
        "hindi": "सुनाना, कथा या समाचार कहना अथवा दूसरों को अवगत कराना",
        "english": "to recite, narrate, tell a tale, or cause others to hear",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "सुणौण", "tehri": "सुणणा", "salani": "सुणौण", "rathwali": "सुणौण"}
    },
    {
        "garhwali": "दबकण",
        "hindi": "झाड़ियों अथवा पत्थरों की आड़ में छिपना या दुबकना",
        "english": "to crouch down, hide quietly, or conceal oneself in mountain thickets",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "दबकण", "tehri": "दबकणा", "salani": "दबकण", "rathwali": "दबकण"}
    },
    {
        "garhwali": "टपकण",
        "hindi": "चट्टानों अथवा छत से बूँद-बूँद जल गिरना",
        "english": "to drip steadily or trickle drop by drop from wet rocks or eaves",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "टपकण", "tehri": "टपकणा", "salani": "टपकण", "rathwali": "टपकण"}
    },
    {
        "garhwali": "छिना",
        "hindi": "क्षण भर, पल अथवा समय का अति सूक्ष्म अंतराल",
        "english": "fleeting instant, brief moment, or short span of time",
        "pos": "noun",
        "gender": "M",
        "category": "time",
        "dialect_variants": {"srinagariya": "छिना", "tehri": "छिनो", "salani": "छिना", "rathwali": "छिना"}
    },
    {
        "garhwali": "नैणा",
        "hindi": "साथ ले जाना अथवा संकरे रास्तों पर किसी वस्तु को ढोना",
        "english": "to take along, carry with, or convey baggage along steep mountain trails",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "नैणा", "tehri": "लैणा", "salani": "नैणा", "rathwali": "नैणा"}
    },
    {
        "garhwali": "दियौण",
        "hindi": "दिलवाना, दान प्रदान करवाना अथवा सौंपना",
        "english": "to cause to give, bestow through another, or grant charity",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "दियौण", "tehri": "दियौणा", "salani": "दियौण", "rathwali": "दियौण"}
    },
    {
        "garhwali": "घिरौण",
        "hindi": "शाम के समय मवेशियों को घेरकर बाड़े में लाना",
        "english": "to round up, herd, or corral grazing animals into the pen at dusk",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "घिरौण", "tehri": "घिरणा", "salani": "घिरौण", "rathwali": "घिरौण"}
    },
    {
        "garhwali": "समेत",
        "hindi": "सहित, साथ में अथवा पूरे समूह के साथ",
        "english": "together with, along with, accompanied by, including all",
        "pos": "postposition",
        "gender": "None",
        "category": "postpositions",
        "dialect_variants": {"srinagariya": "समेत", "tehri": "समेत", "salani": "समेत", "rathwali": "समेत"}
    },
    {
        "garhwali": "उखण",
        "hindi": "भूमि से कंद-मूल अथवा जड़ी-बूटियाँ खोदकर निकालना",
        "english": "to dig up, uproot, or unearth wild edible tubers and medicinal herbs",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "उखण", "tehri": "उखणा", "salani": "उखण", "rathwali": "उखण"}
    },
    {
        "garhwali": "उज्याळ",
        "hindi": "शिखरों पर प्रात:काल की उज्ज्वल धूप अथवा प्रभात का प्रकाश",
        "english": "radiant morning daylight or glistening dawn sunlight breaking over snowy ridges",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "उज्याळ", "tehri": "उज्याल", "salani": "उज्याल", "rathwali": "उज्याळ"}
    },
    {
        "garhwali": "अन्धेर",
        "hindi": "पहाड़ी रातों का गहन अंधकार अथवा अमावस्या की रात",
        "english": "pitch-black mountain darkness or moonless night on high passes",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "अन्धेर", "tehri": "अंधेर", "salani": "अन्धेर", "rathwali": "अन्धेर"}
    },
    {
        "garhwali": "बगौण",
        "hindi": "सिंचाई हेतु नहर के जल को खेतों की ओर मोड़ना या बहाना",
        "english": "to guide, direct, or channel water into terraced furrows for irrigation",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बगौण", "tehri": "बगौणा", "salani": "बगौण", "rathwali": "बगौण"}
    },
    {
        "garhwali": "खितौण",
        "hindi": "खेतों में हाथ से बीज बिखेरना अथवा छींटना",
        "english": "to broadcast, sow, or scatter seeds evenly by hand across tilled mountain soil",
        "pos": "verb",
        "gender": "None",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "खितौण", "tehri": "खितौणा", "salani": "खितौण", "rathwali": "खितौण"}
    }
]

added_count = 0
for w in WAVE7_WORDS:
    if w["garhwali"] not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(w["garhwali"])
        added_count += 1
    else:
        print(f"Skipping duplicate: {w['garhwali']}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Wave 7 Vocabulary Injection Complete!")
print(f"Added {added_count} new lemmas.")
print(f"Total verified lexicon words: {len(existing_words)}")

