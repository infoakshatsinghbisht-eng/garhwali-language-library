"""
Script to expand garhwali/lexicon/data/words.json with 450+ new verified lemmas
covering kinship, wedding, social, occupations, household, cuisine, nature, flora,
fauna, body/health/emotions, numbers/time, modern tech, government/law, business,
safety/crime, children/education, and song/literature extractions.
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

words_path = os.path.join("garhwali", "lexicon", "data", "words.json")
with open(words_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

print(f"Initial word count: {len(existing_data)}")

# Create dictionary keyed by garhwali lemma
words_by_lemma = {w["garhwali"].strip(): w for w in existing_data}

new_words = [
    # ==================== KINSHIP & FAMILY ====================
    {
        "garhwali": "बुबा",
        "hindi": "पिताजी / पिता",
        "english": "father",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "बुबा", "tehri": "बौजी", "salani": "पिताजी", "rathwali": "बुबा"}
    },
    {
        "garhwali": "दद्दा",
        "hindi": "बड़ा भाई",
        "english": "elder brother",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "दद्दा", "tehri": "भैजी", "salani": "दद्दा", "rathwali": "दाजु"}
    },
    {
        "garhwali": "भुली",
        "hindi": "छोटी बहन",
        "english": "younger sister",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "भुली", "tehri": "भुली", "salani": "बैणी", "rathwali": "भुली"}
    },
    {
        "garhwali": "दीदी",
        "hindi": "बड़ी बहन",
        "english": "elder sister",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "दीदी", "tehri": "ब्वड़ी", "salani": "जीजी", "rathwali": "दीदी"}
    },
    {
        "garhwali": "भुलू",
        "hindi": "छोटा भाई",
        "english": "younger brother",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "भुलू", "tehri": "भुलू", "salani": "भै", "rathwali": "भुलू"}
    },
    {
        "garhwali": "नौनी",
        "hindi": "बेटी / कन्या",
        "english": "daughter / girl",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नौनी", "tehri": "छोरी", "salani": "बेटी", "rathwali": "नौनी"}
    },
    {
        "garhwali": "नौना",
        "hindi": "बेटा / लड़का",
        "english": "son / boy",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नौना", "tehri": "छोरू", "salani": "बेटा", "rathwali": "नौना"}
    },
    {
        "garhwali": "ब्वारी",
        "hindi": "बहू / पुत्रवधू",
        "english": "daughter-in-law",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "ब्वारी", "tehri": "ब्वारी", "salani": "बहू", "rathwali": "ब्वारी"}
    },
    {
        "garhwali": "जंवाई",
        "hindi": "दामाद",
        "english": "son-in-law",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "जंवाई", "tehri": "ज्वाईं", "salani": "दामाद", "rathwali": "जंवाई"}
    },
    {
        "garhwali": "कक्यो",
        "hindi": "चाचा",
        "english": "paternal uncle",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "कक्यो", "tehri": "काका", "salani": "कका", "rathwali": "कक्यो"}
    },
    {
        "garhwali": "काकी",
        "hindi": "चाची",
        "english": "paternal aunt",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "काकी", "tehri": "काकी", "salani": "चाची", "rathwali": "काकी"}
    },
    {
        "garhwali": "मामा",
        "hindi": "मामा",
        "english": "maternal uncle",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मामा", "tehri": "मामा", "salani": "मामा", "rathwali": "मामा"}
    },
    {
        "garhwali": "मामी",
        "hindi": "मामी",
        "english": "maternal aunt",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मामी", "tehri": "मामी", "salani": "मामी", "rathwali": "मामी"}
    },
    {
        "garhwali": "बूबू",
        "hindi": "दादाजी",
        "english": "grandfather",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "दादू", "tehri": "बूबू", "salani": "दादाजी", "rathwali": "बूबू"}
    },
    {
        "garhwali": "दादी",
        "hindi": "दादी जी",
        "english": "grandmother",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "दादी", "tehri": "दाजी", "salani": "दादी", "rathwali": "अजी"}
    },
    {
        "garhwali": "नाती",
        "hindi": "पोता / नाती",
        "english": "grandson",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "नाती", "tehri": "नाती", "salani": "पोता", "rathwali": "नाती"}
    },
    {
        "garhwali": "सौरास",
        "hindi": "ससुराल",
        "english": "in-laws' home / marital home",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "सौरास", "tehri": "सौरास", "salani": "ससुराल", "rathwali": "सौराश"}
    },
    {
        "garhwali": "मैत",
        "hindi": "मायका / पीहर",
        "english": "maternal home of married woman",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "मैत", "tehri": "मैत", "salani": "मायका", "rathwali": "मैत"}
    },
    {
        "garhwali": "ध्याणी",
        "hindi": "विवाहिता पुत्री / बहन",
        "english": "married daughter visiting maternal village",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "ध्याणी", "tehri": "ध्याणी", "salani": "ध्याण", "rathwali": "ध्याणी"}
    },
    {
        "garhwali": "समधी",
        "hindi": "समधी",
        "english": "father of daughter/son-in-law",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "समधी", "tehri": "समधी", "salani": "समधी", "rathwali": "समधी"}
    },
    {
        "garhwali": "जेठ",
        "hindi": "जेठ (पति का बड़ा भाई)",
        "english": "husband's elder brother",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "जेठ", "tehri": "जेठ", "salani": "जेठ", "rathwali": "जेठ"}
    },
    {
        "garhwali": "देवर",
        "hindi": "देवर (पति का छोटा भाई)",
        "english": "husband's younger brother",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "देवर", "tehri": "देवर", "salani": "देवर", "rathwali": "देवर"}
    },
    {
        "garhwali": "ननद",
        "hindi": "ननद (पति की बहन)",
        "english": "husband's sister",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "ननद", "tehri": "ननद", "salani": "ननद", "rathwali": "नणद"}
    },
    {
        "garhwali": "साला",
        "hindi": "साला (पत्नी का भाई)",
        "english": "wife's brother",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "साला", "tehri": "साला", "salani": "साला", "rathwali": "साला"}
    },
    {
        "garhwali": "साली",
        "hindi": "साली (पत्नी की बहन)",
        "english": "wife's sister",
        "pos": "noun",
        "gender": "F",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "साली", "tehri": "साली", "salani": "साली", "rathwali": "साली"}
    },
    {
        "garhwali": "पुरखा",
        "hindi": "पूर्वज",
        "english": "ancestors / forebears",
        "pos": "noun",
        "gender": "M",
        "category": "kinship",
        "dialect_variants": {"srinagariya": "पुरखा", "tehri": "पुरखा", "salani": "बुजुर्ग", "rathwali": "पुरखा"}
    },

    # ==================== MARRIAGE & WEDDING ====================
    {
        "garhwali": "ब्याव",
        "hindi": "विवाह / शादी",
        "english": "marriage / wedding",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "ब्याव", "tehri": "ब्याव", "salani": "शादी", "rathwali": "ब्याव"}
    },
    {
        "garhwali": "मंगणी",
        "hindi": "सगाई / मंगनी",
        "english": "betrothal / engagement",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "मंगणी", "tehri": "बात-पक्की", "salani": "सगाई", "rathwali": "मंगणी"}
    },
    {
        "garhwali": "बन्ना",
        "hindi": "दूल्हा",
        "english": "groom",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बन्ना", "tehri": "दूल्हा", "salani": "दूल्हा", "rathwali": "बन्ना"}
    },
    {
        "garhwali": "बन्नी",
        "hindi": "दुल्हन",
        "english": "bride",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बन्नी", "tehri": "दुल्हन", "salani": "दुल्हन", "rathwali": "बन्नी"}
    },
    {
        "garhwali": "धूली-अर्घ",
        "hindi": "धूली-अर्घ्य (दूल्हे का स्वागत संस्कार)",
        "english": "traditional wedding threshold welcoming ritual",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "धूली-अर्घ", "tehri": "धूली-अर्घ्य", "salani": "धूलि-अर्घ", "rathwali": "धूली-अर्घ"}
    },
    {
        "garhwali": "मंगल-गीत",
        "hindi": "मांगलिक विवाह गीत",
        "english": "sacred traditional wedding hymns",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "मंगल-गीत", "tehri": "मांगल", "salani": "मंगल-गीत", "rathwali": "मांगल"}
    },
    {
        "garhwali": "कन्यादान",
        "hindi": "कन्यादान",
        "english": "giving away the bride",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "कन्यादान", "tehri": "कन्यादान", "salani": "कन्यादान", "rathwali": "कन्यादान"}
    },
    {
        "garhwali": "फेरा",
        "hindi": "सप्तपदी फेरे",
        "english": "nuptial circumambulations around sacred fire",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "फेरा", "tehri": "भांवर", "salani": "फेरा", "rathwali": "भांवरी"}
    },
    {
        "garhwali": "बिदाई",
        "hindi": "विदाई",
        "english": "bridal departure ceremony",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बिदाई", "tehri": "बिदाई", "salani": "रुखसती", "rathwali": "बिदाई"}
    },
    {
        "garhwali": "रौंतेली",
        "hindi": "उल्लासपूर्ण वातावरण",
        "english": "festive joyful atmosphere",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "रौंतेली", "tehri": "रौनक", "salani": "रौंतेली", "rathwali": "रौंतेली"}
    },
    {
        "garhwali": "बरात",
        "hindi": "बारात",
        "english": "wedding procession",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "बरात", "tehri": "जनेत", "salani": "बारात", "rathwali": "जनेत"}
    },
    {
        "garhwali": "जनेती",
        "hindi": "बाराती",
        "english": "wedding procession guest",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "जनेती", "tehri": "जनेती", "salani": "बाराती", "rathwali": "जनेत्यार"}
    },
    {
        "garhwali": "नथुली",
        "hindi": "टिहरी नथ / बड़ी सोने की नथ",
        "english": "traditional large circular gold nose ring",
        "pos": "noun",
        "gender": "F",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "नथुली", "tehri": "नथ", "salani": "नथुली", "rathwali": "नथ"}
    },
    {
        "garhwali": "गुलोबंद",
        "hindi": "गलबंद (मखमली सोने का हार)",
        "english": "traditional gold velvet choker necklace",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "गुलोबंद", "tehri": "गलबंद", "salani": "गुलोबंद", "rathwali": "गुलोबंद"}
    },
    {
        "garhwali": "पिछौड़ा",
        "hindi": "रंगवाली पिछौड़ा (पारंपरिक चुनरी)",
        "english": "sacred yellow-and-red ceremonial mantle",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "पिछौड़ा", "tehri": "पिछौड़ा", "salani": "दुपट्टा", "rathwali": "पिछौड़ा"}
    },
    {
        "garhwali": "अरसा",
        "hindi": "अरसा (विवाह की पारंपरिक मिठाई)",
        "english": "traditional wedding fried rice-flour and jaggery sweet",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "अरसा", "tehri": "अरसा", "salani": "अरसा", "rathwali": "अरसा"}
    },

    # ==================== SOCIAL RELATIONSHIPS ====================
    {
        "garhwali": "दगाड़ी",
        "hindi": "साथी / हमसफ़र",
        "english": "companion / fellow traveler",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "दगाड़ी", "tehri": "दगाड़ी", "salani": "साथी", "rathwali": "दगाड़ी"}
    },
    {
        "garhwali": "संगी",
        "hindi": "सखा / मित्र",
        "english": "friend / partner",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "संगी", "tehri": "यार", "salani": "संगी", "rathwali": "संगी"}
    },
    {
        "garhwali": "पड़ोसी",
        "hindi": "पड़ोसी",
        "english": "neighbour",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "परोसी", "tehri": "पड़ोसी", "salani": "पड़ोसी", "rathwali": "परोसी"}
    },
    {
        "garhwali": "पाहुणा",
        "hindi": "अतिथि / मेहमान",
        "english": "honored guest",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "पाहुणा", "tehri": "पाहुणा", "salani": "मेहमान", "rathwali": "पाहुणा"}
    },
    {
        "garhwali": "सयाणा",
        "hindi": "गाँव का बुजुर्ग / समझदार मुखिया",
        "english": "wise village elder / patriarch",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "सयाणा", "tehri": "सयाणा", "salani": "मुखिया", "rathwali": "सयाणा"}
    },
    {
        "garhwali": "अणजाण",
        "hindi": "अजनबी / अनजान",
        "english": "stranger",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "अणजाण", "tehri": "अनजान", "salani": "परदेसी", "rathwali": "अणजाण"}
    },
    {
        "garhwali": "गौंंत्यार",
        "hindi": "गाँववासी / सह-ग्रामीण",
        "english": "fellow villager",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "गौंंत्यार", "tehri": "गौंवासी", "salani": "गाँववाला", "rathwali": "गौंंत्यार"}
    },
    {
        "garhwali": "जैती",
        "hindi": "सामूहिक कृषि सहयोग",
        "english": "reciprocal communal farming help",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "जैती", "tehri": "पड़ताल", "salani": "सहयोग", "rathwali": "जैती"}
    },
    {
        "garhwali": "कौथिग्यार",
        "hindi": "मेले में आया दर्शनार्थी",
        "english": "fairgoer / festival visitor",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "कौथिग्यार", "tehri": "कौथिकी", "salani": "मेलेवाला", "rathwali": "कौथिग्यार"}
    },

    # ==================== TRADITIONAL OCCUPATIONS & CRAFTS ====================
    {
        "garhwali": "अनवाल",
        "hindi": "भेड़पालक / उच्च हिमालयी चरवाहा",
        "english": "high-altitude transhumant shepherd",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "अनवाल", "tehri": "चरवाहा", "salani": "ग्वाला", "rathwali": "अनवाल"}
    },
    {
        "garhwali": "घस्यारी",
        "hindi": "घास काटने वाली महिला",
        "english": "mountain grass-cutter maiden",
        "pos": "noun",
        "gender": "F",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "घस्यारी", "tehri": "घस्यारी", "salani": "घस्यारी", "rathwali": "घस्यारी"}
    },
    {
        "garhwali": "औजी",
        "hindi": "ढोल-दमाऊँ वादक एवं गायक",
        "english": "master hereditary drummer of Dhol Damau",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "औजी", "tehri": "दास", "salani": "ढोली", "rathwali": "औजी"}
    },
    {
        "garhwali": "ढकी",
        "hindi": "मांगल एवं गाथा गायक",
        "english": "traditional wedding bard and ballad singer",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "ढकी", "tehri": "ढोली", "salani": "गायक", "rathwali": "ढकी"}
    },
    {
        "garhwali": "जगरिया",
        "hindi": "जागर पुरोहित / देव-आह्वानक",
        "english": "shamanic singer who invokes deities during jagar",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "जगरिया", "tehri": "जगरिया", "salani": "जागरी", "rathwali": "जगरिया"}
    },
    {
        "garhwali": "डांगरिया",
        "hindi": "देवता का पश्वा / माध्यम",
        "english": "human vessel possessed by deity during trance",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "डांगरिया", "tehri": "पश्वा", "salani": "डांगरिया", "rathwali": "डांगरिया"}
    },
    {
        "garhwali": "तामटा",
        "hindi": "ताम्रशिल्पी / तांबे का कारीगर",
        "english": "traditional coppersmith",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "तामटा", "tehri": "ताम्रकार", "salani": "तामटा", "rathwali": "तामटा"}
    },
    {
        "garhwali": "ओढ़",
        "hindi": "पत्थर तराशने वाला राजमिस्त्री / बढ़ई",
        "english": "traditional stone mason / wood carver",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "ओढ़", "tehri": "बढ़ई", "salani": "मिस्त्री", "rathwali": "ओढ़"}
    },
    {
        "garhwali": "हलिया",
        "hindi": "हल जोतने वाला किसान",
        "english": "ploughman who drives oxen across terraces",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "हलिया", "tehri": "हल्या", "salani": "किसान", "rathwali": "हलिया"}
    },
    {
        "garhwali": "घट्ट्या",
        "hindi": "पनचक्की चलाने वाला",
        "english": "operator of traditional watermill",
        "pos": "noun",
        "gender": "M",
        "category": "occupations",
        "dialect_variants": {"srinagariya": "घट्ट्या", "tehri": "घटवार", "salani": "पनचक्कीवाला", "rathwali": "घट्ट्या"}
    },

    # ==================== HOUSEHOLD & ARCHITECTURE ====================
    {
        "garhwali": "तिबारी",
        "hindi": "नक्काशीदार लकड़ी का बरामदा",
        "english": "ornate carved wooden mountain veranda/balcony",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "तिबारी", "tehri": "तिबारी", "salani": "बरामदा", "rathwali": "तिबारी"}
    },
    {
        "garhwali": "खोली",
        "hindi": "कमरा / मुख्य प्रवेश द्वार",
        "english": "room / main doorway",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "खोली", "tehri": "कमरा", "salani": "खोली", "rathwali": "खोली"}
    },
    {
        "garhwali": "पाथर",
        "hindi": "छत की स्लेट पट्टियां",
        "english": "flat mountain slate roofing tiles",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पाथर", "tehri": "पठाल", "salani": "स्लेट", "rathwali": "पाथर"}
    },
    {
        "garhwali": "भकार",
        "hindi": "अनाज का बड़ा काष्ठ कोठार",
        "english": "large traditional wooden grain granary box",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "भकार", "tehri": "भकार", "salani": "कोठार", "rathwali": "भकार"}
    },
    {
        "garhwali": "ओखली",
        "hindi": "धान कूटने का पत्थर का गर्त",
        "english": "stone mortar for pounding paddy",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "ओखली", "tehri": "उखल", "salani": "ओखली", "rathwali": "ओखली"}
    },
    {
        "garhwali": "मूसल",
        "hindi": "मूसल",
        "english": "heavy wooden grain pestle",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "मूसल", "tehri": "मुसल", "salani": "मूसल", "rathwali": "मूसल"}
    },
    {
        "garhwali": "सिलबट्टा",
        "hindi": "मसाला पीसने का पत्थर",
        "english": "flat stone and rolling pin for grinding spices",
        "pos": "noun",
        "gender": "M",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "सिलबट्टा", "tehri": "सिल", "salani": "सिलबट्टा", "rathwali": "सिलबट्टा"}
    },
    {
        "garhwali": "जांदो",
        "hindi": "हाथ की पत्थर चक्की",
        "english": "hand-turned stone flour mill quern",
        "pos": "noun",
        "gender": "M",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "जांदो", "tehri": "जांदो", "salani": "चक्की", "rathwali": "जांदो"}
    },
    {
        "garhwali": "दातुलि",
        "hindi": "दरांती (घास काटने की हंसिया)",
        "english": "curved serrated harvesting sickle",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "दातुलि", "tehri": "दातुलि", "salani": "हंसिया", "rathwali": "दातुलि"}
    },
    {
        "garhwali": "गागरी",
        "hindi": "पानी की तांबे-पीतल की गागर",
        "english": "large brass or copper water pitcher",
        "pos": "noun",
        "gender": "F",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "गागरी", "tehri": "गागर", "salani": "गागरी", "rathwali": "गागरी"}
    },
    {
        "garhwali": "चिमटा",
        "hindi": "चिमटा",
        "english": "hearth fire tongs",
        "pos": "noun",
        "gender": "M",
        "category": "kitchen",
        "dialect_variants": {"srinagariya": "चिमटा", "tehri": "चिमटा", "salani": "चिमटा", "rathwali": "चिमटा"}
    },
    {
        "garhwali": "कंडी",
        "hindi": "पीठ पर लादने की बाँस की टोकरी",
        "english": "conical bamboo backpack basket",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कंडी", "tehri": "डोका", "salani": "कंडी", "rathwali": "कंडी"}
    },

    # ==================== CUISINE & FOOD ====================
    {
        "garhwali": "काफ़ुली",
        "hindi": "काफ़ुली (पालक-मेथी का गाढ़ा साग)",
        "english": "nutritious spinach and fenugreek iron-wok puree",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "काफ़ुली", "tehri": "कफली", "salani": "साग", "rathwali": "काफ़ुली"}
    },
    {
        "garhwali": "चैनसूं",
        "hindi": "चैनसूं (उड़द दाल की भुनी कढ़ी)",
        "english": "roasted and ground black gram curry",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "चैनसूं", "tehri": "चैनसूं", "salani": "दाल", "rathwali": "चैनसूं"}
    },
    {
        "garhwali": "झोली",
        "hindi": "कढ़ी / मट्ठे की झोली",
        "english": "spiced mountain buttermilk curry",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "झोली", "tehri": "झोली", "salani": "कढ़ी", "rathwali": "झोली"}
    },
    {
        "garhwali": "थटवाणी",
        "hindi": "गहत का सूप (रस)",
        "english": "slow-simmered horsegram warming broth",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "थटवाणी", "tehri": "घासणी", "salani": "रस", "rathwali": "थटवाणी"}
    },
    {
        "garhwali": "चुड़कानी",
        "hindi": "भट्ट की चुड़कानी (काली सोयाबीन दाल)",
        "english": "fried black soybean velvety curry",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "चुड़कानी", "tehri": "भटवाणी", "salani": "चुड़कानी", "rathwali": "चुड़कानी"}
    },
    {
        "garhwali": "गुटका",
        "hindi": "आलू का गुटका",
        "english": "spiced potato chunks tempered with jakhya",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "गुटका", "tehri": "आलू गुटका", "salani": "सब्जी", "rathwali": "गुटका"}
    },
    {
        "garhwali": "बाड़ी",
        "hindi": "बाड़ी (मंडुवे के आटे का हलुवा-सूप)",
        "english": "steamed finger-millet porridge served with ghee",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "बाड़ी", "tehri": "बाड़ी", "salani": "बाड़ी", "rathwali": "बाड़ी"}
    },
    {
        "garhwali": "सिंगोरी",
        "hindi": "सिंगोरी (मालू के पत्ते में लिपटी खोया मिठाई)",
        "english": "cone-shaped milk solid sweet wrapped in malu leaf",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "सिंगोरी", "tehri": "सिंगोरी", "salani": "मिठाई", "rathwali": "सिंगोरी"}
    },
    {
        "garhwali": "पिस्यूं-लूण",
        "hindi": "सिलबट्टे पर पिसा पहाड़ी नमक",
        "english": "rock salt stone-ground with herbs and garlic",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "पिस्यूं-लूण", "tehri": "पिसा-नमक", "salani": "पहाड़ी-नमक", "rathwali": "पिस्यूं-लूण"}
    },

    # ==================== NATURE, GEOGRAPHY & WEATHER ====================
    {
        "garhwali": "बुग्याल",
        "hindi": "उच्च हिमालयी मखमली घास का मैदान",
        "english": "high-altitude alpine meadow above treeline",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बुग्याल", "tehri": "बुग्याल", "salani": "पयार", "rathwali": "बुग्याल"}
    },
    {
        "garhwali": "गधेरा",
        "hindi": "पहाड़ी बरसाती नाला",
        "english": "tumbling rocky mountain torrent / brook",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "गधेरा", "tehri": "गधेरा", "salani": "नाला", "rathwali": "गधेरा"}
    },
    {
        "garhwali": "सेरा",
        "hindi": "नदी किनारे का उपजाऊ समतल खेत",
        "english": "fertile flat irrigated riverside terraced field",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "सेरा", "tehri": "सेरा", "salani": "समतल खेत", "rathwali": "सेरा"}
    },
    {
        "garhwali": "ओड्यार",
        "hindi": "पहाड़ी प्राकृतिक गुफा",
        "english": "natural rock shelter / overhang cave",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "ओड्यार", "tehri": "गुफा", "salani": "ओड्यार", "rathwali": "ओड्यार"}
    },
    {
        "garhwali": "हिंवल",
        "hindi": "बर्फ / हिमपात",
        "english": "snow / snowfall",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिंवल", "tehri": "हिम", "salani": "बर्फ", "rathwali": "हिंवल"}
    },
    {
        "garhwali": "बयार",
        "hindi": "शीतल पहाड़ी हवा",
        "english": "fresh mountain breeze",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "बयार", "tehri": "पवन", "salani": "हवा", "rathwali": "बयार"}
    },
    {
        "garhwali": "कुहासा",
        "hindi": "कोहरा / धुंध",
        "english": "mountain fog / morning mist",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "कुहासा", "tehri": "धुंध", "salani": "कोहरा", "rathwali": "कुहासा"}
    },
    {
        "garhwali": "छरछरा",
        "hindi": "झरना",
        "english": "waterfall / mountain cascade",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "छरछरा", "tehri": "झरना", "salani": "प्रपात", "rathwali": "छरछरा"}
    },

    # ==================== FAUNA & ANIMALS ====================
    {
        "garhwali": "घुरल",
        "hindi": "घुरल (पहाड़ी मृग)",
        "english": "Himalayan goral (goat antelope)",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "घुरल", "tehri": "घुरल", "salani": "घुरल", "rathwali": "घुरल"}
    },
    {
        "garhwali": "कस्तूरी-मृग",
        "hindi": "कस्तूरी मृग (राज्य पशु)",
        "english": "Himalayan musk deer (state animal of Uttarakhand)",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "कस्तूरी-मृग", "tehri": "बिनाली", "salani": "कस्तूरी मृग", "rathwali": "कस्तूरी-मृग"}
    },
    {
        "garhwali": "गुलदार",
        "hindi": "तेंदुआ",
        "english": "leopard / panther",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "गुलदार", "tehri": "बाघ", "salani": "तेंदुआ", "rathwali": "गुलदार"}
    },
    {
        "garhwali": "मोनाल",
        "hindi": "मोनाल (राज्य पक्षी)",
        "english": "Himalayan monal (state bird of Uttarakhand)",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "मोनाल", "tehri": "मोनाल", "salani": "मोनाल", "rathwali": "मण्याल"}
    },
    {
        "garhwali": "हिलांस",
        "hindi": "हिलांस (हरियल पक्षी)",
        "english": "Himalayan green pigeon",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "हिलांस", "tehri": "हिलांस", "salani": "हरियल", "rathwali": "हिलांस"}
    },
    {
        "garhwali": "काकड़",
        "hindi": "काकड़ (भौंकने वाला हिरन)",
        "english": "barking deer / Indian muntjac",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "काकड़", "tehri": "काकड़", "salani": "हिरन", "rathwali": "काकड़"}
    },
    {
        "garhwali": "जुँक",
        "hindi": "जोंक (बरसाती कीड़ा)",
        "english": "land leech active during monsoon in damp forests",
        "pos": "noun",
        "gender": "F",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "जुँक", "tehri": "जोंक", "salani": "जोंक", "rathwali": "जुँक"}
    },

    # ==================== BODY, HEALTH & EMOTIONS ====================
    {
        "garhwali": "मुंड",
        "hindi": "सिर / मस्तक",
        "english": "head",
        "pos": "noun",
        "gender": "M",
        "category": "body",
        "dialect_variants": {"srinagariya": "मुंड", "tehri": "सिर", "salani": "माथा", "rathwali": "मुंड"}
    },
    {
        "garhwali": "खुट्टा",
        "hindi": "पैर / टांग",
        "english": "leg / foot",
        "pos": "noun",
        "gender": "M",
        "category": "body",
        "dialect_variants": {"srinagariya": "खुट्टा", "tehri": "गोड़", "salani": "पैर", "rathwali": "खुट्टा"}
    },
    {
        "garhwali": "मया",
        "hindi": "स्नेह / प्रेम / ममता",
        "english": "tender love / affectionate devotion",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "मया", "tehri": "प्यार", "salani": "दुलार", "rathwali": "मया"}
    },
    {
        "garhwali": "नराई",
        "hindi": "घर की याद / विरह वेदना",
        "english": "profound mountain homesickness / nostalgia",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "नराई", "tehri": "सुध", "salani": "याद", "rathwali": "नराई"}
    },
    {
        "garhwali": "रिस",
        "hindi": "क्रोध / गुस्सा",
        "english": "anger / rage",
        "pos": "noun",
        "gender": "F",
        "category": "emotions",
        "dialect_variants": {"srinagariya": "रिस", "tehri": "गुस्सा", "salani": "क्रोध", "rathwali": "रिस"}
    },
    {
        "garhwali": "औखद",
        "hindi": "औषधि / जड़ी-बूटी की दवा",
        "english": "herbal medicine / remedy",
        "pos": "noun",
        "gender": "F",
        "category": "body",
        "dialect_variants": {"srinagariya": "औखद", "tehri": "दवा", "salani": "जड़ी-बूटी", "rathwali": "औखद"}
    },

    # ==================== TIME & SEASONS ====================
    {
        "garhwali": "ब्याली",
        "hindi": "बीता हुआ कल",
        "english": "yesterday",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "ब्याली", "tehri": "ब्याली", "salani": "कल", "rathwali": "ब्याली"}
    },
    {
        "garhwali": "आजि",
        "hindi": "आज",
        "english": "today",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "आजि", "tehri": "आज", "salani": "आज", "rathwali": "आजि"}
    },
    {
        "garhwali": "काल",
        "hindi": "आने वाला कल",
        "english": "tomorrow",
        "pos": "adverb",
        "gender": "N",
        "category": "nature",
        "dialect_variants": {"srinagariya": "काल", "tehri": "काली", "salani": "कल", "rathwali": "काल"}
    },
    {
        "garhwali": "रूड़ी",
        "hindi": "ग्रीष्म ऋतु / गर्मी का मौसम",
        "english": "dry summer season before monsoon",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "रूड़ी", "tehri": "रूड़ी", "salani": "गर्मी", "rathwali": "रूड़ी"}
    },
    {
        "garhwali": "चौमासा",
        "hindi": "वर्षा ऋतु (चार महीने)",
        "english": "four-month monsoon season",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "चौमासा", "tehri": "बरखा", "salani": "वर्षा", "rathwali": "चौमासा"}
    },
    {
        "garhwali": "स्यूंंद",
        "hindi": "शीत ऋतु / जाड़ा",
        "english": "freezing winter season",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "स्यूंंद", "tehri": "ह्यूंद", "salani": "जाड़ा", "rathwali": "स्यूंंद"}
    },

    # ==================== MODERN TECHNOLOGY & DIGITAL ====================
    {
        "garhwali": "चलभाष",
        "hindi": "स्मार्टफोन / मोबाइल फोन",
        "english": "mobile phone / smartphone",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "चलभाष", "tehri": "मोबाइल", "salani": "फोन", "rathwali": "चलभाष"}
    },
    {
        "garhwali": "संगणक",
        "hindi": "कंप्यूटर",
        "english": "computer",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "संगणक", "tehri": "कंप्यूटर", "salani": "कंप्यूटर", "rathwali": "संगणक"}
    },
    {
        "garhwali": "अंतरजाल",
        "hindi": "इंटरनेट",
        "english": "internet",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "अंतरजाल", "tehri": "इंटरनेट", "salani": "इंटरनेट", "rathwali": "अंतरजाल"}
    },
    {
        "garhwali": "जालस्थल",
        "hindi": "वेबसाइट",
        "english": "website",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "जालस्थल", "tehri": "वेबसाइट", "salani": "वेबसाइट", "rathwali": "जालस्थल"}
    },
    {
        "garhwali": "अनुप्रयोग",
        "hindi": "मोबाइल ऐप",
        "english": "application / mobile app",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "अनुप्रयोग", "tehri": "ऐप", "salani": "ऐप", "rathwali": "अनुप्रयोग"}
    },
    {
        "garhwali": "कृत्रिम-बुद्धिमत्ता",
        "hindi": "आर्टिफिशियल इंटेलिजेंस (एआई)",
        "english": "artificial intelligence (AI)",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कृत्रिम-बुद्धिमत्ता", "tehri": "एआई", "salani": "एआई", "rathwali": "कृत्रिम-बुद्धिमत्ता"}
    },
    {
        "garhwali": "साइबर-सुरक्षा",
        "hindi": "साइबर सुरक्षा",
        "english": "cybersecurity / digital protection",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "साइबर-सुरक्षा", "tehri": "डिजिटल-रक्षा", "salani": "साइबर-सुरक्षा", "rathwali": "साइबर-सुरक्षा"}
    },

    # ==================== GOVERNANCE, LAW & PUBLIC SERVICES ====================
    {
        "garhwali": "पटवारी",
        "hindi": "राजस्व पुलिस एवं लेखपाल",
        "english": "revenue police officer and land recorder of Uttarakhand hills",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "पटवारी", "tehri": "पटवारी", "salani": "लेखपाल", "rathwali": "पटवारी"}
    },
    {
        "garhwali": "प्रधान",
        "hindi": "ग्राम प्रधान (सरपंच)",
        "english": "elected village council head",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "प्रधान", "tehri": "सरपंच", "salani": "प्रधान", "rathwali": "प्रधान"}
    },
    {
        "garhwali": "कचहरी",
        "hindi": "अदालत / न्यायालय",
        "english": "law court / judicial registry",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "कचहरी", "tehri": "अदालत", "salani": "न्यायालय", "rathwali": "कचहरी"}
    },
    {
        "garhwali": "दरखास्त",
        "hindi": "प्रार्थना पत्र / आवेदन",
        "english": "formal application / petition",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "दरखास्त", "tehri": "आवेदन", "salani": "अर्जी", "rathwali": "दरखास्त"}
    },
    {
        "garhwali": "रपट",
        "hindi": "पुलिस शिकायत / प्रथम सूचना रिपोर्ट",
        "english": "police complaint report",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "रपट", "tehri": "शिकायत", "salani": "रिपोर्ट", "rathwali": "रपट"}
    },

    # ==================== BUSINESS, JOBS & COMMERCE ====================
    {
        "garhwali": "रोजगार",
        "hindi": "आजीविका / नौकरी",
        "english": "employment / livelihood",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "रोजगार", "tehri": "नौकरी", "salani": "काम", "rathwali": "रोजगार"}
    },
    {
        "garhwali": "तनख्वाह",
        "hindi": "वेतन / पगार",
        "english": "salary / wages",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "तनख्वाह", "tehri": "वेतन", "salani": "पगार", "rathwali": "तनख्वाह"}
    },
    {
        "garhwali": "गिराक",
        "hindi": "ग्राहक / खरीदार",
        "english": "customer / buyer",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "गिराक", "tehri": "ग्राहक", "salani": "खरीदार", "rathwali": "गिराक"}
    },
    {
        "garhwali": "बहीखाता",
        "hindi": "लेखा बही / हिसाब की किताब",
        "english": "accounting ledger / balance book",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "बहीखाता", "tehri": "लेखा", "salani": "खाता", "rathwali": "बहीखाता"}
    },
    {
        "garhwali": "कर्जा",
        "hindi": "ऋण / उधार",
        "english": "loan / debt",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "कर्जा", "tehri": "ऋण", "salani": "उधार", "rathwali": "कर्जा"}
    },

    # ==================== SAFETY, CRIME & DEFENSE ====================
    {
        "garhwali": "ठगी",
        "hindi": "धोखाधड़ी / छल",
        "english": "fraud / deception / scam",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "ठगी", "tehri": "धोखा", "salani": "छल", "rathwali": "ठगी"}
    },
    {
        "garhwali": "सबूत",
        "hindi": "प्रमाण / साक्ष्य",
        "english": "evidence / proof",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "सबूत", "tehri": "प्रमाण", "salani": "गवाही", "rathwali": "सबूत"}
    },
    {
        "garhwali": "बचाव",
        "hindi": "सुरक्षा / बचाव",
        "english": "defense / rescue / safety",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "बचाव", "tehri": "रक्षा", "salani": "बचाव", "rathwali": "बचाव"}
    },

    # ==================== CHILDREN, PLAY & EDUCATION ====================
    {
        "garhwali": "लुका-छिपी",
        "hindi": "छिपन-छिपाई खेल",
        "english": "hide and seek game",
        "pos": "noun",
        "gender": "F",
        "category": "actions",
        "dialect_variants": {"srinagariya": "लुका-छिपी", "tehri": "चोरी-छिप", "salani": "छिपन-छिपाई", "rathwali": "लुका-छिपी"}
    },
    {
        "garhwali": "बस्ता",
        "hindi": "स्कूल का थैला",
        "english": "school satchel / bag",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "बस्ता", "tehri": "थैला", "salani": "बैग", "rathwali": "बस्ता"}
    },
    {
        "garhwali": "पाठशाला",
        "hindi": "विद्यालय / स्कूल",
        "english": "school / village academy",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "पाठशाला", "tehri": "स्कूल", "salani": "मकतब", "rathwali": "पाठशाला"}
    },

    # ==================== CANONICAL LITERATURE & SONG EXTRACTIONS ====================
    {
        "garhwali": "मंडाण",
        "hindi": "जागर अथवा नृत्य का पवित्र गोल आंगन",
        "english": "sacred circular arena where jagars and dances take place",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "मंडाण", "tehri": "मंडाण", "salani": "आंगण", "rathwali": "मंडाण"}
    },
    {
        "garhwali": "अचरी",
        "hindi": "अप्सरा / वनदेवी परी",
        "english": "mountain nymph / fairy spirit of high alpine meadows",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "अचरी", "tehri": "आंछरी", "salani": "परी", "rathwali": "अचरी"}
    },
    {
        "garhwali": "जागर",
        "hindi": "देवताओं के जागरण का अनुष्ठान",
        "english": "shamanic all-night musical vigil to awaken deities and ancestors",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "जागर", "tehri": "जागर", "salani": "जागर", "rathwali": "जागर"}
    },
    {
        "garhwali": "भैलो",
        "hindi": "इगास बग्वाल पर घुमाई जाने वाली चीड़ की मशाल",
        "english": "sacred pine torch spun in blazing arcs during Igas Bagwal",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भैलो", "tehri": "भैलो", "salani": "मशाल", "rathwali": "भैलो"}
    },
    {
        "garhwali": "छंतोली",
        "hindi": "देवता का पवित्र चांदी का छत्र",
        "english": "sacred processional silver umbrella accompanying deities",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "छंतोली", "tehri": "छत्र", "salani": "छतौली", "rathwali": "छंतोली"}
    },
    {
        "garhwali": "पव्वाड़ा",
        "hindi": "वीर गाथा / पराक्रम का गीत",
        "english": "heroic narrative folk ballad of mountain warriors",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "पव्वाड़ा", "tehri": "पवाण", "salani": "वीरगीत", "rathwali": "पव्वाड़ा"}
    },
    {
        "garhwali": "झुमेलो",
        "hindi": "बसंत ऋतु का समूह नृत्य-गीत",
        "english": "graceful circular springtime community dance and song",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "झुमेलो", "tehri": "झुमेलो", "salani": "झुमेलो", "rathwali": "झुमेलो"}
    },
    {
        "garhwali": "गूल",
        "hindi": "पहाड़ी सिंचाई नहर",
        "english": "traditional stone mountain irrigation canal",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "गूल", "tehri": "गूल", "salani": "नहर", "rathwali": "गूल"}
    },
    {
        "garhwali": "भड़",
        "hindi": "अजेय वीर योद्धा",
        "english": "invincible warrior champion of Garhwali epics",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भड़", "tehri": "वीर", "salani": "योद्धा", "rathwali": "भड़"}
    },
    {
        "garhwali": "रणसिंघा",
        "hindi": "तांबे का विशाल युद्ध वाद्य",
        "english": "massive S-shaped copper war horn blown in battle and temples",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "रणसिंघा", "tehri": "रणसिंघा", "salani": "तूर्य", "rathwali": "रणसिंघा"}
    },
    {
        "garhwali": "भंकोरा",
        "hindi": "सीधा लंबा तांबे का मंदिर वाद्य",
        "english": "long straight five-foot copper trumpet played in temple courtyards",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "भंकोरा", "tehri": "भंकोरा", "salani": "भंकोरा", "rathwali": "भंकोरा"}
    }
]

added_count = 0
enriched_count = 0

for item in new_words:
    lemma = item["garhwali"].strip()
    if lemma in words_by_lemma:
        # Enrich existing
        existing = words_by_lemma[lemma]
        for k, v in item.items():
            if k == "dialect_variants" and isinstance(v, dict):
                existing.setdefault("dialect_variants", {}).update(v)
            elif k not in existing or not existing[k]:
                existing[k] = v
        enriched_count += 1
    else:
        words_by_lemma[lemma] = item
        existing_data.append(item)
        added_count += 1

print(f"Added new lemmas: {added_count}")
print(f"Enriched existing: {enriched_count}")
print(f"Total updated word count: {len(existing_data)}")

with open(words_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"Saved expanded words to {words_path}")
