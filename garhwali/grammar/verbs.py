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


def extract_root(verb: str) -> str:
    """
    Extracts the base verb root from a Garhwali infinitive or inflected form.
    Examples:
        extract_root("खाण") -> "खा"
        extract_root("जाण") -> "जा"
        extract_root("करण") -> "कर"
        extract_root("देखण") -> "देख"
    """
    if not verb:
        return ""
    v = verb.strip()
    if v.endswith("ण") or v.endswith("न"):
        return v[:-1]
    if v.endswith("णु"):
        return v[:-2]
    return v


def conjugate_to_be(
    tense: str = "present",
    person: int = 3,
    number: str = "sg",
    gender: str = "m"
) -> str:
    """
    Conjugates the Garhwali substantive auxiliary verb ('छ-' / 'to be'):
    - Present:
        1sg: छौं (I am)
        1pl: छां / छम (we are)
        2sg: छै (thou art)
        2pl: छा (you are)
        3sg: च / छ (he/she is)
        3pl: छन (they are)
    - Past:
        1sg: छयौं / छयाँ (I was)
        1pl: छया (we were)
        2sg: छये (thou wast)
        2pl: छया (you were)
        3sg m: छौ (he was), 3sg f: छी (she was)
        3pl: छया / छिन (they were)
    - Future:
        3sg m: होलु (he will be), 3sg f: होलि (she will be), 3pl: होला (they will be)
    """
    t_lower = str(tense).lower()
    is_pl = str(number).lower() in ("pl", "plural", "2")
    is_f = str(gender).lower() in ("f", "feminine")

    if "pres" in t_lower:
        if person == 1:
            return "छां" if is_pl else "छौं"
        elif person == 2:
            return "छा" if is_pl else "छै"
        else:
            return "छन" if is_pl else "च"

    elif "past" in t_lower:
        if person == 1:
            return "छया" if is_pl else "छयौं"
        elif person == 2:
            return "छया" if is_pl else "छये"
        else:
            if is_pl:
                return "छया"
            return "छी" if is_f else "छौ"

    elif "fut" in t_lower:
        if person == 1:
            return "होला" if is_pl else "होलु"
        elif person == 2:
            return "होला" if is_pl else "होला"
        else:
            if is_pl:
                return "होला"
            return "होलि" if is_f else "होलु"

    return "च"


def conjugate(
    verb: str,
    tense: str = "present",
    person: int = 3,
    number: str = "sg",
    gender: str = "m"
) -> str:
    """
    Conjugates any Garhwali verb for tense, person, number, and gender.
    """
    root = extract_root(verb)
    t_lower = str(tense).lower()
    is_pl = str(number).lower() in ("pl", "plural", "2")
    is_f = str(gender).lower() in ("f", "feminine")

    # Irregular verbs handling
    if root == "जा":
        if "past" in t_lower:
            if person == 1:
                return "गया" if is_pl else "गयूं"
            elif person == 2:
                return "गया" if is_pl else "गये"
            else:
                if is_pl:
                    return "गैन / गया"
                return "गै" if is_f else "गे / गयो"

    if "pres" in t_lower:
        aux = conjugate_to_be("present", person=person, number=number, gender=gender)
        # Habitual/Present participle stem: root + -द / -दा
        part = root + ("दी" if is_f else ("दा" if is_pl else "द"))
        return f"{part} {aux}"

    elif "past" in t_lower:
        if is_pl:
            return root + "िन" if is_f else root + "िन / या"
        return root + "ी" if is_f else root + "े / यो"

    elif "fut" in t_lower:
        if person == 1:
            return root + "ला" if is_pl else root + "लु"
        elif person == 2:
            return root + "ला"
        else:
            return root + "ला" if is_pl else (root + "लि" if is_f else root + "लु")

    elif "cont" in t_lower:
        aux = conjugate_to_be("present", person=person, number=number, gender=gender)
        return f"{root}ण बैठ्यूं {aux}" if not is_pl else f"{root}ण बैठ्यां {aux}"

    return root


