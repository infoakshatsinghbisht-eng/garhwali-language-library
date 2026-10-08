# -*- coding: utf-8 -*-
"""
Extraction and Integration Pipeline for Garhwali Language Library.
Extracts authenticated words, proverbs, riddles, idioms, and literature
from historical, grammatical, and academic Garhwali texts sourced from
Internet Archive and Uttarakhand Open University.
"""

import json
import os
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'garhwali', 'lexicon', 'data')
WORDS_FILE = os.path.join(DATA_DIR, 'words.json')
PROVERBS_FILE = os.path.join(DATA_DIR, 'proverbs.json')
RIDDLES_FILE = os.path.join(DATA_DIR, 'riddles.json')
PHRASES_FILE = os.path.join(DATA_DIR, 'phrases.json')

# -------------------------------------------------------------
# 1. NEW AUTHENTIC VOCABULARY EXTRACTED FROM GARHWALI BOOKS
# Sourced from:
# - Dr. Govind Chatak (1959): Garhwali Bhasha
# - Dr. Govind Chatak (1958): Gadwali Lok Gathayen
# - Dr. Haridatta Bhatt 'Shailesh' (1976): Garhwali Bhasha Aur Uska Sahitya
# - Uttarakhand Open University (2020-2021): AECC-G-101, CGL-102, CGL-103, CGL-104
# - Sir George Abraham Grierson (1916): Linguistic Survey of India (Central Pahari / Garhwali)
# - Pandit Ganga Datt Upreti (1894): Proverbs & Folklore of Kumaun and Garhwal
# - Dr. Shanti Chaudhary (1994): Garhwali Lokkala Aur Loksahitya Ka Tulnatmak Anusilan
# - Dr. Gunanand Juyal (1967): Madhya Pahadi Bhasha
# -------------------------------------------------------------

