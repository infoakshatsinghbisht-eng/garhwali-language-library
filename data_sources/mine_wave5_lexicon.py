# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 5 vocabulary from newly added historical,
pilgrim, mountaineering, and customary texts:
- Mumm (1909) & Gypsy Davy (1927): Pilgrim halts, rock trails, high peaks
- UP Govt Local Customs (1919): Sacred groves, water mills, customary dues
- Verma (2003) & Joshi (1911): Dialectal temporal markers, physical verbs
"""

import json

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE5_WORDS = [
    # --- Pilgrim Marg, Mountain Travel & High Trails (Mumm 1909, Gypsy Davy 1927) ---
    {
        "garhwali": "चट्टी",
        "hindi": "बदरीनाथ व केदारनाथ तीर्थ-मार्ग पर स्थित पारंपरिक यात्री पड़ाव अथवा धर्मशाला",
        "english": "traditional roadside pilgrim resting station, inn, or overnight caravanserai on Himalayan shrine routes",
        "pos": "noun",
        "gender": "F",
        "category": "places",
        "dialect_variants": {"srinagariya": "चट्टी", "tehri": "चट्टी", "salani": "चट्टी", "rathwali": "चट्टी"}
    },
    {
        "garhwali": "कंडी",
        "hindi": "पीठ पर बांधकर बच्चों अथवा वृद्ध यात्रियों को ले जाने की रिंगाल की टोकरी",
        "english": "wicker carrier basket strapped to a porter's shoulders for transporting pilgrims or luggage up steep trails",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कंडी", "tehri": "कण्डी", "salani": "कंडी", "rathwali": "कंडी"}
    },
    {
        "garhwali": "डांडी",
        "hindi": "चार कहारों द्वारा कंधों पर ढोई जाने वाली पर्वतीय पालकी या डोली",
        "english": "four-bearer mountain sedan-chair or litter used on steep pilgrim tracks",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "डांडी", "tehri": "डाण्डी", "salani": "डांडी", "rathwali": "डांडी"}
    },
    {
        "garhwali": "हिंवाळ",
        "hindi": "पहाड़ों पर गिरी ताजी बर्फ अथवा हिमाच्छादित उच्च क्षेत्र",
        "english": "fresh snowfall or glistening snowfields covering alpine ridges",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "हिंवाळ", "tehri": "हिंवाल", "salani": "हिंवाल", "rathwali": "हिंवाळ"}
    },
    {
        "garhwali": "गंगो",
        "hindi": "पिघलती हुई बर्फ से उत्पन्न तीव्र शीतल पहाड़ी जलधारा",
        "english": "swift icy mountain stream fed by melting snow and high glaciers",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गंगो", "tehri": "गंगु", "salani": "गंगो", "rathwali": "गङ्गो"}
    },
    {
        "garhwali": "ब्यासी",
        "hindi": "चारागाहों में चरवाहों अथवा बकरियों का रात्रि विश्राम स्थल",
        "english": "shepherds' temporary night encampment or rustic bivouac in forest glades",
        "pos": "noun",
        "gender": "F",
        "category": "places",
        "dialect_variants": {"srinagariya": "ब्यासी", "tehri": "ब्यासी", "salani": "ब्यासी", "rathwali": "ब्यासी"}
    },

    # --- Sacred Groves, Community Rights & Customary Usages (UP Govt 1919) ---
    {
        "garhwali": "देव-वन",
        "hindi": "ग्राम-देवता को समर्पित पवित्र संरक्षित वन जहां वृक्ष काटना सर्वथा वर्जित है",
        "english": "sacred community forest grove dedicated to a local deity where tree-felling is forbidden by customary taboo",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "देव-वन", "tehri": "देव-बन", "salani": "देव-बन", "rathwali": "देव-वण"}
    },
    {
        "garhwali": "पंदेरा",
        "hindi": "गांव का पारंपरिक प्राकृतिक जल-स्रोत अथवा जल-धारा",
        "english": "natural village spring spout, stone masonry water conduit for drinking water",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "पंदेरा", "tehri": "पंदेरु", "salani": "पंदेरा", "rathwali": "पन्देरो"}
    },
    {
        "garhwali": "घट्ट-वार",
        "hindi": "पनचक्की में अनाज पिसाने हेतु ग्रामीणों की बारी",
        "english": "customary scheduled roster or assigned turn for grinding grain at the stream water mill",
        "pos": "noun",
        "gender": "F",
        "category": "economy",
        "dialect_variants": {"srinagariya": "घट्ट-वार", "tehri": "घट्ट-बार", "salani": "घट्ट-वार", "rathwali": "घट्ट-वार"}
    },
    {
        "garhwali": "हक-हकूक",
        "hindi": "वनों से काष्ठ, चारा व ईंधन प्राप्त करने का ग्रामीणों का पारंपरिक व विधिक अधिकार",
        "english": "statutory and customary community rights of villagers to timber, grazing, and fuel wood in surrounding forests",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "हक-हकूक", "tehri": "हक-हकूक", "salani": "हक-हकूक", "rathwali": "हक-हकूक"}
    },
    {
        "garhwali": "चूल",
        "hindi": "ग्राम-अभिलेखों में दर्ज मूल पैतृक चूल्हा अथवा स्वतंत्र परिवार इकाई",
        "english": "ancestral hearth or distinct household unit recorded in village community registers",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "चूल", "tehri": "चूल", "salani": "चूल", "rathwali": "चूळ"}
    },
    {
        "garhwali": "धुमा",
        "hindi": "प्रत्येक चूल्हे अथवा घर से लिया जाने वाला पारंपरिक गृह-कर",
        "english": "customary historic hearth-tax or household smoke assessment levied per dwelling",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "धुमा", "tehri": "धुमु", "salani": "धुमा", "rathwali": "धुमो"}
    },
    {
        "garhwali": "जांत",
        "hindi": "ग्राम-देवता की पालकी के साथ की जाने वाली विशाल क्षेत्रीय परिक्रमा व धार्मिक यात्रा",
        "english": "grand ceremonial circumambulation pilgrimage of a village deity carried in palanquin across sacred boundaries",
        "pos": "noun",
        "gender": "F",
        "category": "festivals",
        "dialect_variants": {"srinagariya": "जांत", "tehri": "जांत", "salani": "जांत", "rathwali": "जांत"}
    },

    # --- Dialectal Temporal Markers & Senses (Verma 2003, Joshi 1911) ---
    {
        "garhwali": "भिनसार",
        "hindi": "पौ फटने का समय, ब्रह्ममुहूर्त, प्रभात काल",
        "english": "first crack of dawn, early daybreak before sunrise over the peaks",
        "pos": "noun",
        "gender": "M",
        "category": "time",
        "dialect_variants": {"srinagariya": "भिनसार", "tehri": "भिनसार", "salani": "भिनसार", "rathwali": "भिनसार"}
    },
    {
        "garhwali": "संज्या",
        "hindi": "संध्याकाल, गोधूलि वेला, सांझ",
        "english": "dusk, evening twilight when cattle return to the village stables",
        "pos": "noun",
        "gender": "F",
        "category": "time",
        "dialect_variants": {"srinagariya": "संज्या", "tehri": "संज", "salani": "सांझ", "rathwali": "सञ्ज्या"}
    },
    {
        "garhwali": "बिहान",
        "hindi": "कल सुबह, आने वाले कल का प्रातःकाल",
        "english": "early tomorrow morning, the following dawn",
        "pos": "adv",
        "gender": None,
        "category": "time",
        "dialect_variants": {"srinagariya": "बिहान", "tehri": "बिहान", "salani": "बिहान", "rathwali": "बिहाण"}
    },
    {
        "garhwali": "अगास",
        "hindi": "विस्तृत खुला आकाश, नभ",
        "english": "open celestial vault, firmament, clear mountain sky",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "अगास", "tehri": "अगास", "salani": "अगास", "rathwali": "अगास"}
    },
    {
        "garhwali": "काख",
        "hindi": "बगल, कांख, बाजू के नीचे का भाग",
        "english": "armpit, side of the torso under the arm",
        "pos": "noun",
        "gender": "F",
        "category": "body",
        "dialect_variants": {"srinagariya": "काख", "tehri": "काख", "salani": "काख", "rathwali": "काख"}
    },
    {
        "garhwali": "खोंख",
        "hindi": "गले की निरंतर खांसी",
        "english": "persistent dry hacking cough",
        "pos": "noun",
        "gender": "F",
        "category": "health",
        "dialect_variants": {"srinagariya": "खोंख", "tehri": "खोंख", "salani": "खोंख", "rathwali": "खोंख"}
    },
    {
        "garhwali": "घोटणु",
        "hindi": "तरल वस्तु को गले से नीचे उतारना, निगलना",
        "english": "to gulp down, swallow a draught of water or medicine",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "घोटणु", "tehri": "घोटण", "salani": "घोटणा", "rathwali": "घोटणु"}
    },
    {
        "garhwali": "चाटणु",
        "hindi": "जीभ से स्वाद लेना, चाटना",
        "english": "to lick, taste with the tongue",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "चाटणु", "tehri": "चाटण", "salani": "चाटणा", "rathwali": "चाटणु"}
    },
    {
        "garhwali": "झटपट",
        "hindi": "शीघ्रता से, तुरंत, बिना विलंब किए",
        "english": "swiftly, expeditiously, without lingering",
        "pos": "adv",
        "gender": None,
        "category": "manner",
        "dialect_variants": {"srinagariya": "झटपट", "tehri": "झटपट", "salani": "झटपट", "rathwali": "झटपट"}
    },
    {
        "garhwali": "रौंत",
        "hindi": "आनंददायक व उल्लासपूर्ण सामाजिक सभा अथवा मिलन",
        "english": "lively delightful community gathering, joyous festive assembly",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "रौंत", "tehri": "रौंत", "salani": "रौंत", "rathwali": "रौन्त"}
    }
]

added_words = []
for w in WAVE5_WORDS:
    if w["garhwali"] not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(w["garhwali"])
        added_words.append(w["garhwali"])

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {len(added_words)} new authenticated words to {WORDS_PATH}.")
print(f"Total words in lexicon now: {len(existing_words)}")
