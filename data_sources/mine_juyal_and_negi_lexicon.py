# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline extracting vocabulary from:
- Dr. Gunanand Juyal (1967): Madhya Pahadi Bhasha
- Shyam Chand Negi (1954): Gadwali Sahitya Ki Bhumika
- Shanti Chaudhary (1994): Garhwali Lokkala Aur Loksahitya
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

JUYAL_NEGI_WORDS = [
    # ==================== 1. DIRECTION, SPATIAL & DESCRIPTORS (Juyal 1967) ====================
    {
        "garhwali": "अगाड़ी",
        "hindi": "आगे / सम्मुख",
        "english": "in front / ahead",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "अगाड़ी", "tehri": "आगे", "salani": "अगाड़ी", "rathwali": "अगाळी"}
    },
    {
        "garhwali": "पछाड़ी",
        "hindi": "पीछे",
        "english": "behind / in back",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "पछाड़ी", "tehri": "पीछे", "salani": "पछाड़ी", "rathwali": "पछाळी"}
    },
    {
        "garhwali": "भीतर",
        "hindi": "अंदर / भीतर",
        "english": "inside / within",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "भीतर", "tehri": "अंदर", "salani": "भीतर", "rathwali": "भीतर"}
    },
    {
        "garhwali": "बायर",
        "hindi": "बाहर",
        "english": "outside / outdoors",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "बायर", "tehri": "बाहर", "salani": "बहार", "rathwali": "बायर"}
    },
    {
        "garhwali": "उब्रो",
        "hindi": "ऊपर / ऊंचाई पर",
        "english": "above / upward / uphill",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "उब्रो", "tehri": "ऊपर", "salani": "उबड़", "rathwali": "उब्रो"}
    },
    {
        "garhwali": "उन्दो",
        "hindi": "नीचे / ढलान की ओर",
        "english": "below / downward / downhill",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "उन्दो", "tehri": "नीचे", "salani": "उन्द", "rathwali": "उन्दो"}
    },
    {
        "garhwali": "दाएं",
        "hindi": "दाहिनी ओर",
        "english": "right side / rightward",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "दाएं", "tehri": "दाहिना", "salani": "सीधा", "rathwali": "दाएं"}
    },
    {
        "garhwali": "बाएं",
        "hindi": "बाईं ओर",
        "english": "left side / leftward",
        "pos": "adverb",
        "gender": "N",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "बाएं", "tehri": "बायां", "salani": "उल्टा", "rathwali": "बाएं"}
    },
    {
        "garhwali": "गिल्लो",
        "hindi": "गीला / आर्द्र",
        "english": "wet / moist / damp",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "गिल्लो", "tehri": "गीला", "salani": "भीगा", "rathwali": "गिल्लो"}
    },
    {
        "garhwali": "सूखो",
        "hindi": "सूखा / शुष्क",
        "english": "dry / arid",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सूखो", "tehri": "सूखा", "salani": "सूखा", "rathwali": "सूखो"}
    },
    {
        "garhwali": "गाढ़ो",
        "hindi": "गाढ़ा / सघन",
        "english": "thick / dense",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "गाढ़ो", "tehri": "गाढ़ा", "salani": "सघन", "rathwali": "गाढ़ो"}
    },
    {
        "garhwali": "पात्तलो",
        "hindi": "पतला / विरल",
        "english": "thin / slender / diluted",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "पात्तलो", "tehri": "पतला", "salani": "पतला", "rathwali": "पात्तळो"}
    },
    {
        "garhwali": "सन्नो",
        "hindi": "छोटा / सूक्ष्म / बारीक",
        "english": "tiny / small / fine",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "सन्नो", "tehri": "छोटा", "salani": "सन्ना", "rathwali": "सन्नो"}
    },
    {
        "garhwali": "ठुलो",
        "hindi": "बड़ा / विशाल / ज्येष्ठ",
        "english": "big / large / elder",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "ठुलो", "tehri": "बड़ा", "salani": "बड़ा", "rathwali": "ठुळो"}
    },
    {
        "garhwali": "अणबोलो",
        "hindi": "मौन / शांत / चुपचाप",
        "english": "silent / speechless / mute",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "अणबोलो", "tehri": "चुप", "salani": "मौन", "rathwali": "अणबोळो"}
    },
    {
        "garhwali": "चंचल",
        "hindi": "फुर्तीला / नटखट",
        "english": "agile / nimble / spirited",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "चंचल", "tehri": "फुर्तीला", "salani": "तेज", "rathwali": "चंचळ"}
    },
    {
        "garhwali": "ढीलो",
        "hindi": "सुस्त / मद्धम / ढीला",
        "english": "slow / lethargic / loose",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "ढीलो", "tehri": "सुस्त", "salani": "मंदा", "rathwali": "ढीळो"}
    },

    # ==================== 2. TRADITIONAL WOODCRAFT & CARPENTRY (Chaudhary 1994) ====================
    {
        "garhwali": "गुनिया",
        "hindi": "बढ़ई का समकोण नापने का एल-आकार औजार",
        "english": "carpenter's try-square for checking right angles",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "गुनिया", "tehri": "गुनिया", "salani": "गुनिया", "rathwali": "गुनिया"}
    },
    {
        "garhwali": "रंदा",
        "hindi": "लकड़ी छीलकर चिकना करने का रंदा",
        "english": "wood hand plane for smoothing timber",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "रंदा", "tehri": "रंदा", "salani": "रंदा", "rathwali": "रंदा"}
    },
    {
        "garhwali": "आरी",
        "hindi": "लकड़ी चीरने की दांतेदार आरी",
        "english": "handsaw for cutting timber",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "आरी", "tehri": "आरा", "salani": "आरी", "rathwali": "आरी"}
    },
    {
        "garhwali": "बसूला",
        "hindi": "लकड़ी तराशने की तेज बसूली",
        "english": "carpenter's adze for shaping beams",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "बसूला", "tehri": "बसूला", "salani": "बसूली", "rathwali": "बसूळा"}
    },
    {
        "garhwali": "छेनी",
        "hindi": "पत्थर या लकड़ी तराशने की लोहे की छेनी",
        "english": "cold chisel for carving stone or wood",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "छेनी", "tehri": "छेणी", "salani": "छेनी", "rathwali": "छेणी"}
    },
    {
        "garhwali": "हथौड़ी",
        "hindi": "लोहे की हथौड़ी",
        "english": "hammer",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "हथौड़ी", "tehri": "हथौड़ा", "salani": "मार्टोल", "rathwali": "हथौळी"}
    },

    # ==================== 3. KITCHEN GRINDING & MORTARS (Bhatt 1976 / Juyal 1967) ====================
    {
        "garhwali": "सिल",
        "hindi": "मसाला व चटनी पीसने का समतल पत्थर (सिल)",
        "english": "flat stone slab for grinding spices and condiments",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "सिल", "tehri": "सिलौटा", "salani": "सिल", "rathwali": "सिळ"}
    },
    {
        "garhwali": "लोढ़ा",
        "hindi": "सिल पर मसाला पीसने का बेलनाकार बट्टा",
        "english": "cylindrical stone muller / rolling pestle",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "लोढ़ा", "tehri": "बट्टा", "salani": "लोढ़ा", "rathwali": "लोढ़ा"}
    },
    {
        "garhwali": "ओखली",
        "hindi": "अनाज व धान कूटने की भारी लकड़ी या पत्थर की ओखली",
        "english": "heavy hollowed stone or timber mortar",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "ओखली", "tehri": "उखल", "salani": "ओखली", "rathwali": "ओखळी"}
    },
    {
        "garhwali": "मूसल",
        "hindi": "धान कूटने का भारी लोहे की साम वाला मूसल",
        "english": "heavy iron-tipped wooden pestle for pounding grain",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "मूसल", "tehri": "मूसर", "salani": "मूसल", "rathwali": "मूसळ"}
    },
    {
        "garhwali": "जांदो",
        "hindi": "हाथ से घुमाने वाली दाल व आटा दलने की चक्की (जांत)",
        "english": "manual stone quern handmill for grinding dal and grain",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "जांदो", "tehri": "जांत", "salani": "जांदो", "rathwali": "जांदो"}
    },
    {
        "garhwali": "सरोता",
        "hindi": "सुपारी काटने का सरोता",
        "english": "traditional betel-nut cutter",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सरोता", "tehri": "सरोता", "salani": "सरोता", "rathwali": "सरोता"}
    },

    # ==================== 4. FOLK PERFORMANCE & CULTURAL FESTIVITY (Negi 1954 / Chaudhary 1994) ====================
    {
        "garhwali": "हुड़को",
        "hindi": "पहाड़ी जागर व लोकगीतों का डमरूनुमा तालवाद्य (हुड़का)",
        "english": "hourglass-shaped folk drum played with hand (Hurka)",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "हुड़को", "tehri": "हुड़का", "salani": "हुड़का", "rathwali": "हुड़को"}
    },
    {
        "garhwali": "डौंर",
        "hindi": "जागर अनुष्ठान में कांस्य थाली के साथ बजने वाला छोटा डमरू",
        "english": "small ritual pellet-drum played in shamanic jagars",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "डौंर", "tehri": "डौंरू", "salani": "डमरू", "rathwali": "डौंर"}
    },
    {
        "garhwali": "कौथिग",
        "hindi": "पहाड़ी धार्मिक, व्यापारिक व सांस्कृतिक मेला",
        "english": "traditional Himalayan village fair / festive festival gathering",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "कौथिग", "tehri": "मेला", "salani": "कौथग", "rathwali": "कौथिग"}
    },
    {
        "garhwali": "कौथिग्यार",
        "hindi": "मेला देखने आए हुए ग्रामीण जन",
        "english": "festive fair-goers / visitors attending folk fair",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "कौथिग्यार", "tehri": "मेलार्थी", "salani": "कौथग्यार", "rathwali": "कौथिग्यार"}
    },
    {
        "garhwali": "होल्यार",
        "hindi": "बैठकी व खड़ी होली गाने वाले लोक गायक",
        "english": "traditional folk singers of festive spring Holi songs",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "होल्यार", "tehri": "होलियारे", "salani": "होल्यार", "rathwali": "होल्यार"}
    },
    {
        "garhwali": "सयाणप",
        "hindi": "बुद्धिमत्ता / बुजुर्गों की दूरदर्शिता व समझदारी",
        "english": "wisdom / elder's prudent judgment and sagacity",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "सयाणप", "tehri": "सयानप", "salani": "होशियारी", "rathwali": "सयाणप"}
    },
    {
        "garhwali": "नाता-गोता",
        "hindi": "पारिवारिक रिश्तेदारी व सगे-संबंधी",
        "english": "kinship relations / family clan ties",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नाता-गोता", "tehri": "रिश्तेदार", "salani": "नातेदार", "rathwali": "नाता-गोता"}
    },
    {
        "garhwali": "पड़ोसी",
        "hindi": "पड़ोसी / हमसाया",
        "english": "immediate neighbor in village",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "पड़ोसी", "tehri": "पड़ोसी", "salani": "पड़ोसी", "rathwali": "पड़ोसी"}
    },
    {
        "garhwali": "दगाड़ी",
        "hindi": "सच्चा साथी / अभिन्न मित्र",
        "english": "steadfast companion / lifelong partner",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "दगाड़ी", "tehri": "साथी", "salani": "दगड्या", "rathwali": "दगाळी"}
    },
    {
        "garhwali": "अणजाण",
        "hindi": "अपरिचित / अजनबी व्यक्ति",
        "english": "stranger / unknown person",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "अणजाण", "tehri": "अजनबी", "salani": "अनजान", "rathwali": "अणजाण"}
    },
    {
        "garhwali": "जैती",
        "hindi": "पहाड़ी उत्सवों में विजय के शंखनाद व जयकारे",
        "english": "triumphant festive victory chants and holy salutations",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "जैती", "tehri": "जयकारा", "salani": "जैकार", "rathwali": "जैती"}
    },
    {
        "garhwali": "अनवाल",
        "hindi": "उच्च हिमालयी बुग्यालों में भेड़ें चराने वाला गड़रिया",
        "english": "transhumant shepherd of high alpine bugyals",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "अनवाल", "tehri": "गड़रिया", "salani": "पालसी", "rathwali": "अनवाळ"}
    },
    {
        "garhwali": "घस्यारी",
        "hindi": "जंगल से घास व पत्तियां लाने वाली परिश्रमी पहाड़ी महिला",
        "english": "hardworking mountain woman who cuts and carries grass fodder",
        "pos": "noun",
        "gender": "F",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "घस्यारी", "tehri": "घासी", "salani": "घस्यारी", "rathwali": "घस्यारी"}
    },
    {
        "garhwali": "हलिया",
        "hindi": "खेत जोतने वाला पारंपरिक किसान",
        "english": "ploughman farmer working terraced fields",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "हलिया", "tehri": "हलिया", "salani": "हलवाहा", "rathwali": "हळिया"}
    },
    {
        "garhwali": "औजी",
        "hindi": "ढोल-दमाऊं बजाने वाले पारंपरिक संगीतकार व शिल्पी",
        "english": "master folk percussionist of sacred Dhol-Damau",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "औजी", "tehri": "बाजगी", "salani": "ढोली", "rathwali": "औजी"}
    },
    {
        "garhwali": "तामटा",
        "hindi": "तांबे व पीतल के पारंपरिक बर्तन गढ़ने वाला शिल्पी",
        "english": "traditional coppersmith and brassware artisan",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "तामटा", "tehri": "कसेरा", "salani": "तामटा", "rathwali": "तामटा"}
    },
    {
        "garhwali": "ओढ़",
        "hindi": "पत्थरों के पारंपरिक मकान व सीढ़ियां बनाने वाला राजमिस्त्री",
        "english": "master drystone mason builder of traditional hill houses",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "ओढ़", "tehri": "मिस्त्री", "salani": "राजमिस्त्री", "rathwali": "ओढ़"}
    },
    {
        "garhwali": "तिबारी",
        "hindi": "पहाड़ी मकान के सामने तीन मेहराबों वाला नक्काशीदार लकड़ी का बरामदा",
        "english": "ornately carved three-bay wooden balcony of traditional house",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "तिबारी", "tehri": "तिबारी", "salani": "बरामदा", "rathwali": "तिबारी"}
    },
    {
        "garhwali": "खोली",
        "hindi": "मकान का मुख्य प्रवेश द्वार",
        "english": "main entrance carved wooden portal / doorway of ancestral house",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "खोली", "tehri": "दरवाजा", "salani": "द्वार", "rathwali": "खोळी"}
    },
    {
        "garhwali": "पाथर",
        "hindi": "छत पर छाने वाले प्राकृतिक स्लेट के पत्थर",
        "english": "hewn metamorphic roof slates of mountain homes",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पाथर", "tehri": "स्लेट", "salani": "पत्थर", "rathwali": "पाथर"}
    },
    {
        "garhwali": "भकार",
        "hindi": "अनाज सुरक्षित रखने की लकड़ी की बड़ी कोठार",
        "english": "large timber grain silo / granary built into house",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "भकार", "tehri": "कोठार", "salani": "भंडार", "rathwali": "भकार"}
    },
    {
        "garhwali": "गागरी",
        "hindi": "पानी भरने का पीतल या तांबे का भारी घड़ा",
        "english": "heavy brass or copper spherical water urn",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "गागरी", "tehri": "गागर", "salani": "गगरी", "rathwali": "गागरी"}
    },
    {
        "garhwali": "चिमटा",
        "hindi": "चूल्हे की आग संभालने का लोहे का चिमटा",
        "english": "iron hearth fire tongs",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "चिमटा", "tehri": "चिमटा", "salani": "चिमटी", "rathwali": "चिमटा"}
    },
    {
        "garhwali": "कंडी",
        "hindi": "पीठ पर पीठने वाली रिंगाल की पारंपरिक कंडी",
        "english": "traditional conical bamboo pack-basket carried on shoulders",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कंडी", "tehri": "डोका", "salani": "कंडी", "rathwali": "कंडी"}
    },
    {
        "garhwali": "दीया",
        "hindi": "पूजा व दीपावली का दीपक",
        "english": "earthen or brass devotional oil lamp",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "दीया", "tehri": "दीप", "salani": "दीपक", "rathwali": "दीया"}
    }
]

added = 0
enriched = 0

for item in JUYAL_NEGI_WORDS:
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

print(f"Juyal & Negi mining added: {added}")
print(f"Enriched: {enriched}")
print(f"Total word count now: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved words to {WORDS_PATH}")
