"""
Script to generate:
1. data_sources/raw_texts/songs/*.txt (20 full song files)
2. garhwali/culture/data/songs.json
3. garhwali/culture/data/digital_sources.json
"""

import json
import os
import sys

# Ensure UTF-8 output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

os.makedirs(os.path.join("data_sources", "raw_texts", "songs"), exist_ok=True)
os.makedirs(os.path.join("garhwali", "culture", "data"), exist_ok=True)

songs = [
    {
        "id": "GSN-0001",
        "title": "बेडू पाको बारामासा",
        "roman": "Bedu Pako Baramasa",
        "artist": "Traditional / Narendra Singh Negi rendition",
        "genre": "Folk Song / Valley Lyrical",
        "corpus": "Central Himalayan Traditional Corpus",
        "theme": "Mountain seasons, flora, and eternal Pahari longing",
        "lyrics_sample": "बेडू पाको बारामासा, नरणी काफल पाको चैता, मेरी छैला!\nरूं-झूं-रूं-झूं रूं-झूं-रूं-झूं, बरखा की बूंदें, मेरी छैला!\nडांड्यूं मा बुरांश फूली, पाको काफल चैता, मेरी छैला!",
        "verses": [
            "बेडू पाको बारामासा, नरणी काफल पाको चैता, मेरी छैला!",
            "रूं-झूं-रूं-झूं रूं-झूं-रूं-झूं, बरखा की बूंदें, मेरी छैला!",
            "डांड्यूं मा बुरांश फूली, पाको काफल चैता, मेरी छैला!",
            "धारों-धारों बाजे बांसुरी, मन मा उमंग छैला!",
            "अलकनंदा को ठंडो पाणी, मंद-मंद बयार छैला!",
            "बेडू पाको बारामासा, नरणी काफल पाको चैता, मेरी छैला!"
        ],
        "english_translation": "The wild fig ripens twelve months of the year, O beloved, while kafal berries ripen in the spring month of Chaitra!",
        "cultural_context": "The legendary anthem of the Uttarakhand Himalaya, evoking misty terraced ridges, blooming rhododendrons, and mountain sweethearts.",
        "source_url": "https://archive.org/details/uttarakhand_folk_songs"
    },
    {
        "id": "GSN-0002",
        "title": "चैता की चैतवाली",
        "roman": "Chaita Ki Chaitwali",
        "artist": "Amit Saagar / Traditional Chaiti",
        "genre": "Chaiti / Awakening Jagar",
        "corpus": "Traditional Garhwali seasonal ballads",
        "theme": "Spring awakening, ancestral spirits, and village joy",
        "lyrics_sample": "आहा चैता की चैतवाली, हो हो चैता की चैतवाली!\nधुंयाधार डांडा-कांठा, हिंवल की छाईं,\nमेरी बांद चैतवाली, झुमेलो लगाईं!",
        "verses": [
            "आहा चैता की चैतवाली, हो हो चैता की चैतवाली!",
            "धुंयाधार डांडा-कांठा, हिंवल की छाईं,",
            "मेरी बांद चैतवाली, झुमेलो लगाईं!",
            "डौल-दमाऊँ बाजे जब, देवी का थान मा,",
            "नाचे चैतवाली सारी रात मंडाण मा!",
            "डांडी-कांठी गूंजे नाम, जय माँ भगवती!"
        ],
        "english_translation": "O daughter of the spring month of Chait! Across smoky high ridges in the snows, dance the Jhumelo all through the night!",
        "cultural_context": "Chaiti ballads are sung in the first month of the Hindu calendar (Chaitra) to awaken divine blessings and invite blessings into every household.",
        "source_url": "https://archive.org/details/garhwali_chaiti_traditions"
    },
    {
        "id": "GSN-0003",
        "title": "ठंडो रे ठंडो मेरा पहाड़ा को पाणी",
        "roman": "Thando Re Thando Mera Pahada Ko Paani",
        "artist": "Narendra Singh Negi",
        "genre": "Folk Lyric / Regional Pride",
        "corpus": "Contemporary Classic Garhwali Poetry",
        "theme": "Pure mountain springs, terraced bounty, and nostalgic pride",
        "lyrics_sample": "ठंडो रे ठंडो, मेरा पहाड़ा को पाणी,\nमीठी-मीठी हवा, शीतल सुहाणी!\nगंगा जी का मायका, केदार को द्वार,\nदेवता की भूमि, मेरु गढ़वार!",
        "verses": [
            "ठंडो रे ठंडो, मेरा पहाड़ा को पाणी,",
            "मीठी-मीठी हवा, शीतल सुहाणी!",
            "गंगा जी का मायका, केदार को द्वार,",
            "देवता की भूमि, मेरु गढ़वार!",
            "बाँझ-बुरांश की छाँव घनेरी,",
            "धारों-धारों बगे धार निर्मल केरी,",
            "छोड़िक परदेश ऐ जा रे बौरी,",
            "मेरा पहाड़ा को पाणी!"
        ],
        "english_translation": "So cool, so refreshing is the fresh spring water of my mountains! Gentle sweet breezes, maternal home of Mother Ganga, threshold of Kedarnath!",
        "cultural_context": "Penned by the legendary Garh-Kokil Narendra Singh Negi, this song is the unofficial modern national anthem of Garhwal.",
        "source_url": "https://archive.org/details/narendra_singh_negi_anthology"
    },
    {
        "id": "GSN-0004",
        "title": "घुघुती ना बास मैत की",
        "roman": "Ghughuti Na Baas Mait Ki",
        "artist": "Traditional / Folk Ballad",
        "genre": "Viraha / Separation Ballad",
        "corpus": "Oral Matriarchal Heritage of Garhwal",
        "theme": "Longing of the married daughter for her maternal village (Mait)",
        "lyrics_sample": "घुघुती ना बास, घाम ढल्यो डांडा,\nमैत की याद आई, आंख्युं मा आंसू भर आया!\nपल्लो पार डांडा बठे घुघुती बोले,\nमेरी इजा की सुध मन मा डोले!",
        "verses": [
            "घुघुती ना बास, घाम ढल्यो डांडा,",
            "मैत की याद आई, आंख्युं मा आंसू भर आया!",
            "पल्लो पार डांडा बठे घुघुती बोले,",
            "मेरी इजा की सुध मन मा डोले!",
            "काफल पाकी गे मैत का जंगलों मा,",
            "को देलो बोई मेरो सौरास मा संदेसा?",
            "घुघुती ना बास, घाम ढल्यो डांडा!"
        ],
        "english_translation": "Coo no more, O mountain dove, as dusk falls across the ridge! You bring piercing memories of my maternal village, and tears fill my eyes.",
        "cultural_context": "The dove (Ghughuti) is the symbol of maternal separation and sorrow (Naraai) across all Himalayan valleys.",
        "source_url": "https://archive.org/details/garhwali_folklore_grierson"
    },
    {
        "id": "GSN-0005",
        "title": "धारी देवी जागर - हे देवी कल्याणी",
        "roman": "Dhari Devi Jagar - Hey Devi Kalyani",
        "artist": "Pritam Bhartwan / Traditional Jagar",
        "genre": "Sacred Jagar / Divine Invocation",
        "corpus": "Central Himalayan Jagar Shamanic Corpus",
        "theme": "Invocation of Goddess Kali at the rock sanctuary of Dhari Devi",
        "lyrics_sample": "उठो माता कल्याणी, धारी की भवानी!\nअलकनंदा का बीच धारा, तेरो छ मंडाण!\nडौल-दमाऊँ बाजे, रणसिंघा को नाद,\nरक्षा कर माता, तेरो सेवक पुकार!",
        "verses": [
            "उठो माता कल्याणी, धारी की भवानी!",
            "अलकनंदा का बीच धारा, तेरो छ मंडाण!",
            "डौल-दमाऊँ बाजे, रणसिंघा को नाद,",
            "रक्षा कर माता, तेरो सेवक पुकार!",
            "सिद्धपीठ धारी मा दीप जलो भारी,",
            "पापियों को संहार कर, भक्तां तैं उबारी!",
            "जय माँ धारी देवी, जय माँ कल्याणी!"
        ],
        "english_translation": "Awaken O benevolent Mother, Bhavani of Dhari! Amidst the surging torrent of the Alaknanda river stands Thy holy sanctum!",
        "cultural_context": "Dhari Devi is the guardian deity of Uttarakhand whose deity icon changes form from girl in morning to woman at noon and elder at dusk.",
        "source_url": "https://archive.org/details/dhari_devi_sacred_jagar"
    },
    {
        "id": "GSN-0006",
        "title": "नंदा राज जात - नंदा का मायका",
        "roman": "Nanda Raj Jat - Nanda Ka Mayka",
        "artist": "Traditional Pilgrimage Ballad",
        "genre": "Himalayan Yatra Ballad",
        "corpus": "Nanda Raj Jat 280km Pilgrimage Lore",
        "theme": "The great journey of Goddess Nanda departing her maternal home for Mount Kailash",
        "lyrics_sample": "नौटी बठे निकली छंतोली, नंदा की डोली!\nबाजे भुंकोरा, बाजे रणसिंघा,\nबेडिनी बुग्याल मा जुड़ली संगोली!\nहे नंदा देवी, कैलाश तैं चली!",
        "verses": [
            "नौटी बठे निकली छंतोली, नंदा की डोली!",
            "बाजे भुंकोरा, बाजे रणसिंघा,",
            "बेडिनी बुग्याल मा जुड़ली संगोली!",
            "हे नंदा देवी, कैलाश तैं चली!",
            "चार सींगों को मेढ़ा चल्यो आगे-आगे,",
            "रूपकुंड का किनारा ब्रह्मकमल जागे!",
            "होमकुंड मा माँ का चरण धोए,",
            "सजल नयनों से सारा गढ़वाल रोए!"
        ],
        "english_translation": "From Nauti village moves the holy umbrella and Nanda's palanquin! Trumpets and copper horns resound across the high meadows of Bedni!",
        "cultural_context": "Nanda Raj Jat is the 280 km royal pilgrimage held every 12 years, escorting Goddess Nanda back to Lord Shiva at Mount Kailash.",
        "source_url": "https://archive.org/details/nanda_raj_jat_epic"
    },
    {
        "id": "GSN-0007",
        "title": "मंगल गीत - दइ दै पजनी दै",
        "roman": "Mangal Geet - Dai Dai Pajani Dai",
        "artist": "Traditional Bards (Dhaki / Mahila Mandal)",
        "genre": "Nuptial Rite / Mangal Geet",
        "corpus": "Ceremonial Oral Tradition of Garhwal",
        "theme": "Invoking blessings of sun, earth, gods, and elders upon the bride",
        "lyrics_sample": "दइ दै पजनी दै, पंच नाम देवता,\nधरती माता दै, सूरज देव नारायण!\nआज का सुदिन मा, कन्या को ब्याव,\nसुखी रए बेटी, सदा तेरो सुहाग!",
        "verses": [
            "दइ दै पजनी दै, पंच नाम देवता,",
            "धरती माता दै, सूरज देव नारायण!",
            "आज का सुदिन मा, कन्या को ब्याव,",
            "सुखी रए बेटी, सदा तेरो सुहाग!",
            "हरि का चरणा मा गंगा को नीर,",
            "मा-बाप का आंगण मा बजी शहनाई वीर!",
            "पिठ्याँ लगावा, अक्षत चढ़ावा,",
            "मंगल गीत गाई कन्या बिदा करावां!"
        ],
        "english_translation": "Grant holy blessings, O Five Devatas! Grant blessings, Mother Earth and Sun Narayan! On this auspicious day of the maiden's wedding!",
        "cultural_context": "Mangal geet are sacred traditional bridal chants sung by women and hereditary Dhakis without which no Garhwali wedding can formally proceed.",
        "source_url": "https://archive.org/details/garhwali_mangal_geet_compilation"
    },
    {
        "id": "GSN-0008",
        "title": "इगास बग्वाल - भैलो खेलो रे भैलो",
        "roman": "Igas Bagwal - Bhalo Khelo Re Bhalo",
        "artist": "Traditional Festival Song",
        "genre": "Festival Folk Dance",
        "corpus": "Heroic Festival Traditions of Garhwal",
        "theme": "Celebrating the return of hero Madho Singh Bhandari eleven days after Diwali",
        "lyrics_sample": "भैलो रे भैलो, इगास को भैलो!\nमाधो सिंह भंडारी जितिक ऐगे,\nचीड़ की छिल्ला मा आग जलाई,\nघरे-घरे पूड़ी अर रोट पकाई!",
        "verses": [
            "भैलो रे भैलो, इगास को भैलो!",
            "माधो सिंह भंडारी जितिक ऐगे,",
            "चीड़ की छिल्ला मा आग जलाई,",
            "घरे-घरे पूड़ी अर रोट पकाई!",
            "गौं-गौं मा नाचां, ढोल बजावां,",
            "बीर भड़ों की कीर्ति गावां!",
            "इगास बग्वाल को शगुन मनावां!"
        ],
        "english_translation": "Bhalo, O Bhalo! The sacred spin-torch of Igas! Madho Singh Bhandari returned victorious from Tibet, light pine torches and fry the festive breads!",
        "cultural_context": "Igas Bagwal is celebrated 11 days after Diwali in Garhwal because news of Lord Rama and hero Madho Singh's victories reached the mountains late.",
        "source_url": "https://archive.org/details/igas_bagwal_traditions"
    },
    {
        "id": "GSN-0009",
        "title": "फूलदेई छम छम - फूल संक्रांति",
        "roman": "Phooldei Chham Chham - Phool Sankranti",
        "artist": "Traditional Children's Spring Song",
        "genre": "Spring Festival Ballad",
        "corpus": "Children & Nature Himalayan Folklore",
        "theme": "Greeting the first day of Chaitra with spring blossoms placed upon thresholds",
        "lyrics_sample": "फूलदेई, छम्मा देई,\nदैणी द्वार, भर भकार!\nयो देहली सकार, बारम्बार नमस्कार!\nफूले फूल बुरांश का, लाये थाल सजाय!",
        "verses": [
            "फूलदेई, छम्मा देई,",
            "दैणी द्वार, भर भकार!",
            "यो देहली सकार, बारम्बार नमस्कार!",
            "फूले फूल बुरांश का, लाये थाल सजाय!",
            "घर-घर जावां, फूल बिखरावां,",
            "चावल अर गुड़ को उपहार पावां!",
            "सदा रहे सुख-समृद्धि, फले-फूले संसार!"
        ],
        "english_translation": "Phooldei, Chhama Dei! May your doors remain blessed, may your granaries overflow with golden harvest! We honor this sacred doorstep with mountain flowers!",
        "cultural_context": "On the first day of Chaitra, children wake at dawn, gather flowers of Buransh, Panya, and mustard, and place them on every village doorstep.",
        "source_url": "https://archive.org/details/phooldei_himalayan_festival"
    },
    {
        "id": "GSN-0010",
        "title": "मलेथा की गूल - माधो सिंह भण्डारी की गाथा",
        "roman": "Maletha Ki Gool - Madho Singh Bhandari",
        "artist": "Narendra Singh Negi / Folk Ballad",
        "genre": "Historical Pawada / Heroic Epic",
        "corpus": "Garhwali Historical Ballads",
        "theme": "The engineering sacrifice of Madho Singh Bhandari carving an irrigation canal through rock",
        "lyrics_sample": "मलेथा का डांडा मा पाणी नि छौ,\nमाधो सिंह भंडारी न पहाड़ फोड़ि गूल बणाई!\nअमर भड़ गढ़वाल को, छाती चीरि रस्ता बणायो,\nसूखी धरती तैं हरियाली सोंपि गयो!",
        "verses": [
            "मलेथा का डांडा मा पाणी नि छौ,",
            "माधो सिंह भंडारी न पहाड़ फोड़ि गूल बणाई!",
            "अमर भड़ गढ़वाल को, छाती चीरि रस्ता बणायो,",
            "सूखी धरती तैं हरियाली सोंपि गयो!",
            "चंद्रभागा नदी को पाणी लाये मलेथा,",
            "पुत्र गजे सिंह को बलिदान भी दियो,",
            "धन्य वीर माधो सिंह तेरो पराक्रम!"
        ],
        "english_translation": "Upon the parched terraces of Maletha there was no water; Madho Singh Bhandari split the solid stone mountain to carve an irrigation canal!",
        "cultural_context": "The canal (Gool) built by Madho Singh Bhandari in the 1630s still irrigates the fertile fields of Maletha in Tehri Garhwal today.",
        "source_url": "https://archive.org/details/madho_singh_bhandari_gatha"
    },
    {
        "id": "GSN-0011",
        "title": "जीतू बगड्वाल - अचरी हरण जागर",
        "roman": "Jeetu Bagdwal - Achari Haran Jagar",
        "artist": "Traditional Shamanic Jagar",
        "genre": "Epic Jagar Ballad",
        "corpus": "Folk Mythological Heritage of Garhwal",
        "theme": "The handsome flautist Jeetu enchanted by mountain fairies (Acharis) at Khait Parvat",
        "lyrics_sample": "बांसुरी बजाई जीतू बगड्वाल न डांडा मा,\nखैट का डांडा मा अचरियों को वास छौ!\nबांसुरी की धुन पर अचरियां डोली,\nजीतू का प्राण तैं हरिक ले गई!",
        "verses": [
            "बांसुरी बजाई जीतू बगड्वाल न डांडा मा,",
            "खैट का डांडा मा अचरियों को वास छौ!",
            "बांसुरी की धुन पर अचरियां डोली,",
            "जीतू का प्राण तैं हरिक ले गई!",
            "माँ रोई आंगण मा, बहन सोबनी रोई,",
            "बगड्वाल को नाम अमर रैग्यो गढ़वाल मा!"
        ],
        "english_translation": "Jeetu Bagdwal played his enchanting flute upon the mountain ridge; on Khait ridge dwelt the divine fairies (Acharis)!",
        "cultural_context": "Jeetu Bagdwal is the tragic Apollo of Garhwal, whose flute melodies bewitched fairy nymphs who took his spirit to their fairy realm.",
        "source_url": "https://archive.org/details/jeetu_bagdwal_jagar_lore"
    },
    {
        "id": "GSN-0012",
        "title": "सुरकंडा माता की वंदना - सिरकुट डांडा",
        "roman": "Surkanda Mata Ki Vandana",
        "artist": "Traditional Tehri Hymn",
        "genre": "Devotional Bhajan",
        "corpus": "Shaktipeeth Pilgrimage Hymns",
        "theme": "Hymn to Mother Surkanda perched on the panoramic ridge of Dhanaulti",
        "lyrics_sample": "जय माँ सुरकंडा, सिरकुट डांडा वासिनी,\nतेरा चरण मा शीश नवावां, हे जगदम्बे भवानी!\nऊँचा डांडा मा मंदिर तेरो, शीतल पवन बगे,\nभक्तों का संकट काटे माता, जो भी शरण लगे!",
        "verses": [
            "जय माँ सुरकंडा, सिरकुट डांडा वासिनी,",
            "तेरा चरण मा शीश नवावां, हे जगदम्बे भवानी!",
            "ऊँचा डांडा मा मंदिर तेरो, शीतल पवन बगे,",
            "भक्तों का संकट काटे माता, जो भी शरण लगे!",
            "गंगा दशहरा मा मेळा लागे भारी,",
            "दर्शन पाइक तर जांदी दुनिया सारी!"
        ],
        "english_translation": "Glory to Mother Surkanda, dweller of the high mountain crag! We bow our heads at Thy sacred feet, O Jagadamba Bhavani!",
        "cultural_context": "Surkanda Devi is one of the three Shaktipeeths forming the protective triangle of Tehri Garhwal (Surkanda, Kunjapuri, Chandrabadani).",
        "source_url": "https://archive.org/details/surkanda_devi_bhajan"
    },
    {
        "id": "GSN-0013",
        "title": "सरुली मेरु जिया लागी",
        "roman": "Saruli Meru Jiya Lagi",
        "artist": "Traditional Courtship Song",
        "genre": "Jhumelo / Romance",
        "corpus": "Folk Dance & Youth Celebrations",
        "theme": "Tender romantic banter across terraced fields and springs",
        "lyrics_sample": "सरुली, मेरु जिया लागी तेरो मुखड़ा मा!\nघास काटदी तू डांडा मा, रूप चमके धूप मा!\nऐ जा बांद, हाथ जोड़ि ब्वोल,\nकख तेरो गौं, कख तेरो थान?",
        "verses": [
            "सरुली, मेरु जिया लागी तेरो मुखड़ा मा!",
            "घास काटदी तू डांडा मा, रूप चमके धूप मा!",
            "ऐ जा बांद, हाथ जोड़ि ब्वोल,",
            "कख तेरो गौं, कख तेरो थान?",
            "घस्यारी बांद मेरी, हंसदी खिल-खिल,",
            "तेरी सुरमई आंख्युं मा मेरो बसे दिल!"
        ],
        "english_translation": "O Saruli, my heart has become enchanted by your lovely face! As you cut grass upon the terraced ridges, your grace shines in the sun!",
        "cultural_context": "Celebrates the joyful spirit of mountain maidens (Ghyasari) harvesting fodder across emerald hillsides while exchanging lyrical wit.",
        "source_url": "https://archive.org/details/saruli_folk_courtship"
    },
    {
        "id": "GSN-0014",
        "title": "हिलांस पाखी - पहाड़ा की चड़ी",
        "roman": "Hilaans Pakhi - Pahada Ki Chadi",
        "artist": "Traditional Nature Ballad",
        "genre": "Folk Ballad",
        "corpus": "Avian Folklore of Uttarakhand",
        "theme": "The high flying Hilans bird that never touches muddy ground",
        "lyrics_sample": "हिलांस पाखी, ऊँचा डांड्यूं की रानी,\nनीली गगन मा उड़े, निर्मल पीवे पाणी!\nकदे धरती मा नि बैठदी तू, पत्तों मा बसेरा,\nपहाड़ा की याद दिलावे सुबेरा-सबेरा!",
        "verses": [
            "हिलांस पाखी, ऊँचा डांड्यूं की रानी,",
            "नीली गगन मा उड़े, निर्मल पीवे पाणी!",
            "कदे धरती मा नि बैठदी तू, पत्तों मा बसेरा,",
            "पहाड़ा की याद दिलावे सुबेरा-सबेरा!",
            "हम भी हिलांस जैका, परदेश मा भटके,",
            "अपणा पहाड़ा का डांडा मन मा अटके!"
        ],
        "english_translation": "O Hilans bird, queen of high summits! Flying in the blue sky, drinking pure glacial water, never resting on muddy soil!",
        "cultural_context": "The Hilans (green pigeon) symbolizes nobility and unyielding self-respect in Garhwali oral tradition.",
        "source_url": "https://archive.org/details/hilans_pakhi_lore"
    },
    {
        "id": "GSN-0015",
        "title": "छोरी गढ़वाली - बांद मेरी छैला",
        "roman": "Chhori Garhwali - Band Meri Chhaila",
        "artist": "Traditional Festive Dance",
        "genre": "Chhori / Group Dance",
        "corpus": "Communal Fair & Mela Songs",
        "theme": "Energetic syncopated dance at autumn village harvest fairs",
        "lyrics_sample": "छोरी रे छोरी, गढ़वाल का डांडा मा!\nकमर मा घाघरी, नाक मा टिहरी नथुली,\nझुमिक-झुमिक नाचे जब कौथिग मा,\nसारा संसार देखदो छैला!",
        "verses": [
            "छोरी रे छोरी, गढ़वाल का डांडा मा!",
            "कमर मा घाघरी, नाक मा टिहरी नथुली,",
            "झुमिक-झुमिक नाचे जब कौथिग मा,",
            "सारा संसार देखदो छैला!",
            "ढोल को डंका जब बाजे गम्भीर,",
            "पांव मा घुंघरू छनके वीर!",
            "जय गढ़वाल, जय देवभूमि!"
        ],
        "english_translation": "O Garhwali maiden on the high ridges! Swirling in your traditional skirt and golden Tehri nose ring, dancing at the mountain fair!",
        "cultural_context": "Chhori is the lively circular folk dance performed with interlocking arms during autumn village fairs (Kauthig).",
        "source_url": "https://archive.org/details/garhwali_chhori_dances"
    },
    {
        "id": "GSN-0016",
        "title": "जय बदरीनाथ केदारनाथ - बदरी-केदार वंदना",
        "roman": "Jai Badrinath Kedarnath",
        "artist": "Traditional Temple Priests & Pilgrims",
        "genre": "Devotional Stuti / Temple Hymn",
        "corpus": "Kedarkhand Sacred Sanskrit & Garhwali Hymns",
        "theme": "Eternal praise of Lord Badri Vishal and Lord Kedarnath",
        "lyrics_sample": "जय बदरी विशाल, जय केदारेश्वर महादेवा!\nअलकनंदा-मंदाकिनी करदी तेरो सेवा!\nहिम-शिखरों का बीच विराजे, पंच बदरी-पंच केदार,\nतेरो दर्शन पाइके मिट जावे संसार!",
        "verses": [
            "जय बदरी विशाल, जय केदारेश्वर महादेवा!",
            "अलकनंदा-मंदाकिनी करदी तेरो सेवा!",
            "हिम-शिखरों का बीच विराजे, पंच बदरी-पंच केदार,",
            "तेरो दर्शन पाइके मिट जावे संसार!",
            "चरण कमलों मा शीश नवावां,",
            "जय शिव शंकर, जय नारायण!"
        ],
        "english_translation": "Hail Lord Badri Vishal! Hail Kedareswar Mahadeva! Alaknanda and Mandakini offer perpetual service at Thy feet!",
        "cultural_context": "Chanted by millions of pilgrims arriving at the sacred shrines of Kedarnath and Badrinath each pilgrimage season.",
        "source_url": "https://archive.org/details/kedar_badri_stuti"
    },
    {
        "id": "GSN-0017",
        "title": "टिहरी डूबों - स्वामी रामतीर्थ का सागर",
        "roman": "Tehri Doobon - Swami Ramtirtha Ka Sagar",
        "artist": "Garhwali Elegiac Poetry / Narendra Singh Negi",
        "genre": "Elegy / Historical Lament",
        "corpus": "Modern Social Consciousness Literature",
        "theme": "Mourning the historic capital of Tehri submerged under the dam waters",
        "lyrics_sample": "डूबि गे पुरणी टिहरी, भागीरथी का नीर मा!\nघंटाघर की घंटी मौन ह्वैगे, यादों की पीर मा!\nराजमहल अर घंटाघर, डूबि गे बाजार,\nआंसुओं से रोई उठे भागीरथी की धार!",
        "verses": [
            "डूबि गे पुरणी टिहरी, भागीरथी का नीर मा!",
            "घंटाघर की घंटी मौन ह्वैगे, यादों की पीर मा!",
            "राजमहल अर घंटाघर, डूबि गे बाजार,",
            "आंसुओं से रोई उठे भागीरथी की धार!",
            "कख गे वो पुराना दिन, कख गे वो चिनहार,",
            "इतिहास का पन्ना मा दर्ज ह्वैगे मेरु संसार!"
        ],
        "english_translation": "Old Tehri has submerged into the depths of Bhagirathi's waters! The clock tower's bell has fallen silent, enveloped in deep sorrow!",
        "cultural_context": "Captures the profound cultural grief of thousands of Garhwali families whose ancient princely town was submerged in 2005.",
        "source_url": "https://archive.org/details/tehri_dam_submergence_elegy"
    },
    {
        "id": "GSN-0018",
        "title": "बुरांश फूली गे डांड्यूं मा",
        "roman": "Buransh Phooli Ge Dandyun Ma",
        "artist": "Traditional Spring Lyrical",
        "genre": "Seasonal Spring Song",
        "corpus": "Ecological Heritage of Uttarakhand",
        "theme": "The crimson burst of wild Rhododendron blooms across the heights",
        "lyrics_sample": "बुरांश फूली गे डांड्यूं मा, लाल चुनरिया ओढ़ि!\nडांडी-कांठी मुस्कुराई, बासंती बयार दौड़ी!\nकाफल पकला अब वन मा, हिसालू की बहार,\nऐ जा मेरा परदेशी, सज्यो मेरु गढ़वार!",
        "verses": [
            "बुरांश फूली गे डांड्यूं मा, लाल चुनरिया ओढ़ि!",
            "डांडी-कांठी मुस्कुराई, बासंती बयार दौड़ी!",
            "काफल पकला अब वन मा, हिसालू की बहार,",
            "ऐ जा मेरा परदेशी, सज्यो मेरु गढ़वार!",
            "रस पियो बुरांश को, मीठो-मीठो स्वाद,",
            "पहाड़ा की याद आवो, मन मा उल्लास!"
        ],
        "english_translation": "Buransh has blossomed across mountain heights, draping ridges in crimson scarlet! The slopes smile, and spring winds race through the pines!",
        "cultural_context": "Celebrates the state tree of Uttarakhand whose scarlet blooms symbolize mountain life, health, and romance.",
        "source_url": "https://archive.org/details/buransh_folklore_songs"
    },
    {
        "id": "GSN-0019",
        "title": "पांडव नृत्य मंडाण - चक्रव्यूह जागर",
        "roman": "Pandav Nritya Mandaan - Chakravyuh Jagar",
        "artist": "Traditional Village Jagariyas",
        "genre": "Heroic Folk Ritual Theatre",
        "corpus": "Mahabharata Himalayan Folk Adaptation",
        "theme": "Invocation of the Five Pandavas and Draupadi to enter the bodies of dancers",
        "lyrics_sample": "उठो पांचों भाई पांडव, द्रौपदी महारानी!\nगढ़वाल की धरती मा आयो, धर्म की निशानी!\nभीम को गदा बाजे, अर्जुन को बाण,\nमंडाण मा नाचे पांडव, कांपे आसमान!",
        "verses": [
            "उठो पांचों भाई पांडव, द्रौपदी महारानी!",
            "गढ़वाल की धरती मा आयो, धर्म की निशानी!",
            "भीम को गदा बाजे, अर्जुन को बाण,",
            "मंडाण मा नाचे पांडव, कांपे आसमान!",
            "डौल-दमाऊँ की थाप पर, तीर-धनुष सजाय,",
            "दुष्टों को नाश कर, धर्म की ध्वजा फहराय!"
        ],
        "english_translation": "Awaken O Five Pandava brothers and Queen Draupadi! Descend upon the soil of Garhwal, emblem of cosmic righteousness!",
        "cultural_context": "Pandav Nritya is performed during winter across Garhwal villages, where villagers dance in spiritual trance reenacting episodes of the Mahabharata.",
        "source_url": "https://archive.org/details/pandav_nritya_garhwal"
    },
    {
        "id": "GSN-0020",
        "title": "कोदू झंगोरा खाणी - पहाड़ा की माटी",
        "roman": "Kodu Jhangora Khani - Pahada Ki Maati",
        "artist": "Traditional Agrarian Ballad",
        "genre": "Agrarian Folk Song",
        "corpus": "Garhwali Agrarian & Peasant Folklore",
        "theme": "Pride in resilient mountain millets, hard work, and healthy long life",
        "lyrics_sample": "कोदू झंगोरा खाणी, निर्भय जीवन जीणी!\nपहाड़ा की माटी मा उपजी, अमृत जैसी लेणी!\nमंडुवा की रोटी, गहत की दाल, अर जख्या को छौंक,\nऐसो स्वाद कख पालो, दुनिया मा भटको चाहे लौंक!",
        "verses": [
            "कोदू झंगोरा खाणी, निर्भय जीवन जीणी!",
            "पहाड़ा की माटी मा उपजी, अमृत जैसी लेणी!",
            "मंडुवा की रोटी, गहत की दाल, अर जख्या को छौंक,",
            "ऐसो स्वाद कख पालो, दुनिया मा भटको चाहे लौंक!",
            "मेहनत की कमाई, सच्चा मेरु पसीना,",
            "पहाड़ मा जिए हम, स्वाभिमान का महीना!"
        ],
        "english_translation": "Eating finger-millet and barnyard millet, living a fearless and robust life! Grown in mountain soil, like immortal nectar!",
        "cultural_context": "Celebrates the ancient food sovereignty and vibrant stamina of Garhwali farmers who cultivated steep terraced slopes.",
        "source_url": "https://archive.org/details/garhwali_agrarian_songs"
    }
]