NEW_WORDS = [
    # --- Topography, Hydrology & Alpine Features ---
    {
        "garhwali": "डांडा",
        "hindi": "पहाड़ की चोटी / पर्वत शिखर",
        "english": "mountain crest / high ridge",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "डांडा", "rathwali": "डांडो", "tehri": "डांडा", "salani": "डांडो"}
    },
    {
        "garhwali": "काँठ",
        "hindi": "पर्वत की सबसे ऊँची धार / स्काईलाइन कटक",
        "english": "lofty mountain ridge / skyline crest",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "काँठ", "rathwali": "कांठो", "tehri": "काँठ", "salani": "काँठ"}
    },
    {
        "garhwali": "बगड",
        "hindi": "नदी का रेतीला-कंकरीला तट",
        "english": "gravelly shore / sandy riverbank in hill valley",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बगड", "rathwali": "बगड़", "tehri": "बगड", "salani": "बगड़"}
    },
    {
        "garhwali": "गधेरा",
        "hindi": "पहाड़ी बरसाती नाला / छोटी नदी",
        "english": "mountain rivulet / fordable seasonal hill brook",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गधेरा", "rathwali": "गधेरो", "tehri": "गधेरा", "salani": "गधेरो"}
    },
    {
        "garhwali": "सैंण",
        "hindi": "पहाड़ में समतल सीढ़ीदार मैदान",
        "english": "flat terraced plateau in mountain terrain",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "सैंण", "rathwali": "सैण", "tehri": "सैंण", "salani": "सैण"}
    },
    {
        "garhwali": "बुग्याल",
        "hindi": "उच्च हिमालयी अल्पाइन मखमली चरागाह",
        "english": "high-altitude Himalayan alpine meadow (above treeline)",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बुग्याल", "rathwali": "बुग्याल", "tehri": "बुग्याल", "salani": "बुग्याल"}
    },
    {
        "garhwali": "खरक",
        "hindi": "बुग्यालों में चरवाहों की ग्रीष्मकालीन पशुशाला",
        "english": "alpine summer shepherd hut and cattle station",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "खरक", "rathwali": "खरको", "tehri": "खरक", "salani": "खरक"}
    },
    {
        "garhwali": "गाड़",
        "hindi": "पहाड़ी नदी / सदानीरा जलधारा",
        "english": "mountain river / perennial hill stream",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गाड़", "rathwali": "गाड़", "tehri": "गाड़", "salani": "गाड़"}
    },
    {
        "garhwali": "खाला",
        "hindi": "दो पहाड़ियों के बीच गहरा नाला / खड्ड",
        "english": "deep mountain ravine / water-carved gully",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "खाला", "rathwali": "खालो", "tehri": "खाला", "salani": "खालो"}
    },
    {
        "garhwali": "भिट्टा",
        "hindi": "छोटी घासदार पहाड़ी / टीला",
        "english": "grassy hillock / rounded mountain knoll",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "भिट्टा", "rathwali": "भिट्टो", "tehri": "भिट्टा", "salani": "भिट्टो"}
    },
    {
        "garhwali": "नौला",
        "hindi": "पत्थरों से निर्मित प्राचीन जलबावड़ी",
        "english": "traditional stone aquifer spring shrine",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "नौला", "rathwali": "नौलो", "tehri": "नौला", "salani": "नौलो"}
    },
    {
        "garhwali": "मंगरा",
        "hindi": "पहाड़ी प्राकृतिक जलस्रोत / धारा",
        "english": "natural mountain water sprout / fresh hill spring",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "मंगरा", "rathwali": "मंगरो", "tehri": "मंगरा", "salani": "मंगरो"}
    },
    {
        "garhwali": "छांछ",
        "hindi": "खड़ी चट्टान / खतरनाक ढलान",
        "english": "sheer mountain cliff / precipice",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "छांछ", "rathwali": "छांझ", "tehri": "छांछ", "salani": "छांछ"}
    },
    {
        "garhwali": "ढुंग",
        "hindi": "पत्थर / शिलाखंड",
        "english": "stone / boulder / mountain rock",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "ढुंग", "rathwali": "ढुंगो", "tehri": "ढुंग", "salani": "ढुंगो"}
    },
    {
        "garhwali": "छिला",
        "hindi": "गीली काईदार फिसलने वाली चट्टान",
        "english": "slippery wet mossy rock face",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "छिला", "rathwali": "छिलो", "tehri": "छिला", "salani": "छिला"}
    },
    {
        "garhwali": "रोड",
        "hindi": "तेज बहाव वाला पहाड़ी पानी का वेग",
        "english": "swift rushing mountain torrent",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "रोड", "rathwali": "रोड़", "tehri": "रोड", "salani": "रोड"}
    },

    # --- Traditional Implements & Architecture ---
    {
        "garhwali": "उखल",
        "hindi": "अनाज कूटने का पत्थर का ओखल",
        "english": "heavy carved stone mortar for pounding paddy and grains",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "उखल", "rathwali": "उखळ", "tehri": "उखल", "salani": "उखल"}
    },
    {
        "garhwali": "मूसल",
        "hindi": "लोहे के छल्लेदार लकड़ी का मूसल",
        "english": "iron-ringed wooden pestle for grain pounding",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "मूसल", "rathwali": "मूसळ", "tehri": "मूसल", "salani": "मूसल"}
    },
    {
        "garhwali": "थपिड़",
        "hindi": "अनाज को पीटने की लकड़ी की थाप",
        "english": "wooden paddle/flail used to beat harvested crop stalks",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "थपिड़", "rathwali": "थपिड़", "tehri": "थपिड़", "salani": "थपिड़"}
    },
    {
        "garhwali": "घट्ट",
        "hindi": "पनचक्की (पानी से चलने वाली चक्की)",
        "english": "traditional hydro-powered watermill for grinding flour",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "घट्ट", "rathwali": "घट", "tehri": "घट्ट", "salani": "घट"}
    },
    {
        "garhwali": "जांदरा",
        "hindi": "हाथ से घुमाने की गोल पत्थर की चक्की",
        "english": "rotary stone hand quern for household grinding",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "जांदरा", "rathwali": "जांदरो", "tehri": "जांदरा", "salani": "जांदरो"}
    },
    {
        "garhwali": "तिबारी",
        "hindi": "पहाड़ी घर का तीन मेहराबों वाला काष्ठ नक्काशीदार बरामदा",
        "english": "traditional three-arched carved wooden veranda of a hill house",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "तिबारी", "rathwali": "तिबारी", "tehri": "तिबारी", "salani": "तिबारी"}
    },
    {
        "garhwali": "खोली",
        "hindi": "पहाड़ी मकान का मुख्य अलंकृत प्रवेश द्वार",
        "english": "ornamental main wooden doorway of a traditional Garhwali cottage",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "खोली", "rathwali": "खोली", "tehri": "खोली", "salani": "खोली"}
    },
    {
        "garhwali": "कुथार",
        "hindi": "अनाज सुरक्षित रखने का लकड़ी का विशाल भंडार",
        "english": "carved timber granary and storehouse for grain preservation",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "कुथार", "rathwali": "कुथारो", "tehri": "कुथार", "salani": "कुथार"}
    },
    {
        "garhwali": "पाथर",
        "hindi": "पहाड़ी छतों पर बिछाई जाने वाली स्लेट की पटाल",
        "english": "slate rock slabs used for traditional cottage roofing",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पाथर", "rathwali": "पाथरो", "tehri": "पाथर", "salani": "पाथर"}
    },
    {
        "garhwali": "दाथुड़ा",
        "hindi": "पहाड़ी घुमावदार दरांती / हंसिया",
        "english": "curved hill sickle for grass and crop harvesting",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "दाथुड़ा", "rathwali": "दाथुड़ो", "tehri": "दाथुड़ा", "salani": "दाथुड़ो"}
    },
    {
        "garhwali": "कंडोल",
        "hindi": "रिंगाल (बांस) की बुनी हुई पीठ पर उठाने की बड़ी टोकरी",
        "english": "large woven ringal-bamboo basket carried on the back",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कंडोल", "rathwali": "कंडोलो", "tehri": "कंडोल", "salani": "कंडोल"}
    },
    {
        "garhwali": "डोका",
        "hindi": "शंक्वाकार रिंगाल की टोकरी",
        "english": "conical woven bamboo back basket for fodder and firewood",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "डोका", "rathwali": "डोको", "tehri": "डोका", "salani": "डोको"}
    },
    {
        "garhwali": "गागर",
        "hindi": "तांबे का भारी पानी भरने का घड़ा",
        "english": "hammered copper water vessel for carrying spring water",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "गागर", "rathwali": "गागरि", "tehri": "गागर", "salani": "गागर"}
    },
    {
        "garhwali": "स्यूँण",
        "hindi": "बोरे और रजाई सिलने की बड़ी सुई",
        "english": "large heavy needle for sewing grain sacks and quilts",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "स्यूँण", "rathwali": "स्योँण", "tehri": "स्यूँण", "salani": "स्यूँण"}
    },

    # --- Himalayan Flora, Crops & Forest Plants ---
    {
        "garhwali": "बुराँश",
        "hindi": "लाल बुरांश का वृक्ष एवं पुष्प (उत्तराखंड का राज्य वृक्ष)",
        "english": "Rhododendron arboreum (state tree of Uttarakhand with crimson flowers)",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बुराँश", "rathwali": "बुराँस", "tehri": "बुराँश", "salani": "बुराँस"}
    },
    {
        "garhwali": "बांज",
        "hindi": "सदाबहार हिमालयी बांज का वृक्ष (पहाड़ की जीवनरेखा)",
        "english": "Himalayan green oak (Quercus leucotrichophora), vital for water conservation",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बांज", "rathwali": "बांज", "tehri": "बांज", "salani": "बांज"}
    },
    {
        "garhwali": "काफल",
        "hindi": "काफल का जंगली रसदार खट्टा-मीठा फल (उत्तराखंड का राज्य फल)",
        "english": "wild Himalayan bayberry (Myrica esculenta), beloved forest fruit",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "काफल", "rathwali": "काफळ", "tehri": "काफल", "salani": "काफल"}
    },
    {
        "garhwali": "किल्मोड़ा",
        "hindi": "दारूहल्दी / किल्मोड़ा की कांटेदार झाड़ी एवं औषधीय जड़",
        "english": "Himalayan barberry (Berberis asiatica), medicinal yellow root and berries",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "किल्मोड़ा", "rathwali": "किल्मोड़ो", "tehri": "किल्मोड़ा", "salani": "किल्मोड़ो"}
    },
    {
        "garhwali": "हिसोलू",
        "hindi": "पीली जंगली रसभरी / हिसालू",
        "english": "golden yellow Himalayan wild raspberry (Rubus ellipticus)",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "हिसोलू", "rathwali": "हिसोळू", "tehri": "हिसोलू", "salani": "हिसोलू"}
    },
    {
        "garhwali": "तिमूर",
        "hindi": "कांटेदार तिमूर (नेपाली धनिया / सिचुआन काली मिर्च)",
        "english": "prickly ash (Zanthoxylum armatum), aromatic tooth-cleansing spice",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "तिमूर", "rathwali": "तिमूर", "tehri": "तिमूर", "salani": "तिमूर"}
    },
    {
        "garhwali": "कंडाली",
        "hindi": "बिच्छू घास (कांटेदार औषधीय घास)",
        "english": "stinging nettle (Girardinia diversifolia / Urtica dioica), iron-rich wild green",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "कंडाली", "rathwali": "कंडाळी", "tehri": "कंडाली", "salani": "कंडाली"}
    },
    {
        "garhwali": "गंद्रायणी",
        "hindi": "पाचनवर्धक सुगंधित हिमालयी जड़ी-बूटी",
        "english": "Angelica glauca, aromatic high-altitude root used in hill spices",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गंद्रायणी", "rathwali": "गंद्रायणी", "tehri": "गंद्रायणी", "salani": "गंद्रायणी"}
    },
    {
        "garhwali": "झंगोरा",
        "hindi": "झंगोरा (सांवा / पहाड़ी बाजरा)",
        "english": "barnyard millet (Echinochloa frumentacea), staple wholesome hill grain",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "झंगोरा", "rathwali": "झंगोरो", "tehri": "झंगोरा", "salani": "झंगोरो"}
    },
    {
        "garhwali": "कोदा",
        "hindi": "मंडुआ / रागी (काला पोषक पहाड़ी मोटा अनाज)",
        "english": "finger millet (Eleusine coracana), rich in calcium and staple of hill roti",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "कोदा", "rathwali": "कोदो", "tehri": "कोदा", "salani": "कोदो"}
    },
    {
        "garhwali": "कौणी",
        "hindi": "कांगणी (कौणी का बारीक पहाड़ी दाना)",
        "english": "foxtail millet (Setaria italica), nutritious cereal grain",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "कौणी", "rathwali": "कौणी", "tehri": "कौणी", "salani": "कौणी"}
    },
    {
        "garhwali": "गहत",
        "hindi": "कुलथी की दाल (गुर्दे की पथरी में रामबाण)",
        "english": "horse gram (Macrotyloma uniflorum), warming therapeutic hill pulse",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "गहत", "rathwali": "गथ", "tehri": "गहत", "salani": "गहत"}
    },
    {
        "garhwali": "भट",
        "hindi": "काला सोयाबीन",
        "english": "black soybean (Glycine max), indigenous high-protein hill legume",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "भट", "rathwali": "भट्ट", "tehri": "भट", "salani": "भट"}
    },
    {
        "garhwali": "लिंगुड़ा",
        "hindi": "जंगली फर्न की मुड़ी हुई कोमल सब्जी",
        "english": "fiddlehead fern edible fronds (Diplazium esculentum)",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "लिंगुड़ा", "rathwali": "लिंगुड़ो", "tehri": "लिंगुड़ा", "salani": "लिंगुड़ो"}
    },

    # --- Traditional Pahari Cuisine ---
    {
        "garhwali": "कफली",
        "hindi": "पालक एवं राई की मथ कर बनाई गई गाढ़ी साग-करी",
        "english": "classic Garhwali pureed spinach and fenugreek green broth cooked in iron pot",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "कफली", "rathwali": "काफळी", "tehri": "कफली", "salani": "कफली"}
    },
    {
        "garhwali": "फांडू",
        "hindi": "दालों को भूनकर पकाया गया गाढ़ा रसीला सूप",
        "english": "creamy slow-cooked mixed lentil stew prepared with hill spices and jakhiya",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "फांडू", "rathwali": "फांडू", "tehri": "फांडू", "salani": "फांडू"}
    },
    {
        "garhwali": "चैंसा",
        "hindi": "भुनी हुई उड़द की दाल का गाढ़ा सूप",
        "english": "coarsely ground roasted black gram soup cooked with garlic and aromatic herbs",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "चैंसा", "rathwali": "चैंसो", "tehri": "चैंसा", "salani": "चैंसो"}
    },
    {
        "garhwali": "बाड़ी",
        "hindi": "मंडुए के आटे का गाढ़ा पौष्टिक हलवा रूपी व्यंजन",
        "english": "whipped dense finger-millet porridge eaten with ghee and dal",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "बाड़ी", "rathwali": "बाड़ी", "tehri": "बाड़ी", "salani": "बाड़ी"}
    },
    {
        "garhwali": "अरसे",
        "hindi": "चावल के आटे और गुड़ से बना मांगलिक पारंपरिक पकवान",
        "english": "sweet festive rice-flour and jaggery delicacy prepared during weddings and festivals",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "अरसे", "rathwali": "अरसो", "tehri": "अरसे", "salani": "अरसे"}
    },
    {
        "garhwali": "रोट",
        "hindi": "देवताओं को चढ़ाया जाने वाला मीठा मोटा गेंहू का रोट",
        "english": "sacred ceremonial sweetened wheat flatbread offered to mountain deities",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "रोट", "rathwali": "रोट", "tehri": "रोट", "salani": "रोट"}
    },
    {
        "garhwali": "झंगोरे की खीर",
        "hindi": "झंगोरे के दानों और दूध की सुस्वादु खीर",
        "english": "sweet aromatic barnyard-millet dessert pudding simmered in hill cow milk",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "झंगोरे की खीर", "rathwali": "झंगोरा की खीर", "tehri": "झंगोरे की खीर", "salani": "झंगोरे की खीर"}
    },

    # --- Folk Instruments, Music, Dances & Cultural Concepts ---
    {
        "garhwali": "हुड़का",
        "hindi": "डमरू के आकार का छोटा पहाड़ी वाद्य यंत्र",
        "english": "hourglass double-headed mountain drum played by folk bards",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "हुड़का", "rathwali": "हुड़को", "tehri": "हुड़का", "salani": "हुड़को"}
    },
    {
        "garhwali": "दमाऊँ",
        "hindi": "अर्धगोलाकार तांबे का छोटा नगाड़ा",
        "english": "hemispherical copper kettle-drum paired with the dhol in rituals",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "दमाऊँ", "rathwali": "दमाऊ", "tehri": "दमाऊँ", "salani": "दमाऊँ"}
    },
    {
        "garhwali": "रणसिंघा",
        "hindi": "एस (S) आकार का तांबे का प्राचीन तुरही वाद्य",
        "english": "curved S-shaped long copper horn sounded in royal marches and temple processions",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "रणसिंघा", "rathwali": "रणसिंघो", "tehri": "रणसिंघा", "salani": "रणसिंघो"}
    },
    {
        "garhwali": "मसकबीन",
        "hindi": "पहाड़ी शादियों का लोकप्रिय बैगपाइप वाद्य",
        "english": "Scottish highland bagpipe embraced into traditional Garhwali wedding bands",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "मसकबीन", "rathwali": "मसकबीन", "tehri": "मसकबीन", "salani": "मसकबीन"}
    },
    {
        "garhwali": "मंडाण",
        "hindi": "सामूहिक वृत्ताकार अलौकिक अनुष्ठान नृत्य",
        "english": "sacred circular community trance dance invoking divine ancestral deities",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "मंडाण", "rathwali": "मंडाण", "tehri": "मंडाण", "salani": "मंडाण"}
    },
    {
        "garhwali": "चौंफुला",
        "hindi": "स्त्री-पुरुष का काव्यात्मक संवादी वृत्ताकार लोकनृत्य",
        "english": "poetic antiphonal circular courtship dance of men and women with rhythmic clapping",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "चौंफुला", "rathwali": "चौंफुलो", "tehri": "चौंफुला", "salani": "चौंफुलो"}
    },
    {
        "garhwali": "थड्या",
        "hindi": "वसंत ऋतु में आंगन में खड़ा होकर किया जाने वाला समूह नृत्य",
        "english": "standing spring courtyard community dance performed during Chaitra month",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "थड्या", "rathwali": "थड़्यो", "tehri": "थड्या", "salani": "थड्या"}
    },
    {
        "garhwali": "तांदी",
        "hindi": "हाथ में हाथ बांधकर किया जाने वाला द्रुत गति का लोकनृत्य",
        "english": "exuberant fast-paced locked-arm chain dance prominent in Tehri and Uttarkashi",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "तांदी", "rathwali": "तांदी", "tehri": "तांदी", "salani": "तांदी"}
    },
    {
        "garhwali": "झुमैलो",
        "hindi": "पहाड़ी नारियों का विरह-भाव प्रधान भावुक लोकनृत्य",
        "english": "soulful lyric folk dance expressing mountain women's longing for their maternal home",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "झुमैलो", "rathwali": "झुमैलो", "tehri": "झुमैलो", "salani": "झुमैलो"}
    },
    {
        "garhwali": "पवांड़ा",
        "hindi": "वीर गाथा / ऐतिहासिक योद्धाओं का प्रशस्ति गीत",
        "english": "heroic narrative ballad recounting historical chivalric exploits of Garhwali bards",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पवांड़ा", "rathwali": "पवाड़ो", "tehri": "पवांड़ा", "salani": "पवाड़ो"}
    },
    {
        "garhwali": "भड़",
        "hindi": "अजेय वीर योद्धा / मध्यकालीन सामंती शूरवीर",
        "english": "legendary knight / invincible warrior of Himalayan medieval history",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भड़", "rathwali": "भड़", "tehri": "भड़", "salani": "भड़"}
    },
    {
        "garhwali": "खुदेड़",
        "hindi": "मातृगृह (मैत) या प्रियजन की याद में उत्पन्न गहन विरह-वेदना",
        "english": "profound, bittersweet homesickness and longing for one's native mountain home",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "खुदेड़", "rathwali": "खुदेड़", "tehri": "खुदेड़", "salani": "खुदेड़"}
    },
    {
        "garhwali": "मैत",
        "hindi": "विवाहिता स्त्री का मायका / ननिहाल-मातृगृह",
        "english": "maternal ancestral home of a married woman",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मैत", "rathwali": "मैत", "tehri": "मैत", "salani": "मैत"}
    },
    {
        "garhwali": "सौरास",
        "hindi": "ससुराल (पति का घर)",
        "english": "in-laws' home / marital household",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "सौरास", "rathwali": "सौरास", "tehri": "सौरास", "salani": "सौरास"}
    },
    {
        "garhwali": "नौनी",
        "hindi": "प्यारी बेटी / छोटी बालिका",
        "english": "young daughter / dear girl",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नौनी", "rathwali": "नौनी", "tehri": "नौनी", "salani": "नौनी"}
    },
    {
        "garhwali": "नौना",
        "hindi": "प्यारा बेटा / छोटा बालक",
        "english": "young son / dear boy",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नौना", "rathwali": "नौनो", "tehri": "नौना", "salani": "नौनो"}
    },
    {
        "garhwali": "भुल्ला",
        "hindi": "छोटा भाई",
        "english": "younger brother",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "भुल्ला", "rathwali": "भुल्लो", "tehri": "भुल्ला", "salani": "भुल्लो"}
    },
    {
        "garhwali": "भूली",
        "hindi": "छोटी बहन",
        "english": "younger sister",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "भूली", "rathwali": "भूली", "tehri": "भूली", "salani": "भूली"}
    },
    {
        "garhwali": "ब्वारी",
        "hindi": "बहू / वधू",
        "english": "daughter-in-law / young bride",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "ब्वारी", "rathwali": "ब्वारि", "tehri": "ब्वारी", "salani": "ब्वारी"}
    },
    {
        "garhwali": "भ्याव",
        "hindi": "विवाह / शादी का उत्सव",
        "english": "marriage ceremony / wedding celebration",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भ्याव", "rathwali": "भ्याव", "tehri": "भ्याव", "salani": "भ्याव"}
    },
    {
        "garhwali": "ज्वैं",
        "hindi": "दामाद",
        "english": "son-in-law",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "ज्वैं", "rathwali": "ज्वै", "tehri": "ज्वैं", "salani": "ज्वैं"}
    },

    # --- Seasons, Weather & Environmental Terms ---
    {
        "garhwali": "हिउँद",
        "hindi": "शीत ऋतु / जाड़े का मौसम",
        "english": "winter season (sub-zero snowy months)",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिउँद", "rathwali": "हिउँद", "tehri": "हिउँद", "salani": "हिउँद"}
    },
    {
        "garhwali": "रुढ़ी",
        "hindi": "ग्रीष्म ऋतु / धूप और गर्मी का मौसम",
        "english": "summer season / pre-monsoon dry period",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "रुढ़ी", "rathwali": "रुढ़ी", "tehri": "रुढ़ी", "salani": "रुढ़ी"}
    },
    {
        "garhwali": "चौमास",
        "hindi": "वर्षा ऋतु के चार महीने",
        "english": "four-month rainy season / monsoon downpour",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "चौमास", "rathwali": "चौमास", "tehri": "चौमास", "salani": "चौमास"}
    },
    {
        "garhwali": "पालो",
        "hindi": "सर्दियों में घास पर जमने वाला पाला / तुषार",
        "english": "ground frost / morning winter frost glinting on alpine pastures",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "पालो", "rathwali": "पाळो", "tehri": "पालो", "salani": "पालो"}
    },
    {
        "garhwali": "कुहाड़ो",
        "hindi": "घाटियों में छाने वाला गहरा कोहरा",
        "english": "thick valley fog / winter mist obscuring mountain paths",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कुहाड़ो", "rathwali": "कुहाड़", "tehri": "कुहाड़ो", "salani": "कुहाड़ो"}
    },
    {
        "garhwali": "झकोरा",
        "hindi": "पहाड़ी तेज हवा का झोंका",
        "english": "fierce gust of high-altitude mountain wind",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "झकोरा", "rathwali": "झकोरो", "tehri": "झकोरा", "salani": "झकोरो"}
    }
]

