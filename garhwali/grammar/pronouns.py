# -*- coding: utf-8 -*-
"""
Garhwali Pronouns and Pronominal Declension System.

Includes:
1. Complete Pronominal Declension Matrix across cases:
   Direct, Ergative, Dative/Accusative, Instrumental, Ablative, Genitive, Locative.
2. Dialectal variations:
   Srinagariya, Salani, Rathwali, Tehri, Badhani.
3. Demonstrative (proximate / remote / intermediate), Indefinite, Relative, Correlative,
   Reflexive, Reciprocal, and Interrogative subsystems.
"""

from typing import Dict, List, Any, Optional, Tuple, Union, Set


GARHWALI_PRONOUNS_TABLE: Dict[str, Dict[str, str]] = {
    "1sg": {
        "direct": "मि / मी / मैं",
        "ergative": "म्यन / मि न / मैंन / मैंले / मैले",
        "dative": "मिते / म्यतैं / मूकै / मैंकणी",
        "instrumental": "मि सेती / म्यन सेती",
        "genitive_m": "मेरो / म्यारो / मिरो / मेरु",
        "genitive_f": "मेरी / म्यारी / मिरी",
        "genitive_pl": "मेरा / म्यारा / मिरा",
        "ablative": "मि बटी / मैंबटि / मेरो से",
        "locative": "मि मा / मैंमा",
        "english": "I / Me / My"
    },
    "1pl": {
        "direct": "हमि / हम / हमीं",
        "ergative": "हमन / हमले / हमींले",
        "dative": "हमिते / हमकै / हमकणी / हमतैं",
        "instrumental": "हमि सेती / हमन सेती",
        "genitive_m": "हमारो / हमरु / हमरो",
        "genitive_f": "हमारी / हमरी",
        "genitive_pl": "हमारा / हमरा",
        "ablative": "हमि बटी / हमबटि",
        "locative": "हमि मा / हममा",
        "english": "We / Us / Our"
    },
    "2sg_informal": {
        "direct": "तू",
        "ergative": "त्वेन / तैंले / तू न / त्वैले",
        "dative": "त्वेते / त्वेतैं / तूकै / तैंकणी",
        "instrumental": "त्वे सेती / त्वेन सेती",
        "genitive_m": "तेरो / तिरो / तेरु / त्वारो",
        "genitive_f": "तेरी / तिरी / त्वारी",
        "genitive_pl": "तेरा / तिरा / त्वारा",
        "ablative": "त्वे बटी / तैंबटि",
        "locative": "त्वे मा / तैंमा",
        "english": "You (informal / intimate)"
    },
    "2pl_polite": {
        "direct": "तुमि / तुम / तम / आप",
        "ergative": "तुमन / तुमले / तमले / आपले",
        "dative": "तुमिते / तुमकै / तुमकणी / आपकणी",
        "instrumental": "तुमि सेती / तुम सेती",
        "genitive_m": "तुमारो / तुमरो / आपकु",
        "genitive_f": "तुमारी / तुमरी / आपकी",
        "genitive_pl": "तुमारा / तुमरा / आपका",
        "ablative": "तुमि बटी / तुमबटि / आपबटि",
        "locative": "तुमि मा / तुममा / आपमा",
        "english": "You (polite / plural)"
    },
    "3sg_near": {
        "direct": "यो / यों",
        "ergative": "यन / येन / येले / योंले",
        "dative": "येते / येकै / येकणी / यैतैं",
        "instrumental": "ये सेती / यन सेती",
        "genitive_m": "येको / याको / यिकु / यैको",
        "genitive_f": "येकी / याकी / यिकी / यैकी",
        "genitive_pl": "येका / याका / यैका",
        "ablative": "ये बटी / येबटि",
        "locative": "ये मा / येमा",
        "english": "This / He / She (proximate)"
    },
    "3sg_far": {
        "direct": "वो / वोह / ऊ / उ",
        "ergative": "वन / वेन / वेले / वोले / ऊँले",
        "dative": "वेते / वेकै / वेकणी / वैतैं",
        "instrumental": "वे सेती / वन सेती",
        "genitive_m": "वेको / वाको / विकु / वैको",
        "genitive_f": "वेकी / वाकी / विकी / वैकी",
        "genitive_pl": "वेका / वाका / वैका",
        "ablative": "वे बटी / वेबटि",
        "locative": "वे मा / वेमा",
        "english": "That / He / She (remote)"
    },
    "3pl": {
        "direct": "ये / उन / उनूँ / वे",
        "ergative": "यौंनी / वौंनी / उनले / उनूँले / योंन / वोंन",
        "dative": "येंते / वोंते / उनकै / उनकणी / यौंतैं / वौंतैं",
        "instrumental": "यों सेती / वों सेती / उन सेती",
        "genitive_m": "योंको / वोंको / उनरो / उनको / उनरु",
        "genitive_f": "योंकी / वोंकी / उनरी / उनकी",
        "genitive_pl": "योंका / वोंका / उनरा / उनका",
        "ablative": "यों बटी / वों बटी / उनबटि",
        "locative": "यों मा / वों मा / उनमा",
        "english": "They / Them / Their"
    },
    "relative": {
        "direct": "जो",
        "ergative": "ज्यन / जेन / जेले",
        "dative": "जेते / जेकै / जैतैं",
        "instrumental": "जे सेती",
        "genitive_m": "जेको / जैको",
        "genitive_f": "जेकी / जैकी",
        "genitive_pl": "जेका / जैका",
        "ablative": "जे बटी",
        "locative": "जे मा",
        "english": "Who / Whoever / Which (relative)"
    },
    "correlative": {
        "direct": "सो / वो",
        "ergative": "त्यन / तेन / वेन",
        "dative": "तेते / वेते / तैतैं",
        "instrumental": "ते सेती / वे सेती",
        "genitive_m": "तेको / वेको / वैको",
        "genitive_f": "तेकी / वेकी / वैकी",
        "genitive_pl": "तेका / वेका / वैका",
        "ablative": "ते बटी / वे बटी",
        "locative": "ते मा / वे मा",
        "english": "That one / He / She (correlative)"
    },
    "interrogative_person": {
        "direct": "कु / को / काण",
        "ergative": "कैल / कैले / कन",
        "dative": "कैकै / कैकणी / कैते",
        "instrumental": "कै सेती",
        "genitive_m": "कैकू / कैको",
        "genitive_f": "कैकी",
        "genitive_pl": "कैका",
        "ablative": "कै बटी / कैबटि",
        "locative": "कै मा / कैमा",
        "english": "Who / Whom / Whose"
    },
    "interrogative_thing": {
        "direct": "क्या / कि / के",
        "ergative": "क्या न",
        "dative": "क्याते / क्याकणी",
        "instrumental": "क्या सेती",
        "genitive_m": "क्याको / क्याकु",
        "genitive_f": "क्याकी",
        "genitive_pl": "क्याका",
        "ablative": "क्या बटी",
        "locative": "क्या मा",
        "english": "What / Which"
    },
    "indefinite_animate": {
        "direct": "कोइ / क्वी",
        "ergative": "कै न / कैले",
        "dative": "कैते / कैकणी",
        "instrumental": "कै सेती",
        "genitive_m": "कैको",
        "genitive_f": "कैकी",
        "genitive_pl": "कैका",
        "ablative": "कै बटी",
        "locative": "कै मा",
        "english": "Someone / Anyone"
    },
    "indefinite_inanimate": {
        "direct": "क्यै / कथै / कुछ",
        "ergative": "क्यै न",
        "dative": "क्यैते",
        "instrumental": "क्यै सेती",
        "genitive_m": "क्यैको",
        "genitive_f": "क्यैकी",
        "genitive_pl": "क्यैका",
        "ablative": "क्यै बटी",
        "locative": "क्यै मा",
        "english": "Something / Anything"
    },
    "reflexive": {
        "direct": "आप / अपु / खुद",
        "ergative": "आपु न / अपने",
        "dative": "अपूते / अपुकै",
        "instrumental": "आपु सेती",
        "genitive_m": "अपणो / अपुनो / आपु / म्यारु",
        "genitive_f": "अपणी / अपुनी",
        "genitive_pl": "अपणा / अपुना",
        "ablative": "आपु बटी",
        "locative": "आपु मा",
        "english": "Oneself / Own (reflexive)"
    },
    "reciprocal": {
        "direct": "एक-दूसरो / आपस",
        "ergative": "एक-दूसरान",
        "dative": "एक-दूसरा ते / आपस मा",
        "instrumental": "एक-दूसरा सेती",
        "genitive_m": "एक-दूसरा को / आपस को",
        "genitive_f": "एक-दूसरा की",
        "genitive_pl": "एक-दूसरा का",
        "ablative": "एक-दूसरा बटी",
        "locative": "आपस मा",
        "english": "Each other / One another"
    }
}


