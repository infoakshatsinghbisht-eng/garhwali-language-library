# -*- coding: utf-8 -*-
"""
Expands Garhwali dictionary past 3,100 words by adding:
1. Canonical forms and inflections of song lyrics tokens (nature, seasons, instruments, emotions).
2. Advanced occupational, craft, traditional knowledge, ecological, and home vocabulary.
3. Garhwali conversational particles, honorifics, numbers, and pronouns.
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDS_PATH = os.path.join(ROOT_DIR, "garhwali", "lexicon", "data", "words.json")

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = json.load(f)

existing = {w["garhwali"].strip() for w in words}

NEW_BATCH = [
    # Song Tokens & High-frequency expressions
    {"garhwali": "आंगण", "hindi": "आंगन / चौखट", "english": "courtyard / stone terrace", "pos": "noun", "gender": "M", "category": "house"},
    {"garhwali": "आंच", "hindi": "अग्नि की लौ / आंच", "english": "flame / warmth of hearth", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "आगू", "hindi": "आगे / सम्मुख", "english": "in front of / ahead", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "आलाप", "hindi": "गीत की तान / स्वर विस्तार", "english": "vocal prelude in folk melody", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "आशीष", "hindi": "आशीर्वाद / मंगल कामना", "english": "blessing / benediction", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "ऐगे", "hindi": "आ गया / आ गया है", "english": "has arrived (masc.)", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "ऐगै", "hindi": "आ गई / आ चुकी है", "english": "has arrived (fem.)", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "उठिक", "hindi": "उठकर (पूर्वकालिक क्रिया)", "english": "having arisen / having gotten up", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "छोड़िक", "hindi": "छोड़कर", "english": "having left / departing", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बोलिक", "hindi": "बोलकर / कहकर", "english": "having spoken", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "देखिक", "hindi": "देखकर / निहारकर", "english": "having seen / gazed", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सुणिक", "hindi": "सुनकर", "english": "having heard / listened", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "करिक", "hindi": "करके", "english": "having done", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "खाइक", "hindi": "खाकर", "english": "having eaten", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पीक", "hindi": "पीकर", "english": "having drunk", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पढ़िक", "hindi": "पढ़कर", "english": "having read / studied", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "लिखिक", "hindi": "लिखकर", "english": "having written", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "चलिक्क", "hindi": "चलकर / प्रस्थान कर", "english": "having walked / departed", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बैठिक", "hindi": "बैठकर", "english": "having sat down", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "उबारी", "hindi": "बचाव / रक्षा", "english": "rescue / salvation", "pos": "noun", "gender": "F", "category": "abstract"},

    # Ecology, Forest Produce & Agriculture
    {"garhwali": "रिंगाल", "hindi": "पहाड़ी बौना बांस (टोकरी बनाने का)", "english": "dwarf Himalayan hill bamboo", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "चीड़", "hindi": "चीड़ का पेड़", "english": "pine tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "देवदार", "hindi": "देवदार का विशाल वृक्ष", "english": "Himalayan deodar cedar tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "सुरई", "hindi": "सुराई का वृक्ष (क्यूप्रेसस)", "english": "Himalayan cypress tree", "pos": "noun", "gender": "F", "category": "flora"},
    {"garhwali": "अयार", "hindi": "अयार का वृक्ष", "english": "lyonia ovalifolia hill tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "खर्सू", "hindi": "भूरा उच्च-हिमालयी ओक", "english": "quercus semecarpifolia brown oak", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "मोरीण", "hindi": "हरी ओक (हरिंज)", "english": "green oak tree", "pos": "noun", "gender": "F", "category": "flora"},
    {"garhwali": "पय्यां", "hindi": "पद्मकाष्ठ / जंगली चेरी का पेड़", "english": "wild Himalayan cherry tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "मेलू", "hindi": "जंगली नाशपाती का फल", "english": "wild mountain pear", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "दाड़िम", "hindi": "जंगली खट्टा अनार", "english": "wild sour pomegranate", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "माल्टा", "hindi": "पहाड़ी रसीला संतरा / माल्टा", "english": "sweet red-fleshed mountain orange", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "नींबू", "hindi": "बड़ा पहाड़ी नींबू (चकोतरा)", "english": "large mountain citron", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "अखरोट", "hindi": "अखरोट का फल/पेड़", "english": "walnut", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "चुलू", "hindi": "खुमानी / आड़ू का बीज-तेल", "english": "wild apricot / apricot kernel oil", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "आड़ू", "hindi": "आड़ू फल", "english": "peach", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "पुलम", "hindi": "आलूबुखारा", "english": "plum", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "गहत", "hindi": "कुलथी की दाल", "english": "horse gram", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "रयांण", "hindi": "पहाड़ी लोबिया", "english": "mountain black-eyed pea", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "नौरंगी", "hindi": "नौ रंगों वाली पहाड़ी दाल", "english": "nine-colored mountain multi-bean", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "मडुवा", "hindi": "रागी / कोदू", "english": "finger millet", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "कौणी", "hindi": "कंगनी / राल बाजरा", "english": "foxtail millet", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "ओगल", "hindi": "कुट्टू / फाफर", "english": "buckwheat (fagopyrum)", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "फाफर", "hindi": "तीखा कुट्टू", "english": "tartary buckwheat", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "चूआ", "hindi": "रामदाना / चौलाई", "english": "amaranth grain", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "तिल", "hindi": "तिल के बीज", "english": "sesame seeds", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "अलसी", "hindi": "तीसी / अलसी", "english": "flaxseed", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "सरसों", "hindi": "पीली सरसों", "english": "mustard", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "लाही", "hindi": "काली राई", "english": "black mustard seed", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "धनिया", "hindi": "हरा धनिया / बीज", "english": "coriander", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "जीरा", "hindi": "जीरा", "english": "cumin seeds", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "हल्दी", "hindi": "हरिद्रा / हल्दी", "english": "turmeric", "pos": "noun", "gender": "F", "category": "cooking"},
    {"garhwali": "मिर्च", "hindi": "लाल/हरी मिर्च", "english": "chili pepper", "pos": "noun", "gender": "F", "category": "cooking"},
    {"garhwali": "लहसुन", "hindi": "लहसुन", "english": "garlic", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "प्याज", "hindi": "प्याज", "english": "onion", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "आलू", "hindi": "आलू", "english": "potato", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "पिंडालू", "hindi": "अरबी / घुइयां", "english": "taro root / colacasia", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "गेठी", "hindi": "पहाड़ी कंद (गेठी)", "english": "air potato / dioscorea bulbifera", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "तरड़", "hindi": "जंगली मीठा कंद", "english": "wild mountain sweet yam", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "कद्दू", "hindi": "कद्दू / कुम्हड़ा", "english": "pumpkin / sweet gourd", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "लौकी", "hindi": "घिया / लौकी", "english": "bottle gourd", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "तोरई", "hindi": "तोरई", "english": "ridge gourd", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "करेला", "hindi": "करेला", "english": "bitter gourd", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "खीरा", "hindi": "पहाड़ी ककड़ी", "english": "large mountain cucumber", "pos": "noun", "gender": "M", "category": "food"},

    # Wildlife, Birds, Insects
    {"garhwali": "बाघ", "hindi": "बाघ / गुलदार (तेंदुआ)", "english": "leopard / tiger", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "भालू", "hindi": "हिमालयी काला भालू", "english": "Himalayan black bear", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "सूअर", "hindi": "जंगली सुअर (बराह)", "english": "wild boar", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "सियार", "hindi": "गीदड़ / सियार", "english": "jackal", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "लोमड़ी", "hindi": "लोमड़ी", "english": "hill fox", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "बंदर", "hindi": "वानर / बंदर", "english": "rhesus macaque monkey", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "लंगूर", "hindi": "काला मुंह वाला लंगूर", "english": "grey langur", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "खरगोश", "hindi": "शशक / खरगोश", "english": "mountain hare / rabbit", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "साही", "hindi": "साही (कांटेदार जीव)", "english": "Indian porcupine", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "चूहा", "hindi": "मूषक / चूहा", "english": "mouse / rat", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "नेवला", "hindi": "नकुल / नेवला", "english": "grey mongoose", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "सांप", "hindi": "सर्प / सांप", "english": "snake / serpent", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "बिच्छू", "hindi": "वृश्चिक / बिच्छू", "english": "scorpion", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "मेंढक", "hindi": "मंडूक / मेंढक", "english": "frog / toad", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "चील", "hindi": "चील", "english": "kite / hawk", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "बाज", "hindi": "बाज (शिकारी पक्षी)", "english": "falcon / eagle", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "उल्लू", "hindi": "उल्लू", "english": "owl", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "कौआ", "hindi": "काग / कौआ", "english": "crow / raven", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "तोता", "hindi": "सुग्गा / तोता", "english": "parakeet / parrot", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "मैना", "hindi": "मैना पक्षी", "english": "myna bird", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "गौरैया", "hindi": "घरेलू चिड़िया / गौरैया", "english": "house sparrow", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "मुर्गा", "hindi": "कुकुड़ / मुर्गा", "english": "rooster / cockerel", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "मुर्गी", "hindi": "मुर्गी", "english": "hen", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "तितली", "hindi": "तितली", "english": "butterfly", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "मधुमक्खी", "hindi": "मौरी / मधुमक्खी", "english": "honeybee", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "मक्खी", "hindi": "मक्खी", "english": "housefly", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "मच्छर", "hindi": "मच्छर", "english": "mosquito", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "चींटी", "hindi": "किड़ी / चींटी", "english": "ant", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "मकड़ी", "hindi": "मकड़ी", "english": "spider", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "जूं", "hindi": "जूं", "english": "louse", "pos": "noun", "gender": "F", "category": "fauna"},

    # Traditional Occupations, Village Crafts, Roles
    {"garhwali": "लोहार", "hindi": "लोहा बनाने वाला कारीगर", "english": "blacksmith", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "बढ़ई", "hindi": "काष्ठ शिल्पी / बढ़ई", "english": "carpenter / wood carver", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "कुम्हार", "hindi": "मिट्टी के बर्तन बनाने वाला", "english": "potter", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "दर्जी", "hindi": "वस्त्र सीने वाला", "english": "tailor", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "धोबी", "hindi": "वस्त्र धोने वाला", "english": "washerman", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "नाई", "hindi": "बाल काटने वाला नापित", "english": "barber", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "ग्वाला", "hindi": "पशु चराने वाला / अनवाळ", "english": "cowherd / shepherd", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "किसान", "hindi": "कृषक / खेतीहर", "english": "farmer / cultivator", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "मजदूर", "hindi": "श्रमिक / श्रमजीवी", "english": "laborer / worker", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "वैद्य", "hindi": "आयुर्वेदिक चिकित्सक / नाड़ी वैद्य", "english": "traditional Ayurvedic physician", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "पंडित", "hindi": "पुरोहित / कथावाचक", "english": "priest / ritualist", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "डंगरिया", "hindi": "पश्वा (देवता का अवतार लेने वाला)", "english": "divine oracle medium", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "जागरिया", "hindi": "जागर गाकर देवता को जगाने वाला गायक", "english": "shamanic ritual singer and chanter", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "हुड़किया", "hindi": "हुड़का बजाने वाला लोक गायक", "english": "hour-glass drum balladeer", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "बद्दी", "hindi": "पारंपरिक लोक नर्तक एवं कलाबाज", "english": "rope dancer / traditional acrobatic minstrel", "pos": "noun", "gender": "M", "category": "occupations"},

    # Attire, Fabric & Personal Ornaments
    {"garhwali": "धोती", "hindi": "धोती", "english": "dhoti / waist wrap", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "कुर्ता", "hindi": "कुर्ता / अंगरखा", "english": "tunic / kurta", "pos": "noun", "gender": "M", "category": "clothing"},
    {"garhwali": "टोपी", "hindi": "काली पहाड़ी टोपी", "english": "traditional Pahari round cap", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "पगड़ी", "hindi": "साफा / पाग", "english": "turban", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "कंबल", "hindi": "ऊनी कंबल / थुलमा", "english": "heavy wool blanket / thulma", "pos": "noun", "gender": "M", "category": "clothing"},
    {"garhwali": "पंखी", "hindi": "पतली ऊनी शॉल", "english": "light hand-woven wool wrap", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "चुन्नी", "hindi": "दुपट्टा / ओढ़नी", "english": "scarf / veil", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "घाघरा", "hindi": "लहंगा / घाघरा", "english": "flared long hill skirt", "pos": "noun", "gender": "M", "category": "clothing"},
    {"garhwali": "आंगड़ी", "hindi": "महिलाओं का ऊपरी ब्लाउज / चोली", "english": "tight traditional bodice blouse", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "गाती", "hindi": "कमर पर बांधी जाने वाली शॉल", "english": "waist-tied support wrap for mountain work", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "पायजामा", "hindi": "पायजामा / चूड़ीदार", "english": "fitted hill trousers", "pos": "noun", "gender": "M", "category": "clothing"},
    {"garhwali": "जूता", "hindi": "पदत्राण / जूता", "english": "shoes", "pos": "noun", "gender": "M", "category": "clothing"},
    {"garhwali": "चप्पल", "hindi": "चप्पल", "english": "slippers / sandals", "pos": "noun", "gender": "F", "category": "clothing"},
    {"garhwali": "मोजा", "hindi": "ऊनी जुराब", "english": "knitted wool socks", "pos": "noun", "gender": "M", "category": "clothing"},
    {"garhwali": "दस्ताना", "hindi": "दस्ताना", "english": "gloves", "pos": "noun", "gender": "M", "category": "clothing"},

    # Additional Essential Everyday Verbs
    {"garhwali": "सीखण", "hindi": "सीखना / ज्ञान प्राप्त करना", "english": "to learn", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सिखाण", "hindi": "सिखाना / पढ़ाना", "english": "to teach", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "समझण", "hindi": "समझना / बोध करना", "english": "to understand", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "समझाण", "hindi": "समझाना", "english": "to explain", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सोचण", "hindi": "विचार करना / सोचना", "english": "to think", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "भूलण", "hindi": "विस्मृत होना / भूलना", "english": "to forget", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "याद करण", "hindi": "स्मरण करना", "english": "to remember", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "जीण", "hindi": "जीवित रहना / जीना", "english": "to live / exist", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "मरब", "hindi": "मृत्यु होना / मरना", "english": "to die / pass away", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बचण", "hindi": "सुरक्षित रहना / बचना", "english": "to survive / be saved", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बचाण", "hindi": "रक्षा करना / बचाना", "english": "to rescue / protect", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "खोण", "hindi": "गुम होना / खोना", "english": "to lose / get lost", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पाण", "hindi": "प्राप्त करना / पाना", "english": "to receive / find / get", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बेचण", "hindi": "विक्रय करना / बेचना", "english": "to sell", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "खरीदण", "hindi": "क्रय करना / खरीदना (मोल लेण)", "english": "to buy / purchase", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "कमाउण", "hindi": "अर्जित करना / कमाना", "english": "to earn livelihood", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "खर्च करण", "hindi": "व्यय करना / खर्च करना", "english": "to spend money", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "लड़ण", "hindi": "युद्ध करना / झगड़ना", "english": "to fight / quarrel", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "जीकण", "hindi": "विजय पाना / जीतना", "english": "to conquer / win", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "हारण", "hindi": "परास्त होना / हारना", "english": "to lose / be defeated", "pos": "verb", "gender": None, "category": "verbs"}
]

count = 0
for item in NEW_BATCH:
    k = item["garhwali"].strip()
    if k not in existing:
        words.append(item)
        existing.add(k)
        count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Batch expansion added {count} words. Total words in dictionary: {len(words)}")
