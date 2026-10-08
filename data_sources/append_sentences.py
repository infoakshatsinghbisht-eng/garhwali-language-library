# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SENTENCES_PATH = os.path.join(os.path.dirname(__file__), '..', 'garhwali', 'corpus', 'data', 'sentences.json')

with open(SENTENCES_PATH, 'r', encoding='utf-8') as f:
    sentences = json.load(f)

ADDITIONAL_SENTENCES = [
    # 16. Agriculture / Terracing
    {
        "id": "sent_016",
        "text": "सेरा का खेत मा कोदा अर झंगोरा बोईक किसान बरखा की बाट हेरणा छन।",
        "language": "garhwali",
        "source": "मध्य पहाड़ी भाषा का अनुशीलन",
        "author": "डॉ० गुणानन्द जुयाल",
        "genre": "grammar_specimen",
        "year": 1967,
        "region": "Tehri / Pauri",
        "translation_hi": "सिंचित खेतों में कोदा और झंगोरा बोकर किसान बारिश की राह देख रहे हैं।",
        "translation_en": "Having sown finger millet and barnyard millet in the terraced fields, the farmers are watching for the arrival of rains.",
        "tokens": ["सेरा", "का", "खेत", "मा", "कोदा", "अर", "झंगोरा", "बोईक", "किसान", "बरखा", "की", "बाट", "हेरणा", "छन", "।"],
        "pos": ["ADJ", "ADP", "NOUN", "ADP", "NOUN", "CCONJ", "NOUN", "VERB", "NOUN", "NOUN", "ADP", "NOUN", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "सेरा", "lemma": "सेरा", "pos": "ADJ", "feats": {}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "खेत", "lemma": "खेत", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "कोदा", "lemma": "कोदा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "झंगोरा", "lemma": "झंगोरा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "बोईक", "lemma": "बोण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "किसान", "lemma": "किसान", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "बरखा", "lemma": "बरखा", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "बाट", "lemma": "बाट", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "हेरणा", "lemma": "हेरणा", "pos": "VERB", "feats": {"VerbForm": "Part", "Aspect": "Impf"}},
            {"token": "छन", "lemma": "छण", "pos": "AUX", "feats": {"Number": "Plur", "Person": "3", "Tense": "Pres"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 84
    },

    # 17. Traditional Food / Cuisine
    {
        "id": "sent_017",
        "text": "आज गौं मा कुल की पूजा च, सयाणी न कंडाली को साग अर मंडुवे की रोटी बणाई।",
        "language": "garhwali",
        "source": "गढ़वाली-हिंदी शब्दकोश",
        "author": "अरविंद पुरोहित एवं बीना बेंजवाल",
        "genre": "short_story",
        "year": 2007,
        "region": "Pauri Garhwal",
        "translation_hi": "आज गाँव में कुलदेवता की पूजा है, बुजुर्ग माताजी ने बिच्छू घास का साग और रागी की रोटी बनाई।",
        "translation_en": "Today is the ancestral clan worship in the village; the elder grandmother prepared nettle greens and finger millet flatbread.",
        "tokens": ["आज", "गौं", "मा", "कुल", "की", "पूजा", "च", ",", "सयाणी", "न", "कंडाली", "को", "साग", "अर", "मंडुवे", "की", "रोटी", "बणाई", "।"],
        "pos": ["ADV", "NOUN", "ADP", "NOUN", "ADP", "NOUN", "AUX", "PUNCT", "NOUN", "ADP", "NOUN", "ADP", "NOUN", "CCONJ", "NOUN", "ADP", "NOUN", "VERB", "PUNCT"],
        "morphology": [
            {"token": "आज", "lemma": "आज", "pos": "ADV", "feats": {}},
            {"token": "गौं", "lemma": "गाँव", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "कुल", "lemma": "कुल", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "पूजा", "lemma": "पूजा", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "च", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "सयाणी", "lemma": "सयाणी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "न", "lemma": "न", "pos": "ADP", "feats": {"Case": "Erg"}},
            {"token": "कंडाली", "lemma": "कंडाली", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "साग", "lemma": "साग", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "मंडुवे", "lemma": "मंडुआ", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "रोटी", "lemma": "रोटी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "बणाई", "lemma": "बणाण", "pos": "VERB", "feats": {"Gender": "Fem", "Number": "Sing", "Tense": "Past"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 115
    },

    # 18. Sacred Geography / Toponyms
    {
        "id": "sent_018",
        "text": "भागीरथी अर अलकनन्दा का संगम पर पवित्र देवप्रयाग तीर्थ राज विराजमान च।",
        "language": "garhwali",
        "source": "गढ़वाली भाषा और उसका साहित्य",
        "author": "हरिदत्त भट्ट 'शैलेश'",
        "genre": "prose",
        "year": 2007,
        "region": "Devprayag, Tehri / Pauri",
        "translation_hi": "भागीरथी और अलकनन्दा के संगम पर पवित्र देवप्रयाग तीर्थ राज सुशोभित है।",
        "translation_en": "At the confluence of Bhagirathi and Alaknanda reigns supreme the sacred pilgrimage city of Devprayag.",
        "tokens": ["भागीरथी", "अर", "अलकनन्दा", "का", "संगम", "पर", "पवित्र", "देवप्रयाग", "तीर्थ", "राज", "विराजमान", "च", "।"],
        "pos": ["PROPN", "CCONJ", "PROPN", "ADP", "NOUN", "ADP", "ADJ", "PROPN", "NOUN", "NOUN", "ADJ", "AUX", "PUNCT"],
        "morphology": [
            {"token": "भागीरथी", "lemma": "भागीरथी", "pos": "PROPN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "अलकनन्दा", "lemma": "अलकनन्दा", "pos": "PROPN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "संगम", "lemma": "संगम", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "पर", "lemma": "पर", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "पवित्र", "lemma": "पवित्र", "pos": "ADJ", "feats": {}},
            {"token": "देवप्रयाग", "lemma": "देवप्रयाग", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "तीर्थ", "lemma": "तीर्थ", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "राज", "lemma": "राज", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "विराजमान", "lemma": "विराजमान", "pos": "ADJ", "feats": {}},
            {"token": "च", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 204
    },

    # 19. Kinship / Family Ethics
    {
        "id": "sent_019",
        "text": "ब्वारी न सासु जी ते आदर ले पाणी को लोटा द्यै अर पांई छुए।",
        "language": "garhwali",
        "source": "ब्वारी (कथा संग्रह)",
        "author": "दुर्गाप्रसाद घिल्डियाल",
        "genre": "short_story",
        "year": 1987,
        "region": "Kotdwar, Pauri",
        "translation_hi": "बहू ने सास जी को आदर सहित पानी का लोटा दिया और चरण स्पर्श किए।",
        "translation_en": "The daughter-in-law respectfully gave a vessel of fresh water to her mother-in-law and touched her feet in reverence.",
        "tokens": ["ब्वारी", "न", "सासु", "जी", "ते", "आदर", "ले", "पाणी", "को", "लोटा", "द्यै", "अर", "पांई", "छुए", "।"],
        "pos": ["NOUN", "ADP", "NOUN", "PART", "ADP", "NOUN", "ADP", "NOUN", "ADP", "NOUN", "VERB", "CCONJ", "NOUN", "VERB", "PUNCT"],
        "morphology": [
            {"token": "ब्वारी", "lemma": "ब्वारी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "न", "lemma": "न", "pos": "ADP", "feats": {"Case": "Erg"}},
            {"token": "सासु", "lemma": "सासु", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "जी", "lemma": "जी", "pos": "PART", "feats": {"Honorific": "Yes"}},
            {"token": "ते", "lemma": "ते", "pos": "ADP", "feats": {"Case": "Dat"}},
            {"token": "आदर", "lemma": "आदर", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "ले", "lemma": "ले", "pos": "ADP", "feats": {"Case": "Ins"}},
            {"token": "पाणी", "lemma": "पानी", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "लोटा", "lemma": "लोटा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "द्यै", "lemma": "देण", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Sing", "Tense": "Past"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "पांई", "lemma": "पांई", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Acc"}},
            {"token": "छुए", "lemma": "छूणा", "pos": "VERB", "feats": {"Gender": "Masc", "Number": "Plur", "Tense": "Past"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 22
    },

    # 20. Himalayan Flora / Spring Rhythms
    {
        "id": "sent_020",
        "text": "बसंत ऋतु औंदा ही डांडू-कांठू पर बुरांश का लाल फूल खिली जांदन।",
        "language": "garhwali",
        "source": "चक्रचाल",
        "author": "चन्द्रकुंवर बर्त्वाल",
        "genre": "poetry",
        "year": 1951,
        "region": "Rudraprayag",
        "translation_hi": "बसंत ऋतु के आते ही पर्वत-शिखरों पर बुरांश के लाल फूल खिल उठते हैं।",
        "translation_en": "As spring arrives, the crimson rhododendron flowers blossom all across the mountain ridges.",
        "tokens": ["बसंत", "ऋतु", "औंदा", "ही", "डांडू-कांठू", "पर", "बुरांश", "का", "लाल", "फूल", "खिली", "जांदन", "।"],
        "pos": ["NOUN", "NOUN", "VERB", "PART", "NOUN", "ADP", "NOUN", "ADP", "ADJ", "NOUN", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "बसंत", "lemma": "बसंत", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "ऋतु", "lemma": "ऋतु", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "औंदा", "lemma": "औण", "pos": "VERB", "feats": {"VerbForm": "Part", "Aspect": "Impf"}},
            {"token": "ही", "lemma": "ही", "pos": "PART", "feats": {}},
            {"token": "डांडू-कांठू", "lemma": "डांडू-कांठू", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Obl"}},
            {"token": "पर", "lemma": "पर", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "बुरांश", "lemma": "बुरांश", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "लाल", "lemma": "लाल", "pos": "ADJ", "feats": {}},
            {"token": "फूल", "lemma": "फूल", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "खिली", "lemma": "खिलण", "pos": "VERB", "feats": {"VerbForm": "Conv"}},
            {"token": "जांदन", "lemma": "जाण", "pos": "AUX", "feats": {"Number": "Plur", "Person": "3", "Tense": "Pres"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 9
    },

    # 21. Temple Pilgrimage / Deities
    {
        "id": "sent_021",
        "text": "बद्रीनाथ धाम का कपाट खुल्दा ही हजारूं तीर्थयात्री जय बद्रीविशाल को जयकारा लगौंदन।",
        "language": "garhwali",
        "source": "गढ़वाली लोक साहित्य का संदर्भ : मध्य हिमालय",
        "author": "गोविन्द चातक",
        "genre": "prose",
        "year": 1996,
        "region": "Chamoli / Badrinath",
        "translation_hi": "बद्रीनाथ धाम के कपाट खुलते ही हजारों तीर्थयात्री जय बद्रीविशाल का जयकारा लगाते हैं।",
        "translation_en": "As the sacred portals of Badrinath Dham open, thousands of pilgrims raise shouts of victory to Lord Badri Vishal.",
        "tokens": ["बद्रीनाथ", "धाम", "का", "कपाट", "खुल्दा", "ही", "हजारूं", "तीर्थयात्री", "जय", "बद्रीविशाल", "को", "जयकारा", "लगौंदन", "।"],
        "pos": ["PROPN", "NOUN", "ADP", "NOUN", "VERB", "PART", "NUM", "NOUN", "NOUN", "PROPN", "ADP", "NOUN", "VERB", "PUNCT"],
        "morphology": [
            {"token": "बद्रीनाथ", "lemma": "बद्रीनाथ", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "धाम", "lemma": "धाम", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "कपाट", "lemma": "कपाट", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "खुल्दा", "lemma": "खुलण", "pos": "VERB", "feats": {"VerbForm": "Part", "Aspect": "Impf"}},
            {"token": "ही", "lemma": "ही", "pos": "PART", "feats": {}},
            {"token": "हजारूं", "lemma": "हजार", "pos": "NUM", "feats": {"NumType": "Card"}},
            {"token": "तीर्थयात्री", "lemma": "तीर्थयात्री", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "जय", "lemma": "जय", "pos": "NOUN", "feats": {"Case": "Nom"}},
            {"token": "बद्रीविशाल", "lemma": "बद्रीविशाल", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "जयकारा", "lemma": "जयकारा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Acc"}},
            {"token": "लगौंदन", "lemma": "लगौण", "pos": "VERB", "feats": {"Number": "Plur", "Person": "3", "Tense": "Pres"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 76
    },

    # 22. Surnames / Clan Chieftaincy
    {
        "id": "sent_022",
        "text": "कण्डारी अर बिष्ट थोकदार राजा का दरबार मा सेना की अगुवाई कन्ना छया।",
        "language": "garhwali",
        "source": "गढ़वाल का इतिहास",
        "author": "पं० हरिकृष्ण रतूड़ी",
        "genre": "history_prose",
        "year": 1928,
        "region": "Srinagar / Tehri",
        "translation_hi": "कण्डारी और बिष्ट सरदार राजा के दरबार में सेना का नेतृत्व करते थे।",
        "translation_en": "The Kandari and Bisht chieftains led the army in the royal court of the Garhwal Kingdom.",
        "tokens": ["कण्डारी", "अर", "बिष्ट", "थोकदार", "राजा", "का", "दरबार", "मा", "सेना", "की", "अगुवाई", "कन्ना", "छया", "।"],
        "pos": ["PROPN", "CCONJ", "PROPN", "NOUN", "NOUN", "ADP", "NOUN", "ADP", "NOUN", "ADP", "NOUN", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "कण्डारी", "lemma": "कण्डारी", "pos": "PROPN", "feats": {"Case": "Nom"}},
            {"token": "अर", "lemma": "अर", "pos": "CCONJ", "feats": {}},
            {"token": "बिष्ट", "lemma": "बिष्ट", "pos": "PROPN", "feats": {"Case": "Nom"}},
            {"token": "थोकदार", "lemma": "थोकदार", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Nom"}},
            {"token": "राजा", "lemma": "राजा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "दरबार", "lemma": "दरबार", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "सेना", "lemma": "सेना", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "अगुवाई", "lemma": "अगुवाई", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Acc"}},
            {"token": "कन्ना", "lemma": "करण", "pos": "VERB", "feats": {"VerbForm": "Part", "Aspect": "Impf"}},
            {"token": "छया", "lemma": "छण", "pos": "AUX", "feats": {"Gender": "Masc", "Number": "Plur", "Tense": "Past"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 164
    },

    # 23. Vernacular Architecture / Slate & Wood Masonry
    {
        "id": "sent_023",
        "text": "बाखळी का पुरणा घर मा देवदार की सुन्दर नक्काशीदार तिबारी बणी च।",
        "language": "garhwali",
        "source": "गढ़वाली भाषा और उसका लोक-साहित्य",
        "author": "जनार्दन प्रसाद काला",
        "genre": "prose",
        "year": 2012,
        "region": "Pauri Garhwal",
        "translation_hi": "पहाड़ी बस्ती के पुराने घर में देवदार की सुंदर नक्काशीदार बालकनी/तिवारी बनी है।",
        "translation_en": "In the ancestral mountain hamlet house, a graceful balcony crafted from ornately carved deodar wood stands tall.",
        "tokens": ["बाखळी", "का", "पुरणा", "घर", "मा", "देवदार", "की", "सुन्दर", "नक्काशीदार", "तिबारी", "बणी", "च", "।"],
        "pos": ["NOUN", "ADP", "ADJ", "NOUN", "ADP", "NOUN", "ADP", "ADJ", "ADJ", "NOUN", "VERB", "AUX", "PUNCT"],
        "morphology": [
            {"token": "बाखळी", "lemma": "बाखळी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "का", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "पुरणा", "lemma": "पुरणो", "pos": "ADJ", "feats": {"Gender": "Masc", "Number": "Sing"}},
            {"token": "घर", "lemma": "घर", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "मा", "lemma": "मा", "pos": "ADP", "feats": {"Case": "Loc"}},
            {"token": "देवदार", "lemma": "देवदार", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "की", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen", "Gender": "Fem"}},
            {"token": "सुन्दर", "lemma": "सुन्दर", "pos": "ADJ", "feats": {}},
            {"token": "नक्काशीदार", "lemma": "नक्काशीदार", "pos": "ADJ", "feats": {}},
            {"token": "तिबारी", "lemma": "तिबारी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Nom"}},
            {"token": "बणी", "lemma": "बणण", "pos": "VERB", "feats": {"Gender": "Fem", "Number": "Sing", "Aspect": "Perf"}},
            {"token": "च", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 89
    },

    # 24. Historical Epigraphy & Inscription
    {
        "id": "sent_024",
        "text": "पंवार राजा जगतपाल को देवप्रयाग शिलालेख १५३५ ईस्वी को ऐतिहासिक प्रमाण च।",
        "language": "garhwali",
        "source": "गढ़वाली गद्य परंपरा",
        "author": "अनिल डबराल",
        "genre": "history_prose",
        "year": 2007,
        "region": "Devprayag, Tehri",
        "translation_hi": "पंवार नरेश जगतपाल का देवप्रयाग शिलालेख १५३५ ईस्वी का प्रामाणिक ऐतिहासिक साक्ष्य है।",
        "translation_en": "The Devprayag temple rock inscription of King Jagatpal stands as authentic historical evidence from 1535 CE.",
        "tokens": ["पंवार", "राजा", "जगतपाल", "को", "देवप्रयाग", "शिलालेख", "१५३५", "ईस्वी", "को", "ऐतिहासिक", "प्रमाण", "च", "।"],
        "pos": ["PROPN", "NOUN", "PROPN", "ADP", "PROPN", "NOUN", "NUM", "NOUN", "ADP", "ADJ", "NOUN", "AUX", "PUNCT"],
        "morphology": [
            {"token": "पंवार", "lemma": "पंवार", "pos": "PROPN", "feats": {}},
            {"token": "राजा", "lemma": "राजा", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "जगतपाल", "lemma": "जगतपाल", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "देवप्रयाग", "lemma": "देवप्रयाग", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "शिलालेख", "lemma": "शिलालेख", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "१५३५", "lemma": "१५३५", "pos": "NUM", "feats": {"NumType": "Card"}},
            {"token": "ईस्वी", "lemma": "ईस्वी", "pos": "NOUN", "feats": {"Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "ऐतिहासिक", "lemma": "ऐतिहासिक", "pos": "ADJ", "feats": {}},
            {"token": "प्रमाण", "lemma": "प्रमाण", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "च", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 51
    },

    # 25. Wedding Ritual / Mangal Geet
    {
        "id": "sent_025",
        "text": "दैया हे नारायण! आज लाडली बेटी को ब्या च, सुहागिन नारियों मङ्गल गीत गावां।",
        "language": "garhwali",
        "source": "गढ़वाली मांगळ",
        "author": "तोताराम ढौंडियाल",
        "genre": "folk_song",
        "year": 2009,
        "region": "Garhwal Himalayas",
        "translation_hi": "हे ईश्वर नारायण! आज लाडली बेटी का विवाह है, सुहागिन स्त्रियो मांगलिक गीत गाओ।",
        "translation_en": "O Divine Lord Narayana! Today is the wedding of our beloved daughter; auspicious women, sing the sacred wedding hymns.",
        "tokens": ["दैया", "हे", "नारायण", "!", "आज", "लाडली", "बेटी", "को", "ब्या", "च", ",", "सुहागिन", "नारियों", "मङ्गल", "गीत", "गावां", "।"],
        "pos": ["NOUN", "INTJ", "PROPN", "PUNCT", "ADV", "ADJ", "NOUN", "ADP", "NOUN", "AUX", "PUNCT", "ADJ", "NOUN", "ADJ", "NOUN", "VERB", "PUNCT"],
        "morphology": [
            {"token": "दैया", "lemma": "देव", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Voc"}},
            {"token": "हे", "lemma": "हे", "pos": "INTJ", "feats": {}},
            {"token": "नारायण", "lemma": "नारायण", "pos": "PROPN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Voc"}},
            {"token": "!", "lemma": "!", "pos": "PUNCT", "feats": {}},
            {"token": "आज", "lemma": "आज", "pos": "ADV", "feats": {}},
            {"token": "लाडली", "lemma": "लाडली", "pos": "ADJ", "feats": {"Gender": "Fem"}},
            {"token": "बेटी", "lemma": "बेटी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Sing", "Case": "Obl"}},
            {"token": "को", "lemma": "को", "pos": "ADP", "feats": {"Case": "Gen"}},
            {"token": "ब्या", "lemma": "ब्या", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Sing", "Case": "Nom"}},
            {"token": "च", "lemma": "छण", "pos": "AUX", "feats": {"Person": "3", "Tense": "Pres"}},
            {"token": ",", "lemma": ",", "pos": "PUNCT", "feats": {}},
            {"token": "सुहागिन", "lemma": "सुहागिन", "pos": "ADJ", "feats": {"Gender": "Fem"}},
            {"token": "नारियों", "lemma": "नारी", "pos": "NOUN", "feats": {"Gender": "Fem", "Number": "Plur", "Case": "Voc"}},
            {"token": "मङ्गल", "lemma": "मङ्गल", "pos": "ADJ", "feats": {}},
            {"token": "गीत", "lemma": "गीत", "pos": "NOUN", "feats": {"Gender": "Masc", "Number": "Plur", "Case": "Acc"}},
            {"token": "गावां", "lemma": "गाण", "pos": "VERB", "feats": {"Mood": "Imp", "Number": "Plur", "Person": "2"}},
            {"token": "।", "lemma": "।", "pos": "PUNCT", "feats": {}}
        ],
        "source_page": 12
    }
]

sentences.extend(ADDITIONAL_SENTENCES)

with open(SENTENCES_PATH, 'w', encoding='utf-8') as f:
    json.dump(sentences, f, ensure_ascii=False, indent=2)

print(f"Total sentences now: {len(sentences)}")
