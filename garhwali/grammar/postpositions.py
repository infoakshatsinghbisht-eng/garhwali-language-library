# -*- coding: utf-8 -*-
"""Garhwali Postpositions and Case Markers."""

from dataclasses import dataclass
from typing import Dict, List, Optional

GARHWALI_POSTPOSITIONS = {
    "locative": {
        "markers": ["मा", "माझ", "भीतर", "पर", "माथ"],
        "meaning_hi": "में / पर / अंदर", "meaning_en": "in / on / inside / upon"
    },
    "ablative": {
        "markers": ["बटि", "से", "ले"],
        "meaning_hi": "से (स्थान या समय से)", "meaning_en": "from / since"
    },
    "dative_accusative": {
        "markers": ["कणी", "कथै", "तैं", "कै"],
        "meaning_hi": "को / के लिए", "meaning_en": "to / for / towards"
    },
    "genitive": {
        "markers": ["को", "का", "की", "क", "रो", "रा", "री"],
        "meaning_hi": "का / के / की", "meaning_en": "of ('s)"
    },
    "instrumental": {
        "markers": ["सेती", "ले", "द्वारा"],
        "meaning_hi": "से / के द्वारा", "meaning_en": "with / by"
    },
    "ergative": {
        "markers": ["न", "ले"],
        "meaning_hi": "ने (भूतकाल)", "meaning_en": "by (agentive past)"
    }
}



@dataclass
class CaseMarker:
    name: str
    garhwali: str
    meaning_hi: str
    meaning_en: str
    allomorphs: List[str]


CASE_MARKERS: Dict[str, CaseMarker] = {
    "nominative": CaseMarker(
        name="nominative",
        garhwali="",
        meaning_hi="ने (अप्रत्यक्ष / शून्य)",
        meaning_en="Direct (subject)",
        allomorphs=[""]
    ),
    "ergative": CaseMarker(
        name="ergative",
        garhwali="न / ले",
        meaning_hi="ने (सकर्मक भूतकाल)",
        meaning_en="by / agentive ergative",
        allomorphs=["न", "ले"]
    ),
    "accusative_dative": CaseMarker(
        name="accusative_dative",
        garhwali="ते / तैं",
        meaning_hi="को / के लिए",
        meaning_en="to / for / direct/indirect object",
        allomorphs=["ते", "तैं", "कणी", "कथै"]
    ),
    "instrumental": CaseMarker(
        name="instrumental",
        garhwali="सेती / ले",
        meaning_hi="से / के द्वारा",
        meaning_en="by means of / with",
        allomorphs=["सेती", "ले", "द्वारा"]
    ),
    "ablative": CaseMarker(
        name="ablative",
        garhwali="बटी / से",
        meaning_hi="से (अलगाव / स्थान से)",
        meaning_en="from / since",
        allomorphs=["बटी", "बटि", "से"]
    ),
    "genitive": CaseMarker(
        name="genitive",
        garhwali="कु / को / का / की",
        meaning_hi="का / के / की",
        meaning_en="of / 's",
        allomorphs=["कु", "को", "का", "की"]
    ),
    "locative": CaseMarker(
        name="locative",
        garhwali="मा / पर",
        meaning_hi="में / पर",
        meaning_en="in / on / upon",
        allomorphs=["मा", "म", "पर", "माथ", "भीतर"]
    ),
    "associative": CaseMarker(
        name="associative",
        garhwali="दगड़ / दगड़ी",
        meaning_hi="के साथ / संग",
        meaning_en="with / along with",
        allomorphs=["दगड़", "दगड़ी", "साथ"]
    )
}


def get_marker(case_name: str) -> Optional[str]:
    """Get the primary postposition marker for a grammatical case."""
    key = case_name.lower().strip()
    if key in CASE_MARKERS:
        return CASE_MARKERS[key].allomorphs[0]
    for k, v in CASE_MARKERS.items():
        if key in k or key in v.name:
            return v.allomorphs[0]
    return None


def attach_case(noun: str, case_name: str, number: str = "sg") -> str:
    """
    Attaches a postposition marker to a noun with correct Garhwali oblique inflection.
    Example:
        attach_case("घ्वड़ो", "locative") -> "घ्वड़ा मा"
        attach_case("घर", "ablative") -> "घर बटी"
        attach_case("राम", "ergative") -> "राम न"
    """
    from garhwali.grammar.nouns import to_oblique
    obl = to_oblique(noun, number=number)
    marker = get_marker(case_name)
    if not marker:
        return obl
    return f"{obl} {marker}"

