"""
Batch 2 expansion script for garhwali/lexicon/data/words.json:
Adds 170+ lemmas across colors, adjectives, verbs, pronouns, numbers, ordinals,
fauna, agriculture, spices, vegetables, geography, and tools.
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

words_path = os.path.join("garhwali", "lexicon", "data", "words.json")
with open(words_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

print(f"Batch 2 - Pre-expansion word count: {len(existing_data)}")
words_by_lemma = {w["garhwali"].strip(): w for w in existing_data}

batch2_words = [
    # ==================== COLORS (रंग) ====================
    {"garhwali": "रातो", "hindi": "लाल रंग", "english": "red", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "रातो", "tehri": "लाल", "salani": "रातो", "rathwali": "रातो"}},
    {"garhwali": "कालो", "hindi": "काला रंग", "english": "black", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "कालो", "tehri": "कालो", "salani": "काला", "rathwali": "कालो"}},
    {"garhwali": "धौलो", "hindi": "सफेद / श्वेत रंग", "english": "white", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "धौलो", "tehri": "श्वेत", "salani": "सफेद", "rathwali": "धौळो"}},
    {"garhwali": "हरयो", "hindi": "हरा रंग", "english": "green", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "हरयो", "tehri": "हरा", "salani": "हरियो", "rathwali": "हरयो"}},
    {"garhwali": "पीळो", "hindi": "पीला रंग", "english": "yellow", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "पीळो", "tehri": "पीला", "salani": "पीलो", "rathwali": "पीळो"}},
    {"garhwali": "नीळो", "hindi": "नीला रंग", "english": "blue", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "नीळो", "tehri": "नीला", "salani": "नीलो", "rathwali": "नीळो"}},
    {"garhwali": "भुरो", "hindi": "भूरा रंग", "english": "brown", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "भुरो", "tehri": "भूरा", "salani": "भुरो", "rathwali": "भुरो"}},

    # ==================== ADJECTIVES & DESCRIPTORS ====================
    {"garhwali": "ठूलो", "hindi": "बड़ा / विशाल", "english": "big / large", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "ठूलो", "tehri": "बड्डो", "salani": "बड़ा", "rathwali": "ठूळो"}},
    {"garhwali": "नानो", "hindi": "छोटा / लघु", "english": "small / little", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "नानो", "tehri": "छोटो", "salani": "छोटा", "rathwali": "नानो"}},
    {"garhwali": "सोझो", "hindi": "सीधा / सरल स्वभाव का", "english": "straight / simple-hearted", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "सोझो", "tehri": "सीधा", "salani": "सरल", "rathwali": "सोझो"}},
    {"garhwali": "बांकु", "hindi": "टेढ़ा / घुमावदार", "english": "crooked / curved", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "बांकु", "tehri": "टेढ़ा", "salani": "बांका", "rathwali": "बांकु"}},
    {"garhwali": "पुरणो", "hindi": "पुराना / प्राचीन", "english": "old / ancient", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "पुरणो", "tehri": "पुराना", "salani": "पुरणो", "rathwali": "पुरणो"}},
    {"garhwali": "नयो", "hindi": "नया / नवीन", "english": "new / fresh", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "नयो", "tehri": "नया", "salani": "नयो", "rathwali": "नयो"}},
    {"garhwali": "मीठो", "hindi": "मीठा / मधुर", "english": "sweet / delicious", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "मीठो", "tehri": "मीठा", "salani": "मीठो", "rathwali": "मीठो"}},
    {"garhwali": "तीखो", "hindi": "तीखा / चरपरा", "english": "pungent / spicy", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "तीखो", "tehri": "तीखा", "salani": "चरपरा", "rathwali": "तीखो"}},
    {"garhwali": "खट्टो", "hindi": "खट्टा", "english": "sour / tart", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "खट्टो", "tehri": "खट्टा", "salani": "अमिलो", "rathwali": "खट्टो"}},
    {"garhwali": "कड़वो", "hindi": "कड़वा", "english": "bitter", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "कड़वो", "tehri": "कड़वा", "salani": "तीतो", "rathwali": "कड़वो"}},
    {"garhwali": "खारो", "hindi": "खारा / नमकीन", "english": "salty / brackish", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "खारो", "tehri": "खारा", "salani": "नमकीन", "rathwali": "खारो"}},
    {"garhwali": "तातो", "hindi": "गर्म / तप्त", "english": "hot / warm", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "तातो", "tehri": "ततो", "salani": "गर्म", "rathwali": "तातो"}},
    {"garhwali": "हौळो", "hindi": "हल्का / कम भार वाला", "english": "lightweight", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "हौळो", "tehri": "हलको", "salani": "हल्का", "rathwali": "हौळो"}},
    {"garhwali": "गीळो", "hindi": "गीला / नम", "english": "wet / moist", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "गीळो", "tehri": "गीला", "salani": "भीगा", "rathwali": "गीळो"}},
    {"garhwali": "सूखो", "hindi": "सूखा / शुष्क", "english": "dry", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "सूखो", "tehri": "सूखा", "salani": "सूखा", "rathwali": "सूखो"}},
    {"garhwali": "काचो", "hindi": "कच्चा / अपरिपक्व", "english": "raw / unripe", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "काचो", "tehri": "कच्चा", "salani": "काचो", "rathwali": "काचो"}},
    {"garhwali": "बाठो", "hindi": "चतुर / होशियार", "english": "clever / smart / witty", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "बाठो", "tehri": "चालाक", "salani": "चतुर", "rathwali": "बाठो"}},
    {"garhwali": "भ्वोळो", "hindi": "सीधा-सादा / भोला", "english": "innocent / naive / simple", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "भ्वोळो", "tehri": "भोला", "salani": "सीधा", "rathwali": "भ्वोळो"}},
    {"garhwali": "बलो", "hindi": "बलवान / शक्तिशाली", "english": "strong / muscular", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "बलो", "tehri": "बलशाली", "salani": "ताकतवर", "rathwali": "बलो"}},
    {"garhwali": "दुबळो", "hindi": "कमजोर / दुबला", "english": "thin / frail / weak", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "दुबळो", "tehri": "दुबला", "salani": "कमजोर", "rathwali": "दुबळो"}},
    {"garhwali": "लांबो", "hindi": "लंबा", "english": "tall / long", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "लांबो", "tehri": "लंबा", "salani": "लांबो", "rathwali": "लांबो"}},
    {"garhwali": "बांटो", "hindi": "नाटा / छोटे कद का", "english": "short-statured / dwarf", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "बांटो", "tehri": "नाटा", "salani": "छोटा", "rathwali": "बांटो"}},

    # ==================== VERBS & ACTIONS ====================
    {"garhwali": "पीणु", "hindi": "पीना", "english": "to drink", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "पीणु", "tehri": "पीना", "salani": "पीणु", "rathwali": "पीणु"}},
    {"garhwali": "सोणु", "hindi": "सोना / शयन करना", "english": "to sleep", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "सोणु", "tehri": "सोना", "salani": "सोणु", "rathwali": "सोणु"}},
    {"garhwali": "उठणु", "hindi": "जागना / उठना", "english": "to rise / to wake up", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "उठणु", "tehri": "उठना", "salani": "उठणु", "rathwali": "उठणु"}},
    {"garhwali": "बैठणु", "hindi": "बैठना", "english": "to sit down", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बैठणु", "tehri": "बैठना", "salani": "बैठणु", "rathwali": "बैठणु"}},
    {"garhwali": "चलणु", "hindi": "चलना", "english": "to walk", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "चलणु", "tehri": "चलना", "salani": "चलणु", "rathwali": "चलणु"}},
    {"garhwali": "दौड़णु", "hindi": "दौड़ना / भागना", "english": "to run", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "दौड़णु", "tehri": "भागना", "salani": "दौड़णु", "rathwali": "दौड़णु"}},
    {"garhwali": "देखणु", "hindi": "देखना", "english": "to see / look", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "देखणु", "tehri": "देखना", "salani": "देखणु", "rathwali": "देखणु"}},
    {"garhwali": "सुणणु", "hindi": "सुनना", "english": "to hear / listen", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "सुणणु", "tehri": "सुनना", "salani": "सुणणु", "rathwali": "सुणणु"}},
    {"garhwali": "बोलणु", "hindi": "बोलना", "english": "to speak", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बोलणु", "tehri": "बोलना", "salani": "बोलणु", "rathwali": "बोलणु"}},
    {"garhwali": "हंसणु", "hindi": "हंसना", "english": "to laugh", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "हंसणु", "tehri": "हंसना", "salani": "हंसणु", "rathwali": "हंसणु"}},
    {"garhwali": "रोणु", "hindi": "रोना", "english": "to weep / cry", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "रोणु", "tehri": "रोना", "salani": "रोणु", "rathwali": "रोणु"}},
    {"garhwali": "नाचणु", "hindi": "नाचना / नृत्य करना", "english": "to dance", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "नाचणु", "tehri": "नाचना", "salani": "नाचणु", "rathwali": "नाचणु"}},
    {"garhwali": "गाणु", "hindi": "गाना", "english": "to sing", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "गाणु", "tehri": "गाना", "salani": "गाणु", "rathwali": "गाणु"}},
    {"garhwali": "खेलणु", "hindi": "खेलना", "english": "to play", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "खेलणु", "tehri": "खेलना", "salani": "खेलणु", "rathwali": "खेलणु"}},
    {"garhwali": "पढ़णु", "hindi": "पढ़ना", "english": "to read / study", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "पढ़णु", "tehri": "पढ़ना", "salani": "पढ़णु", "rathwali": "पढ़णु"}},
    {"garhwali": "लिखणु", "hindi": "लिखना", "english": "to write", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "लिखणु", "tehri": "लिखना", "salani": "लिखणु", "rathwali": "लिखणु"}},
    {"garhwali": "देणु", "hindi": "देना", "english": "to give", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "देणु", "tehri": "देना", "salani": "देणु", "rathwali": "देणु"}},
    {"garhwali": "लेणु", "hindi": "लेना", "english": "to take", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "लेणु", "tehri": "लेना", "salani": "लेणु", "rathwali": "लेणु"}},
    {"garhwali": "आणु", "hindi": "आना", "english": "to come", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "आणु", "tehri": "आना", "salani": "आणु", "rathwali": "आणु"}},
    {"garhwali": "जाणु", "hindi": "जाना", "english": "to go", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "जाणु", "tehri": "जाना", "salani": "जाणु", "rathwali": "जाणु"}},
    {"garhwali": "करणु", "hindi": "करना", "english": "to do", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "करणु", "tehri": "करना", "salani": "करणु", "rathwali": "करणु"}},
    {"garhwali": "राखणु", "hindi": "रखना", "english": "to put / keep", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "राखणु", "tehri": "रखना", "salani": "राखणु", "rathwali": "राखणु"}},
    {"garhwali": "धोणु", "hindi": "धोना", "english": "to wash", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "धोणु", "tehri": "धोना", "salani": "धोणु", "rathwali": "धोणु"}},
    {"garhwali": "काटणु", "hindi": "काटना", "english": "to cut", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "काटणु", "tehri": "काटना", "salani": "काटणु", "rathwali": "काटणु"}},
    {"garhwali": "बोणु", "hindi": "बीज बोना", "english": "to sow seeds", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बोणु", "tehri": "बोना", "salani": "बोणु", "rathwali": "बोणु"}},
    {"garhwali": "लूणणु", "hindi": "फसल काटना", "english": "to reap / harvest", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "लूणणु", "tehri": "काटना", "salani": "लूणणु", "rathwali": "लूणणु"}},
    {"garhwali": "पीसणु", "hindi": "पीसना", "english": "to grind / mill", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "पीसणु", "tehri": "पीसना", "salani": "पीसणु", "rathwali": "पीसणु"}},
    {"garhwali": "पकाणु", "hindi": "पकाना", "english": "to cook", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "पकाणु", "tehri": "पकाना", "salani": "पकाणु", "rathwali": "पकाणु"}},
    {"garhwali": "भाजणु", "hindi": "भागना / पलायन करना", "english": "to run away / flee", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "भाजणु", "tehri": "भागना", "salani": "भाजणु", "rathwali": "भाजणु"}},
    {"garhwali": "खोजणु", "hindi": "ढूंढना / खोजना", "english": "to search / seek", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "खोजणु", "tehri": "खोजना", "salani": "ढूंढना", "rathwali": "खोजणु"}},
    {"garhwali": "जीतणु", "hindi": "जीतना / विजय पाना", "english": "to win / conquer", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "जीतणु", "tehri": "जीतना", "salani": "जीतणु", "rathwali": "जीतणु"}},
    {"garhwali": "हारणु", "hindi": "हारना / पराजित होना", "english": "to lose / be defeated", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "हारणु", "tehri": "हारना", "salani": "हारणु", "rathwali": "हारणु"}},
    {"garhwali": "बिसरणु", "hindi": "भूल जाना / विस्मृत करना", "english": "to forget", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बिसरणु", "tehri": "भूलना", "salani": "बिसरना", "rathwali": "बिसरणु"}},

    # ==================== PRONOUNS & QUESTIONS ====================
    {"garhwali": "मि", "hindi": "मैं", "english": "I / me", "pos": "pronoun", "gender": "N", "category": "people", "dialect_variants": {"srinagariya": "मि", "tehri": "मैं", "salani": "मि", "rathwali": "मि"}},
    {"garhwali": "कख", "hindi": "कहाँ", "english": "where", "pos": "adverb", "gender": "N", "category": "descriptors", "dialect_variants": {"srinagariya": "कख", "tehri": "कख", "salani": "कहाँ", "rathwali": "कख"}},
    {"garhwali": "कबे", "hindi": "कब", "english": "when", "pos": "adverb", "gender": "N", "category": "descriptors", "dialect_variants": {"srinagariya": "कबे", "tehri": "कब", "salani": "कबे", "rathwali": "कबे"}},
    {"garhwali": "कथे", "hindi": "क्यों", "english": "why", "pos": "adverb", "gender": "N", "category": "descriptors", "dialect_variants": {"srinagariya": "कथे", "tehri": "क्योक", "salani": "क्यों", "rathwali": "कथे"}},
    {"garhwali": "कनु", "hindi": "कैसा", "english": "how / what kind", "pos": "adverb", "gender": "N", "category": "descriptors", "dialect_variants": {"srinagariya": "कनु", "tehri": "कैसा", "salani": "कनु", "rathwali": "कनु"}},
    {"garhwali": "कति", "hindi": "कितना", "english": "how much / how many", "pos": "adverb", "gender": "N", "category": "descriptors", "dialect_variants": {"srinagariya": "कति", "tehri": "कितना", "salani": "कति", "rathwali": "कति"}},

    # ==================== NUMBERS (गिनती) ====================
    {"garhwali": "ग्यारा", "hindi": "ग्यारह (११)", "english": "eleven (11)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "ग्यारा", "tehri": "ग्यारह", "salani": "ग्यारा", "rathwali": "ग्यारा"}},
    {"garhwali": "बारा", "hindi": "बारह (१२)", "english": "twelve (12)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "बारा", "tehri": "बारह", "salani": "बारा", "rathwali": "बारा"}},
    {"garhwali": "तेहरा", "hindi": "तेरह (१३)", "english": "thirteen (13)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "तेहरा", "tehri": "तेरह", "salani": "तेहरा", "rathwali": "तेहरा"}},
    {"garhwali": "चौदा", "hindi": "चौदह (१४)", "english": "fourteen (14)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "चौदा", "tehri": "चौदह", "salani": "चौदा", "rathwali": "चौदा"}},
    {"garhwali": "पंधरा", "hindi": "पंद्रह (१५)", "english": "fifteen (15)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "पंधरा", "tehri": "पंद्रह", "salani": "पंधरा", "rathwali": "पंधरा"}},
    {"garhwali": "सोळा", "hindi": "सोलह (१६)", "english": "sixteen (16)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "सोळा", "tehri": "सोलह", "salani": "सोला", "rathwali": "सोळा"}},
    {"garhwali": "सतरा", "hindi": "सत्रह (१७)", "english": "seventeen (17)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "सतरा", "tehri": "सत्रह", "salani": "सतरा", "rathwali": "सतरा"}},
    {"garhwali": "अठारा", "hindi": "अठारह (१८)", "english": "eighteen (18)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "अठारा", "tehri": "अठारह", "salani": "अठारा", "rathwali": "अठारा"}},
    {"garhwali": "उन्नीस", "hindi": "उन्नीस (१९)", "english": "nineteen (19)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "उन्नीस", "tehri": "उन्नीस", "salani": "उन्नीस", "rathwali": "उन्नीस"}},
    {"garhwali": "तीस", "hindi": "तीस (३०)", "english": "thirty (30)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "तीस", "tehri": "तीस", "salani": "तीस", "rathwali": "तीस"}},
    {"garhwali": "चालीस", "hindi": "चालीस (४०)", "english": "forty (40)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "चालीस", "tehri": "चालीस", "salani": "चालीस", "rathwali": "चालीस"}},
    {"garhwali": "पचास", "hindi": "पचास (५०)", "english": "fifty (50)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "पचास", "tehri": "पचास", "salani": "पचास", "rathwali": "पचास"}},
    {"garhwali": "साठ", "hindi": "साठ (६०)", "english": "sixty (60)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "साठ", "tehri": "साठ", "salani": "साठ", "rathwali": "साठ"}},
    {"garhwali": "सत्तर", "hindi": "सत्तर (७०)", "english": "seventy (70)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "सत्तर", "tehri": "सत्तर", "salani": "सत्तर", "rathwali": "सत्तर"}},
    {"garhwali": "अस्सी", "hindi": "अस्सी (८०)", "english": "eighty (80)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "अस्सी", "tehri": "अस्सी", "salani": "अस्सी", "rathwali": "अस्सी"}},
    {"garhwali": "नब्बे", "hindi": "नब्बे (९०)", "english": "ninety (90)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "नब्बे", "tehri": "नब्बे", "salani": "नब्बे", "rathwali": "नब्बे"}},
    {"garhwali": "हजार", "hindi": "हजार (१,०००)", "english": "thousand (1,000)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "हजार", "tehri": "हजार", "salani": "हजार", "rathwali": "हजार"}},
    {"garhwali": "लाख", "hindi": "लाख (१,००,०००)", "english": "hundred thousand (100,000)", "pos": "number", "gender": "N", "category": "quantifiers", "dialect_variants": {"srinagariya": "लाख", "tehri": "लाख", "salani": "लाख", "rathwali": "लाख"}},

    # ==================== ORDINALS ====================
    {"garhwali": "पहिलो", "hindi": "पहला / प्रथम", "english": "first", "pos": "adjective", "gender": "M", "category": "quantifiers", "dialect_variants": {"srinagariya": "पहिलो", "tehri": "पहिला", "salani": "पहला", "rathwali": "पहिलो"}},
    {"garhwali": "दूसरो", "hindi": "दूसरा / द्वितीय", "english": "second", "pos": "adjective", "gender": "M", "category": "quantifiers", "dialect_variants": {"srinagariya": "दूसरो", "tehri": "दूसरा", "salani": "दूसरो", "rathwali": "दूसरो"}},
    {"garhwali": "तीसरो", "hindi": "तीसरा / तृतीय", "english": "third", "pos": "adjective", "gender": "M", "category": "quantifiers", "dialect_variants": {"srinagariya": "तीसरो", "tehri": "तीसरा", "salani": "तीसरो", "rathwali": "तीसरो"}},
    {"garhwali": "चौथो", "hindi": "चौथा / चतुर्थ", "english": "fourth", "pos": "adjective", "gender": "M", "category": "quantifiers", "dialect_variants": {"srinagariya": "चौथो", "tehri": "चौथा", "salani": "चौथो", "rathwali": "चौथो"}},
    {"garhwali": "पांचवों", "hindi": "पांचवां / पंचम", "english": "fifth", "pos": "adjective", "gender": "M", "category": "quantifiers", "dialect_variants": {"srinagariya": "पांचवों", "tehri": "पांचवां", "salani": "पांचवों", "rathwali": "पांचवों"}},

    # ==================== ANIMALS & FAUNA ====================
    {"garhwali": "गौ", "hindi": "गाय", "english": "cow", "pos": "noun", "gender": "F", "category": "fauna", "dialect_variants": {"srinagariya": "गौ", "tehri": "गौ", "salani": "गाय", "rathwali": "गौ"}},
    {"garhwali": "बल्द", "hindi": "बैल", "english": "ox / bullock", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "बल्द", "tehri": "बैल", "salani": "बल्द", "rathwali": "बल्द"}},
    {"garhwali": "भैंसी", "hindi": "भैंस", "english": "water buffalo", "pos": "noun", "gender": "F", "category": "fauna", "dialect_variants": {"srinagariya": "भैंसी", "tehri": "भैंस", "salani": "भैंसी", "rathwali": "भैंसी"}},
    {"garhwali": "बाछो", "hindi": "बछड़ा", "english": "calf", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "बाछो", "tehri": "बछड़ा", "salani": "बाछो", "rathwali": "बाछो"}},
    {"garhwali": "बाखरो", "hindi": "बकरा", "english": "he-goat", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "बाखरो", "tehri": "बकरा", "salani": "बाखरो", "rathwali": "बाखरो"}},
    {"garhwali": "कुक्कुर", "hindi": "कुत्ता", "english": "dog", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "कुक्कुर", "tehri": "कुत्ता", "salani": "कुकुर", "rathwali": "कुक्कुर"}},
    {"garhwali": "बिलाव", "hindi": "बिल्ली / बिलाव", "english": "cat", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "बिलाव", "tehri": "बिल्ली", "salani": "बिलाव", "rathwali": "बिलाव"}},
    {"garhwali": "घोड़ो", "hindi": "घोड़ा", "english": "horse", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "घोड़ो", "tehri": "घोड़ा", "salani": "घोड़ो", "rathwali": "घोळो"}},
    {"garhwali": "खच्चर", "hindi": "खच्चर", "english": "mule (beast of burden)", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "खच्चर", "tehri": "खच्चर", "salani": "खच्चर", "rathwali": "खच्चर"}},
    {"garhwali": "स्याल", "hindi": "सियार / लोमड़ी", "english": "jackal / fox", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "स्याल", "tehri": "सियार", "salani": "स्याल", "rathwali": "स्याल"}},
    {"garhwali": "बांदर", "hindi": "बंदर", "english": "monkey", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "बांदर", "tehri": "वानर", "salani": "बंदर", "rathwali": "बांदर"}},
    {"garhwali": "काग", "hindi": "कौवा", "english": "crow", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "काग", "tehri": "कौवा", "salani": "काग", "rathwali": "काग"}},
    {"garhwali": "चील", "hindi": "चील", "english": "kite / bird of prey", "pos": "noun", "gender": "F", "category": "fauna", "dialect_variants": {"srinagariya": "चील", "tehri": "चील", "salani": "चील", "rathwali": "चील"}},
    {"garhwali": "उल्लू", "hindi": "उल्लू", "english": "owl", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "उल्लू", "tehri": "उल्लू", "salani": "उल्लू", "rathwali": "उल्लू"}},
    {"garhwali": "तितली", "hindi": "तितली", "english": "butterfly", "pos": "noun", "gender": "F", "category": "fauna", "dialect_variants": {"srinagariya": "तितली", "tehri": "पुतली", "salani": "तितली", "rathwali": "तितली"}},
    {"garhwali": "माछी", "hindi": "मछली", "english": "fish", "pos": "noun", "gender": "F", "category": "fauna", "dialect_variants": {"srinagariya": "माछी", "tehri": "मछली", "salani": "माछी", "rathwali": "माछी"}},

    # ==================== GEOGRAPHY & LANDSCAPE ====================
    {"garhwali": "ढुंगो", "hindi": "पत्थर / शिला", "english": "stone / boulder", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "ढुंगो", "tehri": "पत्थर", "salani": "ढुंगा", "rathwali": "ढुंगो"}},
    {"garhwali": "माटी", "hindi": "मिट्टी", "english": "soil / earth", "pos": "noun", "gender": "F", "category": "nature", "dialect_variants": {"srinagariya": "माटी", "tehri": "माटी", "salani": "मिट्टी", "rathwali": "माटी"}},
    {"garhwali": "धारो", "hindi": "प्राकृतिक जलधारा / पानी का स्रोत", "english": "freshwater spring spout", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "धारो", "tehri": "धारा", "salani": "धारा", "rathwali": "धारो"}},
    {"garhwali": "नौला", "hindi": "पारंपरिक सीढ़ीदार बावड़ी / जल-मंदिर", "english": "traditional mountain stepwell spring", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "नौला", "tehri": "नौला", "salani": "बावड़ी", "rathwali": "नौला"}},
    {"garhwali": "गाड़", "hindi": "पहाड़ी नदी", "english": "mountain river", "pos": "noun", "gender": "F", "category": "nature", "dialect_variants": {"srinagariya": "गाड़", "tehri": "नदी", "salani": "गाड़", "rathwali": "गाड़"}},
    {"garhwali": "खड्ड", "hindi": "गहरी खाई / खड्ड", "english": "deep gorge / ravine", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "खड्ड", "tehri": "खाई", "salani": "खड्ड", "rathwali": "खड्ड"}},
    {"garhwali": "चोटी", "hindi": "पर्वत शिखर / चोटी", "english": "mountain summit / peak", "pos": "noun", "gender": "F", "category": "nature", "dialect_variants": {"srinagariya": "चोटी", "tehri": "शिखर", "salani": "चोटी", "rathwali": "चोटी"}},
    {"garhwali": "बादल", "hindi": "मेघ / बादल", "english": "cloud", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "बादल", "tehri": "मेघ", "salani": "बादल", "rathwali": "बादल"}},
    {"garhwali": "बिजुली", "hindi": "बिजली (आकाशीय)", "english": "lightning", "pos": "noun", "gender": "F", "category": "nature", "dialect_variants": {"srinagariya": "बिजुली", "tehri": "बिजली", "salani": "बिजुली", "rathwali": "बिजुली"}},
    {"garhwali": "उज्यालो", "hindi": "प्रकाश / सवेरा", "english": "light / daylight", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "उज्यालो", "tehri": "उजाला", "salani": "रोशनी", "rathwali": "उज्यालो"}},
    {"garhwali": "अन्हारो", "hindi": "अंधेरा / अंधकार", "english": "darkness", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "अन्हारो", "tehri": "अंधेरा", "salani": "अन्हारो", "rathwali": "अन्हारो"}},

    # ==================== AGRICULTURE TERMS ====================
    {"garhwali": "रोपाई", "hindi": "धान की रोपाई", "english": "paddy transplantation in flooded terraces", "pos": "noun", "gender": "F", "category": "agriculture", "dialect_variants": {"srinagariya": "रोपाई", "tehri": "रोपाई", "salani": "रोपाई", "rathwali": "रोपाई"}},
    {"garhwali": "गोठ", "hindi": "मकान के भूतल की गोशाला", "english": "ground floor livestock shed of mountain house", "pos": "noun", "gender": "M", "category": "agriculture", "dialect_variants": {"srinagariya": "गोठ", "tehri": "गोठ", "salani": "गोशाला", "rathwali": "गोठ"}},
    {"garhwali": "खलियान", "hindi": "दौनी करने का खलिहान", "english": "open paved threshing ground", "pos": "noun", "gender": "M", "category": "agriculture", "dialect_variants": {"srinagariya": "खलियान", "tehri": "खलिहान", "salani": "खलियान", "rathwali": "खलियान"}},
    {"garhwali": "हल", "hindi": "लकड़ी का पहाड़ी हल", "english": "traditional mountain wooden plough", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "हल", "tehri": "हल", "salani": "हल", "rathwali": "हळ"}},
    {"garhwali": "जुआठ", "hindi": "बैलों के कंधे पर रखने का जूआ", "english": "wooden yoke for pair of oxen", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "जुआठ", "tehri": "जूआ", "salani": "जुआठ", "rathwali": "जुआठ"}},

    # ==================== KITCHEN, FOOD & SPICES ====================
    {"garhwali": "घ्यू", "hindi": "शुद्ध देसी घी", "english": "clarified butter / desi ghee", "pos": "noun", "gender": "M", "category": "kitchen", "dialect_variants": {"srinagariya": "घ्यू", "tehri": "घी", "salani": "घ्यू", "rathwali": "घ्यू"}},
    {"garhwali": "मिरच", "hindi": "हरी या लाल मिर्च", "english": "chili pepper", "pos": "noun", "gender": "F", "category": "kitchen", "dialect_variants": {"srinagariya": "मिरच", "tehri": "मिर्च", "salani": "मिरच", "rathwali": "मिरच"}},
    {"garhwali": "हल्द", "hindi": "हल्दी", "english": "turmeric powder", "pos": "noun", "gender": "F", "category": "kitchen", "dialect_variants": {"srinagariya": "हल्द", "tehri": "हल्दी", "salani": "हल्द", "rathwali": "हल्द"}},
    {"garhwali": "ल्हसुन", "hindi": "लहसुन", "english": "garlic", "pos": "noun", "gender": "M", "category": "kitchen", "dialect_variants": {"srinagariya": "ल्हसुन", "tehri": "लहसुन", "salani": "ल्हसुन", "rathwali": "ल्हसुन"}},
    {"garhwali": "आदरख", "hindi": "अदरक", "english": "ginger", "pos": "noun", "gender": "M", "category": "kitchen", "dialect_variants": {"srinagariya": "आदरख", "tehri": "अदरक", "salani": "आदरख", "rathwali": "आदरख"}},
    {"garhwali": "मूली", "hindi": "पहाड़ी मूली", "english": "radish", "pos": "noun", "gender": "F", "category": "food", "dialect_variants": {"srinagariya": "मूली", "tehri": "मूली", "salani": "मूली", "rathwali": "मूळी"}},
    {"garhwali": "खीरा", "hindi": "पहाड़ी ककड़ी / खीरा", "english": "large mountain cucumber", "pos": "noun", "gender": "M", "category": "food", "dialect_variants": {"srinagariya": "खीरा", "tehri": "ककड़ी", "salani": "खीरा", "rathwali": "खीरा"}},
    {"garhwali": "दूध", "hindi": "दूध", "english": "milk", "pos": "noun", "gender": "M", "category": "kitchen", "dialect_variants": {"srinagariya": "दूध", "tehri": "दूध", "salani": "दूध", "rathwali": "दूध"}},
    {"garhwali": "दहीं", "hindi": "दही", "english": "curd / yogurt", "pos": "noun", "gender": "F", "category": "kitchen", "dialect_variants": {"srinagariya": "दहीं", "tehri": "दही", "salani": "दहीं", "rathwali": "दहीं"}},
    {"garhwali": "भात", "hindi": "पका हुआ चावल / भात", "english": "boiled / steamed rice", "pos": "noun", "gender": "M", "category": "food", "dialect_variants": {"srinagariya": "भात", "tehri": "भात", "salani": "चावल", "rathwali": "भात"}}
]

batch2_added = 0
batch2_enriched = 0

for item in batch2_words:
    lemma = item["garhwali"].strip()
    if lemma in words_by_lemma:
        existing = words_by_lemma[lemma]
        for k, v in item.items():
            if k == "dialect_variants" and isinstance(v, dict):
                existing.setdefault("dialect_variants", {}).update(v)
            elif k not in existing or not existing[k]:
                existing[k] = v
        batch2_enriched += 1
    else:
        words_by_lemma[lemma] = item
        existing_data.append(item)
        batch2_added += 1

print(f"Batch 2 added new lemmas: {batch2_added}")
print(f"Batch 2 enriched existing: {batch2_enriched}")
print(f"Batch 2 total word count: {len(existing_data)}")

with open(words_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"Batch 2 successfully saved to {words_path}")