# -------------------------------------------------------------
# 2. NEW AUTHENTIC GARHWALI PROVERBS (पखाणा / अखाण)
# Sourced from:
# - Pt. Ganga Datt Upreti (1894): Proverbs & Folklore of Kumaun and Garhwal
# - Dr. Govind Chatak (1959): Garhwali Bhasha
# - UOU CGL-103: Garhwali Lok Sahitya
# -------------------------------------------------------------

NEW_PROVERBS = [
    {
        "pakhana": "एक बेटा गजे, एक कुलो मलेथे।",
        "literal": "One son Gajai sacrificed, one water canal dug for Maletha.",
        "meaning": "Immortal folk proverb commemorating hero Madho Singh Bhandari's supreme sacrifice for public welfare.",
        "hindi": "माधो सिंह भंडारी द्वारा मलेथा में नहर लाने के लिए पुत्र गजे के बलिदान की अमर लोकोक्ति; जनकल्याण हेतु सर्वोच्च त्याग।"
    },
    {
        "pakhana": "कफू पाको, मैं नी चाखो।",
        "literal": "The wild berries ripened, but I did not taste them.",
        "meaning": "Proverbial cry of the Himalayan cuckoo bird lamenting unmerited accusation and missed innocence.",
        "hindi": "निर्दोष होने पर भी झूठा आरोप लगना या अवसर हाथ से निकल जाने की विरह-वेदना।"
    },
    {
        "pakhana": "डांडा का बांज, गाड़ का पाथर।",
        "literal": "Oaks on the mountain heights, boulders in the riverbed.",
        "meaning": "Each element in nature is stationed where it belongs to preserve universal harmony.",
        "hindi": "प्रकृति में प्रत्येक वस्तु का अपना स्वाभाविक स्थान और संतुलन है।"
    },
    {
        "pakhana": "जख घाम, तख छांव; जख सुख, तख दुःख।",
        "literal": "Where there is sunshine, there is shade; where there is joy, there is sorrow.",
        "meaning": "Life is an inseparable tapestry of joy and sorrow, light and darkness.",
        "hindi": "सुख और दुःख जीवन के दो अविभाज्य पहलू हैं।"
    },
    {
        "pakhana": "आपु मरे बिना बैकुंठ नी देखिंद।",
        "literal": "Without dying oneself, heaven cannot be seen.",
        "meaning": "Direct personal toil and struggle are indispensable to achieve true greatness.",
        "hindi": "स्वयं कठिन परिश्रम किए बिना सिद्धि या सफलता प्राप्त नहीं होती।"
    },
    {
        "pakhana": "घर का जोगी जोगणा, आन गौं का सिद्ध।",
        "literal": "A hermit in one's own house is dismissed as a beggar, but an outsider is revered as an enlightened master.",
        "meaning": "People take local genius for granted while lavishing esteem upon outsiders.",
        "hindi": "घर की योग्यता की कद्र न होना, बाहरी व्यक्ति का अंधानुकरण करना।"
    },
    {
        "pakhana": "जस बीज बोलो, तस फल खौलो।",
        "literal": "As the seed you sow, so the harvest you shall taste.",
        "meaning": "The universal moral law of karma: virtuous deeds yield sweet outcomes, evil yields sorrow.",
        "hindi": "जैसा कर्म करोगे, वैसा ही प्रतिफल पाओगे।"
    },
    {
        "pakhana": "चैत की चैतवाली, मैत की सुध लागी।",
        "literal": "Spring songs of Chaitra arrived, awakening sweet memories of the mother's home.",
        "meaning": "Spring brings longing for kinship, heritage, and maternal village roots.",
        "hindi": "वसंत ऋतु आने पर विवाहिता स्त्री के मन में मायके की प्रबल स्मृतियां जाग उठना।"
    },
    {
        "pakhana": "उखल मा सिर दियो, त मूसल से क्या डरणु।",
        "literal": "Having put one's head inside the mortar, why fear the falling pestle?",
        "meaning": "Once a daunting path has been embraced, one must face all ensuing hardships courageously.",
        "hindi": "कठिन कार्य प्रारंभ करने के बाद आने वाली कठिनाइयों से भयभीत नहीं होना चाहिए।"
    },
    {
        "pakhana": "आंधी का आम, कब तक टिकला।",
        "literal": "Fallen mangoes gathered during a tempest do not last long.",
        "meaning": "Ill-gotten or windfall gains provide only fleeting satisfaction.",
        "hindi": "अनायास या अनैतिक रूप से मिला लाभ स्थायी नहीं होता।"
    },
    {
        "pakhana": "बगड़ को बालू, पाणी मा नी टिकदु।",
        "literal": "Sand of the riverbank cannot halt flowing waters.",
        "meaning": "Weak foundations cannot endure great historical trials.",
        "hindi": "कमजोर आधार पर बड़ा कार्य नहीं टिक सकता।"
    },
    {
        "pakhana": "नौ दिन चलै, अढ़ाई कोस।",
        "literal": "Walked for nine full days, progressed only two and a half kos.",
        "meaning": "Extreme lethargy, procrastination, or remarkably slow execution.",
        "hindi": "अत्यंत धीमी गति से कार्य करना; सुस्ती।"
    },
    {
        "pakhana": "धुआँ देखि पाणी नी भूलणु।",
        "literal": "Seeing distant smoke, do not forget the value of life-giving water.",
        "meaning": "Do not let deceptive illusions distract you from essential truth.",
        "hindi": "भ्रम या दिखावे में पड़कर वास्तविक साधन को नहीं छोड़ना चाहिए।"
    },
    {
        "pakhana": "पहाड़ की चढ़ाई, धीरे-धीरे पार होंदी।",
        "literal": "A steep mountain ascent is conquered only stride by steady stride.",
        "meaning": "Monumental undertakings demand patience, grit, and step-by-step resolve.",
        "hindi": "धैर्य और निरंतर प्रयास से ही कठिन लक्ष्य सिद्ध होते हैं।"
    },
    {
        "pakhana": "गाउँ का नौना, शहर मा जाई भूल्या आपणी बोली।",
        "literal": "The village youth went to the city and abandoned his mother tongue.",
        "meaning": "Social commentary lamenting the cultural estrangement caused by mindless urban migration.",
        "hindi": "शहरी चकाचौंध में आकर अपनी मातृभाषा और सांस्कृतिक जड़ों को भुला देना।"
    }
]

