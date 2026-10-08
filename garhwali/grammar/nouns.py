# -*- coding: utf-8 -*-
"""Garhwali Noun Declension and Case Inflection Engine."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

class GarhwaliNoun:
    def __init__(self, lemma: str, gender: str = "m", english: Optional[str] = None, hindi: Optional[str] = None):
        self.lemma = lemma.strip()
        self.gender = gender.lower()
        self.english = english
        self.hindi = hindi

    def declensions(self) -> Dict[str, str]:
        """Returns the full 8-case direct and oblique declension table."""
        root = self.lemma
        forms = {}
        if self.gender == "m":
            forms["direct_sg"] = root
            forms["direct_pl"] = root + "ों" if not (root.endswith("ा") or root.endswith("ो") or root.endswith("ु")) else root[:-1] + "ा"
            forms["oblique_sg"] = root[:-1] + "ा" if (root.endswith("ो") or root.endswith("ु")) else root
            forms["oblique_pl"] = root[:-1] + "ौं" if (root.endswith("ा") or root.endswith("ो") or root.endswith("ु")) else root + "ौं"
            forms["ergative_sg"] = forms["oblique_sg"] + "ले"
            forms["ergative_pl"] = forms["oblique_pl"] + "ले"
            forms["accusative_dative"] = forms["oblique_sg"] + " तैं"
            forms["instrumental"] = forms["oblique_sg"] + " सेती"
            forms["ablative"] = forms["oblique_sg"] + " बटी"
            forms["genitive_m"] = forms["oblique_sg"] + " कु"
            forms["genitive_f"] = forms["oblique_sg"] + " की"
            forms["locative"] = forms["oblique_sg"] + " मा"
            forms["vocative_sg"] = "हे " + forms["oblique_sg"] + "ा"
        else: # Feminine
            forms["direct_sg"] = root
            forms["direct_pl"] = root + "याँ" if root.endswith("ी") else root + "ाँ"
            forms["oblique_sg"] = root
            forms["oblique_pl"] = root[:-1] + "यौं" if root.endswith("ी") else root + "ौं"
            forms["ergative_sg"] = forms["oblique_sg"] + "ले"
            forms["ergative_pl"] = forms["oblique_pl"] + "ले"
            forms["accusative_dative"] = forms["oblique_sg"] + " तैं"
            forms["instrumental"] = forms["oblique_sg"] + " सेती"
            forms["ablative"] = forms["oblique_sg"] + " बटी"
            forms["genitive_m"] = forms["oblique_sg"] + " कु"
            forms["genitive_f"] = forms["oblique_sg"] + " की"
            forms["locative"] = forms["oblique_sg"] + " मा"
            forms["vocative_sg"] = "हे " + forms["oblique_sg"] + "े"
        return forms


def pluralize(noun: str, gender: Optional[Union[str, Any]] = None) -> str:
    """
    Pluralizes a Garhwali noun according to authentic morphological rules:
    - Masculine ending in 'ो' (-o) or 'ु' (-u) changes to 'ा' (-a): घ्वड़ो -> घ्वड़ा, नौनू -> नौना
    - Feminine ending in 'ी' (-ee) or 'ि' (-i) adds 'यां' (-yan): नौनी -> नौनियां, डाली -> डालियां
    - Consonant-ending nouns generally remain invariant in direct nominative or add '-न': घर -> घर / घरन
    """
    if not noun:
        return ""
    w = noun.strip()
    if w.endswith("ो") or w.endswith("ु"):
        return w[:-1] + "ा"
    if w.endswith("ी"):
        return w[:-1] + "ियां"
    if w.endswith("ि"):
        return w[:-1] + "ियां"
    if w.endswith("ा"):
        return w  # Many -a masculine nouns are invariant or pluralized via context
    # Consonant ending direct plural
    return w


def to_feminine(noun: str) -> str:
    """
    Converts masculine Garhwali noun to feminine form:
    - Ending in 'ो' (-o) or 'ा' (-a) changes to 'ी' (-i): बकरो -> बकरी, छोरो -> छोरी, नौना -> नौनी
    - Consonants often take 'णी' or 'इ': बामण -> बामणी, स्यार -> स्यारणि
    """
    if not noun:
        return ""
    w = noun.strip()
    if w.endswith("ो") or w.endswith("ा") or w.endswith("ु"):
        return w[:-1] + "ी"
    if w.endswith("ल") or w.endswith("र") or w.endswith("ण") or w.endswith("न"):
        return w + "णी"
    return w + "ी"


def to_masculine(noun: str) -> str:
    """
    Converts feminine Garhwali noun to masculine base form:
    - Ending in 'ी' (-i) changes to 'ो' (-o) or 'ा' (-a): बकरी -> बकरो, छोरी -> छोरो, नौनी -> नौना
    """
    if not noun:
        return ""
    w = noun.strip()
    if w.endswith("णी"):
        return w[:-2]
    if w.endswith("ी"):
        return w[:-1] + "ो"
    return w


def to_oblique(noun: str, number: str = "sg") -> str:
    """
    Generates the oblique stem of a Garhwali noun before postposition attachment:
    - Masculine in 'ो'/'ु' becomes 'ा': घ्वड़ो -> घ्वड़ा (घ्वड़ा मा)
    - Plural oblique adds 'ौं' / 'न': घर -> घरौं, घ्वड़ा -> घ्वड़ौं
    """
    if not noun:
        return ""
    w = noun.strip()
    is_pl = str(number).lower() in ("pl", "plural", "2")
    if is_pl:
        if w.endswith("ी"):
            return w[:-1] + "ियौं"
        if w.endswith("ा") or w.endswith("ो") or w.endswith("ु"):
            return w[:-1] + "ौं"
        return w + "ौं"
    else:
        if w.endswith("ो") or w.endswith("ु"):
            return w[:-1] + "ा"
        return w


def make_diminutive(noun: str) -> str:
    """Generates affectionate/diminutive form (नौन -> नौनू, डाली -> डालुली, छ्वटो -> छ्वटू)."""
    if not noun:
        return ""
    w = noun.strip()
    if w.endswith("ो") or w.endswith("ा"):
        return w[:-1] + "ू"
    if w.endswith("ी"):
        return w[:-1] + "ुली"
    return w + "ू"


def make_augmentative(noun: str) -> str:
    """Generates augmentative/crude form (डांडा -> डांडट, ढुंगो -> ढुंगोट)."""
    if not noun:
        return ""
    w = noun.strip()
    if w.endswith("ो") or w.endswith("ा"):
        return w[:-1] + "ोट"
    return w + "ा"


def decline_noun(
    noun: str,
    gender: Optional[Union[str, Any]] = "m",
    number: Optional[Union[str, Any]] = "sg"
) -> Dict[str, str]:
    """
    Declines any Garhwali noun across all 8 grammatical cases.
    """
    g_str = "f" if str(gender).lower() in ("f", "feminine", "gender.feminine") else "m"
    n_obj = GarhwaliNoun(noun, gender=g_str)
    return n_obj.declensions()

CORE_GARHWALI_NOUNS = [
    GarhwaliNoun("नौन", "m", english="boy", hindi="लड़का"),
    GarhwaliNoun("नौनी", "f", english="girl", hindi="लड़की"),
    GarhwaliNoun("घौर", "m", english="house", hindi="घर"),
    GarhwaliNoun("गौं", "m", english="village", hindi="गाँव"),
    GarhwaliNoun("डांडा", "m", english="mountain", hindi="पहाड़"),
    GarhwaliNoun("धार", "f", english="mountain ridge", hindi="पहाड़ की चोटी"),
    GarhwaliNoun("गाड़", "f", english="river", hindi="नदी"),
    GarhwaliNoun("पाणि", "m", english="water", hindi="पानी"),
    GarhwaliNoun("ब्वै", "f", english="mother", hindi="माँ"),
    GarhwaliNoun("बुबा", "m", english="father", hindi="पिता"),
    GarhwaliNoun("दादू", "m", english="elder brother", hindi="बड़ा भाई"),
    GarhwaliNoun("दिदी", "f", english="elder sister", hindi="बड़ी बहन"),
    GarhwaliNoun("भुला", "m", english="younger brother", hindi="छोटा भाई"),
    GarhwaliNoun("भुली", "f", english="younger sister", hindi="छोटी बहन"),
    GarhwaliNoun("बूबू", "m", english="grandfather", hindi="दादा जी"),
    GarhwaliNoun("बौजी", "f", english="grandmother", hindi="दादी जी"),
    GarhwaliNoun("कुकुर", "m", english="dog", hindi="कुत्ता"),
    GarhwaliNoun("बिलाव", "m", english="cat", hindi="बिल्ली"),
    GarhwaliNoun("गौई", "f", english="cow", hindi="गाय"),
    GarhwaliNoun("बल्द", "m", english="ox", hindi="बैल"),
    GarhwaliNoun("बाखरि", "f", english="goat", hindi="बकरी"),
    GarhwaliNoun("भात", "m", english="rice", hindi="चावल / भात"),
    GarhwaliNoun("रोटी", "f", english="bread", hindi="रोटी"),
    GarhwaliNoun("च्या", "f", english="tea", hindi="चाय"),
    GarhwaliNoun("दूद", "m", english="milk", hindi="दूध"),
    GarhwaliNoun("घ्यू", "m", english="ghee", hindi="घी"),
    GarhwaliNoun("गूर", "m", english="jaggery", hindi="गुड़"),
    GarhwaliNoun("काफल", "m", english="bayberry", hindi="काफल"),
    GarhwaliNoun("बुरांस", "m", english="rhododendron", hindi="बुरांश"),
    GarhwaliNoun("बाट", "m", english="path", hindi="रास्ता"),
    GarhwaliNoun("बदळ", "m", english="cloud", hindi="बादल"),
    GarhwaliNoun("घाम", "f", english="sunlight", hindi="धूप"),
    GarhwaliNoun("ह्यूंद", "m", english="snow", hindi="बर्फ"),
    GarhwaliNoun("बौण", "m", english="forest", hindi="जंगल")
]
