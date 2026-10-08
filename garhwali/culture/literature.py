# -*- coding: utf-8 -*-
"""
Literature, Folklore, and Oral Heritage of the Garhwali Language.

Features:
- Folk Epics (पवाड़े / जागर): Madho Singh Bhandari, Jeetu Bagdwal, Kaphua, Saru Kunwar, Ranubhaut, Dhari Devi
- Classical & Traditional Folk Songs: Chaita Ki Chaitwali, Bedu Pako Baramasa, Ghughuti Na Baas, Mangal Geet
- Canonical Poets & Scholars: Bhajan Singh 'Singh', Chandra Kunwar Bartwal, Narendra Singh Negi, Tara Dutt Gairola, Dr. Govind Chatak, Haridatta Bhatt
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class FolkEpic:
    id: str
    title_garhwali: str
    title_english: str
    genre: str  # "Pawaada", "Jagar", "Ballad"
    hero: str
    region: str
    synopsis: str
    cultural_significance: str
    sample_verses: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class FolkPoem:
    id: str
    title_garhwali: str
    title_english: str
    form: str  # "Chaitwali", "Thadya", "Chaunphula", "Jhumeilo", "Mangal"
    theme: str
    verses_garhwali: List[str]
    verses_roman: List[str]
    english_translation: str
    cultural_context: str


@dataclass
class GarhwaliAuthor:
    name_garhwali: str
    name_english: str
    era: str
    significance: str
    famous_works: List[str]
    sample_quote: Dict[str, str]


# --- Rich Datasets ---

EPICS_DATA: Dict[str, FolkEpic] = {
    "madho_singh_bhandari": FolkEpic(
        id="madho_singh_bhandari",
        title_garhwali="माधो सिंह भंडारी",
        title_english="Madho Singh Bhandari (The Warrior of Maletha)",
        genre="Pawaada (Historical Heroic Epic)",
        hero="Madho Singh Bhandari (मलेथा का सेनापति)",
        region="Maletha, Devprayag, Tehri Garhwal",
        synopsis=(
            "The monumental epic of Madho Singh Bhandari, the chief commander of the Garhwal Kingdom under Maharaja Mahipat Shah. "
            "Witnessing fertile yet parched terraced fields in Maletha, Madho Singh carved a stone irrigation canal (गूल) "
            "through solid mountain rock across the Chandrabhaga river, overcoming impossible geological hurdles and sacrificing "
            "his own son Gajai to appease the mountain goddess of waters."
        ),
        cultural_significance=(
            "Celebrated across Uttarakhand as the epitome of filial sacrifice, visionary engineering, and unyielding valor. "
            "The idiom 'एक बेटा गजे, एक कुलो मलेथे' (One son Gajai, one water canal for Maletha) symbolizes immortal public dedication."
        ),
        sample_verses=[
            {
                "garhwali": "एक बेटा गजे, एक कुलो मलेथे। डांडा काटी पानी ल्याए माधो भंडारी मलेथे॥",
                "roman": "Ek beta Gaje, ek kulo Malethe. Danda kaati paani lyaaye Madho Bhandari Malethe.",
                "english": "One beloved son Gajai sacrificed, one life-giving canal dug for Maletha. Madho Bhandari carved the mountain crest to bring flowing water."
            }
        ]
    ),
    "jeetu_bagdwal": FolkEpic(
        id="jeetu_bagdwal",
        title_garhwali="जीतू बगड़वाल",
        title_english="Jeetu Bagdwal (The Enchanted Piper of Bagodi)",
        genre="Pawaada / Romantic Supernatural Ballad",
        hero="जीतू बगड़वाल (Jeetu Bagdwal)",
        region="Bagodi, Garhwal (Rudraprayag / Chamoli)",
        synopsis=(
            "Jeetu Bagdwal, an extraordinary flute player and gallant young warrior of village Bagodi, journeys to the high alpine "
            "bugyals of Khait Parvat to sow seasonal paddy. As his magical flute echoes across mountain mist, the seven celestial "
            "mountain fairies (आंछरियां) are mesmerized, fall in love with him, and cast a divine spell to whisk him away to their ethereal realm."
        ),
        cultural_significance=(
            "Central folklore of Garhwali youth, romance, and the mystical aura of Khait Parvat, the legendary Fairy Mountain. "
            "Sung during winter hearth gatherings and reenacted in ritual folk dramas."
        ),
        sample_verses=[
            {
                "garhwali": "बाँसुरी बजै जीतू बगड़वाल खैत का डांडा। आंछरियों का मन मोह्या, रूप का उजाला॥",
                "roman": "Bansuri bajai Jeetu Bagdwal Khait ka danda. Aanchhariyon ka man mohya, roop ka ujaala.",
                "english": "Jeetu Bagdwal played his sweet flute on the high ridge of Khait. Enchanting the celestial fairies with divine music and youthful grace."
            }
        ]
    ),
    "kaphua": FolkEpic(
        id="kaphua",
        title_garhwali="कफुआ (कफू पाको, मैं नी चाखो)",
        title_english="Kaphua (The Tragic Ballad of the Cuckoo Bird)",
        genre="Folk Legend / Bird Ballad",
        hero="The Brother and Sister of Garhwal",
        region="Throughout Uttarakhand high hills",
        synopsis=(
            "A heartbreaking folk legend explaining the melancholic cry of the Himalayan cuckoo. A brother entrusted a basket of ripe "
            "mountain berries (काफल) to his sister while working in the terraced fields. Under the afternoon sun, the berries naturally "
            "shrank and lost weight. The brother mistook the reduced volume for deceit and struck his sister dead. When morning dew revived "
            "the berries to full size, grief-stricken with remorse, the brother perished and transformed into the Kaphua bird, crying eternally."
        ),
        cultural_significance=(
            "The soul-stirring cry 'कफू पाको, मैं नी चाखो' (The Kafal ripened, but I did not taste them) echoes through pine forests "
            "each spring, symbolizing remorse, innocence, and fraternal love."
        ),
        sample_verses=[
            {
                "garhwali": "कफू पाको, मैं नी चाखो! पुर पुतै, पुर पुतै, दिन ढल्या डांडा माथे॥",
                "roman": "Kafu pako, main ni chaakho! Pur putai, pur putai, din dhalya danda maathe.",
                "english": "The wild berries ripened, yet I never tasted them! The basket was full, as daylight faded over the mountain crest."
            }
        ]
    ),
    "saru_kunwar": FolkEpic(
        id="saru_kunwar",
        title_garhwali="सरू कुंवर",
        title_english="Saru Kunwar and Rani Champa",
        genre="Pawaada (Chivalric Romance Ballad)",
        hero="Saru Kunwar",
        region="Chandpur Garhi / Srinagar Garhwal",
        synopsis=(
            "The classic romantic ballad of knight Saru Kunwar, celebrated in Govind Chatak's Gadwali Lok Gathayen (1958). "
            "A tale of chivalry, trials of true love, and royal intrigue set during the medieval Panwar dynasty of Garhwal."
        ),
        cultural_significance="Preserved in oral ballad form by traditional hereditary bards (औजी and ढाकी).",
        sample_verses=[
            {
                "garhwali": "घौड़ा दौड़ाए सरू कुंवर चांदपुर डांडा। तलवार चमके हाथ मा, वीर रस बाणा॥",
                "roman": "Ghauda daudaaye Saru Kunwar Chandpur danda. Talwaar chamke haath ma, veer ras baana.",
                "english": "Saru Kunwar spurred his steed along the high ridges of Chandpur, sword flashing bright in the garb of mountain chivalry."
            }
        ]
    ),
    "ranubhaut": FolkEpic(
        id="ranubhaut",
        title_garhwali="रणुभौत (अजेय भड़)",
        title_english="Ranubhaut (The Invincible Warrior)",
        genre="Pawaada (Martial Chivalric Ballad)",
        hero="Ranu Bhaut (रणु रौतेली)",
        region="Rawain, Uttarkashi / Tehri Garhwal",
        synopsis=(
            "The warrior epic of Ranubhaut, the peerless wrestler and swordsman who defended the northern frontiers of Garhwal "
            "against incursions from Tibet and rival warlords, renowned for superhuman endurance and loyalty to his motherland."
        ),
        cultural_significance="Emblem of raw Himalayan courage and knightly honor (भड़ परंपरा).",
        sample_verses=[
            {
                "garhwali": "रणु रौतेलो भड़ बण्यो, गढ़ मा धाक जमाए। सत्रु भागा थर-थर, जब रण मा ललकारे॥",
                "roman": "Ranu Rautelo bhad banyo, Garh ma dhaak jamaaye. Satru bhaaga thar-thar, jab ran ma lal-kaare.",
                "english": "Ranu Rautela stood as the fearless champion, instilling awe across the hill fortresses. Foes trembled when his war cry shook the battlefield."
            }
        ]
    ),
    "dhari_devi": FolkEpic(
        id="dhari_devi",
        title_garhwali="धारी देवी जागर",
        title_english="The Jagar of Dhari Devi (Guardian Deity of Garhwal)",
        genre="Jagar (Sacred Spirit Invocation)",
        hero="Goddess Kali / Dhari Devi",
        region="Kalyasaur, Alaknanda River, Pauri/Rudraprayag border",
        synopsis=(
            "The sacred myth of the upper half of Goddess Kali enshrined on a rocky island in the turbulent Alaknanda River. "
            "Local legends recount how the sacred idol floated upstream against river torrents to rest at Dhari village, "
            "venerated as the supreme protector of the Char Dham pilgrims and the heartbeat of Garhwal."
        ),
        cultural_significance="Supreme guardian deity whose blessing is invoked before undertaking any Himalayan journey.",
        sample_verses=[
            {
                "garhwali": "अलकनंदा की बीच धार मा धारी की देवी। रक्षा करे गढ़वाल की, जय-जय माँ भवानी॥",
                "roman": "Alaknanda ki beech dhaar ma Dhari ki Devi. Raksha kare Garhwal ki, jai-jai Maa Bhawani.",
                "english": "Amidst the rushing waters of Alaknanda stands Dhari Devi, eternal guardian of Garhwal's sacred realm."
            }
        ]
    )
}

POEMS_DATA: List[FolkPoem] = [
    FolkPoem(
        id="chaita_ki_chaitwali",
        title_garhwali="चैता की चैतवाली",
        title_english="Chaita Ki Chaitwali (Spring Blossom Ballad)",
        form="Chaitwali",
        theme="Return of spring, blossoming of Buransh, sisters' yearning for maternal home",
        verses_garhwali=[
            "ऐगे चैत को मैनो, फूल फुली ग्या बुराँश।",
            "डांडा-कांठा हरियाया, धड़कन लागी छाती मा सांस॥",
            "मैत की याद आई ब्वारी, नौनी रोवे सौरास मा।",
            "कबे औलो मेरो भैजी, डोली लेगे मैत मा॥"
        ],
        verses_roman=[
            "Aege Chait ko maino, phool phooli gya buransh.",
            "Danda-kantha hariyaaya, dhadkan laagi chhaati ma saans.",
            "Mait ki yaad aayi bwaari, nauni rove sauras ma.",
            "Kabe aulo mero bhaiji, doli lege mait ma."
        ],
        english_translation=(
            "The month of Chaitra has arrived; red rhododendrons have burst into bloom across the mountains. "
            "The alpine ridges have turned lush green, filling the chest with mountain breath. "
            "The young bride remembers her maternal home and weeps softly in her in-laws' village: "
            "'When will my dear brother come to take me home in the palanquin?'"
        ),
        cultural_context="Sung by traditional Auji singers visiting hill homes during the auspicious spring month of Chaitra."
    ),
    FolkPoem(
        id="bedu_pako_baramasa",
        title_garhwali="बेड़ू पाको बारामासा",
        title_english="Bedu Pako Baramasa (Wild Figs Ripen Twelve Seasons)",
        form="Baramasa",
        theme="Wild nature, seasonal bounty, timeless Himalayan identity",
        verses_garhwali=[
            "बेड़ू पाको बारामासा, नरैण काफल पाको चैता मेरी छैला।",
            "रूं-रूणी बांसा बाजे, नरैण डांडा-कांठा मा मेरी छैला॥",
            "आप खाई काफल मीठा, नरैण मैतल्या कु दिन याद मेरी छैला॥"
        ],
        verses_roman=[
            "Bedu pako baramasa, Narain kafal pako Chaita meri chhaila.",
            "Roon-rooni baansa baaje, Narain danda-kantha ma meri chhaila.",
            "Aap khaayi kafal meetha, Narain maitalya ku din yaad meri chhaila."
        ],
        english_translation=(
            "The wild Himalayan fig ripens through all twelve seasons, and sweet red bayberries ripen in Chaitra, my beloved! "
            "The sweet melodies of the mountain flute echo across ridges and valleys, calling forth memories of home."
        ),
        cultural_context="The undisputed universal anthem of Uttarakhand celebrated globally across the diaspora."
    ),
    FolkPoem(
        id="ghughuti_na_baas",
        title_garhwali="घूघुती ना बास",
        title_english="Ghughuti Na Baas (Lament of the Mountain Dove)",
        form="Jhumeilo",
        theme="Melancholy, maternal affection, solitude of mountain women",
        verses_garhwali=[
            "घूघुती ना बास तू डांडा की डाली मा।",
            "तेरी बास सुणी मैत की खुदेड़ लगदी छाती मा॥",
            "सुदूर डांडा मा बैठी रोवे पंछी उदास।",
            "परदेसी ब्वारी कु दिल तड़पे सौरास॥"
        ],
        verses_roman=[
            "Ghughuti na baas tu danda ki daali ma.",
            "Teri baas suni mait ki khuded lagdi chhaati ma.",
            "Sudoor danda ma baithi rove panchhi udaas.",
            "Pardesi bwaari ku dil tadpe sauras."
        ],
        english_translation=(
            "Sing not your plaintive song, little dove, perched upon that mountain branch. "
            "Hearing your calling awakens a deep, painful longing for my mother's home in my chest."
        ),
        cultural_context="Embodies 'खुदेड़' (khuded)—the unique Pahari emotion of nostalgic homesickness."
    ),
    FolkPoem(
        id="mangal_geet",
        title_garhwali="मांगल गीत (दैवीय विवाह संस्कार)",
        title_english="Mangal Geet (Auspicious Wedding Ritual Chants)",
        form="Mangal",
        theme="Sacred wedding ceremonies, invoking deities, blessing bride and groom",
        verses_garhwali=[
            "सुफल होवे ईं आंगन मा, गणेश जी पधारे।",
            "रिद्धि-सिद्धि संग ल्याए, मंगल चार गावे॥",
            "कन्या दानी पिता धन्य, ब्वै की गोदी भारी।",
            "गंगा-जमुना सी निर्मल, जोड़ी जुग-जुग प्यारी॥"
        ],
        verses_roman=[
            "Suphal hove een aangan ma, Ganesh ji padhaare.",
            "Riddhi-siddhi sang lyaaye, mangal chaar gaave.",
            "Kanya daani pita dhanya, bwai ki godi bhaari.",
            "Ganga-Jamuna si nirmal, jodi jug-jug pyaari."
        ],
        english_translation=(
            "May all blessings blossom in this courtyard as Lord Ganesha arrives with Riddhi and Siddhi. "
            "Blessed is the father giving away the bride, blessed is the mother's lap; pure as Ganga and Yamuna, may this union thrive forever."
        ),
        cultural_context="Chanted exclusively by women elders and hereditary mangal singers during all 16 Garhwali rites of passage."
    )
]

AUTHORS_DATA: Dict[str, GarhwaliAuthor] = {
    "bhajan_singh": GarhwaliAuthor(
        name_garhwali="भजन सिंह 'सिंह'",
        name_english="Bhajan Singh 'Singh'",
        era="1905–1996",
        significance="Pioneer of modern Garhwali epic poetry and cultural philosophy; author of the immortal epic 'Singhnaad'.",
        famous_works=["सिंहनाद (Singhnaad, 1932)", "आर्यों का मूल स्थान मध्य हिमालय", "गढ़वाली लोक साहित्य"],
        sample_quote={
            "garhwali": "उठो गढ़वाली वीरों, अपनी मातृभूमि की रक्षा करो।",
            "english": "Arise, courageous souls of Garhwal, and defend the honor of your motherland."
        }
    ),
    "chandra_kunwar_bartwal": GarhwaliAuthor(
        name_garhwali="चन्द्रकुंवर बर्त्वाल",
        name_english="Chandra Kunwar Bartwal",
        era="1919–1947",
        significance="Known as the 'Kalidasa of the Himalayas' (हिमवंत का कालिदास); transcendent romantic nature poet of Rudraprayag.",
        famous_works=["काफल पाको", "कंकण", "नंदादेवी", "बाँसुरी", "गीत-माधवी"],
        sample_quote={
            "garhwali": "काफल पाको चैता की रुत, बुराँश लाल भयो डांडा माथे।",
            "english": "The wild berries ripened in the season of spring; crimson rhododendrons glowed upon the heights."
        }
    ),
    "narendra_singh_negi": GarhwaliAuthor(
        name_garhwali="नरेन्द्र सिंह नेगी",
        name_english="Narendra Singh Negi",
        era="1949–Present",
        significance="'Garh-Gaurav' and People's Bard (जनकवि); iconic singer, lyricist, and cultural conscience of Uttarakhand.",
        famous_works=["गाड़-कुथार", "खुड़ी-खुड़ी माथे ते", "टका कि तीन", "नौछमी नरैण"],
        sample_quote={
            "garhwali": "ठंडो रे ठंडो मेरो पहाड़ को पाणी, ठंडो रे ठंडो!",
            "english": "Sweet and cool is the crystal spring water of my mountain homeland!"
        }
    ),
    "tara_dutt_gairola": GarhwaliAuthor(
        name_garhwali="तारा दत्त गैरोला",
        name_english="Tara Dutt Gairola",
        era="1883–1940",
        significance="Pioneering scholar, freedom fighter, and poet; co-authored 'Himalayan Folklore' (1935) and penned the poignant classic 'Sadei'.",
        famous_works=["सदेई (Sadei, 1921)", "Himalayan Folklore (1935)", "Garhwali Kavitaawali"],
        sample_quote={
            "garhwali": "सदेई रोवे मैत की याद मा, डांडा-कांठा गूंजे विरह मा।",
            "english": "Sadei weeps in remembrance of her maternal home; high mountain ridges echo with sorrow."
        }
    ),
    "govind_chatak": GarhwaliAuthor(
        name_garhwali="डॉ० गोविन्द चातक",
        name_english="Dr. Govind Chatak",
        era="1933–2007",
        significance="Foundational linguist, folklorist, and playwright; author of 'Garhwali Bhasha' (1959) and 'Gadwali Lok Gathayen' (1958).",
        famous_works=["गढ़वाली भाषा (1959)", "गढ़वाली लोक गाथाएं (1958)", "गढ़वाली लोकगीत (1956)", "जीतू बगड़वाल (नाटक)"],
        sample_quote={
            "garhwali": "लोकगाथाएं केवल अतीत की कथाएं नहीं, बल्कि पहाड़ की आत्मा की जीवित धड़कन हैं।",
            "english": "Folk epics are not merely stories of the past, but the living heartbeat of the Himalayan soul."
        }
    ),
    "haridatta_bhatt": GarhwaliAuthor(
        name_garhwali="डॉ० हरिदत्त भट्ट 'शैलेश'",
        name_english="Dr. Haridatta Bhatt 'Shailesh'",
        era="1926–2004",
        significance="Eminent scholar and author of the comprehensive treatise 'Garhwali Bhasha Aur Uska Sahitya' (Hindi Samiti, 1976).",
        famous_works=["गढ़वाली भाषा और उसका साहित्य (1976)", "उत्तराखंड के लोकतीर्थ", "शैल शिखर"],
        sample_quote={
            "garhwali": "गढ़वाली भाषा की समृद्धता उसकी अद्वितीय व्याकरणिक और मुहावरेदार शक्ति में निहित है।",
            "english": "The richness of the Garhwali language lies in its distinctive grammatical and idiomatic vigor."
        }
    ),
    "harikrishna_raturi": GarhwaliAuthor(
        name_garhwali="रायबहादुर पं० हरिकृष्ण रतूड़ी",
        name_english="Pt. Harikrishna Raturi",
        era="1878–1933",
        significance="Premier historian of Garhwal; author of 'Garhwal Ka Itihas' (1928) and translator of the sacred Kedar Khand.",
        famous_works=["गढ़वाल का इतिहास (1928)", "केदारखंड अनुवाद (1910)", "गढ़वाल वर्णन"],
        sample_quote={
            "garhwali": "गढ़वाल का इतिहास उसके दुर्गम शिखरों और स्वाभिमानी संतानों की गौरव गाथा है।",
            "english": "The history of Garhwal is a proud saga of its impregnable peaks and valiant sons."
        }
    ),
    "abodh_bandhu_bahuguna": GarhwaliAuthor(
        name_garhwali="अबोध बंधु बहुगुणा",
        name_english="Abodh Bandhu Bahuguna",
        era="1927–2001",
        significance="Pioneering prose stylist, dramatist, and lexicographer; compiled the monumental 'Garhwali Shabdkosh' (1980).",
        famous_works=["गढ़वाली शब्दकोश (1980)", "माई को लाल (नाटक)", "दगड्या (कहानियां)", "गढ़ सुमना"],
        sample_quote={
            "garhwali": "शब्द ही भाषा के प्राण हैं, और मातृभाषा में ही हमारी सांस्कृतिक पहचान सुरक्षित है।",
            "english": "Words are the life-breath of language, and in our mother tongue alone is cultural identity preserved."
        }
    ),
    "kanhaiyalal_dandriyal": GarhwaliAuthor(
        name_garhwali="कन्हैयालाल डंडरियाल",
        name_english="Kanhaiyalal Dandriyal",
        era="1932–2003",
        significance="One of the finest modern poets of Garhwal; master of social satire and nature poetry in 'Anwal' and 'Mangtu'.",
        famous_works=["अणवाल (1966)", "मंगतू (1972)", "भिलंगना (1975)"],
        sample_quote={
            "garhwali": "अणवाल डांडा मा घूमे, बकरियों का संग मा जिंदगी बीते।",
            "english": "The alpine shepherd roams the heights, living his tranquil life alongside grazing flocks."
        }
    ),
    "shanti_chaudhary": GarhwaliAuthor(
        name_garhwali="डॉ० शांति चौधरी",
        name_english="Dr. Shanti Chaudhary",
        era="Contemporary Scholar",
        significance="Eminent folklore researcher; author of 'Garhwali Lokkala Aur Loksahitya Ka Tulnatmak Anusilan' (1994).",
        famous_works=["गढ़वाली लोककला और लोकसाहित्य (1994)", "गढ़वाल की वीरांगनाएं", "लोकनृत्य एवं लोकनाट्य"],
        sample_quote={
            "garhwali": "लोकसंस्कृति मा नारी का त्याग और साहस ही गढ़वाल की सच्ची धरोहर है।",
            "english": "In folk culture, the sacrifice and courage of women represent the true heritage of Garhwal."
        }
    )
}


class LiteratureTreasury:
    """Interface to access Garhwali folk epics, poetry, and canonical authors."""

    @staticmethod
    def get_epic(epic_id: str) -> Optional[FolkEpic]:
        return EPICS_DATA.get(epic_id)

    @staticmethod
    def list_epics() -> List[FolkEpic]:
        return list(EPICS_DATA.values())

    @staticmethod
    def list_poems(form: Optional[str] = None) -> List[FolkPoem]:
        if form:
            return [p for p in POEMS_DATA if p.form.lower() == form.lower()]
        return POEMS_DATA

    @staticmethod
    def get_author(author_id: str) -> Optional[GarhwaliAuthor]:
        return AUTHORS_DATA.get(author_id)

    @staticmethod
    def list_authors() -> List[GarhwaliAuthor]:
        return list(AUTHORS_DATA.values())


# Backward-compatible dictionaries and functions
POEMS = [
    {
        "id": p.id,
        "title": f"{p.title_garhwali} ({p.title_english})",
        "genre": p.form,
        "description": p.theme
    }
    for p in POEMS_DATA
]

EPICS = [
    {
        "id": e.id,
        "title": f"{e.title_garhwali} ({e.title_english})",
        "hero": e.hero,
        "theme": e.synopsis
    }
    for e in EPICS_DATA.values()
]

AUTHORS = [
    {
        "id": k,
        "name": f"{a.name_garhwali} ({a.name_english})",
        "era": a.era,
        "work": a.significance
    }
    for k, a in AUTHORS_DATA.items()
]


def poems() -> List[Dict[str, Any]]:
    return POEMS


def epics() -> List[Dict[str, Any]]:
    return EPICS


def authors() -> List[Dict[str, Any]]:
    return AUTHORS
