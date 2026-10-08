# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline extracting heroic, cultural, and ceremonial vocabulary
from Govind Chatak (1958) 'Gadwali Lok Gathayen' (Pawadas & Jagar Epics)
and Haridatta Bhatt (1976).
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

EPIC_WORDS = [
    {
        "garhwali": "कवच",
        "hindi": "युद्ध में शरीर की रक्षा करने वाला लोहे का बख्तर",
        "english": "warrior's iron armor breastplate",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कवच", "tehri": "बख्तर", "salani": "कवच", "rathwali": "कवच"}
    },
    {
        "garhwali": "शिरस्त्राण",
        "hindi": "योद्धा के सिर का लोहे का टोप",
        "english": "warrior's iron battle helmet",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "शिरस्त्राण", "tehri": "टोप", "salani": "हेलमेट", "rathwali": "शिरस्त्राण"}
    },
    {
        "garhwali": "तीर-धनुष",
        "hindi": "धनुष और बाण",
        "english": "bow and arrow",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "तीर-धनुष", "tehri": "कमान-तीर", "salani": "धनुष-बाण", "rathwali": "तीर-धनुष"}
    },
    {
        "garhwali": "तरकश",
        "hindi": "पीठ पर बाण रखने का भाथा / तरकश",
        "english": "arrow quiver carried on warrior's shoulder",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "तरकश", "tehri": "तरकश", "salani": "भाथा", "rathwali": "तरकश"}
    },
    {
        "garhwali": "घोड़साल",
        "hindi": "युद्ध के घोड़ों की अश्वशाला / अस्तबल",
        "english": "cavalry warhorse stable",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "घोड़साल", "tehri": "अस्तबल", "salani": "तबेला", "rathwali": "घोड़साळ"}
    },
    {
        "garhwali": "नगाड़ा",
        "hindi": "किले व मंदिर का भारी युद्ध नगाड़ा",
        "english": "large war kettle-drum / ceremonial nagada",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "नगाड़ा", "tehri": "नगाड़ा", "salani": "नक्कारा", "rathwali": "नगाळा"}
    },
    {
        "garhwali": "रणसिंघा",
        "hindi": "युद्ध व जागर का लंबा तांबे का घुमावदार वाद्य",
        "english": "curved S-shaped brass war trumpet",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "रणसिंघा", "tehri": "रणसिंगा", "salani": "तुरही", "rathwali": "रणसिंघा"}
    },
    {
        "garhwali": "दमाऊं",
        "hindi": "ढोल के साथ बजने वाला छोटा धातु का तालवाद्य",
        "english": "shallow hemispherical copper kettledrum (Damau)",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "दमाऊं", "tehri": "दमामा", "salani": "दमाऊं", "rathwali": "दमाऊं"}
    },
    {
        "garhwali": "कांस्य-थाली",
        "hindi": "डौंर के साथ ताल देने वाली कांसे की थाली",
        "english": "bronze plate cymbal struck with stick in jagar rituals",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "कांस्य-थाली", "tehri": "कांसी-थाली", "salani": "थाली", "rathwali": "कांस्य-थाळी"}
    },
    {
        "garhwali": "सुआ",
        "hindi": "पहाड़ी लोकगीतों का संदेशवाहक तोता",
        "english": "messenger parrot of mountain folk ballads",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "सुआ", "tehri": "सुग्गा", "salani": "तोता", "rathwali": "सुआ"}
    },
    {
        "garhwali": "चिठी-पाती",
        "hindi": "संदेश पत्र / कुशलक्षेम की चिट्ठी",
        "english": "handwritten letter / welfare news missive",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "चिठी-पाती", "tehri": "चिट्ठी", "salani": "पत्र", "rathwali": "चिठी-पाती"}
    },
    {
        "garhwali": "डाक्यु",
        "hindi": "गांव-गांव संदेश पहुंचाने वाला हरकारा / डाकिया",
        "english": "traditional mountain foot postman / runner",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "डाक्यु", "tehri": "डाकिया", "salani": "हरकारा", "rathwali": "डाक्यु"}
    },
    {
        "garhwali": "दानी",
        "hindi": "उदार हृदय / परोपकारी दानी",
        "english": "generous patron / philanthropic donor",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "दानी", "tehri": "दानी", "salani": "उदार", "rathwali": "दाणी"}
    },
    {
        "garhwali": "बलिदानी",
        "hindi": "मातृभूमि पर न्योछावर होने वाला अमर शहीद",
        "english": "martyr who sacrifices life for homeland",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "बलिदानी", "tehri": "शहीद", "salani": "बलिदानी", "rathwali": "बळिदाणी"}
    },
    {
        "garhwali": "वीर-गाथा",
        "hindi": "शौर्य व युद्ध का प्राचीन पवाड़ा गीत",
        "english": "heroic martial folk epic ballad (Pawada)",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "वीर-गाथा", "tehri": "पवाड़ा", "salani": "लोकगाथा", "rathwali": "वीर-गाथा"}
    },
    {
        "garhwali": "शौर्य",
        "hindi": "अदम्य पराक्रम व वीरता",
        "english": "indomitable bravery / battlefield valor",
        "pos": "noun",
        "gender": "M",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "शौर्य", "tehri": "वीरता", "salani": "बहादुरी", "rathwali": "शौर्य"}
    },
    {
        "garhwali": "कीर्ति",
        "hindi": "यश / ख्याति / यशोगान",
        "english": "enduring fame / glory / renown",
        "pos": "noun",
        "gender": "F",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "कीर्ति", "tehri": "यश", "salani": "नाम", "rathwali": "कीर्ति"}
    },
    {
        "garhwali": "अमर",
        "hindi": "जो कभी न मरे / शाश्वत",
        "english": "immortal / eternal",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "अमर", "tehri": "अविनाशी", "salani": "अमर", "rathwali": "अमर"}
    },
    {
        "garhwali": "सती-शिला",
        "hindi": "सती होने वाली वीरांगना का नक्काशीदार स्मृति पत्थर",
        "english": "memorial stone pillar dedicated to heroic faithful woman",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "सती-शिला", "tehri": "सती-स्तंभ", "salani": "शिला", "rathwali": "सती-शिळा"}
    },
    {
        "garhwali": "भड़-शिला",
        "hindi": "वीर योद्धा का युद्ध स्मारक पत्थर",
        "english": "hero stone monument honoring fallen warrior champion",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भड़-शिला", "tehri": "वीर-पत्थर", "salani": "स्मारक", "rathwali": "भड़-शिळा"}
    },
    {
        "garhwali": "चौंतरा",
        "hindi": "पीपल या बरगद के पेड़ के नीचे बना पत्थरों का चबूतरा",
        "english": "paved stone platform around village banyan or pipal tree",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "चौंतरा", "tehri": "चबूतरा", "salani": "चौंतरा", "rathwali": "चौंतरा"}
    },
    {
        "garhwali": "गौड़",
        "hindi": "कुल / वंश / गोत्र",
        "english": "ancestral lineage / clan sept",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "गौड़", "tehri": "गोत्र", "salani": "कुल", "rathwali": "गौड़"}
    },
    {
        "garhwali": "जनेऊ",
        "hindi": "पवित्र सूत का यज्ञोपवीत धागा",
        "english": "sacred ritual investiture thread (Yajnopavita)",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "जनेऊ", "tehri": "जनेऊ", "salani": "जनेउ", "rathwali": "जनेऊ"}
    },
    {
        "garhwali": "तिलक",
        "hindi": "माथे पर लगाया जाने वाला चंदन का टीका",
        "english": "sandalwood paste forehead mark",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "तिलक", "tehri": "टीका", "salani": "तिलक", "rathwali": "तिळक"}
    },
    {
        "garhwali": "पंचांग",
        "hindi": "तिथि, वार, नक्षत्र आदि बताने वाला पारंपरिक पंचांग",
        "english": "traditional Hindu astrological calendar ephemeris",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "पंचांग", "tehri": "पत्री", "salani": "पंचांग", "rathwali": "पंचांग"}
    },
    {
        "garhwali": "मुहूर्त",
        "hindi": "मांगलिक कार्यों का शुभ समय",
        "english": "auspicious astrological hour / right moment",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "मुहूर्त", "tehri": "सायत", "salani": "मुहूर्त", "rathwali": "मुहूर्त"}
    },
    {
        "garhwali": "लगन",
        "hindi": "विवाह की शुभ लग्न पत्रिका",
        "english": "auspicious wedding horoscope and date document",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "लगन", "tehri": "लग्न", "salani": "लगन", "rathwali": "ळगन"}
    },
    {
        "garhwali": "नेग-चार",
        "hindi": "विवाह व उत्सवों में दिया जाने वाला पारंपरिक नेग",
        "english": "customary ceremonial token cash gifts given to relatives",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "नेग-चार", "tehri": "नेग", "salani": "दस्तूर", "rathwali": "नेग-चार"}
    },
    {
        "garhwali": "बरात",
        "hindi": "वर पक्ष की विवाह बारात",
        "english": "groom's wedding procession",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बरात", "tehri": "बारात", "salani": "बरात", "rathwali": "बरात"}
    },
    {
        "garhwali": "जनेती",
        "hindi": "वर पक्ष की बारात में आए हुए बाराती",
        "english": "wedding guests of the groom's procession",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "जनेती", "tehri": "बराती", "salani": "जनेती", "rathwali": "जनेती"}
    },
    {
        "garhwali": "घराती",
        "hindi": "कन्या पक्ष के सम्बन्धी व मेजबान",
        "english": "bridal host family members hosting the wedding",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "घराती", "tehri": "घराती", "salani": "मेजबान", "rathwali": "घराती"}
    },
    {
        "garhwali": "बिदाई",
        "hindi": "विवाह के उपरांत वधू की मायके से विदाई",
        "english": "emotional bridal farewell ceremony leaving parental home",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बिदाई", "tehri": "विदा", "salani": "रुक्सत", "rathwali": "बिदाई"}
    },
    {
        "garhwali": "डोली-कहार",
        "hindi": "पहाड़ों में दुल्हन की डोली उठाने वाले कहार",
        "english": "traditional palanquin-bearers carrying bride's doli",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "डोली-कहार", "tehri": "कहार", "salani": "डोलीदार", "rathwali": "डोळी-कहार"}
    },
    {
        "garhwali": "कलेऊ",
        "hindi": "प्रातःकाल का पहला कलेवा / नाश्ता",
        "english": "morning breakfast / early dawn meal",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "कलेऊ", "tehri": "कलेवा", "salani": "नाश्ता", "rathwali": "कळेऊ"}
    },
    {
        "garhwali": "दुपहरी",
        "hindi": "दोपहर का मध्याह्न भोजन",
        "english": "midday luncheon meal",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "दुपहरी", "tehri": "दोपहरी", "salani": "दोपहर-भात", "rathwali": "दुपहरी"}
    },
    {
        "garhwali": "ब्यालू",
        "hindi": "शाम का रात्रि-भोज",
        "english": "evening dinner / night meal",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "ब्यालू", "tehri": "ब्यालू", "salani": "रात-खाना", "rathwali": "ब्याळू"}
    },
    {
        "garhwali": "सगूणी",
        "hindi": "शुभ शकुन वाला / मंगलकारी",
        "english": "auspicious / portending good omen",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सगूणी", "tehri": "सगुनी", "salani": "शुभ", "rathwali": "सगूणी"}
    },
    {
        "garhwali": "कुशगुणी",
        "hindi": "अशुभ शकुन वाला / अमंगलकारी",
        "english": "inauspicious / portending evil omen",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "कुशगुणी", "tehri": "अपशगुनी", "salani": "अशुभ", "rathwali": "कुशगूणी"}
    },
    {
        "garhwali": "परभात",
        "hindi": "प्रभात / भोर का समय",
        "english": "early morning dawn break",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "परभात", "tehri": "प्रभात", "salani": "सवेरा", "rathwali": "परभात"}
    },
    {
        "garhwali": "निसीथ",
        "hindi": "मध्य रात्रि / आधी रात",
        "english": "dead of night / midnight",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "निसीथ", "tehri": "अधीरात", "salani": "आधी-रात", "rathwali": "निसीथ"}
    },
    {
        "garhwali": "झकोरा",
        "hindi": "पहाड़ी तेज हवा का झोंका",
        "english": "gust of violent mountain wind",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "झकोरा", "tehri": "झोंका", "salani": "हवा-झोंका", "rathwali": "झकोरा"}
    },
    {
        "garhwali": "छछ्याट",
        "hindi": "मूसलाधार वर्षा की सनसनाहट",
        "english": "hissing roar of torrential mountain downpour",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "छछ्याट", "tehri": "झमाझम", "salani": "झड़ी", "rathwali": "छछ्याट"}
    },
    {
        "garhwali": "गड़गड़ाहट",
        "hindi": "बादलों की भीषण गड़गड़ाहट",
        "english": "crashing boom of thunder in the mountains",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गड़गड़ाहट", "tehri": "गरज", "salani": "गरजना", "rathwali": "गड़गड़ाहट"}
    },
    {
        "garhwali": "बौछार",
        "hindi": "हवा के साथ आने वाली वर्षा की फुहार",
        "english": "wind-driven driving rain shower spray",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बौछार", "tehri": "फुहार", "salani": "बौछार", "rathwali": "बौछार"}
    }
]

added = 0
enriched = 0

for item in EPIC_WORDS:
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

print(f"Epic mining added: {added}")
print(f"Enriched: {enriched}")
print(f"Total word count now: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved words to {WORDS_PATH}")
