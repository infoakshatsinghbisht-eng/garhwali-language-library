"""
Batch 4 expansion script: Adds words extracted from the 20 processed Garhwali songs and epics.
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

words_path = os.path.join("garhwali", "lexicon", "data", "words.json")
with open(words_path, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

print(f"Batch 4 - Pre-expansion word count: {len(existing_data)}")
words_by_lemma = {w["garhwali"].strip(): w for w in existing_data}

song_words = [
    {"garhwali": "छैला", "hindi": "प्रियतम / रूपवान युवक", "english": "beloved / charming youth", "pos": "noun", "gender": "M", "category": "people", "dialect_variants": {"srinagariya": "छैला", "tehri": "छैला", "salani": "छैला", "rathwali": "छैला"}},
    {"garhwali": "बांद", "hindi": "पहाड़ी युवती / बाला", "english": "mountain maiden / damsel", "pos": "noun", "gender": "F", "category": "people", "dialect_variants": {"srinagariya": "बांद", "tehri": "बांद", "salani": "कन्या", "rathwali": "बांद"}},
    {"garhwali": "बांसुरी", "hindi": "बांसुरी / वंशी", "english": "bamboo flute", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "बांसुरी", "tehri": "मुरली", "salani": "बांसुरी", "rathwali": "बांसुरी"}},
    {"garhwali": "नाद", "hindi": "गंभीर ध्वनि / नाद", "english": "reverberant sound / sonic vibration", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "नाद", "tehri": "नाद", "salani": "आवाज", "rathwali": "नाद"}},
    {"garhwali": "दीप", "hindi": "दीपक / लौ", "english": "ritual lamp / flame", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "दीप", "tehri": "दीया", "salani": "दीपक", "rathwali": "दीप"}},
    {"garhwali": "डोली", "hindi": "देव पालकी / डोली", "english": "palanquin of deity or bride", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "डोली", "tehri": "डोली", "salani": "पालकी", "rathwali": "डोली"}},
    {"garhwali": "मेढ़ा", "hindi": "चार सींगों वाला खाडू (मेढ़ा)", "english": "sacred four-horned ram leading Nanda Raj Jat", "pos": "noun", "gender": "M", "category": "fauna", "dialect_variants": {"srinagariya": "मेढ़ा", "tehri": "खाडू", "salani": "मेढ़ा", "rathwali": "मेढ़ा"}},
    {"garhwali": "चरण", "hindi": "पवित्र चरण / पाँव", "english": "sacred feet", "pos": "noun", "gender": "M", "category": "body", "dialect_variants": {"srinagariya": "चरण", "tehri": "पांव", "salani": "चरण", "rathwali": "चरण"}},
    {"garhwali": "सुदिन", "hindi": "शुभ दिन", "english": "auspicious holy day", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "सुदिन", "tehri": "शुभ दिन", "salani": "सुदिन", "rathwali": "सुदिन"}},
    {"garhwali": "सुहाग", "hindi": "अखंड सौभाग्य / सुहाग", "english": "marital auspiciousness and blessing", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "सुहाग", "tehri": "सुहाग", "salani": "सौभाग्य", "rathwali": "सुहाग"}},
    {"garhwali": "शहनाई", "hindi": "मांगलिक शहनाई वाद्य", "english": "shehnai (traditional wedding wind instrument)", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "शहनाई", "tehri": "शहनाई", "salani": "शहनाई", "rathwali": "शहनाई"}},
    {"garhwali": "छिल्ला", "hindi": "चीड़ की लीसादार मशाल लकड़ी", "english": "resinous pine torch splinter", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "छिल्ला", "tehri": "छिल्ला", "salani": "मशाल", "rathwali": "छिल्ला"}},
    {"garhwali": "पूड़ी", "hindi": "तेल/घी में तली पूड़ी", "english": "fried wheat flatbread", "pos": "noun", "gender": "F", "category": "food", "dialect_variants": {"srinagariya": "पूड़ी", "tehri": "पूरी", "salani": "पूड़ी", "rathwali": "पूळी"}},
    {"garhwali": "शगुन", "hindi": "शुभ शगुन", "english": "auspicious omen / blessing gift", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "शगुन", "tehri": "सगुन", "salani": "शगुन", "rathwali": "शगुन"}},
    {"garhwali": "पराक्रम", "hindi": "वीरता / पराक्रम", "english": "heroic valor and prowess", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "पराक्रम", "tehri": "बहादुरी", "salani": "पराक्रम", "rathwali": "पराक्रम"}},
    {"garhwali": "बलिदान", "hindi": "त्याग / बलिदान", "english": "supreme sacrifice", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "बलिदान", "tehri": "कुर्बानी", "salani": "बलिदान", "rathwali": "बलिदान"}},
    {"garhwali": "वास", "hindi": "निवास / वास स्थान", "english": "abode / dwelling place", "pos": "noun", "gender": "M", "category": "household", "dialect_variants": {"srinagariya": "वास", "tehri": "डेरा", "salani": "निवास", "rathwali": "वास"}},
    {"garhwali": "वंदना", "hindi": "प्रार्थना / स्तुति", "english": "devotional hymn of reverence", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "वंदना", "tehri": "स्तुति", "salani": "प्रार्थना", "rathwali": "वंदना"}},
    {"garhwali": "संकट", "hindi": "आपत्ति / विपत्ति", "english": "adversity / peril", "pos": "noun", "gender": "M", "category": "emotions", "dialect_variants": {"srinagariya": "संकट", "tehri": "मुसीबत", "salani": "संकट", "rathwali": "संकट"}},
    {"garhwali": "शरण", "hindi": "आश्रय / शरण", "english": "refuge / sanctuary", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "शरण", "tehri": "ओट", "salani": "शरण", "rathwali": "शरण"}},
    {"garhwali": "कौथिग", "hindi": "पहाड़ी मेला / उत्सव", "english": "mountain village fair / festival", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "कौथिग", "tehri": "कौथग", "salani": "मेला", "rathwali": "कौथिग"}},
    {"garhwali": "डंका", "hindi": "नगाड़े की चोट / डंका", "english": "resounding kettle-drum strike", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "डंका", "tehri": "डंका", "salani": "डंका", "rathwali": "डंका"}},
    {"garhwali": "घुंघरू", "hindi": "पैरों के घुंघरू", "english": "metallic dancing bells", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "घुंघरू", "tehri": "घुंघरू", "salani": "पाजेब", "rathwali": "घुंघरू"}},
    {"garhwali": "शिखर", "hindi": "पर्वत चोटी / शिखर", "english": "high mountain peak", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "शिखर", "tehri": "शिखर", "salani": "चोटी", "rathwali": "शिखर"}},
    {"garhwali": "सागर", "hindi": "झील / जलाशय", "english": "lake / vast water body", "pos": "noun", "gender": "M", "category": "nature", "dialect_variants": {"srinagariya": "सागर", "tehri": "सरोवर", "salani": "झील", "rathwali": "सागर"}},
    {"garhwali": "चिनहार", "hindi": "पहचान का चिह्न", "english": "mark of identity / memory landmark", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "चिनहार", "tehri": "पहचान", "salani": "निशानी", "rathwali": "चिनहार"}},
    {"garhwali": "गदा", "hindi": "भीम की गदा", "english": "war mace / weapon of Bhima", "pos": "noun", "gender": "F", "category": "tools", "dialect_variants": {"srinagariya": "गदा", "tehri": "गदा", "salani": "गदा", "rathwali": "गदा"}},
    {"garhwali": "बाण", "hindi": "तीर / बाण", "english": "arrow", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "बाण", "tehri": "तीर", "salani": "बाण", "rathwali": "बाण"}},
    {"garhwali": "धनुष", "hindi": "कमान / धनुष", "english": "archery bow", "pos": "noun", "gender": "M", "category": "tools", "dialect_variants": {"srinagariya": "धनुष", "tehri": "कमान", "salani": "धनुष", "rathwali": "धनुष"}},
    {"garhwali": "पसीना", "hindi": "परिश्रम का पसीना", "english": "sweat / honest labor", "pos": "noun", "gender": "M", "category": "body", "dialect_variants": {"srinagariya": "पसीना", "tehri": "पसीना", "salani": "पसीना", "rathwali": "पसीणा"}},
    {"garhwali": "स्वाभिमान", "hindi": "आत्मसम्मान", "english": "dignity / mountain self-respect", "pos": "noun", "gender": "M", "category": "emotions", "dialect_variants": {"srinagariya": "स्वाभिमान", "tehri": "गैरत", "salani": "सम्मान", "rathwali": "स्वाभिमान"}},
    {"garhwali": "अमृत", "hindi": "अमृत / सुधा", "english": "immortal celestial nectar", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "अमृत", "tehri": "सुधा", "salani": "अमृत", "rathwali": "अमृत"}},
    {"garhwali": "कमाई", "hindi": "मेहनत की आय", "english": "earnings / livelihood", "pos": "noun", "gender": "F", "category": "social", "dialect_variants": {"srinagariya": "कमाई", "tehri": "कमाई", "salani": "आय", "rathwali": "कमाई"}},
    {"garhwali": "निर्भय", "hindi": "निडर / भयहीन", "english": "fearless / brave", "pos": "adjective", "gender": "M", "category": "descriptors", "dialect_variants": {"srinagariya": "निर्भय", "tehri": "निडर", "salani": "बेखौफ", "rathwali": "निर्भय"}},
    {"garhwali": "चौंफुला", "hindi": "बसंत का चौंफुला लोकनृत्य", "english": "classical celebratory spring folk dance", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "चौंफुला", "tehri": "चौंफुला", "salani": "नृत्य", "rathwali": "चौंफुला"}},
    {"garhwali": "थड्या", "hindi": "आंगन का थड्या भक्ति नृत्य", "english": "traditional courtyard devotional community dance", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "थड्या", "tehri": "थड्या", "salani": "थड्या", "rathwali": "थड्या"}},
    {"garhwali": "गौंत", "hindi": "गोमूत्र (पवित्र शोधक)", "english": "sacred cow urine used in ritual purification", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "गौंत", "tehri": "गौंत", "salani": "गोमूत्र", "rathwali": "गौंत"}},
    {"garhwali": "गोबर", "hindi": "गाय का गोबर (आंगन लीपने हेतु)", "english": "cowdung used to wash courtyards and hearths", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "गोबर", "tehri": "गोबर", "salani": "गोबर", "rathwali": "गोबर"}},
    {"garhwali": "लीपणा", "hindi": "गोबर-मिट्टी से आंगन लीपना", "english": "to wash and purify floor with clay and cowdung", "pos": "verb", "gender": "N", "category": "actions", "dialect_variants": {"srinagariya": "लीपणा", "tehri": "लीपना", "salani": "लीपणा", "rathwali": "लीपणा"}},
    {"garhwali": "छींटा", "hindi": "गंगाजल का पवित्र छींटा", "english": "sprinkling holy water for purification", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "छींटा", "tehri": "छींटा", "salani": "छिड़काव", "rathwali": "छींटा"}},
    {"garhwali": "जातरा", "hindi": "धार्मिक तीर्थयात्रा", "english": "religious pilgrimage procession", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "जातरा", "tehri": "यात्रा", "salani": "जातरा", "rathwali": "जातरा"}},
    {"garhwali": "धियान", "hindi": "एकाग्रता / ध्यान", "english": "deep concentration / meditation", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "धियान", "tehri": "ध्यान", "salani": "मन", "rathwali": "धियान"}},
    {"garhwali": "आशीर्वाद", "hindi": "बुजुर्गों का आशीर्वाद", "english": "blessing / benediction from elders", "pos": "noun", "gender": "M", "category": "culture", "dialect_variants": {"srinagariya": "आशीर्वाद", "tehri": "आसीस", "salani": "आशीर्वाद", "rathwali": "असीस"}},
    {"garhwali": "असीस", "hindi": "मातृक आशीर्वाद", "english": "maternal blessing and well-wishes", "pos": "noun", "gender": "F", "category": "culture", "dialect_variants": {"srinagariya": "असीस", "tehri": "आशीष", "salani": "दुआ", "rathwali": "असीस"}},
    {"garhwali": "नेग", "hindi": "मांगलिक उत्सव का पारंपरिक उपहार", "english": "customary ceremonial token gift/money given to relations", "pos": "noun", "gender": "M", "category": "wedding", "dialect_variants": {"srinagariya": "नेग", "tehri": "नेग", "salani": "न्यौता", "rathwali": "नेग"}},
    {"garhwali": "न्यौता", "hindi": "विवाह या भोज का निमंत्रण", "english": "invitation to marriage or feast", "pos": "noun", "gender": "M", "category": "wedding", "dialect_variants": {"srinagariya": "न्यौता", "tehri": "नेवता", "salani": "निमंत्रण", "rathwali": "न्यौता"}}
]

batch4_added = 0
batch4_enriched = 0

for item in song_words:
    lemma = item["garhwali"].strip()
    if lemma in words_by_lemma:
        existing = words_by_lemma[lemma]
        for k, v in item.items():
            if k == "dialect_variants" and isinstance(v, dict):
                existing.setdefault("dialect_variants", {}).update(v)
            elif k not in existing or not existing[k]:
                existing[k] = v
        batch4_enriched += 1
    else:
        words_by_lemma[lemma] = item
        existing_data.append(item)
        batch4_added += 1

print(f"Batch 4 added new lemmas: {batch4_added}")
print(f"Batch 4 enriched existing: {batch4_enriched}")
print(f"Final word count: {len(existing_data)}")

with open(words_path, "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print(f"Batch 4 successfully saved to {words_path}")
