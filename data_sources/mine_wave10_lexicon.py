# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 10 vocabulary from newly added texts:
- Swami Prabodhanand (1961): Across Gangotri Glaciers (Gaumukh, Bhagirathi, Shivling, ice caves)
- Shiv Kumar Painuli et al. (2000): Shri Nanda Devi Raj Jat (Khadu, Chhantoli, Roopkund, Homkund, Nauti)
- Eric Shipton (1936 & 1935): Nanda Devi & Ganges Watershed (Rishi Ganga gorge, Trisul, high cols, arêtes)
- Zoological Survey of India (1997): Fauna of Nanda Devi Biosphere (Bharal, Monal, Danphe, snow leopard)
- K. S. Negi et al. (1985): Flora of Khatling Glacier, Tehri Garhwal (Bhilangna, Jambu, Gandrani, Dolu)
"""

import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE10_WORDS = [
    # --- Nanda Devi Raj Jat Sacred Pilgrimage & Alpine Topography (Painuli et al. 2000) ---
    {
        "garhwali": "चारसींग्या-खाडू",
        "hindi": "नंदा देवी राजजात यात्रा का नेतृत्व करने वाला चार सींगों वाला पवित्र मेढ़ा जो कांसुवा से होमकुंड तक जाता है",
        "english": "sacred four-horned ram born in Garhwal that leads the 280-km Nanda Devi Raj Jat royal pilgrimage to Homkund",
        "pos": "noun",
        "gender": "M",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "चारसींग्या-खाडू", "tehri": "चारसींग्या-खाडू", "salani": "चारसींग्या-खाडू", "rathwali": "चारसींग्या-खाडू"}
    },
    {
        "garhwali": "खाडू",
        "hindi": "पहाड़ी भेड़ा या मेढ़ा, विशेष रूप से देवी नंदा के वाहन और अग्रदूत रूप में पूज्य",
        "english": "mountain ram or sheep, specifically revered as the herald and divine vehicle of Goddess Nanda",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "खाडू", "tehri": "खाडू", "salani": "खाडू", "rathwali": "खाडू"}
    },
    {
        "garhwali": "होमकुंड",
        "hindi": "चमोली गढ़वाल में 16,000 फीट की ऊंचाई पर स्थित वह पवित्र हिमानी ताल जहां नंदा राजजात की अंतिम पूजा होती है",
        "english": "Homkund, sacred high alpine glacial tarn (16,000 ft) at the base of Trishul and Nandaghunti where the Raj Jat concludes",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "होमकुंड", "tehri": "होमकुण्ड", "salani": "होमकुंड", "rathwali": "होमकुंड"}
    },
    {
        "garhwali": "रूपकुंड",
        "hindi": "त्रिशूल पर्वत के नीचे 15,700 फीट पर स्थित रहस्यमयी कंकाल झील जहां प्राचीन राजा यशधवल और उनकी सेना के कंकाल मिलते हैं",
        "english": "Roopkund, the enigmatic high-altitude glacial skeleton lake nestled beneath Mount Trishul in Chamoli Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "रूपकुंड", "tehri": "रूपकुण्ड", "salani": "रूपकुंड", "rathwali": "रूपकुंड"}
    },
    {
        "garhwali": "नौटी",
        "hindi": "कर्णप्रयाग के निकट स्थित नौटी गांव जहां नंदा देवी का मूल मंदिर है और जहां से राजजात विधिवत प्रारंभ होती है",
        "english": "Nauti, historical village in Chamoli Garhwal housing the ancestral temple of Goddess Nanda whence the Raj Jat departs",
        "pos": "noun",
        "gender": "M",
        "category": "places",
        "dialect_variants": {"srinagariya": "नौटी", "tehri": "नौटी", "salani": "नौटी", "rathwali": "नौटी"}
    },
    {
        "garhwali": "कांसुवा",
        "hindi": "चांदपुर गढ़ी के निकट गढ़वाल के पंवार वंशीय कुंवरों का गांव जहां से चार सींगों वाला खाडू यात्रा में शामिल होता है",
        "english": "Kansuwa, ancestral village seat of the royal Kunwar princes of Garhwal who sponsor the four-horned ram",
        "pos": "noun",
        "gender": "M",
        "category": "places",
        "dialect_variants": {"srinagariya": "कांसुवा", "tehri": "कांसुवा", "salani": "कांसुवा", "rathwali": "कांसुवा"}
    },
    {
        "garhwali": "जागिया",
        "hindi": "नंदा देवी एवं स्थानीय देवताओं के पौराणिक जागर गाने वाला पारंपरिक ब्राह्मण अथवा औजी गायक",
        "english": "traditional bard or ritual master singer who intones the sacred oral epics and genealogies during Himalayan Jagars",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "जागिया", "tehri": "जागिया", "salani": "जागिया", "rathwali": "जागिया"}
    },
    {
        "garhwali": "धुणी-पानी",
        "hindi": "पहाड़ी पड़ावों और तीर्थ यात्राओं में मिलने वाला चूल्हे का आश्रय एवं पीने का जल",
        "english": "warmth and drink hospitality (hearthfire and pure mountain spring water) provided to travelers in high camps",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "धुणी-पानी", "tehri": "धुणी-पाणी", "salani": "धुणी-पानी", "rathwali": "धुणी-पानी"}
    },
    {
        "garhwali": "डोलिया",
        "hindi": "देवी नंदा की स्वर्ण-मूर्त को ले जाने वाली सजी हुई पवित्र पालकी",
        "english": "ornate wooden palanquin carrying the golden idol of Goddess Nanda shoulder-borne across alpine passes",
        "pos": "noun",
        "gender": "F",
        "category": "rituals",
        "dialect_variants": {"srinagariya": "डोलिया", "tehri": "डोळिया", "salani": "डोलिया", "rathwali": "डोलिया"}
    },
    {
        "garhwali": "बैतरणी",
        "hindi": "होमकुंड के मार्ग पर स्थित पवित्र अल्पाइन हिमानी ताल जहां मोक्ष हेतु नंदा देवी यात्री पिंडदान करते हैं",
        "english": "Baitarani, high-altitude tarn near Homkund where pilgrims offer symbolic oblations for ancestral passage to heaven",
        "pos": "noun",
        "gender": "F",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "बैतरणी", "tehri": "बैतरणी", "salani": "बैतरणी", "rathwali": "बैतरणी"}
    },
    {
        "garhwali": "शिला-समुद्र",
        "hindi": "रूपकुंड और होमकुंड के बीच पत्थरों और विशाल हिमानी शिलाखंडों से पटा हुआ विस्तृत क्षेत्र",
        "english": "Shila-Samudra ('Ocean of Boulders'), a vast glacial debris basin carpeted in massive granite blocks",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "शिला-समुद्र", "tehri": "शिळा-समुद्र", "salani": "शिला-समुद्र", "rathwali": "शिला-समुद्र"}
    },
    {
        "garhwali": "पातर-नचौणिया",
        "hindi": "रूपकुंड मार्ग पर 13,000 फीट पर स्थित वह स्थल जहां लोक मान्यतानुसार कन्नौज के राजा की नर्तकियों को पत्थर में बदल दिया गया था",
        "english": "Patar-Nachauniya, high ridge flat where according to folk legend the dancing girls of King Jasdhawal were petrified",
        "pos": "noun",
        "gender": "M",
        "category": "folklore",
        "dialect_variants": {"srinagariya": "पातर-नचौणिया", "tehri": "पातर-नचौणिया", "salani": "पातर-नचौणिया", "rathwali": "पातर-नचौणिया"}
    },

    # --- Nanda Devi Sanctuary, Rishi Gorge & Peaks (Shipton 1935, 1936) ---
    {
        "garhwali": "ऋषिगंगा",
        "hindi": "नंदा देवी के भीतरी अभयारण्य से अत्यधिक संकरे और अगम्य महाखड्ड को चीरती हुई बहने वाली प्रचंड नदी",
        "english": "Rishi Ganga, the torrential river that cuts through a virtually impassable canyon draining the inner Nanda Devi sanctuary",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "ऋषिगंगा", "tehri": "ऋषिगंगा", "salani": "ऋषिगंगा", "rathwali": "ऋषिगंगा"}
    },
    {
        "garhwali": "त्रिशूल",
        "hindi": "गढ़वाल हिमालय का 7,120 मीटर ऊंचा विख्यात त्रिकोणीय हिमशिखर जो शिव के त्रिशूल सदृश दिखाई देता है",
        "english": "Trisul (7,120 m), the iconic triple-peaked massif of Garhwal resembling the sacred trident of Lord Shiva",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "त्रिशूल", "tehri": "त्रिशूळ", "salani": "त्रिशूल", "rathwali": "त्रिशूल"}
    },
    {
        "garhwali": "द्रोणागिरि",
        "hindi": "चमोली जिले में स्थित ऐतिहासिक पर्वत एवं गांव जहां से लक्ष्मण मूर्छा में संजीवनी बूटी लाने की लोककथा जुड़ी है",
        "english": "Dronagiri, sacred mountain peak and historic highland village in Chamoli Garhwal famed in Ramayana folklore for Sanjivani herb",
        "pos": "noun",
        "gender": "M",
        "category": "places",
        "dialect_variants": {"srinagariya": "द्रोणागिरि", "tehri": "द्रोणागिरि", "salani": "द्रोणागिरि", "rathwali": "द्रोणागिरि"}
    },
    {
        "garhwali": "गड्डे",
        "hindi": "पहाड़ी चट्टानों के नीचे प्राकृतिक रूप से बनी गुफा या ओट जहां चरवाहे और कुली रात बिताते हैं",
        "english": "natural rock shelter or dry overhang beneath Himalayan cliff faces used by porters and shepherds for bivouacs",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "गड्डे", "tehri": "गड्डा", "salani": "गड्डा", "rathwali": "गड्डे"}
    },
    {
        "garhwali": "धारदार",
        "hindi": "तीखे और धारदार चट्टानी कटक या पर्वत श्रेणी",
        "english": "knife-edged arête or serrated rocky mountain ridge-line",
        "pos": "adjective",
        "gender": "None",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "धारदार", "tehri": "धारदार", "salani": "धारदार", "rathwali": "धारदार"}
    },
    {
        "garhwali": "कड़ा",
        "hindi": "सीधी खड़ी एवं दुर्गम चट्टानी दीवार अथवा कगार",
        "english": "sheer vertical rock precipice or towering mountain scarp",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "कड़ा", "tehri": "कड़ा", "salani": "कडा", "rathwali": "कड़ा"}
    },
    {
        "garhwali": "बर्फानी-तूफान",
        "hindi": "ऊंचे शिखरों पर चलने वाली बर्फीली और भयानक आंधी",
        "english": "severe Himalayan blizzard or high-altitude blinding snow gale",
        "pos": "noun",
        "gender": "M",
        "category": "weather",
        "dialect_variants": {"srinagariya": "बर्फानी-तूफान", "tehri": "बर्फानी-तूफान", "salani": "बर्फानी-तूफान", "rathwali": "बर्फानी-तूफान"}
    },
    {
        "garhwali": "घाटीदार",
        "hindi": "गहरी घाटियों और खाइयों से युक्त पर्वतीय भूभाग",
        "english": "ravine-intersected or deeply furrowed mountain valley terrain",
        "pos": "adjective",
        "gender": "None",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "घाटीदार", "tehri": "घाटीदार", "salani": "घाटीदार", "rathwali": "घाटीदार"}
    },

    # --- High Himalayan Wildlife & Avifauna (ZSI 1997) ---
    {
        "garhwali": "भरल",
        "hindi": "अल्पाइन बुग्यालों और नंदा देवी की चट्टानों पर चरने वाली नीली जंगली भेड़ (Pseudois nayaur)",
        "english": "Bharal or Himalayan blue sheep (Pseudois nayaur) dwelling on steep alpine cliffs above the tree-line",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "भरल", "tehri": "भरळ", "salani": "भरल", "rathwali": "भरल"}
    },
    {
        "garhwali": "मुनाल",
        "hindi": "उत्तराखंड का राज्य पक्षी, सतरंगी चमकीले पंखों वाला हिमालयी तीतर (Lophophorus impejanus)",
        "english": "Himalayan Monal (Lophophorus impejanus), the iridescent rainbow-plumaged state bird of Uttarakhand",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "मुनाल", "tehri": "मुनाळ", "salani": "मुनाल", "rathwali": "मुनाल"}
    },
    {
        "garhwali": "डांफे",
        "hindi": "मुनाल प्रजाति का नर पक्षी जो वसंत ऋतु में उच्च हिमालयी वनों में कूकता है",
        "english": "Danphe, native vernacular name for the resplendent male Himalayan Monal pheasant",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "डांफे", "tehri": "डांफे", "salani": "डांफे", "rathwali": "डांफे"}
    },
    {
        "garhwali": "फिउं",
        "hindi": "उच्च अल्पाइन मोरेन में बिल बनाकर रहने वाला पीले रोएं वाला पहाड़ी चूहा या मारमोट (Himalayan Marmot)",
        "english": "golden Himalayan marmot (Marmota himalayana) whistling on high screes and glacial moraines",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "फिउं", "tehri": "फिउं", "salani": "फिउं", "rathwali": "फिउं"}
    },
    {
        "garhwali": "हिम-तेंदुआ",
        "hindi": "गढ़वाल के उच्च शिखरों और नंदा देवी अभयारण्य का मायावी शिकारी बर्फीला तेंदुआ (Panthera uncia)",
        "english": "snow leopard (Panthera uncia), apex phantom predator stalker of high Garhwal alpine crags",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "हिम-तेंदुआ", "tehri": "हिम-तेन्दुवा", "salani": "हिम-तेंदुआ", "rathwali": "हिम-तेंदुआ"}
    },
    {
        "garhwali": "कालो-भालू",
        "hindi": "गढ़वाल के बांज और बुरांश वनों में घूमने वाला एशियाई काला रीछ (Ursus thibetanus)",
        "english": "Asiatic black bear (Ursus thibetanus) inhabiting temperate oak and rhododendron forest belts of Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "कालो-भालू", "tehri": "कालो-भाळू", "salani": "कालो-भालू", "rathwali": "कालो-भालू"}
    },
    {
        "garhwali": "हिम-कुकुड़",
        "hindi": "अत्यधिक ऊंचाई की चट्टानों पर रहने वाला बड़ा जंगली हिमालयी पक्षी (Himalayan Snowcock)",
        "english": "Himalayan snowcock (Tetraogallus himalayensis) foraging in small flocks along windswept alpine ridgelines",
        "pos": "noun",
        "gender": "M",
        "category": "animals",
        "dialect_variants": {"srinagariya": "हिम-कुकुड़", "tehri": "हिम-कुकुड", "salani": "हिम-कुकुड", "rathwali": "हिम-कुकुड़"}
    },
    {
        "garhwali": "लाल-लोमड़ी",
        "hindi": "अल्पाइन चरागाहों में खरगोश और चूहों का शिकार करने वाली घने बालों वाली पहाड़ी लोमड़ी",
        "english": "Himalayan red fox (Vulpes vulpes montana) sporting thick fur across sub-alpine scrub and moraines",
        "pos": "noun",
        "gender": "F",
        "category": "animals",
        "dialect_variants": {"srinagariya": "लाल-लोमड़ी", "tehri": "लाल-लोमडी", "salani": "लाल-लोमडी", "rathwali": "लाल-लोमड़ी"}
    },

    # --- Khatling Glacier Ethnobotany & Alpine Flora (Negi & Gaur 1985) ---
    {
        "garhwali": "भिलंगना",
        "hindi": "टिहरी गढ़वाल के खतलिंग हिमनद से निकलने वाली पवित्र पहाड़ी नदी जो पुरानी टिहरी में भागीरथी से मिलती थी",
        "english": "Bhilangna River, sacred glacial river born at Khatling Glacier in Tehri Garhwal",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "भिलंगना", "tehri": "भिळंगणा", "salani": "भिलंगना", "rathwali": "भिलंगना"}
    },
    {
        "garhwali": "खतलिंग",
        "hindi": "टिहरी गढ़वाल में स्थित विशाल हिमनद जो भिलंगना नदी का उद्गम स्थल है",
        "english": "Khatling Glacier, extensive lateral ice field in Tehri Garhwal and cradle of the Bhilangna stream",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "खतलिंग", "tehri": "खतलिंग", "salani": "खतलिंग", "rathwali": "खतलिंग"}
    },
    {
        "garhwali": "जम्बू",
        "hindi": "अल्पाइन बुग्यालों में उगने वाली तीखी सुगंधित जंगली घास (Allium stracheyi) जिसे दाल में छौंक लगाने में प्रयोग करते हैं",
        "english": "Jambu (Allium stracheyi), pungent high-altitude Himalayan wild chive prized as a culinary seasoning",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "जम्बू", "tehri": "जम्बू", "salani": "जम्बू", "rathwali": "जम्बू"}
    },
    {
        "garhwali": "गंद्राणी",
        "hindi": "उच्च अल्पाइन ढलानों पर मिलने वाली पाचक एवं वातनाशक औषधीय जड़ (Angelica glauca)",
        "english": "Gandrani (Angelica glauca), aromatic medicinal root gathered on alpine crags for gastric disorders and spices",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "गंद्राणी", "tehri": "गंदराणी", "salani": "गंद्राणी", "rathwali": "गंद्राणी"}
    },
    {
        "garhwali": "धूप-लकड़ी",
        "hindi": "अल्पाइन चट्टानों पर उगने वाली सुगंधित जड़ी (Jurinea macrocephala) जिसकी जड़ों से मंदिरों हेतु पावन धूप बनाई जाती है",
        "english": "Dhup-Lakri (Jurinea macrocephala), fragrant thistle root gathered above 12,000 ft to compound temple incense",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "धूप-लकड़ी", "tehri": "धूप-लकडी", "salani": "धूप-लकडी", "rathwali": "धूप-लकड़ी"}
    },
    {
        "garhwali": "मासी",
        "hindi": "चट्टानों की संधियों में उगने वाली अत्यंत सुवासित औषधीय वनस्पति (Nardostachys jatamansi / जटामासी)",
        "english": "Masi / Jatamansi (Nardostachys jatamansi), aromatic alpine spikenard root esteemed in Ayurvedic herbalism for calming the mind",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "मासी", "tehri": "मासी", "salani": "मासी", "rathwali": "मासी"}
    },
    {
        "garhwali": "डोलू",
        "hindi": "उच्च हिमालयी ढलानों पर उगने वाला औषधीय जंगली रेवंदचीनी का पौधा (Rheum australe)",
        "english": "Dolu (Rheum australe), Himalayan wild rhubarb yielding deep crimson healing roots for sprains and wounds",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "डोलू", "tehri": "डोळू", "salani": "डोलू", "rathwali": "डोलू"}
    },
    {
        "garhwali": "सलामपंजा",
        "hindi": "हाथ के पंजे जैसी दिखने वाली अत्यंत बलवर्धक दुर्लभ अल्पाइन कंद-मूल (Dactylorhiza hatagirea)",
        "english": "Salampanja (Dactylorhiza hatagirea), rare palmate marsh orchid with digit-like tubers prized as a restorative tonic",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "सलामपंजा", "tehri": "सळामपंजा", "salani": "सलामपंजा", "rathwali": "सलामपंजा"}
    },

    # --- Gangotri Glacial Topography & Sanctuaries (Prabodhanand 1961) ---
    {
        "garhwali": "गौमुख",
        "hindi": "गंगोत्री हिमनद के मुहाने पर गाय के मुख सदृश हिम-गुफा जहां से पवित्र भागीरथी गंगा निकलती है",
        "english": "Gaumukh ('Cow's Snout'), the dramatic ice terminus cave of Gangotri Glacier where the Bhagirathi River originates",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "गौमुख", "tehri": "गौमुख", "salani": "गौमुख", "rathwali": "गौमुख"}
    },
    {
        "garhwali": "भागीरथी",
        "hindi": "गौमुख से निकलकर देवप्रयाग में अलकनंदा से मिलकर गंगा बनने वाली गढ़वाल की प्रमुख पवित्र नदी",
        "english": "Bhagirathi, sacred headstream of the Ganges coursing from Gaumukh through Uttarkashi and Tehri to Devprayag",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "भागीरथी", "tehri": "भागीरथी", "salani": "भागीरथी", "rathwali": "भागीरथी"}
    },
    {
        "garhwali": "शिवलिंग",
        "hindi": "गंगोत्री हिमनद के ऊपर तपोवन के पार्श्व में स्थित 6,543 मीटर ऊंचा अत्यंत सुंदर पिरामिड हिमशिखर",
        "english": "Mount Shivling (6,543 m), stunning pyramid spire dominating the Gangotri glacier amphitheatre above Tapovan",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "शिवलिंग", "tehri": "शिवलिंग", "salani": "शिवलिंग", "rathwali": "शिवलिंग"}
    },
    {
        "garhwali": "तपोवन",
        "hindi": "गंगोत्री हिमनद के पार 14,600 फीट पर स्थित वह पावन अल्पाइन बुग्याल जहां प्राचीन काल से संन्यासी ध्यान लगाते हैं",
        "english": "Tapovan, sacred high meadow terrace (14,600 ft) fronting Mount Shivling frequented by ascetic hermits",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "तपोवन", "tehri": "तपोवण", "salani": "तपोवन", "rathwali": "तपोवन"}
    }
]

added_count = 0
for w in WAVE10_WORDS:
    lemma = w["garhwali"]
    if lemma not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(lemma)
        added_count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} words from Wave 10. Total words in library: {len(existing_words)}.")