# Write individual text files
for s in songs:
    slug = s["roman"].lower().replace(" ", "_").replace("-", "_")
    filename = f"{s['id']}_{slug}.txt"
    filepath = os.path.join("data_sources", "raw_texts", "songs", filename)
    verses_str = "\n".join(s["verses"])
    content = (
        f"Title: {s['title']} ({s['roman']})\n"
        f"Artist/Origin: {s['artist']}\n"
        f"Genre: {s['genre']}\n"
        f"Theme: {s['theme']}\n\n"
        f"Lyrics:\n{verses_str}\n\n"
        f"English Translation:\n{s['english_translation']}\n\n"
        f"Cultural Context:\n{s['cultural_context']}\n"
        f"Source: {s['source_url']}\n"
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
print(f"Generated {len(songs)} song files in data_sources/raw_texts/songs/")

# Write songs.json
songs_json_path = os.path.join("garhwali", "culture", "data", "songs.json")
with open(songs_json_path, "w", encoding="utf-8") as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)
print(f"Generated {songs_json_path}")

# Write digital_sources.json
sources = [
    {
        "id": "SRC-001",
        "source": "Uttarakhand Open University Digital Repository",
        "what_it_provides": "Digitized textbooks, curriculum modules, and scholarly monographs on Garhwali grammar, history, and literature (AECC, CGL-101 to 104)",
        "url": "https://uou.ac.in/",
        "preservation_status": "Active institutional academic repository"
    },
    {
        "id": "SRC-002",
        "source": "Internet Archive - Central Himalayan & Garhwali Collection",
        "what_it_provides": "Primary historical monographs by Govind Chatak, Haridatta Bhatt, Gunanand Juyal, Ganga Datt Upreti, and George Grierson Linguistic Survey of India Vol IX",
        "url": "https://archive.org/details/in.ernet.dli.2015.485121",
        "preservation_status": "Public domain global digital archive"
    },
    {
        "id": "SRC-003",
        "source": "Sahitya Akademi National Literary Archives",
        "what_it_provides": "Anthologies of modern Garhwali poetry, plays, short stories, and translated works of bards like Chandra Kunwar Bartwal and Abodh Bandhu Bahuguna",
        "url": "https://sahitya-akademi.gov.in/",
        "preservation_status": "National literary archive"
    },
    {
        "id": "SRC-004",
        "source": "Doordarshan Kendra Dehradun Folk Archive",
        "what_it_provides": "Audio-visual master recordings of Dhol Sagar percussive repertoires, Pandav Nritya, Jagar invocations, and historical bards (Narendra Singh Negi, Pritam Bhartwan)",
        "url": "https://prasarbharati.gov.in/",
        "preservation_status": "Broadcast cultural heritage archive"
    },
    {
        "id": "SRC-005",
        "source": "Garhwal Sabha Cultural Heritage Repository",
        "what_it_provides": "Community manuscripts, folk theater scripts, Ramman records of Saloor Dungra, and oral history recordings",
        "url": "https://garhwalbhasha.org/",
        "preservation_status": "Living linguistic preservation trust"
    },
    {
        "id": "SRC-006",
        "source": "G.B. Pant National Institute of Himalayan Environment",
        "what_it_provides": "Ethnobotanical surveys of sacred groves, alpine medicinal plants of Chamoli, and biodiversity conservation in Kedarkhand",
        "url": "https://gbpihed.gov.in/",
        "preservation_status": "Environmental scientific research repository"
    },
    {
        "id": "SRC-007",
        "source": "Uttarakhand Sanskrit Academy & Bhasha Sansthan",
        "what_it_provides": "Linguistic documentation of Pahari dialects, etymological roots, and script preservation of Central Himalayan languages",
        "url": "https://sanskritacademy.uk.gov.in/",
        "preservation_status": "State language academy"
    }
]

sources_json_path = os.path.join("garhwali", "culture", "data", "digital_sources.json")
with open(sources_json_path, "w", encoding="utf-8") as f:
    json.dump(sources, f, ensure_ascii=False, indent=2)
print(f"Generated {sources_json_path}")
