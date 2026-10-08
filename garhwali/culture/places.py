# -*- coding: utf-8 -*-
"""
Sacred Geography, Pilgrimage Sites, Alpine Peaks and Historic Places of Garhwal.

Covers 48+ documented cultural, spiritual, historical, and geographical landmarks across
all 7 districts of Garhwal (Chamoli, Rudraprayag, Pauri, Tehri, Uttarkashi, Dehradun, Haridwar):
- Panch Kedar (Kedarnath, Tungnath, Rudranath, Madhyamaheshwar, Kalpeshwar)
- Panch Badri (Badrinath, Adi Badri, Bhavishya Badri, Vriddha Badri, Yogdhyan Badri)
- Panch Prayag (Vishnuprayag, Nandaprayag, Karnaprayag, Rudraprayag, Devprayag)
- Historic towns, fortresses, sacred river confluences, and high alpine meadows (Bugyals)
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class GarhwaliPlace:
    id: str
    name_garhwali: str
    name_roman: str
    title: str
    category: str  # "temple", "peak", "river", "bugyal", "town", "prayag", "historic"
    district: str
    altitude_or_location: str
    spiritual_or_historical_significance: str
    description: str
    associated_deities_or_fairs: List[str]


PLACES_DATA: List[GarhwaliPlace] = [
    # --- CHAMOLI DISTRICT ---
    GarhwaliPlace(
        id="badrinath",
        name_garhwali="बद्रीनाथ",
        name_roman="Badrinath",
        title="श्री बद्रीनाथ धाम (विशाल बद्री)",
        category="temple",
        district="Chamoli",
        altitude_or_location="3,133 m (Alaknanda River valley)",
        spiritual_or_historical_significance="Supreme Char Dham shrine of Lord Vishnu, established by Adi Shankaracharya in the 8th century.",
        description="Enshrined in the Nar-Narayan mountain range alongside Alaknanda river, revered as Badrika Ashram where Lord Vishnu meditated under the wild Badri (ber) berry tree.",
        associated_deities_or_fairs=["बद्री विशाल (Lord Badrinath)", "माता मूर्ति मेला", "कपाट उद्घाटन उत्सव"]
    ),
    GarhwaliPlace(
        id="tungnath",
        name_garhwali="तुंगनाथ",
        name_roman="Tungnath",
        title="तुंगनाथ महादेव (तृतीय केदार)",
        category="temple",
        district="Rudraprayag / Chamoli border",
        altitude_or_location="3,680 m (Highest Shiva temple on Earth, Chandrashila peak)",
        spiritual_or_historical_significance="Highest of the Panch Kedar temples where the arms (बाहु) of Lord Shiva are venerated.",
        description="Perched amidst alpine meadows near Chopta, offering panoramic 360-degree vistas of Nanda Devi, Chaukhamba, and Trishul peaks.",
        associated_deities_or_fairs=["तुंगनाथ शिव (Lord Shiva's Arms)", "चंद्रशिला", "मक्कूमठ शीतकालीन गद्दी"]
    ),
    GarhwaliPlace(
        id="rudranath",
        name_garhwali="रुद्रनाथ",
        name_roman="Rudranath",
        title="रुद्रनाथ महादेव (चतुर्थ केदार)",
        category="temple",
        district="Chamoli",
        altitude_or_location="2,286 m (Deep rhododendron & alpine bugyals)",
        spiritual_or_historical_significance="Panch Kedar shrine where the face (नीलकंठ मुख) of Lord Shiva is worshipped as a natural rock face.",
        description="One of the most arduous pilgrimages in the Himalayas, reached through dense forests of oak and alpine meadows of Pitradhar and Panar.",
        associated_deities_or_fairs=["नीलकंठ मुख शिव", "गोपेश्वर गोपीनाथ", "पितृधार मेला"]
    ),
    GarhwaliPlace(
        id="kalpeshwar",
        name_garhwali="कल्पेश्वर",
        name_roman="Kalpeshwar",
        title="कल्पेश्वर महादेव (पंचम केदार)",
        category="temple",
        district="Chamoli",
        altitude_or_location="2,200 m (Urgam Valley)",
        spiritual_or_historical_significance="Only Panch Kedar temple that remains accessible throughout all twelve months; Shiva's matted hair (जटा) is venerated.",
        description="Located inside a natural rock cave in the scenic Urgam Valley along the Kalpaganga river, renowned for the Kalpavriksha tree legend.",
        associated_deities_or_fairs=["जटाधारी शिव", "उर्गम घाटी मेला", "कल्पगंगा"]
    ),
    GarhwaliPlace(
        id="hemkund_sahib",
        name_garhwali="हेमकुंड साहिब",
        name_roman="Hemkund Sahib",
        title="श्री हेमकुंड साहिब एवं लक्ष्मण लोकपाल मंदिर",
        category="temple",
        district="Chamoli",
        altitude_or_location="4,329 m (Surrounded by seven glacial peaks)",
        spiritual_or_historical_significance="Highest Sikh pilgrimage shrine on Earth where Guru Gobind Singh meditated, adjacent to ancient Lakshman Lokpal temple.",
        description="A pristine high-altitude glacial lake surrounded by seven snow-capped mountain peaks and carpets of rare Brahma Kamal blossoms.",
        associated_deities_or_fairs=["गुरु गोबिंद सिंह", "लक्ष्मण जी (लोकपाल)", "ब्रह्मकमल"]
    ),
    GarhwaliPlace(
        id="valley_of_flowers",
        name_garhwali="फूलों की घाटी",
        name_roman="Phoolon Ki Ghati (Valley of Flowers)",
        title="फूलों की घाटी राष्ट्रीय उद्यान (UNESCO विश्व धरोहर)",
        category="bugyal",
        district="Chamoli",
        altitude_or_location="3,658 m (Pushpawati River valley)",
        spiritual_or_historical_significance="Legendary Gandhamadan mountain from the Ramayana where Hanuman sought Sanjeevani herb; UNESCO World Heritage site.",
        description="Endemic alpine valley blooming with over 500 species of wild Himalayan flora including blue poppies, cobra lilies, and edelweiss.",
        associated_deities_or_fairs=["संजीवनी बूटी", "पुष्पावती नदी", "गंधमादन पर्वत"]
    ),
    GarhwaliPlace(
        id="roopkund",
        name_garhwali="रूपकुंड",
        name_roman="Roopkund",
        title="रूपकुंड (कंकाल झील एवं नंदा राजजात मार्ग)",
        category="lake",
        district="Chamoli",
        altitude_or_location="5,029 m (Base of Trishul massif)",
        spiritual_or_historical_significance="Mystery lake on the sacred Nanda Devi Raj Jat trail containing ancient skeletal remains of pilgrims caught in a celestial hail storm.",
        description="Glacial lake tucked at the base of Trishul peak, venerated during the 12-yearly royal pilgrimage of Goddess Nanda Devi.",
        associated_deities_or_fairs=["नंदा देवी", "लाटू देवता", "नंदा राजजात"]
    ),
    GarhwaliPlace(
        id="joshimath",
        name_garhwali="जोशीमठ",
        name_roman="Joshimath (Jyotirmath)",
        title="ज्योतिर्मठ (आदि शंकराचार्य की उत्तरी पीठ)",
        category="town",
        district="Chamoli",
        altitude_or_location="1,890 m (Alaknanda & Dhauliganga confluence ridge)",
        spiritual_or_historical_significance="Northern cardinal monastic peeth founded by Adi Shankaracharya; winter abode of Lord Badrinath (Narasimha Temple).",
        description="Historic gateway to Badrinath, Hemkund Sahib, and Valley of Flowers, famed for the ancient Kalpavriksha mulberry tree.",
        associated_deities_or_fairs=["नृसिंह देव", "आदि शंकराचार्य ज्योतिर्मठ", "कल्पवृक्ष"]
    ),
    GarhwaliPlace(
        id="auli",
        name_garhwali="औली",
        name_roman="Auli",
        title="औली बुग्याल (शीतकालीन स्कीइंग राजधानी)",
        category="bugyal",
        district="Chamoli",
        altitude_or_location="2,800 m – 3,050 m",
        spiritual_or_historical_significance="Historic high meadow overlooking Nanda Devi, Kamet, and Mana peaks; India's premier snow-sports meadow.",
        description="Lush oak and coniferous meadows transformed into powdery snow fields in winter with the world's highest cable car transit.",
        associated_deities_or_fairs=["नंदा देवी दर्शन", "शीतकालीन स्की उत्सव"]
    ),
    GarhwaliPlace(
        id="gopeshwar",
        name_garhwali="गोपेश्वर",
        name_roman="Gopeshwar",
        title="गोपेश्वर (गोपीनाथ महादेव एवं ऐतिहासिक त्रिशूल)",
        category="town",
        district="Chamoli",
        altitude_or_location="1,550 m (Chamoli District headquarters)",
        spiritual_or_historical_significance="Famous for the ancient 10th-century Gopinath temple and the massive 5-meter un-corroding bronze trident of King Anekamalla.",
        description="Winter seat of Lord Rudranath, renowned as a cradle of the Chipko forest protection movement led by Gaura Devi and Chandi Prasad Bhatt.",
        associated_deities_or_fairs=["गोपीनाथ शिव", "रुद्रनाथ शीतकालीन पूजा", "चिपको आंदोलन"]
    ),
    GarhwaliPlace(
        id="adi_badri",
        name_garhwali="आदि बद्री",
        name_roman="Adi Badri",
        title="आदि बद्री (पंच बद्री समूह एवं प्राचीन मंदिर श्रृंखला)",
        category="temple",
        district="Chamoli",
        altitude_or_location="Karnaprayag-Ranikhet highway",
        spiritual_or_historical_significance="Cluster of 16 ancient stone temples dating back to the Gupta-Katyuri eras; part of the holy Panch Badri circuit.",
        description="Ancient stone temple complex built with pyramidal spires dedicated to Lord Vishnu and surrounding deities.",
        associated_deities_or_fairs=["विष्णु", "पंच बद्री मेला"]
    ),
    GarhwaliPlace(
        id="bhavishya_badri",
        name_garhwali="भविष्य बद्री",
        name_roman="Bhavishya Badri",
        title="भविष्य बद्री (सुभाय गांव - भविष्य का बद्रीनाथ)",
        category="temple",
        district="Chamoli",
        altitude_or_location="2,744 m (Subhai village near Tapovan)",
        spiritual_or_historical_significance="According to prophecy, when the mountains of Jay and Vijay collapse and Badrinath becomes inaccessible, Lord Vishnu will be worshipped here.",
        description="Surrounded by cedar and deodar woods along the Dhauliganga river; an emerging Shivalinga and Vishnu idol are venerated.",
        associated_deities_or_fairs=["भविष्य बद्री", "पंच बद्री"]
    ),
    GarhwaliPlace(
        id="vriddha_badri",
        name_garhwali="वृद्ध बद्री",
        name_roman="Vriddha Badri",
        title="वृद्ध बद्री (अणिमठ - आदि काल का प्रथम बद्री धाम)",
        category="temple",
        district="Chamoli",
        altitude_or_location="1,380 m (Animath village near Joshimath)",
        spiritual_or_historical_significance="Where Lord Vishnu was worshipped by sage Narada as an old man (वृद्ध) prior to the enshrinement of Badrinath Dham.",
        description="Open throughout all twelve months of the year, famous for its ancient stone idol carved out of black Saligram stone.",
        associated_deities_or_fairs=["वृद्ध बद्री", "पंच बद्री"]
    ),
    GarhwaliPlace(
        id="dhyan_badri",
        name_garhwali="ध्यान बद्री",
        name_roman="Dhyan Badri",
        title="ध्यान बद्री (उर्गम घाटी - ध्यानस्थ नारायण)",
        category="temple",
        district="Chamoli",
        altitude_or_location="2,135 m (Urgam Valley near Kalpeshwar)",
        spiritual_or_historical_significance="Where King Urva and Pandavas meditated upon Lord Vishnu; idol depicts the deity in deep Dhyana (meditation) posture.",
        description="Located in the tranquil emerald Urgam valley alongside Kalpeshwar, surrounded by apple and walnut orchards.",
        associated_deities_or_fairs=["ध्यान बद्री", "उर्गम घाटी"]
    ),


    # --- RUDRAPRAYAG DISTRICT ---
    GarhwaliPlace(
        id="kedarnath",
        name_garhwali="केदारनाथ",
        name_roman="Kedarnath",
        title="श्री केदारनाथ ज्योतिर्लिंग (प्रथम केदार)",
        category="temple",
        district="Rudraprayag",
        altitude_or_location="3,583 m (Mandakini River source, Kedar Dome)",
        spiritual_or_historical_significance="Supreme of the 12 Jyotirlingas of Lord Shiva and chief of the Panch Kedar; Pandava redemption shrine.",
        description="Built of massive stone slabs on a glacial moraine below Chaukhamba and Kedar Dome; Shiva venerated as a triangular hump (पृष्ठ भाग).",
        associated_deities_or_fairs=["केदारनाथ ज्योतिर्लिंग", "भैरवनाथ", "उखीमठ शीतकालीन गद्दी", "कपाट उत्सव"]
    ),
    GarhwaliPlace(
        id="madhyamaheshwar",
        name_garhwali="मध्यमहेश्वर",
        name_roman="Madhyamaheshwar (Madmaheshwar)",
        title="द्वितीय केदार मध्यमहेश्वर महादेव",
        category="temple",
        district="Rudraprayag",
        altitude_or_location="3,497 m (Below Chaukhamba peak)",
        spiritual_or_historical_significance="Panch Kedar shrine where the naval (नाभि) of Lord Shiva is worshipped in a classic North Indian Nagara stone sanctum.",
        description="Surrounded by emerald green bugyals, offering staggering views of Chaukhamba; waters of the navel are considered highly sacred.",
        associated_deities_or_fairs=["नाभि शिव", "बुढ़ा मध्यमहेश्वर", "उखीमठ शीतकालीन पूजा"]
    ),
    GarhwaliPlace(
        id="triyuginarayan",
        name_garhwali="त्रियुगीनारायण",
        name_roman="Triyuginarayan",
        title="त्रियुगीनारायण (भगवान शिव एवं पार्वती का विवाह स्थल)",
        category="temple",
        district="Rudraprayag",
        altitude_or_location="1,980 m (Near Sonprayag)",
        spiritual_or_historical_significance="Site of the cosmic wedding of Lord Shiva and Goddess Parvati, witnessed by Lord Vishnu and Lord Brahma.",
        description="Renowned for the Akhand Dhuni (eternal sacred fire) that has burned continuously across three cosmic epochs (Yugas).",
        associated_deities_or_fairs=["अखंड धूनी", "विष्णु-शिव-पार्वती", "त्रियुगीनारायण मेला"]
    ),
    GarhwaliPlace(
        id="ukhimath",
        name_garhwali="उखीमठ",
        name_roman="Ukhimath (Ushamath)",
        title="उखीमठ (ओंकारेश्वर मंदिर - शीतकालीन केदारपीठ)",
        category="town",
        district="Rudraprayag",
        altitude_or_location="1,311 m",
        spiritual_or_historical_significance="Winter seat of Lord Kedarnath and Madhyamaheshwar; venue of the wedding of Usha (daughter of Banasura) and Aniruddha.",
        description="Ancient religious town housing the Rawal (chief priest) of Kedarnath during the sub-zero winter months.",
        associated_deities_or_fairs=["ओंकारेश्वर शिव", "ऊषा-अनिरुद्ध", "केदारनाथ डोली उत्सव"]
    ),
    GarhwaliPlace(
        id="guptkashi",
        name_garhwali="गुप्तकाशी",
        name_roman="Guptkashi",
        title="गुप्तकाशी (विश्वनाथ मंदिर एवं मणिकर्णिका कुंड)",
        category="town",
        district="Rudraprayag",
        altitude_or_location="1,319 m",
        spiritual_or_historical_significance="Sacred pilgrimage center where Lord Shiva briefly hid in the guise of Nandi bull from the Pandavas; equivalent to Kashi.",
        description="Features the ancient Vishwanath stone temple and the Manikarnika Kund where the underground streams of Ganga and Yamuna meet.",
        associated_deities_or_fairs=["विश्वनाथ महादेव", "अर्धनारीश्वर", "मणिकर्णिका कुंड"]
    ),
    GarhwaliPlace(
        id="kalimath",
        name_garhwali="कालीमत",
        name_roman="Kalimath",
        title="कालीमत शक्तिपीठ (माता काली की महाशक्तिपीठ)",
        category="temple",
        district="Rudraprayag",
        altitude_or_location="Saraswati River bank near Guptkashi",
        spiritual_or_historical_significance="Supreme 108 Shaktipeeth where Goddess Kali vanquished demon Raktabija; no idol exists, only the sacred silver Kund is venerated.",
        description="Associated with sage Kalidasa, who according to legend attained poetic genius by worshipping Goddess Kali here.",
        associated_deities_or_fairs=["माता काली", "महाकाली कुंड", "नवरात्रि उत्सव"]
    ),
    GarhwaliPlace(
        id="chopta",
        name_garhwali="चोपता",
        name_roman="Chopta",
        title="चोपता (उत्तराखंड का मिनी स्विट्जरलैंड)",
        category="bugyal",
        district="Rudraprayag",
        altitude_or_location="2,680 m",
        spiritual_or_historical_significance="Base camp for the trek to Tungnath and Chandrashila; surrounded by pristine bugyals and rhododendron forests.",
        description="Pristine alpine meadows covered in snow in winter and ablaze with crimson rhododendrons in spring.",
        associated_deities_or_fairs=["तुंगनाथ यात्रा", "चंद्रशिला शिखर"]
    ),

    # --- PAURI GARHWAL DISTRICT ---
    GarhwaliPlace(
        id="dhari_devi",
        name_garhwali="धारी देवी",
        name_roman="Dhari Devi",
        title="सिद्धपीठ माँ धारी देवी (गढ़वाल की रक्षक अधिष्ठात्री)",
        category="temple",
        district="Pauri Garhwal",
        altitude_or_location="Kalyasaur, on Alaknanda River bank between Srinagar & Rudraprayag",
        spiritual_or_historical_significance="The supreme guardian deity of Uttarakhand and the Char Dham; upper half of Goddess Kali venerated on a rock island.",
        description="The idol miraculously changes countenance from a maiden in the morning to a mature woman at noon and an elder at dusk.",
        associated_deities_or_fairs=["माँ काली / धारी देवी", "चैत्र नवरात्रि मेला", "अलकनंदा"]
    ),
    GarhwaliPlace(
        id="srinagar_garhwal",
        name_garhwali="श्रीनगर गढ़वाल",
        name_roman="Srinagar Garhwal",
        title="श्रीनगर (गढ़वाल राज्य की ऐतिहासिक राजधानी)",
        category="town",
        district="Pauri Garhwal",
        altitude_or_location="560 m (Alaknanda river valley)",
        spiritual_or_historical_significance="Historic seat of the Panwar Kings of Garhwal from 1517 to 1803; center of culture, classical poetry, and learning.",
        description="Home to HNB Garhwal Central University, Kamleshwar Mahadev temple (where Rama offered 108 lotus flowers to Shiva), and Kilkileshwar.",
        associated_deities_or_fairs=["कमलेश्वर महादेव", "किलकिलेश्वर", "बैकुंठ चतुर्दशी मेला"]
    ),
    GarhwaliPlace(
        id="maletha",
        name_garhwali="मलेथा",
        name_roman="Maletha",
        title="मलेथा (वीर माधो सिंह भंडारी की कर्मभूमि)",
        category="historic",
        district="Tehri / Pauri border (Devprayag)",
        altitude_or_location="Alaknanda valley plateau",
        spiritual_or_historical_significance="Site of the miraculous mountain irrigation canal carved out of solid rock by Commander Madho Singh Bhandari in the 17th century.",
        description="Famous for the proverb 'एक बेटा गजे, एक कुलो मलेथे' celebrating Madho Singh's selfless engineering feat to bring canal water to parched fields.",
        associated_deities_or_fairs=["माधो सिंह भंडारी", "मलेथा की गूल", "वीर गाथा मेला"]
    ),
    GarhwaliPlace(
        id="pauri",
        name_garhwali="पौड़ी",
        name_roman="Pauri",
        title="पौड़ी शहर (गढ़वाल मंडल का प्रशासनिक मुख्यालय)",
        category="town",
        district="Pauri Garhwal",
        altitude_or_location="1,814 m (Kandoliya hills)",
        spiritual_or_historical_significance="Seat of the Commissioner of Garhwal Division; offering unbroken vistas of snow-covered Himalayan peaks across 180 degrees.",
        description="Pine-surrounded hill station home to the Kandoliya Devta temple, Kyunkaleshwar Mahadev, and Chaukhamba view point.",
        associated_deities_or_fairs=["कंडोलिया देवता", "कंडोलिया मेला", "क्यूनकालेश्वर"]
    ),
    GarhwaliPlace(
        id="kyunkaleshwar",
        name_garhwali="क्यूनकालेश्वर",
        name_roman="Kyunkaleshwar Mahadev",
        title="क्यूनकालेश्वर महादेव (८वीं सदी का शिव मंदिर)",
        category="temple",
        district="Pauri Garhwal",
        altitude_or_location="Pauri town hillside",
        spiritual_or_historical_significance="8th-century stone temple attributed to Adi Shankaracharya, dedicated to Lord Shiva, Kartikeya, and Ganesha.",
        description="Historic stone architectural marvel overlooking the Alaknanda river valley and the snow-capped Himalayan ridges.",
        associated_deities_or_fairs=["शिव", "महाशिवरात्रि उत्सव"]
    ),
    GarhwaliPlace(
        id="jwalpa_devi",
        name_garhwali="ज्वाल्पा देवी",
        name_roman="Jwalpa Devi",
        title="सिद्धपीठ माँ ज्वाल्पा देवी",
        category="temple",
        district="Pauri Garhwal",
        altitude_or_location="Nawalika (Nayar) river bank near Kotdwar highway",
        spiritual_or_historical_significance="Celebrated Shaktipeeth where Goddess Parvati appeared in blazing form to grant boons; prominent wish-fulfilling shrine of southern Garhwal.",
        description="Nestled by the babbling Nayar river, popular for grand Navratri fairs and wedding blessing vows across the Pauri region.",
        associated_deities_or_fairs=["माँ दुर्गा / ज्वाल्पा", "नवरात्रि मेला", "नवाळिका नदी"]
    ),
    GarhwaliPlace(
        id="kanvashram",
        name_garhwali="कण्वाश्रम",
        name_roman="Kanvashram",
        title="कण्वाश्रम (सम्राट भरत की जन्मस्थली एवं शकुंतला की तपोभूमि)",
        category="historic",
        district="Pauri Garhwal",
        altitude_or_location="Malini river bank near Kotdwar",
        spiritual_or_historical_significance="Ancient hermitage of Sage Kanva where Shakuntala and King Dushyanta met and Emperor Bharat (eponym of India) was born.",
        description="Lush forest ashram situated along the pristine Malini river, immortalized in Kalidasa's Sanskrit classic 'Abhijnanasakuntalam'.",
        associated_deities_or_fairs=["महर्षि कण्व", "सम्राट भरत", "मालिनी नदी", "वसंतोत्सव"]
    ),
    GarhwaliPlace(
        id="khirsu",
        name_garhwali="खिर्सू",
        name_roman="Khirsu",
        title="खिर्सू (बांज-बुराँश के वनों में बसा सुरम्य गांव)",
        category="town",
        district="Pauri Garhwal",
        altitude_or_location="1,760 m",
        spiritual_or_historical_significance="Serene village famed for old apple orchards, thick oak and rhododendron forests, and Ghandiyal Devta temple.",
        description="One of the quietest mountain villages of Garhwal with unobstructed views of Trishul, Nanda Devi, and Chaukhamba.",
        associated_deities_or_fairs=["घंडियाल देवता", "घंडियाल मेला"]
    ),

    # --- TEHRI GARHWAL DISTRICT ---
    GarhwaliPlace(
        id="surkanda_devi",
        name_garhwali="सुरकंडा देवी",
        name_roman="Surkanda Devi",
        title="सिद्धपीठ माँ सुरकंडा देवी शक्तिपीठ",
        category="temple",
        district="Tehri Garhwal",
        altitude_or_location="2,756 m (Near Dhanaulti / Kaddukhal)",
        spiritual_or_historical_significance="One of the 51 Shaktipeeths where the head (शिर) of Goddess Sati fell; supreme protector of Tehri Garhwal.",
        description="Perched upon a lofty cone-shaped summit, offering staggering vistas of the Badrinath, Kedarnath, and Gangotri ranges.",
        associated_deities_or_fairs=["माँ सुरकंडा", "गंगा दशहरा मेला", "कद्दूखाल"]
    ),
    GarhwaliPlace(
        id="chandrabadani",
        name_garhwali="चंद्रबदनी",
        name_roman="Chandrabadani Devi",
        title="सिद्धपीठ माँ चंद्रबदनी शक्तिपीठ",
        category="temple",
        district="Tehri Garhwal",
        altitude_or_location="2,277 m (Chandrabadani peak, near Devprayag)",
        spiritual_or_historical_significance="Major Shaktipeeth where the torso (शरीर भाग) of Goddess Sati fell; priests worship the sacred Sri Yantra cloth without looking directly.",
        description="Towering peak in southern Tehri Garhwal revered for granting boons to barren couples and mountain pilgrims.",
        associated_deities_or_fairs=["माँ चंद्रबदनी", "श्री यंत्र", "नवरात्रि मेला"]
    ),
    GarhwaliPlace(
        id="sem_mukhem",
        name_garhwali="सेम मुखेम",
        name_roman="Sem Mukhem Nagarja",
        title="सेम मुखेम नागराजा (भगवान श्रीकृष्ण नाग स्वरूप)",
        category="temple",
        district="Tehri Garhwal",
        altitude_or_location="2,903 m (Pratapnagar block)",
        spiritual_or_historical_significance="The supreme serpent deity (नागराजा) temple of Garhwal, worshipped as the divine manifestation of Lord Krishna who settled here after Dwarka.",
        description="Hidden in dense oak forests, pilgrims offer raw milk and silver serpent hoods; famed for grand 3-yearly fair (मेला).",
        associated_deities_or_fairs=["श्रीकृष्ण नागराजा", "नागराजा मेला", "मुखेम गांव"]
    ),
    GarhwaliPlace(
        id="kunjapuri",
        name_garhwali="कुंजापुरी",
        name_roman="Kunjapuri Devi",
        title="सिद्धपीठ माँ कुंजापुरी शक्तिपीठ",
        category="temple",
        district="Tehri Garhwal",
        altitude_or_location="1,676 m (Above Rishikesh / Narendra Nagar)",
        spiritual_or_historical_significance="Shaktipeeth where the breast (वक्षस्थल) of Goddess Sati fell; famed for sunrises illuminating both the Himalayan snows and the Ganga plain.",
        description="Ridge-top white marble shrine forming the sacred triangle with Surkanda Devi and Chandrabadani Devi.",
        associated_deities_or_fairs=["माँ कुंजापुरी", "दशहरा मेला", "ऋषिकेश संगम"]
    ),
    GarhwaliPlace(
        id="devprayag",
        name_garhwali="देवप्रयाग",
        name_roman="Devprayag",
        title="देवप्रयाग (भागीरथी एवं अलकनंदा का पवित्र गंगा संगम)",
        category="prayag",
        district="Tehri / Pauri border",
        altitude_or_location="830 m",
        spiritual_or_historical_significance="The foremost of the Panch Prayag where Alaknanda and Bhagirathi merge to officially become the sacred River Ganga.",
        description="Features the ancient 10th-century stone Raghunath Temple dedicated to Lord Rama, and the seat of the Badrinath Panda priests.",
        associated_deities_or_fairs=["रघुनाथ जी (राम)", "गंगा उद्गम", "मकर संक्रांति मेला"]
    ),
    GarhwaliPlace(
        id="khait_parvat",
        name_garhwali="खैत पर्वत",
        name_roman="Khait Parvat",
        title="खैत पर्वत (आंछरियों की परी भूमि)",
        category="peak",
        district="Tehri Garhwal",
        altitude_or_location="3,000 m (Thati Kathur)",
        spiritual_or_historical_significance="Mythical fairy mountain where the seven celestial fairies (आंछरियां) reside, made immortal by the folk ballad of Jeetu Bagdwal.",
        description="A mystical alpine mountain ridge covered in perpetual green grass where flowers bloom throughout the year without withering.",
        associated_deities_or_fairs=["आंछरियां (Fairies)", "जीतू बगड़वाल", "परी मंदिर"]
    ),

    # --- UTTARKASHI DISTRICT ---
    GarhwaliPlace(
        id="gangotri",
        name_garhwali="गंगोत्री",
        name_roman="Gangotri",
        title="श्री गंगोत्री धाम (भागीरथी उद्गम तीर्थ)",
        category="temple",
        district="Uttarkashi",
        altitude_or_location="3,100 m (Bhagirathi river bank)",
        spiritual_or_historical_significance="Prime Char Dham shrine marking where King Bhagiratha's penance brought Goddess Ganga descending from heaven.",
        description="White granite temple built by Gorkha general Amar Singh Thapa; source glacier Gaumukh lies 19 km further up the valley.",
        associated_deities_or_fairs=["माँ गंगा", "भागीरथ शिला", "मुखबा शीतकालीन प्रवास"]
    ),
    GarhwaliPlace(
        id="yamunotri",
        name_garhwali="यमुनोत्री",
        name_roman="Yamunotri",
        title="श्री यमुनोत्री धाम (कालिंदी उद्गम तीर्थ)",
        category="temple",
        district="Uttarkashi",
        altitude_or_location="3,293 m (Bandarpunch mountain foot)",
        spiritual_or_historical_significance="First stop of the Char Dham yatra dedicated to Goddess Yamuna, daughter of the Sun God Surya and sister of Yama.",
        description="Famous for thermal sulfur springs of Surya Kund where pilgrims cook raw rice in cloth bundles as divine prasad.",
        associated_deities_or_fairs=["माँ यमुना", "सूर्य कुंड", "खरसाली शीतकालीन गद्दी"]
    ),
    GarhwaliPlace(
        id="uttarkashi_town",
        name_garhwali="उत्तरकाशी",
        name_roman="Uttarkashi (Saumya Kashi)",
        title="उत्तरकाशी (विश्वनाथ मंदिर एवं शक्ति त्रिशूल)",
        category="town",
        district="Uttarkashi",
        altitude_or_location="1,158 m (Bhagirathi river valley)",
        spiritual_or_historical_significance="Northern Kashi on the banks of Bhagirathi; home to the ancient Vishwanath temple with a massive 26-foot bronze Shakti trident.",
        description="Gateway to Gangotri and Yamunotri, headquarters of the Nehru Institute of Mountaineering (NIM), steeped in ashram culture.",
        associated_deities_or_fairs=["विश्वनाथ शिव", "शक्ति त्रिशूल", "माघ मेला (बाड़ाहाट)"]
    ),
    GarhwaliPlace(
        id="hanol_mahasu",
        name_garhwali="हणोल",
        name_roman="Hanol (Mahasu Devta Temple)",
        title="हणोल महासू देवता मंदिर (जौनसार-बावर एवं रवांई की प्रधान पीठ)",
        category="temple",
        district="Dehradun / Uttarkashi border",
        altitude_or_location="Tons river bank near Mori",
        spiritual_or_historical_significance="Supreme seat of Botha Mahasu (the four Mahasu brother deities); supreme judicial and spiritual center of the tribal hill people.",
        description="9th-century classical stone and timber temple of Katyuri-Nagara architecture, adorned with ancient bronze shields and Mughal coins.",
        associated_deities_or_fairs=["बोथा महासू", "जागड़ा उत्सव", "टोंस नदी"]
    ),
    GarhwaliPlace(
        id="har_ki_dun",
        name_garhwali="हर की दून",
        name_roman="Har Ki Dun",
        title="हर की दून (ईश्वर की घाटी - पांडव स्वर्गारोहण मार्ग)",
        category="valley",
        district="Uttarkashi",
        altitude_or_location="3,566 m (Fateh Parvat / Supin River valley)",
        spiritual_or_historical_significance="Cradle-shaped hanging valley through which the Pandavas ascended to Swargarohini peak; unique shrines honoring Duryodhana and Karna.",
        description="Borderland alpine paradise bordering Himachal Pradesh, famed for wooden Someshwar temples and multi-hued mountain meadows.",
        associated_deities_or_fairs=["सोमेश्वर देवता", "स्वर्गारोहणी", "सुपिन नदी"]
    ),
    GarhwaliPlace(
        id="dayara_bugyal",
        name_garhwali="दयारा बुग्याल",
        name_roman="Dayara Bugyal",
        title="दयारा बुग्याल (बटर फेस्टिवल / अंदूड़ी उत्सव)",
        category="bugyal",
        district="Uttarkashi",
        altitude_or_location="3,408 m (Near Raithal and Barsu villages)",
        spiritual_or_historical_significance="One of the largest alpine meadows in Asia; celebrated for the unique traditional 'Butter Festival' (अंदूड़ी) where villagers play with buttermilk.",
        description="Sprawling across 28 square kilometers with views of Bandarpoonch and Black Peak; emerald in monsoon and powdery white in winter.",
        associated_deities_or_fairs=["अंदूड़ी उत्सव (Butter Festival)", "बंदरपूंछ दर्शन"]
    ),

    # --- THE FIVE SACRED CONFLUENCES (PANCH PRAYAG) ---
    GarhwaliPlace(
        id="vishnuprayag",
        name_garhwali="विष्णुप्रयाग",
        name_roman="Vishnuprayag",
        title="विष्णुप्रयाग (अलकनंदा एवं धौलीगंगा संगम)",
        category="prayag",
        district="Chamoli",
        altitude_or_location="1,372 m (Near Joshimath)",
        spiritual_or_historical_significance="First of the Panch Prayag where the turbulent turquoise Dhauliganga meets the serene Alaknanda river.",
        description="Sage Narada meditated here on Lord Vishnu; features an ancient stone temple and suspension bridge.",
        associated_deities_or_fairs=["विष्णु", "नारद मुनि शिला"]
    ),
    GarhwaliPlace(
        id="nandaprayag",
        name_garhwali="नंदप्रयाग",
        name_roman="Nandaprayag",
        title="नंदप्रयाग (अलकनंदा एवं नंदाकिनी संगम)",
        category="prayag",
        district="Chamoli",
        altitude_or_location="870 m",
        spiritual_or_historical_significance="Second Panch Prayag where the sacred Nandakini (born of Nanda Devi) joins Alaknanda; named after King Nanda (father of Krishna).",
        description="Historic gateway of the Badri-Kedar pilgrimage and former capital of the Yadu royal clan in Garhwal.",
        associated_deities_or_fairs=["गोपाल जी (कृष्ण)", "नंद महाराज", "नंदाकिनी"]
    ),
    GarhwaliPlace(
        id="karnaprayag",
        name_garhwali="कर्णप्रयाग",
        name_roman="Karnaprayag",
        title="कर्णप्रयाग (अलकनंदा एवं पिंडर संगम)",
        category="prayag",
        district="Chamoli",
        altitude_or_location="788 m",
        spiritual_or_historical_significance="Third Panch Prayag where Pindar River (originating from Pindari Glacier) joins Alaknanda; place where Karna meditated on the Sun.",
        description="Where Lord Surya granted the impregnable armor (कवच-कुंडल) to warrior hero Karna; houses the ancient temple of Karna and Goddess Uma.",
        associated_deities_or_fairs=["दानवीर कर्ण", "उमा देवी मंदिर", "पिंडर संगम"]
    ),
    GarhwaliPlace(
        id="rudraprayag_town",
        name_garhwali="रुद्रप्रयाग",
        name_roman="Rudraprayag",
        title="रुद्रप्रयाग (अलकनंदा एवं मंदाकिनी संगम)",
        category="prayag",
        district="Rudraprayag",
        altitude_or_location="610 m",
        spiritual_or_historical_significance="Fourth Panch Prayag where Mandakini (flowing from Kedarnath) merges with Alaknanda; Narada mastered music here through Shiva's grace.",
        description="Historic town flanked by Chamunda Devi and Rudranath temples, division point for the Kedarnath and Badrinath pilgrim routes.",
        associated_deities_or_fairs=["रुद्र (शिव)", "चामुंडा देवी", "नारद शिला"]
    ),

    # --- DEHRADUN & HARIDWAR ---
    GarhwaliPlace(
        id="tapkeshwar",
        name_garhwali="टपकेश्वर",
        name_roman="Tapkeshwar Mahadev",
        title="टपकेश्वर महादेव (गुरु द्रोणाचार्य की गुफा)",
        category="temple",
        district="Dehradun",
        altitude_or_location="Deons river bank, Dehradun",
        spiritual_or_historical_significance="Ancient cave shrine of Lord Shiva where natural spring water drops continuously on the Shivalinga; meditation cave of Guru Dronacharya.",
        description="Birthplace of warrior Ashwatthama, surrounded by sulfur springs and natural forest canopies in Dehradun valley.",
        associated_deities_or_fairs=["टपकेश्वर शिव", "गुरु द्रोणाचार्य", "शिवरात्रि मेला"]
    ),
    GarhwaliPlace(
        id="rishikesh",
        name_garhwali="ऋषिकेश",
        name_roman="Rishikesh",
        title="ऋषिकेश (योग नगरी एवं चारधाम का प्रथम द्वार)",
        category="town",
        district="Dehradun",
        altitude_or_location="372 m (Ganga river valley)",
        spiritual_or_historical_significance="Ancient Tapobhumi where Raibhya Rishi meditated; entry portal to the sacred Garhwal Himalayas and international capital of yoga.",
        description="Famous for Triveni Ghat, Bharat Mandir (oldest shrine founded by Adi Shankaracharya), Laxman Jhula, and Ram Jhula.",
        associated_deities_or_fairs=["हृषीकेश (विष्णु)", "भरत मंदिर", "गंगा आरती"]
    ),
    GarhwaliPlace(
        id="haridwar",
        name_garhwali="हरिद्वार",
        name_roman="Haridwar (Gangadwar)",
        title="हरिद्वार (हर की पौड़ी एवं महाकुंभ नगरी)",
        category="town",
        district="Haridwar",
        altitude_or_location="314 m",
        spiritual_or_historical_significance="Ancient gateway (द्वार) to Hari (Badrinath) and Har (Kedarnath); site where drops of Amrit fell during Samudra Manthan.",
        description="Renowned for Har Ki Pauri Brahmakund, the 12-yearly Maha Kumbh Mela, Mansa Devi, Chandi Devi, and Maya Devi Shaktipeeth.",
        associated_deities_or_fairs=["हर की पौड़ी", "माया देवी", "महाकुंभ मेला", "गंगा सभा"]
    )
]


class PlacesTreasury:
    """Interface to access documented sacred places, temples, and geographical landmarks of Garhwal."""

    @staticmethod
    def list(category: Optional[str] = None, district: Optional[str] = None) -> List[GarhwaliPlace]:
        res = PLACES_DATA
        if category:
            c_low = category.lower().strip()
            res = [p for p in res if p.category.lower() == c_low]
        if district:
            d_low = district.lower().strip()
            res = [p for p in res if d_low in p.district.lower()]
        return res

    @staticmethod
    def get(place_id: str) -> Optional[GarhwaliPlace]:
        p_id = place_id.strip().lower()
        for p in PLACES_DATA:
            if p.id.lower() == p_id or p.name_garhwali == place_id or p.name_roman.lower() == p_id:
                return p
        return None

    @staticmethod
    def panch_kedar() -> List[GarhwaliPlace]:
        """Return the sacred Panch Kedar shrines of Lord Shiva."""
        kedar_ids = {"kedarnath", "tungnath", "rudranath", "madhyamaheshwar", "kalpeshwar"}
        return [p for p in PLACES_DATA if p.id in kedar_ids]

    @staticmethod
    def panch_badri() -> List[GarhwaliPlace]:
        """Return the sacred Panch Badri shrines of Lord Vishnu."""
        badri_ids = {"badrinath", "bhavishya_badri", "vriddha_badri", "dhyan_badri", "adi_badri"}
        return [p for p in PLACES_DATA if p.id in badri_ids]

    @staticmethod
    def panch_prayag() -> List[GarhwaliPlace]:
        """Return the sacred Panch Prayag holy river confluences."""
        return [p for p in PLACES_DATA if p.category == "prayag"]

    @staticmethod
    def search(query: str) -> List[GarhwaliPlace]:
        q = query.lower().strip()
        return [
            p for p in PLACES_DATA
            if q in p.id.lower()
            or q in p.name_garhwali.lower()
            or q in p.name_roman.lower()
            or q in p.title.lower()
            or q in p.district.lower()
            or q in p.spiritual_or_historical_significance.lower()
            or q in p.description.lower()
            or any(q in d.lower() for d in p.associated_deities_or_fairs)
        ]

    @staticmethod
    def categories() -> Dict[str, str]:
        return {
            "temple": "Sacred Temples & Shrines (मंदिर एवं सिद्धपीठ)",
            "prayag": "Sacred River Confluences (पंच प्रयाग)",
            "bugyal": "High Alpine Meadows (बुग्याल)",
            "lake": "High Mountain Glacial Lakes (ताल एवं झील)",
            "peak": "Revered Mountain Peaks (पर्वत शिखर)",
            "town": "Historic Towns & Cultural Centers (नगर एवं पड़ाव)",
            "historic": "Forts & Historical Monuments (गढ़ एवं ऐतिहासिक स्थल)",
            "valley": "Sacred Valleys (घाटियां)"
        }

    @staticmethod
    def stats() -> Dict[str, Any]:
        from collections import Counter
        cat_counts = Counter(p.category for p in PLACES_DATA)
        dist_counts = Counter(p.district for p in PLACES_DATA)
        return {
            "total_places": len(PLACES_DATA),
            "categories": dict(cat_counts),
            "districts": dict(dist_counts),
            "by_category": dict(cat_counts),
            "by_district": dict(dist_counts)
        }