def get_pronoun_form(person_key: str, case: str = "direct") -> str:
    """Retrieves the conjugated pronominal form by person key and grammatical case."""
    p_data = GARHWALI_PRONOUNS_TABLE.get(person_key, {})
    return p_data.get(case, p_data.get("direct", ""))


def decline_pronoun(
    pronoun_key: str,
    case: str = "direct",
    dialect: str = "srinagariya"
) -> str:
    """
    Returns the exact case-declined form of any Garhwali pronoun for a given dialect.
    """
    key = pronoun_key.lower().strip()
    p_entry = GARHWALI_PRONOUNS_TABLE.get(key)
    if not p_entry:
        for k, v in GARHWALI_PRONOUNS_TABLE.items():
            if key in v.get("direct", "").split(" / "):
                p_entry = v
                break
    if not p_entry:
        return pronoun_key

    raw_val = p_entry.get(case.lower(), p_entry.get("direct", ""))
    options = [opt.strip() for opt in raw_val.split(" / ")]
    d_low = dialect.lower()

    if "salani" in d_low:
        for opt in options:
            if opt.endswith("ले") or "मी" in opt or "म्या" in opt:
                return opt
    elif "rathwali" in d_low or "tehri" in d_low:
        for opt in options:
            if opt.endswith("कु") or opt.endswith("रु") or "मूकै" in opt:
                return opt

    return options[0]


