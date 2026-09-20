# -*- coding: utf-8 -*-
"""Garhwali Noun Declension and Case Inflection Engine."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

class GarhwaliNoun:
    def __init__(self, lemma: str, gender: str = "m", english: Optional[str] = None, hindi: Optional[str] = None):
        self.lemma = lemma
        self.gender = gender.lower()
        self.english = english
        self.hindi = hindi

    def declensions(self) -> Dict[str, str]:
        root = self.lemma
        forms = {}
        if self.gender == "m":
            forms["direct_sg"] = root
            forms["direct_pl"] = root + "ों" if not root.endswith("ों") else root
            forms["oblique_sg"] = root + "ा" if root.endswith("ो") else root
            forms["oblique_pl"] = root + "ौं"
            forms["locative"] = root + "मा"
            forms["ablative"] = root + "बटि"
            forms["dative"] = root + "कणी"
            forms["genitive"] = root + "कु"
            forms["instrumental"] = root + "ले"
        else:
            forms["direct_sg"] = root
            forms["direct_pl"] = root + "याँ" if not root.endswith("याँ") else root
            forms["oblique_sg"] = root
            forms["oblique_pl"] = root + "यौं"
            forms["locative"] = root + "मा"
            forms["ablative"] = root + "बटि"
            forms["dative"] = root + "कणी"
            forms["genitive"] = root + "की"
            forms["instrumental"] = root + "ले"
        return forms

CORE_GARHWALI_NOUNS = [
    GarhwaliNoun("बाबु", "m", "father", "पिता"),
    GarhwaliNoun("ईजा", "f", "mother", "माँ"),
    GarhwaliNoun("दाज्यू", "m", "elder brother", "बड़ा भाई"),
    GarhwaliNoun("भै", "m", "younger brother", "छोटा भाई"),
    GarhwaliNoun("दीदी", "f", "elder sister", "बड़ी बहन"),
    GarhwaliNoun("बौ", "f", "younger sister / daughter-in-law", "छोटी बहन / बहू"),
    GarhwaliNoun("बूबू", "m", "grandfather", "दादाजी"),
    GarhwaliNoun("आमा", "f", "grandmother", "दादीजी"),
    GarhwaliNoun("नान्तिन", "m", "children / kid", "बच्चे"),
    GarhwaliNoun("छ्वारो", "m", "boy", "लड़का"),
    GarhwaliNoun("छ्वारी", "f", "girl", "लड़की"),
    GarhwaliNoun("घर", "m", "house / home", "घर"),
    GarhwaliNoun("गाँव", "m", "village", "गाँव"),
    GarhwaliNoun("बाटो", "m", "way / road / path", "रास्ता"),
    GarhwaliNoun("पाणि", "m", "water", "पानी"),
    GarhwaliNoun("भात", "m", "cooked rice / food", "भात / भोजन"),
    GarhwaliNoun("चाह", "f", "tea", "चाय"),
    GarhwaliNoun("पहाड़", "m", "mountain", "पहाड़"),
    GarhwaliNoun("जाड़", "m", "cold / winter", "ठंड / शीत"),
    GarhwaliNoun("घाम", "m", "sunshine / heat", "धूप"),
    GarhwaliNoun("बरखा", "f", "rain", "बारिश"),
    GarhwaliNoun("दगड़्या", "m", "friend / companion", "मित्र / साथी"),
    GarhwaliNoun("डांडा", "m", "mountain ridge / peak", "पहाड़ की चोटी"),
    GarhwaliNoun("गधेरा", "m", "mountain stream / rivulet", "पहाड़ी नाला"),
    GarhwaliNoun("नौणा", "m", "spring / fresh water source", "प्राकृतिक जल स्रोत"),
    GarhwaliNoun("खेत", "m", "terrace farm / field", "सीढ़ीदार खेत"),
    GarhwaliNoun("रुप्या", "m", "money / rupee", "रुपया / धन"),
    GarhwaliNoun("अस्पताल", "m", "hospital", "अस्पताल"),
    GarhwaliNoun("दवाई", "f", "medicine", "दवा"),
    GarhwaliNoun("किताब", "f", "book", "पुस्तक"),
    GarhwaliNoun("स्कूल", "m", "school", "विद्यालय")
]
