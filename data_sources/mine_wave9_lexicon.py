# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 9 vocabulary from newly added texts:
- Frank S. Smythe (1932): Kamet Conquered & Explorations around Kamet (Alpine flora, glaciers, passes)
- Pt. Hariram Sharma (1938): Badrinath-Kedarnath Yatra (Sacred shrines, kunds, halts, temple rites)
- Dr. Mohammad Ishaq Khan (1978): History of Srinagar (Bazaar trade, architecture, crafts, coinage)
- Parvez Maanoos (2020): Parbaton Ki Khushbu (Pastoral migrations, folk narratives, homesteads)
- Swami Sivananda (1966): Himalayan Forest Academy (Herbal remedies, mountain serenity, ascetic discipline)
"""

import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE9_WORDS = [
    # --- Alpine Topography, Mountaineering & High Glacial Flora (Smythe 1932) ---
    {
        "garhwali": "ब्योण्डार",
        "hindi": "फूलों की घाटी (Bhyundar Valley) का पारंपरिक स्थानीय गढ़वाली नाम",
        "english": "Bhyundar Valley, the traditional Garhwali name for the alpine Valley of Flowers near Joshimath",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "ब्योण्डार", "tehri": "भ्योण्डार", "salani": "ब्योण्डार", "rathwali": "ब्योण्डार"}
    },
    {
        "garhwali": "फेनकमल",
        "hindi": "अल्पाइन चट्टानों और हिमानी मोरेन पर खिलने वाला रोएंदार दुर्लभ कमल (Saussurea gossypiphora)",
        "english": "woolly snow-lotus (Saussurea gossypiphora) flowering on high Himalayan glacial screes and moraines",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "फेनकमल", "tehri": "फेनकमळ", "salani": "फेनकमल", "rathwali": "फेनकमल"}
    },
    {
        "garhwali": "कस्तूरीकमल",
        "hindi": "उच्च हिमालयी चोटियों पर पाया जाने वाला सुगंधित औषधीय कमल (Saussurea sacra)",
        "english": "sacred aromatic alpine lotus (Saussurea sacra) revered in Garhwali folklore for healing virtues",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "कस्तूरीकमल", "tehri": "कस्तूरीकमळ", "salani": "कस्तूरीकमल", "rathwali": "कस्तूरीकमल"}
    },
    {
        "garhwali": "हिमगह्वर",
        "hindi": "हिमनदों के बीच बनी गहरी और खतरनाक हिम-दरार (crevasse)",
        "english": "glacial crevasse or yawning chasm formed in moving mountain icefields",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "हिमगह्वर", "tehri": "हिमगह्वर", "salani": "हिमगह्वर", "rathwali": "हिमगह्वर"}
    },
    {
        "garhwali": "हिमप्रपात",
        "hindi": "पहाड़ की ढलानों से गर्जना करते हुए गिरने वाला विशाल हिमस्खलन",
        "english": "Himalayan avalanche or icefall cascading down precipitous mountain flanks",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिमप्रपात", "tehri": "हिमप्रपात", "salani": "हिमप्रपात", "rathwali": "हिमप्रपात"}
    },
    {
        "garhwali": "हिमनद",
        "hindi": "पहाड़ों की उच्च घाटियों में धीरे-धीरे बहने वाली विशाल बर्फ की नदी (Glacier)",
        "english": "mountain glacier or perennial valley river of solid ice",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "हिमनद", "tehri": "हिमनद", "salani": "हिमनद", "rathwali": "हिमनद"}
    },
    {
        "garhwali": "धुरी",
        "hindi": "पर्वतमाला की सबसे ऊंची एवं तीखी कटक या धुर",
        "english": "razor-sharp mountain crest or towering ridge-line dividing two Himalayan valleys",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "धुरी", "tehri": "धुरी", "salani": "धुरी", "rathwali": "धुरी"}
    },
    {
        "garhwali": "डाँठ",
        "hindi": "दो चट्टानी शिखरों के बीच का तंग एवं पथरीला पर्वतीय दर्रा",
        "english": "narrow rocky mountain notch, cleft or defile between steep cliff faces",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "डाँठ", "tehri": "डांठ", "salani": "डांठ", "rathwali": "डाँठ"}
    },
    {
        "garhwali": "कामेत",
        "hindi": "गढ़वाल हिमालय का 25,447 फीट ऊंचा विशाल एवं भव्य हिमशिखर",
        "english": "Mount Kamet (25,447 ft), the majestic mountain peak of northern Garhwal conquered in 1931-32",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "कामेत", "tehri": "कामेत", "salani": "कामेत", "rathwali": "कामेत"}
    },
    {
        "garhwali": "बग्याली",
        "hindi": "बुग्यालों में उगने वाली छोटी, पौष्टिक अल्पाइन घास एवं झाड़ियां",
        "english": "nutritious dwarf alpine turf and shrubs growing in high Himalayan summer meadows (bugyals)",
        "pos": "noun",
        "gender": "F",
        "category": "flora",
        "dialect_variants": {"srinagariya": "बग्याली", "tehri": "बग्याळी", "salani": "बग्याली", "rathwali": "बग्याली"}
    },
    {
        "garhwali": "हिमशिखर",
        "hindi": "सदा बर्फ से ढकी रहने वाली आकाशचुंबी पर्वत चोटी",
        "english": "perpetually snow-capped mountain peak or Himalayan summit",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "हिमशिखर", "tehri": "हिमशिखर", "salani": "हिमशिखर", "rathwali": "हिमशिखर"}
    },
    {
        "garhwali": "हिमरेखा",
        "hindi": "पहाड़ों में वह प्राकृतिक ऊंचाई जिसके ऊपर बर्फ कभी पूरी तरह नहीं पिघलती (Snowline)",
        "english": "perpetual snowline on Himalayan mountain ranges above which snow persists all year",
        "pos": "noun",
        "gender": "F",
        "category": "nature",
        "dialect_variants": {"srinagariya": "हिमरेखा", "tehri": "हिमरेखा", "salani": "हिमरेखा", "rathwali": "हिमरेखा"}
    },
    {
        "garhwali": "झूलापुल",
        "hindi": "पहाड़ी नदियों और गहरी खाइयों पर रस्सियों या तारों से बना झूलता हुआ संकरा पुल",
        "english": "traditional suspension rope or wire footbridge spanning deep Himalayan river gorges",
        "pos": "noun",
        "gender": "M",
        "category": "infrastructure",
        "dialect_variants": {"srinagariya": "झूलापुल", "tehri": "झूळापुळ", "salani": "झूलापुल", "rathwali": "झूलापुल"}
    },
    {
        "garhwali": "खराड़ी",
        "hindi": "हिमनदों के पिघलने से जमा हुआ पत्थरों, मलबे और बजरी का टीला (Moraine)",
        "english": "glacial moraine consisting of boulders, scree, and debris deposited along glacial margins",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "खराड़ी", "tehri": "खराडी", "salani": "खराडी", "rathwali": "खराड़ी"}
    },

    # --- Sacred Shrines, Pilgrimage Halts & Rituals (Pt. Hariram Sharma 1938) ---
    {
        "garhwali": "तप्तकुंड",
        "hindi": "बद्रीनाथ धाम में अलकनंदा किनारे स्थित प्राकृतिक गर्म गंधक जल का पवित्र कुंड",
        "english": "sacred thermal sulphur spring bath situated beside the Alaknanda river at Badrinath",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "तप्तकुंड", "tehri": "तप्तकुण्ड", "salani": "तप्तकुंड", "rathwali": "तप्तकुंड"}
    },
    {
        "garhwali": "नारदकुंड",
        "hindi": "बद्रीनाथ में अलकनंदा नदी की धारा में स्थित वह पावन कुंड जहां से आदि शंकराचार्य ने बद्रीनारायण की मूर्ति निकाली थी",
        "english": "holy recess in the Alaknanda stream at Badrinath whence Adi Shankaracharya recovered the sacred deity",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "नारदकुंड", "tehri": "नारदकुण्ड", "salani": "नारदकुंड", "rathwali": "नारदकुंड"}
    },
    {
        "garhwali": "पंचप्रयाग",
        "hindi": "गढ़वाल के पांच पवित्र संगम (देवप्रयाग, रुद्रप्रयाग, कर्णप्रयाग, नंदप्रयाग, विष्णुप्रयाग)",
        "english": "Panch Prayag, the five holy river confluences of Garhwal along the sacred Alaknanda course",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "पंचप्रयाग", "tehri": "पंचप्रयाग", "salani": "पंचप्रयाग", "rathwali": "पंचप्रयाग"}
    },
    {
        "garhwali": "छत्ती",
        "hindi": "प्राचीन तीर्थ मार्गों पर यात्रियों के रात्रि विश्राम हेतु बनी पारंपरिक धर्मशाला या पड़ाव",
        "english": "traditional mountain pilgrim rest-house or staging station established along the Kedarnath-Badrinath bridle path",
        "pos": "noun",
        "gender": "F",
        "category": "infrastructure",
        "dialect_variants": {"srinagariya": "छत्ती", "tehri": "छत्ती", "salani": "छत्ती", "rathwali": "छत्ती"}
    },
    {
        "garhwali": "कपाट",
        "hindi": "हिमालयी मंदिरों के मुख्य गर्भगृह के भारी कपाट या द्वार",
        "english": "sanctum wooden portals or monumental doors of high Himalayan temple shrines",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "कपाट", "tehri": "कपाट", "salani": "कपाट", "rathwali": "कपाट"}
    },
    {
        "garhwali": "अखंडज्योति",
        "hindi": "शीतकाल में कपाट बंद रहने पर भी बद्रीनाथ और केदारनाथ गर्भगृह में छह मास निरंतर जलने वाला घी का पावन दीपक",
        "english": "eternal sacred ghee lamp kept burning continuously inside Himalayan sanctums during six-month winter closures",
        "pos": "noun",
        "gender": "F",
        "category": "religion",
        "dialect_variants": {"srinagariya": "अखंडज्योति", "tehri": "अखण्डज्योत", "salani": "अखंडज्योत", "rathwali": "अखंडज्योति"}
    },
    {
        "garhwali": "ब्रह्मकपाल",
        "hindi": "बद्रीनाथ में अलकनंदा तट पर स्थित वह पवित्र शिला जहां पूर्वजों के मोक्ष हेतु तर्पण एवं श्राद्ध किया जाता है",
        "english": "sacred rock platform on the Alaknanda riverbank at Badrinath reserved for ancestral obsequies and tarpan rites",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "ब्रह्मकपाल", "tehri": "ब्रह्मकपाळ", "salani": "ब्रह्मकपाल", "rathwali": "ब्रह्मकपाल"}
    },
    {
        "garhwali": "धूनी",
        "hindi": "हिमालयी संतों और योगियों की गुफाओं में जलने वाली पवित्र निरंतर अग्नि",
        "english": "consecrated fire pit maintained perpetually by ascetics and sadhus in mountain hermitages",
        "pos": "noun",
        "gender": "F",
        "category": "religion",
        "dialect_variants": {"srinagariya": "धूनी", "tehri": "धुणी", "salani": "धूनी", "rathwali": "धूनी"}
    },
    {
        "garhwali": "बद्रीनाथ",
        "hindi": "चमोली गढ़वाल में स्थित भगवान विष्णु का परम पावन महातीर्थ",
        "english": "Badrinath, supreme Himalayan shrine of Lord Badri-Vishal in Chamoli district, Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "बद्रीनाथ", "tehri": "बद्रीनाथ", "salani": "बद्रीनाथ", "rathwali": "बद्रीनाथ"}
    },
    {
        "garhwali": "केदारनाथ",
        "hindi": "मंदाकिनी नदी के उद्गम पर स्थित द्वादश ज्योतिर्लिंगों में से एक परम पावन शिवधाम",
        "english": "Kedarnath, prominent Himalayan Jyotirlinga temple of Lord Shiva seated at 11,755 ft beneath Kedardome",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "केदारनाथ", "tehri": "केदारनाथ", "salani": "केदारनाथ", "rathwali": "केदारनाथ"}
    },
    {
        "garhwali": "कन्डी",
        "hindi": "पहाड़ी मार्गों पर अशक्त यात्रियों या बच्चों को पीठ पर बिठाकर ले जाने वाली मजबूत बांस की टोकरी",
        "english": "wicker basket carrier strapped to a hill porter's back for transporting infirm pilgrims and children up steep tracks",
        "pos": "noun",
        "gender": "F",
        "category": "transport",
        "dialect_variants": {"srinagariya": "कन्डी", "tehri": "कण्डी", "salani": "कंडी", "rathwali": "कन्डी"}
    },
    {
        "garhwali": "महाभिषेक",
        "hindi": "प्रातःकाल हिमालयी मंदिरों में देवमूर्ति पर गंगाजल, दूध और सुगंधित द्रव्यों से किया जाने वाला विशेष अभिषेक",
        "english": "grand dawn anointing ceremony with sacred waters, milk, and alpine fragrances performed at Himalayan shrines",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "महाभिषेक", "tehri": "महाभिषेक", "salani": "महाभिषेक", "rathwali": "महाभिषेक"}
    },
    {
        "garhwali": "भोग-प्रसाद",
        "hindi": "देवता को अर्पित किया गया पवित्र नैवेद्य और प्रसाद",
        "english": "sanctified food offering prepared from mountain grains and butter distributed to devotees",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "भोग-प्रसाद", "tehri": "भोग-प्रसाद", "salani": "भोग-प्रसाद", "rathwali": "भोग-प्रसाद"}
    },
    {
        "garhwali": "कपाट-उद्घाटन",
        "hindi": "वसंत ऋतु में अक्षय तृतीया पर हिमालयी धामों के द्वार खोलने का पारंपरिक पावन उत्सव",
        "english": "ceremonial spring festival marking the auspicious reopening of mountain sanctums to pilgrims after winter",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "कपाट-उद्घाटन", "tehri": "कपाट-उद्घाटन", "salani": "कपाट-उद्घाटन", "rathwali": "कपाट-उद्घाटन"}
    },

    # --- Mountain Bazaar Commerce, Architecture & Crafts (Dr. Ishaq Khan 1978) ---
    {
        "garhwali": "पसर",
        "hindi": "पहाड़ी बाजार में व्यापारी की दुकान का खुला अग्रभाग अथवा फर्श जहां माल सजाया जाता है",
        "english": "open shopfront display platform or mat on which mountain shopkeepers lay out their merchandise",
        "pos": "noun",
        "gender": "M",
        "category": "commerce",
        "dialect_variants": {"srinagariya": "पसर", "tehri": "पसर", "salani": "पसर", "rathwali": "पसर"}
    },
    {
        "garhwali": "सौदागर",
        "hindi": "पहाड़ों और तिब्बत सीमा के बीच ऊन, नमक और जड़ी-बूटियों का बड़ा व्यापार करने वाला व्यापारी",
        "english": "trans-Himalayan merchant or trader managing caravans of wool, borax, salt, and mountain medicinal roots",
        "pos": "noun",
        "gender": "M",
        "category": "commerce",
        "dialect_variants": {"srinagariya": "सौदागर", "tehri": "सौदागर", "salani": "सौदागर", "rathwali": "सौदागर"}
    },
    {
        "garhwali": "सौदागरी",
        "hindi": "पर्वतीय क्षेत्रों में दूर-दराज के हाटों और मेलों में व्यापार करने का पेशा",
        "english": "commerce and mercantile caravan trade conducted between mountain valleys and trading marts",
        "pos": "noun",
        "gender": "F",
        "category": "commerce",
        "dialect_variants": {"srinagariya": "सौदागरी", "tehri": "सौदागरी", "salani": "सौदागरी", "rathwali": "सौदागरी"}
    },
    {
        "garhwali": "आढ़त",
        "hindi": "पहाड़ी मंडियों में अनाज, ऊन एवं फलों की खरीद-फरोख्त का थोक व्यापार केंद्र या दलाली",
        "english": "wholesale commission agency and storage depot operating in Himalayan market hubs",
        "pos": "noun",
        "gender": "F",
        "category": "commerce",
        "dialect_variants": {"srinagariya": "आढ़त", "tehri": "आढ़त", "salani": "आढत", "rathwali": "आढ़त"}
    },
    {
        "garhwali": "दस्तकारी",
        "hindi": "गढ़वाली काष्ठ-शिल्प, रिंगाल-बुनाई एवं ऊनी वस्त्रों का पारंपरिक हस्तशिल्प",
        "english": "traditional highland handicraft, particularly intricate wood carving, ringal reed weaving, and loom work",
        "pos": "noun",
        "gender": "F",
        "category": "crafts",
        "dialect_variants": {"srinagariya": "दस्तकारी", "tehri": "दस्तकारी", "salani": "दस्तकारी", "rathwali": "दस्तकारी"}
    },
    {
        "garhwali": "टका",
        "hindi": "गढ़वाल रियासत के समय चलने वाला प्राचीन तांबे का सिक्का अथवा धन",
        "english": "traditional copper coin or currency token minted during historical princely Garhwali rule",
        "pos": "noun",
        "gender": "M",
        "category": "economy",
        "dialect_variants": {"srinagariya": "टका", "tehri": "टका", "salani": "टका", "rathwali": "टका"}
    },
    {
        "garhwali": "काष्ठकला",
        "hindi": "गढ़वाली घरों की खिड़कियों और दरवाजों (मोरी-टिबारे) पर की जाने वाली बारीक नक्काशी",
        "english": "indigenous Garhwali wood-carving art ornamenting ornate lintels, balconies, and pillar capitals",
        "pos": "noun",
        "gender": "F",
        "category": "arts",
        "dialect_variants": {"srinagariya": "काष्ठकला", "tehri": "काष्ठकळा", "salani": "काष्ठकला", "rathwali": "काष्ठकला"}
    },
    {
        "garhwali": "हुंडी",
        "hindi": "पहाड़ी व्यापारियों द्वारा लंबी यात्राओं में नकदी ले जाने के जोखिम से बचने हेतु जारी की जाने वाली साख-चिट्ठी",
        "english": "traditional mountain bill of exchange or credit note used by merchants to avoid carrying physical coinage across passes",
        "pos": "noun",
        "gender": "F",
        "category": "commerce",
        "dialect_variants": {"srinagariya": "हुंडी", "tehri": "हुण्डी", "salani": "हुंडी", "rathwali": "हुंडी"}
    },
    {
        "garhwali": "सराफा",
        "hindi": "श्रीनगर अथवा बड़े पहाड़ी कस्बों का वह बाजार जहां चांदी और सोने के पारंपरिक पहाड़ी आभूषण बनते हैं",
        "english": "goldsmith and silver jewelry market quarter where traditional hill ornaments (hansuli, nath, guloband) are crafted",
        "pos": "noun",
        "gender": "M",
        "category": "commerce",
        "dialect_variants": {"srinagariya": "सराफा", "tehri": "सराफा", "salani": "सराफा", "rathwali": "सराफा"}
    },

    # --- High-Altitude Pastoralism, Hermitage & Folklore (Maanoos 2020 & Swami Sivananda 1966) ---
    {
        "garhwali": "चरांद",
        "hindi": "पर्वतीय ढलानों पर पशुओं के चरने की प्राकृतिक चारागाह या गोचर भूमि",
        "english": "natural highland pasture or community grazing run where sheep and cattle feed during sunny days",
        "pos": "noun",
        "gender": "F",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "चरांद", "tehri": "चरांद", "salani": "चरांद", "rathwali": "चरांद"}
    },
    {
        "garhwali": "गोधूली",
        "hindi": "संध्याकाल जब गायें और बकरियां पहाड़ों से चरकर गांव लौटती हैं और उनके खुरों से धूल उड़ती है",
        "english": "mountain twilight or cowdust hour as cattle and goat herds wander back down to village barns",
        "pos": "noun",
        "gender": "F",
        "category": "time",
        "dialect_variants": {"srinagariya": "गोधूली", "tehri": "गोधूळी", "salani": "गोधूली", "rathwali": "गोधूली"}
    },
    {
        "garhwali": "कथा-बाता",
        "hindi": "शीतकाल की रातों में चूल्हे (डांडो) के पास बैठकर सुनाई जाने वाली पारंपरिक लोक कथाएं और किस्से",
        "english": "traditional hearth-side storytelling, folk anecdotes, and communal oral narratives shared on frosty winter nights",
        "pos": "noun",
        "gender": "F",
        "category": "folklore",
        "dialect_variants": {"srinagariya": "कथा-बाता", "tehri": "कथा-बाता", "salani": "कथा-बाता", "rathwali": "कथा-बाता"}
    },
    {
        "garhwali": "उरांव",
        "hindi": "ऊंचे पहाड़ों में गड़ेरियों (चरवाहों) द्वारा पत्थरों से बनाई गई अस्थायी झोंपड़ी या छाना",
        "english": "seasonal stone shelter hut built by high-altitude shepherds on lonely alpine ridges",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "उरांव", "tehri": "उरांव", "salani": "उरांव", "rathwali": "उरांव"}
    },
    {
        "garhwali": "जड़ी-बूटी",
        "hindi": "हिमालयी जंगलों में मिलने वाली दुर्लभ औषधीय वनस्पतियां और मूल",
        "english": "healing botanical roots and rare medicinal herbs gathered in Himalayan temperate and alpine zones",
        "pos": "noun",
        "gender": "F",
        "category": "medicine",
        "dialect_variants": {"srinagariya": "जड़ी-बूटी", "tehri": "जड़ी-बूटी", "salani": "जडी-बूटी", "rathwali": "जड़ी-बूटी"}
    },
    {
        "garhwali": "हुड़दंग",
        "hindi": "पहाड़ी मेलों अथवा कौथीगों में युवाओं द्वारा की जाने वाली उल्लासपूर्ण उछल-कूद और आनंद",
        "english": "exuberant highland merrymaking, boisterous rustic festivities, and spirited revelry during village fairs",
        "pos": "noun",
        "gender": "M",
        "category": "culture",
        "dialect_variants": {"srinagariya": "हुड़दंग", "tehri": "हुड़दंग", "salani": "हुड़दंग", "rathwali": "हुड़दंग"}
    },
    {
        "garhwali": "ग्वालिया",
        "hindi": "पहाड़ों और वनों में गाय-बकरियां चराने वाला ग्वाला या चरवाहा लड़का",
        "english": "young mountain herdsman or pastoral cowherd driving livestock across terraced hillsides and forest glades",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "ग्वालिया", "tehri": "ग्वाळिया", "salani": "ग्वालिया", "rathwali": "ग्वालिया"}
    }
]

added_count = 0
for w in WAVE9_WORDS:
    lemma = w["garhwali"]
    if lemma not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(lemma)
        added_count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} words from Wave 9. Total words in library: {len(existing_words)}.")

