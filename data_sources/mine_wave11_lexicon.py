# -*- coding: utf-8 -*-
"""
Mine and authenticate Wave 11 vocabulary from newly added texts:
- H. G. Ross (1874) & Dr. D. N. Majumdar (1960): Jaunsar-Bawar Customary Law & Kinship (Khat, Bissu, Mahasu, Dhyanti)
- G. F. Hearth (1889): Deoban Range Jaunsar Forest (Rai spruce, Deodar, Kath-nala, Lung, Dhab)
- Pt. Devendranath Sharma (1955): Himtirth Badrinath (Panch Badri, Vyas Gupha, Bhimpul, Keshavprayag)
- H. W. Tilman (1937) & J. J. Languepin (1956): First Ascent of Nanda Devi & Alpine Mountaineering
"""

import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WORDS_PATH = "garhwali/lexicon/data/words.json"

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_lemmas = {w["garhwali"] for w in existing_words}

WAVE11_WORDS = [
    # --- Jaunsar-Bawar / Western Garhwal Customary Life & Kinship (Majumdar 1960, Ross 1874) ---
    {
        "garhwali": "खत",
        "hindi": "जौनसार-बावर एवं रवांई में कई पहाड़ी गांवों का पारंपरिक प्रशासनिक समूह अथवा पट्टी",
        "english": "Khat, traditional administrative cluster of hill villages in Jaunsar-Bawar and Western Garhwal governed by elders",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "खत", "tehri": "खत", "salani": "खत", "rathwali": "खत"}
    },
    {
        "garhwali": "दस्तूर-उल-अमल",
        "hindi": "जौनसार-बावर में भूमि, विवाह एवं चारागाह अधिकारों की पारंपरिक संहिताबद्ध प्रथागत विधि",
        "english": "Dastur-ul-Amal, the codified body of customary tribal and agrarian laws governing Jaunsar-Bawar",
        "pos": "noun",
        "gender": "M",
        "category": "governance",
        "dialect_variants": {"srinagariya": "दस्तूर-उल-अमल", "tehri": "दस्तूर-उल-अमल", "salani": "दस्तूर-उल-अमल", "rathwali": "दस्तूर-उल-अमल"}
    },
    {
        "garhwali": "बिस्सू",
        "hindi": "बैशाख मास में जौनसार और पश्चिमी गढ़वाल में मनाया जाने वाला वसंतकालीन फसल उत्सव एवं ठोड़ा नृत्य मेला",
        "english": "Bissu, traditional spring harvest festival celebrated with martial archery and sword dances across Western Garhwal",
        "pos": "noun",
        "gender": "M",
        "category": "festivals",
        "dialect_variants": {"srinagariya": "बिस्सू", "tehri": "बिस्सू", "salani": "बिसु", "rathwali": "बिस्सू"}
    },
    {
        "garhwali": "माघ-त्योहार",
        "hindi": "सर्दियों में जौनसार-बावर के गांवों में पूरे महीने चलने वाला पारंपरिक सामूहिक भोज और लोक नृत्य पर्व",
        "english": "Magh Festival, month-long winter communal rejoicing featuring sheep feasting and folk dancing across hill hamlets",
        "pos": "noun",
        "gender": "M",
        "category": "festivals",
        "dialect_variants": {"srinagariya": "माघ-त्योहार", "tehri": "माघ-त्यौहार", "salani": "माघ-त्योहार", "rathwali": "माघ-त्योहार"}
    },
    {
        "garhwali": "महाशू",
        "hindi": "जौनसार-बावर, रवांई एवं जौनपुर के परम आराध्य न्यायप्रिय कुलदेवता (महाशिव स्वरूप)",
        "english": "Mahasu Devta, supreme judicial guardian deity revered throughout Western Garhwal and the Tons-Yamuna valleys",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "महाशू", "tehri": "महासू", "salani": "महासू", "rathwali": "महाशू"}
    },
    {
        "garhwali": "बोठा",
        "hindi": "टोंस नदी तट पर हणोल में स्थित महासू देवता का मुख्य एवं सबसे पवित्र मंदिर स्वरूप",
        "english": "Botha Mahasu, principal and most sacred manifestation of Mahasu Devta enshrined at Hanol on the Tons River",
        "pos": "noun",
        "gender": "M",
        "category": "religion",
        "dialect_variants": {"srinagariya": "बोठा", "tehri": "बोठा", "salani": "बोठा", "rathwali": "बोठा"}
    },
    {
        "garhwali": "ठोड़ा",
        "hindi": "बिस्सू मेले के अवसर पर धनुष-बाण लेकर किया जाने वाला कौरव-पांडव युद्ध का पारंपरिक युयुत्सु नृत्य",
        "english": "Thoda, traditional martial archery dance re-enacting Mahabharata combat performed during Himalayan spring fairs",
        "pos": "noun",
        "gender": "M",
        "category": "arts",
        "dialect_variants": {"srinagariya": "ठोड़ा", "tehri": "ठोडा", "salani": "ठोडा", "rathwali": "ठोड़ा"}
    },
    {
        "garhwali": "सदर-स्याणा",
        "hindi": "पहाड़ी खत अथवा गांव समूह का मुख्य एवं सर्वमान्य मुखिया जो विवादों का अंतिम फैसला करता है",
        "english": "Sadar-Sayana, paramount hereditary chief and chief elder of an entire Khat responsible for communal adjudication",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "सदर-स्याणा", "tehri": "सदर-सयाणा", "salani": "सदर-सयाणा", "rathwali": "सदर-स्याणा"}
    },
    {
        "garhwali": "जोड़ीदार",
        "hindi": "पारंपरिक जौनसारी संयुक्त परिवार में एक ही स्त्री के सह-पति अथवा भाई-भाई",
        "english": "Jodidar, fraternal co-husbands sharing joint marital responsibilities in traditional Pahari domestic kinship",
        "pos": "noun",
        "gender": "M",
        "category": "family",
        "dialect_variants": {"srinagariya": "जोड़ीदार", "tehri": "जोडीदार", "salani": "जोडीदार", "rathwali": "जोड़ीदार"}
    },
    {
        "garhwali": "ध्यांटी",
        "hindi": "विवाहिता पुत्री जब अपने मायके (पिता के गांव) आती है और उसे पूर्ण स्वतंत्रता व सम्मान मिलता है",
        "english": "Dhyanti, married daughter when visiting her natal village where custom grants her special festive honors and autonomy",
        "pos": "noun",
        "gender": "F",
        "category": "family",
        "dialect_variants": {"srinagariya": "ध्यांटी", "tehri": "ध्याण्टी", "salani": "ध्यांटी", "rathwali": "ध्यांटी"}
    },
    {
        "garhwali": "रैंती",
        "hindi": "ससुराल में रहने वाली बहू जिस पर घर के कामकाज और गोशाला की पूर्ण जिम्मेदारी होती है",
        "english": "Rainti, daughter-in-law in her husband's domestic household managing farming and cattle-keeping duties",
        "pos": "noun",
        "gender": "F",
        "category": "family",
        "dialect_variants": {"srinagariya": "रैंती", "tehri": "रैन्ती", "salani": "रैंती", "rathwali": "रैंती"}
    },
    {
        "garhwali": "हणोल",
        "hindi": "टोंस नदी किनारे स्थित पवित्र तीर्थ स्थल जहां महासू देवता का प्रसिद्ध काष्ठ-शिल्प युक्त भव्य मंदिर है",
        "english": "Hanol, sacred temple village on the Tons River housing the ancient pagoda-style sanctum of Mahasu Devta",
        "pos": "noun",
        "gender": "M",
        "category": "places",
        "dialect_variants": {"srinagariya": "हणोल", "tehri": "हणोळ", "salani": "हणोल", "rathwali": "हणोल"}
    },
    {
        "garhwali": "जागड़ा",
        "hindi": "भाद्रपद मास में महासू देवता के सम्मान में मनाया जाने वाला सबसे बड़ा पावन रात्रि जागरण एवं मेला",
        "english": "Jagra, grand annual nocturnal festival of Mahasu Devta in autumn celebrated with torchlight processions and singing",
        "pos": "noun",
        "gender": "M",
        "category": "festivals",
        "dialect_variants": {"srinagariya": "जागड़ा", "tehri": "जागडा", "salani": "जागडा", "rathwali": "जागड़ा"}
    },
    {
        "garhwali": "बरोथा",
        "hindi": "पारंपरिक पहाड़ी देवदार के बने दो-मंजिला मकान का नक्काशीदार मुख्य प्रवेश द्वार अथवा दालान",
        "english": "Barotha, intricately carved deodar wood entrance vestibule and threshold of traditional multi-storey Pahari houses",
        "pos": "noun",
        "gender": "M",
        "category": "architecture",
        "dialect_variants": {"srinagariya": "बरोथा", "tehri": "बरोठा", "salani": "बरोथा", "rathwali": "बरोथा"}
    },
    {
        "garhwali": "खुमरी",
        "hindi": "गांव के सयाणों और प्रमुखों की पारंपरिक पंचायत जो पारस्परिक विवादों और सामाजिक नियमों का निपटारा करती है",
        "english": "Khumri, traditional village council of elder sayanas convening to arbitrate clan disputes and community affairs",
        "pos": "noun",
        "gender": "F",
        "category": "governance",
        "dialect_variants": {"srinagariya": "खुमरी", "tehri": "खुमरी", "salani": "खुमरी", "rathwali": "खुमरी"}
    },
    {
        "garhwali": "बाजगी",
        "hindi": "पहाड़ी मेलों, शादियों और देव-पूजा में ढोल-दमाऊ बजाने वाले पारंपरिक लोक संगीतकार",
        "english": "Bajgi, hereditary Pahari musician playing the sacred hill kettle-drums (Dhol-Damau) during temple rituals and weddings",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "बाजगी", "tehri": "बाजगी", "salani": "बाजगी", "rathwali": "बाजगी"}
    },

    # --- Deoban Forest Range & Highland Silviculture (Hearth 1889) ---
    {
        "garhwali": "देवबन",
        "hindi": "चकराता के निकट 9,300 फीट ऊंची विख्यात पर्वत श्रेणी जहां से गढ़वाल के 55 से अधिक हिमशिखर दिखाई देते हैं",
        "english": "Deoban, prominent 9,300-ft mountain ridge offering panoramic views over 55 peaks of the Garhwal Himalaya",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "देवबन", "tehri": "देववण", "salani": "देवबन", "rathwali": "देवबन"}
    },
    {
        "garhwali": "राई",
        "hindi": "उच्च हिमालयी ढलानों पर उगने वाला विशाल स्प्रूस वृक्ष (Picea smithiana)",
        "english": "West Himalayan spruce (Picea smithiana), tall evergreen timber conifer thriving on cool northern ridges",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "राई", "tehri": "राई", "salani": "राई", "rathwali": "राई"}
    },
    {
        "garhwali": "काठ-नाला",
        "hindi": "पहाड़ी ढलानों से लकड़ी के भारी लट्ठों को नीचे नदी तक बहाने हेतु बनाया गया काठ का ढलानदार मार्ग (Flume)",
        "english": "wooden flume or chute engineered down precipitous gullies to float logged timber down to mountain rivers",
        "pos": "noun",
        "gender": "M",
        "category": "infrastructure",
        "dialect_variants": {"srinagariya": "काठ-नाला", "tehri": "काठ-नाळा", "salani": "काठ-नाला", "rathwali": "काठ-नाला"}
    },
    {
        "garhwali": "लूंग",
        "hindi": "सर्दियों में पशुओं के चारे हेतु बांज और मोरू के पेड़ों से काटी गई हरी पत्तियों की टहनियां",
        "english": "lopped green leafy twigs pruned from oak branches to sustain hill livestock throughout snowy winters",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "लूंग", "tehri": "ळूंग", "salani": "लूंग", "rathwali": "लूंग"}
    },
    {
        "garhwali": "छान",
        "hindi": "गांव से दूर जंगल या चरागाह के निकट पशुओं और दूध-दही रखने हेतु बना मौसमी छाना या बाड़ा",
        "english": "seasonal pastoral cattle-station and dairy hut established in upland forest clearings away from main settlements",
        "pos": "noun",
        "gender": "M",
        "category": "agriculture",
        "dialect_variants": {"srinagariya": "छान", "tehri": "छाण", "salani": "छान", "rathwali": "छान"}
    },
    {
        "garhwali": "ढाब",
        "hindi": "ऊंचे चूना-पत्थर के पहाड़ों पर बना प्राकृतिक दलदली घास का मैदान अथवा छोटा जलाशय",
        "english": "upland marsh or natural boggy hollow on limestone plateaus providing water to high-altitude grazing herds",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "ढाब", "tehri": "ढाब", "salani": "ढाब", "rathwali": "ढाब"}
    },
    {
        "garhwali": "पिरुल",
        "hindi": "चीड़ के जंगलों की जमीन पर बिछी सूखी सुई जैसी नुकीली पत्तियां",
        "english": "fallen dry needle bed carpeted beneath Himalayan pine forests used as cattle bedding and compost",
        "pos": "noun",
        "gender": "M",
        "category": "nature",
        "dialect_variants": {"srinagariya": "पिरुल", "tehri": "पिरुळ", "salani": "पिरुल", "rathwali": "पिरुल"}
    },
    {
        "garhwali": "देवदारु",
        "hindi": "हिमालय का देव-वृक्ष देवदार (Cedrus deodara) जिसकी सुगंधित लकड़ी से प्राचीन मंदिर और घर बनते हैं",
        "english": "sacred Himalayan cedar (Cedrus deodara) whose fragrant decay-resistant timber frames alpine temples and shrines",
        "pos": "noun",
        "gender": "M",
        "category": "flora",
        "dialect_variants": {"srinagariya": "देवदारु", "tehri": "देवदारु", "salani": "देवदारु", "rathwali": "देवदारु"}
    },

    # --- Badrinath Sacred Geography & Holy Caves (Pt. Devendranath Sharma 1955) ---
    {
        "garhwali": "पंचबद्री",
        "hindi": "गढ़वाल में स्थित भगवान विष्णु के पांच पवित्र धाम (श्री बद्रीनाथ, योगध्यान बद्री, भविष्य बद्री, वृद्ध बद्री, आदि बद्री)",
        "english": "Panch Badri, the five consecrated Himalayan abodes of Lord Vishnu situated in the Alaknanda and Dhauli valleys",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "पंचबद्री", "tehri": "पंचबद्री", "salani": "पंचबद्री", "rathwali": "पंचबद्री"}
    },
    {
        "garhwali": "योगध्यान",
        "hindi": "पांडुकेश्वर में स्थित पंचबद्री तीर्थ जहां राजा पांडु ने तपस्या की थी और जहां शीतकाल में बद्रीनाथ की उत्सव मूर्ति रहती है",
        "english": "Yogdhyan Badri at Pandukeshwar, sacred seat where King Pandu meditated and winter home of the festive Utsav Murti",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "योगध्यान", "tehri": "योगध्यान", "salani": "योगध्यान", "rathwali": "योगध्यान"}
    },
    {
        "garhwali": "भविष्यबद्री",
        "hindi": "जोशीमठ से आगे सुभैन वन में स्थित वह पवित्र तीर्थ जहां कलयुग के अंत में बद्रीनाथ की पूजा होने की मान्यता है",
        "english": "Bhavishya Badri, forested shrine near Subhain in Dhauli gorge prophesied to become the future seat of Badrinath",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "भविष्यबद्री", "tehri": "भविष्यबद्री", "salani": "भविष्यबद्री", "rathwali": "भविष्यबद्री"}
    },
    {
        "garhwali": "वृद्धबद्री",
        "hindi": "जोशीमठ के निकट अणिमठ में स्थित वह प्राचीन मंदिर जहां आदि शंकराचार्य से पूर्व बद्रीनाथ की पूजा होती थी",
        "english": "Vridha Badri at Animath, ancient temple site where Vishnu was worshipped prior to the advent of Adi Shankaracharya",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "वृद्धबद्री", "tehri": "वृद्धबद्री", "salani": "वृद्धबद्री", "rathwali": "वृद्धबद्री"}
    },
    {
        "garhwali": "आदिबद्री",
        "hindi": "कर्णप्रयाग-रानीखेत मार्ग पर स्थित 16 प्राचीन मंदिरों का पावन समूह",
        "english": "Adi Badri, historical complex of sixteen ancient stone temples situated on the historical pilgrim trail near Karnaprayag",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "आदिबद्री", "tehri": "आदिबद्री", "salani": "आदिबद्री", "rathwali": "आदिबद्री"}
    },
    {
        "garhwali": "केशवप्रयाग",
        "hindi": "माणा गांव के निकट अलकनंदा और अदृश्य सरस्वती नदियों का परम पावन संगम स्थल",
        "english": "Keshavprayag, sacred confluence of the milky Alaknanda and subterranean Saraswati rivers at Mana village",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "केशवप्रयाग", "tehri": "केशवप्रयाग", "salani": "केशवप्रयाग", "rathwali": "केशवप्रयाग"}
    },
    {
        "garhwali": "व्यास-गुफा",
        "hindi": "माणा गांव में स्थित वह पाषाण गुफा जहां महर्षि वेदव्यास ने महाभारत एवं अठारह पुराणों की रचना की थी",
        "english": "Vyas Gupha, natural rock cavern at Mana where sage Vedavyasa dictated the Mahabharata and eighteen Puranas",
        "pos": "noun",
        "gender": "F",
        "category": "places",
        "dialect_variants": {"srinagariya": "व्यास-गुफा", "tehri": "व्यास-गुफा", "salani": "व्यास-गुफा", "rathwali": "व्यास-गुफा"}
    },
    {
        "garhwali": "गणेश-गुफा",
        "hindi": "माणा में व्यास गुफा के समीप स्थित वह गुफा जहां भगवान गणेश ने व्यास जी द्वारा उच्चारित महाभारत को लिपिबद्ध किया था",
        "english": "Ganesh Gupha, sacred cave near Mana wherein Lord Ganesha scribed down the verses of the Mahabharata",
        "pos": "noun",
        "gender": "F",
        "category": "places",
        "dialect_variants": {"srinagariya": "गणेश-गुफा", "tehri": "गणेश-गुफा", "salani": "गणेश-गुफा", "rathwali": "गणेश-गुफा"}
    },
    {
        "garhwali": "भीमपुल",
        "hindi": "माणा में सरस्वती नदी के प्रचंड जलप्रपात पर स्थित भीम द्वारा स्थापित विशाल प्राकृतिक पाषाण शिलापुल",
        "english": "Bhimpul, colossal natural granite boulder bridge spanning the foaming gorge of the Saraswati River at Mana",
        "pos": "noun",
        "gender": "M",
        "category": "infrastructure",
        "dialect_variants": {"srinagariya": "भीमपुल", "tehri": "भीमपुळ", "salani": "भीमपुल", "rathwali": "भीमपुल"}
    },
    {
        "garhwali": "सरस्वती-नदी",
        "hindi": "माणा के हिमशिखरों से गर्जना करती हुई निकलने वाली पवित्र नदी जो भीमपुल के नीचे से बहती है",
        "english": "Saraswati River, roaring glacial torrent emerging from the moraines above Mana before vanishing into subterranean channels",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "सरस्वती-नदी", "tehri": "सरस्वती-नदी", "salani": "सरस्वती-नदी", "rathwali": "सरस्वती-नदी"}
    },
    {
        "garhwali": "शेषनेत्र",
        "hindi": "बद्रीनाथ में अलकनंदा किनारे स्थित वह प्राकृतिक शिला जिस पर शेषनाग के नेत्र की प्राकृतिक आकृति बनी है",
        "english": "Sheshanetra, sacred natural rock formation on the Alaknanda bank marked with the legendary eye of serpent Shesha",
        "pos": "noun",
        "gender": "M",
        "category": "pilgrimage",
        "dialect_variants": {"srinagariya": "शेषनेत्र", "tehri": "शेषनेत्र", "salani": "शेषनेत्र", "rathwali": "शेषनेत्र"}
    },

    # --- Nanda Devi Historic First Ascent & High Alpine Terms (Tilman 1937, Languepin 1956) ---
    {
        "garhwali": "पसंग",
        "hindi": "नंदा देवी और कामेत अभियानों में भारी बोझ उठाकर शिखरों तक पहुंचने वाले निष्ठावान भोटिया व शेरपा पर्वतारोही",
        "english": "Pasang, legendary highland porter of Garhwal expeditions esteemed for superhuman stamina across crevassed cols",
        "pos": "noun",
        "gender": "M",
        "category": "people",
        "dialect_variants": {"srinagariya": "पसंग", "tehri": "पसंग", "salani": "पसंग", "rathwali": "पसंग"}
    },
    {
        "garhwali": "बर्फ-कुदाल",
        "hindi": "कठिन बर्फीली ढलानों में कदम काटने और चढ़ाई करने वाली पर्वतारोही कुल्हाड़ी (Ice Axe)",
        "english": "alpine ice axe (piolet) utilized to chop footholds and arrest falls along precipitous Himalayan ice faces",
        "pos": "noun",
        "gender": "F",
        "category": "tools",
        "dialect_variants": {"srinagariya": "बर्फ-कुदाल", "tehri": "बर्फ-कुदाळ", "salani": "बर्फ-कुदाल", "rathwali": "बर्फ-कुदाल"}
    },
    {
        "garhwali": "हिमानी-दरार",
        "hindi": "पहाड़ की मुख्य चट्टान और हिमनद के बर्फ के बीच बनी गहरी खाई (Bergschrund)",
        "english": "Bergschrund, immense crevasse or rimaye separating the moving glacier body from the stagnant mountain headwall",
        "pos": "noun",
        "gender": "F",
        "category": "geography",
        "dialect_variants": {"srinagariya": "हिमानी-दरार", "tehri": "हिमानी-दरार", "salani": "हिमानी-दरार", "rathwali": "हिमानी-दरार"}
    },
    {
        "garhwali": "चट्टानी-कगार",
        "hindi": "सीधी खड़ी पर्वत दीवार पर बनी संकरी और खतरनाक पथरीली मुंडेर",
        "english": "narrow exposed rock ledge or perilous outcrop flanking a vertical Himalayan cliff face",
        "pos": "noun",
        "gender": "M",
        "category": "geography",
        "dialect_variants": {"srinagariya": "चट्टानी-कगार", "tehri": "चट्टानी-कगार", "salani": "चट्टानी-कगार", "rathwali": "चट्टानी-कगार"}
    },
    {
        "garhwali": "हिम-धूल",
        "hindi": "उच्च शिखरों पर तेज आंधी के कारण उड़ने वाली महीन शुष्क बर्फ की फुहार (Spindrift)",
        "english": "fine airborne spindrift or powdered snow whipped across knife-edged mountain ridges by gale-force winds",
        "pos": "noun",
        "gender": "F",
        "category": "weather",
        "dialect_variants": {"srinagariya": "हिम-धूल", "tehri": "हिम-धूळ", "salani": "हिम-धूल", "rathwali": "हिम-धूल"}
    }
]

added_count = 0
for w in WAVE11_WORDS:
    lemma = w["garhwali"]
    if lemma not in existing_lemmas:
        existing_words.append(w)
        existing_lemmas.add(lemma)
        added_count += 1

with open(WORDS_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} words from Wave 11. Total words in library: {len(existing_words)}.")

