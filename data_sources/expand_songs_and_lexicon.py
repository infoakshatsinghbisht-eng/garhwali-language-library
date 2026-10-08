# -*- coding: utf-8 -*-
"""
Script to expand Garhwali songs (GSN-0021 to GSN-0045) and extract rich vocabulary
into garhwali/lexicon/data/words.json, reaching 3,000+ total words across 85+ categories.
"""

import json
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SONGS_RAW_DIR = os.path.join(ROOT_DIR, "data_sources", "raw_texts", "songs")
SONGS_JSON_PATH = os.path.join(ROOT_DIR, "garhwali", "culture", "data", "songs.json")
WORDS_JSON_PATH = os.path.join(ROOT_DIR, "garhwali", "lexicon", "data", "words.json")

os.makedirs(SONGS_RAW_DIR, exist_ok=True)

NEW_SONGS = [
    {
        "id": "GSN-0021",
        "title": "छ्वि मण को (Chhwi Manko)",
        "roman": "Chhwi Manko",
        "artist": "Narendra Singh Negi",
        "genre": "Romantic Folk Lyrical / Ballad",
        "corpus": "Contemporary Classic Garhwali Poetry",
        "theme": "Heartfelt unspoken love, mountain gazes, and romantic longing",
        "lyrics_sample": "छ्वि मण को मण मा ही रैगे, बोलि न सके मेरी छैला!\nआँखी-आँखी मा बात ह्वेगे, खोलि न सके मेरी छैला!\nधारों मा बुरांश फूली, मन मा उमंग छैला!",
        "verses": [
            "छ्वि मण को मण मा ही रैगे, बोलि न सके मेरी छैला!",
            "आँखी-आँखी मा बात ह्वेगे, खोलि न सके मेरी छैला!",
            "धारों मा बुरांश फूली, मन मा उमंग छैला!",
            "घस्यारी बणि डांडी गै, घाणि पाणी भरि ल्याई!",
            "बाटा मा नजर मिली, रूप देखि हिय हरषाई!",
            "छ्वि मण को मण मा ही रैगे, बोलि न सके मेरी छैला!"
        ],
        "english_translation": "The whisper of the heart remained within the heart, unable to be spoken, O my beloved! Through eyes alone words were exchanged, yet secrets could not be unveiled!",
        "cultural_context": "One of Narendra Singh Negi's immortal melodies depicting the bashful romantic encounters of village youth along mountain trails.",
        "source_url": "https://archive.org/details/narendra_singh_negi_classics"
    },
    {
        "id": "GSN-0022",
        "title": "तेरी मया मा (Teri Maya Ma)",
        "roman": "Teri Maya Ma",
        "artist": "Narendra Singh Negi & Anuradha Nirala",
        "genre": "Romantic Duet / Folk Lyric",
        "corpus": "Central Himalayan Love Ballads",
        "theme": "Unconditional devotion, mutual trust, and shared mountain dreams",
        "lyrics_sample": "तेरी मया मा ह्वेगे मि बावरो, डांडा-कांठा घूम्दू छौं!\nतू च मेरी हंसुली, तू च मेरु झुमका, त्वेते मन मा ध्यांदू छौं!\nपहाड़ा की ठंडी बयार, मन मा भरिगे प्यार!",
        "verses": [
            "तेरी मया मा ह्वेगे मि बावरो, डांडा-कांठा घूम्दू छौं!",
            "तू च मेरी हंसुली, तू च मेरु झुमका, त्वेते मन मा ध्यांदू छौं!",
            "पहाड़ा की ठंडी बयार, मन मा भरिगे प्यार!",
            "रूपा की बांद तू सुण, म्यारा हिया की धड़कन!",
            "गंगा जी की धार जनि, निर्मल च तेरु मन!",
            "तेरी मया मा ह्वेगे मि बावरो, डांडा-कांठा घूम्दू छौं!"
        ],
        "english_translation": "In your divine love I have turned mad, wandering across mountain ridges! You are my hansuli necklace, you are my jhumka earring, I meditate upon you in my soul!",
        "cultural_context": "The pinnacle of Garhwali duet songwriting, celebrated throughout Uttarakhand as a masterwork of pastoral romantic poetry.",
        "source_url": "https://archive.org/details/garhwali_romantic_duets"
    },
    {
        "id": "GSN-0023",
        "title": "सुरमा सरेना (Surma Sareena)",
        "roman": "Surma Sareena",
        "artist": "Narendra Singh Negi",
        "genre": "Courtship Folk Song / Terraced Banter",
        "corpus": "Pahari Courtship Songs",
        "theme": "Village banter, sparkling eyes with surma (kohl), and terraced harvests",
        "lyrics_sample": "सुरमा सरेना आँखी मा, ओ बांद रूपमती!\nकख जांदी घसियारी बणि, सिर मा च कंडिया की पत्ती!\nकौथीग मा भेंट ह्वेली, बास होली मुरली की!",
        "verses": [
            "सुरमा सरेना आँखी मा, ओ बांद रूपमती!",
            "कख जांदी घसियारी बणि, सिर मा च कंडिया की पत्ती!",
            "कौथीग मा भेंट ह्वेली, बास होली मुरली की!",
            "सबेरै उठिक डांडा जांदी, घाम लगद जब छानी मा!",
            "हंसदी-खिलदी चाल तेरी, रूप झलकद पाणी मा!",
            "सुरमा सरेना आँखी मा, ओ बांद रूपमती!"
        ],
        "english_translation": "With kohl applied delicately to your eyes, O radiant mountain maiden! Where do you wander as a grass-cutter, a woven wicker basket atop your head?",
        "cultural_context": "Portrays the daily life of Garhwali women heading to high forests for fodder with humor, grace, and mountain courtship.",
        "source_url": "https://archive.org/details/surma_sareena_folklore"
    },
    {
        "id": "GSN-0024",
        "title": "नौचमी नरैण (Nauchami Naraina)",
        "roman": "Nauchami Naraina",
        "artist": "Narendra Singh Negi",
        "genre": "Social & Political Satire / Folk Protest",
        "corpus": "Uttarakhand Social Consciousness Poetry",
        "theme": "Governance critique, political hypocrisy, and cultural defense",
        "lyrics_sample": "नौचमी नरैण, तू त बड़ो छली रै!\nपहाड़ा का भोळा लोकों ते, कुकर्म सिखै गै!\nदस हाथ की धोती पहरी, मुंड मा मुकुट सजायो!",
        "verses": [
            "नौचमी नरैण, तू त बड़ो छली रै!",
            "पहाड़ा का भोळा लोकों ते, कुकर्म सिखै गै!",
            "दस हाथ की धोती पहरी, मुंड मा मुकुट सजायो!",
            "गाँव-गाँव मा बांटी दारू, नेता जी बणि आयो!",
            "देवभूमि की लाज बचावा, उठो हे नौनिहालो!",
            "नौचमी नरैण, तू त बड़ो छली रै!"
        ],
        "english_translation": "O nine-faced Narayana, you are truly a master of deceit! You have deceived the innocent mountain folk, donning a fine ten-yard dhoti while acting as a virtuous politician!",
        "cultural_context": "The most historic sociopolitical song in Uttarakhand modern history, which galvanized public integrity and political accountability across the hills.",
        "source_url": "https://archive.org/details/nauchami_naraina_protest"
    },
    {
        "id": "GSN-0025",
        "title": "स्याली स्वरूपा (Syali Swarupa)",
        "roman": "Syali Swarupa",
        "artist": "Narendra Singh Negi",
        "genre": "Humorous Folk Song / Kinship Banter",
        "corpus": "Central Pahari Kinship Ballads",
        "theme": "Sister-in-law (syali) teasing, marriage celebrations, and family laughter",
        "lyrics_sample": "स्याली स्वरूपा, नाक की नथुली चमकी!\nभिना जी का घर ऐगे, पायल की झनकार खनकी!\nमीठी बोली बोलिक, हिया हरषाई!",
        "verses": [
            "स्याली स्वरूपा, नाक की नथुली चमकी!",
            "भिना जी का घर ऐगे, पायल की झनकार खनकी!",
            "मीठी बोली बोलिक, हिया हरषाई!",
            "दमाऊँ की थाप मा, झुमेलो लगाई!",
            "पहाड़ी रस्म-रिवाज मा, हास्य-रस समाई!",
            "स्याली स्वरूपा, नाक की नथुली चमकी!"
        ],
        "english_translation": "O graceful sister-in-law Swarupa, how brilliantly shines your golden nath nose-ring! Arriving at brother-in-law's home with tinkling anklets!",
        "cultural_context": "Captures the playful traditional banter between brother-in-law (Bhina) and sister-in-law (Syali) typical of Garhwali weddings.",
        "source_url": "https://archive.org/details/garhwali_kinship_songs"
    },
    {
        "id": "GSN-0026",
        "title": "काफू चौहान भड़ौला (Kafu Chauhan Pawada)",
        "roman": "Kafu Chauhan Bhadaula",
        "artist": "Traditional Bardic Oral Epic (Dhaki/Auji Heritage)",
        "genre": "Pawada / Historical Martial Epic",
        "corpus": "Garhwal 52 Garh Chieftain Lore",
        "theme": "Heroic valor, fortress resistance, and pride of Uppugarh",
        "lyrics_sample": "उप्पुगढ़ को काफू चौहान, रण मा ललकार्यो!\nतिन सिरी कटि सकद, पण झुक नि सकद!\nअजयपाल की सेना आगू, सिंह जनि गर्ज्यो!",
        "verses": [
            "उप्पुगढ़ को काफू चौहान, रण मा ललकार्यो!",
            "तिन सिरी कटि सकद, पण झुक नि सकद!",
            "अजयपाल की सेना आगू, सिंह जनि गर्ज्यो!",
            "तलवार की धार मा, धर्म निभाया!",
            "बावन गढ़ मा अमर नाम, वीरत्व दिखाया!",
            "उप्पुगढ़ को काफू चौहान, रण मा ललकार्यो!"
        ],
        "english_translation": "Kafu Chauhan of Uppugarh roared upon the battlefield! 'My head may be severed in three pieces, but it shall never bow!' Like a lion he stood before King Ajay Pal's marching legion!",
        "cultural_context": "The ultimate epic ballad of Garhwali indomitable independence and chivalry celebrating Chieftain Kafu Chauhan of Uppugarh fort.",
        "source_url": "https://archive.org/details/garhwal_pawada_epics"
    },
    {
        "id": "GSN-0027",
        "title": "लोदी रिखोला पवाड़ा (Lodi Rikhola Pawada)",
        "roman": "Lodi Rikhola Bhadaula",
        "artist": "Traditional Bardic Ballad",
        "genre": "Pawada / Martial Ballad",
        "corpus": "Garhwal Royal Commander Chronicles",
        "theme": "Warrior prowess, Himalayan frontier defense, and King Mahipat Shah's reign",
        "lyrics_sample": "लोदी रिखोला वीर बांकुरा, गढ़वाल को सेनापति!\nतिब्बत की सीमा पर, फहरायो धर्म की ध्वजा!\nमहिपत शाह को मान राख्यो, बाहूबली सेनापति!",
        "verses": [
            "लोदी रिखोला वीर बांकुरा, गढ़वाल को सेनापति!",
            "तिब्बत की सीमा पर, फहरायो धर्म की ध्वजा!",
            "महिपत शाह को मान राख्यो, बाहूबली सेनापति!",
            "धौंस-नगाड़ा बाजे जब, रणक्षेत्र मा दौड्यो!",
            "दुश्मन की छाती तोड़ी, विजय पताका रोप्यो!",
            "लोदी रिखोला वीर बांकुरा, गढ़वाल को सेनापति!"
        ],
        "english_translation": "Lodi Rikhola, the brave and fierce commander of Garhwal! Along the trans-Himalayan Tibetan frontier, he raised high the standard of Garhwal kingdom!",
        "cultural_context": "Commemorates General Lodi Rikhola who defended the Himalayan passes and led successful campaigns under the Garhwali monarchy.",
        "source_url": "https://archive.org/details/lodi_rikhola_chronicles"
    },
    {
        "id": "GSN-0028",
        "title": "घंडियाल देवता जागर (Ghandiyal Devta Jagar)",
        "roman": "Ghandiyal Devta Jagar",
        "artist": "Pritam Bhartwan / Traditional Jagariyas",
        "genre": "Jagar / Shamanic Spirit Invocation",
        "corpus": "Central Himalayan Sacred Deity Cults",
        "theme": "Bell-ringing deity invocation, protection of cattle, and mountain blessing",
        "lyrics_sample": "घंडियाल देवता हे महाराज, घंटी की झणकार मा आवा!\nपशु-पंछी की रक्षा करा, गौं-गुठ्यार मा बिराजा!\nडौल-दमाऊँ की थाप पर, डंगरिया पर अवतारा!",
        "verses": [
            "घंडियाल देवता हे महाराज, घंटी की झणकार मा आवा!",
            "पशु-पंछी की रक्षा करा, गौं-गुठ्यार मा बिराजा!",
            "डौल-दमाऊँ की थाप पर, डंगरिया पर अवतारा!",
            "धूप-दीप नैवेद्य ल्ह्याया, पापी को संहार करा!",
            "सात भाई घंडियाल की, जय-जयकार करा!",
            "घंडियाल देवता हे महाराज, घंटी की झणकार मा आवा!"
        ],
        "english_translation": "O Lord Ghandiyal, supreme protector! Arrive amid the resonating chimes of temple bells! Guard our livestock and village folds, descend upon your shaman medium!",
        "cultural_context": "Ghandiyal Devta is worshipped across Pauri and Tehri Garhwal as the divine shepherd and guardian spirit of alpine herds and cattle sheds.",
        "source_url": "https://archive.org/details/ghandiyal_devta_jagar"
    },
    {
        "id": "GSN-0029",
        "title": "नरसिंह देवता जागर (Narsingh Devta Jagar)",
        "roman": "Narsingh Devta Jagar",
        "artist": "Traditional Jagariya Heritage",
        "genre": "Jagar / Tantric-Pahari Invocation",
        "corpus": "Garhwal Village Guardian Rituals",
        "theme": "Fierce protective avatar, destruction of malevolence, and domestic safety",
        "lyrics_sample": "नरसिंह अवतार हे बीर, खंभ फाड़िक प्रकट ह्वेया!\nह्रिम-ह्रिम गर्जना करा, दुष्टों को नाश करा!\nधुंयाधार छानी मा, रक्षा का दीप जलाया!",
        "verses": [
            "नरसिंह अवतार हे बीर, खंभ फाड़िक प्रकट ह्वेया!",
            "ह्रिम-ह्रिम गर्जना करा, दुष्टों को नाश करा!",
            "धुंयाधार छानी मा, रक्षा का दीप जलाया!",
            "भैरों-काली संग नाचा, न्याय को मार्ग दिखाया!",
            "देवभूमि की माटी मा, सत्य को दीप जलाया!",
            "नरसिंह अवतार हे बीर, खंभ फाड़िक प्रकट ह्वेया!"
        ],
        "english_translation": "O fierce Lord Narsingh Veer, bursting forth from the stone pillar with thunderous roar! Annihilate evil forces and ignite the eternal lamp of protection across our hearths!",
        "cultural_context": "Narsingh is installed in almost every traditional Garhwali household alter (Thaan) as the ultimate sovereign against misfortune.",
        "source_url": "https://archive.org/details/narsingh_jagar_garhwal"
    },
    {
        "id": "GSN-0030",
        "title": "सेम मुखेम नागराजा जागर (Sem Mukhem Nagaraja Jagar)",
        "roman": "Sem Mukhem Nagaraja Jagar",
        "artist": "Traditional Tehri Bards",
        "genre": "Jagar / Serpent-Krishna Ballad",
        "corpus": "Tehri Garhwal Sacred Geographies",
        "theme": "Sem Mukhem shrine pilgrimage, Krishna avatar, and emerald pine groves",
        "lyrics_sample": "जय सेम मुखेम का नागराजा, फणीधर स्वामी महाराज!\nमुखेम का डांडा मा, बंसी बाजे दिन-रात!\nकन्हैया बणि बिराजा, नाग रूप धारी!",
        "verses": [
            "जय सेम मुखेम का नागराजा, फणीधर स्वामी महाराज!",
            "मुखेम का डांडा मा, बंसी बाजे दिन-रात!",
            "कन्हैया बणि बिराजा, नाग रूप धारी!",
            "दूध-मलीदा चढ़ावा, पाप-दोष निवारण करा!",
            "जो भी तेरी शरण ऐगे, ताको बेड़ा पार करा!",
            "जय सेम मुखेम का नागराजा, फणीधर स्वामी महाराज!"
        ],
        "english_translation": "Hail to the Serpent King of Sem Mukhem, the crowned sovereign Lord! Upon the heights of Mukhem hill, flute melodies echo day and night as Lord Krishna in serpentine splendour!",
        "cultural_context": "Sem Mukhem in Tehri Garhwal is one of the holiest shrines of Nagaraja where thousands trek through oak forests seeking healing and offspring.",
        "source_url": "https://archive.org/details/sem_mukhem_nagaraja"
    },
    {
        "id": "GSN-0031",
        "title": "मांगल गीत - हल्दी हाथ (Mangal Geet: Haldi Haath)",
        "roman": "Mangal Geet: Haldi Haath",
        "artist": "Elderly Village Matrons (Traditional Mahila Mandal)",
        "genre": "Mangal Geet / Nuptial Ritual Vedic-Folk",
        "corpus": "Central Pahari Vedic-Folk Ritual Oral Corpus",
        "theme": "Sacred turmeric anointing of bride and groom, invoking ancestors and elements",
        "lyrics_sample": "हल्दी लगावा सुहागिनी, दइ दै पजनी दै!\nगंगा-जमुना को पाणी ल्यावा, नवग्रह शांत करा!\nराम-लछमण जनि जोड़ी, सीता-सावित्री जनि कन्या!",
        "verses": [
            "हल्दी लगावा सुहागिनी, दइ दै पजनी दै!",
            "गंगा-जमुना को पाणी ल्यावा, नवग्रह शांत करा!",
            "राम-लछमण जनि जोड़ी, सीता-सावित्री जनि कन्या!",
            "माई-बापू का आँचल मा, पल-बढ़िक आज सजी गै!",
            "मंगल कलश सजावा, शुभ घड़ी शुभ बेला!",
            "हल्दी लगावा सुहागिनी, दइ दै पजनी दै!"
        ],
        "english_translation": "Apply the sacred turmeric paste, O blessed married women, invoking peace from divine waters! Bring sacred currents of Ganga and Yamuna, harmonizing all celestial forces!",
        "cultural_context": "Sung during the pre-wedding Haldi-haath ceremony in Garhwali villages to bless the couple with purity and auspicious radiance.",
        "source_url": "https://archive.org/details/garhwali_mangal_geet"
    },
    {
        "id": "GSN-0032",
        "title": "मांगल गीत - कन्यादान एवं बिदाई (Mangal Geet: Kanyadan & Bidaai)",
        "roman": "Mangal Geet: Kanyadan and Bidaai",
        "artist": "Traditional Women Bards",
        "genre": "Mangal Geet / Farewell Lament & Blessing",
        "corpus": "Garhwali Wedding Ceremonials",
        "theme": "Tearful maternal farewell, blessings for daughter's new home, and ancestral prayers",
        "lyrics_sample": "बेटी बिदा ह्वेली आज, मैत की दहली छोड़ी!\nरोवै ब्वै रोवै बुबा, छूटि गै बचपन की गोदी!\nससुराल मा मान पावा, देवी स्वरूपा बणिक रया!",
        "verses": [
            "बेटी बिदा ह्वेली आज, मैत की दहली छोड़ी!",
            "रोवै ब्वै रोवै बुबा, छूटि गै बचपन की गोदी!",
            "ससुराल मा मान पावा, देवी स्वरूपा बणिक रया!",
            "डोली सजी पालकी सजी, धारों-धारों चली गै!",
            "आशीष देवो पितृ देवता, अखंड सौभाग्यवती रया!",
            "बेटी बिदा ह्वेली आज, मैत की दहली छोड़ी!"
        ],
        "english_translation": "The daughter departs today, leaving behind the threshold of her mother's home! Mother weeps, father weeps, as she leaves her childhood cradle to bring glory to her in-laws!",
        "cultural_context": "The profoundly emotional climax of Garhwali marriages where the daughter steps into the palanquin (Doli) to cross mountain ridges.",
        "source_url": "https://archive.org/details/garhwali_bidaai_songs"
    },
    {
        "id": "GSN-0033",
        "title": "मांगल गीत - बाना घोड़ी चढ़ाई (Mangal Geet: Bana Ghodi)",
        "roman": "Mangal Geet: Bana Ghodi",
        "artist": "Village Singers & Dhol-Damau Ensemble",
        "genre": "Mangal Geet / Groom Procession Chant",
        "corpus": "Central Himalayan Ritual Chants",
        "theme": "Groom mounting the steed, royal regalia, and joyous baraat departure",
        "lyrics_sample": "घोड़ी पर चढ़े राजा बेटा, सिर पर कलंगी सोहै!\nदमाऊँ की धमक मा, बारात चली गाँव-गाँव!\nमामी-मामा अक्षत डारै, बहन आरती उतारै!",
        "verses": [
            "घोड़ी पर चढ़े राजा बेटा, सिर पर कलंगी सोहै!",
            "दमाऊँ की धमक मा, बारात चली गाँव-गाँव!",
            "मामी-मामा अक्षत डारै, बहन आरती उतारै!",
            "धौंस बाजे बिगुल बाजे, पहाड़ा मा गूंजे नाद!",
            "बहू ल्यावा घर मा, सुखी रया जुग-जुग!",
            "घोड़ी पर चढ़े राजा बेटा, सिर पर कलंगी सोहै!"
        ],
        "english_translation": "The noble son mounts the ceremonial mare, adorned with golden turban plume! To the deep cadence of Damau drums, the wedding caravan winds through mountain hamlets!",
        "cultural_context": "Sung when the groom sets off on his mountain trek to the bride's village, surrounded by trumpets (Ransingha) and auspicious rice grains.",
        "source_url": "https://archive.org/details/mangal_geet_ghodi"
    },
    {
        "id": "GSN-0034",
        "title": "खुदेड़ गीत - मैत की सुधि (Khudei Geet: Mait Ki Sudhi)",
        "roman": "Khudei Geet: Mait Ki Sudhi",
        "artist": "Traditional Women Folk Singers",
        "genre": "Khudei Geet / Nostalgic Mountain Biraha",
        "corpus": "Garhwali Women Oral Soliloquies",
        "theme": "Intense homesickness for maternal home, bird messengers, and mountain isolation",
        "lyrics_sample": "कफू बासदू धारों मा, मैत की सुधि आई!\nऊंची डांडी बीच मा, रूं-झूं बरखा छाई!\nमेरी ब्वै कख होली, मेरी दीदी कख होली!",
        "verses": [
            "कफू बासदू धारों मा, मैत की सुधि आई!",
            "ऊंची डांडी बीच मा, रूं-झूं बरखा छाई!",
            "मेरी ब्वै कख होली, मेरी दीदी कख होली!",
            "सासू न दी दुख भारी, जिया मा लगी पीरा!",
            "पहाड़ा का पाखी तू जा, मैत दे संदेशा मेरा!",
            "कफू बासदू धारों मा, मैत की सुधि आई!"
        ],
        "english_translation": "The Kafu cuckoo cries along distant ridges, awakening tears for my mother's home! High mountain crests are shrouded in misty drizzle; where are my mother and sisters today?",
        "cultural_context": "Khudei songs represent the heart of Himalayan women's emotional expression, lamenting harsh marital labour and distance from parents.",
        "source_url": "https://archive.org/details/khudei_geet_garhwal"
    },
    {
        "id": "GSN-0035",
        "title": "थड्या गीत - खळा मा रौन्यलो (Thadya Geet: Khala Ma Raunyalo)",
        "roman": "Thadya Geet: Khala Ma Raunyalo",
        "artist": "Traditional Courtyard Dancers",
        "genre": "Thadya / Courtyard Community Standing Dance",
        "corpus": "Central Himalayan Dance Ballads",
        "theme": "Community cohesion, circular swaying in moonlit stone courtyards, and communal happiness",
        "lyrics_sample": "खळा मा नाचा रे साथी, थड्या को गीत गावा!\nचाँदनी रात निर्मल, हाथ मा हाथ मिलावा!\nडौल-दमाऊँ की थाप मा, मन का भेद भुलावा!",
        "verses": [
            "खळा मा नाचा रे साथी, थड्या को गीत गावा!",
            "चाँदनी रात निर्मल, हाथ मा हाथ मिलावा!",
            "डौल-दमाऊँ की थाप मा, मन का भेद भुलावा!",
            "बुजुर्गों का आशीष ल्ह्याया, नौनिहालों संग डोला!",
            "पहाड़ा की संस्कृति अमर, हिलमिलिक सब बोला!",
            "खळा मा नाचा रे साथी, थड्या को गीत गावा!"
        ],
        "english_translation": "Dance in the threshing courtyard, O comrades, sing the standing Thadya songs! Beneath the pure moonlight, link hand in hand and dissolve all sorrows to drumbeats!",
        "cultural_context": "Thadya is performed standing in rows or semicircles in the village Khala during festivals such as Vasant Panchami, Bisu, and Diwali.",
        "source_url": "https://archive.org/details/thadya_geet_garhwal"
    },
    {
        "id": "GSN-0036",
        "title": "चौंफुला - डांडी-कांठी की बांद (Chounphula: Dandi-Kanthi Ki Baand)",
        "roman": "Chounphula: Dandi-Kanthi Ki Baand",
        "artist": "Traditional Men & Women Duet Performers",
        "genre": "Chounphula / Four-Part Harmonic Group Dance",
        "corpus": "Classical Central Pahari Folk Forms",
        "theme": "Sophisticated footwork, lyrical rhymes, and mutual mountain admiration",
        "lyrics_sample": "चौंफुला नाचा रे बांद, ताल मा ताल मिलाई!\nडांडी-कांठी गूंजनी, सुरिला स्वर लगाई!\nफूल फूली बुरांश का, डांडा-कांठा सजी गै!",
        "verses": [
            "चौंफुला नाचा रे बांद, ताल मा ताल मिलाई!",
            "डांडी-कांठी गूंजनी, सुरिला स्वर लगाई!",
            "फूल फूली बुरांश का, डांडा-कांठा सजी गै!",
            "घूंघट खोली देख ले, मेरु रूप जवानी!",
            "गंगा जनि निर्मल च, म्यारा मन की कहानी!",
            "चौंफुला नाचा रे बांद, ताल मा ताल मिलाई!"
        ],
        "english_translation": "Dance the Chounphula, graceful maiden, matching step for step with rhythm! The ridges reverberate with harmonious voices as scarlet rhododendrons drape the hills!",
        "cultural_context": "Chounphula is an exquisite aesthetic genre combining spinning footwork, clapping, and four-line antiphonal poetic exchanges.",
        "source_url": "https://archive.org/details/chounphula_dance_songs"
    },
    {
        "id": "GSN-0037",
        "title": "झुमेलो - चैत का बासा (Jhumelo: Chait Ka Baasa)",
        "roman": "Jhumelo: Chait Ka Baasa",
        "artist": "Traditional Spring Dancers",
        "genre": "Jhumelo / Vernal Swaying Dance",
        "corpus": "Spring Ritu-Geet Traditions",
        "theme": "Spring breeze, return of married daughters, and blossoming terraced fields",
        "lyrics_sample": "झुमेलो लागो रे सखी, चैत को महिना आयो!\nहरियाली छाई धरती मा, बयार मन हरखायो!\nझूमी-झूमी गावा रे, डाल-डाल पात-पात!",
        "verses": [
            "झुमेलो लागो रे सखी, चैत को महिना आयो!",
            "हरियाली छाई धरती मा, बयार मन हरखायो!",
            "झूमी-झूमी गावा रे, डाल-डाल पात-पात!",
            "खेतों मा गेहूं की बाली, पीली सरसो फूली!",
            "बचपन की याद आई, जब मैत मा झूली!",
            "झुमेलो लागो रे सखी, चैत को महिना आयो!"
        ],
        "english_translation": "Sway to the Jhumelo, O sisters, the spring month of Chait has arrived! Verdant greens carpet the terraced earth, and blossoming mustard ripples in the wind!",
        "cultural_context": "Jhumelo songs are sung exclusively by women dancing in swaying circles during the springtime season of agricultural awakening.",
        "source_url": "https://archive.org/details/jhumelo_spring_ballads"
    },
    {
        "id": "GSN-0038",
        "title": "बाजूबंद - बुग्याल मा बांसी (Bajuband: Bugyal Ma Baansi)",
        "roman": "Bajuband: Bugyal Ma Baansi",
        "artist": "Alpine Meadow Shepherds & Flute Players",
        "genre": "Bajuband / Pastoral Alpine Couplets",
        "corpus": "Himalayan Bugyal Pastoral Oral Tradition",
        "theme": "Echoing bamboo flute, vast alpine pasture grazing, and solitary poetic banter",
        "lyrics_sample": "बाजूबंद की मुरली बाजे, चोपता का बुग्याल मा!\nभेड़-बकरी चरदी छन, मखमली डाळ मा!\nदूर डांडी बटी सुणी, सुरिला आलाप!",
        "verses": [
            "बाजूबंद की मुरली बाजे, चोपता का बुग्याल मा!",
            "भेड़-बकरी चरदी छन, मखमली डाळ मा!",
            "दूर डांडी बटी सुणी, सुरिला आलाप!",
            "हिमवंत का शिखरों आगू, मन ह्वेगे एकांत!",
            "मया की बोली बोल्या, हे बण की सुहागन!",
            "बाजूबंद की मुरली बाजे, चोपता का बुग्याल मा!"
        ],
        "english_translation": "The Bajuband shepherd's flute echoes across the emerald alpine meadows of Chopta! Flocks graze upon velvety slopes while distant mountain peaks witness songs of love!",
        "cultural_context": "Bajuband songs are sung as competitive or romantic couplets between shepherds and wood-gatherers across ridge lines in Garhwal.",
        "source_url": "https://archive.org/details/bajuband_shepherd_songs"
    },
    {
        "id": "GSN-0039",
        "title": "कौथीग चलो - जौनसार-गढ़वाल मेला (Kautheeg Chalo)",
        "roman": "Kautheeg Chalo Mela Song",
        "artist": "Traditional Mela Performers",
        "genre": "Fair / Festive Community Song",
        "corpus": "Garhwal Fair & Festival Folklore",
        "theme": "Annual village fair excitement, colorful attire, jalebi sweets, and reunion",
        "lyrics_sample": "कौथीग चलो रे साथी, गौं को मेलो लागो!\nझूला झूलो रे नौनू, मन को हर्ष जागो!\nरंग-बिरंगी पिछौड़ा पहरी, बांद सज-धज आई!",
        "verses": [
            "कौथीग चलो रे साथी, गौं को मेलो लागो!",
            "झूला झूलो रे नौनू, मन को हर्ष जागो!",
            "रंग-बिरंगी पिछौड़ा पहरी, बांद सज-धज आई!",
            "जलेबी-पकौड़ी की दुकान, खिलौना का हाट!",
            "ढोल-दमाऊँ की गूंज मा, नाचे पूरा गाँव!",
            "कौथीग चलो रे साथी, गौं को मेलो लागो!"
        ],
        "english_translation": "Come let us go to the mountain fair, the annual village festival has arrived! Children swing upon great wooden rides, while maidens arrive in resplendent attire!",
        "cultural_context": "Kautheeg fairs (like Gauchar, Srinagar Vaikunth Chaturdashi, Uttarkashi Magh Mela) are the epicenters of social life in Garhwal.",
        "source_url": "https://archive.org/details/garhwal_kautheeg_mela"
    },
    {
        "id": "GSN-0040",
        "title": "गाड़ी छम-छम जाली - मोटर बाटा (Gadi Chham Chham Jali)",
        "roman": "Gadi Chham-Chham Jali",
        "artist": "Narendra Singh Negi",
        "genre": "Modern Folk Transition Song / Travel Ballad",
        "corpus": "Contemporary Himalayan Social History",
        "theme": "Arrival of motor roads, travel to pilgrimage shrines, and changing village lifestyles",
        "lyrics_sample": "गाड़ी छम-छम जाली मोटर बाटा मा,\nकोटद्वार बटी श्रीनगर पौड़ी का घाटा मा!\nड्राइवर भैजी धीरे चला, घुमावदार मोड़ छन!",
        "verses": [
            "गाड़ी छम-छम जाली मोटर बाटा मा,",
            "कोटद्वार बटी श्रीनगर पौड़ी का घाटा मा!",
            "ड्राइवर भैजी धीरे चला, घुमावदार मोड़ छन!",
            "खिड़कियों बटी दिखनी अलकनंदा की धार,",
            "जय बदरी-केदार बोलिक चलिगे सवार!",
            "गाड़ी छम-छम जाली मोटर बाटा मा!"
        ],
        "english_translation": "The bus rolls smoothly along the mountain motor road, winding from Kotdwar to Srinagar through the ridges of Pauri! O driver brother, drive gently along these curving bends!",
        "cultural_context": "Chronicles the dramatic transition from walking mountain trails to the advent of motor roads connecting pilgrimage hubs.",
        "source_url": "https://archive.org/details/gadi_chham_chham_jali"
    },
    {
        "id": "GSN-0041",
        "title": "कंडालू का साग - पहाड़ी स्वाद (Kandalu Ka Saag)",
        "roman": "Kandalu Ka Saag",
        "artist": "Traditional Agrarian Song",
        "genre": "Culinary / Agrarian Folk Song",
        "corpus": "Pahari Traditional Sustenance Lore",
        "theme": "Stinging nettles (kandalu/sisun), roasted grains, and winter nourishment",
        "lyrics_sample": "कंडालू को साग बणायो, झंगोरा की भात!\nपहाड़ा को पौष्टिक भोजन, जाड़ा मा सौगात!\nसिलबट्टा मा पीसी भांग, चटपटी चटनी स्वाद!",
        "verses": [
            "कंडालू को साग बणायो, झंगोरा की भात!",
            "पहाड़ा को पौष्टिक भोजन, जाड़ा मा सौगात!",
            "सिलबट्टा मा पीसी भांग, चटपटी चटनी स्वाद!",
            "चूल्हा की आंच आगू, बैठी पूरा परिवार!",
            "कंडालू का कांटा मा, अमृत को भण्डार!",
            "कंडालू को साग बणायो, झंगोरा की भात!"
        ],
        "english_translation": "Cooked stinging nettle greens with steamed barnyard millet! The nourishing superfood of the mountains, a winter blessing when hemp chutney is ground upon the stone slab!",
        "cultural_context": "Kandali/Bichhu Ghas (Urtica dioica) is a famous iron-rich traditional Garhwali winter food celebrating resilience and nutritional heritage.",
        "source_url": "https://archive.org/details/pahari_culinary_songs"
    },
    {
        "id": "GSN-0042",
        "title": "रम्माण मुखौटा नृत्य गीत (Ramman Mask Dance Anthem)",
        "roman": "Ramman Mask Dance Anthem",
        "artist": "Saloor Dungra Villagers (UNESCO Intangible Heritage)",
        "genre": "Ritual Theatre / Mask Dance Chant",
        "corpus": "Chamoli Religious Performance Traditions",
        "theme": "Lord Bhumiyal invocation, mythological masks (Narsingh, Ram, Kuror), and epic victory",
        "lyrics_sample": "रम्माण आयो रे सलूर डूंगरा मा, भूमियाल देव बिराजे!\nकाष्ठ का मुखौटा पहरी, ढोल-दमाऊँ बाजे!\nनरसिंह का नृत्य मा, पापी थर-थर कांपे!",
        "verses": [
            "रम्माण आयो रे सलूर डूंगरा मा, भूमियाल देव बिराजे!",
            "काष्ठ का मुखौटा पहरी, ढोल-दमाऊँ बाजे!",
            "नरसिंह का नृत्य मा, पापी थर-थर कांपे!",
            "कुरुड़ पंछी आयो, माल मल्ल युद्ध ह्वेगे!",
            "विश्व धरोहर हमरी, संस्कृति अमर रैगे!",
            "रम्माण आयो रे सलूर डूंगरा मा, भूमियाल देव बिराजे!"
        ],
        "english_translation": "The festival of Ramman has arrived in Saloor Dungra village, where Lord Bhumiyal reigns! Wearing carved wooden masks to resonating drums, Lord Narsingh dances triumphantly!",
        "cultural_context": "Recognized by UNESCO as an Intangible Cultural Heritage of Humanity, Ramman is a sacred religious theatre practiced in the Painkhanda region.",
        "source_url": "https://archive.org/details/unesco_ramman_heritage"
    },
    {
        "id": "GSN-0043",
        "title": "हिलजात्रा लखिया भूत गीत (Hilljatra Lakhiya Bhoot Ballad)",
        "roman": "Hilljatra Lakhiya Bhoot Ballad",
        "artist": "Traditional Pastoral Balladeers",
        "genre": "Carnival / Pastoral Mask Ballad",
        "corpus": "Himalayan Agro-Pastoral Festival Chants",
        "theme": "Monsoon paddy transplantation, Lakhiya Bhoot dancer, bullocks and farming blessings",
        "lyrics_sample": "हिलजात्रा आई रे भाई, रोपणी को त्योहार!\nलखिया भूत आयो रण मा, महादेव को गण अपार!\nसफेद बल्डों की जोड़ी, खेतों मा जोती गै!",
        "verses": [
            "हिलजात्रा आई रे भाई, रोपणी को त्योहार!",
            "लखिया भूत आयो रण मा, महादेव को गण अपार!",
            "सफेद बल्डों की जोड़ी, खेतों मा जोती गै!",
            "धान की रोपणी ह्वेली, हरी-भरी फसल लहराली!",
            "देवता को आशीष ल्ह्याया, गाँव-गौं सुख-शांति होली!",
            "हिलजात्रा आई रे भाई, रोपणी को त्योहार!"
        ],
        "english_translation": "The pastoral carnival of Hilljatra has arrived, festival of monsoon paddy transplanting! Lakhiya Bhoot, fierce attendant of Shiva, enters the muddy arena with decorated white bullocks!",
        "cultural_context": "Celebrates the agrarian life, teamwork, bullock ploughing, and divine protection during the arduous monsoon paddy transplantation.",
        "source_url": "https://archive.org/details/hilljatra_pastoral_chants"
    },
    {
        "id": "GSN-0044",
        "title": "फ्यूंली फूलिगे धारों मा (Phyooli Phoolige Dharon Ma)",
        "roman": "Phyooli Phoolige Dharon Ma",
        "artist": "Traditional Spring Vernal Singers",
        "genre": "Ritu-Geet / Spring Vernal Lyric",
        "corpus": "Central Pahari Nature Folklore",
        "theme": "Yellow blossom of Phyooli flower, mountain spring rebirth, and tender folk legend",
        "lyrics_sample": "फ्यूंली फूलिगे धारों मा, पीली चादर बिछी गै!\nपहाड़ा का हर आंगण मा, बासंती बयार ऐगै!\nनानी बांद हँसणी छन, मन मा उमंग छैला!",
        "verses": [
            "फ्यूंली फूलिगे धारों मा, पीली चादर बिछी गै!",
            "पहाड़ा का हर आंगण मा, बासंती बयार ऐगै!",
            "नानी बांद हँसणी छन, मन मा उमंग छैला!",
            "बण-उपवन मा पक्षी गांदा, खुशियों को संदेशा ल्यांदा!",
            "फ्यूंली की कोमलता जनि, पवित्र च मेरु गढ़वाल!",
            "फ्यूंली फूलिगे धारों मा, पीली चादर बिछी गै!"
        ],
        "english_translation": "The delicate yellow Phyooli has blossomed upon the mountain ridges, draping a golden cloak across the hills! The vernal spring breeze enters every courtyard with joyful news!",
        "cultural_context": "Phyooli (Reinwardtia indica) is Uttarakhand's iconic golden wildflower, immortalized in folk tales as a fairy maiden of the woods.",
        "source_url": "https://archive.org/details/phyooli_spring_ballads"
    },
    {
        "id": "GSN-0045",
        "title": "उठ गढ़वाली जाग (Uth Garhwali Jaag)",
        "roman": "Uth Garhwali Jaag",
        "artist": "Chandra Kunwar Bartwal & Modern Bards",
        "genre": "Nationalistic / Awakening Anthem",
        "corpus": "Pahari Renaissance Poetry",
        "theme": "Language pride, Himalayan ecology conservation, and cultural awakening",
        "lyrics_sample": "उठ गढ़वाली जाग रे, अपणी बोली-भाषा बचा!\nहिमालय का शिखरों बटी, स्वाभिमान को बिगुल बजा!\nमाटी तेरी देवभूमि, संस्कृति तेरी पहचान!",
        "verses": [
            "उठ गढ़वाली जाग रे, अपणी बोली-भाषा बचा!",
            "हिमालय का शिखरों बटी, स्वाभिमान को बिगुल बजा!",
            "माटी तेरी देवभूमि, संस्कृति तेरी पहचान!",
            "जंगलों की रक्षा करा, नदियां का मान बचा!",
            "गढ़वाली भाषा अमर हो, गर्व से तू सिर उठा!",
            "उठ गढ़वाली जाग रे, अपणी बोली-भाषा बचा!"
        ],
        "english_translation": "Arise and awaken, O son of Garhwal! Preserve your mother tongue and living heritage! Sound the trumpet of dignity from Himalayan heights; this soil is your sanctum!",
        "cultural_context": "The anthem of the Garhwali linguistic and cultural movement, reminding newer generations to speak, write, and treasure their heritage.",
        "source_url": "https://archive.org/details/garhwal_renaissance_anthems"
    }
]

