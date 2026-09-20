# -*- coding: utf-8 -*-
"""Garhwali Pronouns and Pronominal Declension System."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

GARHWALI_PRONOUNS_TABLE = {
    "1sg": {
        "direct": "मैं", "ergative": "मैंले", "dative": "मूकै / मैंकणी",
        "genitive_m": "मेरो / मिरो / मेरु", "genitive_f": "मेरी / मिरी",
        "genitive_pl": "मेरा / मिरा", "ablative": "मैंबटि / मेरो से", "locative": "मैंमा",
        "english": "I / Me / My"
    },
    "1pl": {
        "direct": "हम / हमीं", "ergative": "हमले / हमींले", "dative": "हमकै / हमकणी",
        "genitive_m": "हमारो / हमरु", "genitive_f": "हमारी / हमरी",
        "genitive_pl": "हमारा / हमरा", "ablative": "हमबटि", "locative": "हममा",
        "english": "We / Us / Our"
    },
    "2sg_informal": {
        "direct": "तू", "ergative": "तैंले", "dative": "तूकै / तैंकणी",
        "genitive_m": "तेरो / तिरो / तेरु", "genitive_f": "तेरी / तिरी",
        "genitive_pl": "तेरा / तिरा", "ablative": "तैंबटि", "locative": "तैंमा",
        "english": "You (informal)"
    },
    "2pl_polite": {
        "direct": "तुम / तम / आप", "ergative": "तुमले / तमले / आपले", "dative": "तुमकै / तुमकणी / आपकणी",
        "genitive_m": "तुमरो / तुमारो / आपकु", "genitive_f": "तुमरी / तुमारी / आपकी",
        "genitive_pl": "तुमरा / तुमारा / आपका", "ablative": "तुमबटि / आपबटि", "locative": "तुममा / आपमा",
        "english": "You (polite/plural)"
    },
    "3sg_near": {
        "direct": "यो / यों", "ergative": "येले / योंले", "dative": "येकै / येकणी",
        "genitive_m": "येको / याको / यिकु", "genitive_f": "येकी / याकी / यिकी",
        "genitive_pl": "येका / याका", "ablative": "येबटि", "locative": "येमा",
        "english": "This / He / She (near)"
    },
    "3sg_far": {
        "direct": "वो / वोह / ऊ", "ergative": "वेले / वोले / ऊँले", "dative": "वेकै / वेकणी",
        "genitive_m": "वेको / वाको / विकु", "genitive_f": "वेकी / वाकी / विकी",
        "genitive_pl": "वेका / वाका", "ablative": "वेबटि", "locative": "वेमा",
        "english": "That / He / She (far)"
    },
    "3pl": {
        "direct": "उन / उनूँ / वे", "ergative": "उनले / उनूँले", "dative": "उनकै / उनकणी",
        "genitive_m": "उनरो / उनको / उनरु", "genitive_f": "उनरी / उनकी / उनरी",
        "genitive_pl": "उनरा / उनका", "ablative": "उनबटि", "locative": "उनमा",
        "english": "They / Them / Their"
    },
    "interrogative_person": {
        "direct": "कु / को / काण", "ergative": "कैल / कैले", "dative": "कैकै / कैकणी",
        "genitive_m": "कैकू / कैको", "genitive_f": "कैकी", "genitive_pl": "कैका",
        "ablative": "कैबटि", "locative": "कैमा",
        "english": "Who / Whom / Whose"
    },
    "interrogative_thing": {
        "direct": "क्या / कि / के", "dative": "क्याकणी", "genitive_m": "क्याको / क्याकु",
        "english": "What / Which"
    },
    "reflexive": {
        "direct": "आप / अपु / खुद", "genitive_m": "अपणो / अपुनो / आपु",
        "genitive_f": "अपणी / अपुनी", "genitive_pl": "अपणा / अपुना",
        "english": "Oneself / Own"
    }
}

def get_pronoun_form(person_key: str, case: str = "direct") -> str:
    p_data = GARHWALI_PRONOUNS_TABLE.get(person_key, {})
    return p_data.get(case, p_data.get("direct", ""))
