"""
Batch 3 expansion script for garhwali/lexicon/data/words.json:
Adds 125+ lemmas across extended kinship, garments/ornaments, sacred temple terms,
traditional tools, mountain trees/fruits, and everyday action verbs.
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

words_path = os.path.join("garhwali", "lexicon", "data", "words.json")
with open(words_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

print(f"Batch 3 - Pre-expansion word count: {len(existing_data)}")
words_by_lemma = {w["garhwali"].strip(): w for w in existing_data}

batch3_words = [
    # ==================== EXTENDED KINSHIP & FAMILY ====================
    {"garhwali": "फूफू", "hindi": "बुआ / फूफी", "english": "paternal aunt (father's sister)", "pos": "noun", "gender": "F", "category": "kinship", "dialect_variants": {"srinagariya": "फूफू", "tehri": "बुआ", "salani": "फूपी", "rathwali": "फूफू"}},
    {"garhwali": "फूफा", "hindi": "फूफा (बुआ के पति)", "english": "paternal aunt's husband", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "फूफा", "tehri": "फूफा", "salani": "फूफा", "rathwali": "फूफा"}},
    {"garhwali": "मौसी", "hindi": "मौसी (माता की बहन)", "english": "maternal aunt", "pos": "noun", "gender": "F", "category": "kinship", "dialect_variants": {"srinagariya": "मौसी", "tehri": "मासी", "salani": "मौसी", "rathwali": "मौसी"}},
    {"garhwali": "मौसा", "hindi": "मौसा (मौसी के पति)", "english": "maternal aunt's husband", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "मौसा", "tehri": "मौसा", "salani": "मौसा", "rathwali": "मौसा"}},
    {"garhwali": "साढ़ू", "hindi": "साढ़ू (पत्नी की बहन का पति)", "english": "co-brother-in-law (wife's sister's husband)", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "साढ़ू", "tehri": "साढ़ू", "salani": "साढू", "rathwali": "साढ़ू"}},
    {"garhwali": "भांजा", "hindi": "भांजा (बहन का पुत्र)", "english": "sister's son / nephew", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "भांजा", "tehri": "भाणजा", "salani": "भांजा", "rathwali": "भाणजा"}},
    {"garhwali": "भांजी", "hindi": "भांजी (बहन की पुत्री)", "english": "sister's daughter / niece", "pos": "noun", "gender": "F", "category": "kinship", "dialect_variants": {"srinagariya": "भांजी", "tehri": "भाणजी", "salani": "भांजी", "rathwali": "भाणजी"}},
    {"garhwali": "भतीजा", "hindi": "भतीजा (भाई का पुत्र)", "english": "brother's son / nephew", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "भतीजा", "tehri": "भतीजा", "salani": "भतीजा", "rathwali": "भतीजा"}},
    {"garhwali": "भतीजी", "hindi": "भतीजी (भाई की पुत्री)", "english": "brother's daughter / niece", "pos": "noun", "gender": "F", "category": "kinship", "dialect_variants": {"srinagariya": "भतीजी", "tehri": "भतीजी", "salani": "भतीजी", "rathwali": "भतीजी"}},
    {"garhwali": "ससुर", "hindi": "ससुर", "english": "father-in-law", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "ससुर", "tehri": "ससुर", "salani": "ससुर", "rathwali": "ससुर"}},
    {"garhwali": "सासू", "hindi": "सास", "english": "mother-in-law", "pos": "noun", "gender": "F", "category": "kinship", "dialect_variants": {"srinagariya": "सासू", "tehri": "सासू", "salani": "सास", "rathwali": "सासू"}},
    {"garhwali": "पुरोहित", "hindi": "कुल पुरोहित / पण्डित", "english": "family priest / hereditary ritual preceptor", "pos": "noun", "gender": "M", "category": "kinship", "dialect_variants": {"srinagariya": "पुरोहित", "tehri": "पुरोहित", "salani": "पण्डित", "rathwali": "पुरोहित"}},

    # ==================== GARMENTS & ORNAMENTS ====================
    {"garhwali": "घाघरी", "hindi": "पारंपरिक घेरदार घाघरा", "english": "traditional flared pleated mountain skirt", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "घाघरी", "tehri": "घाघरा", "salani": "घाघरी", "rathwali": "घाघरी"}},
    {"garhwali": "आंगड़ी", "hindi": "पारंपरिक कुर्ती / आंगड़ी", "english": "traditional long-sleeved mountain bodice", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "आंगड़ी", "tehri": "कुर्ती", "salani": "आंगड़ी", "rathwali": "आंगळी"}},
    {"garhwali": "गाती", "hindi": "कमर पर बांधी जाने वाली चादर / गाती", "english": "woolen shawl tied around waist and shoulders for mountain chores", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "गाती", "tehri": "गाती", "salani": "कमरबंद", "rathwali": "गाती"}},
    {"garhwali": "पाजेब", "hindi": "चांदी की पायल / पाजेब", "english": "silver ankle bells / anklet", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "पाजेब", "tehri": "पायल", "salani": "पाजेब", "rathwali": "पाजेब"}},
    {"garhwali": "बिछुआ", "hindi": "पैरों की उंगलियों की बिछिया", "english": "silver toe rings worn by married women", "pos": "noun", "gender": "M", "category": "clothing", "dialect_variants": {"srinagariya": "बिछुआ", "tehri": "चुटकी", "salani": "बिछुआ", "rathwali": "बिछुआ"}},
    {"garhwali": "पौंची", "hindi": "मखमली पट्टी पर जड़ा सोने का कंगन", "english": "gold beaded bracelet mounted on red velvet", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "पौंची", "tehri": "पौंची", "salani": "पहुंची", "rathwali": "पौंची"}},
    {"garhwali": "तिलहरी", "hindi": "तिलहरी (सोने का पारंपरिक हार)", "english": "traditional golden multi-bead necklace strung on silk thread", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "तिलहरी", "tehri": "तिलहरी", "salani": "माला", "rathwali": "तिलहरी"}},
    {"garhwali": "बुलाक", "hindi": "बुलाक (नाक के बीच का आभूषण)", "english": "delicate filigree gold ring worn in the nasal septum", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "बुलाक", "tehri": "बुलाक", "salani": "बुलाक", "rathwali": "बुलाक"}},
    {"garhwali": "चरू", "hindi": "काले मोतियों का मंगलसूत्र", "english": "sacred black bead marital necklace", "pos": "noun", "gender": "M", "category": "clothing", "dialect_variants": {"srinagariya": "चरू", "tehri": "मंगलसूत्र", "salani": "चरू", "rathwali": "चरू"}},
    {"garhwali": "थुलमा", "hindi": "ऊन का मोटा गर्म कंबल", "english": "thick fluffy high-altitude sheep-wool blanket", "pos": "noun", "gender": "M", "category": "clothing", "dialect_variants": {"srinagariya": "थुलमा", "tehri": "थुलमा", "salani": "कंबल", "rathwali": "थुलमा"}},
    {"garhwali": "पंखी", "hindi": "भेड़ के ऊन की महीन चादर", "english": "fine handloom sheep-wool wrap cape woven in Chamoli", "pos": "noun", "gender": "F", "category": "clothing", "dialect_variants": {"srinagariya": "पंखी", "tehri": "पंखी", "salani": "शॉल", "rathwali": "पंखी"}},
    {"garhwali": "चुटका", "hindi": "खुरदरा ऊनी कालीन", "english": "heavy coarse mountain sheep-wool floor rug", "pos": "noun", "gender": "M", "category": "clothing", "dialect_variants": {"srinagariya": "चुटका", "tehri": "चुटका", "salani": "कालीन", "rathwali": "चुटका"}},

    # ==================== SACRED TEMPLE, DEITY & SPIRITUAL TERMS ====================
    {"garhwali": "थान", "hindi": "ग्राम देवता का खुला शिला-स्थान", "english": "open-air consecrated stone shrine of a village deity", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "थान", "tehri": "थान", "salani": "स्थान", "rathwali": "थान"}},
    {"garhwali": "देवाल", "hindi": "मंदिर / देवालय", "english": "stone temple / house of God", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "देवाल", "tehri": "मंदिर", "salani": "देवालय", "rathwali": "देवाल"}},
    {"garhwali": "रावल", "hindi": "बदरीनाथ व केदारनाथ के मुख्य नम्बूदिरी/पुजारी", "english": "chief high priest of Badrinath and Kedarnath temples", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "रावल", "tehri": "रावल", "salani": "मुख्य पुजारी", "rathwali": "रावल"}},
    {"garhwali": "भोग", "hindi": "देवता को अर्पित नैवेद्य", "english": "sacred consecrated food offering to deities", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "भोग", "tehri": "भोग", "salani": "प्रसाद", "rathwali": "भोग"}},
    {"garhwali": "प्रसाद", "hindi": "प्रसाद", "english": "blessed food distributed to worshippers", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "प्रसाद", "tehri": "प्रसाद", "salani": "प्रसाद", "rathwali": "प्रसाद"}},
    {"garhwali": "प्रयाग", "hindi": "पवित्र नदियों का संगम स्थल", "english": "sacred confluence of Himalayan rivers (Panch Prayag)", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "प्रयाग", "tehri": "संगम", "salani": "प्रयाग", "rathwali": "प्रयाग"}},
    {"garhwali": "परिक्रमा", "hindi": "मंदिर या तीर्थ की प्रदक्षिणा", "english": "ritual circumambulation of temple or mountain", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "परिक्रमा", "tehri": "फेरा", "salani": "प्रदक्षिणा", "rathwali": "परिक्रमा"}},
    {"garhwali": "संकल्प", "hindi": "धार्मिक प्रतिज्ञा / संकल्प", "english": "solemn ritual vow taken with water in palm", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "संकल्प", "tehri": "संकल्प", "salani": "नियम", "rathwali": "संकल्प"}},
    {"garhwali": "जप", "hindi": "मंत्र जप", "english": "silent meditative chant of sacred syllables", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "जप", "tehri": "जाप", "salani": "जप", "rathwali": "जप"}},
    {"garhwali": "आहुति", "hindi": "हवन में अर्पित घृत एवं सामग्री", "english": "sacred offering of ghee and samagri poured into fire", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "आहुति", "tehri": "आहुति", "salani": "हवि", "rathwali": "आहुति"}},
    {"garhwali": "चरणामृत", "hindi": "भगवान के चरणों का पवित्र जल", "english": "consecrated holy water of deity's feet", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "चरणामृत", "tehri": "चरणामृत", "salani": "तीर्थ-जल", "rathwali": "चरणामृत"}},

    # ==================== TRADITIONAL TOOLS & IMPLEMENTS ====================
    {"garhwali": "गैंती", "hindi": "पत्थर तोड़ने की गैंती", "english": "pickaxe for excavating rocky terraced hillsides", "pos": "noun", "gender": "F", "category": "tools", "dialect_variants": {"srinagariya": "गैंती", "tehri": "गैंती", "salani": "पिकैक्स", "rathwali": "गैंती"}},
    {"garhwali": "वसूला", "hindi": "लकड़ी तराशने का बसूला", "english": "carpenter's adze for smoothing timber beams", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "वसूला", "tehri": "बसूला", "salani": "वसूला", "rathwali": "वसूला"}},
    {"garhwali": "आरी", "hindi": "लकड़ी काटने की आरी", "english": "handsaw for slicing wood", "pos": "noun", "gender": "F", "category": "tools", "dialect_variants": {"srinagariya": "आरी", "tehri": "आरी", "salani": "आरी", "rathwali": "आरी"}},
    {"garhwali": "हथौड़ा", "hindi": "हथौड़ा", "english": "hammer", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "हथौड़ा", "tehri": "हथौड़ा", "salani": "हथौड़ा", "rathwali": "हथौड़ा"}},
    {"garhwali": "सुआ", "hindi": "बोरा सीने का बड़ा सुआ", "english": "large thick needle for stitching jute/wool bags", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "सुआ", "tehri": "सुआ", "salani": "सुआ", "rathwali": "सुआ"}},
    {"garhwali": "तकली", "hindi": "ऊन कातने की तकली", "english": "traditional drop spindle for spinning sheep wool", "pos": "noun", "gender": "F", "category": "tools", "dialect_variants": {"srinagariya": "तकली", "tehri": "तकली", "salani": "तकली", "rathwali": "तकळी"}},
    {"garhwali": "चरखा", "hindi": "चरखा", "english": "spinning wheel", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "चरखा", "tehri": "चरखा", "salani": "चरखा", "rathwali": "चरखा"}},
    {"garhwali": "खड्डी", "hindi": "हाथकरघा (हैंडलूम)", "english": "traditional wooden pit handloom for weaving wool", "pos": "noun", "gender": "F", "category": "tools", "dialect_variants": {"srinagariya": "खड्डी", "tehri": "करघा", "salani": "खड्डी", "rathwali": "खड्डी"}},
    {"garhwali": "सूप", "hindi": "अनाज फटकने का बाँस का सूप", "english": "woven bamboo winnowing tray for grain", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "सूप", "tehri": "सूप", "salani": "सूपड़ा", "rathwali": "सूप"}},
    {"garhwali": "चलनी", "hindi": "आटा छानने की छलनी", "english": "flour sieve", "pos": "noun", "gender": "F", "category": "kitchen", "dialect_variants": {"srinagariya": "चलनी", "tehri": "छलनी", "salani": "चलनी", "rathwali": "चलनी"}},
    {"garhwali": "दीया", "hindi": "मिट्टी का तेल का दीपक", "english": "earthen clay lamp filled with mustard oil", "pos": "noun", "gender": "M", "category": "household", "dialect_variants": {"srinagariya": "दीया", "tehri": "दीपक", "salani": "दीया", "rathwali": "दीया"}},

    # ==================== MOUNTAIN TREES, FRUITS & FLORA ====================
    {"garhwali": "पंगर", "hindi": "पहाड़ी चेस्टनट (घोड़ा शाहबलूत)", "english": "Himalayan horse chestnut tree (Aesculus indica)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "पंगर", "tehri": "पंगर", "salani": "चेस्टनट", "rathwali": "पंगर"}},
    {"garhwali": "अखरोट", "hindi": "अखरोट", "english": "Himalayan walnut tree and nut (Juglans regia)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "अखरोट", "tehri": "अखरोट", "salani": "अखरोट", "rathwali": "अखरोट"}},
    {"garhwali": "चुलू", "hindi": "जंगली खुबानी", "english": "wild mountain apricot (Prunus armeniaca)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "चुलू", "tehri": "खुबानी", "salani": "चुलू", "rathwali": "चुलू"}},
    {"garhwali": "आड़ू", "hindi": "आड़ू", "english": "mountain peach (Prunus persica)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "आड़ू", "tehri": "आड़ू", "salani": "आड़ू", "rathwali": "आड़ू"}},
    {"garhwali": "दाड़िम", "hindi": "जंगली अनार (दाड़िम)", "english": "wild mountain pomegranate (Punica granatum)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "दाड़िम", "tehri": "दाड़िम", "salani": "अनार", "rathwali": "दाड़िम"}},
    {"garhwali": "आंवला", "hindi": "आंवला", "english": "Indian gooseberry (Phyllanthus emblica)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "आंवला", "tehri": "आंवला", "salani": "आंवला", "rathwali": "आंवला"}},
    {"garhwali": "हरड़", "hindi": "हरड़ (हरीतकी)", "english": "black myrobalan medicinal fruit (Terminalia chebula)", "pos": "noun", "gender": "F", "category": "flora", "dialect_variants": {"srinagariya": "हरड़", "tehri": "हरड़", "salani": "हरड़", "rathwali": "हरड़"}},
    {"garhwali": "पीपल", "hindi": "पीपल का पवित्र वृक्ष", "english": "sacred fig tree (Ficus religiosa)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "पीपल", "tehri": "पीपल", "salani": "पीपल", "rathwali": "पीपळ"}},
    {"garhwali": "बरगद", "hindi": "बरगद (वट वृक्ष)", "english": "banyan tree (Ficus benghalensis)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "बरगद", "tehri": "बड़", "salani": "बरगद", "rathwali": "बड़"}},
    {"garhwali": "तुलसी", "hindi": "तुलसी का पौधा", "english": "holy basil (Ocimum sanctum)", "pos": "noun", "gender": "F", "category": "flora", "dialect_variants": {"srinagariya": "तुलसी", "tehri": "तुलसी", "salani": "तुलसी", "rathwali": "तुलसी"}},
    {"garhwali": "दूब", "hindi": "दूर्वा / दूब घास", "english": "sacred Bermuda grass (Cynodon dactylon) used in pujas", "pos": "noun", "gender": "F", "category": "flora", "dialect_variants": {"srinagariya": "दूब", "tehri": "दूर्वा", "salani": "दूब", "rathwali": "दूब"}},
    {"garhwali": "कुश", "hindi": "कुश घास", "english": "sacred sacrificial grass (Desmostachya bipinnata)", "pos": "noun", "gender": "M", "category": "flora", "dialect_variants": {"srinagariya": "कुश", "tehri": "कुश", "salani": "कुशा", "rathwali": "कुश"}},

    # ==================== ADDITIONAL EVERYDAY VERBS ====================
    {"garhwali": "बुलाणु", "hindi": "बुलाना / निमंत्रण देना", "english": "to call / summon / invite", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बुलाणु", "tehri": "बुलाना", "salani": "बुलाणु", "rathwali": "बुलाणु"}},
    {"garhwali": "समझाणु", "hindi": "समझाना", "english": "to explain / persuade", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "समझाणु", "tehri": "समझाना", "salani": "समझाणु", "rathwali": "समझाणु"}},
    {"garhwali": "पूछणु", "hindi": "पूछना / प्रश्न करना", "english": "to ask / inquire", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "पूछणु", "tehri": "पूछना", "salani": "पूछणु", "rathwali": "पूछणु"}},
    {"garhwali": "बतौणु", "hindi": "बताना / दिखाना", "english": "to tell / disclose / show", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बतौणु", "tehri": "बताना", "salani": "बतौणु", "rathwali": "बतौणु"}},
    {"garhwali": "सिखाणु", "hindi": "सिखाना / शिक्षा देना", "english": "to teach / instruct", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "सिखाणु", "tehri": "सिखाना", "salani": "सिखाणु", "rathwali": "सिखाणु"}},
    {"garhwali": "सीखणु", "hindi": "सीखना / ज्ञान पाना", "english": "to learn", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "सीखणु", "tehri": "सीखना", "salani": "सीखणु", "rathwali": "सीखणु"}},
    {"garhwali": "बचाणु", "hindi": "बचाना / रक्षा करना", "english": "to save / protect / rescue", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बचाणु", "tehri": "बचाना", "salani": "बचाणु", "rathwali": "बचाणु"}},
    {"garhwali": "पकड़णु", "hindi": "पकड़ना", "english": "to catch / grasp / hold", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "पकड़णु", "tehri": "पकड़ना", "salani": "पकड़णु", "rathwali": "पकड़णु"}},
    {"garhwali": "छोड़णु", "hindi": "छोड़ना / त्यागना", "english": "to release / let go / leave", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "छोड़णु", "tehri": "छोड़ना", "salani": "छोड़णु", "rathwali": "छोड़णु"}},
    {"garhwali": "बांधणु", "hindi": "बांधना", "english": "to tie / fasten", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "बांधणु", "tehri": "बांधना", "salani": "बांधणु", "rathwali": "बांधणु"}},
    {"garhwali": "खोलणु", "hindi": "खोलना", "english": "to untie / open", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "खोलणु", "tehri": "खोलना", "salani": "खोलणु", "rathwali": "खोलणु"}},
    {"garhwali": "भरणु", "hindi": "भरना", "english": "to fill up", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "भरणु", "tehri": "भरना", "salani": "भरणु", "rathwali": "भरणु"}},
    {"garhwali": "चढ़णु", "hindi": "चढ़ना / ऊपर जाना", "english": "to climb / ascend steep slopes", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "चढ़णु", "tehri": "चढ़ना", "salani": "चढ़णु", "rathwali": "चढ़णु"}},
    {"garhwali": "उतरणु", "hindi": "उतरना / नीचे आना", "english": "to descend mountain path", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "उतरणु", "tehri": "उतरना", "salani": "उतरणु", "rathwali": "उतरणु"}},
    {"garhwali": "गिरणु", "hindi": "गिरना", "english": "to fall down", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "गिरणु", "tehri": "गिरना", "salani": "गिरणु", "rathwali": "गिरणु"}},
    {"garhwali": "संभालणु", "hindi": "संभालना / देखभाल करना", "english": "to manage / look after / take care of", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "संभालणु", "tehri": "संभालना", "salani": "संभालणु", "rathwali": "संभालणु"}},
    {"garhwali": "सुकौणु", "hindi": "धूप में सुखाना", "english": "to dry in the sun", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "सुकौणु", "tehri": "सुखाना", "salani": "सुकौणु", "rathwali": "सुकौणु"}}
]

batch3_added = 0
batch3_enriched = 0

for item in batch3_words:
    lemma = item["garhwali"].strip()
    if lemma in words_by_lemma:
        existing = words_by_lemma[lemma]
        for k, v in item.items():
            if k == "dialect_variants" and isinstance(v, dict):
                existing.setdefault("dialect_variants", {}).update(v)
            elif k not in existing or not existing[k]:
                existing[k] = v
        batch3_enriched += 1
    else:
        words_by_lemma[lemma] = item
        existing_data.append(item)
        batch3_added += 1

print(f"Batch 3 added new lemmas: {batch3_added}")
print(f"Batch 3 enriched existing: {batch3_enriched}")
print(f"Final word count in lexicon: {len(existing_data)}")

with open(words_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"Batch 3 successfully saved to {words_path}")