def conjunctive_participle(verb: str) -> str:
    """
    Forms the Garhwali conjunctive participle (-ik / -ee-k).
    Equivalent to Hindi 'कर / करके' (खाईक, जाईक, देखिक, करिक).
    """
    root = extract_root(verb)
    if root.endswith("ा") or root.endswith("ी") or root.endswith("ू"):
        return root + "ईक"
    return root + "िक"


def causative(verb: str, degree: int = 1, grade: Optional[int] = None) -> str:
    """
    Forms 1st and 2nd degree causative verbs in Garhwali:
    - Degree 1 (-aun): खाण -> खिलौण, करण -> करौण, देखण -> दिखौण
    - Degree 2 (-vaan): खाण -> खिलवाण, करण -> करवाण, देखण -> दिखवाण
    """
    if grade is not None:
        degree = grade
    root = extract_root(verb)
    if root == "खा":
        return "खिलवाण" if degree == 2 else "खिलौण"
    elif root == "पी":
        return "पिलवाण" if degree == 2 else "पिलौण"
    elif root == "दि":
        return "दिलवाण" if degree == 2 else "दिलाउण"
    if degree == 2:
        return root + "वाण"
    return root + "ौण"



def passive(verb: str) -> str:
    """Forms passive voice verb: जाण -> जाईण, खाण -> खवाईण, करण -> कराईण."""
    root = extract_root(verb)
    return root + "ाईण"


def medio_passive_inability(verb: str, subject_agent: Optional[str] = None, dialect: str = "srinagariya") -> str:
    """
    Forms the Himalayan medio-passive construction expressing inability.
    Example: खाण -> 'नि खाये जांद' (is not able to be eaten), जाण -> 'नि जाये जांद'
    """
    root = extract_root(verb)
    if subject_agent:
        return f"{subject_agent} बटी {root}ये नि जांद"
    return f"नि {root}ये जांद"


def compound_verb(v1: str, v2: str) -> str:
    """
    Forms vector/compound verb in Garhwali:
    Examples:
        compound_verb("खाण", "हाळण") -> "खाइ-हाळण" (to finish eating up)
        compound_verb("बैठण", "जाण") -> "बैठि-जाण" (to sit down)
        compound_verb("देण", "हाळण") -> "दे-हाळण" (to give away)
    """
    r1 = extract_root(v1)
    part = r1 + "ि" if not (r1.endswith("ा") or r1.endswith("े")) else r1 + "इ"
    return f"{part}-{v2}"


def conditional(condition_or_verb: str, consequence_or_condition: str = "अगर") -> str:
    """Constructs a Garhwali conditional clause: 'अगर तू जाला त...'."""
    if " " in condition_or_verb and consequence_or_condition != "अगर":
        return f"{condition_or_verb} त {consequence_or_condition}"
    root = extract_root(condition_or_verb)
    return f"{consequence_or_condition} {root}लो त"


def imperative(verb: str, honorific: bool = False, plural: bool = False) -> str:
    """
    Generates imperative forms:
    - Familiar/informal: जा (go), खा (eat), कर (do)
    - Honorific/respectful: जावा (please go), खावा (please eat), करा (please do)
    """
    root = extract_root(verb)
    if honorific or plural:
        return root + "वा" if root.endswith("ा") else root + "ा"
    return root


def prohibitive(verb: str, honorific: bool = False, marker: str = "झनि") -> str:
    """
    Generates Garhwali prohibitive negative command with 'झनि' or 'झन':
    - झनि जा (don't go), झनि जावा (please don't go), झनि करा (please don't do)
    """
    imp = imperative(verb, honorific=honorific)
    return f"{marker} {imp}"


def modal_ability(verb: str, person: int = 3, number: str = "sg", gender: str = "M", tense: str = "present") -> str:
    """Forms modal potential 'can / able to': करि सकद (can do), खाई सकद (can eat)."""
    root = extract_root(verb)
    stem = root + "ि" if not root.endswith("ा") else root + "इ"
    is_pl = str(number).lower() in ("pl", "plural", "2")
    if is_pl:
        marker = "सकदन"
    elif str(gender).upper() in ("F", "FEMALE", "FEMININE"):
        marker = "सकदी"
    else:
        marker = "सकदू"
    return f"{stem} {marker}"


