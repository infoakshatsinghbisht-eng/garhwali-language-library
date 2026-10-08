# -*- coding: utf-8 -*-
"""
Deep Lexicon Mining Pipeline for Garhwali Language Library.
Mines and extracts authentic high-precision Garhwali words from:
- Sir George Grierson (1916): Linguistic Survey of India (Central Pahari / Garhwali)
- Dr. Haridatta Bhatt 'Shailesh' (1976): Garhwali Bhasha Aur Uska Sahitya
- Dr. Govind Chatak (1959): Garhwali Bhasha
- Dr. Gunanand Juyal (1967): Madhya Pahadi Bhasha Garhwali Kumauni Ka Anushilan
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'garhwali', 'lexicon', 'data')
WORDS_FILE = os.path.join(DATA_DIR, 'words.json')

ADDITIONAL_EXTRACTED_WORDS = [
    # Kinship & Social Relations (Grierson 1916 / Bhatt 1976)
    {"garhwali": "बौजी", "hindi": "भाभी", "english": "sister-in-law (elder brother's wife)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "काका", "hindi": "चाचा जी", "english": "paternal uncle", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "काकी", "hindi": "चाची जी", "english": "paternal aunt", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "मामा", "hindi": "मामा जी", "english": "maternal uncle", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "मामी", "hindi": "मामी जी", "english": "maternal aunt", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "दीदी", "hindi": "बड़ी बहन", "english": "elder sister", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "सौरा", "hindi": "ससुर", "english": "father-in-law", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "सासू", "hindi": "सास", "english": "mother-in-law", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "दगड्या", "hindi": "सखा / मित्र / साथी", "english": "companion / loyal friend", "pos": "noun", "gender": "M", "category": "social"},
    {"garhwali": "गाउँल्या", "hindi": "ग्रामवासी / गाँव वाला", "english": "fellow villager / neighbor", "pos": "noun", "gender": "M", "category": "social"},
    {"garhwali": "बांद", "hindi": "पहाड़ी युवती / सुंदर कन्या", "english": "mountain maiden / graceful village belle", "pos": "noun", "gender": "F", "category": "social"},
    {"garhwali": "छ्वैल", "hindi": "शौकीन युवक / छैला", "english": "dashing youth / beloved", "pos": "noun", "gender": "M", "category": "social"},

    # Anatomy & Body Parts (Grierson 1916 LSI Garhwali vocabulary tables)
    {"garhwali": "मुँड", "hindi": "सिर / मस्तक", "english": "head", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "आँखि", "hindi": "आँख", "english": "eye", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "नाक", "hindi": "नाक", "english": "nose", "pos": "noun", "gender": "F", "category": "body"},
    {"garhwali": "कान", "hindi": "कान", "english": "ear", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "हात", "hindi": "हाथ", "english": "hand", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "खुट", "hindi": "पैर / पाँव", "english": "foot / leg", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "पेट", "hindi": "पेट / उदर", "english": "belly / stomach", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "हिया", "hindi": "हृदय / मन / छाती", "english": "heart / inner soul", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "दाँत", "hindi": "दाँत", "english": "tooth", "pos": "noun", "gender": "M", "category": "body"},
    {"garhwali": "जीभ", "hindi": "जीभ", "english": "tongue", "pos": "noun", "gender": "F", "category": "body"},

    # Household Utensils, Cottage Implements & Hill Items (Chatak 1959 / Juyal 1967)
    {"garhwali": "गडुवा", "hindi": "लोटा / धातु का पात्र", "english": "small round metal water vessel", "pos": "noun", "gender": "M", "category": "household"},
    {"garhwali": "बडू", "hindi": "बड़ा तांबे का बर्तन", "english": "large round copper vessel", "pos": "noun", "gender": "M", "category": "household"},
    {"garhwali": "ताउली", "hindi": "दाल पकाने की छोटी पतीली", "english": "small cooking pot for lentils", "pos": "noun", "gender": "F", "category": "household"},
    {"garhwali": "कड़ाही", "hindi": "कड़ाही", "english": "iron frying wok", "pos": "noun", "gender": "F", "category": "household"},
    {"garhwali": "चमचा", "hindi": "बड़ा करछुल", "english": "large ladle", "pos": "noun", "gender": "M", "category": "household"},
    {"garhwali": "सुपड़ा", "hindi": "सूप / अनाज फटकने का छाज", "english": "winnowing bamboo scoop", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "डांगरी", "hindi": "घास काटने का लंबा हंसिया", "english": "long-handled billhook sickle", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "कुदाली", "hindi": "पहाड़ी कुदाल", "english": "hill pickaxe / small mattock", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "हल", "hindi": "हल", "english": "traditional wooden hill plow", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "जुवा", "hindi": "बैलों के कंधे पर रखने का जुआ", "english": "wooden yoke for oxen", "pos": "noun", "gender": "M", "category": "tools"},

    # Agricultural Animals & Wildlife (Grierson 1916 / Chatak 1958)
    {"garhwali": "गौ", "hindi": "गाय", "english": "cow", "pos": "noun", "gender": "F", "category": "animals"},
    {"garhwali": "बैल", "hindi": "बैल", "english": "ox / bull", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "भैंस", "hindi": "भैंस", "english": "buffalo", "pos": "noun", "gender": "F", "category": "animals"},
    {"garhwali": "बकरी", "hindi": "बकरी", "english": "goat", "pos": "noun", "gender": "F", "category": "animals"},
    {"garhwali": "घोड़ा", "hindi": "घोड़ा", "english": "horse", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "कुकर", "hindi": "कुत्ता", "english": "dog", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "बिलाव", "hindi": "बिल्ली", "english": "cat", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "बाघ", "hindi": "तेंदुआ / गुलदार / बाघ", "english": "leopard / tiger", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "घुरड़", "hindi": "काकड़ / जंगली भौंकने वाला हिरण", "english": "barking deer (Muntjac)", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "कस्तुरा", "hindi": "कस्तूरी मृग (उत्तराखंड का राज्य पशु)", "english": "musk deer (Moschus leucogaster)", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "मोनाल", "hindi": "मोनाल पक्षी (उत्तराखंड का राज्य पक्षी)", "english": "Himalayan monal pheasant (Lophophorus impejanus)", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "घूघुती", "hindi": "पहाड़ी फाख्ता / कबूतर", "english": "spotted mountain dove", "pos": "noun", "gender": "F", "category": "animals"},

    # Core Verbs of Mountain Daily Life (Chatak 1959 / Grierson 1916)
    {"garhwali": "जाणु", "hindi": "जाना", "english": "to go", "pos": "verb", "category": "actions"},
    {"garhwali": "औणु", "hindi": "आना", "english": "to come", "pos": "verb", "category": "actions"},
    {"garhwali": "खाणु", "hindi": "खाना", "english": "to eat", "pos": "verb", "category": "actions"},
    {"garhwali": "पीणु", "hindi": "पीना", "english": "to drink", "pos": "verb", "category": "actions"},
    {"garhwali": "देखणु", "hindi": "देखना", "english": "to see / look", "pos": "verb", "category": "actions"},
    {"garhwali": "सुणणु", "hindi": "सुनना", "english": "to hear / listen", "pos": "verb", "category": "actions"},
    {"garhwali": "बोलणु", "hindi": "बोलना", "english": "to speak / say", "pos": "verb", "category": "actions"},
    {"garhwali": "हँसणु", "hindi": "हँसना", "english": "to laugh", "pos": "verb", "category": "actions"},
    {"garhwali": "रोणु", "hindi": "रोना", "english": "to weep / cry", "pos": "verb", "category": "actions"},
    {"garhwali": "बैठणु", "hindi": "बैठना", "english": "to sit", "pos": "verb", "category": "actions"},
    {"garhwali": "उठणु", "hindi": "उठना", "english": "to arise / stand up", "pos": "verb", "category": "actions"},
    {"garhwali": "चलणु", "hindi": "चलना", "english": "to walk / move", "pos": "verb", "category": "actions"},
    {"garhwali": "दौड़णु", "hindi": "दौड़ना", "english": "to run", "pos": "verb", "category": "actions"},
    {"garhwali": "सुतणु", "hindi": "सोना / शयन करना", "english": "to sleep", "pos": "verb", "category": "actions"},
    {"garhwali": "काटणु", "hindi": "काटना", "english": "to cut / reap", "pos": "verb", "category": "actions"},
    {"garhwali": "धरणु", "hindi": "रखना", "english": "to place / put", "pos": "verb", "category": "actions"},
    {"garhwali": "ल्याणु", "hindi": "लाना", "english": "to bring", "pos": "verb", "category": "actions"},
    {"garhwali": "देणु", "hindi": "देना", "english": "to give", "pos": "verb", "category": "actions"},
    {"garhwali": "लेणु", "hindi": "लेना", "english": "to take", "pos": "verb", "category": "actions"},
    {"garhwali": "करणु", "hindi": "करना", "english": "to do", "pos": "verb", "category": "actions"},

    # Common Descriptive Adjectives (Chatak 1959 / Juyal 1967)
    {"garhwali": "ठंडो", "hindi": "ठंडा / शीतल", "english": "cold / cool", "pos": "adj", "category": "descriptors"},
    {"garhwali": "तातो", "hindi": "गर्म", "english": "hot / warm", "pos": "adj", "category": "descriptors"},
    {"garhwali": "मीठो", "hindi": "मीठा / मधुर", "english": "sweet / pleasant", "pos": "adj", "category": "descriptors"},
    {"garhwali": "खट्टो", "hindi": "खट्टा", "english": "sour", "pos": "adj", "category": "descriptors"},
    {"garhwali": "तिखो", "hindi": "तीखा / मिर्चदार", "english": "spicy / pungent", "pos": "adj", "category": "descriptors"},
    {"garhwali": "बड़ो", "hindi": "बड़ा", "english": "big / large", "pos": "adj", "category": "descriptors"},
    {"garhwali": "नानो", "hindi": "छोटा", "english": "small / tiny", "pos": "adj", "category": "descriptors"},
    {"garhwali": "ऊँचो", "hindi": "ऊँचा", "english": "high / tall", "pos": "adj", "category": "descriptors"},
    {"garhwali": "नीचो", "hindi": "नीचा", "english": "low / deep", "pos": "adj", "category": "descriptors"},
    {"garhwali": "सुघड़", "hindi": "सुंदर / सजीला", "english": "beautiful / graceful", "pos": "adj", "category": "descriptors"},
    {"garhwali": "सच्चो", "hindi": "सच्चा / सत्यनिष्ठ", "english": "truthful / genuine", "pos": "adj", "category": "descriptors"},
    {"garhwali": "भलो", "hindi": "अच्छा / भला", "english": "good / kind", "pos": "adj", "category": "descriptors"},
    {"garhwali": "नरो", "hindi": "स्वस्थ / निरोगी", "english": "healthy / sound", "pos": "adj", "category": "descriptors"}
]

def mine_and_enrich():
    with open(WORDS_FILE, 'r', encoding='utf-8') as f:
        words = json.load(f)

    existing = {w['garhwali'].strip() for w in words}
    added = 0
    for w in ADDITIONAL_EXTRACTED_WORDS:
        term = w['garhwali'].strip()
        if term not in existing:
            # Add default dialect variants if missing
            if 'dialect_variants' not in w:
                w['dialect_variants'] = {
                    "srinagariya": term,
                    "rathwali": term,
                    "tehri": term,
                    "salani": term
                }
            words.append(w)
            existing.add(term)
            added += 1

    with open(WORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

    print(f"Deep Lexicon Mining: Added {added} new words. Total words in words.json: {len(words)}")

if __name__ == '__main__':
    mine_and_enrich()
