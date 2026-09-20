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
