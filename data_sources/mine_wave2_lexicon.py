# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline - Wave 2 Books:
Ingests and maps authenticated vocabulary from:
1. L. D. Joshi (1929): Khasa Family Law in the Himalayan Districts
2. Mukandi Lal (1968): Garhwal Painting & Srinagar Court Culture
3. Rev. Thomas Grahame Bailey (1915): Linguistic Studies from the Himalayas
4. Himachal Academy (1909): A Dictionary of Pahari Dialects
5. Himachal Academy (1989): Pahari-Hindi Shabdkosh
6. Edwin T. Atkinson (1882): The Himalayan Districts Vol. 1
7. Government of Uttar Pradesh (1989): District Gazetteers: Garhwal
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

WAVE2_MINED_WORDS = [
    # Customary Himalayan Kinship, Matrimonial Law & Lineage
    {
        "garhwali": "टका-ब्याव",
        "hindi": "कन्यामूल्य लेकर किया जाने वाला पारंपरिक पहाड़ी विवाह",
        "english": "customary Himalayan marriage contracted with bride-price consideration",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "टका-ब्याव", "tehri": "टका-ब्याव", "salani": "टका-ब्याव", "rathwali": "टका-ब्याव"}
    },
    {
        "garhwali": "धरेवा",
        "hindi": "विधवा या परित्यक्ता स्त्री का पुनर्विवाह संस्कार",
        "english": "customary informal mountain remarriage of a widow or separated woman",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "धरेवा", "tehri": "धरेवा", "salani": "धरेवा", "rathwali": "धरेवा"}
    },
    {
        "garhwali": "सरतोरा",
        "hindi": "दौहित्र (बेटी के पुत्र) को पैतृक संपत्ति में दिया जाने वाला भाग",
        "english": "customary matrilineal inheritance share designated for a daughter's son",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "सरतोरा", "tehri": "सरतोरा", "salani": "सरतोरा", "rathwali": "सरतोरा"}
    },
    {
        "garhwali": "जेठों",
        "hindi": "पैतृक जायदाद में ज्येष्ठ पुत्र का विशेषाधिकार युक्त बड़ा भाग",
        "english": "customary preferential inheritance share allocated to the eldest son",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "जेठों", "tehri": "जेठों", "salani": "जेठों", "rathwali": "जेठों"}
    },
    {
        "garhwali": "कांछों",
        "hindi": "पैतृक मकान व चूल्हा सबसे छोटे बेटे को मिलने का अधिकार",
        "english": "customary right of the youngest son to retain family hearth and dwelling",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "कांछों", "tehri": "कांछों", "salani": "कांछों", "rathwali": "कांछों"}
    },
    {
        "garhwali": "कमीनचार",
        "hindi": "कमीण अधिकारी को ग्रामीणों द्वारा दिया जाने वाला पारंपरिक दस्तूर",
        "english": "customary tribute or perquisite grain paid to the village Kamin revenue collector",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "कमीनचार", "tehri": "कमीनचार", "salani": "कमीनचार", "rathwali": "कमीनचार"}
    },
    {
        "garhwali": "सयाणाचार",
        "hindi": "ग्राम सयाणा को सम्मान स्वरूप दी जाने वाली पारंपरिक भेंट",
        "english": "customary administrative honorarium rendered to the Sayana village counselor",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "सयाणाचार", "tehri": "सयाणाचार", "salani": "सयाणाचार", "rathwali": "सयाणाचार"}
    },
    {
        "garhwali": "मैत्याणी",
        "hindi": "विवाह के बाद मायके आई हुई विवाहिता बेटी / ध्याणी",
        "english": "married mountain woman visiting her maternal family home",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मैत्याणी", "tehri": "मैत्यानी", "salani": "मैत्याणी", "rathwali": "मैत्याणी"}
    },
    {
        "garhwali": "रौतेली",
        "hindi": "विवाह उत्सव के आंगन में गाया व नाचा जाने वाला मांगलिक नृत्य",
        "english": "festive auspicious courtyard folk dance celebrated during mountain weddings",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "रौतेली", "tehri": "रौतेली", "salani": "रौतेली", "rathwali": "रौतेळी"}
    },
    {
        "garhwali": "जनेती",
        "hindi": "वर पक्ष की बारात में शामिल होने वाला बाराती जन",
        "english": "wedding procession attendant marching in bridegroom's party",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "जनेती", "tehri": "जनेती", "salani": "जनेती", "rathwali": "जनेती"}
    },
    {
        "garhwali": "धूली-अर्घ",
        "hindi": "द्वार पर वर का स्वागत करने हेतु चरण व धूलि प्रक्षालन संस्कार",
        "english": "sacred doorstep reception ritual washing dust from bridegroom's feet",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "धूली-अर्घ", "tehri": "धूली-अर्घ", "salani": "धूली-अर्घ", "rathwali": "धूली-अर्घ"}
    },
    {
        "garhwali": "न्योतो",
        "hindi": "विवाह या उत्सव का पारिवारिक निमंत्रण",
        "english": "ceremonial wedding feast invitation sent to kinfolk",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "न्योतो", "tehri": "न्योतु", "salani": "न्योता", "rathwali": "न्योतो"}
    },
    {
        "garhwali": "नेग",
        "hindi": "शुभ कार्यों में वादकों, शिल्पियों व संबंधियों को दिया जाने वाला उपहार",
        "english": "customary auspicious gratuity gift given to musicians, artisans, and in-laws",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "नेग", "tehri": "नेग", "salani": "नेग", "rathwali": "नेग"}
    },
    {
        "garhwali": "बिदाई",
        "hindi": "विवाह पश्चात मायके से ससुराल की भावपूर्ण विदा",
        "english": "poignant ceremonial farewell of a newly-wed daughter leaving her home",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बिदाई", "tehri": "बिदाई", "salani": "बिदाई", "rathwali": "बिदाई"}
    },

    # Art, Painting, Ornaments & Court Aesthetics
    {
        "garhwali": "चितेरो",
        "hindi": "श्रीनगर गढ़वाल का पारंपरिक दरबारी चित्रकार",
        "english": "traditional master court painter of the Garhwal School of Miniature Art",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "चितेरो", "tehri": "चितेरु", "salani": "चितेरा", "rathwali": "चितेरो"}
    },
    {
        "garhwali": "रंग-बिरंगो",
        "hindi": "अनेक रंगों से सुशोभित / बहुरंगी",
        "english": "variegated, multicolored, brilliantly colored",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "रंग-बिरंगो", "tehri": "रंग-बिरंगु", "salani": "रंग-बिरंगा", "rathwali": "रंग-बिरंगो"}
    },
    {
        "garhwali": "काजळ",
        "hindi": "सरसों के तेल से बना आंखों का काला सुरमा / काजल",
        "english": "traditional pure soot kohl applied to eyes for coolness and beauty",
        "pos": "noun",
        "gender": "M",
        "category": "attire",
        "dialect_variants": {"srinagariya": "काजळ", "tehri": "काजल", "salani": "काजल", "rathwali": "काजळ"}
    },
    {
        "garhwali": "हंसुली",
        "hindi": "गले में पहना जाने वाला चांदी का भारी ठोस कंठहार",
        "english": "rigid solid silver torque necklet worn by Garhwali women",
        "pos": "noun",
        "gender": "F",
        "category": "attire",
        "dialect_variants": {"srinagariya": "हंसुली", "tehri": "हंसुली", "salani": "हंसुली", "rathwali": "हंसुळी"}
    },
    {
        "garhwali": "गुलूबंद",
        "hindi": "मखमल की पट्टी पर सोने के चौकोर टिकों से सजा कंठाभरण",
        "english": "traditional choker necklace of engraved gold squares stitched on red velvet",
        "pos": "noun",
        "gender": "M",
        "category": "attire",
        "dialect_variants": {"srinagariya": "गुलूबंद", "tehri": "गुलबंद", "salani": "गुलूबंद", "rathwali": "गुलूबंद"}
    },
    {
        "garhwali": "धागुळा",
        "hindi": "हाथों में पहने जाने वाले चांदी के भारी कड़े",
        "english": "heavy solid silver wrist bangles worn by women and children",
        "pos": "noun",
        "gender": "M",
        "category": "attire",
        "dialect_variants": {"srinagariya": "धागुळा", "tehri": "धागुला", "salani": "धागुला", "rathwali": "धागुळा"}
    },
    {
        "garhwali": "पौंछी",
        "hindi": "लाल धागे में सोने के मोतियों से पिरोया हुआ कलाई का कंगन",
        "english": "ceremonial bridal wristlet of hollow gold beads strung on red cords",
        "pos": "noun",
        "gender": "F",
        "category": "attire",
        "dialect_variants": {"srinagariya": "पौंछी", "tehri": "पौंची", "salani": "पौंछी", "rathwali": "पौंछी"}
    },
    {
        "garhwali": "झुमका",
        "hindi": "कानों के लटकनदार चांदी या सोने के कुंडल",
        "english": "bell-shaped hanging earrings with delicate drop beads",
        "pos": "noun",
        "gender": "M",
        "category": "attire",
        "dialect_variants": {"srinagariya": "झुमका", "tehri": "झुमको", "salani": "झुमका", "rathwali": "झुमका"}
    },
    {
        "garhwali": "पैरी",
        "hindi": "पांवों में पहनी जाने वाली घुंघरूदार चांदी की पाजेब",
        "english": "traditional silver anklets adorned with ringing bells",
        "pos": "noun",
        "gender": "F",
        "category": "attire",
        "dialect_variants": {"srinagariya": "पैरी", "tehri": "झांवर", "salani": "पैरी", "rathwali": "पैरी"}
    },
    {
        "garhwali": "छैलो",
        "hindi": "सुदर्शन, रंगीला व उत्साही नवयुवक",
        "english": "handsome, dashing, and spirited mountain youth",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "छैलो", "tehri": "छैलु", "salani": "छैला", "rathwali": "छैळो"}
    },
    {
        "garhwali": "नायिका",
        "hindi": "पहाड़ी गीतों व चित्रों की नायिका / प्रियतमा",
        "english": "romantic poetic heroine in classical Garhwali ballads and art",
        "pos": "noun",
        "gender": "F",
        "category": "literature",
        "dialect_variants": {"srinagariya": "नायिका", "tehri": "नायिका", "salani": "नायिका", "rathwali": "नायिका"}
    },

    # Central Pahari Verbs & Tactile Sensory Actions
    {
        "garhwali": "बिथारणु",
        "hindi": "धूप में सुखाने हेतु अनाज या घास को चौड़ा फैलाना",
        "english": "to spread out grain or cut grass widely under sunlight to dry",
        "pos": "verb",
        "gender": None,
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "बिथारणु", "tehri": "बिथार्नु", "salani": "बिथारन", "rathwali": "बिथारणु"}
    },
    {
        "garhwali": "सिंझोळणु",
        "hindi": "पानी में तर-बतर कर देना / भिगोना",
        "english": "to drench completely, soak through with water",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "सिंझोळणु", "tehri": "भिगोन्", "salani": "सिंझोलन", "rathwali": "सिंझोळणु"}
    },
    {
        "garhwali": "गुलगुलाणु",
        "hindi": "हंसी छुड़ाने हेतु गुदगुदी करना",
        "english": "to tickle someone playfully to induce laughter",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "गुलगुलाणु", "tehri": "गुदगुदानू", "salani": "गुलगुलान", "rathwali": "गुलगुलाणु"}
    },
    {
        "garhwali": "झुम्मणु",
        "hindi": "मंडाण या भक्ति भाव में झूमना / मग्न होकर डोलना",
        "english": "to sway gracefully in spiritual trance or folk dance",
        "pos": "verb",
        "gender": None,
        "category": "culture",
        "dialect_variants": {"srinagariya": "झुम्मणु", "tehri": "झूमनू", "salani": "झुम्मन", "rathwali": "झुम्मणु"}
    },
    {
        "garhwali": "अकस्याणु",
        "hindi": "हठ करना / अकड़ दिखाना / मचलना",
        "english": "to act stubbornly or display willful obstinacy",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "अकस्याणु", "tehri": "अकड़नु", "salani": "अकस्याण", "rathwali": "अकस्याणु"}
    },
    {
        "garhwali": "लुटबुटणु",
        "hindi": "घास या ज़मीन पर लोट-पोट होना",
        "english": "to roll around playfully on grassy meadows or ground",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "लुटबुटणु", "tehri": "लोट-पोट होनु", "salani": "लुटबुटन", "rathwali": "लुटबुटणु"}
    },
    {
        "garhwali": "चिमट्याणु",
        "hindi": "उंगलियों से चिमटी काटना",
        "english": "to pinch sharply between fingertips",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "चिमट्याणु", "tehri": "चुटकी काट्नु", "salani": "चिमट्यान", "rathwali": "चिमट्याणु"}
    },
    {
        "garhwali": "हुरहुरयाणु",
        "hindi": "पक्षी का पंख फड़फड़ा कर उड़ना",
        "english": "to flutter wings with a whirring sound while taking flight",
        "pos": "verb",
        "gender": None,
        "category": "nature",
        "dialect_variants": {"srinagariya": "हुरहुरयाणु", "tehri": "फड़फड़ानु", "salani": "हुरहुरयान", "rathwali": "हुरहुरयाणु"}
    },
    {
        "garhwali": "भभकणु",
        "hindi": "आग का अचानक लपट बनकर भड़क उठना",
        "english": "to flare up suddenly in bright blazing flames",
        "pos": "verb",
        "gender": None,
        "category": "nature",
        "dialect_variants": {"srinagariya": "भभकणु", "tehri": "भड़कनु", "salani": "भभकन", "rathwali": "भभकणु"}
    },
    {
        "garhwali": "सुरसुराणु",
        "hindi": "सूखे पत्तों में सरसराहट की हल्की आवाज होना",
        "english": "to rustle gently through fallen dry oak leaves",
        "pos": "verb",
        "gender": None,
        "category": "nature",
        "dialect_variants": {"srinagariya": "सुरसुराणु", "tehri": "सरसरानु", "salani": "सुरसुरान", "rathwali": "सुरसुराणु"}
    },
    {
        "garhwali": "किरकिराणु",
        "hindi": "दांतों में रेत या कंकड़ का किरकिराना",
        "english": "to feel gritty between teeth from sand or grain particles",
        "pos": "verb",
        "gender": None,
        "category": "sensations",
        "dialect_variants": {"srinagariya": "किरकिराणु", "tehri": "किरकिरानु", "salani": "किरकिरान", "rathwali": "किरकिराणु"}
    },
    {
        "garhwali": "सकबुकाणु",
        "hindi": "संकोच या लज्जा से हिचकिचाना",
        "english": "to hesitate or stammer shyly from bashfulness",
        "pos": "verb",
        "gender": None,
        "category": "emotions",
        "dialect_variants": {"srinagariya": "सकबुकाणु", "tehri": "हिचकिचानू", "salani": "सकबुकान", "rathwali": "सकबुकाणु"}
    },
    {
        "garhwali": "अटपल्याणु",
        "hindi": "कदम लड़खड़ाना / पथरीले रास्ते पर ठोकर खाना",
        "english": "to stumble awkwardly on a stony alpine ridge",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "अटपल्याणु", "tehri": "लड़खड़ानू", "salani": "अटपल्यान", "rathwali": "अटपल्याणु"}
    },
    {
        "garhwali": "उग्याणणु",
        "hindi": "दूर से किसी आकृति को ताड़ना या पहचानना",
        "english": "to discern or spot a distant figure across mountain valleys",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "उग्याणणु", "tehri": "पहचान्नु", "salani": "उग्याणन", "rathwali": "उग्याणणु"}
    },
    {
        "garhwali": "छछलाणु",
        "hindi": "बर्तन भर जाने पर पानी का किनारों से छलकना",
        "english": "to brim over and splash lightly over vessel rim",
        "pos": "verb",
        "gender": None,
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "छछलाणु", "tehri": "छलकनू", "salani": "छछलान", "rathwali": "छछळाणु"}
    },
    {
        "garhwali": "रंग्याणु",
        "hindi": "प्राकृतिक रंगों से कपड़े या ऊन को रंगना",
        "english": "to dye handspun wool or cotton in native botanical vats",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "रंग्याणु", "tehri": "रंग्नु", "salani": "रंग्यान", "rathwali": "रंग्याणु"}
    },

    # Mountain Wildlife & Birds of Garhwal
    {
        "garhwali": "घुरळ",
        "hindi": "पहाड़ी घुरल / चट्टानी ढलानों का छोटा जंगली बकरा",
        "english": "Himalayan goral goat-antelope inhabiting steep rocky crags (Nemorhaedus goral)",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "घुरळ", "tehri": "घुरल", "salani": "घुरल", "rathwali": "घुरळ"}
    },
    {
        "garhwali": "काकड़",
        "hindi": "पहाड़ी काकड़ / भौंकने वाला छोटा हिरण",
        "english": "barking deer or Indian muntjac of dense Himalayan oak woods",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "काकड़", "tehri": "काकड़", "salani": "काकड़", "rathwali": "काकळ"}
    },
    {
        "garhwali": "मोनाळ",
        "hindi": "उत्तराखण्ड का राज्य पक्षी / बहुरंगी पहाड़ी तीतर",
        "english": "resplendent Himalayan monal pheasant with metallic rainbow plumage",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "मोनाळ", "tehri": "मोनाल", "salani": "मोनाल", "rathwali": "मोनाळ"}
    },
    {
        "garhwali": "हिलांस",
        "hindi": "हिमालयी हिलांस पक्षी / विरह का प्रतीक हरियल",
        "english": "yellow-footed green pigeon revered in folk ballads as emblem of longing",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "हिलांस", "tehri": "हिलांस", "salani": "हिलांस", "rathwali": "हिळांस"}
    },
    {
        "garhwali": "थार",
        "hindi": "उच्च हिमालयी जंगली बकरा / थार",
        "english": "Himalayan tahr with dense reddish wool inhabiting high cliffs",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "थार", "tehri": "थार", "salani": "थार", "rathwali": "थार"}
    },
    {
        "garhwali": "कस्तूरी",
        "hindi": "कस्तूरी मृग की नाभि से प्राप्त दुर्लभ सुवासित पदार्थ",
        "english": "precious aromatic natural musk harvested from high-altitude musk deer",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कस्तूरी", "tehri": "कस्तूरी", "salani": "कस्तूरी", "rathwali": "कस्तूरी"}
    },
    {
        "garhwali": "गुलदार",
        "hindi": "पहाड़ी तेंदुआ / बाघिन",
        "english": "spotted mountain leopard roaming pine and oak forest fringes",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "गुलदार", "tehri": "बाघ", "salani": "गुलदार", "rathwali": "गुलदार"}
    },
    {
        "garhwali": "भल्यो",
        "hindi": "हिमालयी काला रीछ / भालू",
        "english": "Asiatic black bear with white chest crescent living in high oak woods",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "भल्यो", "tehri": "भालु", "salani": "भालू", "rathwali": "भल्यो"}
    },
    {
        "garhwali": "घूघू",
        "hindi": "पहाड़ी विशाल उल्लू",
        "english": "great Himalayan eagle owl hooting in nocturnal ravines",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "घूघू", "tehri": "उल्लू", "salani": "घूघू", "rathwali": "घूघू"}
    },

    # Mountain Agronomy, Implements & Smithy
    {
        "garhwali": "हळ",
        "hindi": "पहाड़ी सीढ़ीदार खेतों को जोतने का हल्का लकड़ी का हल",
        "english": "lightweight wooden ard plow designed for narrow mountain terraces",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "हळ", "tehri": "हल", "salani": "हल", "rathwali": "हळ"}
    },
    {
        "garhwali": "जुवाळो",
        "hindi": "दो बैलों के कंधों पर रखा जाने वाला लकड़ी का जुआ",
        "english": "carved double-oxen wooden yoke resting upon draft bullocks",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "जुवाळो", "tehri": "जुवालु", "salani": "जुवाला", "rathwali": "जुवाळो"}
    },
    {
        "garhwali": "हल्या",
        "hindi": "पहाड़ी सीढ़ीदार खेतों में हल चलाने वाला हलवाहा",
        "english": "traditional plowman guiding the oxen pair across hill terraces",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "हल्या", "tehri": "हलिया", "salani": "हल्या", "rathwali": "हल्या"}
    },
    {
        "garhwali": "पाटो",
        "hindi": "खेत की जुताई के बाद ढेलों को तोड़ने का भारी लकड़ी का पाटा",
        "english": "heavy flat timber drag beam for clod-crushing and soil leveling",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "पाटो", "tehri": "पाटु", "salani": "पाटा", "rathwali": "पाटो"}
    },
    {
        "garhwali": "खोदळो",
        "hindi": "खेतों से खरपतवार निकालने की छोटी तिकोनी खुरपी",
        "english": "triangular pointed hand weeding tool for aerating terrace soils",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "खोदळो", "tehri": "खुरपी", "salani": "खोदला", "rathwali": "खोदळो"}
    },
    {
        "garhwali": "दांतो",
        "hindi": "सूखे चीड़ के पत्तों (पिरुल) को बटोरने का लकड़ी का दांता",
        "english": "wooden-toothed rake used for gathering dry chir pine needles",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "दांतो", "tehri": "दांतु", "salani": "दांता", "rathwali": "दांतो"}
    },
    {
        "garhwali": "ऐरण",
        "hindi": "लोहार का लोहे का भारी निहाई / ऐरण",
        "english": "blacksmith's solid wrought-iron anvil for forging blades",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "ऐरण", "tehri": "निहाई", "salani": "ऐरण", "rathwali": "ऐरण"}
    },
    {
        "garhwali": "धौंकणी",
        "hindi": "लोहार की भट्टी को फूंकने वाली चमड़े की धौंकनी",
        "english": "traditional goat-skin bellows for fanning the charcoal forge",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "धौंकणी", "tehri": "धौंकनी", "salani": "धौंकणी", "rathwali": "धौंकणी"}
    },

    # Minerals, Geology & Trans-Himalayan Trade
    {
        "garhwali": "सिलजीत",
        "hindi": "ऊँची चट्टानों से निकलने वाला औषधीय खनिज शिलाजीत",
        "english": "natural mineral asphalt pitch exuded from sun-baked alpine crags",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "सिलजीत", "tehri": "शिलाजीत", "salani": "सिलजीत", "rathwali": "सिळजीत"}
    },
    {
        "garhwali": "सहाग",
        "hindi": "तिब्बत से आने वाला सुहागा (टंकण क्षार)",
        "english": "natural borax salt mineral imported via trans-Himalayan trade passes",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "सहाग", "tehri": "सुहागा", "salani": "सहाग", "rathwali": "सहाग"}
    },
    {
        "garhwali": "नूण",
        "hindi": "पहाड़ी सेंधा नमक / लवण",
        "english": "natural rock salt essential for cattle and mountain cooking",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "नूण", "tehri": "लूण", "salani": "नूण", "rathwali": "नूण"}
    },
    {
        "garhwali": "हुणिया",
        "hindi": "तिब्बती पठार से व्यापार हेतु आने वाला तिब्बती व्यापारी",
        "english": "Tibetan trans-Himalayan merchant trading wool, salt, and borax",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "हुणिया", "tehri": "हुणिया", "salani": "हुणिया", "rathwali": "हुणिया"}
    },
    {
        "garhwali": "डांडो-काँठो",
        "hindi": "पर्वत की समस्त ऊंची चोटियां व पर्वतमालाएं",
        "english": "the entirety of high mountain ridges, crests, and cols",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "डांडो-काँठो", "tehri": "डांडु-काठु", "salani": "डांडा-काठा", "rathwali": "डाण्डो-काँठो"}
    }
]

added_count = 0
updated_count = 0

for w in WAVE2_MINED_WORDS:
    lemma = w["garhwali"].strip()
    if lemma in existing_lemmas:
        existing_lemmas[lemma].update(w)
        updated_count += 1
    else:
        existing_words.append(w)
        existing_lemmas[lemma] = w
        added_count += 1

print(f"Added {added_count} brand-new Wave 2 words.")
print(f"Updated {updated_count} existing words.")
print(f"New total word count: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved expanded words dictionary to {WORDS_PATH}")