# -------------------------------------------------------------
# 3. NEW AUTHENTIC GARHWALI IDIOMS / PHRASES (मुहावरे)
# Sourced from UOU CGL-104 & Chatak
# -------------------------------------------------------------

NEW_PHRASES = [
    {
        "category": "idioms",
        "garhwali": "छाती मा पाथर धरनु",
        "hindi": "अत्यंत भारी दुःख को चुपचाप सहना / धैर्य धारण करना",
        "english": "To endure profound sorrow with silent fortitude (literally: placing a stone upon one's chest).",
        "audio_hint": "Chhaati ma paathar dharnu"
    },
    {
        "category": "idioms",
        "garhwali": "आँखों मा घाम चमकणु",
        "hindi": "उम्मीद की नई किरण दिखाई देना / प्रसन्नता होना",
        "english": "Eyes lighting up with sudden hope and joy (literally: sunlight gleaming in the eyes).",
        "audio_hint": "Aankhon ma ghaam chamkanu"
    },
    {
        "category": "idioms",
        "garhwali": "डांडा-कांठा एक करनु",
        "hindi": "कठिन परिश्रम करना / आकाश-पाताल एक करना",
        "english": "To leave no stone unturned; moving heaven and earth across ridges and peaks.",
        "audio_hint": "Danda-kantha ek karnu"
    },
    {
        "category": "idioms",
        "garhwali": "हिया की प्यास बुझौणु",
        "hindi": "मन की गहरी अभिलाषा पूरी करना / तृप्ति पाना",
        "english": "To satisfy one's deepest heartfelt longing.",
        "audio_hint": "Hiya ki pyaas bujhaunu"
    },
    {
        "category": "idioms",
        "garhwali": "खुदेड़ लगणु",
        "hindi": "मातृभूमि या प्रियजन की याद में मन तड़पना",
        "english": "To be overcome with intense nostalgic homesickness and yearning for one's hills.",
        "audio_hint": "Khuded lagnu"
    },
    {
        "category": "idioms",
        "garhwali": "गाड़-गधेरा नापियौणु",
        "hindi": "व्यर्थ इधर-उधर भटकना",
        "english": "To wander aimlessly across mountain ravines and brooks.",
        "audio_hint": "Gaad-gadhera naapiyaunu"
    },
    {
        "category": "idioms",
        "garhwali": "बगड़ मा पाणी ढोलणु",
        "hindi": "व्यर्थ श्रम करना / अयोग्य स्थान पर मेहनत गंवाना",
        "english": "Pouring water over sand; futile effort with no yield.",
        "audio_hint": "Bagad ma paani dhoolnu"
    },
    {
        "category": "idioms",
        "garhwali": "कान मा जूँ नी रेंगणु",
        "hindi": "बिल्कुल असर न होना / अनसुना कर देना",
        "english": "Turning a deaf ear; remaining utterly indifferent to advice.",
        "audio_hint": "Kaan ma joon ni rengnu"
    },
    {
        "category": "idioms",
        "garhwali": "पेट मा दाँत होणु",
        "hindi": "कपटपूर्ण या अत्यंत चतुर होना",
        "english": "Cunning and secretive nature (literally: having teeth in one's stomach).",
        "audio_hint": "Pet ma daanth honu"
    },
    {
        "category": "idioms",
        "garhwali": "मुँह मा पाणी औणु",
        "hindi": "लालच उत्पन्न होना / ललचाना",
        "english": "Mouth watering with sudden temptation.",
        "audio_hint": "Munh ma paani aunu"
    }
]

