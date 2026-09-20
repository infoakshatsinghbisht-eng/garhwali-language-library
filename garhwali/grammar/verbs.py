# -*- coding: utf-8 -*-
"""Garhwali Verb Conjugation Engine."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

class GarhwaliVerb:
    def __init__(self, root: str, english: str, hindi: str, is_transitive: bool = True):
        self.root = root.strip()
        self.english = english
        self.hindi = hindi
        self.is_transitive = is_transitive

    def conjugate(self) -> Dict[str, Any]:
        """Generates the full aspectual, temporal, and modal conjugation matrix."""
        r = self.root
        
        # Base without trailing 'ा' for matra suffixes
        base = r[:-1] if r.endswith("ा") else r
        
        # Infinitive
        infinitive = r + "ण" if not (r.endswith("ण") or r.endswith("न")) else r
        
        # Past stem
        if r == "जा":
            past_m_sg = "गयो"
            past_f_sg = "गै"
            past_pl = "गया"
            past_1sg = "गयूं"
        elif r == "आ":
            past_m_sg = "आयो"
            past_f_sg = "आई"
            past_pl = "आया"
            past_1sg = "आयूं"
        elif r == "खा":
            past_m_sg = "खायो"
            past_f_sg = "खाई"
            past_pl = "खाया"
            past_1sg = "खायूं"
        elif r == "पी":
            past_m_sg = "पीयूं / पीयो"
            past_f_sg = "पीई"
            past_pl = "पीया"
            past_1sg = "पीयूं"
        elif r == "दि":
            past_m_sg = "दिने / दियो"
            past_f_sg = "दी"
            past_pl = "दिया"
            past_1sg = "दियूं"
        elif r == "लि":
            past_m_sg = "लिने / लियो"
            past_f_sg = "ली"
            past_pl = "लिया"
            past_1sg = "लियूं"
        elif r == "कर":
            past_m_sg = "कयो / कर्यो"
            past_f_sg = "करी"
            past_pl = "कया / कर्या"
            past_1sg = "कर्यूं"
        elif r == "रौ":
            past_m_sg = "रयो"
            past_f_sg = "रई"
            past_pl = "रया"
            past_1sg = "रयूं"
        else:
            past_m_sg = r + "्यो"
            past_f_sg = r + "ी"
            past_pl = r + "्या"
            past_1sg = r + "्यूं"

        return {
            "root": r,
            "infinitive": infinitive,
            "is_transitive": self.is_transitive,
            "present_habitual": {
                "1sg_m": r + "न्दु छौं", "1sg_f": r + "न्दी छौं", "1pl": r + "न्दा छा",
                "2sg_m": r + "न्द छै", "2sg_f": r + "न्दी छै", "2pl": r + "न्दा छा",
                "3sg_m": r + "न्दु छ", "3sg_f": r + "न्दी छ", "3pl": r + "न्दा छन"
            },
            "present_continuous": {
                "1sg_m": r + "णो छौं", "1sg_f": r + "णी छौं", "1pl": r + "णा छा",
                "2sg_m": r + "णो छै", "2sg_f": r + "णी छै", "2pl": r + "णा छा",
                "3sg_m": r + "णो छ", "3sg_f": r + "णी छ", "3pl": r + "णा छन"
            },
            "past_simple": {
                "3sg_m": past_m_sg, "3sg_f": past_f_sg, "3pl": past_pl, "1sg": past_1sg
            },
            "past_continuous": {
                "1sg_m": r + "णो छो", "1sg_f": r + "णी छी", "1pl": r + "णा छा",
                "3sg_m": r + "णो छो", "3sg_f": r + "णी छी", "3pl": r + "णा छा"
            },
            "future": {
                "1sg_m": base + "ौलो", "1sg_f": base + "ौली", "1pl": base + "ौला",
                "2sg_m": base + "ैले", "2sg_f": base + "ैली", "2pl": base + "ौला",
                "3sg_m": (r if r.endswith("ा") else r + "ा") + "लो",
                "3sg_f": (r if r.endswith("ा") else r + "ा") + "ली",
                "3pl": (r if r.endswith("ा") else r + "ा") + "ला"
            },
            "imperative": {
                "informal": r,
                "polite_formal": r + "वा" if not r.endswith("ा") else r + "या",
                "prohibition_informal": "झन् " + r,
                "prohibition_formal": "झन् " + (r + "वा" if not r.endswith("ा") else r + "या")
            },
            "conjunctive_participle": r + "क / " + r + "िक",
            "causative_1": r + "वाण",
            "causative_2": r + "वाळण"
        }

CORE_GARHWALI_VERBS = [
    GarhwaliVerb("जा", "to go", "जाना", is_transitive=False),
    GarhwaliVerb("आ", "to come", "आना", is_transitive=False),
    GarhwaliVerb("खा", "to eat", "खाना", is_transitive=True),
    GarhwaliVerb("पी", "to drink", "पीना", is_transitive=True),
    GarhwaliVerb("सुण", "to listen", "सुनना", is_transitive=True),
    GarhwaliVerb("देख", "to see", "देखना", is_transitive=True),
    GarhwaliVerb("क", "to say", "कहना", is_transitive=True),
    GarhwaliVerb("बोल", "to speak", "बोलना", is_transitive=True),
    GarhwaliVerb("कर", "to do", "करना", is_transitive=True),
    GarhwaliVerb("बौठ", "to sit", "बैठना", is_transitive=False),
    GarhwaliVerb("उठ", "to rise", "उठना", is_transitive=False),
    GarhwaliVerb("सुत", "to sleep", "सोना", is_transitive=False),
    GarhwaliVerb("हँस", "to laugh", "हँसना", is_transitive=False),
    GarhwaliVerb("रू", "to cry", "रोना", is_transitive=False),
    GarhwaliVerb("ल्या", "to bring", "लाना", is_transitive=True),
    GarhwaliVerb("दि", "to give", "देना", is_transitive=True),
    GarhwaliVerb("लि", "to take", "लेना", is_transitive=True),
    GarhwaliVerb("चल", "to walk", "चलना", is_transitive=False),
    GarhwaliVerb("दौड़", "to run", "दौड़ना", is_transitive=False),
    GarhwaliVerb("रौ", "to live / stay", "रहना", is_transitive=False),
    GarhwaliVerb("लिख", "to write", "लिखना", is_transitive=True),
    GarhwaliVerb("पढ़", "to read", "पढ़ना", is_transitive=True),
    GarhwaliVerb("सीख", "to learn", "सीखना", is_transitive=True),
    GarhwaliVerb("बणा", "to make / cook", "बनाना", is_transitive=True),
    GarhwaliVerb("काट", "to cut / harvest", "काटना", is_transitive=True),
    GarhwaliVerb("धो", "to wash", "धोना", is_transitive=True),
    GarhwaliVerb("नहा", "to bathe", "नहाना", is_transitive=False),
    GarhwaliVerb("गा", "to sing", "गाना", is_transitive=True),
    GarhwaliVerb("नाच", "to dance", "नाचना", is_transitive=False),
    GarhwaliVerb("खेल", "to play", "खेलना", is_transitive=False)
]
