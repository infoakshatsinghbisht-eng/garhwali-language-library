"""
Script to expand garhwali/lexicon/data/words.json with comprehensive vocabulary for:
- School & Education
- Government Jobs, Appointments, Transfers, Pensions
- Business, Trading, Wholesale, Retail, Profits
- Government Job Scams, Paper Leaks, Bribes, Corruption
- Robbery, Thefts, Burglary, Police, Court, Custody, Jail
- Office Things, Files, Registers, Stamps, Desk Supplies
- Home Furniture, Bedding, Cleaning, Linen
- Crockery, Dining Utensils, Cookware, Kitchenware
- Children's Stages, Movements (crawl, toddler steps), Babble, Tantrums, Cradles
- Childhood Life-Cycle Rituals (Namkaran, Mundan/Jhadula, Annaprashan/Pasni, Karnavedha, Vidyarambha, Nazar-Utarna)
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

words_path = os.path.join("garhwali", "lexicon", "data", "words.json")
with open(words_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

print(f"Pre-domain expansion word count: {len(existing_data)}")
words_by_lemma = {w["garhwali"].strip(): w for w in existing_data}

new_domain_words = [
    # ==================== 1. SCHOOL & EDUCATION ====================
    {
        "garhwali": "स्कूल",
        "hindi": "विद्यालय / स्कूल",
        "english": "school",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "स्कूल", "tehri": "पाठशाला", "salani": "स्कूल", "rathwali": "स्कूल"}
    },
    {
        "garhwali": "पाटी",
        "hindi": "लकड़ी की स्लेट / तख्ती",
        "english": "wooden slate for writing practice",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "पाटी", "tehri": "पट्टी", "salani": "तख्ती", "rathwali": "पाटी"}
    },
    {
        "garhwali": "खड़िया",
        "hindi": "सफेद चाक / खड़िया मिट्टी",
        "english": "chalk for writing on slate or blackboard",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "खड़िया", "tehri": "चाक", "salani": "खड़िया", "rathwali": "खड़िया"}
    },
    {
        "garhwali": "कलम",
        "hindi": "कलम / पेन",
        "english": "pen / reed pen",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "कलम", "tehri": "पेन", "salani": "कलम", "rathwali": "कलम"}
    },
    {
        "garhwali": "दवात",
        "hindi": "स्याही की दवात",
        "english": "inkpot",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "दवात", "tehri": "दवात", "salani": "दवात", "rathwali": "दवात"}
    },
    {
        "garhwali": "सिहाई",
        "hindi": "स्याही",
        "english": "ink",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "सिहाई", "tehri": "स्याही", "salani": "सिहाई", "rathwali": "सिहाई"}
    },
    {
        "garhwali": "कापी",
        "hindi": "अभ्यास पुस्तिका / नोटबुक",
        "english": "notebook / exercise book",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "कापी", "tehri": "कापी", "salani": "नोटबुक", "rathwali": "कापी"}
    },
    {
        "garhwali": "पोथी",
        "hindi": "पुस्तक / ग्रंथ",
        "english": "book / scripture text",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "पोथी", "tehri": "किताब", "salani": "पोथी", "rathwali": "पोथी"}
    },
    {
        "garhwali": "मास्टरजी",
        "hindi": "अध्यापक / शिक्षक",
        "english": "school teacher / schoolmaster",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "मास्टरजी", "tehri": "गुरुजी", "salani": "शिक्षक", "rathwali": "मास्टरजी"}
    },
    {
        "garhwali": "विद्यार्थी",
        "hindi": "छात्र / शिक्षार्थी",
        "english": "student / pupil",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "विद्यार्थी", "tehri": "चेला", "salani": "छात्र", "rathwali": "विद्यार्थी"}
    },
    {
        "garhwali": "इम्तिहान",
        "hindi": "परीक्षा",
        "english": "examination / school test",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "इम्तिहान", "tehri": "परीक्षा", "salani": "इम्तिहान", "rathwali": "इम्तिहान"}
    },
    {
        "garhwali": "नतीजा",
        "hindi": "परीक्षाफल / परिणाम",
        "english": "exam result / outcome",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "नतीजा", "tehri": "परिणाम", "salani": "नतीजा", "rathwali": "नतीजा"}
    },
    {
        "garhwali": "छुट्टी",
        "hindi": "अवकाश / छुट्टी",
        "english": "school holiday / vacation",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "छुट्टी", "tehri": "अवकाश", "salani": "छुट्टी", "rathwali": "छुट्टी"}
    },
    {
        "garhwali": "घंटी",
        "hindi": "स्कूल की घंटी",
        "english": "school period bell",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "घंटी", "tehri": "घंटी", "salani": "टल्ली", "rathwali": "घंटी"}
    },
    {
        "garhwali": "हाजिरी",
        "hindi": "उपस्थिति / रोल कॉल",
        "english": "attendance roll-call",
        "pos": "noun",
        "gender": "F",
        "category": "education",
        "dialect_variants": {"srinagariya": "हाजिरी", "tehri": "हाजिरी", "salani": "उपस्थिति", "rathwali": "हाजिरी"}
    },
    {
        "garhwali": "गृहकार्य",
        "hindi": "गृहकार्य / होमवर्क",
        "english": "homework assignment",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "गृहकार्य", "tehri": "होमवर्क", "salani": "गृहकार्य", "rathwali": "गृहकार्य"}
    },
    {
        "garhwali": "वजीफा",
        "hindi": "छात्रवृत्ति",
        "english": "scholarship grant",
        "pos": "noun",
        "gender": "M",
        "category": "education",
        "dialect_variants": {"srinagariya": "वजीफा", "tehri": "छात्रवृत्ति", "salani": "वजीफा", "rathwali": "वजीफा"}
    },

    # ==================== 2. JOBS & GOVERNMENT EMPLOYMENT ====================
    {
        "garhwali": "सरकारी-नौकरी",
        "hindi": "सरकारी सेवा / सरकारी नौकरी",
        "english": "government job / public sector service",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "सरकारी-नौकरी", "tehri": "सरकारी-काम", "salani": "सरकारी-नौकरी", "rathwali": "सरकारी-नौकरी"}
    },
    {
        "garhwali": "भर्ती",
        "hindi": "नियुक्ति रैली / सेना या पुलिस में भर्ती",
        "english": "recruitment rally / enlistment",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "भर्ती", "tehri": "भरती", "salani": "भर्ती", "rathwali": "भर्ती"}
    },
    {
        "garhwali": "साक्षात्कार",
        "hindi": "साक्षात्कार / इंटरव्यू",
        "english": "job interview",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "साक्षात्कार", "tehri": "मुलाकात", "salani": "इंटरव्यू", "rathwali": "साक्षात्कार"}
    },
    {
        "garhwali": "तरक्की",
        "hindi": "पदोन्नति / तरक्की",
        "english": "job promotion",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "तरक्की", "tehri": "बढ़ोत्तरी", "salani": "तरक्की", "rathwali": "तरक्की"}
    },
    {
        "garhwali": "बदली",
        "hindi": "स्थानांतरण / तबादला",
        "english": "official transfer to another region",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "बदली", "tehri": "तबादला", "salani": "बदली", "rathwali": "बदळी"}
    },
    {
        "garhwali": "पेंशन",
        "hindi": "सेवानिवृत्ति पेंशन",
        "english": "retirement pension",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "पेंशन", "tehri": "पेंशन", "salani": "पेंशन", "rathwali": "पेंशन"}
    },
    {
        "garhwali": "हाकिम",
        "hindi": "उच्चाधिकारी / साहब",
        "english": "senior presiding officer / magistrate",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "हाकिम", "tehri": "अफसर", "salani": "हाकिम", "rathwali": "हाकिम"}
    },
    {
        "garhwali": "बाबू",
        "hindi": "दफ्तरी लिपिक / क्लर्क",
        "english": "office clerk",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "बाबू", "tehri": "क्लर्क", "salani": "बाबू", "rathwali": "बाबू"}
    },
    {
        "garhwali": "चपरासी",
        "hindi": "अर्दली / सेवादार",
        "english": "office attendant / peon",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "चपरासी", "tehri": "अर्दली", "salani": "चपरासी", "rathwali": "चपरासी"}
    },

    # ==================== 3. OFFICE THINGS & SUPPLIES ====================
    {
        "garhwali": "नस्ती",
        "hindi": "फाइल / मिसिल",
        "english": "official case file / folder",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "नस्ती", "tehri": "फाइल", "salani": "नस्ती", "rathwali": "नस्ती"}
    },
    {
        "garhwali": "रजिस्टर",
        "hindi": "दफ्तरी पंजी / रजिस्टर",
        "english": "office logbook register",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "रजिस्टर", "tehri": "बही", "salani": "रजिस्टर", "rathwali": "रजिस्टर"}
    },
    {
        "garhwali": "मोहर",
        "hindi": "रबर की मुहर / सील",
        "english": "official rubber or metal stamp / seal",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "मोहर", "tehri": "सील", "salani": "मोहर", "rathwali": "मोहर"}
    },
    {
        "garhwali": "लिफाफा",
        "hindi": "डाक लिफाफा",
        "english": "postal envelope",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "लिफाफा", "tehri": "लिफाफा", "salani": "लिफाफा", "rathwali": "लिफाफा"}
    },
    {
        "garhwali": "नत्थी",
        "hindi": "कागजात को धागे से बांधना",
        "english": "tagging papers together with twine / file fastener",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "नत्थी", "tehri": "टैग", "salani": "नत्थी", "rathwali": "नत्थी"}
    },
    {
        "garhwali": "मेज",
        "hindi": "मेज / टेबल",
        "english": "office desk / work table",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "मेज", "tehri": "टेबल", "salani": "मेज", "rathwali": "मेज"}
    },
    {
        "garhwali": "कुर्सी",
        "hindi": "कुर्सी",
        "english": "chair",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "कुर्सी", "tehri": "कुर्सी", "salani": "कुर्सी", "rathwali": "कुर्सी"}
    },

    # ==================== 4. BUSINESS, TRADING & COMMERCE ====================
    {
        "garhwali": "ब्योपार",
        "hindi": "व्यापार / वाणिज्य",
        "english": "trade / business / commerce",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "ब्योपार", "tehri": "व्यापार", "salani": "कारोबार", "rathwali": "ब्योपार"}
    },
    {
        "garhwali": "दूकानदार",
        "hindi": "दुकानदार",
        "english": "shopkeeper / retail store owner",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "दूकानदार", "tehri": "दूकानदार", "salani": "दुकानदार", "rathwali": "दूकानदार"}
    },
    {
        "garhwali": "थोक-ब्योपार",
        "hindi": "थोक व्यापार",
        "english": "wholesale trading",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "थोक-ब्योपार", "tehri": "थोक", "salani": "थोक-व्यापार", "rathwali": "थोक-ब्योपार"}
    },
    {
        "garhwali": "फुटकर",
        "hindi": "फुटकर बिक्री",
        "english": "retail trade / loose sale",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "फुटकर", "tehri": "खुदरा", "salani": "फुटकर", "rathwali": "फुटकर"}
    },
    {
        "garhwali": "पूँजी",
        "hindi": "व्यापारिक पूँजी",
        "english": "business capital / investment",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "पूँजी", "tehri": "पूंजी", "salani": "सरमाया", "rathwali": "पूँजी"}
    },
    {
        "garhwali": "मुनाफा",
        "hindi": "मुनाफा / लाभ",
        "english": "profit / commercial gain",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "मुनाफा", "tehri": "नफा", "salani": "लाभ", "rathwali": "मुनाफा"}
    },
    {
        "garhwali": "घाटो",
        "hindi": "व्यापारिक घाटा / नुकसान",
        "english": "financial loss",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "घाटो", "tehri": "नुकसान", "salani": "घाटा", "rathwali": "घाटो"}
    },
    {
        "garhwali": "मंडी",
        "hindi": "अनाज व सब्जी मंडी",
        "english": "wholesale grain or vegetable market",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "मंडी", "tehri": "मंडी", "salani": "बाजार", "rathwali": "मंडी"}
    },
    {
        "garhwali": "पर्चा",
        "hindi": "बिक्री का पर्चा / बिल",
        "english": "invoice / sales bill",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "पर्चा", "tehri": "बिल", "salani": "पर्चा", "rathwali": "पर्चा"}
    },
    {
        "garhwali": "रसीद",
        "hindi": "भुगतान की रसीद",
        "english": "payment receipt",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "रसीद", "tehri": "पावती", "salani": "रसीद", "rathwali": "रसीद"}
    },
    {
        "garhwali": "साझेदारी",
        "hindi": "व्यापार में भागीदारी",
        "english": "business partnership",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "साझेदारी", "tehri": "साझेदारी", "salani": "हिस्सेदारी", "rathwali": "साझेदारी"}
    },
    {
        "garhwali": "उधार",
        "hindi": "उधार पर सामान",
        "english": "credit purchase",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "उधार", "tehri": "उधार", "salani": "कर्ज", "rathwali": "उधार"}
    },
    {
        "garhwali": "साहूकार",
        "hindi": "पारंपरिक महाजन / साहूकार",
        "english": "traditional village moneylender",
        "pos": "noun",
        "gender": "M",
        "category": "business",
        "dialect_variants": {"srinagariya": "साहूकार", "tehri": "महाजन", "salani": "सेठ", "rathwali": "साहूकार"}
    },

    # ==================== 5. SCAMS, CORRUPTION, ROBBERY & POLICE ====================
    {
        "garhwali": "घपलो",
        "hindi": "घोटाला / हेराफेरी",
        "english": "scam / financial embezzlement / fraud",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "घपलो", "tehri": "घोटाला", "salani": "घपला", "rathwali": "घपलो"}
    },
    {
        "garhwali": "पर्चा-लीक",
        "hindi": "भर्ती परीक्षा का पेपर लीक",
        "english": "recruitment exam question paper leak scam",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "पर्चा-लीक", "tehri": "पेपर-लीक", "salani": "पर्चा-लीक", "rathwali": "पर्चा-लीक"}
    },
    {
        "garhwali": "घूस",
        "hindi": "रिश्वत / घूस",
        "english": "bribe / illegal payoff",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "घूस", "tehri": "रिश्वत", "salani": "घूस", "rathwali": "घूस"}
    },
    {
        "garhwali": "भ्रष्टाचार",
        "hindi": "भ्रष्टाचार",
        "english": "administrative corruption",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "भ्रष्टाचार", "tehri": "भ्रष्टाचार", "salani": "बदचलनी", "rathwali": "भ्रष्टाचार"}
    },
    {
        "garhwali": "दलाल",
        "hindi": "बिचौलिया / दलाल",
        "english": "corrupt middleman / tout",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "दलाल", "tehri": "बिचौलिया", "salani": "दलाल", "rathwali": "दलाल"}
    },
    {
        "garhwali": "फर्जी",
        "hindi": "नकली / जाली दस्तावेज",
        "english": "counterfeit / forged / fraudulent",
        "pos": "adjective",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "फर्जी", "tehri": "नकली", "salani": "जाली", "rathwali": "फर्जी"}
    },
    {
        "garhwali": "धोखो",
        "hindi": "धोखा / छल",
        "english": "cheating / deception",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "धोखो", "tehri": "धोखा", "salani": "छल", "rathwali": "धोखो"}
    },
    {
        "garhwali": "डाका",
        "hindi": "सशस्त्र डकैती",
        "english": "armed dacoity / violent gang robbery",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "डाका", "tehri": "डकैती", "salani": "डाका", "rathwali": "डाका"}
    },
    {
        "garhwali": "लूट",
        "hindi": "लूटपाट",
        "english": "robbery / plunder / looting",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "लूट", "tehri": "लूटपाट", "salani": "लूट", "rathwali": "लूट"}
    },
    {
        "garhwali": "चोर",
        "hindi": "चोर",
        "english": "thief / burglar",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "चोर", "tehri": "चोर", "salani": "चोर", "rathwali": "चोर"}
    },
    {
        "garhwali": "सेंधमारी",
        "hindi": "दीवार फोड़कर चोरी करना",
        "english": "burglary by housebreaking through walls",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "सेंधमारी", "tehri": "सेंध", "salani": "सेंधमारी", "rathwali": "सेंधमारी"}
    },
    {
        "garhwali": "जेबकतरा",
        "hindi": "जेब काटने वाला",
        "english": "pickpocket",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "जेबकतरा", "tehri": "जेबकतरा", "salani": "उचक्का", "rathwali": "जेबकतरा"}
    },
    {
        "garhwali": "उगाही",
        "hindi": "जबरन वसूली / अवैध उगाही",
        "english": "extortion of money",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "उगाही", "tehri": "वसूली", "salani": "उगाही", "rathwali": "उगाही"}
    },
    {
        "garhwali": "थाना",
        "hindi": "पुलिस थाना",
        "english": "police station",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "थाना", "tehri": "कोतवाली", "salani": "थाना", "rathwali": "थाना"}
    },
    {
        "garhwali": "थानेदार",
        "hindi": "दरोगा / थाना प्रभारी",
        "english": "station house officer / police sub-inspector",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "थानेदार", "tehri": "दारोगा", "salani": "कोतवाल", "rathwali": "थानेदार"}
    },
    {
        "garhwali": "गिरफ्तारी",
        "hindi": "पुलिस हिरासत / गिरफ्तारी",
        "english": "police arrest / apprehension",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "गिरफ्तारी", "tehri": "पकड़", "salani": "हिरासत", "rathwali": "गिरफ्तारी"}
    },
    {
        "garhwali": "हथकड़ी",
        "hindi": "हथकड़ी",
        "english": "handcuffs",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "हथकड़ी", "tehri": "हथकड़ी", "salani": "बेड़ी", "rathwali": "हथकड़ी"}
    },
    {
        "garhwali": "हवालात",
        "hindi": "पुलिस हवालात / जेल",
        "english": "lockup cell / jail",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "हवालात", "tehri": "कैदखाना", "salani": "जेल", "rathwali": "हवालात"}
    },
    {
        "garhwali": "जमानत",
        "hindi": "अदालत से जमानत",
        "english": "court bail",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "जमानत", "tehri": "जमानत", "salani": "रिहाई", "rathwali": "जमानत"}
    },
    {
        "garhwali": "बयान",
        "hindi": "अदालती गवाही / बयान",
        "english": "legal statement / witness deposition",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "बयान", "tehri": "गवाही", "salani": "बयान", "rathwali": "बयान"}
    },
    {
        "garhwali": "सजा",
        "hindi": "अदालती सजा / कारावास",
        "english": "judicial sentence / penal punishment",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "सजा", "tehri": "दंड", "salani": "सजा", "rathwali": "सजा"}
    },
    {
        "garhwali": "मुजरिम",
        "hindi": "दोषी / अपराधी",
        "english": "convict / criminal",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "मुजरिम", "tehri": "अपराधी", "salani": "गुनहगार", "rathwali": "मुजरिम"}
    },
    {
        "garhwali": "मुकद्दमा",
        "hindi": "न्यायालयी वाद / मुकदमा",
        "english": "court lawsuit / litigation trial",
        "pos": "noun",
        "gender": "M",
        "category": "social",
        "dialect_variants": {"srinagariya": "मुकद्दमा", "tehri": "वाद", "salani": "केस", "rathwali": "मुकद्दमा"}
    },

    # ==================== 6. HOME THINGS & FURNITURE ====================
    {
        "garhwali": "खाट",
        "hindi": "चारपाई / खाट",
        "english": "traditional wooden woven string cot",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "खाट", "tehri": "चारपाई", "salani": "खटोला", "rathwali": "खाट"}
    },
    {
        "garhwali": "पलंग",
        "hindi": "बड़ा लकड़ी का पलंग",
        "english": "wooden bedstead",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पलंग", "tehri": "पलंग", "salani": "बेड", "rathwali": "पलंग"}
    },
    {
        "garhwali": "गद्दा",
        "hindi": "कपास का गद्दा",
        "english": "cotton sleeping mattress",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "गद्दा", "tehri": "गद्दा", "salani": "तौशक", "rathwali": "गद्दा"}
    },
    {
        "garhwali": "सिरहाना",
        "hindi": "तकिया / सिरहाना",
        "english": "head pillow / headrest",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "सिरहाना", "tehri": "तकिया", "salani": "सिरहाना", "rathwali": "सिरहाणा"}
    },
    {
        "garhwali": "रजाई",
        "hindi": "सर्दियों की रजाई",
        "english": "winter cotton-padded quilt",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "रजाई", "tehri": "लेफ", "salani": "रजाई", "rathwali": "रजाई"}
    },
    {
        "garhwali": "कंबल",
        "hindi": "ऊन का कंबल",
        "english": "warm woolen blanket",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "कंबल", "tehri": "कम्बल", "salani": "लोई", "rathwali": "कम्बळ"}
    },
    {
        "garhwali": "चादर",
        "hindi": "बिस्तर की चादर",
        "english": "cotton bedsheet",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "चादर", "tehri": "चादर", "salani": "खेस", "rathwali": "चादर"}
    },
    {
        "garhwali": "अलमारी",
        "hindi": "अलमारी",
        "english": "cupboard / wardrobe",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "अलमारी", "tehri": "अलमारी", "salani": "कोठरी", "rathwali": "अलमारी"}
    },
    {
        "garhwali": "सीसा",
        "hindi": "दर्पण / आईना",
        "english": "looking mirror",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "सीसा", "tehri": "ऐना", "salani": "दर्पण", "rathwali": "सीसा"}
    },
    {
        "garhwali": "बुहारी",
        "hindi": "झाड़ू",
        "english": "straw broom for sweeping house",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "बुहारी", "tehri": "झाड़ू", "salani": "बढ़नी", "rathwali": "बुहारी"}
    },
    {
        "garhwali": "पोछा",
        "hindi": "फर्श पोंछने का कपड़ा",
        "english": "floor mop cloth",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पोछा", "tehri": "पोछा", "salani": "पोछा", "rathwali": "पोछा"}
    },
    {
        "garhwali": "बाल्टी",
        "hindi": "पानी की बाल्टी",
        "english": "water bucket",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "बाल्टी", "tehri": "डोल", "salani": "बाल्टी", "rathwali": "बाल्टी"}
    },
    {
        "garhwali": "मग्गो",
        "hindi": "नहाने का मग",
        "english": "bathing or washing mug",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "मग्गो", "tehri": "मग", "salani": "डब्बा", "rathwali": "मग्गो"}
    },
    {
        "garhwali": "अरगनी",
        "hindi": "कपड़े सुखाने की डोरी / अरगनी",
        "english": "clothesline / hanging rod for clothes",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "अरगनी", "tehri": "डोरी", "salani": "अलंगनी", "rathwali": "अरगणी"}
    },
    {
        "garhwali": "संदूक",
        "hindi": "लोहे या लकड़ी का बड़ा बक्सा",
        "english": "large storage trunk / clothes chest",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "संदूक", "tehri": "पेटी", "salani": "बक्सा", "rathwali": "संदूक"}
    },
    {
        "garhwali": "ताला",
        "hindi": "ताला",
        "english": "padlock / door lock",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "ताला", "tehri": "कुंडी", "salani": "ताला", "rathwali": "ताळा"}
    },
    {
        "garhwali": "कुंजी",
        "hindi": "चाबी",
        "english": "door key",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "कुंजी", "tehri": "चाबी", "salani": "ताली", "rathwali": "कुंजी"}
    },
    {
        "garhwali": "चटाई",
        "hindi": "बैठने की चटाई",
        "english": "woven grass floor sitting mat",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "चटाई", "tehri": "गौंदली", "salani": "सफ़", "rathwali": "चटाई"}
    },
    {
        "garhwali": "पीढ़ा",
        "hindi": "बैठने का छोटा लकड़ी का पाटा",
        "english": "low wooden sitting stool",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पीढ़ा", "tehri": "पाटा", "salani": "मुढ़ा", "rathwali": "पीढ़ा"}
    },

    # ==================== 7. CROCKERY, UTENSILS & COOKWARE ====================
    {
        "garhwali": "थाली",
        "hindi": "भोजन की थाली",
        "english": "dining plate / platter",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "थाली", "tehri": "थाळी", "salani": "तश्तरी", "rathwali": "थाळी"}
    },
    {
        "garhwali": "कटोरा",
        "hindi": "दाल या सब्जी का कटोरा",
        "english": "deep dining bowl",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "कटोरा", "tehri": "बटोही", "salani": "कटोरी", "rathwali": "कटोरा"}
    },
    {
        "garhwali": "कचौड़ी",
        "hindi": "छोटी कटोरी",
        "english": "small side bowl for chutney or desserts",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "कचौड़ी", "tehri": "कटोरी", "salani": "प्याली", "rathwali": "कचौळी"}
    },
    {
        "garhwali": "गिलास",
        "hindi": "पानी पीने का गिलास",
        "english": "drinking glass / metal tumbler",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "गिलास", "tehri": "ग्लास", "salani": "गिलास", "rathwali": "गिलास"}
    },
    {
        "garhwali": "प्याला",
        "hindi": "चाय का कप",
        "english": "tea cup",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "प्याला", "tehri": "कप", "salani": "प्याली", "rathwali": "प्याला"}
    },
    {
        "garhwali": "तश्तरी",
        "hindi": "कप के नीचे की तश्तरी / प्लेट",
        "english": "saucer / small serving dish",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "तश्तरी", "tehri": "प्लेट", "salani": "रकाबी", "rathwali": "तश्तरी"}
    },
    {
        "garhwali": "जग",
        "hindi": "पानी का जग",
        "english": "water serving jug",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "जग", "tehri": "जग", "salani": "सुराही", "rathwali": "जग"}
    },
    {
        "garhwali": "चमचा",
        "hindi": "चम्मच",
        "english": "eating spoon",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "चमचा", "tehri": "चम्मू", "salani": "चम्मच", "rathwali": "चमचा"}
    },
    {
        "garhwali": "काँटा",
        "hindi": "काँटा चम्मच",
        "english": "dining fork",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "काँटा", "tehri": "कांटा", "salani": "कांटा", "rathwali": "काँटा"}
    },
    {
        "garhwali": "चाकू",
        "hindi": "सब्जी काटने का चाकू / छुरी",
        "english": "kitchen cutting knife",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "चाकू", "tehri": "छुरी", "salani": "चाकू", "rathwali": "चाकू"}
    },
    {
        "garhwali": "पतीला",
        "hindi": "दूध या दाल पकाने का भगोना / पतीला",
        "english": "large cooking vessel / saucepan",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "पतीला", "tehri": "भगोना", "salani": "देगची", "rathwali": "पतीळा"}
    },
    {
        "garhwali": "कड़ाही",
        "hindi": "लोहे या पीतल की कड़ाही",
        "english": "deep iron or brass cooking wok",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "कड़ाही", "tehri": "कढ़ाई", "salani": "कड़ाही", "rathwali": "कड़ाही"}
    },
    {
        "garhwali": "ढक्कन",
        "hindi": "बर्तन का ढक्कन",
        "english": "pot lid / vessel cover",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "ढक्कन", "tehri": "ढाकण", "salani": "सरपोश", "rathwali": "ढक्कन"}
    },
    {
        "garhwali": "कद्दूकस",
        "hindi": "सब्जी कसने का कद्दूकस",
        "english": "vegetable grater",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "कद्दूकस", "tehri": "कसनी", "salani": "कद्दूकस", "rathwali": "कद्दूकस"}
    },
    {
        "garhwali": "छिलनी",
        "hindi": "सब्जी छीलने का चाकू",
        "english": "vegetable peeler",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "छिलनी", "tehri": "छिलनी", "salani": "पीलर", "rathwali": "छिलणी"}
    },
    {
        "garhwali": "छलनी",
        "hindi": "आटा या चाय छानने की छलनी",
        "english": "tea strainer / flour sieve",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "छलनी", "tehri": "छानी", "salani": "छलनी", "rathwali": "छळणी"}
    },
    {
        "garhwali": "चकला",
        "hindi": "रोटी बेलने का चकला",
        "english": "circular roti rolling board",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "चकला", "tehri": "चकला", "salani": "चकला", "rathwali": "चकळा"}
    },
    {
        "garhwali": "बेलन",
        "hindi": "रोटी बेलने का बेलन",
        "english": "wooden rolling pin",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "बेलन", "tehri": "बेलन", "salani": "बेलन", "rathwali": "बेळन"}
    },
    {
        "garhwali": "मटका",
        "hindi": "मिट्टी का ठंडा पानी रखने का घड़ा",
        "english": "earthen clay water pitcher",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "मटका", "tehri": "घड़ा", "salani": "मटका", "rathwali": "मटका"}
    },
    {
        "garhwali": "सुराही",
        "hindi": "लंबी गर्दन वाली मिट्टी की सुराही",
        "english": "long-necked clay water flask",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "सुराही", "tehri": "सुराही", "salani": "सुराही", "rathwali": "सुराही"}
    },
    {
        "garhwali": "डिब्बा",
        "hindi": "भोजन रखने का डिब्बा / टिफिन",
        "english": "storage box / lunch container",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "डिब्बा", "tehri": "डब्बा", "salani": "कनस्तर", "rathwali": "डिब्बा"}
    },
    {
        "garhwali": "सँड़सी",
        "hindi": "गरम बर्तन पकड़ने की संडासी",
        "english": "pincer tongs for grasping hot pots",
        "pos": "noun",
        "gender": "F",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "सँड़सी", "tehri": "संडासी", "salani": "चिमटी", "rathwali": "सँड़सी"}
    },
    {
        "garhwali": "तवा",
        "hindi": "रोटी सेंकने का लोहे का तवा",
        "english": "iron flat griddle for baking bread",
        "pos": "noun",
        "gender": "M",
        "category": "crockery",
        "dialect_variants": {"srinagariya": "तवा", "tehri": "तवा", "salani": "तवा", "rathwali": "तवा"}
    },

    # ==================== 8. CHILDREN: MOVEMENTS, BABBLE, CRYING & WORDS ====================
    {
        "garhwali": "लल्ला",
        "hindi": "नवजात शिशु / छोटा बालक",
        "english": "infant / newborn baby",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "लल्ला", "tehri": "नानू", "salani": "बच्चा", "rathwali": "लल्ला"}
    },
    {
        "garhwali": "पालना",
        "hindi": "शिशु का झूला / पालना",
        "english": "baby rocking cradle / crib",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "पालना", "tehri": "हिंडोला", "salani": "झूला", "rathwali": "पाळना"}
    },
    {
        "garhwali": "लोरी",
        "hindi": "शिशु को सुलाने का मधुर गीत",
        "english": "maternal baby lullaby",
        "pos": "noun",
        "gender": "F",
        "category": "children",
        "dialect_variants": {"srinagariya": "लोरी", "tehri": "लोरी", "salani": "लोरकी", "rathwali": "लोरी"}
    },
    {
        "garhwali": "स्तनपान",
        "hindi": "शिशु को मां का दूध पिलाना",
        "english": "breastfeeding / nursing infant",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "स्तनपान", "tehri": "दूध-पिलाणु", "salani": "दूध-पिलाना", "rathwali": "स्तनपान"}
    },
    {
        "garhwali": "घुटन्यूं-चलणु",
        "hindi": "घुटनों के बल चलना (रेंगना)",
        "english": "to crawl on hands and knees",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "घुटन्यूं-चलणु", "tehri": "घुटने-चलना", "salani": "घिसटना", "rathwali": "घुटन्यूं-चलणु"}
    },
    {
        "garhwali": "डगमग-चलणु",
        "hindi": "डगमगाते नन्हें कदमों से चलना",
        "english": "to take wobbly first toddler steps",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "डगमग-चलणु", "tehri": "डगमगाना", "salani": "ठुमकना", "rathwali": "डगमग-चलणु"}
    },
    {
        "garhwali": "रून-झुन",
        "hindi": "पैरों में घुंघरू बांधकर चलना",
        "english": "toddler walking with tinkling ankle-bell steps",
        "pos": "adverb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "रून-झुन", "tehri": "छम-छम", "salani": "झुन-झुन", "rathwali": "रून-झुन"}
    },
    {
        "garhwali": "तोतलो-बोलणु",
        "hindi": "तोतली मीठी बोली बोलना",
        "english": "to talk in sweet baby babble",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "तोतलो-बोलणु", "tehri": "तोतलाना", "salani": "तोतला-बोलना", "rathwali": "तोतळो-बोलणु"}
    },
    {
        "garhwali": "किलकारी",
        "hindi": "शिशु की खुशी की हंसी / चीख",
        "english": "baby squeal of delight / happy shriek",
        "pos": "noun",
        "gender": "F",
        "category": "children",
        "dialect_variants": {"srinagariya": "किलकारी", "tehri": "किलकारी", "salani": "चीख", "rathwali": "किळकारी"}
    },
    {
        "garhwali": "बिलखणु",
        "hindi": "फफक कर रोना / सिसकना",
        "english": "to sob / weep inconsolably",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बिलखणु", "tehri": "सिसकना", "salani": "रोना", "rathwali": "बिलखणु"}
    },
    {
        "garhwali": "मचलणु",
        "hindi": "बालहठ करना / मचलना",
        "english": "to throw a childhood tantrum / sulk stubbornly",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "मचलणु", "tehri": "जिद-करना", "salani": "मचलना", "rathwali": "मचळणु"}
    },
    {
        "garhwali": "चिपकणु",
        "hindi": "मां के गले से लिपट जाना",
        "english": "to cling tightly to mother's chest or neck",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "चिपकणु", "tehri": "लिपटना", "salani": "गले-लगना", "rathwali": "चिपकणु"}
    },
    {
        "garhwali": "कांख",
        "hindi": "मां की गोद / कमर जहां बालक को बैठाते हैं",
        "english": "mother's hip or side lap where child is carried",
        "pos": "noun",
        "gender": "F",
        "category": "children",
        "dialect_variants": {"srinagariya": "कांख", "tehri": "गोद", "salani": "कांख", "rathwali": "कांख"}
    },
    {
        "garhwali": "कंचा",
        "hindi": "कांच की गोलियां (कंचे)",
        "english": "glass marbles game",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "कंचा", "tehri": "ल्वाटा", "salani": "गोली", "rathwali": "कंचा"}
    },
    {
        "garhwali": "स्टापू",
        "hindi": "स्टापू / छिपरी (कूदने का खेल)",
        "english": "hopscotch jumping game",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "स्टापू", "tehri": "छिपरी", "salani": "किटकित", "rathwali": "स्टापू"}
    },
    {
        "garhwali": "लट्टू",
        "hindi": "डोरी से नचाने का लट्टू",
        "english": "spinning top toy",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "लट्टू", "tehri": "लट्टू", "salani": "भौंवरा", "rathwali": "लट्टू"}
    },
    {
        "garhwali": "पतंग",
        "hindi": "आकाश में उड़ने वाली पतंग",
        "english": "paper kite",
        "pos": "noun",
        "gender": "F",
        "category": "children",
        "dialect_variants": {"srinagariya": "पतंग", "tehri": "गुड्डी", "salani": "पतंग", "rathwali": "पतंग"}
    },
    {
        "garhwali": "झूला",
        "hindi": "पेड़ पर डाला गया झूला",
        "english": "tree branch rope swing",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "झूला", "tehri": "हिंडोला", "salani": "पिंग", "rathwali": "झूळा"}
    },
    {
        "garhwali": "कूदणु",
        "hindi": "उछलना / कूदना",
        "english": "to jump / leap",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "कूदणु", "tehri": "उछलना", "salani": "कूदना", "rathwali": "कूदणु"}
    },
    {
        "garhwali": "छलांग-मारणु",
        "hindi": "लंबी छलांग लगाना",
        "english": "to take a wide leap across mountain rocks",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "छलांग-मारणु", "tehri": "फांदना", "salani": "कूदना", "rathwali": "छलांग-मारणु"}
    },
    {
        "garhwali": "ठोकर-खाणु",
        "hindi": "पत्थर से ठोकर लगना",
        "english": "to stumble / trip over stones",
        "pos": "verb",
        "gender": "N",
        "category": "actions",
        "dialect_variants": {"srinagariya": "ठोकर-खाणु", "tehri": "फिसलना", "salani": "ठोकर-लगना", "rathwali": "ठोकर-खाणु"}
    },

    # ==================== 9. CHILDHOOD LIFE-CYCLE RITUALS ====================
    {
        "garhwali": "नामकरण",
        "hindi": "नामकरण संस्कार (११वें/१२वें दिन)",
        "english": "naming ritual ceremony held on 11th or 12th day after birth",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "नामकरण", "tehri": "नामकरण", "salani": "नामकरण", "rathwali": "नामकरण"}
    },
    {
        "garhwali": "झडूला",
        "hindi": "चूड़ाकर्म / मुंडन संस्कार (प्रथम बाल उतारना)",
        "english": "first ritual tonsure / sacred haircut ceremony",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "झडूला", "tehri": "मुंडन", "salani": "झडूला", "rathwali": "झडूळा"}
    },
    {
        "garhwali": "अन्नप्राशन",
        "hindi": "अन्नप्राशन (प्रथम ठोस आहार/खीर चटाना)",
        "english": "first solid food tasting ritual at six months",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "अन्नप्राशन", "tehri": "पसनी", "salani": "अन्नप्राशन", "rathwali": "अन्नप्राशन"}
    },
    {
        "garhwali": "कर्णवेध",
        "hindi": "कान छेदन संस्कार",
        "english": "sacred ritual ear piercing ceremony",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "कर्णवेध", "tehri": "कान-छेदन", "salani": "कर्णवेध", "rathwali": "कर्णवेध"}
    },
    {
        "garhwali": "विद्यारंभ",
        "hindi": "अक्षरारंभ / विद्यारंभ संस्कार",
        "english": "initiation of learning and writing ceremony",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "विद्यारंभ", "tehri": "अक्षरारंभ", "salani": "विद्यारंभ", "rathwali": "विद्यारंभ"}
    },
    {
        "garhwali": "नजर-उतारणु",
        "hindi": "शिशु की बुरी नजर उतारना",
        "english": "ritual to ward off evil eye from infant with salt and chilies",
        "pos": "verb",
        "gender": "N",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "नजर-उतारणु", "tehri": "दृष्टि-उतारना", "salani": "नजर-झाड़ना", "rathwali": "नजर-उतारणु"}
    }
]

added_count = 0
enriched_count = 0

for item in new_domain_words:
    lemma = item["garhwali"].strip()
    if lemma in words_by_lemma:
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

print(f"Domain expansion added new lemmas: {added_count}")
print(f"Domain expansion enriched existing: {enriched_count}")
print(f"New total word count: {len(existing_data)}")

with open(words_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"Saved domain expanded words to {words_path}")
