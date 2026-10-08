"""
Garhwali ethnobotany, sacred Himalayan flora, indigenous trees, medicinal herbs, and wildflowers.
Catalogues sacred trees, oaks, alpine florals, wild fruits, and agricultural crops of Garhwal.
Based on botanical surveys of Chamoli, Tehri, Pauri, Uttarkashi, and Rudraprayag,
along with traditional knowledge documented by Chandi Prasad Bhatt, Sunderlal Bahuguna, and CSIR ethnobotanical reports.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class GarhwaliPlant:
    id: str
    name_garhwali: str
    name_roman: str
    name_hindi: str
    scientific_name: str
    category: str  # "Sacred & Ritual Tree", "Himalayan Forest Tree", "Alpine Flower & Sacred Herb", "Wild Mountain Fruit & Shrub", "Medicinal & Aromatic Flora", "Sacred Grass & Agricultural Flora"
    botanical_family: str
    habitat_altitude: str
    traditional_uses: str
    spiritual_and_temple_significance: str
    cultural_folklore: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


FLORA_DATA: Dict[str, GarhwaliPlant] = {
    # ==================== SACRED & RITUAL TREES ====================
    "banjh": GarhwaliPlant(
        id="banjh",
        name_garhwali="बाँझ",
        name_roman="Banjh",
        name_hindi="बांज (सफेद बांज)",
        scientific_name="Quercus leucotrichophora",
        category="Himalayan Forest Tree",
        botanical_family="Fagaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Nutritious evergreen cattle fodder in winter, humus-rich soil conservation, perpetual spring water aquifer preservation, durable agricultural tool handles.",
        spiritual_and_temple_significance="Revered as the maternal forest goddess ('Banjhyani Devi'). Sacred groves of Banjh shelter village guardian deities (Kshetrapal, Bhumiya, Nagaraja). Green Banjh twigs are planted during Harela and agricultural rituals.",
        cultural_folklore="The spiritual soul of the Chipko Movement. Women of Reni and Mandal sang: 'Banjh raula ta paani raulo, paani raula ta zindagani rauli' (If the oak lives, water lives; if water lives, mountain life endures)."
    ),
    "moru": GarhwaliPlant(
        id="moru",
        name_garhwali="मोरू",
        name_roman="Moru",
        name_hindi="मोरू बांज",
        scientific_name="Quercus floribunda",
        category="Himalayan Forest Tree",
        botanical_family="Fagaceae",
        habitat_altitude="2,000m – 2,800m",
        traditional_uses="Hard timber for village door lintels, dense charcoal, premium winter leaf fodder for sheep and cows.",
        spiritual_and_temple_significance="Associated with high-altitude shrines of Kshetrapal and local village protectors in upper Chamoli and Rudraprayag.",
        cultural_folklore="Known as the elder brother of the Banjh oak tree, praised for standing firm under severe snow blizzards."
    ),
    "kharsu": GarhwaliPlant(
        id="kharsu",
        name_garhwali="खर्सू",
        name_roman="Kharsu",
        name_hindi="खर्सू बांज (भूरा बांज)",
        scientific_name="Quercus semecarpifolia",
        category="Himalayan Forest Tree",
        botanical_family="Fagaceae",
        habitat_altitude="2,400m – 3,500m",
        traditional_uses="Upper sub-alpine protection, critical summer shelter and fodder for transhumant Anwal shepherds.",
        spiritual_and_temple_significance="Marks the boundary of the subalpine sacred bugyals. Associated with Lord Shiva's hermitage at Tungnath and Madhyamaheshwar.",
        cultural_folklore="Celebrated as the eternal timber that watches over the high shepherd routes of Kedarkhand."
    ),
    "buransh": GarhwaliPlant(
        id="buransh",
        name_garhwali="बुरांश / बुरांस",
        name_roman="Buransh",
        name_hindi="बुरांश",
        scientific_name="Rhododendron arboreum",
        category="Sacred & Ritual Tree",
        botanical_family="Ericaceae",
        habitat_altitude="1,500m – 3,000m",
        traditional_uses="Fresh crimson petals pressed into mountain squash and sharbat; cardiovascular tonic; anti-inflammatory honey flora.",
        spiritual_and_temple_significance="State Tree of Uttarakhand. Blossoms offered directly to Lord Shiva at Kedarnath and Tungnath, and to Goddess Nanda Devi during springtime Chaiti celebrations.",
        cultural_folklore="Heralds the arrival of spring across the ridges. Garhwali poets sing: 'Buransh phooli ge danda-kandyon ma' (The hills have ignited with the crimson fire of Buransh flowers)."
    ),
    "simru": GarhwaliPlant(
        id="simru",
        name_garhwali="सिमरू / सिमड़ू",
        name_roman="Simru",
        name_hindi="सफेद बुरांश",
        scientific_name="Rhododendron campanulatum",
        category="Sacred & Ritual Tree",
        botanical_family="Ericaceae",
        habitat_altitude="3,000m – 4,000m",
        traditional_uses="Subalpine dwarf shrub protecting soil on slopes above the treeline.",
        spiritual_and_temple_significance="Bell-shaped lilac and white blossoms offered at alpine shrines of Nanda Devi and Trishul.",
        cultural_folklore="Marks the transition from tall forests into the mystical world of Bugyals (alpine meadows)."
    ),
    "deodar": GarhwaliPlant(
        id="deodar",
        name_garhwali="देवदार",
        name_roman="Deodar",
        name_hindi="देवदार",
        scientific_name="Cedrus deodara",
        category="Sacred & Ritual Tree",
        botanical_family="Pinaceae",
        habitat_altitude="1,800m – 3,000m",
        traditional_uses="Imperishable aromatic timber for sanctum temple architecture; insect-repellent wood; cedar oil for skin ailments.",
        spiritual_and_temple_significance="Sanskrit 'Devadaru' (Divine Timber). The ancient temples of Mahasu Devta at Hanol and Triyuginarayan stand within Deodar canopies. Regarded as Shiva's sacred forest.",
        cultural_folklore="Believed to be inhabited by mountain rishis. Felling live deodars in temple groves is traditionally forbidden by ancient community taboos."
    ),
    "chir": GarhwaliPlant(
        id="chir",
        name_garhwali="चीड़ / सल्ला",
        name_roman="Chir / Salla",
        name_hindi="चीड़",
        scientific_name="Pinus roxburghii",
        category="Himalayan Forest Tree",
        botanical_family="Pinaceae",
        habitat_altitude="800m – 2,000m",
        traditional_uses="Needles (Pirul) collected for cattle bedding and compost; resin (Lisha) tapped for turpentine; wood used in hill construction.",
        spiritual_and_temple_significance="Resinous heartwood chips (Chhiluka) lit as sacred ceremonial torches in temple night processions and Jagars.",
        cultural_folklore="The scent of pine needles fills every Garhwali ridge. Salla wood crackles in winter hearths (Ghyar) across Pauri and Tehri."
    ),
    "kail": GarhwaliPlant(
        id="kail",
        name_garhwali="कैल",
        name_roman="Kail",
        name_hindi="नीली चीड़",
        scientific_name="Pinus wallichiana",
        category="Himalayan Forest Tree",
        botanical_family="Pinaceae",
        habitat_altitude="2,000m – 3,200m",
        traditional_uses="High-grade carpentry timber, fragrant resin, and building beams.",
        spiritual_and_temple_significance="Grows on the heights above Joshimath, Badrinath valley, and Gangotri.",
        cultural_folklore="Resilient high-altitude pine standing tall amidst heavy winter snowfalls."
    ),
    "bhojpatra": GarhwaliPlant(
        id="bhojpatra",
        name_garhwali="भोजपत्र",
        name_roman="Bhojpatra",
        name_hindi="भोजपत्र",
        scientific_name="Betula utilis",
        category="Sacred & Ritual Tree",
        botanical_family="Betulaceae",
        habitat_altitude="3,000m – 4,200m",
        traditional_uses="Peeled bark used for sacred manuscripts, protective charms (Yantras), wrapping butter in alpine weather.",
        spiritual_and_temple_significance="Ancient Himalayan manuscripts, Vedas, and Tantric texts were written on Bhojpatra bark. Sacred trees at Bhojbasa on the trail to Gaumukh.",
        cultural_folklore="Considered the sacred paper of the Rishis. Pilgrims carrying water from Gaumukh historically wrap the holy vessel in Bhojpatra bark."
    ),
    "panya": GarhwaliPlant(
        id="panya",
        name_garhwali="पंया / पैयाँ",
        name_roman="Panya / Paiyan",
        name_hindi="पद्मकाष्ठ (पद्म)",
        scientific_name="Prunus cerasoides",
        category="Sacred & Ritual Tree",
        botanical_family="Rosaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Autumn-blooming Himalayan wild cherry; wood used for sacred havan and sacrificial ladles; medicinal bark.",
        spiritual_and_temple_significance="Most sacred sacrificial wood (Samidha) used in Garhwali Havan rituals and house consecrations (Griha Pravesh). No holy ritual is complete without Paiyan wood.",
        cultural_folklore="Known as the tree that blossoms when all other trees shed their leaves in late autumn, signaling the coming winter peace."
    ),
    "bhimal": GarhwaliPlant(
        id="bhimal",
        name_garhwali="भीमल",
        name_roman="Bhimal",
        name_hindi="भीमल",
        scientific_name="Grewia optiva",
        category="Himalayan Forest Tree",
        botanical_family="Malvaceae",
        habitat_altitude="800m – 1,800m",
        traditional_uses="Superb winter cattle fodder; bark soaked in river streams yields strong fibers (Selu) braided into mountain ropes; bark pulp used as natural herbal shampoo.",
        spiritual_and_temple_significance="The sacred fibers are braided into ceremonial cords used in temple installations.",
        cultural_folklore="The lifeline tree planted directly on field terrace edges by mountain farmers to sustain cattle during barren winter months."
    ),
    "kharik": GarhwaliPlant(
        id="kharik",
        name_garhwali="खरिक / खिकरी",
        name_roman="Kharik / Khikri",
        name_hindi="खरक",
        scientific_name="Celtis australis",
        category="Himalayan Forest Tree",
        botanical_family="Cannabaceae",
        habitat_altitude="1,000m – 2,200m",
        traditional_uses="Nutritious fodder, durable timber for agricultural tool handles and mountain ploughs, sweet small edible berries.",
        spiritual_and_temple_significance="Planted near village public squares (Chauk) for cool shade during village panchayat assemblies.",
        cultural_folklore="The shade of the ancient Kharik tree is where village elders historically gathered to resolve boundary disputes."
    ),
    "utis": GarhwaliPlant(
        id="utis",
        name_garhwali="उतीस",
        name_roman="Utis",
        name_hindi="उतीस",
        scientific_name="Alnus nepalensis",
        category="Himalayan Forest Tree",
        botanical_family="Betulaceae",
        habitat_altitude="1,000m – 2,500m",
        traditional_uses="Fast-growing pioneer tree that fixes atmospheric nitrogen, stabilizing landslide-prone mountain slopes; light timber for boxes.",
        spiritual_and_temple_significance="Regarded as the earth-healer tree that covers bare wounded landslide hillsides with green life.",
        cultural_folklore="Known as the first tree to arrive and protect a slope after a cloudburst washes away soil."
    ),
    "timru": GarhwaliPlant(
        id="timru",
        name_garhwali="तिमरू / तिमूर",
        name_roman="Timru / Timur",
        name_hindi="तिमरू",
        scientific_name="Zanthoxylum armatum",
        category="Medicinal & Aromatic Flora",
        botanical_family="Rutaceae",
        habitat_altitude="1,000m – 2,400m",
        traditional_uses="Thorny aromatic twigs used as dental cleanser (Datun) curing toothaches; pungent seed pericarps used as zesty spice; walking sticks carved from wood to ward off wild animals.",
        spiritual_and_temple_significance="Extremely sacred ritual plant; thorny branches kept at home thresholds to repel malevolent ghosts and evil spirits. Dedicated to Lord Shiva.",
        cultural_folklore="No Garhwali traveler ventured into lonely mountain passes without a sturdy Timru walking stick (Timru ki Laathi), said to keep both venomous snakes and spirits away."
    ),
    "bel": GarhwaliPlant(
        id="bel",
        name_garhwali="बेल / बिल्व",
        name_roman="Bel / Bilva",
        name_hindi="बेल",
        scientific_name="Aegle marmelos",
        category="Sacred & Ritual Tree",
        botanical_family="Rutaceae",
        habitat_altitude="300m – 1,200m",
        traditional_uses="Fruit pulp digestive remedy for stomach disorders; cooling summer sharbat.",
        spiritual_and_temple_significance="Trifoliate leaves represent Shiva's Trishul and are offered without fail at Kedarnath, Tungnath, and Rudranath temples.",
        cultural_folklore="Revered in the Shiva-Purana; planting a Bel tree near one's homestead is believed to bestow auspicious blessings."
    ),
    "malu": GarhwaliPlant(
        id="malu",
        name_garhwali="मालू",
        name_roman="Malu",
        name_hindi="मालू",
        scientific_name="Bauhinia vahlii",
        category="Himalayan Forest Tree",
        botanical_family="Fabaceae",
        habitat_altitude="400m – 1,500m",
        traditional_uses="Gigantic mountain creeper; broad tough leaves stitched with bamboo slivers into traditional bio-plates (Pattal) and bowls (Duna); seeds roasted and eaten.",
        spiritual_and_temple_significance="Pattals made of Malu leaves are mandatory for serving sacred community feasts (Dham) during Garhwali weddings and religious pujas.",
        cultural_folklore="Symbolizes generous mountain abundance, spreading vast green canopies across lower river valleys."
    ),

    # ==================== ALPINE FLOWERS & SACRED HERBS ====================
    "brahma_kamal": GarhwaliPlant(
        id="brahma_kamal",
        name_garhwali="ब्रह्मकमल / कौल",
        name_roman="Brahma Kamal",
        name_hindi="ब्रह्मकमल",
        scientific_name="Saussurea obvallata",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="3,700m – 4,800m",
        traditional_uses="Medicinal plant used in Tibetan and Ayurvedic healing for bone aches and urinary disorders.",
        spiritual_and_temple_significance="State Flower of Uttarakhand. The most sacred flower in the Himalayas, blooming only between July and September around Roopkund, Hemkund Sahib, and Valley of Flowers. Offered directly to Lord Kedarnath and Lord Badrinath.",
        cultural_folklore="According to the Mahabharata, Draupadi was enchanted by its ethereal fragrance in the high hills. It is reverently plucked on Nandashtami to present at the feet of Maa Nanda Devi."
    ),
    "fen_kamal": GarhwaliPlant(
        id="fen_kamal",
        name_garhwali="फेनकमल",
        name_roman="Fen Kamal",
        name_hindi="फेनकमल",
        scientific_name="Saussurea simpsoniana",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="4,200m – 5,500m",
        traditional_uses="High-altitude woolly alpine herb protected by dense white fuzz against sub-zero blizzards.",
        spiritual_and_temple_significance="Offered at the highest alpine shrines along the Nanda Devi Raj Jat route at Homkund and Roopkund.",
        cultural_folklore="Regarded as the ascetic lotus meditating under freezing winds on the eternal snowfields."
    ),
    "jatamansi": GarhwaliPlant(
        id="jatamansi",
        name_garhwali="जटामांसी / बालछड़",
        name_roman="Jatamansi",
        name_hindi="जटामांसी",
        scientific_name="Nardostachys jatamansi",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Caprifoliaceae",
        habitat_altitude="3,300m – 4,800m",
        traditional_uses="Aromatic rhizomes used in Ayurvedic nervine tonics, memory enhancement, and precious incense formulation.",
        spiritual_and_temple_significance="Primary sacred aromatic ingredient in temple Dhoop burnt before the deities at Kedarnath and Badrinath.",
        cultural_folklore="Named after the matted locks (Jata) of Lord Shiva, filling high alpine cliffs with divine fragrance."
    ),
    "koot": GarhwaliPlant(
        id="koot",
        name_garhwali="कूट",
        name_roman="Koot",
        name_hindi="कुष्ठ",
        scientific_name="Saussurea costus",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Asteraceae",
        habitat_altitude="2,800m – 3,800m",
        traditional_uses="Valuable medicinal roots used for respiratory disorders and high-grade incense.",
        spiritual_and_temple_significance="Burned in havan samagri at high-altitude shrines of Garhwal.",
        cultural_folklore="Cultivated historically by alpine villagers of Painkhanda and Chamoli as a prized trade commodity."
    ),
    "atees": GarhwaliPlant(
        id="atees",
        name_garhwali="अतीस",
        name_roman="Atees",
        name_hindi="अतीस",
        scientific_name="Aconitum heterophyllum",
        category="Medicinal & Aromatic Flora",
        botanical_family="Ranunculaceae",
        habitat_altitude="2,500m – 4,000m",
        traditional_uses="Non-toxic medicinal aconite root used for fevers, diarrhea, and pediatric gastrointestinal remedies.",
        spiritual_and_temple_significance="Known as the divine plant doctor of the high Himalaya.",
        cultural_folklore="Collected with strict ritual purity by mountain Anwals and vaidyas."
    ),
    "meetha_bikh": GarhwaliPlant(
        id="meetha_bikh",
        name_garhwali="मीठा-बिख / महूर",
        name_roman="Meetha-Bikh",
        name_hindi="मीठा विष",
        scientific_name="Aconitum balfourii",
        category="Medicinal & Aromatic Flora",
        botanical_family="Ranunculaceae",
        habitat_altitude="3,000m – 4,300m",
        traditional_uses="Potent root used after rigorous purification (Shodhana) in specialized Ayurvedic treatments for neuralgic pain.",
        spiritual_and_temple_significance="Associated with Shiva's consumption of Halahala poison at Neelkanth Mahadev.",
        cultural_folklore="Historically used by Garhwali hunters to poison arrow tips against dangerous wild beasts."
    ),
    "salam_panja": GarhwaliPlant(
        id="salam_panja",
        name_garhwali="सलामपंजा / हथजड़ी",
        name_roman="Salam Panja / Hathjadi",
        name_hindi="सलामपंजा",
        scientific_name="Dactylorhiza hatagirea",
        category="Alpine Flower & Sacred Herb",
        botanical_family="Orchidaceae",
        habitat_altitude="2,800m – 4,200m",
        traditional_uses="Hand-shaped tuberous orchid root revered as a powerful rejuvenating adaptogen and tonic.",
        spiritual_and_temple_significance="The root resembles a sacred open palm blessing devotees, considered a symbol of divine protection.",
        cultural_folklore="Subject to strict conservation protection due to heavy harvesting in high alpine meadows."
    ),
    "keedajadi": GarhwaliPlant(
        id="keedajadi",
        name_garhwali="कीड़ाजड़ी / यार्त्सा गुन्बू",
        name_roman="Keedajadi / Yartsa Gunbu",
        name_hindi="कीड़ाजड़ी",
        scientific_name="Ophiocordyceps sinensis",
        category="Medicinal & Aromatic Flora",
        botanical_family="Ophiocordycipitaceae",
        habitat_altitude="3,500m – 5,000m",
        traditional_uses="Rare fungal-insect entheogen harvested in May-June in high meadows of Chamoli and Pithoragarh; world-renowned vitality tonic.",
        spiritual_and_temple_significance="Regarded as the mystical miraculous gift of the high snow peaks.",
        cultural_folklore="Entire alpine villages migrate to Bugyals each summer to carefully spot these precious stalks emerging through the melting snow."
    ),

    # ==================== WILD MOUNTAIN FRUITS & SHRUBS ====================
    "kafal": GarhwaliPlant(
        id="kafal",
        name_garhwali="काफल",
        name_roman="Kafal",
        name_hindi="काफल",
        scientific_name="Myrica esculenta",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Myricaceae",
        habitat_altitude="1,300m – 2,100m",
        traditional_uses="Succulent crimson wild berry with sweet-tart taste, sprinkled with rock salt and chili; astringent bark used in traditional dentistry and dyeing.",
        spiritual_and_temple_significance="Offered at village deity shrines during the month of Baisakh.",
        cultural_folklore="Immortalized in the poignant Garhwali legend of the mother, the child, and the song of the Kafal bird: 'Kafal pakko, mil ni chakho' (The berries ripened, but I tasted none!). Celebrated in Chandrakunwar Bartwal's timeless poems."
    ),
    "hisalu": GarhwaliPlant(
        id="hisalu",
        name_garhwali="हिसालू / हिंसोल",
        name_roman="Hisalu / Hinsol",
        name_hindi="हिसालू",
        scientific_name="Rubus ellipticus",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Rosaceae",
        habitat_altitude="1,000m – 2,200m",
        traditional_uses="Golden mountain raspberry; highly prized sweet summer wild fruit; rich in antioxidants and vitamin C; roots used in stomach ailments.",
        spiritual_and_temple_significance="Wild thorny bushes shelter sacred boundary shrines.",
        cultural_folklore="Beloved summer fruit of Garhwali village children who graze cows upon the hill slopes."
    ),
    "kilmora": GarhwaliPlant(
        id="kilmora",
        name_garhwali="किल्मोड़ा / किंगोड़",
        name_roman="Kilmora / Kingod",
        name_hindi="दारूहल्दी",
        scientific_name="Berberis aristata",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Berberidaceae",
        habitat_altitude="1,400m – 2,800m",
        traditional_uses="Yellow root (Daru-haldi) contains potent berberine, used as cure for jaundice, eye infections, and skin disorders; purple berries eaten.",
        spiritual_and_temple_significance="Yellow herbal paste used in ritual Tilak at mountain shrines.",
        cultural_folklore="Famous hill remedy: washing infected eyes with water soaked in Kilmora bark brings instant relief."
    ),
    "bedu": GarhwaliPlant(
        id="bedu",
        name_garhwali="बेडू",
        name_roman="Bedu",
        name_hindi="जंगली अंजीर",
        scientific_name="Ficus palmata",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Moraceae",
        habitat_altitude="600m – 2,000m",
        traditional_uses="Wild Himalayan fig; sweet ripe fruits eaten; green raw figs cooked into spicy mountain subji; digestive fruit.",
        spiritual_and_temple_significance="Regarded as an auspicious wild tree providing sweet sustenance.",
        cultural_folklore=" immortalized across the world in the iconic Himalayan anthem: 'Bedu pako baramasa, narani kafal pako chaita' (The Bedu fruit ripens all twelve months, O maiden, while Kafal ripens in Chaitra)."
    ),
    "timla": GarhwaliPlant(
        id="timla",
        name_garhwali="तिमला / तिमुल",
        name_roman="Timla / Timul",
        name_hindi="तिमला",
        scientific_name="Ficus auriculata",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Moraceae",
        habitat_altitude="800m – 1,800m",
        traditional_uses="Broad saucer leaves used for making disposable eating plates; large figs cooked as subji and jam; rich fodder for milch cows.",
        spiritual_and_temple_significance="Used in outdoor community feasts and temple Annakut rituals.",
        cultural_folklore="A cornerstone of traditional zero-waste mountain banquet hospitality."
    ),
    "kandali": GarhwaliPlant(
        id="kandali",
        name_garhwali="कंडाली / सिंसोण",
        name_roman="Kandali / Sinson",
        name_hindi="बिच्छू घास",
        scientific_name="Urtica dioica",
        category="Medicinal & Aromatic Flora",
        botanical_family="Urticaceae",
        habitat_altitude="1,000m – 3,000m",
        traditional_uses="Tender young leaves boiled and mashed into the iconic nourishing winter dish 'Kapha / Kafuli'; rich in iron, minerals, and joint-pain remedies.",
        spiritual_and_temple_significance="Used in folk disciplinary rituals and the historic Kandali festival in Pithoragarh and Chamoli celebrating victory over invaders.",
        cultural_folklore="Every Garhwali child remembers the fiery sting of Kandali, immediately cured by rubbing leaves of Palak or cold water."
    ),
    "linguda": GarhwaliPlant(
        id="linguda",
        name_garhwali="लिंगुड़ा / लिंगुड़",
        name_roman="Linguda / Lingud",
        name_hindi="ढेकिया साग (फर्न)",
        scientific_name="Diplazium esculentum",
        category="Wild Mountain Fruit & Shrub",
        botanical_family="Athyriaceae",
        habitat_altitude="1,200m – 2,400m",
        traditional_uses="Tender coiled fiddlehead ferns harvested from forest streams during monsoon; cooked with mustard oil and Jakhya seeds as a seasonal delicacy.",
        spiritual_and_temple_significance="Pure wild food collected from pristine mountain brooks.",
        cultural_folklore="A monsoon delicacy eagerly awaited across Garhwal as mountain streams swell with fresh rain."
    ),

    # ==================== SACRED AGRICULTURAL CROPS & GRAINS ====================
    "manduwa": GarhwaliPlant(
        id="manduwa",
        name_garhwali="मंडुवा / कोदा",
        name_roman="Manduwa / Koda",
        name_hindi="मंडुवा (रागी)",
        scientific_name="Eleusine coracana",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="1,000m – 2,400m",
        traditional_uses="Staple calcium- and iron-rich finger millet of Uttarakhand; kneaded into hot rotis eaten with Ghee and Gur; fermented into traditional brew; therapeutic for diabetes.",
        spiritual_and_temple_significance="The core sustenance of the hill people, offered with gratitude to Bhumiya Devta during harvest festivals.",
        cultural_folklore="Celebrated as the resilient crop that never fails even in severe mountain droughts, providing iron strength to Garhwali farmers."
    ),
    "jhangora": GarhwaliPlant(
        id="jhangora",
        name_garhwali="झंगोरा",
        name_roman="Jhangora",
        name_hindi="सांवा (झंगोरा)",
        scientific_name="Echinochloa frumentacea",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Poaceae",
        habitat_altitude="1,000m – 2,200m",
        traditional_uses="Barnyard millet boiled as light fluffy rice (Bhaat) or simmered with milk into festive Jhangore ki Kheer; fast-digesting and highly nutritious.",
        spiritual_and_temple_significance="Pure unpolished grain eaten during religious fasts (Vrats) and Navratri.",
        cultural_folklore="A guest in a Garhwali home is greeted with warm hospitality of steaming Jhangora bhaat and hot Gahat ki daal."
    ),
    "marsa": GarhwaliPlant(
        id="marsa",
        name_garhwali="मर्सा / चूआ",
        name_roman="Marsa / Chooa",
        name_hindi="रामदाना",
        scientific_name="Amaranthus cruentus",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Amaranthaceae",
        habitat_altitude="1,200m – 2,600m",
        traditional_uses="Crimson grain popped into crispy Ramdana laddoos; leaves cooked as green saag; grain consumed during fasts.",
        spiritual_and_temple_significance="Sacred Phalahari grain offered to deities during Navratri fasts.",
        cultural_folklore="In autumn, the terraces of upper Garhwal glow with vibrant red and golden fields of Marsa, creating a breathtaking tapestry."
    ),
    "ugal": GarhwaliPlant(
        id="ugal",
        name_garhwali="उगल / फाफर",
        name_roman="Ugal / Phaphar",
        name_hindi="कुट्टू (फाफर)",
        scientific_name="Fagopyrum esculentum",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Polygonaceae",
        habitat_altitude="1,800m – 3,500m",
        traditional_uses="Buckwheat flour made into puris and rotis during religious fasts; leaves eaten as greens.",
        spiritual_and_temple_significance="Permissible food during strict Hindu fasting periods; staple crop of high Chamoli and Uttarkashi valleys.",
        cultural_folklore="A high-altitude mountain crop that flourishes where paddy cannot grow."
    ),
    "gahat": GarhwaliPlant(
        id="gahat",
        name_garhwali="गहत / कुल्थी",
        name_roman="Gahat / Kulthi",
        name_hindi="कुलथी",
        scientific_name="Macrotyloma uniflorum",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Fabaceae",
        habitat_altitude="800m – 2,000m",
        traditional_uses="Horsegram pulse boiled into warming winter soup (Ghatwani / Ras) and stuffed in breads (Gahat ke Fande / Paranthe); world-famous natural solvent for kidney stones.",
        spiritual_and_temple_significance="Consumed during winter to provide inner thermal warmth to the body.",
        cultural_folklore="Regarded as the medicine-food of the hills: a bowl of piping hot Gahat soup with a spoonful of hill desi ghee dispels the bitterest Himalayan cold."
    ),
    "bhatt": GarhwaliPlant(
        id="bhatt",
        name_garhwali="काली भट",
        name_roman="Bhatt (Kali Bhatt)",
        name_hindi="काली सोयाबीन",
        scientific_name="Glycine soja",
        category="Sacred Grass & Agricultural Flora",
        botanical_family="Fabaceae",
        habitat_altitude="1,000m – 2,200m",
        traditional_uses="Indigenous black soybean; dry-roasted and ground into the signature Garhwali dish 'Bhatwani / Churdkani' cooked in iron pans; extremely protein-rich.",
        spiritual_and_temple_significance="Staple agrarian legume of the Central Himalaya.",
        cultural_folklore="Iron wok cooked Bhatt turns into a velvety dark curry that builds the sturdy mountain constitution."
    ),
    "jakhya": GarhwaliPlant(
        id="jakhya",
        name_garhwali="जख्या",
        name_roman="Jakhya",
        name_hindi="जख्या",
        scientific_name="Cleome viscosa",
        category="Medicinal & Aromatic Flora",
        botanical_family="Cleomaceae",
        habitat_altitude="600m – 1,800m",
        traditional_uses="Wild mountain mustard; tiny crunchy black seeds used as the quintessential tempering (Chhonk) in every Garhwali potato dish, saag, and dal; seeds provide a uniquely nutty aromatic crunch.",
        spiritual_and_temple_significance="The indispensable culinary signature of Garhwali food culture.",
        cultural_folklore="Garhwalis living across the world always carry packets of Jakhya seeds from home, declaring that without Jakhya, potato subji lacks its soul."
    ),
    "faran": GarhwaliPlant(
        id="faran",
        name_garhwali="फरन / जम्बू",
        name_roman="Faran / Jambu",
        name_hindi="जम्बू",
        scientific_name="Allium stracheyi",
        category="Medicinal & Aromatic Flora",
        botanical_family="Amaryllidaceae",
        habitat_altitude="2,500m – 4,000m",
        traditional_uses="Dried alpine wild chive leaves fried in ghee as aromatic tempering for dals and curries; aids digestion and combats high altitude mountain sickness.",
        spiritual_and_temple_significance="Harvested from alpine meadows of Niti, Mana, and Nilang.",
        cultural_folklore="The pungent aroma of Faran fried in desi ghee wafts through hill villages, whetting every appetite."
    ),
    "gandharayan": GarhwaliPlant(
        id="gandharayan",
        name_garhwali="गंधरायण / चोरा",
        name_roman="Gandharayan / Chora",
        name_hindi="गंधरायण",
        scientific_name="Angelica glauca",
        category="Medicinal & Aromatic Flora",
        botanical_family="Apiaceae",
        habitat_altitude="2,800m – 4,200m",
        traditional_uses="Aromatic dried root used as carminative, digestive flavoring in curries, and traditional remedy for colic and gastric troubles.",
        spiritual_and_temple_significance="Gathered from the subalpine slopes of Chamoli.",
        cultural_folklore="A tiny pinch of powdered Gandharayan in winter lentils warms the body and banishes indigestion."
    ),
    "bhangjeera": GarhwaliPlant(
        id="bhangjeera",
        name_garhwali="भंगजीरा",
        name_roman="Bhangjeera",
        name_hindi="भंगजीरा",
        scientific_name="Perilla frutescens",
        category="Medicinal & Aromatic Flora",
        botanical_family="Lamiaceae",
        habitat_altitude="1,000m – 2,200m",
        traditional_uses="Aromatic perilla seeds roasted and stone-ground with garlic, green chillies, and lemon into tangy nutty chutney; rich in Omega-3 fatty acids.",
        spiritual_and_temple_significance="Traditional festive and winter condiment.",
        cultural_folklore="No Garhwali meal of Manduwa roti is complete without fresh spicy Bhangjeera chutney ground on a stone Silbatta."
    )
}


class FloraTreasury:
    """Master registry and query interface for Garhwali ethnobotanical flora."""

    @classmethod
    def list(cls) -> List[GarhwaliPlant]:
        return list(FLORA_DATA.values())

    @classmethod
    def get(cls, id_or_name: str) -> Optional[GarhwaliPlant]:
        key = id_or_name.strip().lower().replace(" ", "_")
        if key in FLORA_DATA:
            return FLORA_DATA[key]
        for p in FLORA_DATA.values():
            if (id_or_name in p.name_garhwali or
                key == p.name_roman.lower() or
                key == p.name_hindi.lower() or
                key in p.scientific_name.lower()):
                return p
        return None

    @classmethod
    def search(cls, query: str) -> List[GarhwaliPlant]:
        if not query:
            return cls.list()
        q = query.strip().lower()
        results = []
        for p in FLORA_DATA.values():
            if (q in p.name_garhwali.lower() or
                q in p.name_roman.lower() or
                q in p.name_hindi.lower() or
                q in p.scientific_name.lower() or
                q in p.category.lower() or
                q in p.botanical_family.lower() or
                q in p.traditional_uses.lower() or
                q in p.spiritual_and_temple_significance.lower() or
                q in p.cultural_folklore.lower()):
                results.append(p)
        return results

    @classmethod
    def stats(cls) -> Dict[str, Any]:
        categories: Dict[str, int] = {}
        for p in FLORA_DATA.values():
            categories[p.category] = categories.get(p.category, 0) + 1
        return {
            "total_plants": len(FLORA_DATA),
            "categories": categories,
        }
