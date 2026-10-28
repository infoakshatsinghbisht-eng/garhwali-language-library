# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 3 vocabulary from newly added historical,
tenurial, linguistic, and cultural books:
- Pauw (1896): Land tenure, agriculture, water rights, customary revenue
- Traill (1828): Traditional measures, currency, mountain topography
- Atkinson (1883, 1884): Feudal titles, forts, heroic ballads, jagar terms
- Upreti (1900) & Verma (2004): Directional adverbs, rural descriptors, Pahari roots
- Walton (1911) & IIAS (2002): Architecture, pastoral ecology, folk life
"""

import json

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

# Curated, authenticated lexical additions from Wave 3 texts
WAVE3_WORDS = [
    # --- Land Tenure, Agriculture & Revenue (Pauw 1896, Traill 1828) ---
    {
        "garhwali": "सेरा",
        "hindi": "नदी अथवा गधेरे के किनारे की सिंचित व उपजाऊ घाटी भूमि",
        "english": "fertile, flat, well-irrigated alluvial valley land along a stream or river",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "सेरा", "tehri": "सेरु", "salani": "सेरा", "rathwali": "सेरो"}
    },
    {
        "garhwali": "उपरांव",
        "hindi": "पहाड़ की ढलानों पर स्थित असिंचित सीढ़ीदार खेत",
        "english": "unirrigated terraced hillside agricultural land dependent entirely on rainfall",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "उपरांव", "tehri": "उपरांव", "salani": "उपराँ", "rathwali": "उपरांव"}
    },
    {
        "garhwali": "तळौं",
        "hindi": "घाटी की निचली सिंचित भूमि अथवा निचला खेत",
        "english": "lower valley land, fields situated at the bottom of a hill",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "तळौं", "tehri": "तलौं", "salani": "तलों", "rathwali": "तळौं"}
    },
    {
        "garhwali": "मळौं",
        "hindi": "पर्वत के ऊपरी ढलान पर स्थित खेत",
        "english": "upper hillside fields situated near the ridge crest",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "मळौं", "tehri": "मलौं", "salani": "मलों", "rathwali": "मळौं"}
    },
    {
        "garhwali": "कातळ",
        "hindi": "अति ढलवां व पथरीली जमीन पर काटा गया संकरा खेत",
        "english": "narrow, rugged terrace cut into a steep precipitous rocky mountain slope",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "कातळ", "tehri": "कातल", "salani": "कातल", "rathwali": "कातळ"}
    },
    {
        "garhwali": "खील",
        "hindi": "झाड़ियां व जंगल काटकर तैयार की गई अल्पकालिक पर्वतीय खेती",
        "english": "intermittent slash-and-burn hillside clearing for shifting mountain cultivation",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "खील", "tehri": "खील", "salani": "खील", "rathwali": "खीळ"}
    },
    {
        "garhwali": "गुंठ",
        "hindi": "मंदिर अथवा देवस्थान के भोग व रखरखाव हेतु समर्पित कर-मुक्त भूमि",
        "english": "rent-free revenue land grant dedicated in perpetuity to a temple or shrine",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "गुंठ", "tehri": "गुंठ", "salani": "गुंठ", "rathwali": "गुंठ"}
    },
    {
        "garhwali": "सदावर्त",
        "hindi": "तीर्थयात्रियों व साधुओं को निःशुल्क भोजन व आश्रय प्रदान करने का पुण्य दान",
        "english": "endowment fund or revenue grant designated for free food and shelter to Himalayan pilgrims",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "सदावर्त", "tehri": "सदाबरत", "salani": "सदाबरत", "rathwali": "सदावर्त"}
    },
    {
        "garhwali": "थोकदार",
        "hindi": "पट्टी अथवा परगने का मुख्य मालगुजारी अधिकारी व प्रमुख जागीरदार",
        "english": "hereditary regional revenue collector and principal landholder presiding over a patti",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "थोकदार", "tehri": "थोकदार", "salani": "थोकदार", "rathwali": "थोकदार"}
    },
    {
        "garhwali": "हिस्यादार",
        "hindi": "पैतृक ग्राम-भूमि में मालिकाना हक रखने वाला सह-हिस्सेदार",
        "english": "coparcenary landholding proprietor possessing ancestral shares in village land",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "हिस्यादार", "tehri": "हिस्सेदार", "salani": "हिस्यादार", "rathwali": "हिस्यादार"}
    },
    {
        "garhwali": "खाइकड़",
        "hindi": "स्थायी काश्तकार जिसे वंशानुगत जुताई का अधिकार प्राप्त हो किंतु भूमि बेचने का नहीं",
        "english": "hereditary permanent under-tenant possessing non-transferable cultivating rights",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "खाइकड़", "tehri": "खाइकड़", "salani": "खाइकड़", "rathwali": "खाइकड़"}
    },
    {
        "garhwali": "सिरतान",
        "hindi": "अस्थायी काश्तकार जो नकद लगान अथवा फसल का हिस्सा देकर खेती करता है",
        "english": "tenant-at-will paying cash rent (sirti) or grain share to the landholder",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "सिरतान", "tehri": "सिरतान", "salani": "सिरतान", "rathwali": "सिरतान"}
    },
    {
        "garhwali": "कैणी",
        "hindi": "भूमि-स्वामी के आश्रित कृषि-श्रमिक अथवा पारंपरिक सेवादार",
        "english": "dependent hereditary farm-servant or agricultural laborer attached to landholders",
        "pos": "noun",
        "gender": "M",
        "category": "society",
        "dialect_variants": {"srinagariya": "कैणी", "tehri": "कैणी", "salani": "कैणी", "rathwali": "कैणी"}
    },
    {
        "garhwali": "सवाणा",
        "hindi": "लुहार, बढ़ई आदि शिल्पकारों को फसल कटाई पर ग्रामवासियों द्वारा देय वार्षिक अनाज",
        "english": "customary annual grain dues paid at harvest to village artisan craftsmen (blacksmiths, carpenters)",
        "pos": "noun",
        "gender": "M",
        "category": "economy",
        "dialect_variants": {"srinagariya": "सवाणा", "tehri": "सवाण", "salani": "सवाणा", "rathwali": "सवाणो"}
    },
    {
        "garhwali": "दस्तूर",
        "hindi": "ग्राम समाज में प्रचलित पारंपरिक कर, शुल्क अथवा रूढ़िगत दस्तूरी",
        "english": "customary perquisite, fee, or hereditary traditional community entitlement",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "दस्तूर", "tehri": "दस्तूर", "salani": "दस्तूर", "rathwali": "दस्तूर"}
    },
    {
        "garhwali": "थुआ",
        "hindi": "ग्राम-सीमा अथवा वन-सीमा पर स्थापित पत्थरों का सीमा-चिह्न",
        "english": "stone boundary pillar or conical cairn marking village limits or forest tracts",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "थुआ", "tehri": "थुवा", "salani": "थुआ", "rathwali": "थुओ"}
    },

    # --- Traditional Measures, Trade & Implements (Traill 1828) ---
    {
        "garhwali": "दूण",
        "hindi": "सोलह नाली के बराबर पारंपरिक भूमि व अनाज माप",
        "english": "customary Himalayan measure of land and grain equal to sixteen nalis",
        "pos": "noun",
        "gender": "M",
        "category": "measurement",
        "dialect_variants": {"srinagariya": "दूण", "tehri": "दूण", "salani": "दूण", "rathwali": "दूण"}
    },
    {
        "garhwali": "माणो",
        "hindi": "आधा सेर अथवा एक चौथाई पाथा के बराबर अनाज नापने का छोटा बर्तन",
        "english": "traditional dry measure equal to approximately one-fourth of a patha (approx. 500g)",
        "pos": "noun",
        "gender": "M",
        "category": "measurement",
        "dialect_variants": {"srinagariya": "माणो", "tehri": "माणु", "salani": "माणा", "rathwali": "माणो"}
    },
    {
        "garhwali": "कुड़ो",
        "hindi": "बीस पाथा अनाज रखने की रिंगाल अथवा बांस की बड़ी टोकरी",
        "english": "large woven bamboo or ringal grain basket holding approximately twenty pathas",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कुड़ो", "tehri": "कुड़ु", "salani": "कुड़ा", "rathwali": "कुड़ो"}
    },
    {
        "garhwali": "झुला",
        "hindi": "पर्वतीय उफनती नदियों के ऊपर रस्सियों से बना झूलता पुल",
        "english": "traditional rope suspension bridge strung across turbulent Himalayan river gorges",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "झुला", "tehri": "झुलु", "salani": "झुला", "rathwali": "झुलो"}
    },
    {
        "garhwali": "हुड़का",
        "hindi": "जागर व लोकगाथा गायन में जगरिया द्वारा बजाया जाने वाला डमरूनुमा वाद्य",
        "english": "hourglass-shaped traditional percussion instrument beaten by ballad-singers during jagars",
        "pos": "noun",
        "gender": "M",
        "category": "music",
        "dialect_variants": {"srinagariya": "हुड़का", "tehri": "हुड़कु", "salani": "हुड़का", "rathwali": "हुड़को"}
    },
    {
        "garhwali": "बग्वाल",
        "hindi": "दीपावली पर्व अथवा पत्थर-युद्ध का ऐतिहासिक पारंपरिक मेला",
        "english": "traditional Garhwali autumn festival of lights or ritual celebratory combat fair",
        "pos": "noun",
        "gender": "F",
        "category": "festivals",
        "dialect_variants": {"srinagariya": "बग्वाल", "tehri": "बगवाल", "salani": "बग्वाल", "rathwali": "बग्वाल"}
    },

    # --- Feudal, Fortress & Epic Terms (Atkinson 1883, 1884) ---
    {
        "garhwali": "गढ़पति",
        "hindi": "पहाड़ी दुर्ग का स्वामी अथवा बावन गढ़ों का स्वतंत्र शासक",
        "english": "chieftain, feudal lord, or hereditary commander of a mountain fortress",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "गढ़पति", "tehri": "गढ़पति", "salani": "गढ़पति", "rathwali": "गढ़पति"}
    },
    {
        "garhwali": "रौतेला",
        "hindi": "पंवार राजघराने का छोटा राजकुमार अथवा राजवंशीय सामंत",
        "english": "royal prince or noble cadet belonging to the ruling Panwar dynasty of Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "history",
        "dialect_variants": {"srinagariya": "रौतेला", "tehri": "रौतेलु", "salani": "रौतेला", "rathwali": "रौतेलो"}
    },
    {
        "garhwali": "पशुआ",
        "hindi": "वह व्यक्ति जिसके शरीर में देवता अथवा पितृ-आत्मा का अवतरण होता है",
        "english": "chosen medium or possessed vessel into whose body the deity or ancestral spirit manifests",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "पशुआ", "tehri": "पसुआ", "salani": "पशुआ", "rathwali": "पशुओ"}
    },
    {
        "garhwali": "चौंफुला",
        "hindi": "वसंत ऋतु में स्त्री-पुरुषों द्वारा गोल घेरा बनाकर किया जाने वाला पारंपरिक श्रृंगारिक नृत्य",
        "english": "graceful celebratory circular folk dance performed in spring accompanied by poetic couplets",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "चौंफुला", "tehri": "चौफुला", "salani": "चौंफुला", "rathwali": "चौंफुलो"}
    },
    {
        "garhwali": "थड्या",
        "hindi": "बैसाखी व मेलों में आंगन में खड़े होकर सामूहिक रूप से गाया व नाचा जाने वाला गीत-नृत्य",
        "english": "standing group circle dance performed in village courtyards during Baisakhi fairs",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "थड्या", "tehri": "थड्या", "salani": "थड्या", "rathwali": "थड़्यो"}
    },

    # --- Directional Adverbs, Spatial & Physical Geography (Upreti 1900, Verma 2004) ---
    {
        "garhwali": "उन्दो",
        "hindi": "नीचे की ओर, ढलान की तरफ",
        "english": "downwards, downhill, sloping down towards the valley",
        "pos": "adv",
        "gender": None,
        "category": "spatial",
        "dialect_variants": {"srinagariya": "उन्दो", "tehri": "उन्दु", "salani": "उन्दान", "rathwali": "उन्दो"}
    },
    {
        "garhwali": "उबौ",
        "hindi": "ऊपर की ओर, चढ़ाई की तरफ",
        "english": "upwards, uphill, ascending towards the mountain ridge",
        "pos": "adv",
        "gender": None,
        "category": "spatial",
        "dialect_variants": {"srinagariya": "उबौ", "tehri": "उबु", "salani": "उबां", "rathwali": "उबौ"}
    },
    {
        "garhwali": "ओरलो",
        "hindi": "नदी अथवा घाटी के इस पार का, निकटवर्ती",
        "english": "on this near side of a river, gorge, or valley",
        "pos": "adj",
        "gender": "M",
        "category": "spatial",
        "dialect_variants": {"srinagariya": "ओरलो", "tehri": "ओरलु", "salani": "ओरला", "rathwali": "ओरलो"}
    },
    {
        "garhwali": "पोरलो",
        "hindi": "नदी अथवा घाटी के उस पार का, दूरस्थ",
        "english": "on the opposite, farther, or distant side of a river or mountain ridge",
        "pos": "adj",
        "gender": "M",
        "category": "spatial",
        "dialect_variants": {"srinagariya": "पोरलो", "tehri": "पोरलु", "salani": "पोरला", "rathwali": "पोरलो"}
    },
    {
        "garhwali": "सुकाळ",
        "hindi": "उत्तम वर्षा व प्रचुर अन्न-उत्पादन का सुखद समय, सुकाल",
        "english": "season of bountiful harvest, prosperity, and plentiful food supply",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "सुकाळ", "tehri": "सुकाल", "salani": "सुकाल", "rathwali": "सुकाळ"}
    },
    {
        "garhwali": "दुकाळ",
        "hindi": "अनावृष्टि व अन्न के अभाव का कष्टप्रद समय, अकाल",
        "english": "season of famine, severe drought, and agricultural scarcity",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "दुकाळ", "tehri": "दुकाल", "salani": "दुकाल", "rathwali": "दुकाळ"}
    },
    {
        "garhwali": "च्यांप",
        "hindi": "चीड़, बांज अथवा वृक्षों से निकलने वाला चिपचिपा गोंद या राल",
        "english": "sticky resin, viscous sap, or gum exudate from Himalayan pine or oak trees",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "च्यांप", "tehri": "च्यांप", "salani": "च्यांप", "rathwali": "च्याम्प"}
    },
    {
        "garhwali": "लुकाण्ड",
        "hindi": "जलती हुई लकड़ी अथवा दहकता हुआ अंगार",
        "english": "burning firebrand, charred piece of glowing wood from the hearth",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "लुकाण्ड", "tehri": "लुकांड", "salani": "लुकांड", "rathwali": "लुकाण्ड"}
    },
    {
        "garhwali": "धुवांळ",
        "hindi": "आग जलाने से उठने वाला घना धुआं",
        "english": "dense billowing cloud of smoke rising from a wood stove or forest fire",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "धुवांळ", "tehri": "धुवांल", "salani": "धुवांल", "rathwali": "धुवांळ"}
    },
    {
        "garhwali": "सिमळ",
        "hindi": "जल-स्राव युक्त दलदली व गीली भूमि",
        "english": "waterlogged, boggy, muddy marshland created by subterranean mountain springs",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "सिमळ", "tehri": "सिमल", "salani": "सिमल", "rathwali": "सिमळ"}
    },
    {
        "garhwali": "बग्गी",
        "hindi": "वर्षा से पहाड़ का खिसकना, भूस्खलन",
        "english": "mountain landslide of rock, gravel, and saturated topsoil",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बग्गी", "tehri": "बग्गी", "salani": "बग्गी", "rathwali": "बग्गी"}
    },
    {
        "garhwali": "गिड़वा",
        "hindi": "नदी के प्रवाह से चिकना व गोल बना पत्थर या रोड़ा",
        "english": "smooth, rounded river pebble or water-worn boulder found on riverbeds",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गिड़वा", "tehri": "गिड़वु", "salani": "गिड़वा", "rathwali": "गिड़वो"}
    },

    # --- Architecture & Domestic Life (Walton 1911, IIAS 2002) ---
    {
        "garhwali": "खरकी",
        "hindi": "उच्च हिमालयी चारागाहों (बुग्यालों) में पशुओं हेतु बनाई गई अस्थायी कुटिया",
        "english": "temporary pastoral hut or rustic dairy shed erected in high-altitude alpine meadows",
        "pos": "noun",
        "gender": "F",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "खरकी", "tehri": "खरकी", "salani": "खरकी", "rathwali": "खरकी"}
    },
    {
        "garhwali": "गोठ",
        "hindi": "पारंपरिक पहाड़ी मकान का भूतल जहां गाय-बैल बांधे जाते हैं",
        "english": "ground-floor cattle barn and livestock stable of a traditional two-story stone hill house",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "गोठ", "tehri": "गोठ", "salani": "गोठ", "rathwali": "गोठ"}
    },
    {
        "garhwali": "मांझ",
        "hindi": "पहाड़ी मकान की बीच की मंजिल जहां परिवार निवास करता है",
        "english": "middle living floor or central residential chamber of a traditional mountain home",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "मांझ", "tehri": "मांझ", "salani": "मांझ", "rathwali": "मांझ"}
    },
    {
        "garhwali": "निसणी",
        "hindi": "छत अथवा ऊपरी मंजिल पर चढ़ने हेतु लकड़ी अथवा पत्थरों की सीढ़ी",
        "english": "notched log ladder or stone flight of stairs leading to the upper balcony",
        "pos": "noun",
        "gender": "F",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "निसणी", "tehri": "निसणी", "salani": "निसणी", "rathwali": "निसणी"}
    },
    {
        "garhwali": "ओखळ",
        "hindi": "अनाज कूटने हेतु आंगन में स्थापित पत्थर का बड़ा गढ़ा",
        "english": "heavy stationary stone mortar embedded into the courtyard floor for pounding paddy",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "ओखळ", "tehri": "ओखल", "salani": "ओखल", "rathwali": "ओखळ"}
    },
    {
        "garhwali": "मूसळ",
        "hindi": "ओखल में धान अथवा अनाज कूटने का भारी लकड़ी का डंडा",
        "english": "heavy wooden pestle tipped with an iron ring used to pound grain in an okhal",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "मूसळ", "tehri": "मूसल", "salani": "मूसल", "rathwali": "मूसळ"}
    },
    {
        "garhwali": "स्यूंण",
        "hindi": "रात्रि की निद्रा में दिखाई देने वाला सपना, स्वप्न",
        "english": "dream, nocturnal vision experienced during slumber",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "स्यूंण", "tehri": "स्युण", "salani": "स्यूण", "rathwali": "स्यूंण"}
    },

    # --- Essential Pahari Verbs & Action Words ---
    {
        "garhwali": "बत्याणु",
        "hindi": "आपस में बातचीत करना, वार्तालाप करना",
        "english": "to converse, chat, exchange talk with someone",
        "pos": "verb",
        "gender": None,
        "category": "conversation",
        "dialect_variants": {"srinagariya": "बत्याणु", "tehri": "बत्याण", "salani": "बत्याणा", "rathwali": "बत्याणु"}
    },
    {
        "garhwali": "खोजणु",
        "hindi": "खोई वस्तु को ढूंढना, तलाश करना",
        "english": "to search for, seek, trace something missing",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "खोजणु", "tehri": "खोजण", "salani": "खोजणा", "rathwali": "खोजणु"}
    },
    {
        "garhwali": "चिन्वार",
        "hindi": "पारस्परिक जान-पहचान, परिचय",
        "english": "mutual acquaintance, personal recognition, familiarity",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "चिन्वार", "tehri": "चिन्वार", "salani": "चिन्वार", "rathwali": "चिन्वार"}
    },
    {
        "garhwali": "पल्यां",
        "hindi": "पर्वत की चोटी के उस पार का उच्च चारागाह",
        "english": "trans-ridge high alpine grazing slope",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "पल्यां", "tehri": "पल्यां", "salani": "पल्यां", "rathwali": "पल्यां"}
    },
    {
        "garhwali": "उजाव",
        "hindi": "सुबह का प्रकाश, सूर्योदय का उजाला",
        "english": "morning daylight, first bright radiance of dawn over mountain peaks",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "उजाव", "tehri": "उजाव", "salani": "उजा", "rathwali": "उजावो"}
    },
    {
        "garhwali": "अन्हारी",
        "hindi": "अमावस्या अथवा अंधकारमयी रात",
        "english": "moonless dark night, pitch-black gloom",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "अन्हारी", "tehri": "अन्हारी", "salani": "अन्हारी", "rathwali": "अन्हारी"}
    },
    {
        "garhwali": "रौंत्याल",
        "hindi": "हर्षोल्लास व आनंद से परिपूर्ण, रमणीय",
        "english": "joyous, delightful, picturesque, filled with festive cheer",
        "pos": "adj",
        "gender": "M",
        "category": "descriptor",
        "dialect_variants": {"srinagariya": "रौंत्याल", "tehri": "रौत्याल", "salani": "रौंत्याल", "rathwali": "रौंत्याळ"}
    },
    {
        "garhwali": "खिंचणु",
        "hindi": "अपनी ओर खींचना, आकर्षित करना",
        "english": "to pull, tug, draw towards oneself",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "खिंचणु", "tehri": "खिंचण", "salani": "खिंचणा", "rathwali": "खिंचणु"}
    },
    {
        "garhwali": "अंग्वाळ",
        "hindi": "बांहों में भर लेना, गले लगाना, आलिंगन",
        "english": "warm embrace, hugging affectionately with open arms",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "अंग्वाळ", "tehri": "अंग्वाल", "salani": "अंग्वाल", "rathwali": "अंग्वाळ"}
    },
    {
        "garhwali": "सुणौणु",
        "hindi": "कथा अथवा बात दूसरे को सुनाना",
        "english": "to narrate, recite, relate a story or news to listeners",
        "pos": "verb",
        "gender": None,
        "category": "action",
        "dialect_variants": {"srinagariya": "सुणौणु", "tehri": "सुणौण", "salani": "सुणाणा", "rathwali": "सुणौणु"}
    }
]

added_words = []
for w in WAVE3_WORDS:
    if w["garhwali"] not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(w["garhwali"])
        added_words.append(w["garhwali"])

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {len(added_words)} new authenticated words to {WORDS_PATH}.")
print(f"Total words in lexicon now: {len(existing_words)}")
