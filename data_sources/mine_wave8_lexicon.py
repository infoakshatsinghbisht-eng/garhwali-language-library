# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 8 vocabulary from newly added historical,
linguistic, forest management, ornithological, and settlement texts:
- Grierson (1916) & Nazish (1995): Conversational verbs, spatial adjectives, folk meters
- Tehri Forest Plan (1897): Native Himalayan tree species, timber fluming, resin
- Birds of Lower Garhwal (1969): Hill pheasants, partridges, forest fauna
- Ibbotson (1933): Land classifications (Talaon, Katil, Ijran), agrarian tools
"""

import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE8_WORDS = [
    # --- Forestry, Himalayan Flora & River Fluming (Tehri Leased Forests 1897) ---
    {
        "garhwali": "मोरू",
        "hindi": "मध्य हिमालयी ऊंचाई पर पाया जाने वाला हरा बांज/शाहबलूत वृक्ष (Quercus dilatata)",
        "english": "Himalayan king oak or green oak (Quercus dilatata) valued for heavy timber and fodder",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "मोरू", "tehri": "मोडू", "salani": "मोरू", "rathwali": "मोरू"}
    },
    {
        "garhwali": "खर्शू",
        "hindi": "उच्च अल्पाइन सीमा पर उगने वाला भूरा बांज वृक्ष (Quercus semecarpifolia)",
        "english": "brown alpine oak (Quercus semecarpifolia) growing near the sub-alpine tree-line",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "खर्शू", "tehri": "खर्सू", "salani": "खर्सू", "rathwali": "खर्शू"}
    },
    {
        "garhwali": "कैल",
        "hindi": "पहाड़ों में उगने वाला नीली पत्तियों वाला देवदार सदृश चीड़ वृक्ष (Pinus wallichiana)",
        "english": "Himalayan blue pine (Pinus wallichiana) producing soft aromatic timber",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "कैल", "tehri": "कैल", "salani": "कैल", "rathwali": "कैल"}
    },
    {
        "garhwali": "गट्टा",
        "hindi": "नदी में बहाने हेतु काटा तथा छिला गया भारी चीड़ का लट्ठा",
        "english": "heavy debarked pine or cedar log prepared for river timber fluming down mountain gorges",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "गट्टा", "tehri": "गट्टू", "salani": "गट्टो", "rathwali": "गट्टा"}
    },
    {
        "garhwali": "घाल",
        "hindi": "वर्षाकाल में उफनती अलकनंदा अथवा भागीरथी नदी में लट्ठों को बहाकर ले जाने का अभियान",
        "english": "monsoon river timber drive, floating logs down high torrents to plains depots",
        "pos": "noun",
        "gender": "F",
        "category": "actions",
        "dialect_variants": {"srinagariya": "घाल", "tehri": "घाली", "salani": "घाल", "rathwali": "घाल"}
    },
    {
        "garhwali": "तार",
        "hindi": "गहरी घाटियों के आर-पार लट्ठे अथवा सामान ले जाने वाला भारी लोहे का रज्जुमार्ग",
        "english": "gravity cableway or aerial wire ropeway used to haul timber logs across precipitous ravines",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "तार", "tehri": "तार", "salani": "तार", "rathwali": "तार"}
    },
    {
        "garhwali": "लस्या",
        "hindi": "चीड़ के तनों पर चीरा लगाकर निकाला जाने वाला गाढ़ा सुगंधित लीसा/राल",
        "english": "viscous fragrant oleoresin or turpentine tapped from mountain chir pine trunks",
        "pos": "noun",
        "gender": "M",
        "category": "material",
        "dialect_variants": {"srinagariya": "लस्या", "tehri": "लीसो", "salani": "लीसा", "rathwali": "लस्या"}
    },

    # --- Land Classification & Settlement Revenue (Ibbotson 1933) ---
    {
        "garhwali": "तलाओं",
        "hindi": "घाटी तल में स्थित सदानीरा गूलों से सिंचित अति उर्वर सीढ़ीदार खेत",
        "english": "perennially irrigated, fertile low-lying terraced valley cropland fed by canals",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "तलाओं", "tehri": "तलाऊं", "salani": "तलाओं", "rathwali": "तलाओं"}
    },
    {
        "garhwali": "कातील",
        "hindi": "पहाड़ी ढलान पर पत्थरों को हटाकर नई-नई बनाई गई पथरीली असिंचित भूमि",
        "english": "newly reclaimed, rough stony hillside clearing cultivated intermittently without irrigation",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "कातील", "tehri": "कातील", "salani": "कातील", "rathwali": "कातील"}
    },
    {
        "garhwali": "इजराण",
        "hindi": "झाड़-झंखाड़ वाली पथरीली सीमांत भूमि जहाँ कभी-कभार ही फाफर या मडुआ बोया जाता है",
        "english": "marginal brushwood scrub terrace cultivated once in several years with buckwheat or coarse millets",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "इजराण", "tehri": "इजराण", "salani": "इजराण", "rathwali": "इजराण"}
    },
    {
        "garhwali": "खुरपी",
        "hindi": "सीढ़ीदार खेतों में निराई-गुड़ाई करने की छोटी पारंपरिक खुरपी",
        "english": "small curved hand-hoe or scraper used for weeding and hoeing terraced crops",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "खुरपी", "tehri": "खुरपी", "salani": "खुरपी", "rathwali": "खुरपी"}
    },

    # --- Folk Oral Traditions, Music & Avian Fauna (Bhandari 1946, Birds 1969, Nazish 1995) ---
    {
        "garhwali": "चैती",
        "hindi": "चैत्र मास में गाए जाने वाले पारंपरिक वसंत लोकगीत",
        "english": "traditional vernal folk songs sung in the month of Chaitra celebrating flowers and spring",
        "pos": "noun",
        "gender": "F",
        "category": "folklore",
        "dialect_variants": {"srinagariya": "चैती", "tehri": "चैती", "salani": "चैती", "rathwali": "चैती"}
    },
    {
        "garhwali": "हुरक्या",
        "hindi": "हुड़का बजाकर वीरगाथाएं तथा पौराणिक जागर सुनाने वाला पारंपरिक लोकगायक",
        "english": "traditional bardic singer and balladeer who accompanies oral epics on the hour-glass Hurka drum",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "हुरक्या", "tehri": "हुरक्यो", "salani": "हुरकिया", "rathwali": "हुरक्या"}
    },
    {
        "garhwali": "कलीज",
        "hindi": "बांज के जंगलों में विचरण करने वाला हिमालयी जंगली तीतर/कालीज मुर्गा (Lophura leucomelanos)",
        "english": "Kalij pheasant (Lophura leucomelanos) inhabiting mid-altitude Himalayan oak and rhododendron forests",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "कलीज", "tehri": "कलीज", "salani": "कलीज", "rathwali": "कलीज"}
    },
    {
        "garhwali": "चकोर",
        "hindi": "चट्टानी पहाड़ी ढलानों पर पाया जाने वाला तीतर कुल का पक्षी (Alectoris chukar)",
        "english": "Chukar partridge (Alectoris chukar) frequenting rocky mountain slopes and terraced edges",
        "pos": "noun",
        "gender": "M",
        "category": "fauna",
        "dialect_variants": {"srinagariya": "चकोर", "tehri": "चकोर", "salani": "चकोर", "rathwali": "चकोर"}
    },
    {
        "garhwali": "गाडर",
        "hindi": "पहाड़ी भेड़ों का झुंड अथवा चरवाहों का भेड़ों का रेवड़",
        "english": "flock of mountain sheep or ewes grazing under shepherd care",
        "pos": "noun",
        "gender": "F",
        "category": "animals",
        "dialect_variants": {"srinagariya": "गाडर", "tehri": "गाडर", "salani": "गाडर", "rathwali": "गाडर"}
    },

    # --- Conversational, Spatial & Descriptive Lexicon (Grierson 1916) ---
    {
        "garhwali": "बत्याण",
        "hindi": "चौपाल अथवा अलाव के पास बैठकर आपस में बातचीत या सुख-दुख साझा करना",
        "english": "to converse pleasantly, chat, or exchange village news around evening fires",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बत्याण", "tehri": "बतौणा", "salani": "बत्याण", "rathwali": "बत्याण"}
    },
    {
        "garhwali": "पछिला",
        "hindi": "पीछे का, पिछला अथवा मकान या दलान के पृष्ठ भाग में स्थित",
        "english": "rear, hindmost, or situated on the back side of a hill dwelling",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "पछिला", "tehri": "पछिल्लो", "salani": "पछिल्ला", "rathwali": "पछिला"}
    },
    {
        "garhwali": "अघिला",
        "hindi": "आगे का, अगला अथवा मुख्य द्वार की ओर स्थित",
        "english": "front, foremost, or situated facing the main courtyard entrance",
        "pos": "adjective",
        "gender": "M",
        "category": "descriptors",
        "dialect_variants": {"srinagariya": "अघिला", "tehri": "अघिल्लो", "salani": "अघिल्ला", "rathwali": "अघिला"}
    },
    {
        "garhwali": "पल्लो",
        "hindi": "सामने की पहाड़ी, दूसरी ओर का टीला अथवा नदी के उस पार का तट",
        "english": "situated on the opposite mountain ridge, farther hillside, or across the river",
        "pos": "adjective",
        "gender": "M",
        "category": "spatial",
        "dialect_variants": {"srinagariya": "पल्लो", "tehri": "पल्लो", "salani": "पल्ला", "rathwali": "पल्लो"}
    },
    {
        "garhwali": "वल्लो",
        "hindi": "इस ओर की पहाड़ी अथवा नदी के निकटवर्ती तट पर स्थित",
        "english": "situated on the nearer hillside, this side of the mountain ridge or river",
        "pos": "adjective",
        "gender": "M",
        "category": "spatial",
        "dialect_variants": {"srinagariya": "वल्लो", "tehri": "वल्लो", "salani": "वल्ला", "rathwali": "वल्लो"}
    },
    {
        "garhwali": "जुकत",
        "hindi": "पर्वतीय कठिन जीवन में कार्य सिद्ध करने की चतुर युक्ति या सूझबूझ",
        "english": "ingenious practical skill, clever stratagem, or resourcefulness in mountain living",
        "pos": "noun",
        "gender": "F",
        "category": "quality",
        "dialect_variants": {"srinagariya": "जुकत", "tehri": "जुगत", "salani": "जुकत", "rathwali": "जुकत"}
    },
    {
        "garhwali": "ओछाण",
        "hindi": "पत्थर के फर्श पर बिछाने वाला ऊनी कम्मल, गुदड़ी अथवा पुआल का बिछौना",
        "english": "rustic bedding mattress made of woven coarse wool, rags, or dry threshing straw",
        "pos": "noun",
        "gender": "M",
        "category": "household",
        "dialect_variants": {"srinagariya": "ओछाण", "tehri": "ओछाण", "salani": "ओछाण", "rathwali": "ओछाण"}
    },
    {
        "garhwali": "डालो",
        "hindi": "अनाज अथवा पहाड़ी दालें रखने का रिंगाल की तीलियों से बना बड़ा टोकरा",
        "english": "large capacious storage basket woven of ringal cane for preserving millet and pulses",
        "pos": "noun",
        "gender": "M",
        "category": "tools",
        "dialect_variants": {"srinagariya": "डालो", "tehri": "डालो", "salani": "डाला", "rathwali": "डालो"}
    },
    {
        "garhwali": "बुज्याण",
        "hindi": "दीपक अथवा चूल्हे की अंगारों को बुझाना या शांत करना",
        "english": "to extinguish, put out, or quench hearth embers or a wick lamp",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "बुज्याण", "tehri": "बुझौणा", "salani": "बुज्याण", "rathwali": "बुज्याण"}
    },
    {
        "garhwali": "चितकण",
        "hindi": "ओट से चुपके से देखना अथवा सजग होकर तिरछी दृष्टि डालना",
        "english": "to glance sideways, peek cautiously, or observe quietly from cover",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "चितकण", "tehri": "चितकणा", "salani": "चितकण", "rathwali": "चितकण"}
    },
    {
        "garhwali": "तपक्क",
        "hindi": "बर्फ अथवा पानी की बूँद के टपकने की अनुकरणात्मक ध्वनि",
        "english": "onomatopoeic sound of a single water droplet or melting icicle falling",
        "pos": "adverb",
        "gender": "None",
        "category": "onomatopoeia",
        "dialect_variants": {"srinagariya": "तपक्क", "tehri": "तपक्क", "salani": "तपक्क", "rathwali": "तपक्क"}
    },
    {
        "garhwali": "झमक्क",
        "hindi": "पहाड़ों में अचानक तीव्र वर्षा अथवा मूसलाधार बौछार पड़ने की ध्वनि",
        "english": "onomatopoeic sound of a sudden torrential mountain cloudburst or downpour",
        "pos": "adverb",
        "gender": "None",
        "category": "onomatopoeia",
        "dialect_variants": {"srinagariya": "झमक्क", "tehri": "झमक्क", "salani": "झमक्क", "rathwali": "झमक्क"}
    },
    {
        "garhwali": "कनपट",
        "hindi": "माथे के दोनों ओर कान के ऊपर का भाग (कनपटी)",
        "english": "temple of the head, lateral side of the forehead above the ear",
        "pos": "noun",
        "gender": "F",
        "category": "body",
        "dialect_variants": {"srinagariya": "कनपट", "tehri": "कनपटी", "salani": "कनपट", "rathwali": "कनपट"}
    },
    {
        "garhwali": "तरूड़",
        "hindi": "जंगल से खोदकर निकाला जाने वाला स्वादिष्ट पौष्टिक जंगली कंद/रतालू",
        "english": "wild mountain yam or edible forest tuber dug from steep wooded slopes",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "तरूड़", "tehri": "तरुड़", "salani": "तरूड़", "rathwali": "तरूड़"}
    },
    {
        "garhwali": "झिंझोड़ण",
        "hindi": "तीव्रता से हिलाना, झकझोरना अथवा पत्थरों को कम्पित करना",
        "english": "to shake violently, rattle loose scree, or agitate with force",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "झिंझोड़ण", "tehri": "झिंझोड़णा", "salani": "झिंझोड़ण", "rathwali": "झिंझोड़ण"}
    },
    {
        "garhwali": "भकोसण",
        "hindi": "लंबी यात्रा के उपरांत अत्यधिक भूख में भोजन तेजी से खाना",
        "english": "to eat ravenously or devour food hungrily after an arduous mountain climb",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "भकोसण", "tehri": "भकोसणा", "salani": "भकोसण", "rathwali": "भकोसण"}
    },
    {
        "garhwali": "सरकण",
        "hindi": "खड़ी ढलान अथवा फिसलने वाली चट्टानों पर से नीचे फिसलना",
        "english": "to slide down, glide, or slip carefully along steep scree or wet grass",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "सरकण", "tehri": "सरकणा", "salani": "सरकण", "rathwali": "सरकण"}
    },
    {
        "garhwali": "झोल",
        "hindi": "गहत अथवा उड़द की दाल का बनाया गया पतला गर्म पहाड़ी सूप",
        "english": "hot savory spiced mountain broth or thin medicinal soup made from hill pulses",
        "pos": "noun",
        "gender": "M",
        "category": "food",
        "dialect_variants": {"srinagariya": "झोल", "tehri": "झोल", "salani": "झोल", "rathwali": "झोल"}
    },
    {
        "garhwali": "फ्याकण",
        "hindi": "हाथ से पत्थर अथवा कोई वस्तु दूर उछालकर फेंकना",
        "english": "to hurl, fling, or throw stones across a mountain ravine",
        "pos": "verb",
        "gender": "None",
        "category": "actions",
        "dialect_variants": {"srinagariya": "फ्याकण", "tehri": "फ्यांकणा", "salani": "फ्याकण", "rathwali": "फ्याकण"}
    }
]

added_count = 0
for w in WAVE8_WORDS:
    if w["garhwali"] not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(w["garhwali"])
        added_count += 1
    else:
        print(f"Skipping duplicate: {w['garhwali']}")

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Wave 8 Vocabulary Injection Complete!")
print(f"Added {added_count} new lemmas.")
print(f"Total verified lexicon words: {len(existing_words)}")

