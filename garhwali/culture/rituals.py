"""
Garhwali temple implements, sacred vessels, hawan paraphernalia, and ritual objects.
Catalogues sacred objects used in Garhwali temples (Dewaal/Mundir), village hearth shrines (Thaan),
shamanic jagars, and daily household pujas.
Based on ethnographic records of Garhwal, Dhol Sagar treatises, and temple traditions of
Kedarnath, Badrinath, Gangotri, Yamunotri, Dhari Devi, and Mahasu Devta.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class GarhwaliRitualItem:
    id: str
    name_garhwali: str
    name_roman: str
    name_hindi: str
    category: str  # "Sacred Mark & Thread", "Vessel & Offering Implement", "Hawan & Fire Sacrifice", "Temple Insignia & Processional", "Jagar & Musical Implement", "Sacred Attire & Ornaments", "Sacred Feast & Food Offering"
    traditional_material: str
    sacred_purpose: str
    cultural_context: str
    associated_deities_or_shrines: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


RITUAL_ITEMS_DATA: Dict[str, GarhwaliRitualItem] = {
    # ==================== SACRED MARKS & THREADS ====================
    "pithya": GarhwaliRitualItem(
        id="pithya",
        name_garhwali="पिठ्याँ / पिठ्या",
        name_roman="Pithya",
        name_hindi="पिठ्या (रोली-हल्दी का तिलक)",
        category="Sacred Mark & Thread",
        traditional_material="Pure mountain turmeric powder mixed with lime water, camphor, and consecrated water, creating luminous red-orange vermilion.",
        sacred_purpose="Vertical sacred tilak drawn with the right ring finger from the bridge of the nose upwards across the center of the forehead.",
        cultural_context="The supreme visual badge of Garhwali blessing and hospitality. No puja, temple pilgrimage, wedding ceremony (Dhuli-argh), or festival begins without elders applying Pithya to family and guests.",
        associated_deities_or_shrines=["Universal across all Garhwal shrines", "Dhari Devi", "Nanda Devi", "Kedarnath"]
    ),
    "akshat": GarhwaliRitualItem(
        id="akshat",
        name_garhwali="अक्षत / चोखा",
        name_roman="Akshat / Chokha",
        name_hindi="अक्षत (अक्षत चावल)",
        category="Sacred Mark & Thread",
        traditional_material="Whole, unbroken white rice grains.",
        sacred_purpose="Pressed into the moist Pithya on the forehead; scattered in blessing over idols, brides, grooms, and sacred altars.",
        cultural_context="Literally 'that which cannot be broken'. Represents wholeness, cosmic fertility, and resilience. In shamanic Jagars, used by the Jagariya in 'Akshat-Parkh' to divine the root of illnesses.",
        associated_deities_or_shrines=["Universal across all rituals", "Jagar rituals", "Badrinath", "Kedarnath"]
    ),
    "dhago_kalawa": GarhwaliRitualItem(
        id="dhago_kalawa",
        name_garhwali="धागो / कलावा / मौली",
        name_roman="Dhago / Kalawa",
        name_hindi="कलावा (रक्षासूत्र)",
        category="Sacred Mark & Thread",
        traditional_material="Unspun sacred cotton thread dyed in bright turmeric yellow and auspicious vermilion red.",
        sacred_purpose="Tied around the right wrist of men and the left wrist of women by priests with mantras of divine shield.",
        cultural_context="Known as 'Raksha Sutra' (thread of protection). Worn continuously to seal spiritual merit and ward off the malevolent gaze (Drishti / Bhoot-Pichash).",
        associated_deities_or_shrines=["Universal across Garhwal temples", "Bhairav Shrines"]
    ),
    "janyo": GarhwaliRitualItem(
        id="janyo",
        name_garhwali="जन्यो / यज्ञोपवीत",
        name_roman="Janyo / Yajnopavita",
        name_hindi="जनेऊ",
        category="Sacred Mark & Thread",
        traditional_material="Three hand-twisted strands of pure cotton thread symbolizing the cosmic Trinity and debts to ancestors, gods, and teachers.",
        sacred_purpose="Invested across the left shoulder diagonally over the torso as an initiation into spiritual duty and learning.",
        cultural_context="Conferred during the 'Janyo-Sanskar'. Consecrated and renewed every year on 'Shravani Purnima / Raksha Bandhan' at holy river prayags (Devprayag, Karnaprayag, Rudraprayag).",
        associated_deities_or_shrines=["Panch Prayag confluences", "Raghunath Temple Devprayag", "Badrinath Dham"]
    ),

    # ==================== VESSELS & OFFERING IMPLEMENTS ====================
    "tamakundi": GarhwaliRitualItem(
        id="tamakundi",
        name_garhwali="तामकुंडी / अर्घा",
        name_roman="Tamakundi / Argha",
        name_hindi="ताम्रकुंडी (अर्घ्य पात्र)",
        category="Vessel & Offering Implement",
        traditional_material="Hand-hammered pure Himalayan copper.",
        sacred_purpose="Vessel used for holding sacred Ganga water to offer libations (Arghya) and bathe holy idols (Abhisheka).",
        cultural_context="Crafted by traditional Tamta coppersmiths; copper is regarded in Garhwali ritual lore as the purest metal that naturally neutralizes toxicity.",
        associated_deities_or_shrines=["Gangotri Dham", "Kedarnath Dham", "Yamunotri Dham"]
    ),
    "dhoopdani": GarhwaliRitualItem(
        id="dhoopdani",
        name_garhwali="धूपदानी / छालाक",
        name_roman="Dhoopdani / Chhalak",
        name_hindi="धूपदानी",
        category="Vessel & Offering Implement",
        traditional_material="Cast bell metal, brass, or copper with decorative perforated lid and handle.",
        sacred_purpose="Holds glowing cowdung coals onto which resin of Sal, aromatic Jatamansi roots, Guggal, and Camphor are offered.",
        cultural_context="The fragrant white smoke sanctifies the inner sanctum and purges negative energy from the village home.",
        associated_deities_or_shrines=["Universal across Garhwal shrines", "Dhari Devi", "Ansuya Devi"]
    ),
    "panchaarti": GarhwaliRitualItem(
        id="panchaarti",
        name_garhwali="पंचारती / आरती",
        name_roman="Panchaarti / Aarti",
        name_hindi="पंचारती",
        category="Vessel & Offering Implement",
        traditional_material="Brass or bell-metal tiered lamp featuring five individual wick-spouts and a central camphor receptacle.",
        sacred_purpose="Circulated clockwise before deities during dawn and dusk worship to manifest divine light.",
        cultural_context="Filled with pure desi cow ghee; the ringing of the Garud-Ghanti and beating of the Dhol accompany the waving of the Panchaarti.",
        associated_deities_or_shrines=["Badrinath Dham", "Kedarnath Dham", "Tungnath"]
    ),
    "shankh": GarhwaliRitualItem(
        id="shankh",
        name_garhwali="शंख",
        name_roman="Shankh",
        name_hindi="शंख",
        category="Vessel & Offering Implement",
        traditional_material="Natural sacred sea conch shell, often mounted with engraved brass or silver filigree.",
        sacred_purpose="Blown at the commencement and conclusion of worship, aartis, and temple openings; used to sprinkle holy water.",
        cultural_context="The reverberating sound of the Shankh awakens the spirit, expels evil entities, and purifies the mountain atmosphere.",
        associated_deities_or_shrines=["Badrinath Dham", "Triyuginarayan", "Srinagar Kamleshwar"]
    ),
    "garud_ghanti": GarhwaliRitualItem(
        id="garud_ghanti",
        name_garhwali="गरुड़-घंटी / घंटी",
        name_roman="Garud-Ghanti",
        name_hindi="घंटी (गरुड़ घंटी)",
        category="Vessel & Offering Implement",
        traditional_material="Ashtadhatu (eight sacred alloys) or resonant bell metal with the image of kneeling Garud carved upon the handle.",
        sacred_purpose="Rung rhythmically in the left hand while waving the ghee lamp in the right hand during temple aarti.",
        cultural_context="Creates high vibrational frequencies that focus the worshipper's mind and invite heavenly celestials into the sanctum.",
        associated_deities_or_shrines=["Badrinath Dham", "Narsingh Temple Joshimath"]
    ),

    # ==================== HAWAN & FIRE SACRIFICE ====================
    "havan_kund": GarhwaliRitualItem(
        id="havan_kund",
        name_garhwali="हवन कुंड",
        name_roman="Havan Kund",
        name_hindi="हवन कुंड",
        category="Hawan & Fire Sacrifice",
        traditional_material="Tiered copper pyramid or stone hearth lined with clay and cowdung wash.",
        sacred_purpose="Conducted for invocations of Agni Devta during household Griha Pravesh, weddings, and annual village pujas.",
        cultural_context="Sacred offerings of barley, sesame, ghee, jaggery, and herbs are poured with chants of 'Swaha'.",
        associated_deities_or_shrines=["Triyuginarayan (Akhand Dhuni)", "Koteshwar Mahadev", "Dhari Devi"]
    ),
    "sruva_sruk": GarhwaliRitualItem(
        id="sruva_sruk",
        name_garhwali="स्रुवा और स्रुक",
        name_roman="Sruva & Sruk",
        name_hindi="स्रुवा-स्रुक (हवन आहुति चम्मच)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Carved wood of sacred Panya (Prunus cerasoides) or Palasha.",
        sacred_purpose="Long-handled ceremonial wooden ladles used by the presiding Brahmin priest to scoop and offer pure ghee into the sacrificial flames.",
        cultural_context="Metal ladles are prohibited in certain ancient Vedic mountain havan rites; only consecrated forest wood is permitted.",
        associated_deities_or_shrines=["Vedic Havan ceremonies across Garhwal", "Upanayana rites"]
    ),
    "samidha": GarhwaliRitualItem(
        id="samidha",
        name_garhwali="समिधा",
        name_roman="Samidha",
        name_hindi="समिधा (हवन की पवित्र लकड़ियाँ)",
        category="Hawan & Fire Sacrifice",
        traditional_material="Dried twigs of Panya (wild cherry), Bel, Peepal, Banjh oak, and Shami.",
        sacred_purpose="Sacred fuels placed in prescribed order in the fire altar to produce medicinal and spiritually uplifting smoke.",
        cultural_context="Collected by family members from pure forest zones without using iron axes.",
        associated_deities_or_shrines=["Universal across Garhwal Havan rituals"]
    ),

    # ==================== TEMPLE INSIGNIA & PROCESSIONAL ====================
    "doli": GarhwaliRitualItem(
        id="doli",
        name_garhwali="डोली / देव-डोली",
        name_roman="Doli / Dev-Doli",
        name_hindi="देव-डोली (देव पालकी)",
        category="Temple Insignia & Processional",
        traditional_material="Carved sacred Deodar or walnut wood frame draped in red silk, brass/silver crests, and floral garlands.",
        sacred_purpose="Carries the metal mask (Mukhauta) and mobile icon of the deity across mountain passes, visiting every village homestead.",
        cultural_context="The living vehicle of the mountain god. Borne on the shoulders of consecrated youth, the doli dances dynamically, tilting, swaying, and stopping miraculously at specific thresholds.",
        associated_deities_or_shrines=["Nanda Devi Doli", "Dhari Devi Doli", "Mahasu Devta Palki", "Surkanda Devi"]
    ),
    "chhantoli": GarhwaliRitualItem(
        id="chhantoli",
        name_garhwali="छंतोली / छत्र",
        name_roman="Chhantoli / Chhatra",
        name_hindi="छंतोली (देव छत्र)",
        category="Temple Insignia & Processional",
        traditional_material="Silver filigree umbrella with red and golden silk frills and sacred bamboo pole.",
        sacred_purpose="Held high over the Dev-Doli and moving deity palanquins during pilgrimages.",
        cultural_context="The ceremonial crown umbrella. The sacred Chhantoli of Nauti village leads the world-famous 280-kilometer Nanda Devi Raj Jat pilgrimage to Homkund.",
        associated_deities_or_shrines=["Nanda Devi Raj Jat", "Nauti Village Shrine", "Hanol Mahasu"]
    ),
    "chaunr": GarhwaliRitualItem(
        id="chaunr",
        name_garhwali="चौंर / चँवर",
        name_roman="Chaunr / Chamara",
        name_hindi="चँवर (सुरागाय के बालों का पंखा)",
        category="Temple Insignia & Processional",
        traditional_material="Silken white tail hair of high Himalayan alpine yak mounted on a hand-carved silver handle.",
        sacred_purpose="Waved gently in slow rhythmic arcs before the sanctum idols during imperial temple services.",
        cultural_context="Symbolizes royal sovereignty and reverence. Procured historically from alpine transhumant traders of Niti and Mana.",
        associated_deities_or_shrines=["Badrinath Dham", "Kedarnath Dham", "Joshimath"]
    ),
    "nishan": GarhwaliRitualItem(
        id="nishan",
        name_garhwali="निशान / देव-ध्वजा",
        name_roman="Nishan",
        name_hindi="निशान (देव ध्वज / त्रिशूल)",
        category="Temple Insignia & Processional",
        traditional_material="Crimson or saffron triangle silk banner mounted with a heavy iron or brass trident (Trishul).",
        sacred_purpose="Carried at the vanguard of deity journeys, fairs, and community defense.",
        cultural_context="Represents the territorial authority of the deity over their mountain realm (Dev-Bhumi).",
        associated_deities_or_shrines=["Bhairavnath", "Kshetrapal", "Nagaraja Sem-Mukhem"]
    ),

    # ==================== JAGAR & MUSICAL IMPLEMENTS ====================
    "dhol": GarhwaliRitualItem(
        id="dhol",
        name_garhwali="ढोल",
        name_roman="Dhol",
        name_hindi="ढोल",
        category="Jagar & Musical Implement",
        traditional_material="Large barrel of resonant cast copper or bell-metal alloy; heads made of goatskin stretched with leather thongs.",
        sacred_purpose="Played by master Auji / Das percussionists to summon ancestors, narrate cosmic origins, and drive spiritual trances.",
        cultural_context="The monarch of mountain instruments. Governed by the ancient oral treatise 'Dhol Sagar'. Every beat (Taal) corresponds to a deity invocation, battle march, or mourning rite.",
        associated_deities_or_shrines=["Universal across all Garhwal shrines", "Jagar sessions", "Panch Kedar"]
    ),
    "damau": GarhwaliRitualItem(
        id="damau",
        name_garhwali="दमाऊँ",
        name_roman="Damau",
        name_hindi="दमाऊँ",
        category="Jagar & Musical Implement",
        traditional_material="Shallow hemisphere bowl of pure hammered copper; covered with thick hide and beaten with thin wooden sticks (Danko).",
        sacred_purpose="Provides the driving bass and syncopated counter-rhythm to the Dhol during rituals, dances, and weddings.",
        cultural_context="Inseparable partner of the Dhol; the pair 'Dhol-Damau' is the musical heart and soul of Garhwali folk life.",
        associated_deities_or_shrines=["Universal across Garhwal villages", "Pandav Nritya", "Mandaan ceremonies"]
    ),
    "ransingha": GarhwaliRitualItem(
        id="ransingha",
        name_garhwali="रणसिंघा",
        name_roman="Ransingha",
        name_hindi="रणसिंघा",
        category="Jagar & Musical Implement",
        traditional_material="Massive curved two-piece S-shaped trumpet crafted of pure hand-beaten sheet copper.",
        sacred_purpose="Blown with powerful lung pressure at pivotal moments of worship, temple openings, and village mobilization.",
        cultural_context="Originally a battle horn sounded from high hill forts; later adopted as a divine herald announcing the arrival of deities.",
        associated_deities_or_shrines=["Kanda Devta", "Dhari Devi", "Nanda Raj Jat", "Mahasu Devta"]
    ),
    "bhankora": GarhwaliRitualItem(
        id="bhankora",
        name_garhwali="भंकोरा",
        name_roman="Bhankora",
        name_hindi="भंकोरा (सीधा तांबे का तुरही)",
        category="Jagar & Musical Implement",
        traditional_material="Long, straight cylindrical trumpet (nearly five feet in length) crafted entirely of shining copper.",
        sacred_purpose="Blown exclusively inside sacred temple precincts; strictly taboo in secular, commercial, or private settings.",
        cultural_context="Produces a deep, unearthly resonant drone that reverberates down mountain gorges, signaling the awakening of divine powers.",
        associated_deities_or_shrines=["Kedarnath Dham", "Rudranath", "Madhyamaheshwar"]
    ),
    "thali_kans": GarhwaliRitualItem(
        id="thali_kans",
        name_garhwali="कांस्य थाली / थाली",
        name_roman="Kansya Thali",
        name_hindi="कांस्य थाली (जगा की थाली)",
        category="Jagar & Musical Implement",
        traditional_material="Heavy plate of resonant bell-metal alloy (Kansa).",
        sacred_purpose="Beaten continuously with a split bamboo rod or wooden wand by the Jagariya while chanting genealogies.",
        cultural_context="Produces hypnotic metallic micro-tones that facilitate the entry of the spirit (Awtar) into the body of the Dangariya medium.",
        associated_deities_or_shrines=["Ghadiala rituals", "Jagar séances", "Bhairav invocations"]
    ),

    # ==================== SACRED ATTIRE & ORNAMENTS ====================
    "tehri_nath": GarhwaliRitualItem(
        id="tehri_nath",
        name_garhwali="टिहरी नथ / नथुली",
        name_roman="Tehri Nath / Nathuli",
        name_hindi="टिहरी नथ (गढ़वाली नथ)",
        category="Sacred Attire & Ornaments",
        traditional_material="Pure 24k gold, weighing between 10 to 40 grams, adorned with intricate filigree peacocks, paisley motifs, and pearl clusters.",
        sacred_purpose="The crowning bridal ornament worn in the left nostril, supported by a delicate gold chain hooked into the hair.",
        cultural_context="The supreme symbol of conjugal blessing (Suhag) and matriarchal dignity in Garhwali culture. Handed down across generations as a prized family heirloom.",
        associated_deities_or_shrines=["Traditional Garhwali weddings", "Devi temples"]
    ),
    "guloband": GarhwaliRitualItem(
        id="guloband",
        name_garhwali="गुलोबंद / गलूबंद",
        name_roman="Guloband",
        name_hindi="गलबंद",
        category="Sacred Attire & Ornaments",
        traditional_material="Square gold plaques etched with floral carvings, securely mounted on a band of crimson or scarlet velvet cloth.",
        sacred_purpose="Worn snugly around the throat by married women during festivals and nuptial ceremonies.",
        cultural_context="A distinctive mountain choker reflecting highland aesthetics and marital status.",
        associated_deities_or_shrines=["Traditional weddings", "Igas Bagwal", "Phool Dei"]
    ),
    "hansuli": GarhwaliRitualItem(
        id="hansuli",
        name_garhwali="हंसुली / खगवाली",
        name_roman="Hansuli / Khagwali",
        name_hindi="हंसुली",
        category="Sacred Attire & Ornaments",
        traditional_material="Solid torque collar of heavy forged sterling silver, thickest at the collarbone center with tapered tips.",
        sacred_purpose="Worn around the neck during folk dances (Jhumelo, Chhori) and weddings.",
        cultural_context="Crafted by village silversmiths; protects the neck and serves as mobile family silver wealth.",
        associated_deities_or_shrines=["Pandav Nritya dancers", "Traditional village celebrations"]
    ),
    "dhagula": GarhwaliRitualItem(
        id="dhagula",
        name_garhwali="धागुला / खांडवे",
        name_roman="Dhagula / Khandwe",
        name_hindi="धागुला (चांदी के कड़े)",
        category="Sacred Attire & Ornaments",
        traditional_material="Solid heavy silver wrist bangles with carved lion-face or serpent-face finials.",
        sacred_purpose="Worn on both wrists by women and small children.",
        cultural_context="Silver conducts cooling energy and is believed in mountain folk medicine to steady the pulse and ward off fear.",
        associated_deities_or_shrines=["Childhood naming ceremonies", "Festivals"]
    ),

    # ==================== SACRED FEASTS & FOOD OFFERINGS ====================
    "rot": GarhwaliRitualItem(
        id="rot",
        name_garhwali="रोट",
        name_roman="Rot",
        name_hindi="रोट (महाप्रसाद)",
        category="Sacred Feast & Food Offering",
        traditional_material="Thick cake of stone-ground whole wheat flour kneaded with warm jaggery syrup, fennel, and desi cow ghee; baked slowly over cowdung embers.",
        sacred_purpose="The principal sacred offering (Bhog) presented to Lord Bhairav, Kshetrapal, and Hanumanji at mountain shrines.",
        cultural_context="After consecration, small portions of the warm, dense Rot are distributed among every household in the village as a talisman of protective health.",
        associated_deities_or_shrines=["Bhairavnath Kedarnath", "Kshetrapal temples", "Ghandiyal Devta"]
    ),
    "arsa": GarhwaliRitualItem(
        id="arsa",
        name_garhwali="अरसा",
        name_roman="Arsa",
        name_hindi="अरसा (पारंपरिक मिठाई)",
        category="Sacred Feast & Food Offering",
        traditional_material="Highland red rice soaked for days, pounded in a traditional wooden mortar (Okhli), mixed into thick jaggery syrup, shaped into discs, and deep-fried in pure mustard oil or ghee.",
        sacred_purpose="The quintessential sweet of Garhwali celebrations, sent as auspicious marriage gifts (Kanya Daan / Dhyanti Bhet).",
        cultural_context="Can be preserved for weeks without spoiling in cool mountain air; handed lovingly to married daughters departing for their in-laws' villages.",
        associated_deities_or_shrines=["Garhwali weddings", "Diwali / Igas Bagwal", "Navratri"]
    ),
    "malu_pattal": GarhwaliRitualItem(
        id="malu_pattal",
        name_garhwali="मालू पत्तल और दूना",
        name_roman="Malu Pattal & Duna",
        name_hindi="मालू के पत्तल-दूने",
        category="Sacred Feast & Food Offering",
        traditional_material="Fresh broad tough leaves of the Malu creeper (Bauhinia vahlii) stitched together with fine bamboo slivers (Tinka).",
        sacred_purpose="Biodegradable dining plates and bowls used for serving community feasts (Dhaam) during village ceremonies.",
        cultural_context="Zero-waste highland hospitality. Leaves impart a delicate herbal aroma to piping hot rice, dal, and kheer.",
        associated_deities_or_shrines=["Universal in community feasts (Dhaam)", "Temple Bhandaras"]
    )
}


class RitualsTreasury:
    """Master registry and query interface for Garhwali temple implements, vessels, and ritual objects."""

    @classmethod
    def list(cls) -> List[GarhwaliRitualItem]:
        return list(RITUAL_ITEMS_DATA.values())

    @classmethod
    def get(cls, id_or_name: str) -> Optional[GarhwaliRitualItem]:
        key = id_or_name.strip().lower().replace(" ", "_")
        if key in RITUAL_ITEMS_DATA:
            return RITUAL_ITEMS_DATA[key]
        for r in RITUAL_ITEMS_DATA.values():
            if (id_or_name in r.name_garhwali or
                key == r.name_roman.lower() or
                key == r.name_hindi.lower()):
                return r
        return None

    @classmethod
    def search(cls, query: str) -> List[GarhwaliRitualItem]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for r in RITUAL_ITEMS_DATA.values():
            if (q in r.name_garhwali.lower() or
                q in r.name_roman.lower() or
                q in r.name_hindi.lower() or
                q in r.category.lower() or
                q in r.traditional_material.lower() or
                q in r.sacred_purpose.lower() or
                q in r.cultural_context.lower() or
                any(q in shrine.lower() for shrine in r.associated_deities_or_shrines)):
                results.append(r)
        return results

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        categories: Dict[str, int] = {}
        for r in RITUAL_ITEMS_DATA.values():
            categories[r.category] = categories.get(r.category, 0) + 1
        return {
            "total_ritual_items": len(RITUAL_ITEMS_DATA),
            "categories": categories,
        }