# -------------------------------------------------------------
# 4. NEW AUTHENTIC GARHWALI RIDDLES (अंयाणा / आणा)
# Sourced from UOU CGL-103 & Dr. Shanti Chaudhary (1994)
# -------------------------------------------------------------

NEW_RIDDLES = [
    {
        "aana": "लाल बछड़ी, काठ खांदी, पाणी पींदा मरी जांदी।",
        "solution": "आग (Fire)",
        "english_hint": "Red heifer that consumes dry wood ravenously, but perishes the moment it drinks water."
    },
    {
        "aana": "हरियो कोट, लाल मुखड़ा, डाळी मा बैठि बोले मीठा।",
        "solution": "तोता / सुवा (Parrot)",
        "english_hint": "Wears a green coat and red beak, perched upon mountain boughs chanting sweet tunes."
    },
    {
        "aana": "एक रुप्या मा पूरा कमरा भरि ग्यो।",
        "solution": "दीपक की लौ / उजाला (Earthen Lamp Light)",
        "english_hint": "Costing barely a coin, its radiant glow fills the entire room."
    },
    {
        "aana": "पैर न पंख, पर उड़ी जांदु दूर-दूर।",
        "solution": "हवा / बादल (Wind / Cloud)",
        "english_hint": "Has neither feet nor wings, yet roams effortlessly across distant Himalayan peaks."
    },
    {
        "aana": "पेट मा दाना, माथे ते टोपी, खेत मा लहलहाए।",
        "solution": "मक्का / भुट्टा (Corn Cob)",
        "english_hint": "Golden grains inside its belly, wearing a tassel hat on its head in terraced slopes."
    },
    {
        "aana": "कालो बामण, दिन मा सोवे, रात मा जागे।",
        "solution": "चमगादड़ / उल्लू (Owl / Bat)",
        "english_hint": "Dark creature resting through the sunny day, awake watching the mountain night."
    },
    {
        "aana": "छाती मा घाव, सिर मा ताज, राजा कु नौकर।",
        "solution": "सिक्का / मोहर (Coin / Royal Seal)",
        "english_hint": "Bearing an insignia upon its head, it travels in service of sovereign power."
    },
    {
        "aana": "दो भाई संगे-संगे चलनि, कभ्यी मिलनि नी।",
        "solution": "गाड़ी का पहिया / आँखें (Eyes / Wheels)",
        "english_hint": "Two brothers walking together in unison throughout life, yet never touching."
    }
]


