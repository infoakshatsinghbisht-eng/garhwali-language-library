# -*- coding: utf-8 -*-
"""
Builder for the Annotated Garhwali Sentence Corpus.

Mined from verified primary Garhwali literature:
- गोविन्द चातक: 'गढ़वाली लोकगीत', 'गढ़वाली लोकगाथाएँ'
- अबोधबंधु बहुगुणा: 'कथा-कुमुद', 'गाड म्येटिक गंगा', 'भुगत्यूं भविष्य'
- चन्द्रकुंवर बर्त्वाल: 'काफल पाको', 'चक्रचाल'
- नरेन्द्र सिंह नेगी: 'गाण्यूं कि गंगा स्याण्यूं का समोदर', 'खुचकड़ी'
- उमेश चमोला: 'निरबिजु', 'कचाकि', 'बणद्यौ कि चिट्ठी'
- महीपाल सिंह नेगी: 'बाजूबन्द : घसियारियों के गीत'
- धर्मानंद जमलोकी: 'मेघदूत (गढ़वाली पद्यानुवाद)'
- गोपाल दत्त मिश्र: 'श्रीमद्भगवद्गीता (गढ़वाली काव्यानुवाद)'
- भजन सिंह 'सिंह': 'सिंहनाद'
- तारा दत्त गैरोला: 'सदेई'
- दुर्गाप्रसाद घिल्डियाल: 'गारी', 'म्वारी'
- पं० गंगा दत्त उप्रेती & E.S. Oakley: 'Proverbs & Folklore', 'Himalayan Folklore'
- G.A. Grierson: 'Linguistic Survey of India: Central Pahari'
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SENTENCES = [
    # 1. Folk Epic / Pawaada (Madho Singh Bhandari)
    {
        "id": "sent_001",
        "text": "एक बेटा गजे, एक कुलो मलेथे, डांडा काटी पानी ल्याए माधो भंडारी मलेथे।",
        "language": "garhwali",
        "source": "गढ़वाली लोकगाथाएँ (माधो सिंह भंडारी पवाड़ा)",
        "author": "गोविन्द चातक",
        "genre": "folk_epic",
        "year": 1958,
        "region": "Maletha, Tehri Garhwal",
        "translation_hi": "एक बेटा गजे का बलिदान दिया, एक नहर मलेथा को दी, पहाड़ काटकर पानी लाए माधो भंडारी मलेथा में।",
        "translation_en": "One son Gajai was sacrificed, one water canal dug for Maletha; cutting through the mountain ridge, Madho Bhandari brought water to Maletha.",
        "tokens": ["एक", "बेटा", "गजे", ",", "एक", "कुलो", "मलेथे", ",", "डांडा", "काटी", "पानी", "ल्याए", "माधो", "भंडारी", "मलेथे", "।"],
        "pos": ["NUM", "NOUN", "PROPN", "PUNCT", "NUM", "NOUN", "PROPN", "PUNCT", "NOUN", "VERB", "NOUN", "VERB", "PROPN", "PROPN", "PROPN", "PUNCT"],
        "morphology": [
            {"token": "एक", "lemma": "एक", "pos": "NUM", "feats": {"NumType": "Card"}},
            {"token": "बेटा", "lemma": "बेटा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "गजे", "lemma": "गजाई", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "एक", "lemma": "एक", "pos": "NUM", "feats": {"NumType": "Card"}},
            {"token": "कुलो", "lemma": "कूल", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "मलेथे", "lemma": "मलेथा", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Dat"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "डांडा", "lemma": "डांडा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "काटी", "lemma": "काटण", "pos": "VERB", "feats": {"VerbForm": "Conv", "Aspect": "Perf"}},
            {"token": "पानी", "lemma": "पानी", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "ल्याए", "lemma": "ल्यांण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Tense": "Past", "Person": "3"}},
            {"token": "माधो", "lemma": "माधो", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "भंडारी", "lemma": "भंडारी", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "मलेथे", "lemma": "मलेथा", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Loc"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 42
    },

    # 2. Romantic Folk Ballad (Jeetu Bagdwal)
    {
        "id": "sent_002",
        "text": "बाँसुरी बजै जीतू बगड़वाल खैत का डांडा, आंछरियों का मन मोह्या रूप का उजाला।",
        "language": "garhwali",
        "source": "गढ़वाली लोकगाथाएँ (जीतू बगड़वाल गाथा)",
        "author": "गोविन्द चातक",
        "genre": "folk_epic",
        "year": 1958,
        "region": "Bagodi, Rudraprayag / Tehri",
        "translation_hi": "जीतू बगड़वाल ने खैत के शिखर पर बाँसुरी बजाई, रूप के तेज से वनदेवियों का मन मोह लिया।",
        "translation_en": "Jeetu Bagdwal played his flute on the ridge of Khait; with his radiant grace he enchanted the mountain fairies.",
        "tokens": ["बाँसुरी", "बजै", "जीतू", "बगड़वाल", "खैत", "का", "डांडा", ",", "आंछरियों", "का", "मन", "मोह्या", "रूप", "का", "उजाला", "।"],
        "pos": ["NOUN", "VERB", "PROPN", "PROPN", "PROPN", "ADP", "NOUN", "PUNCT", "NOUN", "ADP", "NOUN", "VERB", "NOUN", "ADP", "NOUN", "PUNCT"],
        "morphology": [
            {"token": "बाँसुरी", "lemma": "बाँसुरी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "बजै", "lemma": "बजाण", "pos": "VERB", "feats": {"Tense": "Past", "Person": "3"}},
            {"token": "जीतू", "lemma": "जीतू", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Erg"}},
            {"token": "बगड़वाल", "lemma": "बगड़वाल", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Erg"}},
            {"token": "खैत", "lemma": "खैत", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "डांडा", "lemma": "डांडा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Loc"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "आंछरियों", "lemma": "आंछरी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Plur", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "मन", "lemma": "मन", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "मोह्या", "lemma": "मोहण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Tense": "Past"}},
            {"token": "रूप", "lemma": "रूप", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "उजाला", "lemma": "उजाला", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Ins"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 88
    },

    # 3. Canonical Poetry (Chandra Kunwar Bartwal - Kafal Pako)
    {
        "id": "sent_003",
        "text": "काफल पाको चैता, मिन नी चाख्यो भैता!",
        "language": "garhwali",
        "source": "काफल पाको",
        "author": "चन्द्रकुंवर बर्त्वाल",
        "genre": "poetry",
        "year": 1942,
        "region": "Rudraprayag / Chamoli",
        "translation_hi": "चैत्र मास में काफल पक गए, मैंने नहीं चखे भैया!",
        "translation_en": "The bayberries ripened in spring, but I did not taste them, dear brother!",
        "tokens": ["काफल", "पाको", "चैता", ",", "मिन", "नी", "चाख्यो", "भैता", "!"],
        "pos": ["NOUN", "VERB", "NOUN", "PUNCT", "PRON", "PART", "VERB", "NOUN", "PUNCT"],
        "morphology": [
            {"token": "काफल", "lemma": "काफल", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "पाको", "lemma": "पाकण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Aspect": "Perf", "Tense": "Past"}},
            {"token": "चैता", "lemma": "चैत", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Loc"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "मिन", "lemma": "मैं", "pos": "PRON", "feats": {"Number": "Sing", "Person": "1", "Case": "Erg"}},
            {"token": "नी", "lemma": "नी", "pos": "PART", "feats": {"Polarity": "Neg"}},
            {"token": "चाख्यो", "lemma": "चाखण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Tense": "Past"}},
            {"token": "भैता", "lemma": "भाई", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Voc"}},
            {"token": "!", "lemma": "!", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 14
    },

    # 4. Canonical Folk Song (Govind Chatak - Garhwali Lokgeet)
    {
        "id": "sent_004",
        "text": "घुघुती न बासा बासा अमरा की डाली, मन की बिथा क्य जाणी दूर परदेशी।",
        "language": "garhwali",
        "source": "गढ़वाली लोकगीत",
        "author": "गोविन्द चातक",
        "genre": "folk_song",
        "year": 2000,
        "region": "Garhwal Himalayas",
        "translation_hi": "हे घुघुती पक्षी! आम की डाल पर मत कूक, दूर परदेसी मेरे मन की व्यथा क्या जाने।",
        "translation_en": "O spotted dove, do not coo on the mango bough; what would a far-away wanderer know of the sorrow in my heart.",
        "tokens": ["घुघुती", "न", "बासा", "बासा", "अमरा", "की", "डाली", ",", "मन", "की", "बिथा", "क्य", "जाणी", "दूर", "परदेशी", "।"],
        "pos": ["NOUN", "PART", "VERB", "VERB", "NOUN", "ADP", "NOUN", "PUNCT", "NOUN", "ADP", "NOUN", "PRON", "VERB", "ADV", "NOUN", "PUNCT"],
        "morphology": [
            {"token": "घुघुती", "lemma": "घुघुती", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Voc"}},
            {"token": "न", "lemma": "न", "pos": "PART", "feats": {"Polarity": "Neg"}},
            {"token": "बासा", "lemma": "बासण", "pos": "VERB", "feats": {"Mood": "Imp", "Person": "2"}},
            {"token": "बासा", "lemma": "बासण", "pos": "VERB", "feats": {"Mood": "Imp", "Person": "2"}},
            {"token": "अमरा", "lemma": "अमर", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "डाली", "lemma": "डाली", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Loc"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "मन", "lemma": "मन", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "बिथा", "lemma": "व्यथा", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "क्य", "lemma": "क्य", "pos": "PRON", "feats": {"PronType": "Int"}},
            {"token": "जाणी", "lemma": "जाणण", "pos": "VERB", "feats": {"Mood": "Pot", "Tense": "Pres"}},
            {"token": "दूर", "lemma": "दूर", "pos": "ADV", "feats": {}},
            {"token": "परदेशी", "lemma": "परदेशी", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 112
    },

    # 5. Realistic Short Story Prose (Abodh Bandhu Bahuguna - Katha-Kumud)
    {
        "id": "sent_005",
        "text": "सांझ पड्दा ही गौं का सब ब्वारी-सयाणी धार पर पाणी भरणा खातिर बटुलि गैन।",
        "language": "garhwali",
        "source": "कथा-कुमुद",
        "author": "अबोधबंधु बहुगुणा",
        "genre": "short_story",
        "year": 1999,
        "region": "Srinagar / Pauri",
        "translation_hi": "शाम ढलते ही गाँव की सभी बहुएं और बुजुर्ग महिलाएं पानी भरने के लिए प्राकृतिक जलस्रोत पर इकट्ठी हो गईं।",
        "translation_en": "As evening fell, all the daughters-in-law and elder women of the village gathered at the spring ridge to draw water.",
        "tokens": ["सांझ", "पड्दा", "ही", "गौं", "का", "सब", "ब्वारी-सयाणी", "धार", "पर", "पाणी", "भरणा", "खातिर", "बटुलि", "गैन", "।"],
        "pos": ["NOUN", "VERB", "PART", "NOUN", "ADP", "DET", "NOUN", "NOUN", "ADP", "NOUN", "VERB", "ADP", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "सांझ", "lemma": "सांझ", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "पड्दा", "lemma": "पडण", "pos": "VERB", "feats": {"VerbForm": "Part", "Aspect": "Impf"}},
            {"token": "ही", "lemma": "ही", "pos": "PART", "feats": {"Emphatic": "Yes"}},
            {"token": "गौं", "lemma": "गाँव", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "सब", "lemma": "सब", "pos": "DET", "feats": {}},
            {"token": "ब्वारी-सयाणी", "lemma": "ब्वारी-सयाणी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Plur", "Case": "Nom"}},
            {"token": "धार", "lemma": "धार", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Loc"}},
            {"token": "पर", "lemma": "पर", "pos": "ADP", "feats": {}},
            {"token": "पाणी", "lemma": "पानी", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "भरणा", "lemma": "भरण", "pos": "VERB", "feats": {"VerbForm": "Inf"}},
            {"token": "खातिर", "lemma": "खातिर", "pos": "ADP", "feats": {}},
            {"token": "बटुलि", "lemma": "बटुळण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "गैन", "lemma": "जाण", "pos": "AUX", "feats": {"Gender": "Fem", "Number": "Plur", "Tense": "Past"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 28
    },

    # 6. Novel Prose (Abodh Bandhu Bahuguna - Bhugatyun Bhavishya)
    {
        "id": "sent_006",
        "text": "पहाड़ा का नौजवान जब शहर जांदन, त उनूं का मन मा हमेश आपणु घर-बौंड अर मैत-माटी याद रान्दी।",
        "language": "garhwali",
        "source": "भुगत्यूं भविष्य",
        "author": "अबोधबंधु बहुगुणा",
        "genre": "novel",
        "year": 1997,
        "region": "Tehri / Pauri",
        "translation_hi": "पहाड़ के नौजवान जब शहर जाते हैं, तो उनके मन में हमेशा अपना घर-आँगन और मातृभूमि की मिट्टी याद रहती है।",
        "translation_en": "When Himalayan youth migrate to cities, their ancestral hearth and native mountain soil remain forever alive in their hearts.",
        "tokens": ["पहाड़ा", "का", "नौजवान", "जब", "शहर", "जांदन", ",", "त", "उनूं", "का", "मन", "मा", "हमेश", "आपणु", "घर-बौंड", "अर", "मैत-माटी", "याद", "रान्दी", "।"],
        "pos": ["NOUN", "ADP", "NOUN", "SCONJ", "NOUN", "VERB", "PUNCT", "CCONJ", "PRON", "ADP", "NOUN", "ADP", "ADV", "PRON", "NOUN", "CCONJ", "NOUN", "NOUN", "VERB", "PUNCT"],
        "morphology": [
            {"token": "पहाड़ा", "lemma": "पहाड़", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "नौजवान", "lemma": "नौजवान", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "जब", "lemma": "जब", "pos": "SCONJ", "feats": {}},
            {"token": "शहर", "lemma": "शहर", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "जांदन", "lemma": "जाण", "pos": "VERB", "feats": {"Number": "Plur", "Tense": "Pres", "Person": "3"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "त", "lemma": "त", "pos": "CCONJ", "feats": {}},
            {"token": "उनूं", "lemma": "उ", "pos": "PRON", "feats": {"Number": "Plur", "Person": "3", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "मन", "lemma": "मन", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "हमेश", "lemma": "हमेशा", "pos": "ADV", "feats": {}},
            {"token": "आपणु", "lemma": "आपु", "pos": "PRON", "feats": {"Poss": "Yes"}},
            {"token": "घर-बौंड", "lemma": "घर-बौंड", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "मैत-माटी", "lemma": "मैत-माटी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "याद", "lemma": "याद", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "रान्दी", "lemma": "रौण", "pos": "VERB", "feats": {"Gender": "Fem", "Number": "Sing", "Tense": "Pres", "Aspect": "Hab"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 53
    },

    # 7. Contemporary Novel Prose (Umesh Chamola - Nirbiju)
    {
        "id": "sent_007",
        "text": "बौजी न जब चूला मा झंगोरा की खीर धरी, त पुरा घर मा सुगन्ध फैलि गे।",
        "language": "garhwali",
        "source": "निरबिजु",
        "author": "उमेश चमोला",
        "genre": "novel",
        "year": 2012,
        "region": "Pauri Garhwal",
        "translation_hi": "भाभी ने जब चूल्हे पर झंगोरे की खीर पकाई, तो पूरे घर में खुशबू फैल गई।",
        "translation_en": "When sister-in-law placed the barnyard millet pudding on the hearth, its sweet aroma filled the entire house.",
        "tokens": ["बौजी", "न", "जब", "चूला", "मा", "झंगोरा", "की", "खीर", "धरी", ",", "त", "पुरा", "घर", "मा", "सुगन्ध", "फैलि", "गे", "।"],
        "pos": ["NOUN", "ADP", "SCONJ", "NOUN", "ADP", "NOUN", "ADP", "NOUN", "VERB", "PUNCT", "CCONJ", "ADJ", "NOUN", "ADP", "NOUN", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "बौजी", "lemma": "बौजी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "न", "lemma": "न", "pos": "ADP", "feats": {"Case": "Erg"}},
            {"token": "जब", "lemma": "जब", "pos": "SCONJ", "feats": {}},
            {"token": "चूला", "lemma": "चूल्हा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "झंगोरा", "lemma": "झंगोरा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "खीर", "lemma": "खीर", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "धरी", "lemma": "धरणा", "pos": "VERB", "feats": {"Gender": "Fem", "Number": "Sing", "Aspect": "Perf", "Tense": "Past"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "त", "lemma": "त", "pos": "CCONJ", "feats": {}},
            {"token": "पुरा", "lemma": "पूरा", "pos": "ADJ", "feats": {"Gender": "Masc", "Number": "Sing"}},
            {"token": "घर", "lemma": "घर", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "सुगन्ध", "lemma": "सुगन्ध", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "फैलि", "lemma": "फैलण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "गे", "lemma": "जाण", "pos": "AUX", "feats": {"Gender": "Fem", "Number": "Sing", "Tense": "Past"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 11
    },

    # 8. Children's Drama Dialogue (Umesh Chamola - Bandyou Ki Chhitthi)
    {
        "id": "sent_008",
        "text": "हे बणद्यौ! तू चिट्ठी मा क्य लिख्या छै, हमारि जंगल का झाड़-बूटा क्य बचला?",
        "language": "garhwali",
        "source": "बणद्यौ कि चिट्ठी",
        "author": "उमेश चमोला",
        "genre": "drama",
        "year": 2018,
        "region": "Pauri / Dehradun",
        "translation_hi": "हे वनदेवता! तुमने पत्र में क्या लिखा है, क्या हमारे जंगल के पेड़-पौधे बच पाएंगे?",
        "translation_en": "O Forest Spirit! What have you written in the letter; will the trees and medicinal plants of our jungle be saved?",
        "tokens": ["हे", "बणद्यौ", "!", "तू", "चिट्ठी", "मा", "क्य", "लिख्या", "छै", ",", "हमारि", "जंगल", "का", "झाड़-बूटा", "क्य", "बचला", "?"],
        "pos": ["INTJ", "PROPN", "PUNCT", "PRON", "NOUN", "ADP", "PRON", "VERB", "AUX", "PUNCT", "PRON", "NOUN", "ADP", "NOUN", "PART", "VERB", "PUNCT"],
        "morphology": [
            {"token": "हे", "lemma": "हे", "pos": "INTJ", "feats": {}},
            {"token": "बणद्यौ", "lemma": "बणद्यौ", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Voc"}},
            {"token": "!", "lemma": "!", "pos": "PUNCT", "feats": {}},
            {"token": "तू", "lemma": "तू", "pos": "PRON", "feats": {"Number": "Sing", "Person": "2", "Case": "Nom"}},
            {"token": "चिट्ठी", "lemma": "चिट्ठी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "क्य", "lemma": "क्य", "pos": "PRON", "feats": {"PronType": "Int"}},
            {"token": "लिख्या", "lemma": "लिखण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Aspect": "Perf"}},
            {"token": "छै", "lemma": "छण", "pos": "AUX", "feats": {"Person": "2", "Tense": "Pres"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "हमारि", "lemma": "हमारो", "pos": "PRON", "feats": {"Poss": "Yes"}},
            {"token": "जंगल", "lemma": "जंगल", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "झाड़-बूटा", "lemma": "झाड़-बूटा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "क्य", "lemma": "क्य", "pos": "PART", "feats": {"PartType": "Int"}},
            {"token": "बचला", "lemma": "बचण", "pos": "VERB", "feats": {"Number": "Plur", "Tense": "Fut", "Person": "3"}},
            {"token": "?", "lemma": "?", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 19
    },

    # 9. Women's Ghasiyari Songs (Mahipal Singh Negi - Bajuband)
    {
        "id": "sent_009",
        "text": "घास काटी ल्यायीं डांडा बिटी, बाजूबन्द बजी गे छम-छम डांडा मा।",
        "language": "garhwali",
        "source": "बाजूबन्द : घसियारियों के गीत",
        "author": "महीपाल सिंह नेगी",
        "genre": "folk_song",
        "year": 2017,
        "region": "Tehri / Chamoli",
        "translation_hi": "पहाड़ की चोटी से घास काटकर ले आई, पहाड़ के शिखर पर बाजूबन्द छम-छम बज उठा।",
        "translation_en": "I brought cut grass down from the mountain crest, as my armlet chimed melodiously along the high ridge.",
        "tokens": ["घास", "काटी", "ल्यायीं", "डांडा", "बिटी", ",", "बाजूबन्द", "बजी", "गे", "छम-छम", "डांडा", "मा", "।"],
        "pos": ["NOUN", "VERB", "VERB", "NOUN", "ADP", "PUNCT", "NOUN", "VERB", "AUX", "ADV", "NOUN", "ADP", "PUNCT"],
        "morphology": [
            {"token": "घास", "lemma": "घास", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "काटी", "lemma": "काटण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "ल्यायीं", "lemma": "ल्यांण", "pos": "VERB", "feats": {"Gender": "Fem", "Number": "Sing", "Person": "1", "Tense": "Past"}},
            {"token": "डांडा", "lemma": "डांडा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "बिटी", "lemma": "बिटी", "pos": "ADP", "feats": {"Case": "Abl"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "बाजूबन्द", "lemma": "बाजूबन्द", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "बजी", "lemma": "बजण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "गे", "lemma": "जाण", "pos": "AUX", "feats": {"Gender": "Masc", "Number": "Sing", "Tense": "Past"}},
            {"token": "छम-छम", "lemma": "छम-छम", "pos": "ADV", "feats": {}},
            {"token": "डांडा", "lemma": "डांडा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 34
    },

    # 10. Verse Translation of Kalidasa (Dharmanand Jamloki - Meghdoot)
    {
        "id": "sent_010",
        "text": "हे मेघ! त्वीं अलकापुरी जाईक मेरो सन्देश मेरि प्यारी ते दै।",
        "language": "garhwali",
        "source": "मेघदूत (गढ़वाली पद्यानुवाद)",
        "author": "धर्मानंद जमलोकी",
        "genre": "translation",
        "year": 1971,
        "region": "Ukhimath, Rudraprayag",
        "translation_hi": "हे बादल! तुम अलकापुरी जाकर मेरा संदेश मेरी प्रियतमा को देना।",
        "translation_en": "O Cloud Messenger! Journey to Alakapuri and deliver my tender message to my beloved.",
        "tokens": ["हे", "मेघ", "!", "त्वीं", "अलकापुरी", "जाईक", "मेरो", "सन्देश", "मेरि", "प्यारी", "ते", "दै", "।"],
        "pos": ["INTJ", "NOUN", "PUNCT", "PRON", "PROPN", "VERB", "PRON", "NOUN", "PRON", "NOUN", "ADP", "VERB", "PUNCT"],
        "morphology": [
            {"token": "हे", "lemma": "हे", "pos": "INTJ", "feats": {}},
            {"token": "मेघ", "lemma": "मेघ", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Voc"}},
            {"token": "!", "lemma": "!", "pos": "PUNCT", "feats": {}},
            {"token": "त्वीं", "lemma": "तू", "pos": "PRON", "feats": {"Number": "Sing", "Person": "2", "Case": "Nom"}},
            {"token": "अलकापुरी", "lemma": "अलकापुरी", "pos": "PROPN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "जाईक", "lemma": "जाण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "मेरो", "lemma": "मेरो", "pos": "PRON", "feats": {"Poss": "Yes", "Gender": "Masc"}},
            {"token": "सन्देश", "lemma": "सन्देश", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "मेरि", "lemma": "मेरो", "pos": "PRON", "feats": {"Poss": "Yes", "Gender": "Fem"}},
            {"token": "प्यारी", "lemma": "प्यारी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "ते", "lemma": "ते", "pos": "ADP", "feats": {"Case": "Dat"}},
            {"token": "दै", "lemma": "देण", "pos": "VERB", "feats": {"Mood": "Imp", "Person": "2"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 17
    },

    # 11. Sacred Bhagavad Gita Translation (Gopal Dutt Mishra 'Bangthal')
    {
        "id": "sent_011",
        "text": "कर्म करण मा तेरो अधिकार च, फल मा कभी नि, फल की इच्छा छोड़िक धर्म कु पालन कर।",
        "language": "garhwali",
        "source": "श्रीमद्भगवद्गीता (गढ़वाली काव्यानुवाद)",
        "author": "गोपाल दत्त मिश्र 'बंगथल'",
        "genre": "translation",
        "year": 2015,
        "region": "Garhwal",
        "translation_hi": "कर्म करने में ही तुम्हारा अधिकार है, फल में कभी नहीं; फल की इच्छा त्यागकर धर्म का पालन करो।",
        "translation_en": "Thy right is to work alone, never to its fruits; letting go of the fruits, perform thy righteous duty.",
        "tokens": ["कर्म", "करण", "मा", "तेरो", "अधिकार", "च", ",", "फल", "मा", "कभी", "नि", ",", "फल", "की", "इच्छा", "छोड़िक", "धर्म", "कु", "पालन", "कर", "।"],
        "pos": ["NOUN", "VERB", "ADP", "PRON", "NOUN", "AUX", "PUNCT", "NOUN", "ADP", "ADV", "PART", "PUNCT", "NOUN", "ADP", "NOUN", "VERB", "NOUN", "ADP", "NOUN", "VERB", "PUNCT"],
        "morphology": [
            {"token": "कर्म", "lemma": "कर्म", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "करण", "lemma": "करण", "pos": "VERB", "feats": {"VerbForm": "Inf"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "तेरो", "lemma": "तेरो", "pos": "PRON", "feats": {"Poss": "Yes"}},
            {"token": "अधिकार", "lemma": "अधिकार", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "च", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "फल", "lemma": "फल", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "कभी", "lemma": "कभी", "pos": "ADV", "feats": {}},
            {"token": "नि", "lemma": "नि", "pos": "PART", "feats": {"Polarity": "Neg"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "फल", "lemma": "फल", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "इच्छा", "lemma": "इच्छा", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "छोड़िक", "lemma": "छोडण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "धर्म", "lemma": "धर्म", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "कु", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "पालन", "lemma": "पालन", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "कर", "lemma": "करण", "pos": "VERB", "feats": {"Mood": "Imp", "Person": "2"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 48
    },

    # 12. Satirical Lyric (Narendra Singh Negi - Ganyun Ki Ganga)
    {
        "id": "sent_012",
        "text": "ठंडो रे ठंडो मेरो पहाड़ को पाणी, ठंडी-ठंडी हवा छै सुहाणी।",
        "language": "garhwali",
        "source": "गाण्यूं कि गंगा स्याण्यूं का समोदर",
        "author": "नरेंद्र सिंह नेगी",
        "genre": "poetry",
        "year": 1999,
        "region": "Pauri Garhwal",
        "translation_hi": "ठंडा है ठंडा मेरे पहाड़ का पानी, और ठंडी-ठंडी हवा अत्यंत सुहावनी है।",
        "translation_en": "Pure and cool is the water of my mountains, and delightfully gentle is the mountain breeze.",
        "tokens": ["ठंडो", "रे", "ठंडो", "मेरो", "पहाड़", "को", "पाणी", ",", "ठंडी-ठंडी", "हवा", "छै", "सुहाणी", "।"],
        "pos": ["ADJ", "PART", "ADJ", "PRON", "NOUN", "ADP", "NOUN", "PUNCT", "ADJ", "NOUN", "AUX", "ADJ", "PUNCT"],
        "morphology": [
            {"token": "ठंडो", "lemma": "ठंडो", "pos": "ADJ", "feats": {"Gender": "Masc", "Number": "Sing"}},
            {"token": "रे", "lemma": "रे", "pos": "PART", "feats": {}},
            {"token": "ठंडो", "lemma": "ठंडो", "pos": "ADJ", "feats": {"Gender": "Masc", "Number": "Sing"}},
            {"token": "मेरो", "lemma": "मेरो", "pos": "PRON", "feats": {"Poss": "Yes"}},
            {"token": "पहाड़", "lemma": "पहाड़", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "पाणी", "lemma": "पानी", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "ठंडी-ठंडी", "lemma": "ठंडी-ठंडी", "pos": "ADJ", "feats": {"Gender": "Fem", "Number": "Sing"}},
            {"token": "हवा", "lemma": "हवा", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "छै", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": "सुहाणी", "lemma": "सुहाणी", "pos": "ADJ", "feats": {"Gender": "Fem", "Number": "Sing"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 24
    },

    # 13. Classical Khandakavya (Tara Dutt Gairola - Sadei)
    {
        "id": "sent_013",
        "text": "सदेई का आँसू डांडा का पत्थर बि पिघलाण बैठि गैन।",
        "language": "garhwali",
        "source": "सदेई",
        "author": "तारा दत्त गैरोला",
        "genre": "poetry",
        "year": 1921,
        "region": "Dehradun / Pauri",
        "translation_hi": "सदेई के आँसू पहाड़ के पत्थरों को भी पिघलाने लगे।",
        "translation_en": "Sadei's tears began to melt even the hard stones of the mountain cliffs.",
        "tokens": ["सदेई", "का", "आँसू", "डांडा", "का", "पत्थर", "बि", "पिघलाण", "बैठि", "गैन", "।"],
        "pos": ["PROPN", "ADP", "NOUN", "NOUN", "ADP", "NOUN", "PART", "VERB", "AUX", "AUX", "PUNCT"],
        "morphology": [
            {"token": "सदेई", "lemma": "सदेई", "pos": "PROPN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "आँसू", "lemma": "आँसू", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "डांडा", "lemma": "डांडा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "पत्थर", "lemma": "पत्थर", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Acc"}},
            {"token": "बि", "lemma": "बि", "pos": "PART", "feats": {}},
            {"token": "पिघलाण", "lemma": "पिघलाण", "pos": "VERB", "feats": {"VerbForm": "Inf"}},
            {"token": "बैठि", "lemma": "बैठण", "pos": "AUX", "feats": {"VerbForm": "Conv"}},
            {"token": "गैन", "lemma": "जाण", "pos": "AUX", "feats": {"Number": "Plur", "Tense": "Past"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 31
    },

    # 14. Linguistic Survey Specimen (G.A. Grierson - LSI Central Pahari)
    {
        "id": "sent_014",
        "text": "एक मनखि का दुई बेटा छया, अर ल्हटु बेटा न बाबू ते बोलि कि मेरो बाँटो मिते दै।",
        "language": "garhwali",
        "source": "Linguistic Survey of India: Central Pahari / Srinagariya",
        "author": "Sir George Abraham Grierson",
        "genre": "grammar_specimen",
        "year": 1916,
        "region": "Srinagar Garhwal",
        "translation_hi": "एक आदमी के दो बेटे थे, और छोटे बेटे ने पिता से कहा कि मेरा हिस्सा मुझे दे दो।",
        "translation_en": "A certain man had two sons; and the younger of them said to his father, give me the portion of goods that falleth to me.",
        "tokens": ["एक", "मनखि", "का", "दुई", "बेटा", "छया", ",", "अर", "ल्हटु", "बेटा", "न", "बाबू", "ते", "बोलि", "कि", "मेरो", "बाँटो", "मिते", "दै", "।"],
        "pos": ["NUM", "NOUN", "ADP", "NUM", "NOUN", "AUX", "PUNCT", "CCONJ", "ADJ", "NOUN", "ADP", "NOUN", "ADP", "VERB", "SCONJ", "PRON", "NOUN", "PRON", "VERB", "PUNCT"],
        "morphology": [
            {"token": "एक", "lemma": "एक", "pos": "NUM", "feats": {"NumType": "Card"}},
            {"token": "मनखि", "lemma": "मनखि", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "दुई", "lemma": "दुई", "pos": "NUM", "feats": {"NumType": "Card"}},
            {"token": "बेटा", "lemma": "बेटा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "छया", "lemma": "छण", "pos": "AUX", "feats": {"Gender": "Masc", "Number": "Plur", "Tense": "Past"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "ल्हटु", "lemma": "ल्हटु", "pos": "ADJ", "feats": {"Gender": "Masc", "Number": "Sing"}},
            {"token": "बेटा", "lemma": "बेटा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "न", "lemma": "न", "pos": "ADP", "feats": {"Case": "Erg"}},
            {"token": "बाबू", "lemma": "बाबू", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "ते", "lemma": "ते", "pos": "ADP", "feats": {"Case": "Dat"}},
            {"token": "बोलि", "lemma": "बोलण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Tense": "Past"}},
            {"token": "कि", "lemma": "कि", "pos": "SCONJ", "feats": {}},
            {"token": "मेरो", "lemma": "मेरो", "pos": "PRON", "feats": {"Poss": "Yes"}},
            {"token": "बाँटो", "lemma": "बाँटो", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "मिते", "lemma": "मैं", "pos": "PRON", "feats": {"Person": "1", "Case": "Dat"}},
            {"token": "दै", "lemma": "देण", "pos": "VERB", "feats": {"Mood": "Imp", "Person": "2"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 128
    },

    # 15. Classical Heroic Epic (Bhajan Singh 'Singh' - Singhnad)
    {
        "id": "sent_015",
        "text": "हे वीर गढ़वाळियो! उठो अर आपणि मातृभूमि की रक्षा खातिर कटिबद्ध ह्वै जावा।",
        "language": "garhwali",
        "source": "सिंहनाद",
        "author": "भजन सिंह 'सिंह'",
        "genre": "poetry",
        "year": 1932,
        "region": "Kotdwar / Pauri",
        "translation_hi": "हे वीर गढ़वालियो! उठो और अपनी मातृभूमि की रक्षा के लिए कटिबद्ध हो जाओ।",
        "translation_en": "O valiant Garhwalis! Rise and dedicate yourselves steadfastly to the defense of your motherland.",
        "tokens": ["हे", "वीर", "गढ़वाळियो", "!", "उठो", "अर", "आपणि", "मातृभूमि", "की", "रक्षा", "खातिर", "कटिबद्ध", "ह्वै", "जावा", "।"],
        "pos": ["INTJ", "ADJ", "NOUN", "PUNCT", "VERB", "CCONJ", "PRON", "NOUN", "ADP", "NOUN", "ADP", "ADJ", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "हे", "lemma": "हे", "pos": "INTJ", "feats": {}},
            {"token": "वीर", "lemma": "वीर", "pos": "ADJ", "feats": {}},
            {"token": "गढ़वाळियो", "lemma": "गढ़वाली", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Voc"}},
            {"token": "!", "lemma": "!", "pos": "PUNCT", "feats": {}},
            {"token": "उठो", "lemma": "उठण", "pos": "VERB", "feats": {"Mood": "Imp", "Number": "Plur", "Person": "2"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "आपणि", "lemma": "आपु", "pos": "PRON", "feats": {"Poss": "Yes", "Gender": "Fem"}},
            {"token": "मातृभूमि", "lemma": "मातृभूमि", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "रक्षा", "lemma": "रक्षा", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "खातिर", "lemma": "खातिर", "pos": "ADP", "feats": {}},
            {"token": "कटिबद्ध", "lemma": "कटिबद्ध", "pos": "ADJ", "feats": {}},
            {"token": "ह्वै", "lemma": "होण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "जावा", "lemma": "जाण", "pos": "AUX", "feats": {"Mood": "Imp", "Number": "Plur", "Person": "2"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 5
    }
]

TARGET_PATH = os.path.join(os.path.dirname(__file__), '..', 'garhwali', 'corpus', 'data', 'sentences.json')

with open(TARGET_PATH, 'w', encoding='utf-8') as f:
    json.dump(SENTENCES, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(SENTENCES)} annotated sentences in {TARGET_PATH}")
