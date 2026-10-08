"""
Garhwali surnames, clans, historical lineages, gotras, and social structure of Uttarakhand.
Includes comprehensive cataloguing of Brahmin, Rajput/Kshatriya, Marchha/Tolchha/Jadh, and Artisan/Shilpkar heritage clans.
Based on historical documentation from Hari Krishna Raturi's 'Garhwal Ka Itihas', Pati Ram's 'Garhwal: Ancient and Modern',
Gunanand Juyal, Govind Chatak, and colonial ethnographic records.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class GarhwaliSurname:
    id: str
    surname_garhwali: str
    surname_roman: str
    title: str
    community: str  # "Brahmin", "Rajput / Kshatriya", "Marchha / Alpine Bhotia", "Shilpkar / Artisan"
    traditional_title_or_role: str
    gotras: List[str]
    ancestral_villages_or_origin: str
    notable_historical_figures: List[str]
    cultural_and_historical_notes: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


SURNAMES_DATA: Dict[str, GarhwaliSurname] = {
    # ==================== GARHWALI BRAHMIN CLANS ====================
    "khanduri": GarhwaliSurname(
        id="khanduri",
        surname_garhwali="खंडूड़ी",
        surname_roman="Khanduri",
        title="Royal Kanungos, Chief Chroniclers & Scribes of Srinagar Kingdom",
        community="Brahmin",
        traditional_title_or_role="Chief Kanungos, royal record keepers, diplomatic envoys, and ministers of the Panwar kings.",
        gotras=["भारद्वाज (Bharadwaj)", "शांडिल्य (Shandilya)"],
        ancestral_villages_or_origin="Khandura village in Chamoli/Pauri; established in Srinagar, Lansdowne, and Pauri.",
        notable_historical_figures=["Ramachandra Khanduri (Royal Envoy to the Mughal Court)", "Major General B.C. Khanduri (Former Chief Minister of Uttarakhand & Union Minister)"],
        cultural_and_historical_notes="One of the primary administrative Brahmin families of Garhwal. Held hereditary posts as Kanungo under the Rajas of Srinagar and later under British Garhwal."
    ),
    "nautiyal": GarhwaliSurname(
        id="nautiyal",
        surname_garhwali="नौटियाल",
        surname_roman="Nautiyal",
        title="Royal Astronomers, Astrologers (Jyotish) & Philosophers",
        community="Brahmin",
        traditional_title_or_role="Hereditary royal astrologers (Raj-jyotishi), Sanskrit grammarians, and judicial advisers.",
        gotras=["कश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Nauti village in Karanprayag block (Chamoli) — the sacred hub where Nanda Devi's Chanti (silver palanquin) is crafted for the Raj Jat.",
        notable_historical_figures=["Pt. Shambhu Prasad Nautiyal (Eminent scholar)", "Anil Nautiyal (Eminent environmental educator)"],
        cultural_and_historical_notes="Originating from Nauti village, the Nautiyals are deeply bound to the sacred 280 km Nanda Devi Raj Jat pilgrimage, serving as the ceremonial custodians of the holy umbrella (Chhantoli)."
    ),
    "bahuguna": GarhwaliSurname(
        id="bahuguna",
        surname_garhwali="बहुगुणा",
        surname_roman="Bahuguna",
        title="Eminent Statesmen, Philosophers, Poets & Ecologists",
        community="Brahmin",
        traditional_title_or_role="Royal counselors, diplomats, educators, and social reformers.",
        gotras=["गर्ग (Garga)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Bugu / Bughana in Tehri Garhwal; ancestral branches across Pauri and Tehri.",
        notable_historical_figures=["Hemwati Nandan Bahuguna (1919-1989, Former Chief Minister of UP & Freedom Fighter)", "Sunderlal Bahuguna (1927-2021, Padma Vibhushan, Architect of the Chipko Movement & Himalayan conservationist)", "Vijay Bahuguna (Former Chief Minister of Uttarakhand)"],
        cultural_and_historical_notes="A family line synonymous with social consciousness, Himalayan ecology, and modern statecraft in 20th-century Uttarakhand."
    ),
    "gairola": GarhwaliSurname(
        id="gairola",
        surname_garhwali="गैरोला",
        surname_roman="Gairola",
        title="Pioneering Folklorists, Legal Scholars & Bards of Garhwali Heritage",
        community="Brahmin",
        traditional_title_or_role="Judges, legal jurists, folklorists, and custodians of Garhwali oral poetry.",
        gotras=["कौशिक (Kaushika)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Gairoli village in Chamoli/Pauri; settled extensively in Srinagar and Dehradun.",
        notable_historical_figures=["Tara Dutt Gairola (1875-1940, Co-author of 'Himalayan Folklore', pioneer of the Garhwal Union)", "Dr. Vachaspati Gairola (Renowned Sanskrit and Indological scholar)"],
        cultural_and_historical_notes="Tara Dutt Gairola was among the very first Garhwali intellectuals to systematize and publish Garhwali oral ballads, pawadas, and folk tales in English and Devanagari."
    ),
    "uniyal": GarhwaliSurname(
        id="uniyal",
        surname_garhwali="उनियाल",
        surname_roman="Uniyal",
        title="Royal Preceptors & Custodians of Devi Shrines",
        community="Brahmin",
        traditional_title_or_role="Rajguru to the Rajas of Tehri, priests at Surkanda Devi and Kunjapuri shrines.",
        gotras=["काश्यप (Kashyapa)", "भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Ooni village in Tehri Garhwal.",
        notable_historical_figures=["Mahidhar Uniyal (Court Astrologer to Raja Sudarshan Shah)", "Pt. Govind Ram Uniyal (Freedom Fighter and Social Reformer)"],
        cultural_and_historical_notes="Hereditary priests at several supreme Shaktipeeths of Tehri Garhwal, including Surkanda Devi temple atop the ridge near Dhanaulti."
    ),
    "semwal": GarhwaliSurname(
        id="semwal",
        surname_garhwali="सेमवाल",
        surname_roman="Semwal",
        title="Hereditary Head Priests (Pujaris) of Gangotri Dham",
        community="Brahmin",
        traditional_title_or_role="Pujaris, caretakers, and ritual custodians of Shri Gangotri Temple and Mukhba winter seat.",
        gotras=["शांडिल्य (Shandilya)"],
        ancestral_villages_or_origin="Sem and Mukhba (Mukhimath) villages in Uttarkashi district on the Bhagirathi river.",
        notable_historical_figures=["Pt. Vidyadhar Semwal (Traditional Head Priest of Gangotri Dham)"],
        cultural_and_historical_notes="Every year when Gangotri shrine closes for winter on Bhai Dooj, the Semwal priests carry the idol of Goddess Ganga in a doli to Mukhba village where she is worshipped for six months."
    ),
    "dimri": GarhwaliSurname(
        id="dimri",
        surname_garhwali="डिमरी",
        surname_roman="Dimri",
        title="Hereditary Culinary Caretakers & Executive Priests of Badrinath",
        community="Brahmin",
        traditional_title_or_role="Custodians of the sacred food (Bhog) and daily seva at Badrinath Dham alongside the Namboodiri Rawal.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Dimmer village in Chamoli district near Karnaprayag.",
        notable_historical_figures=["Bhuwan Chandra Dimri (Scholar of Badri-Mahatmya)"],
        cultural_and_historical_notes="The Dimri Brahmins have held the sacred hereditary right to assist the Rawal, prepare the Mahaprasad bhog, and organize temple ceremonies for over a millennium."
    ),
    "bhatt": GarhwaliSurname(
        id="bhatt",
        surname_garhwali="भट्ट",
        surname_roman="Bhatt",
        title="Vedic Grammarians, Rawals of Rudranath & Devprayag Scholars",
        community="Brahmin",
        traditional_title_or_role="Head priests of Rudranath (one of the Panch Kedar), Pujaris of Devprayag Raghunathji, and teachers of Sanskrit.",
        gotras=["भारद्वाज (Bharadwaj)", "वशिष्ठ (Vashishta)"],
        ancestral_villages_or_origin="Devprayag, Gopeshwar, and Srinagar; historical migrations from Maharashtra and Karnataka.",
        notable_historical_figures=["Chandi Prasad Bhatt (Padma Bhushan, Ramon Magsaysay awardee, Pioneer of the Chipko Movement)", "Dr. Haridatta Bhatt 'Shailesh' (1926-2006, Renowned author & educator)"],
        cultural_and_historical_notes="Chandi Prasad Bhatt mobilized Himalayan villagers in Gopeshwar in 1973 through Dasholi Gram Swarajya Mandal, igniting the Chipko movement against commercial deforestation."
    ),
    "thapliyal": GarhwaliSurname(
        id="thapliyal",
        surname_garhwali="थपलियाल",
        surname_roman="Thapliyal",
        title="Royal Preceptors (Rajgurus) & Scholars of the Srinagar Court",
        community="Brahmin",
        traditional_title_or_role="Rajguru to the Panwar Rajas, temple administrators, and scholars of Dharma-shastra.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Thapli village in Pauri Garhwal.",
        notable_historical_figures=["Pandit Chakradhar Thapliyal (Royal Preceptor to Raja Pradyumna Shah)", "Lalit Mohan Thapliyal (Distinguished Garhwali playwright and scholar)"],
        cultural_and_historical_notes="Traditionally served as spiritual and moral advisers to the sovereign rulers of Srinagar Garhwal."
    ),
    "raturi": GarhwaliSurname(
        id="raturi",
        surname_garhwali="रतूड़ी",
        surname_roman="Raturi",
        title="Distinguished Historians, Ministers & Chroniclers of Garhwal",
        community="Brahmin",
        traditional_title_or_role="Diwans, judges, historians, and educators.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Ratura village in Tehri Garhwal.",
        notable_historical_figures=["Pandit Hari Krishna Raturi (1878-1934, Author of the seminal history 'Garhwal Ka Itihas', Diwan of Tehri Garhwal)"],
        cultural_and_historical_notes="Pandit Hari Krishna Raturi's magnum opus 'Garhwal Ka Itihas' (published 1928) remains the bedrock historical treatise on the dynasties, forts, culture, and society of Garhwal."
    ),
    "dhasmana": GarhwaliSurname(
        id="dhasmana",
        surname_garhwali="धस्माना",
        surname_roman="Dhasmana",
        title="Judges, Administrative Scribes & Freedom Fighters",
        community="Brahmin",
        traditional_title_or_role="Judicial officers, administrative patwaris, and literary chroniclers.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Dhasman village in Lansdowne tehsil, Pauri Garhwal.",
        notable_historical_figures=["Bhairab Datt Dhasmana (Freedom fighter & educator)", "Dr. M.M. Dhasmana (Anthropological scholar of Himalayan defense)"],
        cultural_and_historical_notes="Prominent in British-era education and civil administration throughout southern Garhwal."
    ),
    "chamoli": GarhwaliSurname(
        id="chamoli",
        surname_garhwali="चमोली",
        surname_roman="Chamoli",
        title="Custodians of Mountain Hermitages & Priests",
        community="Brahmin",
        traditional_title_or_role="Priests, village astrologers, and spiritual instructors.",
        gotras=["वशिष्ठ (Vashishta)"],
        ancestral_villages_or_origin="Chamola / Chamoli in Alaknanda valley.",
        notable_historical_figures=["Pt. Jagdamba Prasad Chamoli (Local educator and folklorist)"],
        cultural_and_historical_notes="Name tied directly to the sacred Chamoli district heartland of upper Garhwal."
    ),

    # ==================== GARHWALI RAJPUT / KSHATRIYA CLANS ====================
    "panwar": GarhwaliSurname(
        id="panwar",
        surname_garhwali="पंवार / परमार",
        surname_roman="Panwar / Parmar",
        title="The Royal Dynasty of Garhwal Kingdom (Chandpurgarh & Srinagar)",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Kings, sovereigns, commanders-in-chief, and sovereign rulers of the 52 Garhs.",
        gotras=["शौनक (Shaunaka)", "वशिष्ठ (Vashishta)"],
        ancestral_villages_or_origin="Dhar (Malwa) origin via Prince Kanakpal (888 CE); founded Chandpurgarh, later shifted capital to Devalgarh (1512 CE) and Srinagar (1517 CE).",
        notable_historical_figures=["Raja Kanakpal (Founder of dynasty in 888 CE)", "Raja Ajaypal (Consolidator of the 52 Garhs into a unified Garhwal kingdom)", "Raja Man Shah (Conqueror of Doti and Champawat)", "Raja Fateh Shah (Reigned 1684-1716, patron of arts and fierce military sovereign)"],
        cultural_and_historical_notes="Reigned continuously for almost a millennium over the Garhwal Kingdom, establishing peace, building stone forts, unifying dialects, and founding high Himalayan traditions."
    ),
    "negi": GarhwaliSurname(
        id="negi",
        surname_garhwali="नेगी",
        surname_roman="Negi",
        title="Martial Commanders, Fortress Governors & Thokdars",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Military generals (Senapati), fortress commanders (Garhadhipati), and provincial governors.",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)", "सूर्यवंशी (Suryavanshi)"],
        ancestral_villages_or_origin="Encompasses renowned subclans across Garhwal: Aswal Negi, Lodha Negi, Chauhan Negi, Kaphola Negi, etc.",
        notable_historical_figures=["Rifleman Gabar Singh Negi (1895-1915, Victoria Cross recipient in WWI at Neuve Chapelle)", "Narendra Singh Negi (Renowned voice of Uttarakhand folk music & conscience of the hills)", "Trevor Negi / Col. D.S. Negi (Distinguished military commanders)"],
        cultural_and_historical_notes="The title 'Negi' derives from 'Nega' (honorary stipends and feudal privileges). Known historically as fierce warriors who defended the passes against Rohillas and Gurkhas."
    ),
    "rawat": GarhwaliSurname(
        id="rawat",
        surname_garhwali="रावत",
        surname_roman="Rawat",
        title="Feudal Lords of Rawatsar, Chieftains & Military Leaders",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Autonomous feudal rulers (Rawats of Rawatsar), military commanders, and village headmen.",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Rawatsar pargana in Pauri Garhwal; branches in Chamoli and Uttarkashi.",
        notable_historical_figures=["General Bipin Rawat (1958-2021, India's First Chief of Defence Staff & Chief of Army Staff)", "Trivendra Singh Rawat (Former Chief Minister of Uttarakhand)", "Tirath Singh Rawat (Former Chief Minister of Uttarakhand)"],
        cultural_and_historical_notes="Originally titled 'Rao-kula' (princes/rulers), the Rawats held major estates and furnished thousands of valiant soldiers to the Garhwal Rifles."
    ),
    "bisht": GarhwaliSurname(
        id="bisht",
        surname_garhwali="बिष्ट",
        surname_roman="Bisht",
        title="Nobles, Estate Administrators & Cavalry Chieftains",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Derived from Sanskrit 'Vashishta' (the distinguished/noble); ministers, high officers, and estate overseers.",
        gotras=["भारद्वाज (Bharadwaj)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Dispersed throughout Pauri, Chamoli, and Tehri Garhwal.",
        notable_historical_figures=["Kavindra Madhukar Bisht (Garhwali literary bard)", "Ranger Mohan Singh Bisht (Defender of mountain ecosystems)"],
        cultural_and_historical_notes="A classical Pahari aristocratic lineage holding high status in village governance, traditional landholding, and civic diplomacy."
    ),
    "bhandari": GarhwaliSurname(
        id="bhandari",
        surname_garhwali="भंडारी",
        surname_roman="Bhandari",
        title="Hereditary Royal Treasurers & Legendary Heroic Warriors (Bhad)",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Hereditary keepers of the royal treasury, fortress wardens, and legendary combat heroes.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Maletha in Tehri Garhwal; also settled in Srinagar and Chamoli.",
        notable_historical_figures=["Madho Singh Bhandari (1595-1640, The legendary 'Garh Ka Sardar' who carved the Maletha irrigation canal through solid rock and led the Tibetan campaigns of Raja Mahipat Shah)"],
        cultural_and_historical_notes="Madho Singh Bhandari is an eternal folk icon in Garhwali pawadas. He engineered the miracle tunnel through a mountain at Maletha to bring water to parched fields."
    ),
    "chauhan": GarhwaliSurname(
        id="chauhan",
        surname_garhwali="चौहान",
        surname_roman="Chauhan",
        title="Descendants of Classical Agnikula Warriors & Fortress Lords",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Fortress wardens, military commanders, and landowners.",
        gotras=["वत्स (Vatsa)"],
        ancestral_villages_or_origin="Chandpurgarh, Dhanpur, Srinagar, and Jaunsar-Bawar.",
        notable_historical_figures=["Sher Singh Chauhan (Traditional commander of the Garhwali border guard)"],
        cultural_and_historical_notes="Claim descent from Prithviraj Chauhan's lineage who migrated to the Garhwal Himalaya during the medieval Turkish incursions."
    ),
    "bartwal": GarhwaliSurname(
        id="bartwal",
        surname_garhwali="बर्तवाल",
        surname_roman="Bartwal",
        title="Lyrical Poets & Royal Chamberlain Officers",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Chamberlains to the royal throne, poets, and military officers.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Maluotha in Chamoli; branches in Rudraprayag and Pauri.",
        notable_historical_figures=["Chandrakunwar Bartwal (1919-1947, The 'Keats of Hindi and Pahari Poetry', author of 'Himvant Ka Kavi', 'Kafal Pakko')"],
        cultural_and_historical_notes="Chandrakunwar Bartwal died young of tuberculosis at age 28, leaving behind timeless, evocative nature poetry steeped in the mists, rhododendrons, and silence of Garhwal."
    ),
    "gusain": GarhwaliSurname(
        id="gusain",
        surname_garhwali="गुसाईं",
        surname_roman="Gusain",
        title="Princes of the Royal Bloodline & Hereditary Jagirdars",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Royal scions, younger brothers of reigning Panwar kings granted hereditary estates (Maufidars).",
        gotras=["शौनक (Shaunaka)"],
        ancestral_villages_or_origin="Srinagar, Chandpurgarh, and Tehri royals.",
        notable_historical_figures=["Kunwar Surat Singh Gusain (Historic commander under Raja Fateh Shah)"],
        cultural_and_historical_notes="Title historically given to the younger sons and princes of the Garhwal royal court who governed feudatory valleys."
    ),
    "aswal": GarhwaliSurname(
        id="aswal",
        surname_garhwali="अस्वाल्",
        surname_roman="Aswal",
        title="The Legendary Cavalry Chieftains (Ashwapati) of Chandpur",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Hereditary commanders of the royal cavalry, knights, and estate holders of Aswalsyoon.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Aswalsyoon patti in Pauri Garhwal.",
        notable_historical_figures=["Jeetu Bagdwal (Legendary mythological hero & flute player beloved of the Acharis)"],
        cultural_and_historical_notes="Renowned for horse breeding and cavalry mastery. Folk epics remember the hero Jeetu Bagdwal who played magical flute tunes upon the alpine meadows of Bagdwalgaon."
    ),
    "kathait": GarhwaliSurname(
        id="kathait",
        surname_garhwali="कठैत",
        surname_roman="Kathait",
        title="Valiant Fortress Captains & Vanguard Warriors",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Commanders of mountain passes and frontier stockades.",
        gotras=["भारद्वाज (Bharadwaj)"],
        ancestral_villages_or_origin="Kathoor and Srinagar valleys.",
        notable_historical_figures=["Banwari Kathait (Legendary commander in the army of Raja Mahipat Shah)"],
        cultural_and_historical_notes="Celebrated in Garhwali oral ballads (Pawada) as fearless fighters who held hill fortresses against all odds."
    ),
    "sajwan": GarhwaliSurname(
        id="sajwan",
        surname_garhwali="सजवाण",
        surname_roman="Sajwan",
        title="Lords of Sajwankhol & Highland Chieftains",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Chieftains of Sajwankhol, frontier garrison masters, and thokdars.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Sajwankhol in Tehri Garhwal.",
        notable_historical_figures=["Gaje Singh Sajwan (Martial commander celebrated in local folk epics)"],
        cultural_and_historical_notes="Renowned for fierce independence and resistance against unauthorized tax intrusions."
    ),
    "kaintura": GarhwaliSurname(
        id="kaintura",
        surname_garhwali="कैंतुरा",
        surname_roman="Kaintura",
        title="Highland Chieftains of Rawain Valley",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Sayanas (tribal chieftains) of the upper Yamuna and Tons watersheds.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Rawain, Purola, and Jaunpur valleys.",
        notable_historical_figures=["Sayana Dayaram Kaintura (Historic leader of the Rawain movement)"],
        cultural_and_historical_notes="Prominent in the indigenous mountain resistance movements against arbitrary royal taxes (Dhandak movement) in Tehri state."
    ),
    "rana": GarhwaliSurname(
        id="rana",
        surname_garhwali="राणा",
        surname_roman="Rana",
        title="Highland Warrior Chieftains of Painkhanda and Uttarkashi",
        community="Rajput / Kshatriya",
        traditional_title_or_role="Border guards, valley administrators, and prominent military veterans.",
        gotras=["सूर्यवंशी (Suryavanshi)", "कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Painkhanda (Chamoli), Rawain (Uttarkashi), and Dhanpur.",
        notable_historical_figures=["Rifleman Jaswant Singh Rawat / Rana lineages of the border defense", "Mahavir Singh Rana (Traditional leader)"],
        cultural_and_historical_notes="Held frontier posts along the Tibetan boundary passes and served as vital links between the plains and alpine valleys."
    ),

    # ==================== ALPINE BORDER COMMUNITIES (MARCHHA / TOLCHHA / JADH) ====================
    "marchha": GarhwaliSurname(
        id="marchha",
        surname_garhwali="मारछा",
        surname_roman="Marchha",
        title="Trans-Himalayan Wool Merchants & Passes Guardians of Mana-Niti",
        community="Marchha / Alpine Bhotia",
        traditional_title_or_role="Trans-Himalayan barter merchants, yaks and sheep breeders, and custodians of high passes (Mana, Niti).",
        gotras=["सूर्यवंशी (Suryavanshi)"],
        ancestral_villages_or_origin="Mana (the last Indian village near Badrinath) and Niti Valley in Chamoli.",
        notable_historical_figures=["Kishan Singh Marchha / Pundit Explorers of Survey of India", "Chander Singh (Pioneer border trader)"],
        cultural_and_historical_notes="Bilingual masters of Pahari and Tibetan; historically carried out trade in salt, borax, and pashmina wool across the passes until 1962."
    ),
    "tolchha": GarhwaliSurname(
        id="tolchha",
        surname_garhwali="तोलछा",
        surname_roman="Tolchha",
        title="Sedentary Agronomists & High Valley Craftsmen of Painkhanda",
        community="Marchha / Alpine Bhotia",
        traditional_title_or_role="Farmers of buckwheat and rajma, wool weavers (Pankhi, Thulma, Chutka), and mountain guides.",
        gotras=["कश्यप (Kashyapa)"],
        ancestral_villages_or_origin="Dronagiri, Malari, and Joshimath sectors of Painkhanda (Chamoli).",
        notable_historical_figures=["Gram Pradhans of Malari Valley"],
        cultural_and_historical_notes="Deeply connected to the Ramman festival of Saloor-Dungra village; famed for their masterly weaving of sheep wool blankets."
    ),
    "jadh": GarhwaliSurname(
        id="jadh",
        surname_garhwali="जाढ़",
        surname_roman="Jadh",
        title="Himalayan Pastoralists & Traders of Nilang Valley",
        community="Marchha / Alpine Bhotia",
        traditional_title_or_role="Pastoralist herdsmen of mountain sheep and pashmina goats, border guides.",
        gotras=["प्रकृति-पूजक (Nature lineage)"],
        ancestral_villages_or_origin="Nilang and Jadhang valleys in Uttarkashi (now relocated to Bagori/Dunda).",
        notable_historical_figures=["Champa Singh Jadh (Border caravan master)"],
        cultural_and_historical_notes="A unique syncretic culture observing both Tibetan Buddhist and Hindu Pahari customs; winter settlement at Bagori village."
    ),

    # ==================== ARTISAN & FOLK PERFORMER LINEAGES (SHILPKAR / TRADITIONAL CRAFTS) ====================
    "auji_das": GarhwaliSurname(
        id="auji_das",
        surname_garhwali="औजी / दास",
        surname_roman="Auji / Das",
        title="Master Percussionists, Drummers of Dhol Damau & Preservers of Jagar Lore",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Hereditary custodians of the sacred Dhol Sagar (ocean of rhythms), ceremonial drummers, and oral ballad singers.",
        gotras=["शिव-शिष्य (Shiva-Shishya / Devotee)"],
        ancestral_villages_or_origin="Every village of Garhwal; essential participants in every ritual, temple awakening, and wedding.",
        notable_historical_figures=["Ustad Karim / Mohan Lal Auji (Master of the 1200 beats of Dhol Sagar)", "Pritam Bhartwan (Padma Shri, Master Jagar singer & Dhol exponent)"],
        cultural_and_historical_notes="Preserve the miraculous oral scripture 'Dhol Sagar' where drumming beats narrate cosmic creation, call gods, and cure curses. Highly revered for their sacred ritual function."
    ),
    "tamta": GarhwaliSurname(
        id="tamta",
        surname_garhwali="तामटा",
        surname_roman="Tamta",
        title="Master Coppersmiths & Sculptors of Divine Idols",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Makers of copper pots (Gagri), musical instruments (Ransingha, Bhankora), and temple umbrellas.",
        gotras=["विश्वकर्मा (Vishwakarma)"],
        ancestral_villages_or_origin="Srinagar, Tehri, Chamoli, and brass-casting centers.",
        notable_historical_figures=["Munshi Hari Prasad Tamta (Pioneer social reformer who fought for equal human rights and coin terms for hill artisans)"],
        cultural_and_historical_notes="Crafted the magnificent copper plates, horns, and sanctum-sanctorum metal sheets across the shrines of Kedarkhand."
    ),
    "dhaki": GarhwaliSurname(
        id="dhaki",
        surname_garhwali="ढकी / ढोली",
        surname_roman="Dhaki / Dholi",
        title="Hereditary Bards of the Royal Courtyard & Wedding Singers",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Singers of auspicious Mangal Geet, awakening chants (Bedako), and court songs.",
        gotras=["नाद-ब्रह्म (Nada-Brahma)"],
        ancestral_villages_or_origin="Settled around Srinagar palace and principal tehsils.",
        notable_historical_figures=["Ramlal Dhaki (Legendary palace court bard)"],
        cultural_and_historical_notes="Vocal keepers of the ancient marriage invocations without which no Garhwali wedding can formally begin."
    ),
    "beda": GarhwaliSurname(
        id="beda",
        surname_garhwali="बेडा",
        surname_roman="Beda",
        title="Acrobatic Folk Heroes of the Sacred Beda-Vart Rope Sliding",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Performers of the daring ancient Beda-Vart (rope-sliding festival) to invoke rains and avert catastrophe.",
        gotras=["महादेव (Mahadeva)"],
        ancestral_villages_or_origin="Specific highland villages of Chamoli and Rudraprayag.",
        notable_historical_figures=["Jeetu Beda (Legendary performer of the sacred Himalayan slide)"],
        cultural_and_historical_notes="In the Beda-Vart ritual, a Beda slides down a thousand-foot steep rope tied between mountain cliffs as an offering for collective village prosperity."
    ),
    "lohar": GarhwaliSurname(
        id="lohar",
        surname_garhwali="लोहार",
        surname_roman="Lohar",
        title="Makers of Traditional Agricultural Implements & Weapons",
        community="Shilpkar / Artisan",
        traditional_title_or_role="Crafting ploughshares (Kutal, Dandiyal), sickles, axes, and swords for Garhwal's defense.",
        gotras=["विश्वकर्मा (Vishwakarma)"],
        ancestral_villages_or_origin="Found in traditional artisan quarters throughout all valley settlements.",
        notable_historical_figures=["Master craftsmen of Chandpurgarh armoury"],
        cultural_and_historical_notes="Vital pillars of agrarian village self-sufficiency in mountain terraced cultivation."
    ),
}

SOCIAL_CONCEPTS_DATA: Dict[str, Dict[str, str]] = {
    "thokdaar": {
        "term_garhwali": "थोकदार",
        "transliteration": "Thokdaar",
        "meaning_english": "Feudal Tax Overseer / Pargana Chief",
        "description": "A hereditary feudal landlord and tax collector under the Rajas of Garhwal who maintained administrative control over a Thok (cluster of villages) and supplied recruits for the royal levies."
    },
    "gauntyaar_sayana": {
        "term_garhwali": "गौंंत्यार / सयाणा",
        "transliteration": "Gauntyaar / Sayana",
        "meaning_english": "Hereditary Village Headman & Elder",
        "description": "The revered head of the village community responsible for settling land boundary disputes, coordinating common pasturage, organizing the annual temple fair, and representing the village before state officers."
    },
    "bhad": {
        "term_garhwali": "भड़",
        "transliteration": "Bhad",
        "meaning_english": "Legendary Epic Warrior / Champion Hero",
        "description": "The title given to invincible champions of Garhwali lore—such as Madho Singh Bhandari, Jeetu Bagdwal, and Rikhola Lodi—whose superhuman courage and military exploits are immortalized in the Pawada oral ballads."
    },
    "jagariya": {
        "term_garhwali": "जगरिया",
        "transliteration": "Jagariya",
        "meaning_english": "Shamanic Balladeer & Spirit Evoker",
        "description": "The ritual priest who recites the genealogies of gods and dead ancestors to the accompaniment of the Hurka or Dhol Damau, singing all night long until the spirit enters the body of the medium."
    },
    "dangariya": {
        "term_garhwali": "डांगरिया",
        "transliteration": "Dangariya",
        "meaning_english": "The Divine Spirit Medium / Deity Vessel",
        "description": "The consecrated villager who goes into trance during a Jagar session, possessed by the deity (such as Golu Dev, Devi, or Nagaraja), delivering oracles, resolving community grievances, and blessing worshippers."
    },
    "dhol_sagar": {
        "term_garhwali": "ढोल सागर",
        "transliteration": "Dhol Sagar",
        "meaning_english": "The Ocean of Percussive Lore & Rhythms",
        "description": "An ancient Garhwali oral treatise on drum science and percussive theology that correlates every rhythm of the Dhol and Damau with a phase of cosmic creation, divine awakening, combat, grief, or bliss."
    },
    "beda_vart": {
        "term_garhwali": "बेडा-वर्त",
        "transliteration": "Beda-Vart",
        "meaning_english": "The Sacred Mountain Rope-Sliding Ceremony",
        "description": "An ancient ritual where a consecrated acrobat glides at terrifying speeds down an enormous grass rope suspended between two mountain cliffs to purge the region of pestilence and famine."
    },
    "jaiti": {
        "term_garhwali": "जैती / पड़ताल",
        "transliteration": "Jaiti / Padtal",
        "meaning_english": "Collective Reciprocal Farming Solidarity",
        "description": "The age-old Garhwali community tradition where all village households assemble together to harvest, weed, or plough one another's terraced fields in turns, accompanied by folk songs and shared meals."
    },
    "dhandak": {
        "term_garhwali": "ढांडक",
        "transliteration": "Dhandak",
        "meaning_english": "Traditional Peasant Non-Cooperation Strike",
        "description": "A historic Garhwali form of nonviolent peasant protest against unjust royal ministers or exorbitant revenue levies, where entire villages abandoned their hamlets and retreated into high forests until the king redressed their grievances."
    }
}


class SurnamesTreasury:
    """Master registry and lookup interface for Garhwali surnames, clans, and social concepts."""

    @classmethod
    def list(cls) -> List[GarhwaliSurname]:
        return list(SURNAMES_DATA.values())

    @classmethod
    def get(cls, surname_id: str) -> Optional[GarhwaliSurname]:
        key = surname_id.strip().lower().replace(" ", "_")
        if key in SURNAMES_DATA:
            return SURNAMES_DATA[key]
        for s in SURNAMES_DATA.values():
            if s.id == key or s.surname_roman.lower() == surname_id.lower() or s.surname_garhwali == surname_id:
                return s
        return None

    @classmethod
    def search(cls, query: str) -> List[GarhwaliSurname]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for s in SURNAMES_DATA.values():
            if (q in s.surname_garhwali.lower() or
                q in s.surname_roman.lower() or
                q in s.community.lower() or
                q in s.title.lower() or
                q in s.ancestral_villages_or_origin.lower() or
                any(q in g.lower() for g in s.gotras) or
                any(q in fig.lower() for fig in s.notable_historical_figures) or
                q in s.cultural_and_historical_notes.lower()):
                results.append(s)
        return results

    @classmethod
    def social_concepts(cls) -> Dict[str, Dict[str, str]]:
        return SOCIAL_CONCEPTS_DATA

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        communities: Dict[str, int] = {}
        for s in SURNAMES_DATA.values():
            communities[s.community] = communities.get(s.community, 0) + 1
        return {
            "total_surnames": len(SURNAMES_DATA),
            "communities": communities,
            "total_social_concepts": len(SOCIAL_CONCEPTS_DATA)
        }
