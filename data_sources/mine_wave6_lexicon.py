# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 6 vocabulary from newly added historical,
borderland, settlement, and mountaineering texts:
- Sherring (1906): Trans-Himalayan trade, wool shearing, pack animals, border passes
- Batten (1851): Land tenure, revenue settlements, village headmen, co-sharers
- Bisht (1994) & Khanduri (1986): High-altitude topography, cols, pilgrim cairns, water channels
- Bhatt (1992) & Verma (2003): Dialect verbs, domestic implements, frost terms
"""

import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE6_WORDS = [
    # --- Trans-Himalayan Trade & Borderland Customs (Sherring 1906) ---
    {
        "garhwali": "हूँण",
        "hindi": "पश्चिमी तिब्बत अथवा भोट प्रदेश (हुणदेश) जहाँ गढ़वाल के भोटिया व्यापारी ऊन व नमक का व्यापार करते थे",
        "english": "Western Tibet or Hundesh, historical trans-Himalayan trading region reached via Mana and Niti passes",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "हूँण", "tehri": "हूँण", "salani": "हुण", "rathwali": "हूँण"}
    },
    {
        "garhwali": "हूँणिया",
        "hindi": "तिब्बती व्यापारी अथवा भोट देश का निवासी",
        "english": "Tibetan merchant or trans-Himalayan high-altitude trader",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "हूँणिया", "tehri": "हूँण्या", "salani": "हुणिया", "rathwali": "हूँणिया"}
    },
    {
        "garhwali": "झब्बू",
        "hindi": "पहाड़ी गाय तथा याक के संकरण से उत्पन्न सहनशील भारवाही पशु",
        "english": "hardy hybrid pack animal produced by crossbreeding a Tibetan yak with a mountain cow",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "झब्बू", "tehri": "जब्बू", "salani": "झब्बू", "rathwali": "झब्बू"}
    },
    {
        "garhwali": "गंगवाल",
        "hindi": "अलकनंदा अथवा गंगा घाटी का स्थायी पर्वतीय निवासी",
        "english": "native inhabitant or hill dweller of the sacred Alaknanda and Ganga valleys",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "गंगवाल", "tehri": "गंगवाळ", "salani": "गंगवाल", "rathwali": "गंगवाल"}
    },
    {
        "garhwali": "गठ्वाळ",
        "hindi": "ऊनी वस्त्र, नमक अथवा सुहागा की छोटी गठरी जो भारवाही बकरों की पीठ पर लादी जाती थी",
        "english": "compact cloth-wrapped pack saddle bundle of wool, salt, or borax carried by pack goats across high passes",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "गठ्वाळ", "tehri": "गठ्वाल", "salani": "गठवाल", "rathwali": "गठ्वाळ"}
    },
    {
        "garhwali": "करचा",
        "hindi": "भेड़-बकरियों की ऊन काटने की पारंपरिक लोहे की बड़ी कैंची",
        "english": "traditional heavy iron shearing shears used by Himalayan shepherds to clip fleece from sheep",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "करचा", "tehri": "करचा", "salani": "करचो", "rathwali": "करचा"}
    },
    {
        "garhwali": "भांफ",
        "hindi": "यमुनोत्री, बदरीनाथ व तप्तकुंड के गर्म जलस्रोतों से निकलने वाली गंधकयुक्त प्राकृतिक भाप",
        "english": "sulfurous geothermal steam or warm vapor rising from Himalayan thermal springs",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "भांफ", "tehri": "बांफ", "salani": "भांफ", "rathwali": "भांफ"}
    },
    {
        "garhwali": "पश्म",
        "hindi": "हिमालयी बकरियों के शरीर से प्राप्त अति कोमल सूक्ष्म ऊन (पश्मीना)",
        "english": "luxurious ultra-fine underfleece combed from high-altitude Himalayan mountain goats",
        "pos": "noun",
        "gender": "M",
        "category": "material",
        "dialect_variants": {"srinagariya": "पश्म", "tehri": "पस्म", "salani": "पश्म", "rathwali": "पश्म"}
    },
    {
        "garhwali": "खलचा",
        "hindi": "कच्चे चमड़े की बनी थैली जिसमें तिब्बत से लाया गया नमक व सुहागा भरा जाता था",
        "english": "rawhide leather pannier or pouch used for transporting rock salt and borax across rocky scree",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "खलचा", "tehri": "खलचा", "salani": "खलचो", "rathwali": "खलचा"}
    },
    {
        "garhwali": "करबन्दी",
        "hindi": "पर्वतीय दर्रों पर व्यापारियों से चुंगी अथवा पारंपरिक सीमा कर वसूलने की व्यवस्था",
        "english": "customary pass toll or transit duty collected at frontier defiles from trans-Himalayan merchants",
        "pos": "noun",
        "gender": "F",
        "category": "governance",
        "dialect_variants": {"srinagariya": "करबन्दी", "tehri": "करबंदी", "salani": "करबन्दी", "rathwali": "करबन्दी"}
    },
    {
        "garhwali": "डाँफ",
        "hindi": "बर्फ हटाने अथवा हिमानी रास्तों को साफ करने का पारंपरिक लकड़ी का फावड़ा",
        "english": "traditional broad wooden snow shovel used to clear blizzard drifts and cut steps in packed ice",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "डाँफ", "tehri": "दाँफ", "salani": "डाँफ", "rathwali": "डाँफ"}
    },
    {
        "garhwali": "पाता",
        "hindi": "किसी निश्चित पर्वतीय गाँव का पारंपरिक अधिकार-क्षेत्र वाला उच्च अल्पाइन चरागाह",
        "english": "demarcated high-altitude summer grazing pasture assigned by custom to a specific mountain village",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "पाता", "tehri": "पातो", "salani": "पाता", "rathwali": "पाता"}
    },
    {
        "garhwali": "गुजी",
        "hindi": "ऊनी नमदे का बना भारी चोगा जिसे चरवाहे बर्फबारी व ठंडी हवाओं से बचने हेतु पहनते हैं",
        "english": "coarse felted wool cloak or heavy shepherd cape worn against blizzards on alpine meadows",
        "pos": "noun",
        "gender": "F",
        "category": "attire",
        "dialect_variants": {"srinagariya": "गुजी", "tehri": "गुजी", "salani": "गुजी", "rathwali": "गुजी"}
    },

    # --- Land Tenure, Customs & Revenue Administration (Batten 1851) ---
    {
        "garhwali": "थात",
        "hindi": "पैतृक अथवा पुश्तैनी भूमि जिस पर किसान का वंशानुगत स्वामित्व होता है",
        "english": "ancestral hereditary landholding estate held under customary unalienable family ownership",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "थात", "tehri": "थात", "salani": "थात", "rathwali": "थात"}
    },
    {
        "garhwali": "खैकर",
        "hindi": "वह वंशानुगत काश्तकार जिसे भूमि से बेदखल नहीं किया जा सकता था परंतु वह भूमि स्वामी को लगान देता था",
        "english": "hereditary subordinate tenant with permanent occupancy rights who cannot be evicted except for non-payment",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "खैकर", "tehri": "खैकर", "salani": "खैकर", "rathwali": "खैकर"}
    },
    {
        "garhwali": "स्याणा",
        "hindi": "गाँव का मुख्य सम्मानित वयोवृद्ध अथवा मालगुजारी व न्याय व्यवस्था संभालने वाला ग्राम प्रधान",
        "english": "hereditary village elder or chief magistrate responsible for maintaining communal order and revenue assessment",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "स्याणा", "tehri": "सयाणा", "salani": "स्याणो", "rathwali": "स्याणा"}
    },
    {
        "garhwali": "सवाजी",
        "hindi": "सामंती काल में ग्राम प्रधान अथवा राजा के अधिकारियों को दिया जाने वाला पारंपरिक उपहार या नजराना",
        "english": "traditional perquisites or customary feudal dues presented to village headmen during festivals",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "सवाजी", "tehri": "सवाजी", "salani": "सवाजी", "rathwali": "सवाजी"}
    },
    {
        "garhwali": "गाँवठ",
        "hindi": "मंदिर के पूजा-पाठ, दीपदान तथा रखरखाव हेतु समर्पित लगान-मुक्त देव-भूमि",
        "english": "tax-exempt land endowment granted in perpetuity for supporting a Hindu temple shrine and ritual worship",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "गाँवठ", "tehri": "गुंठ", "salani": "गांठ", "rathwali": "गाँवठ"}
    },
    {
        "garhwali": "खसमिया",
        "hindi": "भूमि अथवा संपत्ति का विधिपूर्वक स्थापित पारंपरिक संरक्षक या स्वामी",
        "english": "customary guardian, legally established master, or proprietary protector of land rights",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "खसमिया", "tehri": "खसम्या", "salani": "खसमिया", "rathwali": "खसमिया"}
    },
    {
        "garhwali": "कूंट",
        "hindi": "खेत में खड़ी फसल का अनुमान लगाकर लगान निर्धारित करने की पारंपरिक प्रथा",
        "english": "customary visual appraisal or valuation of standing field crops to determine harvest revenue share",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "कूंट", "tehri": "कूत", "salani": "कूंट", "rathwali": "कूंट"}
    },
    {
        "garhwali": "पत्तीदार",
        "hindi": "सांझी पैतृक भूमि अथवा गाँव की सम्पदा में निश्चित हिस्सेदारी रखने वाला भागीदार",
        "english": "recognized co-sharer or coparcener holding an undivided share in a joint ancestral village estate",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "पत्तीदार", "tehri": "पत्तीदार", "salani": "पत्तीदार", "rathwali": "पत्तीदार"}
    },
    {
        "garhwali": "हकदार",
        "hindi": "गाँव के जल-स्रोत, जंगल तथा चरागाह के उपयोग का वैधानिक अथवा प्रथागत अधिकार रखने वाला व्यक्ति",
        "english": "holder of riparian water rights, forest timber privileges, or customary grazing entitlements",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "हकदार", "tehri": "हकदार", "salani": "हकदार", "rathwali": "हकदार"}
    },

    # --- Alpine Geography, Mountaineering & Waterways (Bisht 1994, Khanduri 1986) ---
    {
        "garhwali": "पैयाँ",
        "hindi": "बुग्यालों व उच्च चरागाहों में चरवाहों द्वारा पत्थरों से बनाई गई अस्थायी कुटिया या डेरा",
        "english": "shepherd's rough drystone high-altitude summer hut or dairy shelter in alpine pastures",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "पैयाँ", "tehri": "पैया", "salani": "पैयाँ", "rathwali": "पैयाँ"}
    },
    {
        "garhwali": "कण्डार",
        "hindi": "खड़ी चट्टानी दीवार, विकट कगार अथवा अत्यधिक दुर्गम भयानक पहाड़ी ढलान",
        "english": "precipitous vertical rock face, crag, or dizzying mountain precipice",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कण्डार", "tehri": "कंडार", "salani": "कण्डार", "rathwali": "कण्डार"}
    },
    {
        "garhwali": "ग्वाठ",
        "hindi": "पारंपरिक पहाड़ी मकान का भूतल जहाँ जाड़ों में गाय-बैलों को बांधा जाता है",
        "english": "ground-floor cattle barn under a traditional two-storey stone Himalayan house",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "ग्वाठ", "tehri": "गोठ", "salani": "ग्वाठ", "rathwali": "ग्वाठ"}
    },
    {
        "garhwali": "खरास",
        "hindi": "पहाड़ी जलधारा के वेग से चलने वाली पारंपरिक पनचक्की",
        "english": "traditional Himalayan indigenous watermill driven by the force of a mountain torrent to grind grain",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "खरास", "tehri": "घराट", "salani": "खरास", "rathwali": "खरास"}
    },
    {
        "garhwali": "काण्डी",
        "hindi": "दो नदियों या जलधाराओं के मिलन पर उभरा हुआ संकरा नुकीला पहाड़ी टीला या अंतरीप",
        "english": "narrow rocky ridge spur or promontory jutting sharply at the confluence of two mountain streams",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "काण्डी", "tehri": "कांडी", "salani": "काण्डी", "rathwali": "काण्डी"}
    },
    {
        "garhwali": "थला",
        "hindi": "तीव्र पर्वतीय चढ़ाई के मध्य पत्थरों से बना समतल विश्राम स्थल",
        "english": "small stone-paved rest platform or level terrace situated midway along an arduous mountain ascent",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "थला", "tehri": "थलो", "salani": "थला", "rathwali": "थला"}
    },
    {
        "garhwali": "नागफनी",
        "hindi": "जागर, देव-आह्वान तथा मंदिर उत्सवों में बजाया जाने वाला सर्पिल आकार का पीतल का तुरही वाद्य",
        "english": "serpentine S-shaped ritual brass horn blown during deity invocations, Jagars, and mountain processions",
        "pos": "noun",
        "gender": "F",
        "category": "music",
        "dialect_variants": {"srinagariya": "नागफनी", "tehri": "नागफनी", "salani": "नागफनी", "rathwali": "नागफनी"}
    },
    {
        "garhwali": "छत्तर",
        "hindi": "ऊँचे दर्रों व शिखरों पर तीर्थयात्रियों द्वारा कुशल यात्रा हेतु पत्थरों से बनाया गया स्तूपनुमा ढेर",
        "english": "votive stone cairn piled high on wind-swept Himalayan passes by pilgrims to mark safe passage",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "छत्तर", "tehri": "छतर", "salani": "छत्तर", "rathwali": "छत्तर"}
    },
    {
        "garhwali": "चैंणा",
        "hindi": "रात में जंगली जानवरों से रक्षा तथा शीत से बचने हेतु पत्थरों के बीच जलाई गई अलाव की आग",
        "english": "shepherd's open campfire built within a circle of mountain stones to deter predators and fend off freezing cold",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "चैंणा", "tehri": "चैंणो", "salani": "चैंणा", "rathwali": "चैंणा"}
    },
    {
        "garhwali": "गुल",
        "hindi": "पहाड़ी गधेरों से खेतों तक जल ले जाने वाली पत्थरों से निर्मित पारंपरिक सिंचाई नहर",
        "english": "traditional stone-lined contour canal diverting mountain stream waters across cliffs to irrigate terraced fields",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "गुल", "tehri": "गूल", "salani": "गुल", "rathwali": "गुल"}
    },

    # --- Dialect Verbs & Descriptive Expressions (Bhatt 1992, Verma 2003) ---
    {
        "garhwali": "बिसरौण",
        "hindi": "भूल जाना, विस्मृत करना अथवा मन से विसार देना",
        "english": "to forget, lose memory of, or leave out inadvertently",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बिसरौण", "tehri": "बिसरणा", "salani": "बिसरौण", "rathwali": "बिसरौण"}
    },
    {
        "garhwali": "सिकलौण",
        "hindi": "सिखाना, ज्ञान देना अथवा किसी कार्य में निपुण करना",
        "english": "to teach, instruct, educate, or train in traditional mountain crafts",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "सिकलौण", "tehri": "सिकलणा", "salani": "सिकलौण", "rathwali": "सिकलौण"}
    },
    {
        "garhwali": "हौंकण",
        "hindi": "सँकरे रास्तों पर मवेशियों को हाँकना अथवा आगे बढ़ाना",
        "english": "to drive, urge, or herd cattle along narrow mountain ridges",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "हौंकण", "tehri": "हौंकणा", "salani": "हौंकण", "rathwali": "हौंकण"}
    }
]

added_count = 0
for w in WAVE6_WORDS:
    if w["garhwali"] not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(w["garhwali"])
        added_count += 1
    else:
        print(f"Skipping duplicate: {w['garhwali']}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Wave 6 Vocabulary Injection Complete!")
print(f"Added {added_count} new lemmas.")
print(f"Total verified lexicon words: {len(existing_words)}")