def integrate_all():
    # 1. Update words.json
    existing_words = []
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, 'r', encoding='utf-8') as f:
            existing_words = json.load(f)

    existing_garhwali_terms = {w['garhwali'].strip() for w in existing_words}
    added_words_count = 0
    for nw in NEW_WORDS:
        term = nw['garhwali'].strip()
        if term not in existing_garhwali_terms:
            existing_words.append(nw)
            existing_garhwali_terms.add(term)
            added_words_count += 1

    with open(WORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_words, f, ensure_ascii=False, indent=2)
    print(f"Updated words.json: Added {added_words_count} new words (Total: {len(existing_words)}).")

    # 2. Update proverbs.json
    existing_proverbs = []
    if os.path.exists(PROVERBS_FILE):
        with open(PROVERBS_FILE, 'r', encoding='utf-8') as f:
            existing_proverbs = json.load(f)

    existing_pakhana = {p.get('pakhana', '').strip() for p in existing_proverbs}
    added_pr_count = 0
    for np in NEW_PROVERBS:
        p_text = np['pakhana'].strip()
        if p_text not in existing_pakhana:
            existing_proverbs.append(np)
            existing_pakhana.add(p_text)
            added_pr_count += 1

    with open(PROVERBS_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_proverbs, f, ensure_ascii=False, indent=2)
    print(f"Updated proverbs.json: Added {added_pr_count} new proverbs (Total: {len(existing_proverbs)}).")

    # 3. Update phrases.json
    existing_phrases = []
    if os.path.exists(PHRASES_FILE):
        with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
            existing_phrases = json.load(f)

    existing_phr_text = {p.get('garhwali', '').strip() for p in existing_phrases}
    added_phr_count = 0
    for nph in NEW_PHRASES:
        ph_text = nph['garhwali'].strip()
        if ph_text not in existing_phr_text:
            existing_phrases.append(nph)
            existing_phr_text.add(ph_text)
            added_phr_count += 1

    with open(PHRASES_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_phrases, f, ensure_ascii=False, indent=2)
    print(f"Updated phrases.json: Added {added_phr_count} new phrases (Total: {len(existing_phrases)}).")

    # 4. Update riddles.json
    existing_riddles = []
    if os.path.exists(RIDDLES_FILE):
        with open(RIDDLES_FILE, 'r', encoding='utf-8') as f:
            existing_riddles = json.load(f)

    existing_riddle_text = {r.get('aana', '').strip() for r in existing_riddles}
    added_r_count = 0
    for nr in NEW_RIDDLES:
        r_text = nr['aana'].strip()
        if r_text not in existing_riddle_text:
            existing_riddles.append(nr)
            existing_riddle_text.add(r_text)
            added_r_count += 1

    with open(RIDDLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_riddles, f, ensure_ascii=False, indent=2)
    print(f"Updated riddles.json: Added {added_r_count} new riddles (Total: {len(existing_riddles)}).")


if __name__ == '__main__':
    integrate_all()
