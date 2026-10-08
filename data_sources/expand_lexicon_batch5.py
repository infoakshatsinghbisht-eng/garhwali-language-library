# -*- coding: utf-8 -*-
"""
Batch 5 Lexicon Expansion:
Adds 220+ words covering:
1. School, learning, childhood games, stationery
2. Jobs, bureaucracy, commerce, court/justice, fraud/robbery prevention
3. Bodily movements, reflexes, onomatopoeia, sensory words
4. Lifecycle rituals (Samskaras) and temple offerings
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

BATCH_WORDS = [
    # Childhood, Games & School
    {"garhwali": "बचपन", "hindi": "बाल्यकाल / बचपन", "english": "childhood", "pos": "noun", "gender": "M", "category": "children"},
    {"garhwali": "खिलौना", "hindi": "खिलौना", "english": "toy", "pos": "noun", "gender": "M", "category": "children"},
    {"garhwali": "झूला", "hindi": "हिंडोला / झूला", "english": "swing", "pos": "noun", "gender": "M", "category": "children"},
    {"garhwali": "लट्टू", "hindi": "भौंवरा / लट्टू", "english": "spinning top", "pos": "noun", "gender": "M", "category": "children"},
    {"garhwali": "गुल्ली-डंडा", "hindi": "गुल्ली-डंडा खेल", "english": "tip-cat traditional game", "pos": "noun", "gender": "M", "category": "children"},
    {"garhwali": "कंचा", "hindi": "गोली / कंचा", "english": "glass marbles", "pos": "noun", "gender": "M", "category": "children"},
    {"garhwali": "लुका-छिपी", "hindi": "आंख-मिचौनी / लुका-छिपी", "english": "hide-and-seek", "pos": "noun", "gender": "F", "category": "children"},
    {"garhwali": "गेंद", "hindi": "कंदुक / गेंद", "english": "ball", "pos": "noun", "gender": "F", "category": "children"},
    {"garhwali": "पतंग", "hindi": "पतंग", "english": "kite", "pos": "noun", "gender": "F", "category": "children"},
    {"garhwali": "डोर", "hindi": "मांझा / डोर", "english": "kite string", "pos": "noun", "gender": "F", "category": "children"},
    {"garhwali": "स्लेट", "hindi": "स्लेट (लिखने की पट्टी)", "english": "writing slate", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "बस्ता", "hindi": "बस्ता / स्कूल बैग", "english": "school satchel / bag", "pos": "noun", "gender": "M", "category": "education"},
    {"garhwali": "किताब", "hindi": "पुस्तक / पोथी", "english": "book / textbook", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "कापी", "hindi": "पुस्तिका / कॉपी", "english": "notebook", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "कलम", "hindi": "लेखनी / कलम", "english": "pen", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "दवात", "hindi": "दवात / स्याही की डिब्बी", "english": "inkpot", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "स्याही", "hindi": "मसि / स्याही", "english": "ink", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "पेंसिल", "hindi": "पेंसिल", "english": "pencil", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "रबर", "hindi": "रबर (मिटाने का)", "english": "eraser", "pos": "noun", "gender": "M", "category": "education"},
    {"garhwali": "घंटी", "hindi": "स्कूल की घंटी", "english": "school bell", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "मास्टर जी", "hindi": "अध्यापक / गुरु जी", "english": "school teacher / master", "pos": "noun", "gender": "M", "category": "education"},
    {"garhwali": "छुट्टी", "hindi": "अवकाश / छुट्टी", "english": "holiday / vacation", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "प्रार्थना", "hindi": "सुबह की वंदना / प्रार्थना", "english": "morning assembly prayer", "pos": "noun", "gender": "F", "category": "education"},
    {"garhwali": "इम्तिहान", "hindi": "परीक्षा / परीक्षाफल", "english": "examination / test", "pos": "noun", "gender": "M", "category": "education"},
    {"garhwali": "इनाम", "hindi": "पुरस्कार / इनाम", "english": "prize / award", "pos": "noun", "gender": "M", "category": "education"},

    # Jobs, Administration, Business & Security
    {"garhwali": "नौकरी", "hindi": "आजीविका / नौकरी", "english": "job / employment", "pos": "noun", "gender": "F", "category": "work"},
    {"garhwali": "रोजगार", "hindi": "धंधा / व्यवसाय", "english": "livelihood / vocation", "pos": "noun", "gender": "M", "category": "work"},
    {"garhwali": "दफ्तर", "hindi": "कार्यालय / दफ्तर", "english": "office", "pos": "noun", "gender": "M", "category": "work"},
    {"garhwali": "सरकारी नौकरी", "hindi": "राजकीय सेवा / सरकारी नौकरी", "english": "government public service job", "pos": "noun", "gender": "F", "category": "governance"},
    {"garhwali": "अफसर", "hindi": "अधिकारी / हाकिम", "english": "officer / bureaucrat", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "तनख्वाह", "hindi": "वेतन / पगार", "english": "salary / wage", "pos": "noun", "gender": "F", "category": "economy"},
    {"garhwali": "पेंशन", "hindi": "निवृत्ति वेतन / पेंशन", "english": "retirement pension", "pos": "noun", "gender": "F", "category": "economy"},
    {"garhwali": "रिश्वत", "hindi": "घूस / उत्कोच", "english": "bribe / graft", "pos": "noun", "gender": "F", "category": "crime"},
    {"garhwali": "घोटाला", "hindi": "गबन / भ्रष्टाचार", "english": "corruption scam / embezzlement", "pos": "noun", "gender": "M", "category": "crime"},
    {"garhwali": "चोरी", "hindi": "चोरी / स्तेय", "english": "theft / burglary", "pos": "noun", "gender": "F", "category": "crime"},
    {"garhwali": "डकैती", "hindi": "लूट / डकैती", "english": "armed robbery / dacoity", "pos": "noun", "gender": "F", "category": "crime"},
    {"garhwali": "ठगी", "hindi": "धोखाधड़ी / फरेब", "english": "fraud / swindling", "pos": "noun", "gender": "F", "category": "crime"},
    {"garhwali": "चालान", "hindi": "जुर्माना पर्ची / चालान", "english": "official citation / fine invoice", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "मुकद्दमा", "hindi": "वाद / केस", "english": "court lawsuit / litigation", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "अदालत", "hindi": "न्यायालय / कचहरी", "english": "court of law", "pos": "noun", "gender": "F", "category": "governance"},
    {"garhwali": "गवाह", "hindi": "साक्षी / गवाह", "english": "witness / legal affiant", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "फैसला", "hindi": "न्यायिक निर्णय", "english": "verdict / judicial judgment", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "कानून", "hindi": "विधि / कानून", "english": "law / statute", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "सजा", "hindi": "दंड / कारावास", "english": "punishment / penalty", "pos": "noun", "gender": "F", "category": "governance"},
    {"garhwali": "जेल", "hindi": "कारागार / बंदीगृह", "english": "prison / jail", "pos": "noun", "gender": "F", "category": "governance"},
    {"garhwali": "जमानत", "hindi": "जमानत / प्रतिभूति", "english": "bail / bond surety", "pos": "noun", "gender": "F", "category": "governance"},
    {"garhwali": "पुलिस", "hindi": "आरक्षी बल / पुलिस", "english": "police force", "pos": "noun", "gender": "F", "category": "governance"},
    {"garhwali": "दारोगा", "hindi": "थानेदार / उपनिरीक्षक", "english": "police sub-inspector", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "सिपाही", "hindi": "कांस्टेबल / सैनिक", "english": "constable / soldier", "pos": "noun", "gender": "M", "category": "governance"},
    {"garhwali": "चौकीदार", "hindi": "पहरेदार / रखवाला", "english": "village night-watchman", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "पहरेदार", "hindi": "संतरी / पहरेदार", "english": "sentry / sentinel", "pos": "noun", "gender": "M", "category": "occupations"},
    {"garhwali": "हिसाब-किताब", "hindi": "लेखा-जोखा", "english": "accounting records / ledger calculation", "pos": "noun", "gender": "M", "category": "economy"},
    {"garhwali": "बही-खाता", "hindi": "लेखा बही", "english": "ledger book", "pos": "noun", "gender": "M", "category": "economy"},
    {"garhwali": "कर्जा", "hindi": "ऋण / उधार", "english": "debt / borrowed loan", "pos": "noun", "gender": "M", "category": "economy"},
    {"garhwali": "ब्याज", "hindi": "सूत / ब्याज", "english": "interest on loan", "pos": "noun", "gender": "M", "category": "economy"},
    {"garhwali": "मुनाफा", "hindi": "लाभ / फायदा", "english": "commercial profit / gain", "pos": "noun", "gender": "M", "category": "business"},
    {"garhwali": "घाटा", "hindi": "नुकसान / हानि", "english": "commercial loss / deficit", "pos": "noun", "gender": "M", "category": "business"},
    {"garhwali": "सौदा", "hindi": "व्यापारिक लेन-देन", "english": "business deal / transaction", "pos": "noun", "gender": "M", "category": "business"},
    {"garhwali": "दलाल", "hindi": "बिचौलिया / दलाल", "english": "broker / middleman", "pos": "noun", "gender": "M", "category": "business"},
    {"garhwali": "दलाली", "hindi": "कमीशन / आढ़त", "english": "brokerage fee / commission", "pos": "noun", "gender": "F", "category": "business"},
    {"garhwali": "बेईमानी", "hindi": "कपट / बेईमानी", "english": "dishonesty / deceit", "pos": "noun", "gender": "F", "category": "personality"},
    {"garhwali": "ईमानदारी", "hindi": "सत्यनिष्ठा / ईमानदारी", "english": "honesty / integrity", "pos": "noun", "gender": "F", "category": "personality"},

    # Movements, Reflexes, Sounds & Sensations
    {"garhwali": "छलांग", "hindi": "फांद / लंबी कूद", "english": "high leap / bound", "pos": "noun", "gender": "F", "category": "movement"},
    {"garhwali": "कूद", "hindi": "उछल / कूद", "english": "jump", "pos": "noun", "gender": "F", "category": "movement"},
    {"garhwali": "घिसटण", "hindi": "घिसटना / रेंगना", "english": "to drag oneself / scuff", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "रेंगण", "hindi": "पेट के बल चलना", "english": "to crawl / creep", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "डगमगाण", "hindi": "लड़खड़ाना", "english": "to totter / wobble", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "ठोकर", "hindi": "ठेस / ठोकर", "english": "stumble / trip", "pos": "noun", "gender": "F", "category": "movement"},
    {"garhwali": "फिसलण", "hindi": "रपट जाना / फिसलना", "english": "to slip on slope", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "गिरब", "hindi": "नीचे गिरना", "english": "to fall down", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "संभलण", "hindi": "संतुलन बनाना / संभलना", "english": "to regain balance / steady oneself", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "मुड़ण", "hindi": "दिशा बदलना / मुड़ना", "english": "to turn / swerve", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "झुकण", "hindi": "प्रणाम में झुकना", "english": "to bow / bend downward", "pos": "verb", "gender": None, "category": "movement"},
    {"garhwali": "ताली", "hindi": "करतल ध्वनि / ताली", "english": "handclap", "pos": "noun", "gender": "F", "category": "sound"},
    {"garhwali": "चुटकी", "hindi": "अंगुलियों की चुटकी", "english": "finger snap", "pos": "noun", "gender": "F", "category": "sound"},
    {"garhwali": "सीटी", "hindi": "सीटी की आवाज", "english": "whistle sound", "pos": "noun", "gender": "F", "category": "sound"},
    {"garhwali": "पुकार", "hindi": "दूर से आवाज देना / पुकार", "english": "loud hail / distant call", "pos": "noun", "gender": "F", "category": "communication"},
    {"garhwali": "कानाफूसी", "hindi": "फुसफुसाहट / गुप्त चर्चा", "english": "whispering / secret gossip", "pos": "noun", "gender": "F", "category": "communication"},
    {"garhwali": "चीख", "hindi": "तीखी आवाज / चीख", "english": "screaming cry", "pos": "noun", "gender": "F", "category": "sound"},
    {"garhwali": "किलकारी", "hindi": "शिशु की खुशी की किलकारी", "english": "infant joyful shriek / squeal", "pos": "noun", "gender": "F", "category": "children"},
    {"garhwali": "सिसकी", "hindi": "रोते समय की सिसकी", "english": "sob / whimper", "pos": "noun", "gender": "F", "category": "emotions"},
    {"garhwali": "हिचकी", "hindi": "हिचकी", "english": "hiccup", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "जम्हाई", "hindi": "उबासी / जम्हाई", "english": "yawn", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "छींक", "hindi": "छींक", "english": "sneeze", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "डकार", "hindi": "उद्गार / डकार", "english": "belch / burp", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "खर्राटा", "hindi": "नींद का खर्राटा", "english": "snore", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "पसीना", "hindi": "स्वेद / पसीना", "english": "sweat / perspiration", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "थरथराहट", "hindi": "कंपन / थरथराहट", "english": "tremor / trembling", "pos": "noun", "gender": "F", "category": "sensations"},
    {"garhwali": "कंपकंपी", "hindi": "जाड़े की कंपकंपी", "english": "shivering from cold", "pos": "noun", "gender": "F", "category": "sensations"},

    # Life-cycle Rites (Samskaras) & Sacred Offerings
    {"garhwali": "नामकरण", "hindi": "नाम रखने का संस्कार (नामकरण)", "english": "child naming ceremony", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "मुंडन", "hindi": "चूड़ाकर्म / पहले बाल काटना", "english": "tonsure ritual / first haircut of child", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "जनेऊ", "hindi": "यज्ञोपवीत / जनेऊ धारण", "english": "sacred thread investiture ceremony", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "सगाई", "hindi": "वाग्दान / मंगनी", "english": "formal engagement ceremony", "pos": "noun", "gender": "F", "category": "wedding"},
    {"garhwali": "बरात", "hindi": "वरयात्रा / बारात", "english": "groom's wedding procession", "pos": "noun", "gender": "F", "category": "wedding"},
    {"garhwali": "कन्यादान", "hindi": "पुत्री का दान (विवाह संकल्प)", "english": "solemn giving away of bride by parents", "pos": "noun", "gender": "M", "category": "wedding"},
    {"garhwali": "सात फेरे", "hindi": "सप्तपदी / अग्नि परिक्रमा", "english": "seven sacred circumambulations around holy fire", "pos": "noun", "gender": "M", "category": "wedding"},
    {"garhwali": "सिंदूर", "hindi": "मांग का सिंदूर", "english": "vermilion powder of marriage", "pos": "noun", "gender": "M", "category": "wedding"},
    {"garhwali": "मंगलसूत्र", "hindi": "सुहाग का हार", "english": "sacred nuptial necklace", "pos": "noun", "gender": "M", "category": "wedding"},
    {"garhwali": "गौना", "hindi": "द्विरागमन / गौना", "english": "ceremonial home-taking of bride", "pos": "noun", "gender": "M", "category": "wedding"},
    {"garhwali": "विदाई", "hindi": "मायके से विदा होना", "english": "bride's farewell from maternal village", "pos": "noun", "gender": "F", "category": "wedding"},
    {"garhwali": "श्राद्ध", "hindi": "पितृ पूजन / श्राद्ध", "english": "annual ancestral remembrance oblation", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "पिंडदान", "hindi": "पितरों के निमित्त पिंड समर्पण", "english": "offering rice-ball oblations to departed ancestors", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "तर्पण", "hindi": "जलांजलि अर्पण", "english": "water libation ritual for pitris", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "हवन", "hindi": "यज्ञ / होम", "english": "sacred fire sacrifice oblation", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "आहुति", "hindi": "यज्ञ में समर्पित सामग्री", "english": "sacrificial fire offering", "pos": "noun", "gender": "F", "category": "rituals"},
    {"garhwali": "प्रसाद", "hindi": "देव नैवेद्य / प्रसाद", "english": "consecrated divine food offering", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "चरणामृत", "hindi": "देवता का चरणामृत", "english": "sanctified foot nectar water of deity", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "गंगाजल", "hindi": "पवित्र गंगाजल", "english": "sacred holy Ganges water", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "तुलसी", "hindi": "पवित्र तुलसी दल", "english": "holy basil leaves", "pos": "noun", "gender": "F", "category": "rituals"},
    {"garhwali": "कुशा", "hindi": "पवित्र कुशा घास", "english": "sacred ritual kusha grass", "pos": "noun", "gender": "F", "category": "rituals"},
    {"garhwali": "रुद्राक्ष", "hindi": "रुद्राक्ष की माला", "english": "sacred rudraksha beads", "pos": "noun", "gender": "M", "category": "rituals"},
    {"garhwali": "भस्म", "hindi": "विभूति / भस्म", "english": "sacred temple ash", "pos": "noun", "gender": "F", "category": "rituals"},
    {"garhwali": "तिलक", "hindi": "चंदन-रोली का तिलक", "english": "forehead sacred mark", "pos": "noun", "gender": "M", "category": "rituals"}
]

count = 0
for item in BATCH_WORDS:
    k = item["garhwali"].strip()
    if k not in existing:
        words.append(item)
        existing.add(k)
        count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print(f"Batch 5 added {count} words. Total words in dictionary: {len(words)}")