def modal_obligation(verb: str, subject: Optional[str] = None, urgency: str = "need") -> str:
    """Forms deontic modal obligation 'must / should': करणु चैं (ought to do)."""
    root = extract_root(verb)
    base = f"{root}णु चैं" if urgency == "need" else f"{root}णु च्वै"
    if subject:
        return f"{subject} {base}"
    return base


def modal_desiderative(verb: str, subject: Optional[str] = None, tense: str = "present") -> str:
    """Forms desiderative modal 'wants to': खाण चांदू (wants to eat)."""
    root = extract_root(verb)
    base = f"{root}ण चांदू"
    if subject:
        return f"{subject} {base}"
    return base


def subjunctive(verb: str, person: int = 3, number: str = "sg") -> str:
    """
    Forms the Garhwali subjunctive / optative mood:
    - 1sg: खां / जां, 1pl: खावां / जावाूं
    - 2sg: खायै / जायै, 2pl: खावा / जावा
    - 3sg: खाउ / जाउ, 3pl: खाउन / जाउन
    """
    root = extract_root(verb)
    is_pl = str(number).lower() in ("pl", "plural", "2")
    if person == 1:
        return f"{root}वां" if is_pl else f"{root}ं"
    elif person == 2:
        return f"{root}वा" if is_pl else f"{root}यै"
    else:
        return f"{root}उन" if is_pl else f"{root}उ"


def habitual_past(verb: str, gender: str = "m", number: str = "sg") -> str:
    """Forms the Garhwali habitual past: खांदो थौ (used to eat), खांदी छी."""
    root = extract_root(verb)
    is_pl = str(number).lower() in ("pl", "plural", "2")
    is_f = str(gender).lower() in ("f", "feminine")
    if is_pl:
        return f"{root}ंदा छा" if not is_f else f"{root}ंदी छन"
    return f"{root}ंदी छी" if is_f else f"{root}ंदो थौ"


def progressive(verb: str, tense: str = "present", gender: str = "m", number: str = "sg") -> str:
    """Forms continuative / progressive aspect with 'रौण' (to stay/keep doing)."""
    root = extract_root(verb)
    is_f = str(gender).lower() in ("f", "feminine")
    if "past" in str(tense).lower():
        aux = "रई" if is_f else "रौ"
    else:
        aux = "रौंद" if not is_f else "रौंदी"
    return f"{root}ंदौ {aux}"


def inceptive(verb: str, gender: str = "m", number: str = "sg") -> str:
    """Forms inceptive aspect 'began to X' with 'लगण': खाण लगिगे, जाण लगिगे."""
    root = extract_root(verb)
    is_f = str(gender).lower() in ("f", "feminine")
    aux = "लगि गै" if is_f else "लगिगे"
    return f"{root}ण {aux}"


def completive(verb: str) -> str:
    """Forms completive aspect 'finish doing X' with 'हाळण': खाइ-हाळ, काम करि-हाळ."""
    root = extract_root(verb)
    part = root + "ि" if not (root.endswith("ा") or root.endswith("े")) else root + "इ"
    return f"{part}-हाळ"


def conjugate_full_paradigm(verb: str, gender: str = "m") -> Dict[str, Dict[str, str]]:
    """
    Generates the complete 18-form standard conjugational matrix for any Garhwali verb
    across Present, Past, and Future tenses for all person-number combinations.
    """
    matrix: Dict[str, Dict[str, str]] = {}
    for tense in ("present", "past", "future"):
        matrix[tense] = {}
        for p in (1, 2, 3):
            for n in ("sg", "pl"):
                k = f"{p}{n}"
                matrix[tense][k] = conjugate(verb, tense=tense, person=p, number=n, gender=gender)
    return matrix