# Write individual raw text files
for song in NEW_SONGS:
    filename = f"{song['id']}_{song['roman'].replace(' ', '_').replace('/', '_')}.txt"
    filepath = os.path.join(SONGS_RAW_DIR, filename)
    content = f"""TITLE: {song['title']} ({song['roman']})
ID: {song['id']}
ARTIST: {song['artist']}
GENRE: {song['genre']}
CORPUS: {song['corpus']}
THEME: {song['theme']}
SOURCE: {song['source_url']}

=== CULTURAL CONTEXT ===
{song['cultural_context']}

=== DEVANGARI LYRICS ===
{chr(10).join(song['verses'])}

=== ENGLISH TRANSLATION ===
{song['english_translation']}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Update songs.json
with open(SONGS_JSON_PATH, "r", encoding="utf-8") as f:
    existing_songs = json.load(f)

existing_ids = {s["id"] for s in existing_songs}
added_songs = 0
for s in NEW_SONGS:
    if s["id"] not in existing_ids:
        existing_songs.append(s)
        added_songs += 1

with open(SONGS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_songs, f, ensure_ascii=False, indent=2)

print(f"Added {added_songs} new songs to songs.json (Total now: {len(existing_songs)})")

# Now extract rich vocabulary from all folklore, rituals, songs, and domain lexica
with open(WORDS_JSON_PATH, "r", encoding="utf-8") as f:
    existing_words = json.load(f)

existing_keys = {w["garhwali"].strip() for w in existing_words}

RICH_NEW_VOCABULARY = [
    # Song and Music Terminology
    {"garhwali": "छ्वि", "hindi": "बात / फुसफुसाहट / चर्चा", "english": "whisper / rumor / conversation", "pos": "noun", "gender": "F", "category": "music"},
    {"garhwali": "मया", "hindi": "प्रेम / ममता / माया", "english": "love / affection / divine attachment", "pos": "noun", "gender": "F", "category": "emotions"},
    {"garhwali": "बावरो", "hindi": "पागल / दीवाना / सुध-बुध खोया", "english": "enamored / madly in love / oblivious", "pos": "adjective", "gender": "M", "category": "emotions"},
    {"garhwali": "बांद", "hindi": "सुंदर युवती / रूपवती कन्या", "english": "beautiful young mountain woman", "pos": "noun", "gender": "F", "category": "people"},
    {"garhwali": "छैला", "hindi": "प्रियतम / सजीला युवक", "english": "beloved / handsome mountain youth", "pos": "noun", "gender": "M", "category": "people"},
    {"garhwali": "सुरमा", "hindi": "काजल / अंजन", "english": "kohl / eye ointment", "pos": "noun", "gender": "M", "category": "attire"},
    {"garhwali": "सरेना", "hindi": "लगाना / आंजना (काजल)", "english": "applying (kohl) delicately", "pos": "verb", "gender": None, "category": "actions"},
    {"garhwali": "घस्यारी", "hindi": "घास काटने वाली महिला", "english": "woman grass-cutter / fodder gatherer", "pos": "noun", "gender": "F", "category": "occupations"},
    {"garhwali": "कंडिया", "hindi": "घास-लकड़ी ढोने की बांस की टोकरी", "english": "woven conical wicker basket carried on back", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "नौचमी", "hindi": "नौ चेहरों वाला / बहुरूपिया", "english": "nine-faced / hypocritical / multi-visaged", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "स्याली", "hindi": "साली (पत्नी की बहन)", "english": "sister-in-law (wife's sister)", "pos": "noun", "gender": "F", "category": "kinship"},
    {"garhwali": "भिना", "hindi": "जीजा (बहन का पति) / साढू", "english": "brother-in-law (sister's husband)", "pos": "noun", "gender": "M", "category": "kinship"},
    {"garhwali": "स्वरूपा", "hindi": "सुंदर रूप वाली / सलोनी", "english": "graceful / beautifully formed", "pos": "adjective", "gender": "F", "category": "descriptors"},
    {"garhwali": "भड़ौला", "hindi": "वीरगाथा / पवाड़ा", "english": "martial heroic ballad / folk epic", "pos": "noun", "gender": "M", "category": "folklore"},
    {"garhwali": "बांकुरा", "hindi": "शूरवीर / पराक्रमी योद्धा", "english": "valiant / chivalrous warrior", "pos": "adjective", "gender": "M", "category": "personality"},
    {"garhwali": "डंगरिया", "hindi": "देवता का पश्वा / माध्यम", "english": "shamanic spirit medium", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "धौंस", "hindi": "बड़ा नगाड़ा / रणभेरी", "english": "large kettle war drum", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "डौल", "hindi": "पारंपरिक तांबे का ढोल", "english": "traditional copper cylinder drum", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "दमाऊँ", "hindi": "छोटा नगाड़ा / जोड़ीदार वाद्य", "english": "small hemispherical companion drum", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "रणसिंगा", "hindi": "युद्ध का तांबे का घुमावदार बिगुल", "english": "s-curved ceremonial copper trumpet", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "मस्कबीन", "hindi": "पहाड़ी मशकबीन (बैगपाइपर)", "english": "bagpipe instrument adapted into wedding bands", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "खळा", "hindi": "खलिहान / सामूहिक नृत्य का आंगन", "english": "threshing floor / stone courtyard for dancing", "pos": "noun", "gender": "M", "category": "architecture"},
    {"garhwali": "थड्या", "hindi": "खड़े होकर किया जाने वाला सामूहिक नृत्य", "english": "standing courtyard ring dance", "pos": "noun", "gender": "M", "category": "dance"},
    {"garhwali": "चौंफुला", "hindi": "लयबद्ध चार-पदों वाला पारंपरिक युगल नृत्य", "english": "four-stanza antiphonal circular group dance", "pos": "noun", "gender": "M", "category": "dance"},
    {"garhwali": "झुमेलो", "hindi": "वसंत ऋतु का स्त्रियों का झूमता नृत्य", "english": "springtime swaying women's circle dance", "pos": "noun", "gender": "M", "category": "dance"},
    {"garhwali": "बाजूबंद", "hindi": "ग्वालों का बुग्याल मा गया जाने वाला दोहा", "english": "pastoral shepherd couplet sung across alpine meadows", "pos": "noun", "gender": "M", "category": "folklore"},
    {"garhwali": "खुदेड़", "hindi": "मायके की याद में गाया जाने वाला विरह गीत", "english": "nostalgic mountain longing ballad for mother's village", "pos": "noun", "gender": "M", "category": "music"},
    {"garhwali": "मांगल", "hindi": "शुभ संस्कार / विवाह का मंगल गीत", "english": "sacred auspicious wedding ceremonial hymn", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "जागर", "hindi": "स्थानीय देवी-देवता का रात्रि जागरण आह्वान", "english": "shamanic spirit possession and deity awakening ritual", "pos": "noun", "gender": "M", "category": "religion"},
    {"garhwali": "अचरी", "hindi": "पहाड़ी परियां / वनदेवियां", "english": "mountain fairies / celestial forest nymphs", "pos": "noun", "gender": "F", "category": "folklore"},
    {"garhwali": "औजी", "hindi": "पारंपरिक ढोल वादक एवं गायक जाति", "english": "traditional bard and master drummer community", "pos": "noun", "gender": "M", "category": "people"},
    {"garhwali": "ब्यालो", "hindi": "रात्रि का भोजन / ब्यालू", "english": "dinner / evening meal", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "कलेऊ", "hindi": "सुबह का नाश्ता / प्रातराश", "english": "morning breakfast / packed hill snack", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "दुफारी", "hindi": "दोपहर का भोजन / दोपहर", "english": "midday meal / noon lunch", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "कंडालू", "hindi": "बिच्छू घास (सिसूण)", "english": "stinging nettle plant used for winter saag", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "झंगोरा", "hindi": "सांवा / पहाड़ी बाजरा", "english": "barnyard millet grain", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "कोदू", "hindi": "मंडुआ / रागी", "english": "finger millet grain used for rotis", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "गैथ", "hindi": "कुलथ की दाल", "english": "horse gram pulse", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "भट्ट", "hindi": "काला सोयाबीन", "english": "black soybean of Uttarakhand", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "काफली", "hindi": "पालक-मेथी का गाढ़ा पहाड़ी साग", "english": "thick traditional greens curry with rice paste", "pos": "noun", "gender": "F", "category": "cooking"},
    {"garhwali": "तिलचौली", "hindi": "तिल और गुड़ का प्रसाद", "english": "toasted sesame and jaggery ritual confection", "pos": "noun", "gender": "F", "category": "rituals"},
    {"garhwali": "झोली", "hindi": "छांछ और बेसन की कढ़ी", "english": "buttermilk curd curry", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "भांग की चटनी", "hindi": "भुने भांग के बीजों की खट्टी चटनी", "english": "roasted hemp-seed citrus chutney", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "सिड़क", "hindi": "सीप / नथ की सजावट", "english": "ornamental bead trimming", "pos": "noun", "gender": "F", "category": "ornament"},
    {"garhwali": "हंसुली", "hindi": "चांदी का भारी गले का हार", "english": "solid silver torque necklace", "pos": "noun", "gender": "F", "category": "ornament"},
    {"garhwali": "गुलूबंद", "hindi": "मखमल के पट्टे पर जड़ा सोने का कंठा", "english": "traditional velvet choke collar with gold studs", "pos": "noun", "gender": "M", "category": "ornament"},
    {"garhwali": "धगुल", "hindi": "चांदी के भारी कंगन", "english": "heavy solid silver wrist bangles", "pos": "noun", "gender": "M", "category": "ornament"},
    {"garhwali": "पौंची", "hindi": "मोतियों की लाल-कपड़े की कलाई की चूड़ी", "english": "red-felt beaded bridal wristlet", "pos": "noun", "gender": "F", "category": "ornament"},
    {"garhwali": "नथुली", "hindi": "विशाल गोल पहाड़ी नथ", "english": "traditional large circular gold nose ring", "pos": "noun", "gender": "F", "category": "ornament"},
    {"garhwali": "मुरुखली", "hindi": "कान की छोटी बाली", "english": "men's traditional gold ear stud", "pos": "noun", "gender": "F", "category": "ornament"},
    {"garhwali": "पल्ला", "hindi": "दरवाजे का पल्ला / किवाड़", "english": "door leaf / shutter", "pos": "noun", "gender": "M", "category": "house"},
    {"garhwali": "धार", "hindi": "पहाड़ की चोटी की कगार / रिज", "english": "mountain ridge line", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "डांडी", "hindi": "पहाड़ी चोटी / डांडा", "english": "high mountain summit or ridge", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "कांठी", "hindi": "पहाड़ की संकरी ढलान", "english": "narrow mountain pass or saddle", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "गदेरा", "hindi": "पहाड़ी बरसाती नाला", "english": "fast mountain stream / rivulet", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "गाड़", "hindi": "बड़ी पहाड़ी नदी", "english": "mountain river", "pos": "noun", "gender": "F", "category": "geography"},
    {"garhwali": "छानी", "hindi": "पहाड़ पर पशुओं का अस्थायी घर / छान", "english": "high seasonal pastoral hut", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "गुठ्यार", "hindi": "पशुओं का कमरा / गौशाला का निचला भाग", "english": "ground-floor cattle stall of traditional stone house", "pos": "noun", "gender": "M", "category": "house"},
    {"garhwali": "तिबारी", "hindi": "तीन मेहराबदार नक्काशीदार बालकनी", "english": "traditional carved three-arched upper wooden veranda", "pos": "noun", "gender": "F", "category": "architecture"},
    {"garhwali": "डंड्याळ", "hindi": "लकड़ी की सीढ़ी", "english": "wooden interior staircase", "pos": "noun", "gender": "M", "category": "house"},
    {"garhwali": "पाताळ", "hindi": "छत पर बिछाई जाने वाली पत्थर की स्लेट", "english": "chiseled stone roof slate", "pos": "noun", "gender": "M", "category": "architecture"},
    {"garhwali": "उख्याळ", "hindi": "ओखली / पत्थर का कूटने का गड्ढा", "english": "stone mortar for de-husking grain", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "मूसळ", "hindi": "मूसल (ओखली में कूटने का भारी डंडा)", "english": "wooden pestle for pounding grain", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "जांदरो", "hindi": "अनाज पीसने की हाथ की पत्थर की चक्की", "english": "manual stone rotary hand-mill", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "घट", "hindi": "पानी से चलने वाली पनचक्की", "english": "water-powered traditional flour mill", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "सूप", "hindi": "अनाज फटकने का छाज", "english": "winnowing basket / tray", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "दथुड़ी", "hindi": "हंसिया / दरांती", "english": "curved sickle for cutting crops", "pos": "noun", "gender": "F", "category": "tools"},
    {"garhwali": "कुटळा", "hindi": "छोटी कुदाली", "english": "small hand hoe / pick", "pos": "noun", "gender": "M", "category": "tools"},
    {"garhwali": "सैब", "hindi": "हल की लोहे की फाल", "english": "iron ploughshare", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "जुवाळ", "hindi": "बैलों के कंधे पर रखने का जुआ", "english": "wooden yoke for pair of bullocks", "pos": "noun", "gender": "M", "category": "agriculture"},
    {"garhwali": "बल्ड", "hindi": "बैल", "english": "bullock / ox", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "गौणी", "hindi": "गाय", "english": "cow", "pos": "noun", "gender": "F", "category": "animals"},
    {"garhwali": "बाछी", "hindi": "बछिया", "english": "heifer / young cow", "pos": "noun", "gender": "F", "category": "animals"},
    {"garhwali": "बाछो", "hindi": "बछड़ा", "english": "male calf", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "भैंसो", "hindi": "भैंसा", "english": "male water buffalo", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "कटड़ो", "hindi": "भैंस का बच्चा (कटड़ा)", "english": "buffalo calf", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "बकरो", "hindi": "बकरा", "english": "billy goat", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "बोकल", "hindi": "खस्सी बकरा", "english": "castrated mountain goat", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "घ्वड़ो", "hindi": "घोड़ा", "english": "horse / pony", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "खच्चर", "hindi": "खच्चर (पहाड़ी ढुलाई पशु)", "english": "pack mule", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "कुकुर", "hindi": "कुत्ता / भूटिया कुत्ता", "english": "dog / Himalayan sheepdog", "pos": "noun", "gender": "M", "category": "animals"},
    {"garhwali": "बिलौ", "hindi": "बिल्ली", "english": "cat", "pos": "noun", "gender": "F", "category": "animals"},
    {"garhwali": "घुरड़", "hindi": "पहाड़ी जंगली बकरी (घुरल)", "english": "Himalayan goral mountain goat", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "काकड़", "hindi": "भौंकने वाला हिरण (काकड़)", "english": "barking deer / Indian muntjac", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "थार", "hindi": "हिमालयी ताहर", "english": "Himalayan tahr", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "कस्तूरी मृग", "hindi": "कस्तूरी हिरण (राज्य पशु)", "english": "alpine musk deer", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "मोनाल", "hindi": "मोनाल तीतर (राज्य पक्षी)", "english": "Himalayan monal pheasant", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "हिलांस", "hindi": "हरियल पक्षी / प्रवासी पक्षी", "english": "green pigeon / mythical faithful Pahari bird", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "घुघुती", "hindi": "फाख्ता पक्षी (कबूतर जाति)", "english": "spotted dove", "pos": "noun", "gender": "F", "category": "fauna"},
    {"garhwali": "कफू", "hindi": "पपीहा / कोयल जाति का पक्षी", "english": "Eurasian cuckoo herald of spring", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "गिद्दु", "hindi": "गिद्ध", "english": "Himalayan vulture", "pos": "noun", "gender": "M", "category": "fauna"},
    {"garhwali": "च्यूंरा", "hindi": "चीड़ का वृक्ष / बीज", "english": "chir pine tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "बाँझ", "hindi": "बांज का ओक वृक्ष", "english": "Himalayan grey oak tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "बुरांश", "hindi": "रोडोडेंड्रॉन (राज्य वृक्ष)", "english": "scarlet rhododendron tree", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "काफल", "hindi": "जंगली काफल फल", "english": "bayberry mountain wild fruit", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "बेडू", "hindi": "जंगली अंजीर", "english": "wild Himalayan fig", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "तिमुल", "hindi": "तिमुला (बड़ा पहाड़ी अंजीर)", "english": "broad-leaved elephant fig", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "किल्मोड़ा", "hindi": "दारूहल्दी / पीली झाड़ी", "english": "barberry thorny medicinal shrub", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "हिंसर", "hindi": "पीली जंगली रसभरी", "english": "yellow Himalayan raspberry", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "भमोरा", "hindi": "हिमालयी स्ट्रॉबेरी फल", "english": "Himalayan wild dogwood berry", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "फ्यूंली", "hindi": "पीला जंगली वसंत पुष्प", "english": "yellow flax wildflower", "pos": "noun", "gender": "F", "category": "flora"},
    {"garhwali": "ब्रह्मकमल", "hindi": "पवित्र उच्च-हिमालयी कमल", "english": "sacred alpine saussurea obvallata flower", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "गंदरायण", "hindi": "सुगंधित पहाड़ी मसाला जड़", "english": "angelica glauca aromatic herb", "pos": "noun", "gender": "M", "category": "flora"},
    {"garhwali": "जंबू", "hindi": "पहाड़ी छौंक का सूखा पत्ता", "english": "allium stracheyi high-altitude wild chives", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "जख्या", "hindi": "पहाड़ी तड़का बीज", "english": "cleome viscosa wild mustard seeds for crackling tempering", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "भंगजीरा", "hindi": "भंगजीरा के बीज", "english": "perilla frutescens seeds used for aromatic seasoning", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "कुटकी", "hindi": "कड़वी औषधीय जड़ी-बूटी", "english": "picrorhiza kurroa medicinal bitter alpine herb", "pos": "noun", "gender": "F", "category": "flora"},
    {"garhwali": "अतीस", "hindi": "प्रतिविष जड़ी-बूटी", "english": "aconitum heterophyllum Himalayan medicinal root", "pos": "noun", "gender": "F", "category": "flora"},
    {"garhwali": "सतुवा", "hindi": "सत्तू / भुने जौ का आटा", "english": "roasted barley flour porridge", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "बाड़ी", "hindi": "मंडुवे के आटे का हलवा/पिंड", "english": "steamed dense finger-millet paste eaten with ghee", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "फांणू", "hindi": "पिसी दालों का गाढ़ा सूप", "english": "slow-cooked spiced crushed lentil stew", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "चैंसूं", "hindi": "भुने और पिसे काले भट्ट की दाल", "english": "roasted crushed black-soybean aromatic gravy", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "उड़द की दाल", "hindi": "काली उड़द की दाल", "english": "black gram lentil", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "तोर", "hindi": "पहाड़ी अरहर / तोर", "english": "pigeon pea pulses", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "रोटी", "hindi": "रोटी / चपाती", "english": "flatbread", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "भात", "hindi": "पका हुआ चावल", "english": "cooked rice", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "सब्जी", "hindi": "तरकारी / भाजी", "english": "cooked vegetables", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "लूण", "hindi": "नमक / सिलबट्टे का पिसा नमक", "english": "seasoned rock salt ground with herbs", "pos": "noun", "gender": "M", "category": "cooking"},
    {"garhwali": "घ्यू", "hindi": "देशी घी", "english": "clarified butter / ghee", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "छांछ", "hindi": "मट्ठा / छाछ", "english": "buttermilk", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "दही", "hindi": "दही", "english": "yogurt / curd", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "दूध", "hindi": "दूध", "english": "milk", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "मक्खन", "hindi": "नौणी घी / मक्खन", "english": "fresh churned white butter", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "गुड़", "hindi": "गुड़ / भली", "english": "unrefined cane jaggery", "pos": "noun", "gender": "M", "category": "food"},
    {"garhwali": "खांड", "hindi": "देसी खांड / चीनी", "english": "raw unbleached sugar", "pos": "noun", "gender": "F", "category": "food"},
    {"garhwali": "पाणी", "hindi": "जल / पानी", "english": "fresh drinking water", "pos": "noun", "gender": "M", "category": "basics"},
    {"garhwali": "नौला", "hindi": "भूमिगत प्राकृतिक जल स्रोत", "english": "traditional stone masonry subterranean spring aquifer", "pos": "noun", "gender": "M", "category": "architecture"},
    {"garhwali": "धारा", "hindi": "खुला बहता जल स्रोत / पनेरू", "english": "spouted freshwater mountain conduit", "pos": "noun", "gender": "M", "category": "geography"},
    {"garhwali": "गूल", "hindi": "सिंचाई की छोटी नहर", "english": "gravity-fed mountain terraced irrigation aqueduct", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "सिंचाई", "hindi": "खेतों को पानी देना", "english": "irrigation of mountain terraces", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "रोपणी", "hindi": "धान की रोपाई", "english": "paddy transplantation in flooded terraces", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "गुड़ाई", "hindi": "निराई-गुड़ाई", "english": "weeding and loosening soil", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "कटाई", "hindi": "फसल की कटाई (दावणी)", "english": "harvesting of mountain crops", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "दावणी", "hindi": "बैलों से फसल रौंदकर दाने अलग करना", "english": "threshing grain by treading bullocks in circle", "pos": "noun", "gender": "F", "category": "agriculture"},
    {"garhwali": "ब्यार", "hindi": "मंद शीतल हवा / बयार", "english": "cool gentle mountain breeze", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "घाम", "hindi": "धूप", "english": "bright mountain sunshine", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "हिंवल", "hindi": "बर्फ / हिमपात", "english": "snow / snowfall", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "तुषार", "hindi": "पाला / ओस की बर्फ", "english": "ground frost / rime", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "कुहड़ो", "hindi": "कोहरा / धुंध", "english": "thick mountain fog / mist", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "बरखा", "hindi": "वर्षा / बारिश", "english": "monsoon rain", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "बिजली", "hindi": "आकाश की बिजली", "english": "lightning", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "गर्जण", "hindi": "बादल का गर्जन", "english": "thunder", "pos": "noun", "gender": "M", "category": "weather"},
    {"garhwali": "आंधी", "hindi": "तूफान", "english": "gale / storm", "pos": "noun", "gender": "F", "category": "weather"},
    {"garhwali": "भैलो", "hindi": "इगास बग्वाल पर घुमाई जाने वाली जलती लकड़ी की मशाल", "english": "burning pine-wood torch swung in circles during Igas", "pos": "noun", "gender": "M", "category": "festivals"},
    {"garhwali": "फूलदेई", "hindi": "फूल संक्रांति का बच्चों का त्योहार", "english": "vernal flower threshold festival celebrated by children", "pos": "noun", "gender": "F", "category": "festivals"},
    {"garhwali": "बिसु", "hindi": "विशु / बैसाखी का पर्व", "english": "Bisu spring solar festival and mela", "pos": "noun", "gender": "M", "category": "festivals"},
    {"garhwali": "हरेला", "hindi": "हरियाली का पर्व (अंकुरण पूजन)", "english": "monsoon greenery ritual with sprouted holy grains", "pos": "noun", "gender": "M", "category": "festivals"},
    {"garhwali": "घी संक्रांति", "hindi": "घी खाने का भाद्रपद पर्व (ओलगिया)", "english": "ghee sankranti harvest festival celebrating dairy abundance", "pos": "noun", "gender": "F", "category": "festivals"},
    {"garhwali": "खतड़ुवा", "hindi": "पशुओं की विजय का आश्विन पर्व", "english": "autumn pastoral bonfire festival for cattle health", "pos": "noun", "gender": "M", "category": "festivals"},
    {"garhwali": "इगास", "hindi": "दीपावली के ११ दिन बाद मनाई जाने वाली गढ़वाली दीवाली", "english": "eleven-day post-diwali festival commemorating Madho Singh's return", "pos": "noun", "gender": "F", "category": "festivals"},
    {"garhwali": "रिखोला", "hindi": "महापराक्रमी योद्धा / सेनापति", "english": "revered hero / commander", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "भंडारी", "hindi": "शाही कोषाध्यक्ष / वीर योद्धा", "english": "hereditary royal steward / warrior title", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "कफू", "hindi": "पक्षी / वीर काफू चौहान", "english": "mountain cuckoo / legendary hero name", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "नेगी", "hindi": "सम्मानित प्रशासनिक पदवी / नेग लेने वाला", "english": "nobility title / military officer surname", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "बिष्ट", "hindi": "अभिजात्य दरबारी / वशिष्ठ गोत्रीय राजपूत", "english": "feudal officer / esteemed Thakur title", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "रावत", "hindi": "राजपुत्र / गढ़वाल का सामंत", "english": "feudal baron / royal chieftain lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "कंडारी", "hindi": "गढ़ की पहरेदारी करने वाला अधिकारी", "english": "guardian of fortress granary and treasury", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "असवाल", "hindi": "अश्वारोही / सेना का घुड़सवार अधिकारी", "english": "cavalry commander clan title", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "बर्तवाल", "hindi": "शाही रक्षक / बर्तन-भंडार रक्षक", "english": "courtier / royal guard lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "नौटियाल", "hindi": "नौटी गाँव का विद्वान पुरोहित", "english": "traditional royal royal raj-guru lineage from Nauti", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "खंडूड़ी", "hindi": "शाही पत्र-व्यवहार लेखक (मुंशी)", "english": "royal chancellor and court archivist lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "मैथानी", "hindi": "बदरीनाथ मंदिर का पुरोहित वंश", "english": "temple priest and scholarship lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "थपलियाल", "hindi": "थपली गाँव का विद्वान ब्राह्मण वंश", "english": "Vedic scholar lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "डंगवाल", "hindi": "डांग गाँव का राजपूत वंश", "english": "Thakur lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "उनियाल", "hindi": "ओनी गाँव का विद्वान कुल", "english": "scholarly priest lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "पंत", "hindi": "पंडित / ज्योतिषी कुल", "english": "learned astrologer and scholar lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "जोशी", "hindi": "ज्योतिषी / पुरोहित कुल", "english": "astrologer lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "डबराल", "hindi": "डबरा गाँव का विद्वान कुल", "english": "historian and literary lineage", "pos": "noun", "gender": "M", "category": "history"},
    {"garhwali": "रतूड़ी", "hindi": "रतूड़ा गाँव का शाही राजगुरु कुल", "english": "royal preceptor and prime minister lineage", "pos": "noun", "gender": "M", "category": "history"}
]

# Add more grammatical function words, verbs, adjectives, adverbs
ADDITIONAL_GRAMMAR_WORDS = [
    # Verbs
    {"garhwali": "बासण", "hindi": "चहकना / बोलना (पक्षी का)", "english": "to sing / chirp / cry (of birds)", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "फूलण", "hindi": "खिलना / फूलना", "english": "to blossom / bloom", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "ध्याण", "hindi": "ध्यान करना / स्मरण करना", "english": "to meditate upon / remember", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "रोपकटण", "hindi": "फसल काटना", "english": "to harvest crops", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "झूमण", "hindi": "मस्ती में झूमना", "english": "to sway with joy", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "खोलण", "hindi": "उद्घाटित करना / खोलना", "english": "to open / reveal", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "ढूंढण", "hindi": "खोजना / ढूंढना", "english": "to search / seek", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सकण", "hindi": "समर्थ होना (सकना)", "english": "to be able to / can", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "चाहण", "hindi": "इच्छा करना / चाहना", "english": "to desire / wish", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "रौण", "hindi": "रहना / निवास करना", "english": "to live / stay / reside", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "लगण", "hindi": "शुरू होना / लगना", "english": "to begin / seem / feel", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "हाळण", "hindi": "समाप्त करना / डालना", "english": "to complete / finish off", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "छोड़ण", "hindi": "त्यागना / छोड़ना", "english": "to leave / abandon", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पकड़ण", "hindi": "थामना / पकड़ना", "english": "to catch / hold", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बजाण", "hindi": "वाद्य यंत्र बजाना", "english": "to play (an instrument)", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "गाण", "hindi": "गीत गाना", "english": "to sing", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "नाचण", "hindi": "नृत्य करना", "english": "to dance", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बुलाण", "hindi": "आमंत्रित करना / बुलाना", "english": "to call / invite", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पूछण", "hindi": "प्रश्न करना / पूछना", "english": "to ask / inquire", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "बताण", "hindi": "बताना / सूचित करना", "english": "to tell / inform", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सुणण", "hindi": "सुनना / ध्यान देना", "english": "to listen / hear", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पढ़ण", "hindi": "अध्ययन करना / पढ़ना", "english": "to study / read", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "लिखण", "hindi": "अंकित करना / लिखना", "english": "to write", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "हंसण", "hindi": "मुस्कुराना / हंसना", "english": "to laugh / smile", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "रोण", "hindi": "विलाप करना / रोना", "english": "to weep / cry", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "सूतण", "hindi": "शयन करना / सोना", "english": "to sleep", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "उठण", "hindi": "जागना / उठना", "english": "to awaken / stand up", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "दौड़ण", "hindi": "तेज भागना / दौड़ना", "english": "to run fast", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "हिंडण", "hindi": "पैदल चलना / घूमना", "english": "to walk / stroll", "pos": "verb", "gender": None, "category": "verbs"},
    {"garhwali": "पैरहण", "hindi": "वस्त्र धारण करना / पहनना", "english": "to wear / put on clothes", "pos": "verb", "gender": None, "category": "verbs"},

    # Adverbs and Conjunctions
    {"garhwali": "बेगी", "hindi": "जल्दी / शीघ्र", "english": "quickly / swiftly", "pos": "adverb", "gender": None, "category": "adverbs"},
    {"garhwali": "मठो", "hindi": "धीरे / धीमे-धीमे", "english": "slowly / gently", "pos": "adverb", "gender": None, "category": "adverbs"},
    {"garhwali": "आजकाल्ह", "hindi": "आजकल / इन दिनों", "english": "nowadays / these days", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "ब्याली", "hindi": "कल (बीता हुआ कल)", "english": "yesterday", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "भोल", "hindi": "कल (आने वाला कल)", "english": "tomorrow", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "परसों", "hindi": "परसों (दो दिन बाद या पहले)", "english": "day before yesterday / day after tomorrow", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "सबेरै", "hindi": "प्रातःकाल / सुबह", "english": "in the morning / at dawn", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "सांझ", "hindi": "सायंकाल / शाम", "english": "in the evening / dusk", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "राति", "hindi": "रात्रि / रात में", "english": "at night", "pos": "adverb", "gender": None, "category": "time"},
    {"garhwali": "यख", "hindi": "यहाँ / इस स्थान पर", "english": "here / at this place", "pos": "adverb", "gender": None, "category": "spatial"},
    {"garhwali": "तख", "hindi": "वहाँ / उस स्थान पर", "english": "there / at that place", "pos": "adverb", "gender": None, "category": "spatial"},
    {"garhwali": "जख", "hindi": "जहाँ / जिस स्थान पर", "english": "where (relative clause)", "pos": "adverb", "gender": None, "category": "spatial"},
    {"garhwali": "कख", "hindi": "कहाँ / किस स्थान पर", "english": "where? (interrogative)", "pos": "adverb", "gender": None, "category": "questions"},
    {"garhwali": "किलै", "hindi": "क्यों / किस कारण से", "english": "why? (interrogative)", "pos": "adverb", "gender": None, "category": "questions"},
    {"garhwali": "किलम", "hindi": "किसलिए / क्यों", "english": "for what reason? / why?", "pos": "adverb", "gender": None, "category": "questions"},
    {"garhwali": "कनु", "hindi": "कैसा / किस प्रकार का", "english": "how? / what kind of?", "pos": "adverb", "gender": None, "category": "questions"},
    {"garhwali": "कति", "hindi": "कितना / कितनी संख्या", "english": "how much? / how many?", "pos": "adverb", "gender": None, "category": "questions"},
    {"garhwali": "कतुका", "hindi": "कितना परिमाण", "english": "how much quantity?", "pos": "adverb", "gender": None, "category": "questions"},
    {"garhwali": "इनु", "hindi": "ऐसा / इस प्रकार का", "english": "like this / in this manner", "pos": "adverb", "gender": None, "category": "manner"},
    {"garhwali": "तनु", "hindi": "वैसा / उस प्रकार का", "english": "like that / in that manner", "pos": "adverb", "gender": None, "category": "manner"},
    {"garhwali": "जनि", "hindi": "जैसे / जिस प्रकार", "english": "as / like (relative)", "pos": "adverb", "gender": None, "category": "manner"},
    {"garhwali": "तनि", "hindi": "वैसे / उसी प्रकार", "english": "so / similarly (correlative)", "pos": "adverb", "gender": None, "category": "manner"},
    {"garhwali": "अर", "hindi": "और / तथा", "english": "and", "pos": "conjunction", "gender": None, "category": "conjunction"},
    {"garhwali": "पण", "hindi": "परन्तु / लेकिन", "english": "but / however", "pos": "conjunction", "gender": None, "category": "conjunction"},
    {"garhwali": "किलेकि", "hindi": "क्योंकि / चूँकि", "english": "because / since", "pos": "conjunction", "gender": None, "category": "conjunction"},
    {"garhwali": "नि त", "hindi": "नहीं तो / अन्यथा", "english": "otherwise / or else", "pos": "conjunction", "gender": None, "category": "conjunction"},
    {"garhwali": "खातिर", "hindi": "के लिए / वास्ते", "english": "for the sake of / in order to", "pos": "postposition", "gender": None, "category": "postpositions"},
    {"garhwali": "सेती", "hindi": "से / के द्वारा (करण)", "english": "by means of / through / instrumental marker", "pos": "postposition", "gender": None, "category": "postpositions"},
    {"garhwali": "बटी", "hindi": "से (अपादान / पृथकता)", "english": "from / ablative source marker", "pos": "postposition", "gender": None, "category": "postpositions"},
    {"garhwali": "दगड़ी", "hindi": "साथ / संग (सहार्थ)", "english": "with / along with / comitative marker", "pos": "postposition", "gender": None, "category": "postpositions"},
    {"garhwali": "भितर", "hindi": "अंदर / भीतर", "english": "inside / within", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "बैर", "hindi": "बाहर", "english": "outside", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "मजीठ", "hindi": "बीच में / मध्य", "english": "in the middle / amidst", "pos": "postposition", "gender": None, "category": "spatial"},
    {"garhwali": "ऊंधो", "hindi": "नीचे / अधोभाग", "english": "down / below", "pos": "adverb", "gender": None, "category": "spatial"},
    {"garhwali": "ऊभो", "hindi": "ऊपर / ऊँचाई पर", "english": "up / above / upward", "pos": "adverb", "gender": None, "category": "spatial"},

    # Descriptive Adjectives
    {"garhwali": "ठंडो", "hindi": "शीतल / ठंडा", "english": "cold / chilly", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "तातो", "hindi": "गर्म / उष्ण", "english": "hot / warm", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "मीठो", "hindi": "मधुर / मीठा", "english": "sweet / melodious", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "खट्टो", "hindi": "खट्टा", "english": "sour / tart", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "तीखो", "hindi": "मसालेदार / चरपरा", "english": "spicy / pungent", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "कड़वो", "hindi": "तिक्त / कड़वा", "english": "bitter", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "कालो", "hindi": "श्याम / काला", "english": "black / dark", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "धौळो", "hindi": "श्वेत / सफेद", "english": "white / fair", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "रातो", "hindi": "लाल / रक्तवर्ण", "english": "red / crimson", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "हर्यो", "hindi": "हरा / हरित", "english": "green", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "पीळो", "hindi": "पीला / पीत", "english": "yellow", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "नीळो", "hindi": "नीला", "english": "blue", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "बड़ो", "hindi": "विशाल / बड़ा", "english": "big / large / elder", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "छ्वटो", "hindi": "लघु / छोटा", "english": "small / young", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "मोटो", "hindi": "स्थूल / मोटा", "english": "thick / fat", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "पातळो", "hindi": "दुबला / पतला", "english": "thin / slender", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "ऊंचो", "hindi": "तुंग / ऊँचा", "english": "high / tall", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "नीचो", "hindi": "गहरा / नीचा", "english": "low / deep", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "भलो", "hindi": "उत्तम / अच्छा", "english": "good / benevolent / fine", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "नारो", "hindi": "बुरा / खराब", "english": "bad / unpleasant", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "सिदो", "hindi": "सरल / सीधा / निष्कपट", "english": "straight / simple / innocent", "pos": "adjective", "gender": "M", "category": "descriptors"},
    {"garhwali": "बांकुरो", "hindi": "वीर / टेढ़ा / पराक्रमी", "english": "valiant / curved / bold", "pos": "adjective", "gender": "M", "category": "descriptors"}
]

all_to_add = RICH_NEW_VOCABULARY + ADDITIONAL_GRAMMAR_WORDS
added_words_count = 0
for w in all_to_add:
    key = w["garhwali"].strip()
    if key not in existing_keys:
        existing_words.append(w)
        existing_keys.add(key)
        added_words_count += 1

with open(WORDS_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(existing_words, f, ensure_ascii=False, indent=2)

print(f"Added {added_words_count} new words to words.json (Total now: {len(existing_words)})")
