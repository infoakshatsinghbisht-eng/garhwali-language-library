# -*- coding: utf-8 -*-
"""
Mines and enriches comprehensive vocabulary from the 45-song Garhwali corpus
into garhwali/lexicon/data/words.json, expanding word base well past 3,000 words.
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

SONG_LEXICON_EXPANSION = [
    # Verbs and participial forms
    {"garhwali": "बासदू", "hindi": "चहकता है / बोलता है (पक्षी)", "english": "chirps / calls (bird)", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "बासदी", "hindi": "चहकती है / बोलती है (पक्षी)", "english": "chirps / calls (fem.)", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "बासी", "hindi": "बोला / चहका", "english": "chirped / cried", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "फूली", "hindi": "खिली (फूल)", "english": "bloomed / blossomed", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "फूलिगे", "hindi": "खिल गया / खिल चुकी", "english": "blossomed completely", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पाको", "hindi": "पका / परिपक्व हुआ", "english": "ripened / matured", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "पाकी", "hindi": "पकी (स्त्रीलिंग)", "english": "ripened (fem.)", "pos": "adjective", "gender": "F", "category": "descriptors"},
    {"garhwali": "घूम्दू", "hindi": "घूमता है", "english": "wanders / roams", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "घूम्दी", "hindi": "घूमती है", "english": "wanders (fem.)", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "ध्यांदू", "hindi": "ध्यान करता है / याद करता है", "english": "meditates upon / remembers", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "हरषाई", "hindi": "प्रसन्न हुआ / हर्षित हुआ", "english": "gladdened / rejoiced", "pos": "verb", "gender": None, "category": "emotions"},
    {"garhwali": "हरखायो", "hindi": "खुश हुआ / उल्लसित हुआ", "english": "delighted / rejoiced", "pos": "verb", "gender": "M", "category": "emotions"},
    {"garhwali": "ललकार्यो", "hindi": "ललकारा / चुनौती दी", "english": "challenged / roared defiance", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "गर्ज्यो", "hindi": "गरजा / दहाड़ा", "english": "roared like a lion / thundered", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "दौड्यो", "hindi": "दौड़ा / तेजी से भागा", "english": "ran / charged forward", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "रोप्यो", "hindi": "रोपा / गाड़ा / स्थापित किया", "english": "planted / hoisted firmly", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "राख्यो", "hindi": "रखा / मान रखा", "english": "kept / preserved honor", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "सजायो", "hindi": "सजाया / सुशोभित किया", "english": "adorned / decorated", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "सजी", "hindi": "सजी / संवरी", "english": "adorned (fem.)", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "सजी गै", "hindi": "सज गई / तैयार हो गई", "english": "became fully adorned", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "छोड़ी", "hindi": "छोड़ी / त्यागी", "english": "left behind / departed from", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "छूटि गै", "hindi": "छूट गई", "english": "parted from / left behind", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "रोवै", "hindi": "रोती है / रोता है", "english": "weeps / sheds tears", "pos": "verb", "gender": None, "category": "emotions"},
    {"garhwali": "चरदी", "hindi": "चरती है (पशु)", "english": "grazes (fem.)", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "चरदा", "hindi": "चरते हैं (पशु)", "english": "graze (pl.)", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "चढ़े", "hindi": "सवार हुआ / चढ़ा", "english": "mounted / climbed upon", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "डारै", "hindi": "डालते हैं / छिड़कते हैं", "english": "scatter / shower (rice/petals)", "pos": "verb", "gender": None, "category": "rituals"},
    {"garhwali": "उतारै", "hindi": "उतारते हैं (आरती)", "english": "perform (aarti waving)", "pos": "verb", "gender": None, "category": "rituals"},
    {"garhwali": "झुलदी", "hindi": "झूलती है", "english": "swings gently", "pos": "verb", "gender": "F", "category": "verbs"},
    {"garhwali": "कांपे", "hindi": "कांपता है / भयभीत होता है", "english": "trembles / shivers", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "जोती", "hindi": "जोता गया (हल)", "english": "ploughed", "pos": "verb", "gender": "F", "category": "agriculture"},
    {"garhwali": "लहराली", "hindi": "लहराएगी (फसल)", "english": "will wave in breeze (crops)", "pos": "verb", "gender": "F", "category": "agriculture"},
    {"garhwali": "हँसणी", "hindi": "हँसती हुई", "english": "smiling / laughing", "pos": "verb", "gender": "F", "category": "emotions"},
    {"garhwali": "गांदा", "hindi": "गाते हैं", "english": "sing (plural)", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "ल्यांदा", "hindi": "लाते हैं", "english": "bring (plural)", "pos": "verb", "gender": "M", "category": "verbs"},
    {"garhwali": "बचावा", "hindi": "बचाइए / रक्षा कीजिए", "english": "save / protect (imperative)", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बजावा", "hindi": "बजाइए (वाद्य)", "english": "play / sound (instrument)", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "मिलावा", "hindi": "मिलाइए / जोड़िए", "english": "join / unite (hands)", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "भुलावा", "hindi": "भुला दीजिए", "english": "forget / forgive", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सिखै", "hindi": "सिखाया", "english": "taught / instructed", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बिराजा", "hindi": "विराजमान होइए", "english": "be seated / bless us with presence", "pos": "verb", "gender": None, "category": "religion"},
    {"garhwali": "अवतारा", "hindi": "अवतरित होइए", "english": "manifest / descend into medium", "pos": "verb", "gender": None, "category": "religion"},

    # Nouns and Cultural Entities
    {"garhwali": "हिया", "hindi": "हृदय / मन / छाती", "english": "heart / soul / bosom", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "मुंड", "hindi": "सिर / मस्तक", "english": "head / forehead", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "सिरी", "hindi": "सिर / शीश (सम्मानसूचक)", "english": "sacred head / crown", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "आँखी", "hindi": "आँख / नेत्र", "english": "eyes", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "कान", "hindi": "कान / कर्ण", "english": "ear", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "नाक", "hindi": "नाक / नासिका", "english": "nose", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "दाँत", "hindi": "दांत", "english": "teeth", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "जीभ", "hindi": "जीभ / रसना", "english": "tongue", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "हाथ", "hindi": "हाथ / कर", "english": "hand", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "गोड़", "hindi": "पैर / पांव", "english": "foot / leg", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "कमर", "hindi": "कमर / कटि", "english": "waist", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "छाती", "hindi": "वक्षस्थल / छाती", "english": "chest / breast", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "कंठ", "hindi": "गला / कंठ", "english": "throat / neck", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "बांह", "hindi": "भुजा / बांह", "english": "arm", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "अंगूठा", "hindi": "अंगूठा", "english": "thumb", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "अंगुली", "hindi": "उंगली", "english": "finger", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "बाल", "hindi": "केश / बाल", "english": "hair", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "गाल", "hindi": "कपोल / गाल", "english": "cheek", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "होठ", "hindi": "ओष्ठ / होंठ", "english": "lips", "pos": "noun", "gender": "M", "category": "body"},

    # Family and Social Life
    {"garhwali": "बुबा", "hindi": "पिताजी / पिता", "english": "father", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "दाजी", "hindi": "बड़ा भाई / दाज्यू", "english": "elder brother", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "दीदी", "hindi": "बड़ी बहन", "english": "elder sister", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "बौजी", "hindi": "भाभी (बड़े भाई की पत्नी)", "english": "sister-in-law (elder brother's wife)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "काका", "hindi": "चाचा", "english": "paternal uncle (younger)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "काकी", "hindi": "चाची", "english": "paternal aunt", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "बड़ा बापू", "hindi": "ताऊ (पिता के बड़े भाई)", "english": "paternal senior uncle", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "बड़ी ब्वै", "hindi": "ताई (ताऊ की पत्नी)", "english": "senior aunt", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "मामा", "hindi": "मामा (माता के भाई)", "english": "maternal uncle", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "मामी", "hindi": "मामी", "english": "maternal aunt", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "फूफा", "hindi": "फूफा (बुआ के पति)", "english": "uncle (aunt's husband)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "फूफू", "hindi": "बुआ (पिता की बहन)", "english": "paternal aunt (father's sister)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "मौसा", "hindi": "मौसा", "english": "maternal aunt's husband", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "मौसी", "hindi": "मौसी (माता की बहन)", "english": "mother's sister / maternal aunt", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "ननद", "hindi": "ननद (पति की बहन)", "english": "sister-in-law (husband's sister)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "देवर", "hindi": "देवर (पति का छोटा भाई)", "english": "brother-in-law (husband's younger brother)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "जेठ", "hindi": "जेठ (पति का बड़ा भाई)", "english": "husband's elder brother", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "जेठानी", "hindi": "जेठानी (जेठ की पत्नी)", "english": "co-sister-in-law (elder)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "देवरानी", "hindi": "देवरानी (देवर की पत्नी)", "english": "co-sister-in-law (younger)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "सास", "hindi": "सासू माँ", "english": "mother-in-law", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "ससुर", "hindi": "ससुर जी", "english": "father-in-law", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "दामाद", "hindi": "ज्वाईं / दामाद", "english": "son-in-law", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "बहू", "hindi": "ब्वारी / बहू", "english": "daughter-in-law", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "भतीजा", "hindi": "भतीजा", "english": "nephew (brother's son)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "भतीजी", "hindi": "भतीजी", "english": "niece (brother's daughter)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "भांजा", "hindi": "भांजा (बहन का पुत्र)", "english": "nephew (sister's son)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "भांजी", "hindi": "भांजी (बहन की पुत्री)", "english": "niece (sister's daughter)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "पोता", "hindi": "नाती / पोता", "english": "grandson (son's son)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "पोती", "hindi": "नातिन / पोती", "english": "granddaughter (son's daughter)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "मैत", "hindi": "मायका / पीहर", "english": "maternal family home of married daughter", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "ससुराल", "hindi": "ससुराल", "english": "in-laws' home", "pos": "noun", "gender": "M", "category": "kinship"},

    # Village, Tools, Household Items
    {"garhwali": "थाल", "hindi": "थाली (भोजन परोसने की)", "english": "large brass dinner plate", "pos": "noun", "gender": "M", "category": "crockery"},
    {"garhwali": "कटोरी", "hindi": "कटोरी / प्याली", "english": "bowl / katori", "pos": "noun", "gender": "F", "category": "crockery"},
    {"garhwali": "लोटा", "hindi": "तांबे-पीतल का लोटा", "english": "water pot / spouted metal pot", "pos": "noun", "gender": "M", "category": "crockery"},
    {"garhwali": "गिलास", "hindi": "गिलास", "english": "glass / tumbler", "pos": "noun", "gender": "M", "category": "crockery"},
    {"garhwali": "चमच", "hindi": "चम्मच", "english": "spoon", "pos": "noun", "gender": "F", "category": "crockery"},
    {"garhwali": "कड़ाही", "hindi": "लोहे की कड़ाही", "english": "iron wok / cauldron", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "तवा", "hindi": "रोटी सेकने का तवा", "english": "flat griddle for flatbread", "pos": "noun", "gender": "M", "category": "kitchen"},
    {"garhwali": "पतीली", "hindi": "पतीला / देगची", "english": "cooking pot", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "परौत", "hindi": "आटा गूंथने की परात", "english": "large wide brass kneading platter", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "सिलबट्टा", "hindi": "मसाला पीसने का पत्थर एवं लोढ़ा", "english": "flat granite grinding stone and muller", "pos": "noun", "gender": "M", "category": "kitchen"},
    {"garhwali": "चिमटा", "hindi": "चिमटा (अंगारों का)", "english": "iron hearth tongs", "pos": "noun", "gender": "M", "category": "kitchen"},
    {"garhwali": "फुंकणी", "hindi": "चूल्हे में आग फूंकने की नली", "english": "iron hollow blowpipe for reviving wood flames", "pos": "noun", "gender": "F", "category": "kitchen"},
    {"garhwali": "चूल्हा", "hindi": "मिट्टी-पत्थर का पारंपरिक चूल्हा", "english": "traditional stone masonry wood hearth", "pos": "noun", "gender": "M", "category": "kitchen"},
    {"garhwali": "दीया", "hindi": "मिट्टी का दीपक / दीवा", "english": "earthen clay oil lamp", "pos": "noun", "gender": "M", "category": "household"},
    {"garhwali": "लालटेन", "hindi": "लालटेन", "english": "kerosene lantern", "pos": "noun", "gender": "F", "category": "household"},
    {"garhwali": "मोमबत्ती", "hindi": "मोमबत्ती", "english": "candle", "pos": "noun", "gender": "F", "category": "household"},
    {"garhwali": "झाड़ू", "hindi": "बुहारी / झाड़ू", "english": "broom", "pos": "noun", "gender": "F", "category": "household"},
    {"garhwali": "रस्सी", "hindi": "बाण / जेवड़ी / रस्सी", "english": "grass rope / hemp twine", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "गठरी", "hindi": "घास या कपड़ों की पोटली", "english": "tied bundle / load", "pos": "noun", "gender": "F", "category": "household"},
    {"garhwali": "टोकरी", "hindi": "डालिया / चंगेरी", "english": "shallow woven cane basket", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "कुल्हाड़ी", "hindi": "कुल्हाड़ी", "english": "woodcutter axe", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "हथौड़ा", "hindi": "हथौड़ा", "english": "hammer", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "छेनी", "hindi": "पत्थर काटने की छेनी", "english": "iron masonry chisel", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "आरी", "hindi": "आरी (लकड़ी चीरने की)", "english": "hand saw", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "कील", "hindi": "लोहे की कील / मेख", "english": "iron nail / peg", "pos": "noun", "gender": "F", "category": "tools"},

    # Geography, Settlements, Nature
    {"garhwali": "बण", "hindi": "जंगल / वन", "english": "forest / woodland", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "रुख", "hindi": "पेड़ / वृक्ष", "english": "tree", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "डाळ", "hindi": "डाल / शाखा / ढलान", "english": "tree bough / branch / grassy slope", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "पात", "hindi": "पत्ता / पर्ण", "english": "leaf", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "फूल", "hindi": "पुष्प / फूल", "english": "flower / blossom", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "फल", "hindi": "फल / फलक", "english": "fruit", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "जड़", "hindi": "मूल / जड़", "english": "root", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "घास", "hindi": "तृण / घास", "english": "fodder grass / lawn", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "कांटा", "hindi": "कंटक / कांटा", "english": "thorn / prickle", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "पत्थर", "hindi": "पाषाण / ढुंगो", "english": "stone / boulder", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "ढुंगो", "hindi": "बड़ा पत्थर", "english": "heavy mountain stone", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "माटी", "hindi": "मृदा / मिट्टी", "english": "soil / sacred earth", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "धूल", "hindi": "धूल / गर्द", "english": "dust", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "धुआं", "hindi": "धूम / धुआं", "english": "smoke", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "आग", "hindi": "अग्नि / आग", "english": "fire", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "आकाश", "hindi": "गगन / आसमान", "english": "sky", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "बादल", "hindi": "मेघ / बादल", "english": "cloud", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "सूरज", "hindi": "सूर्य / घाम", "english": "sun", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "चांद", "hindi": "चंद्रमा / चांद", "english": "moon", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "तारा", "hindi": "नक्षत्र / सितारा", "english": "star", "pos": "noun", "gender": "M", "category": "nature"},
    {"garhwali": "धरती", "hindi": "पृथ्वी / धरती", "english": "earth / homeland", "pos": "noun", "gender": "F", "category": "nature"},
    {"garhwali": "पहाड़", "hindi": "पर्वत / गिरि", "english": "mountain", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "मैदान", "hindi": "सपाट भूमि / मैदान", "english": "plain / valley flat", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "गुफा", "hindi": "कंदरा / उड्यार", "english": "mountain cave / rock shelter", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "उड्यार", "hindi": "पहाड़ी प्राकृतिक गुफा", "english": "high Himalayan rock cavern", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "खड्ड", "hindi": "गहरी खाई", "english": "ravine / precipitous gorge", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "मोड़", "hindi": "सड़क का घुमाव", "english": "sharp hairpin curve", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "बाटो", "hindi": "मार्ग / रास्ता / पगडंडी", "english": "path / mountain track", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "पगडंडी", "hindi": "पैदल चलने की संकरी राह", "english": "footpath along mountain terraced ridges", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "पुल", "hindi": "सेतु / झूला पुल", "english": "suspension rope bridge over river", "pos": "noun", "gender": "M", "category": "architecture"},
    {"garhwali": "गौं", "hindi": "ग्राम / गाँव", "english": "village / mountain hamlet", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "सहर", "hindi": "नगर / शहर", "english": "city / market town", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "बाजार", "hindi": "हाट / बाजार", "english": "bazaar / marketplace", "pos": "noun", "gender": "M", "category": "society"},
    {"garhwali": "दुकान", "hindi": "दुकान / हट्टी", "english": "shop / village store", "pos": "noun", "gender": "F", "category": "business"},
    {"garhwali": "स्कूल", "hindi": "विद्यालय / पाठशाला", "english": "school", "pos": "noun", "gender": "M", "category": "education"},
    {"garhwali": "अस्पताल", "hindi": "चिकित्सालय", "english": "hospital / dispensary", "pos": "noun", "gender": "M", "category": "health"},
    {"garhwali": "थाना", "hindi": "कोतवाली / पुलिस चौकी", "english": "police station", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "डाकघर", "hindi": "डाकखाना", "english": "post office", "pos": "noun", "gender": "M", "category": "communication"},

    # Abstract, Emotions, States
    {"garhwali": "सुख", "hindi": "आनंद / सुख", "english": "happiness / joy / contentment", "pos": "noun", "gender": "M", "category": "emotions"},
    {"garhwali": "दुख", "hindi": "कष्ट / संताप / पीड़ा", "english": "sorrow / grief / suffering", "pos": "noun", "gender": "M", "category": "emotions"},
    {"garhwali": "पीरा", "hindi": "दर्द / वेदना", "english": "pain / anguish", "pos": "noun", "gender": "F", "category": "emotions"},
    {"garhwali": "हर्ष", "hindi": "उल्लास / खुशी", "english": "delight / exuberance", "pos": "noun", "gender": "M", "category": "emotions"},
    {"garhwali": "क्रोध", "hindi": "गुस्सा / रीस", "english": "anger / wrath", "pos": "noun", "gender": "M", "category": "emotions"},
    {"garhwali": "रीस", "hindi": "नाराजगी / क्रोध", "english": "resentment / annoyance", "pos": "noun", "gender": "F", "category": "emotions"},
    {"garhwali": "लाज", "hindi": "लज्जा / शर्म / मर्यादा", "english": "honor / modest shame", "pos": "noun", "gender": "F", "category": "emotions"},
    {"garhwali": "डर", "hindi": "भय / त्रास", "english": "fear / dread", "pos": "noun", "gender": "M", "category": "emotions"},
    {"garhwali": "हिम्मत", "hindi": "साहस / वीरता", "english": "courage / valor", "pos": "noun", "gender": "F", "category": "personality"},
    {"garhwali": "दया", "hindi": "करुणा / कृपा", "english": "compassion / mercy", "pos": "noun", "gender": "F", "category": "emotions"},
    {"garhwali": "सत्य", "hindi": "सच / यथार्थ", "english": "truth / veracity", "pos": "noun", "gender": "M", "category": "abstract"},
    {"garhwali": "झूठ", "hindi": "असत्य / मिथ्या", "english": "falsehood / lie", "pos": "noun", "gender": "M", "category": "abstract"},
    {"garhwali": "पाप", "hindi": "अधर्म / पाप", "english": "sin / moral transgression", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "पुण्य", "hindi": "सत्कर्म / पुण्य", "english": "virtue / merit", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "धर्म", "hindi": "कर्तव्य / धर्म", "english": "righteous duty / religion", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "कर्म", "hindi": "कार्य / कर्म", "english": "deed / action / destiny", "pos": "noun", "gender": "M", "category": "abstract"},
    {"garhwali": "भाग्य", "hindi": "किस्मत / तकदीर", "english": "fortune / destiny", "pos": "noun", "gender": "M", "category": "abstract"},
    {"garhwali": "समय", "hindi": "काल / वक्त", "english": "time / season", "pos": "noun", "gender": "M", "category": "time"},
    {"garhwali": "उम्र", "hindi": "आयु / वय", "english": "age / lifespan", "pos": "noun", "gender": "F", "category": "abstract"},
    {"garhwali": "जिंदगी", "hindi": "जीवन / प्राण", "english": "life / existence", "pos": "noun", "gender": "F", "category": "abstract"},
    {"garhwali": "मौत", "hindi": "मृत्यु / मरण", "english": "death / passing", "pos": "noun", "gender": "F", "category": "abstract"}
]

added = 0
for item in SONG_LEXICON_EXPANSION:
    key = item["garhwali"].strip()
    if key not in existing:
        words.append(item)
        existing.add(key)
        added += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Added {added} words from song lexicon expansion. Total dictionary size now: {len(words)}")
