# -*- coding: utf-8 -*-
"""Garhwali Verb Conjugation Engine."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

class GarhwaliVerb:
    def __init__(self, root: str, english: str, hindi: str):
        self.root = root
        self.english = english
        self.hindi = hindi

    def conjugate(self) -> Dict[str, Any]:
        r = self.root
        past_m_sg = r + "्यो" if r != "जा" else "ग्यो"
        past_f_sg = r + "्यी" if r != "जा" else "ग्यी"
        past_pl = r + "्या" if r != "जा" else "ग्या"
        return {
            "infinitive": r + "ण" if not r.endswith("ण") else r,
            "present_habitual": {
                "1sg_m": r + "दू छूँ", "1sg_f": r + "दी छूँ", "1pl": r + "दा छा",
                "2sg_m": r + "द छै", "2sg_f": r + "दी छै", "2pl": r + "दा छा",
                "3sg_m": r + "दु छ", "3sg_f": r + "दी छ", "3pl": r + "दा छन",
            },
            "present_continuous": {
                "1sg_m": r + "णू छूँ", "1sg_f": r + "णी छूँ", "1pl": r + "णा छा",
                "2sg_m": r + "णू छै", "2sg_f": r + "णी छै", "2pl": r + "णा छा",
                "3sg_m": r + "णू छ", "3sg_f": r + "णी छ", "3pl": r + "णा छन",
            },
            "past_simple": {
                "1sg_m": past_m_sg + " छियूँ", "1sg_f": past_f_sg + " छियूँ", "1pl": past_pl + " छिया",
                "2sg_m": past_m_sg + " छिये", "2sg_f": past_f_sg + " छिये", "2pl": past_pl + " छिया",
                "3sg_m": past_m_sg + " छी", "3sg_f": past_f_sg + " छी", "3pl": past_pl + " छ्या",
            },
            "future": {
                "1sg_m": r + "लो", "1sg_f": r + "ली", "1pl": r + "ला",
                "2sg_m": r + "ले", "2sg_f": r + "ली", "2pl": r + "ला",
                "3sg_m": r + "लो", "3sg_f": r + "ली", "3pl": r + "ला",
            },
            "imperative": {
                "informal": r, "polite": r + "या / " + r + "ओ",
                "prohibitive_informal": "झनि " + r, "prohibitive_polite": "झनि " + r + "या"
            }
        }

CORE_GARHWALI_VERBS = [
    GarhwaliVerb("कर", "to do", "करना"),
    GarhwaliVerb("जा", "to go", "जाना"),
    GarhwaliVerb("आ", "to come", "आना"),
    GarhwaliVerb("खा", "to eat", "खाना"),
    GarhwaliVerb("पी", "to drink", "पीना"),
    GarhwaliVerb("बोल", "to speak / say", "बोलना"),
    GarhwaliVerb("सुण", "to hear / listen", "सुनना"),
    GarhwaliVerb("देख", "to see / look", "देखना"),
    GarhwaliVerb("रै", "to live / stay", "रहना"),
    GarhwaliVerb("चल", "to walk / move / work", "चलना"),
    GarhwaliVerb("रुक", "to stop / wait", "रुकना"),
    GarhwaliVerb("सो", "to sleep", "सोना"),
    GarhwaliVerb("उठ", "to wake up / rise", "उठना"),
    GarhwaliVerb("बैठ", "to sit", "बैठना"),
    GarhwaliVerb("लिख", "to write", "लिखना"),
    GarhwaliVerb("पढ़", "to read / study", "पढ़ना"),
    GarhwaliVerb("सीख", "to learn", "सीखना"),
    GarhwaliVerb("दे", "to give", "देना"),
    GarhwaliVerb("ले", "to take", "लेना"),
    GarhwaliVerb("बला", "to call / summon", "बुलाना"),
    GarhwaliVerb("बता", "to tell / explain", "बताना"),
    GarhwaliVerb("मदद कर", "to help", "मदद करना"),
    GarhwaliVerb("खेल", "to play", "खेलना"),
    GarhwaliVerb("गा", "to sing", "गाना"),
    GarhwaliVerb("नाच", "to dance", "नाचना"),
    GarhwaliVerb("हँस", "to laugh", "हँसना"),
    GarhwaliVerb("रो", "to cry / weep", "रोना")
]
