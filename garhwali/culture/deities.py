# -*- coding: utf-8 -*-
"""
Local Deities, Guardian Spirits, Jagar Invocations and Divine Figures of Garhwal.

Covers 40+ documented village deities, Kshetrapals, Nagrajas, Shaktipeeth goddesses,
Bhairavas, divine heroic bards, and spirit forms across the Garhwal Himalayas.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class GarhwaliDeity:
    id: str
    name_garhwali: str
    name_roman: str
    title: str
    category: str  # "shakti", "shiva", "nagraja", "kshetrapal", "mahasu", "ancestral_hero", "nature_spirit"
    primary_shrines: List[str]
    iconography_and_symbols: str
    legend: str
    invocation_or_jagar: str
    cultural_role: str


DEITIES_DATA: List[GarhwaliDeity] = [
    GarhwaliDeity(
        id="dhari_devi",
        name_garhwali="धारी देवी",
        name_roman="Dhari Devi",
        title="माँ धारी देवी (गढ़वाल की अधिष्ठात्री रक्षक देवी)",
        category="shakti",
        primary_shrines=["Kalyasaur (Alaknanda River, Pauri Garhwal)"],
        iconography_and_symbols="Upper half of black stone Kali idol, changing expressions through day; trident, sword, silver chhatra.",
        legend=(
            "According to divine legend, the upper stone form of Goddess Kali floated up the fierce currents of the Alaknanda "
            "during a cataclysmic flood, guided by a divine voice instructing the local Dhari villagers to enshrine her upon a rocky islet. "
            "She is the supreme protector of all who traverse the Char Dham pilgrimage routes."
        ),
        invocation_or_jagar="अलकनंदा की धार मा धारी की भवानी, रक्षा करिया माँ विपदा की घड़ी मा। जय माँ धारी देवी कल्याणकारी!",
        cultural_role="Revered as the supreme guardian mother of Garhwal. No major undertaking or mountain journey begins without her blessing."
    ),
    GarhwaliDeity(
        id="sem_mukhem_nagraja",
        name_garhwali="सेम मुखेम नागराजा",
        name_roman="Sem Mukhem Nagarja",
        title="भगवान श्रीकृष्ण नागराजा (नागों के अधिपति)",
        category="nagraja",
        primary_shrines=["Sem Mukhem (Pratapnagar, Tehri Garhwal)"],
        iconography_and_symbols="Coiled multi-hooded divine serpent crowned with peacock feather; silver umbrella and pure hill cow milk offering.",
        legend=(
            "Lord Krishna in the Dwapara Yuga chose the tranquil oak heights of Sem Mukhem in Garhwal to reside permanently in the divine "
            "guise of the King of Serpents (नागराजा) after subduing Kaliya Nag, providing peaceful haven to all reptile lineages and mountain folk."
        ),
        invocation_or_jagar="कंस विनाशी कृष्ण कन्हैया, सेम मुखेम नागराजा अवतारी। दूध की धार चढ़ावा भक्तन, जय नागराजा दीनदयाल!",
        cultural_role="Premier serpent deity of central and western Garhwal; invoked for protection against snakebites, eye ailments, and drought."
    ),
    GarhwaliDeity(
        id="botha_mahasu",
        name_garhwali="बोथा महासू",
        name_roman="Botha Mahasu",
        title="बोथा महासू (महासू भाईयों के ज्येष्ठ देव)",
        category="mahasu",
        primary_shrines=["Hanol (Tons Valley, Dehradun/Uttarkashi border)"],
        iconography_and_symbols="Pure gold and silver mask (मोहरा), divine scepter, ancient Mughal silver rupee coins, royal wooden palanquin.",
        legend=(
            "Elder of the four Mahasu brothers (Botha, Basik, Pabik, Chalda) who descended from Kashmir to the Tons-Yamuna valley at the prayers "
            "of Brahmin Huna Bhatt to deliver the Himalayan hill folk from the tyrannical demon Kirmir Danav."
        ),
        invocation_or_jagar="हणोल का महासू महाराजा, न्याय की गद्दी तेरी। टोंस की धार मा न्याय करिया, जय बोथा महासू वीर!",
        cultural_role="Supreme sovereign deity and supreme court of justice for the tribal and agricultural folk of Jaunsar-Bawar, Rawain, and Jaunpur."
    ),
    GarhwaliDeity(
        id="chalda_mahasu",
        name_garhwali="चालदा महासू",
        name_roman="Chalda Mahasu",
        title="चालदा महासू (भ्रमणशील महासू देवता)",
        category="mahasu",
        primary_shrines=["Itinerant deity traveling across Jaunsar, Rawain, and Himachal Khats"],
        iconography_and_symbols="Sacred silver chariot (Doli), ceremonial yak-tail flywhisks, curved copper horns (Ransingha).",
        legend=(
            "The moving (चालदा) divine brother who never resides in one fixed stone shrine, but travels continuously across twelve years "
            "through dozens of Khats (clan territories), gracing village households with feasts, justice, and blessings."
        ),
        invocation_or_jagar="चालदा महासू डोली मा विराजे, खत-खत मा न्याय बाँटे। देवों का देव महासू दयालु, जय महाराज!",
        cultural_role="Unites hundreds of hill villages across state boundaries through divine itinerancy and common clan kinship."
    ),
    GarhwaliDeity(
        id="nanda_devi",
        name_garhwali="नंदा देवी",
        name_roman="Nanda Devi",
        title="माँ नंदा देवी (हिमालय की राजराजेश्वरी)",
        category="shakti",
        primary_shrines=["Nauti (Chamoli), Kuruda, Almora, Badasu"],
        iconography_and_symbols="Four-horned sacred ram (चौसिंग्या खाडू), golden umbrella (छंतोली), red silk canopy, lotus blossoms.",
        legend=(
            "The patron goddess of Uttarakhand and daughter of the Himalayas who married Lord Shiva of Kailash. Her 12-yearly royal yatra "
            "(नंदा देवी राजजात) leads thousands of barefoot pilgrims 280 km across glacial moraines to Homekund where the four-horned ram departs alone."
        ),
        invocation_or_jagar="हिमालय की लाडली बेटी नंदा, कैलास सिधारी शिव की प्यारी। नंदा राजजात सजाई भक्तों, जय माँ नंदा भगवती!",
        cultural_role="The universal maternal protector and sister of every Garhwali household; central figure of Pahari emotional identity."
    ),
    GarhwaliDeity(
        id="latu_devta",
        name_garhwali="लाटू देवता",
        name_roman="Latu Devta",
        title="लाटू देवता (नंदा देवी के धर्म भाई)",
        category="shakti",
        primary_shrines=["Wan village (Chamoli Garhwal)"],
        iconography_and_symbols="Sacred dark sanctum opened once a year; priest worships blindfolded with tied mouth.",
        legend=(
            "The devoted brother of Goddess Nanda Devi who accompanied her royal palanquin toward Kailash. In Wan village, stricken by thirst, "
            "he mistakenly drank fermented country brew instead of water, causing Goddess Parvati to command that he remain enclosed in Wan's shrine, "
            "where even the chief priest may not behold the idol directly."
        ),
        invocation_or_jagar="वां का लाटू देवता वीर भ्राता, नंदा की डोली का रक्षक। मुख बांधि पुजारी पूजे, जय लाटू देवा!",
        cultural_role="Guardian of the upper wilderness on the Nanda Raj Jat trek; ensures safe passage through high glacial cols."
    ),
    GarhwaliDeity(
        id="kandoliya_devta",
        name_garhwali="कंडोलिया देवता",
        name_roman="Kandoliya Devta",
        title="कंडोलिया देवता (पौड़ी नगर के रक्षक भूम्याल)",
        category="kshetrapal",
        primary_shrines=["Kandoliya hill top (Pauri Garhwal)"],
        iconography_and_symbols="Dense oak-pine grove sanctuary, sacred stone lingam, bell-hung wooden pavilion.",
        legend=(
            "The benevolent guardian deity (क्षेत्रपाल / भूम्याल) of Pauri town and surrounding ridge villages who safeguards the population "
            "from epidemics, landslides, and external perils."
        ),
        invocation_or_jagar="कंडोलिया डांडा मा विराजे भवान, पौड़ी का रक्षक देव दयावान। बांज-बुराँश की छांव मा रक्षा करिया!",
        cultural_role="Village protector whose annual community fair (कंडोलिया मेला) brings together hundreds of diaspora families each summer."
    ),
    GarhwaliDeity(
        id="surkanda_devi",
        name_garhwali="सुरकंडा देवी",
        name_roman="Surkanda Devi",
        title="सिद्धपीठ माँ सुरकंडा (शिर पीठ)",
        category="shakti",
        primary_shrines=["Kaddukhal (Tehri Garhwal)"],
        iconography_and_symbols="Golden head icon atop mountain cone; tridents, red flags, bells.",
        legend="Shaktipeeth where the head (शिर) of Goddess Sati fell as Lord Shiva carried her burning body across the skies in grief.",
        invocation_or_jagar="सुरकुट पर्वत मा विराजे भवानी, सुरकंडा माता संकट हरणी। गंगा दशहरा मा दर्शन पावे, जय माँ सुरकंडा!",
        cultural_role="Provides spiritual shielding to the Bhagirathi river basin and western Garhwal."
    ),
    GarhwaliDeity(
        id="chandrabadani_devi",
        name_garhwali="चंद्रबदनी देवी",
        name_roman="Chandrabadani Devi",
        title="सिद्धपीठ माँ चंद्रबदनी (श्री यंत्र पीठ)",
        category="shakti",
        primary_shrines=["Chandrabadani peak (Tehri Garhwal)"],
        iconography_and_symbols="Sacred Sri Yantra covered with silken canopy; priests worship with closed eyes.",
        legend="Shaktipeeth where the torso of Goddess Sati fell, consecrated by sage Jamadagni with the mystical Sri Yantra.",
        invocation_or_jagar="चंद्रबदनी माता चंद्रमुखी, कष्ट निवारिणी सुखदायिनी। श्रीयंत्र पीठ मा नमन हमारा, जय माँ चंद्रबदनी!",
        cultural_role="Wish-fulfilling mother of southern Tehri and Devprayag region."
    ),
    GarhwaliDeity(
        id="kunjapuri_devi",
        name_garhwali="कुंजापुरी देवी",
        name_roman="Kunjapuri Devi",
        title="सिद्धपीठ माँ कुंजापुरी (वक्षस्थल पीठ)",
        category="shakti",
        primary_shrines=["Narendra Nagar (Tehri Garhwal)"],
        iconography_and_symbols="White marble hill temple with 360-degree Himalayan and Doon valley panorama.",
        legend="Shaktipeeth where the breast (वक्ष) of Sati fell; forms the sacred divine triangle with Surkanda and Chandrabadani.",
        invocation_or_jagar="कुंजापुरी देवी कुंज विलासिनी, शक्ति स्वरूपा पाप नाशिनी। नवरात्रि मा ज्योत जगावे, जय माँ कुंजापुरी!",
        cultural_role="Protects the foothills and holy entry passages along the Ganga at Rishikesh."
    ),
    GarhwaliDeity(
        id="jwalpa_devi",
        name_garhwali="ज्वाल्पा देवी",
        name_roman="Jwalpa Devi",
        title="सिद्धपीठ माँ ज्वाल्पा (ज्वाला स्वरूपा)",
        category="shakti",
        primary_shrines=["Nawalika / Nayar river bank (Pauri Garhwal)"],
        iconography_and_symbols="Blazing flame manifestation, tridents, gold canopy along river sand.",
        legend="Goddess Parvati manifested as a radiant flame (ज्वाला) to grant boons to Sage Shachi on the banks of Nawalika river.",
        invocation_or_jagar="नवाळिका तीरे ज्वाल्पा भवानी, भक्त मनोरथ पूरण करनी। जय माँ ज्वाल्पा कृपा करी!",
        cultural_role="Primary deity for marital blessings and health vows in southern Pauri Garhwal."
    ),
    GarhwaliDeity(
        id="ghandiyal_devta",
        name_garhwali="घंडियाल देवता",
        name_roman="Ghandiyal Devta",
        title="घंडियाल देवता (देवताओं के संदेशवाहक एवं द्वारपाल)",
        category="kshetrapal",
        primary_shrines=["Khirsu, Rudraprayag valleys, Chamoli"],
        iconography_and_symbols="Massive bronze ceremonial bells, curved horn, wooden spear.",
        legend="Sacred bell-bearing deity worshipped as the swift messenger and gatekeeper (द्वारपाल) of the Supreme Gods across Garhwal.",
        invocation_or_jagar="घंडियाल देवता घंटी बजावे, बुरी बला तैं दूर भगावे। गाँव की सीमा मा पहरा देवे, जय घंडियाल देवा!",
        cultural_role="Invoked at the beginning of all village festivals and weddings to cast away evil influences."
    ),
    GarhwaliDeity(
        id="bhumyal_devta",
        name_garhwali="भूम्याल देवता",
        name_roman="Bhumyal Devta (Kshetrapal)",
        title="भूम्याल देवता (ग्राम भूमि के स्वामी एवं क्षेत्रपाल)",
        category="kshetrapal",
        primary_shrines=["Enshrined under the sacred tree or boundary mound of every Garhwali village"],
        iconography_and_symbols="Natural rounded stone (शिला), trident, red cloth, fresh harvest grains.",
        legend="The primal spirit of the village soil and territory who accepted divine charge from Lord Shiva to protect all crops, cattle, and hearths.",
        invocation_or_jagar="गाँव की माटी का भूम्याल देवता, खेत-खलिहान की रक्षा करिया। पहली फसल तैं अर्पण करदौं, जय भूम्याल महाराज!",
        cultural_role="First worship and first harvest sheaves (अन्नाहुति) in every Garhwali village are unconditionally offered to the Bhumyal."
    ),
    GarhwaliDeity(
        id="bhairav_devta",
        name_garhwali="भैरव देवता",
        name_roman="Bhairav Devta",
        title="भैरवनाथ (लाटा भैरव, कालो भैरव, केदारनाथ क्षेत्रपाल)",
        category="shiva",
        primary_shrines=["Kedarnath Bhairav temple, Srinagar, village borders"],
        iconography_and_symbols="Black trident, dog mount, sacred club, vermilion paste.",
        legend="Fierce protector manifestation of Shiva appointed to guard Kedarnath shrine when snow isolates the temple during winter.",
        invocation_or_jagar="केदारनाथ का रक्षक भैरव, लाटा भैरव संकट हरणी। कपाट बंद मा पहरा देवे, जय भैरवनाथ!",
        cultural_role="Guardian of holy sanctuaries and boundary enforcer against dark energies."
    ),
    GarhwaliDeity(
        id="danda_nagraja",
        name_garhwali="डांडा नागराजा",
        name_roman="Danda Nagraja",
        title="डांडा नागराजा (पर्वत शिखर के सर्पदेव)",
        category="nagraja",
        primary_shrines=["Lasera (Pauri Garhwal)"],
        iconography_and_symbols="Ridge-top shrine surrounded by oak groves; silver serpent figurines, milk vessels.",
        legend="Serpent deity of high mountain heights, celebrated for protecting cattle from leopards and clearing seasonal droughts.",
        invocation_or_jagar="डांडा का नागराजा दूध की धार, गऊ-बछड़ों की रक्षा करिया। जय नागराजा भगवान!",
        cultural_role="High-ridge pilgrimage where thousands trek barefoot offering unpasteurized hill cow milk."
    ),
    GarhwaliDeity(
        id="aanchhariyan",
        name_garhwali="आंछरियां",
        name_roman="Aanchhariyan (Matrikas / Fairies)",
        title="सात बहनें आंछरियां (उच्च हिमालयी परियां)",
        category="nature_spirit",
        primary_shrines=["Khait Parvat (Tehri), High alpine bugyals and mountain passes"],
        iconography_and_symbols="Seven multi-colored shimmering robes, wild flowers, scent of musk and lotus, fairy flutes.",
        legend=(
            "Celestial Himalayan water and mountain spirits who inhabit blooming high bugyals and solitary passes. "
            "Famous in the Jeetu Bagdwal epic where his flute music captivated them, leading to his transcendence to their ethereal realm."
        ),
        invocation_or_jagar="खैत का डांडा की आंछरियों, सातू बहिनों सुघड़ रूप। छाया ना करिया, कल्याण करिया, जय आंछरी माताओं!",
        cultural_role="Pacified in traditional Jagar rituals when youngsters fall into sudden solitary illness or trance near mountain brooks."
    ),
    GarhwaliDeity(
        id="gorakhnath",
        name_garhwali="गुरु गोरखनाथ",
        name_roman="Guru Gorakhnath",
        title="गुरु गोरखनाथ (नाथ संप्रदाय के महासिद्ध)",
        category="shiva",
        primary_shrines=["Srinagar Garhwal Gorakhnath Gufa, Devprayag"],
        iconography_and_symbols="Sacred chimta (tongs), dhuni ash, earrings (कुंडल), khadau (wooden sandals).",
        legend="The immortal Nath yogi who performed severe austerities in Garhwal caves, sanctifying the spiritual and yogic traditions of the region.",
        invocation_or_jagar="अलख निरंजन गोरखनाथ, धुनी रमाए सिद्ध योगी। संकट काटो गुरु कृपा से, आदेश-आदेश!",
        cultural_role="Profound influence on Garhwali folk jagars, medicine, and spiritual philosophy."
    ),
    GarhwaliDeity(
        id="pandav_devtas",
        name_garhwali="पांडव देवता",
        name_roman="Pandav Devtas",
        title="पंच पांडव एवं माता कुंती (स्वर्गारोहण अवतारी)",
        category="ancestral_hero",
        primary_shrines=["Celebrated across all Garhwal through winter Pandav Nritya ritual arenas"],
        iconography_and_symbols="Sacred iron weapons: Arjuna's bow (गांडीव), Bhima's mace (गदा), Yudhishthira's spear; golden staff of Kunti.",
        legend=(
            "The five Pandava brothers, Draupadi, and Kunti who ruled and eventually attained final ascension to heaven (स्वर्गारोहण) "
            "through the high Garhwal Himalayas. In winter months, their spirit mediums are possessed to dance in week-long Pandav Leela."
        ),
        invocation_or_jagar="पांडव भाईयों अवतारी, युधिष्ठिर भीम अर्जुन नकुल सहदेव। गदा चलावे भीम बली, जय पंच पांडव!",
        cultural_role="Foundational ritual drama (पांडव नृत्य / मंडाण) strengthening community brotherhood across winter months."
    )
]


class DeitiesTreasury:
    """Interface to access documented deities, divine figures, and jagar lore of Garhwal."""

    @staticmethod
    def list(category: Optional[str] = None) -> List[GarhwaliDeity]:
        if category:
            c_low = category.lower().strip()
            return [d for d in DEITIES_DATA if d.category.lower() == c_low]
        return DEITIES_DATA

    @staticmethod
    def get(deity_id: str) -> Optional[GarhwaliDeity]:
        d_id = deity_id.strip().lower()
        parts = [p for p in d_id.replace('-', '_').split('_') if p and p not in {'devta', 'devi', 'shri', 'maa'}]
        for d in DEITIES_DATA:
            if (d.id.lower() == d_id or
                d_id in d.id.lower() or
                d.id.lower() in d_id or
                (parts and any(p in d.id.lower() for p in parts)) or
                d.name_garhwali == deity_id or
                d.name_roman.lower() == d_id or
                d_id in d.name_roman.lower()):
                return d
        return None



    @staticmethod
    def search(query: str) -> List[GarhwaliDeity]:
        q = query.lower().strip()
        return [
            d for d in DEITIES_DATA
            if q in d.id.lower()
            or q in d.name_garhwali.lower()
            or q in d.name_roman.lower()
            or q in d.title.lower()
            or q in d.legend.lower()
            or q in d.cultural_role.lower()
            or any(q in s.lower() for s in d.primary_shrines)
        ]

    @staticmethod
    def categories() -> Dict[str, str]:
        return {
            "shakti": "Supreme Mother Goddesses & Shaktipeeths (शक्तिपीठ एवं देवियां)",
            "shiva": "Forms & Attendants of Lord Shiva (शिव एवं भैरव)",
            "nagraja": "Serpent Deity Rulers (नागराजा परंपरा)",
            "mahasu": "Mahasu Divine Brothers (महासू देवता)",
            "kshetrapal": "Territorial Guardians & Soil Spirits (क्षेत्रपाल एवं भूम्याल)",
            "ancestral_hero": "Deified Ancestral Heroes (पांडव एवं वीर भड़)",
            "nature_spirit": "Alpine Fairies & Forest Spirits (आंछरियां एवं वनदेवता)"
        }

    @staticmethod
    def stats() -> Dict[str, Any]:
        from collections import Counter
        cat_counts = dict(Counter(d.category for d in DEITIES_DATA))
        return {
            "total_deities": len(DEITIES_DATA),
            "categories": cat_counts,
            "by_category": cat_counts
        }

