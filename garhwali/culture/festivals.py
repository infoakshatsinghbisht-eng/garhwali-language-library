# -*- coding: utf-8 -*-
"""Garhwali Festivals and Celebrations."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

GARHWALI_FESTIVALS = [
    {
        "name": "फूलदेई (Phooldei)",
        "month": "चैत (Chait)",
        "description": "Himalayan flower festival where children place freshly bloomed wild flowers (Buransh, Pyoli) on village doorsteps.",
        "blessing": "फूल देई, छम्मा देई, दैणी द्वार, भर भकार!"
    },
    {
        "name": "इगास बग्वाल (Igas Bagwal)",
        "month": "कातिक (Katik)",
        "description": "Celebrated 11 days after Diwali in Garhwal to welcome warrior hero Madho Singh Bhandari back from victorious battle.",
        "tradition": "Spinning fire rope torch (भैलो / Bhelo) and community Raso-Thadya folk dances."
    },
    {
        "name": "नंदा देवी राज जात (Nanda Devi Raj Jat)",
        "month": "भादौ (Bhado)",
        "description": "The Mahakumbh of the Himalayas — 280km pilgrimage trek across high Alpine meadows to Roopkund & Homkund.",
        "tradition": "Led by the sacred four-horned ram (चौसिंग्या खाडू) honoring Goddess Nanda Devi."
    },
    {
        "name": "बटर फेस्टिवल / अंदूड़ी उत्सव (Anduri Butter Festival)",
        "month": "भादौ (Bhado)",
        "description": "Celebrated in Dayara Bugyal meadow (Uttarkashi) where villagers play Holi with fresh milk, butter, and chaach to thank nature.",
        "tradition": "Offering first dairy harvest to Lord Krishna and forest deities."
    }
]

def list_festivals() -> List[Dict[str, Any]]:
    return GARHWALI_FESTIVALS
