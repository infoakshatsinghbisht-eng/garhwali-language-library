# -*- coding: utf-8 -*-
"""Garhwali Folk Songs, Epics, Literature & Authors."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

POEMS = [
    {
        "title": "चैता की चैतवाली (Chaita Ki Chaitwali)",
        "genre": "Folk Romance & Legend",
        "description": "Classic ballad celebrating the return of springtime, blossoms of the rhododendron (Buransh), and Garhwali mountain heritage."
    },
    {
        "title": "बेड़ू पाको बारामासा (Bedu Pako Baramasa)",
        "genre": "Universal Uttarakhand Anthem",
        "description": "Immortal folk song of the Himalayas describing wild Himalayan figs ripening across the 12 seasons of Garhwal & Kumaon."
    }
]

EPICS = [
    {
        "title": "माधो सिंह भंडारी (Madho Singh Bhandari)",
        "hero": "Madho Singh Bhandari (मलेथा का सेनापति)",
        "theme": "Engineering marvel of digging the mountain canal of Maletha and ultimate courage in defending Garhwal Kingdom."
    },
    {
        "title": "जीतू बगड़वाल (Jeetu Bagdwal)",
        "hero": "Jeetu Bagdwal",
        "theme": "Legendary flute player whose divine music enchanted the celestial fairies (आंछरियों) of the high Alpine bugyals."
    }
]

AUTHORS = [
    {
        "name": "भजन सिंह 'सिंह' (Bhajan Singh 'Singh')",
        "era": "1905-1996",
        "work": "'सिंहनाद' (Singhnaad) and pioneer of modern Garhwali epic poetry and cultural philosophy."
    },
    {
        "name": "चन्द्रकुंवर बर्त्वाल (Chandra Kunwar Bartwal)",
        "era": "1919-1947",
        "work": "'हिमवंत का कालिदास' — Legendary romantic and nature poet of Rudraprayag, Garhwal."
    },
    {
        "name": "नरेन्द्र सिंह नेगी (Narendra Singh Negi)",
        "era": "Contemporary",
        "work": "'Garh-Gaurav' — Voice of Garhwal, songwriter and folk maestro chronicling the socio-cultural soul of Uttarakhand."
    }
]

def poems() -> List[Dict[str, Any]]: return POEMS
def epics() -> List[Dict[str, Any]]: return EPICS
def authors() -> List[Dict[str, Any]]: return AUTHORS