def get_demonstrative(proximity: str = "proximate", case: str = "direct", number: str = "sg") -> str:
    """
    Returns demonstrative pronoun (proximate 'यो', remote 'वो', plural 'ये'/'वे').
    """
    is_pl = str(number).lower() in ("pl", "plural", "2")
    if is_pl:
        key = "3pl"
    elif proximity.lower().startswith("prox") or proximity.lower() in ("near", "this"):
        key = "3sg_near"
    else:
        key = "3sg_far"
    return decline_pronoun(key, case=case)


def get_indefinite(animacy: str = "animate", case: str = "direct") -> str:
    """Returns indefinite pronoun ('कोइ' for someone, 'क्यै' for something)."""
    key = "indefinite_animate" if animacy.lower().startswith("anim") or animacy.lower() == "person" else "indefinite_inanimate"
    return decline_pronoun(key, case=case)


def get_relative_pair(clause_type: str = "entity") -> Tuple[str, str]:
    """
    Returns correlative pairs:
    - entity: ('जो', 'सो')
    - time: ('जब', 'तब')
    - place: ('जख', 'तख')
    - manner: ('जनि', 'तनि')
    - quantity: ('जतुका', 'वतुका')
    """
    t = clause_type.lower()
    if t in ("time", "temporal"):
        return ("जब", "तब")
    elif t in ("place", "spatial", "locative"):
        return ("जख", "तख")
    elif t in ("manner", "modal"):
        return ("जनि", "तनि")
    elif t in ("quantity", "amount"):
        return ("जतुका", "वतुका")
    return ("जो", "सो")


def list_all_pronouns() -> List[str]:
    """Returns list of all registered pronoun keys in the Garhwali system."""
    return list(GARHWALI_PRONOUNS_TABLE.keys())
