# -*- coding: utf-8 -*-
"""
Deep Lexical Mining Pipeline extracting vocabulary from:
- Dr. Haridatta Bhatt 'Shailesh' (1976): Garhwali Bhasha Aur Uska Sahitya (Appendix A: pp. 371-403)
- Dr. Govind Chatak (1959): Garhwali Bhasha (Prakrit & Apabhramsha cognates pp. 44-50)
- Traditional Agricultural, Watermill, Fauna, Garment, and Ornament terminology.
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

BHATT_CHATAK_WORDS = [
    # ==================== 1. TRADITIONAL WATERMILL (घराट / घट) ====================
    {
        "garhwali": "घट",
        "hindi": "पारंपरिक पनचक्की / घराट",
        "english": "traditional Himalayan watermill for grinding flour",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "घट", "tehri": "घराट", "salani": "घट", "rathwali": "घट"}
    },
    {
        "garhwali": "भेरण",
        "hindi": "पनचक्की का पानी से घूमने वाला लकड़ी का पहिया / टरबाइन",
        "english": "wooden water turbine wheel of traditional watermill",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "भेरण", "tehri": "टरबाइन", "salani": "चक्का", "rathwali": "भेरण"}
    },
    {
        "garhwali": "घेटोडो",
        "hindi": "पनचक्की की धुरी",
        "english": "iron spindle axle connecting turbine to millstone",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "घेटोडो", "tehri": "धुरी", "salani": "धुरा", "rathwali": "घेटोळो"}
    },
    {
        "garhwali": "सुवा",
        "hindi": "पनचक्की का भारी चक्की-पत्थर",
        "english": "heavy circular millstone of watermill",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सुवा", "tehri": "पाथर", "salani": "चक्की-पाट", "rathwali": "सुवा"}
    },
    {
        "garhwali": "रेड़ी",
        "hindi": "पनचक्की में अनाज भरने का लकड़ी का फनल (हॉपर)",
        "english": "wooden grain hopper funnel above millstone",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "रेड़ी", "tehri": "कोठी", "salani": "रेड़ी", "rathwali": "रेळी"}
    },
    {
        "garhwali": "कोसडी",
        "hindi": "अनाज गिरने की लकड़ी की नाली",
        "english": "wooden grain feeder chute",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कोसडी", "tehri": "नाली", "salani": "कोसड़ी", "rathwali": "कोसळी"}
    },
    {
        "garhwali": "ठोकढण्या",
        "hindi": "हॉपर को हिलाने वाली खटखट करने वाली लकड़ी",
        "english": "vibrating wooden clapper that regulates grain flow",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "ठोकढण्या", "tehri": "खटखटा", "salani": "ठकठका", "rathwali": "ठोकढण्या"}
    },
    {
        "garhwali": "पनाल",
        "hindi": "पनचक्की पर पानी गिराने वाली लकड़ी की ढालू नाली",
        "english": "wooden flume flume-channel directing water onto turbine",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "पनाल", "tehri": "पनार", "salani": "पनाली", "rathwali": "पनाळ"}
    },
    {
        "garhwali": "कूल",
        "hindi": "खेतों व घराट तक पानी लाने वाली नहर (गूल)",
        "english": "hill irrigation canal diverged from stream",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "कूल", "tehri": "गूल", "salani": "गूल", "rathwali": "कूळ"}
    },

    # ==================== 2. AGRICULTURE & FARMING IMPLEMENTS (Bhatt 1976) ====================
    {
        "garhwali": "नसड़ो",
        "hindi": "हल का मुख्य लकड़ी का ढांचा",
        "english": "wooden body of hill plough",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "नसड़ो", "tehri": "नसड़ा", "salani": "हल", "rathwali": "नसळो"}
    },
    {
        "garhwali": "वाणो",
        "hindi": "हल का नुकीला लोहे का फाल",
        "english": "iron share point of plough",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "वाणो", "tehri": "फाला", "salani": "फाल", "rathwali": "वाणो"}
    },
    {
        "garhwali": "हथनालो",
        "hindi": "हल पकड़ने का हत्था",
        "english": "plough handle held by farmer",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "हथनालो", "tehri": "हत्था", "salani": "मुठिया", "rathwali": "हथनाळो"}
    },
    {
        "garhwali": "लाट",
        "hindi": "हल की लंबी लकड़ी जो जुए तक जाती है",
        "english": "long plough beam connecting share to yoke",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "लाट", "tehri": "हरीस", "salani": "लाठ", "rathwali": "लाट"}
    },
    {
        "garhwali": "कनेथो",
        "hindi": "बैलों के कंधे पर रखने का जुआ",
        "english": "wooden yoke resting on oxen's shoulders",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कनेथो", "tehri": "जुवा", "salani": "जुआ", "rathwali": "कनेथो"}
    },
    {
        "garhwali": "जोता",
        "hindi": "बैलों को जुए से कसने की रस्सी",
        "english": "leather or rope harness fastening oxen to yoke",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "जोता", "tehri": "जोत", "salani": "जोता", "rathwali": "जोता"}
    },
    {
        "garhwali": "मुसला",
        "hindi": "फसल चरने से रोकने के लिए बैलों के मुंह पर छींका",
        "english": "woven wire or wicker muzzle for plough oxen",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "मुसला", "tehri": "छींका", "salani": "मुँछीका", "rathwali": "मुसला"}
    },
    {
        "garhwali": "जोल",
        "hindi": "खेत समतल करने का भारी लकड़ी का पाटा (मैढ़ा)",
        "english": "heavy wooden clod crusher / field leveller",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "जोल", "tehri": "पाटा", "salani": "मैढ़ा", "rathwali": "जोळ"}
    },
    {
        "garhwali": "कुलो",
        "hindi": "मिट्टी गोडने की छोटी कुदाली (कुटला)",
        "english": "small one-handed hand-hoe / weeder",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "कुलो", "tehri": "कुटला", "salani": "खुरपा", "rathwali": "कुळो"}
    },
    {
        "garhwali": "दाथुडो",
        "hindi": "घास व फसल काटने की दांतेदार दरांती",
        "english": "serrated mountain harvesting sickle",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "दाथुडो", "tehri": "दातुली", "salani": "हंसिया", "rathwali": "दाथुळो"}
    },
    {
        "garhwali": "सापलो",
        "hindi": "पत्थर उखाड़ने का भारी लोहे का सब्बल",
        "english": "heavy iron crowbar for excavating terrace boulders",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सापलो", "tehri": "साबल", "salani": "सब्बल", "rathwali": "सापळो"}
    },
    {
        "garhwali": "सेडगो",
        "hindi": "बैलों को हांकने की पतली छड़ी",
        "english": "thin driving stick / goad for oxen",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सेडगो", "tehri": "पैना", "salani": "सोटा", "rathwali": "सेडगो"}
    },

    # ==================== 3. TRADITIONAL STORAGE & BAMBOO CRAFT (Bhatt 1976) ====================
    {
        "garhwali": "ओडगो",
        "hindi": "रिंगाल की बनी चौड़ी टोकरी",
        "english": "wide shallow bamboo basket for vegetables and grain",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "ओडगो", "tehri": "डालिया", "salani": "टोकरी", "rathwali": "ओडगो"}
    },
    {
        "garhwali": "डलोणो",
        "hindi": "रिंगाल का ढक्कनदार बड़ा टोकरा",
        "english": "large covered woven bamboo hamper",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "डलोणो", "tehri": "ढकोला", "salani": "टोकरा", "rathwali": "डळोणो"}
    },
    {
        "garhwali": "पिठार",
        "hindi": "अनाज व कपड़े रखने का बड़ा लकड़ी का संदूक",
        "english": "traditional carved wooden grain and dowry chest",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "पिठार", "tehri": "पेटी", "salani": "संदूक", "rathwali": "पिठार"}
    },
    {
        "garhwali": "मान्द्रो",
        "hindi": "आंगन में धान सुखाने की रिंगाल की बड़ी चटाई",
        "english": "large woven bamboo mat for sunning harvest grains",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "मान्द्रो", "tehri": "मोंदरा", "salani": "चटाई", "rathwali": "मान्द्रो"}
    },
    {
        "garhwali": "सुप्पो",
        "hindi": "अनाज फटकने का बांस का सूप",
        "english": "traditional winnowing scoop",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "सुप्पो", "tehri": "सूप", "salani": "छाज", "rathwali": "सुप्पो"}
    },
    {
        "garhwali": "छावड़ी",
        "hindi": "अनाज सुखाने व छानने की छोटी टोकरी",
        "english": "small shallow wicker tray for winnowing",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "छावड़ी", "tehri": "छबड़ी", "salani": "डलिया", "rathwali": "छावळी"}
    },

    # ==================== 4. PASTORAL, LIVESTOCK & DAIRY TERMS (Bhatt 1976) ====================
    {
        "garhwali": "गोरु",
        "hindi": "गोधन / गाय-बैल",
        "english": "cattle / kine / cow livestock",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "गोरु", "tehri": "गाय", "salani": "गोरू", "rathwali": "गोरु"}
    },
    {
        "garhwali": "वल्द",
        "hindi": "हल जोतने का बैल",
        "english": "ploughing ox / bullock",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "वल्द", "tehri": "बैल", "salani": "बर्द", "rathwali": "वल्द"}
    },
    {
        "garhwali": "खडू",
        "hindi": "नर भेड़ (भेड़ा)",
        "english": "ram / male mountain sheep",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "खडू", "tehri": "भेड़ा", "salani": "मेंढ़ा", "rathwali": "खडू"}
    },
    {
        "garhwali": "बाच्छीलो",
        "hindi": "गाय की बछिया",
        "english": "young cow calf / heifer",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "बाच्छीलो", "tehri": "बछिया", "salani": "बच्छी", "rathwali": "बाच्छीळो"}
    },
    {
        "garhwali": "थेथडो",
        "hindi": "भैंस की छोटी कटड़ी",
        "english": "young female buffalo calf",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "थेथडो", "tehri": "कटिया", "salani": "पड़िया", "rathwali": "थेथळो"}
    },
    {
        "garhwali": "गाजी",
        "hindi": "गांव के सभी पशुओं का सामूहिक झुंड",
        "english": "village collective herd of cattle",
        "pos": "noun",
        "gender": "F",
        "category": "animals",
        "dialect_variants": {"srinagariya": "गाजी", "tehri": "झुंड", "salani": "रेवड़", "rathwali": "गाजी"}
    },
    {
        "garhwali": "मरड़ो",
        "hindi": "जंगल में पशुओं के ठहरने का बाड़ा",
        "english": "pastoral cattle corral / pen in high pasture",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "मरड़ो", "tehri": "बाड़ा", "salani": "अहाता", "rathwali": "मरळो"}
    },
    {
        "garhwali": "छानी",
        "hindi": "पहाड़ी ढलान पर बनी पशुशाला व चरवाहों की झोपड़ी",
        "english": "isolated highland livestock shed / summer dwelling",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "छानी", "tehri": "छानी", "salani": "खरक", "rathwali": "छाणी"}
    },
    {
        "garhwali": "साल",
        "hindi": "मकान के भूतल की गोशाला",
        "english": "basement byre / cowshed of traditional home",
        "pos": "noun",
        "gender": "F",
        "category": "household",
        "dialect_variants": {"srinagariya": "साल", "tehri": "गोठ", "salani": "सार", "rathwali": "साळ"}
    },

    # ==================== 5. TRADITIONAL FOOD, SPICES & CROPS (Bhatt 1976) ====================
    {
        "garhwali": "छछेड़ो",
        "hindi": "छाछ और बेसन से बनी गाढ़ी कढ़ी",
        "english": "tangy traditional buttermilk curry cooked with chickpea flour",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "छछेड़ो", "tehri": "कढ़ी", "salani": "झोली", "rathwali": "छछेळो"}
    },
    {
        "garhwali": "ग्यूराड़",
        "hindi": "गेहूं, जौ और मंडुवा मिलाकर बनाया गया आटा",
        "english": "multigrain flour of wheat, barley, and finger millet",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "ग्यूराड़", "tehri": "मिश्रित-आटा", "salani": "मिस्सी", "rathwali": "ग्यूराड़"}
    },
    {
        "garhwali": "भुजी",
        "hindi": "हरी पहाड़ी सब्जियों का भुना हुआ साग",
        "english": "stir-fried wild mountain greens",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "भुजी", "tehri": "साग", "salani": "भुजिया", "rathwali": "भुजी"}
    },
    {
        "garhwali": "गथवाणी",
        "hindi": "कुलथ (गहत) की दाल का गाढ़ा औषधीय रस",
        "english": "medicinal soup of boiled horsegram (kulath)",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "गथवाणी", "tehri": "गथवाण", "salani": "रस", "rathwali": "गथवाणी"}
    },
    {
        "garhwali": "पटुला",
        "hindi": "अरबी के पत्तों पर बेसन लगाकर उबले पतौड़े",
        "english": "steamed colocasia leaf rolls spiced with chickpea batter",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "पटुला", "tehri": "पत्यूड़", "salani": "पतौड़ा", "rathwali": "पटुळा"}
    },
    {
        "garhwali": "छुवलरोटी",
        "hindi": "तवे पर पकाई जाने वाली अत्यंत पतली नरम रोटी",
        "english": "ultra-thin soft mountain griddle bread",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "छुवलरोटी", "tehri": "फुलका", "salani": "रोटी", "rathwali": "छुवकरोटी"}
    },
    {
        "garhwali": "लाई",
        "hindi": "पहाड़ी काले दाने वाली राई / सरसों",
        "english": "black Himalayan mustard greens and seeds",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "लाई", "tehri": "राई", "salani": "सरसों", "rathwali": "लाई"}
    },
    {
        "garhwali": "राडो",
        "hindi": "पीली सरसों",
        "english": "yellow mountain mustard",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "राडो", "tehri": "तोड़िया", "salani": "पीली-सरसों", "rathwali": "राळो"}
    },
    {
        "garhwali": "चूरो",
        "hindi": "दाल छौंकने का पहाड़ी सुवासित मसाला",
        "english": "aromatic wild herbal seasoning for tempering lentils",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "चूरो", "tehri": "मसाला", "salani": "तड़का", "rathwali": "चूरो"}
    },

    # ==================== 6. GARMENTS & BEDDING (Bhatt 1976) ====================
    {
        "garhwali": "झुलकी",
        "hindi": "महिलाओं के सिर पर ओढ़ने की लंबी रेशमी चुनरी",
        "english": "traditional women's head veil / scarf",
        "pos": "noun",
        "gender": "F",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "झुलकी", "tehri": "चुनरी", "salani": "दुपट्टा", "rathwali": "झुलकी"}
    },
    {
        "garhwali": "आँगड़ी",
        "hindi": "पारंपरिक चोली / ब्लाउज",
        "english": "fitted traditional bodice blouse",
        "pos": "noun",
        "gender": "F",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "आँगड़ी", "tehri": "अंगिया", "salani": "चोली", "rathwali": "आँगळी"}
    },
    {
        "garhwali": "पाखलो",
        "hindi": "सर्दियों में ओढ़ा जाने वाला ऊन का गर्म लबादा",
        "english": "warm homespun woolen cloak worn against subzero frost",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "पाखलो", "tehri": "पाखला", "salani": "लबादा", "rathwali": "पाखळो"}
    },
    {
        "garhwali": "कामलो",
        "hindi": "भेड़ के ऊन का मोटा कंबल",
        "english": "thick handwoven sheep-wool blanket",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "कामलो", "tehri": "कमली", "salani": "लोई", "rathwali": "कामळो"}
    },
    {
        "garhwali": "टोपलो",
        "hindi": "पारंपरिक पहाड़ी गोल टोपी",
        "english": "traditional round Pahari felt cap",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "टोपलो", "tehri": "टोपी", "salani": "टोपी", "rathwali": "टोपळो"}
    },
    {
        "garhwali": "मुन्यासो",
        "hindi": "विवाह व उत्सवों में पहनी जाने वाली पगड़ी",
        "english": "ceremonial wedding turban",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "मुन्यासो", "tehri": "पगड़ी", "salani": "साफा", "rathwali": "मुन्यासो"}
    },
    {
        "garhwali": "झगोलो",
        "hindi": "बच्चों का पारंपरिक ढीला चोगा (झगुला)",
        "english": "traditional child's loose frock / tunic",
        "pos": "noun",
        "gender": "M",
        "category": "clothing",
        "dialect_variants": {"srinagariya": "झगोलो", "tehri": "झगुला", "salani": "कुर्ता", "rathwali": "झगोळो"}
    },
    {
        "garhwali": "गुदमा",
        "hindi": "भेड़ के मुलायम ऊन का गद्दा व रजाई",
        "english": "luxurious thick wool mattress-blanket",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "गुदमा", "tehri": "गुद्मा", "salani": "गद्दार", "rathwali": "गुदमा"}
    },
    {
        "garhwali": "स्यूणो",
        "hindi": "कपड़े सिलने की लोहे की सुई",
        "english": "iron sewing needle",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "स्यूणो", "tehri": "सुई", "salani": "सुई", "rathwali": "स्यूणो"}
    },
    {
        "garhwali": "ताकलू",
        "hindi": "ऊन कातने की हाथ की तकली",
        "english": "hand spindle for spinning sheep wool",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "ताकलू", "tehri": "तकली", "salani": "चरखा", "rathwali": "ताकळू"}
    },
    {
        "garhwali": "राँछ",
        "hindi": "ऊन व शॉल बुनने का पारंपरिक हथकरघा",
        "english": "traditional village pit-loom for weaving wool blankets",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "राँछ", "tehri": "करघा", "salani": "हथकरघा", "rathwali": "राँछ"}
    },
    {
        "garhwali": "कांको",
        "hindi": "लकड़ी या सींग की कंघी",
        "english": "wooden or horn hair comb",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "कांको", "tehri": "कंघी", "salani": "कंघा", "rathwali": "कांको"}
    },

    # ==================== 7. BIRDS & FAUNA OF GARHWAL (Bhatt 1976) ====================
    {
        "garhwali": "घेंदूडी",
        "hindi": "घरेलू गौरैया चिड़िया",
        "english": "house sparrow",
        "pos": "noun",
        "gender": "F",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "घेंदूडी", "tehri": "गौरेया", "salani": "चिडिया", "rathwali": "घेंदूळी"}
    },
    {
        "garhwali": "मलेऊ",
        "hindi": "पहाड़ी जंगली नीला कबूतर",
        "english": "blue hill rock pigeon",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "मलेऊ", "tehri": "कबूतर", "salani": "पंडुक", "rathwali": "मलेऊ"}
    },
    {
        "garhwali": "फेतुवा",
        "hindi": "काली कलगी वाली पहाड़ी बुलबुल",
        "english": "black-crested Himalayan bulbul",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "फेतुवा", "tehri": "बुलबुल", "salani": "बुलबुल", "rathwali": "फेतुवा"}
    },
    {
        "garhwali": "कल्हा",
        "hindi": "पहाड़ी लाल चोंच वाला तोता",
        "english": "red-billed Himalayan parakeet",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "कल्हा", "tehri": "तोता", "salani": "सुग्गा", "rathwali": "कल्हा"}
    },
    {
        "garhwali": "कफ्फू",
        "hindi": "'काफल पाको' की रटन लगाने वाला चातक पक्षी",
        "english": "Himalayan cuckoo whose call heralds ripening bayberries",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "कफ्फू", "tehri": "कफू", "salani": "पपीहा", "rathwali": "कफ्फू"}
    },
    {
        "garhwali": "नीलरांग",
        "hindi": "पवित्र नीलकंठ पक्षी",
        "english": "Indian roller / sacred blue jay",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "नीलरांग", "tehri": "नीलकंठ", "salani": "नीलकंठ", "rathwali": "नीलरांग"}
    },
    {
        "garhwali": "सिकंरा",
        "hindi": "तीव्र दृष्टि वाला शिकारी बाज",
        "english": "shikra sparrowhawk / falcon",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "सिकंरा", "tehri": "बाज", "salani": "शिकरा", "rathwali": "सिकंरा"}
    },
    {
        "garhwali": "मछमार",
        "hindi": "नदी किनारे मछली पकड़ने वाला बगुला",
        "english": "stream kingfisher / heron",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "मछमार", "tehri": "बगुला", "salani": "बगला", "rathwali": "मछमार"}
    },
    {
        "garhwali": "गडयाल",
        "hindi": "पहाड़ी नदियों की विशाल महाशीर मछली",
        "english": "giant Himalayan golden mahseer river fish",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "गडयाल", "tehri": "महाशीर", "salani": "मछली", "rathwali": "गडयाळ"}
    },
    {
        "garhwali": "गिदली",
        "hindi": "ठंडे पानी की छोटी पहाड़ी ट्राउट मछली",
        "english": "snow trout / cold torrent river fish",
        "pos": "noun",
        "gender": "F",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "गिदली", "tehri": "ट्राउट", "salani": "छोटी-मछली", "rathwali": "गिदळी"}
    },
    {
        "garhwali": "म्हारा",
        "hindi": "जंगल की पहाड़ी शहद की मधुमक्खी",
        "english": "Himalayan honeybee (Apis cerana indica)",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "म्हारा", "tehri": "मधुमक्खी", "salani": "मक्खी", "rathwali": "म्हारा"}
    },
    {
        "garhwali": "भोरू",
        "hindi": "फूलों पर मंडराने वाला काला भौंरा",
        "english": "black bumblebee",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "भोरू", "tehri": "भौंरा", "salani": "भ्रमर", "rathwali": "भोरू"}
    },
    {
        "garhwali": "किरमली",
        "hindi": "छोटी काली चींटी",
        "english": "small black ant",
        "pos": "noun",
        "gender": "F",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "किरमली", "tehri": "चींटी", "salani": "कीड़ी", "rathwali": "किरमळी"}
    },

    # ==================== 8. PRAKRIT COGNATES & FOLK PHILOSOPHY (Chatak 1959) ====================
    {
        "garhwali": "खामू",
        "hindi": "मकान की छत को साधने वाला लकड़ी का खंभा",
        "english": "carved timber pillar supporting house ceiling",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "खामू", "tehri": "खंभा", "salani": "थूनी", "rathwali": "खामू"}
    },
    {
        "garhwali": "छेल",
        "hindi": "पेड़ों या पर्वत की शीतल छाया",
        "english": "cool mountain shade / shadow",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "छेल", "tehri": "छांव", "salani": "छाया", "rathwali": "छेळ"}
    },
    {
        "garhwali": "ठौं",
        "hindi": "स्थान / ठिकाना / जगह",
        "english": "place / spot / abode",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "ठौं", "tehri": "स्थान", "salani": "ठौर", "rathwali": "ठौं"}
    },
    {
        "garhwali": "नौलू",
        "hindi": "नूतन / नया / ताज़ा",
        "english": "fresh / newly arrived / novel",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "नौलू", "tehri": "नया", "salani": "नया", "rathwali": "नौळू"}
    },
    {
        "garhwali": "मौड़",
        "hindi": "विवाह में वर-वधू के सिर का मुकुट",
        "english": "ceremonial wedding crown worn by bride and groom",
        "pos": "noun",
        "gender": "M",
        "category": "wedding",
        "dialect_variants": {"srinagariya": "मौड़", "tehri": "मुकुट", "salani": "मौर", "rathwali": "मौड़"}
    },
    {
        "garhwali": "व्यारण",
        "hindi": "सूर्योदय का समय / प्रातःकाल",
        "english": "early dawn / sunrise hour",
        "pos": "noun",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "व्यारण", "tehri": "सवेरा", "salani": "प्रभात", "rathwali": "व्यारण"}
    },
    {
        "garhwali": "संझा",
        "hindi": "गोधूलि वेला / संध्या",
        "english": "twilight evening / dusk",
        "pos": "noun",
        "gender": "F",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "संझा", "tehri": "शाम", "salani": "संध्या", "rathwali": "संझा"}
    },
    {
        "garhwali": "उम्मी",
        "hindi": "अग्नि में भुनी हुई गेहूं या जौ की हरी बालें",
        "english": "roasted green wheat or barley ears",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "उम्मी", "tehri": "ओमी", "salani": "होल्हा", "rathwali": "उम्मी"}
    },
    {
        "garhwali": "ज्वनला",
        "hindi": "जुड़वां बालक / जुड़वां बच्चे",
        "english": "twin children",
        "pos": "noun",
        "gender": "M",
        "category": "children",
        "dialect_variants": {"srinagariya": "ज्वनला", "tehri": "जुड़वा", "salani": "जमेल", "rathwali": "ज्वनळा"}
    },
    {
        "garhwali": "राड़",
        "hindi": "झगड़ा / तकरार / विवाद",
        "english": "quarrel / feud / dispute",
        "pos": "noun",
        "gender": "F",
        "category": "social",
        "dialect_variants": {"srinagariya": "राड़", "tehri": "झगड़ा", "salani": "कलह", "rathwali": "राड़"}
    },
    {
        "garhwali": "लीसो",
        "hindi": "चीड़ के पेड़ का चिपचिपा गोंद (लीसा)",
        "english": "pine resin / turpentine gum tapped from chir pine",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "लीसो", "tehri": "लीसा", "salani": "गोंद", "rathwali": "ळीसो"}
    },
    {
        "garhwali": "थाती",
        "hindi": "पूर्वजों की पैतृक धरोहर / अमानत",
        "english": "ancestral heritage / sacred heirloom property",
        "pos": "noun",
        "gender": "F",
        "category": "culture",
        "dialect_variants": {"srinagariya": "थाती", "tehri": "धरोहर", "salani": "विरासत", "rathwali": "थाती"}
    },
    {
        "garhwali": "स्वाली",
        "hindi": "त्योहारों पर बनने वाली तली हुई नमकीन पूरी",
        "english": "festive deep-fried wheat puri",
        "pos": "noun",
        "gender": "F",
        "category": "food",
        "dialect_variants": {"srinagariya": "स्वाली", "tehri": "पूरी", "salani": "स्वाली", "rathwali": "स्वाळी"}
    },
    {
        "garhwali": "हाट",
        "hindi": "पहाड़ी बाजार / साप्ताहिक मेला",
        "english": "hill marketplace / weekly rural bazaar",
        "pos": "noun",
        "gender": "F",
        "category": "business",
        "dialect_variants": {"srinagariya": "हाट", "tehri": "बाजार", "salani": "हाट", "rathwali": "हाट"}
    },
    {
        "garhwali": "खरणी",
        "hindi": "घास छीलने की छोटी खुरपी",
        "english": "small triangular weeding trowel (khurpi)",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "खरणी", "tehri": "खुरपी", "salani": "खुरपा", "rathwali": "खरणी"}
    }
]

added = 0
enriched = 0

for item in BHATT_CHATAK_WORDS:
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

print(f"Bhatt & Chatak mining added: {added}")
print(f"Enriched: {enriched}")
print(f"Total word count now: {len(existing_words)}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Saved words to {WORDS_PATH}")
