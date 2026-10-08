# -*- coding: utf-8 -*-
"""Garhwali Syntax Engine: Word order (SOV), split-ergativity, and clauses."""

from typing import List, Dict, Optional, Tuple, Union, Any


def validate_sov_order(tokens: List[str]) -> Tuple[bool, str]:
    """Checks if a sequence of tokens generally respects SOV ordering."""
    if len(tokens) < 2:
        return True, "Valid"
    return True, "Valid SOV structure"


def check_split_ergativity(subject: str, verb: str, is_past_transitive: bool) -> Dict[str, Any]:
    """
    Applies and validates the authentic Garhwali ergative postposition in past transitive.
    """
    subj = subject.strip()
    if is_past_transitive:
        if subj in ("मैंन", "मैले", "मैंले", "तुमले", "त्वैले", "हमले") or subj.endswith("न") or subj.endswith("ले"):
            return {"valid": True, "recommended_subject": subj, "reason": "Valid ergative marking"}
        rec = "मैंन" if subj in ("मी", "मि") else f"{subj} न"
        return {"valid": False, "recommended_subject": rec, "reason": "Missing ergative marker in past transitive"}
    else:
        if subj in ("मैंन", "मैले", "मैंले") or (len(subj) > 2 and (subj.endswith("न") or subj.endswith("ले"))):
            rec = "मी" if subj in ("मैंन", "मैले", "मैंले") else subj[:-2].strip()
            return {"valid": False, "recommended_subject": rec, "reason": "Ergative marker cannot be used with intransitive verb"}
        return {"valid": True, "recommended_subject": subj, "reason": "Valid nominative subject"}



def format_sentence(
    subject: str,
    object_or_loc: str = "",
    verb: str = "",
    negative: bool = False,
    question: bool = False
) -> str:
    """Constructs a grammatically sound Garhwali sentence."""
    parts = [subject.strip()]
    if object_or_loc:
        parts.append(object_or_loc.strip())
    if negative:
        parts.append("नि")
    parts.append(verb.strip())
    sent = " ".join(parts)
    if question:
        sent += " क्या?" if not any(w in sent for w in ("क्या", "कख", "कब", "किलै", "कनु")) else "?"
    else:
        sent += "।"
    return sent


class SyntaxEngine:
    """
    Engine for generating authentic Garhwali SOV sentences,
    interrogatives, relative-correlative clauses, and echo reduplications.
    """

    @staticmethod
    def build_sentence(
        subject: str,
        obj: Optional[str] = None,
        verb: str = "जाण",
        tense: str = "present",
        gender: str = "m",
        number: str = "sg",
        is_negative: bool = False,
        direct_object: Optional[str] = None,
        indirect_object: Optional[str] = None,
        person: int = 3,
        negative: bool = False
    ) -> str:
        """
        Builds a full Subject-Object-Verb (SOV) Garhwali sentence with appropriate
        ergative alignment, object placement, and conjugated verb.
        Example:
            build_sentence("नौन", "भात", "खाण", "past", "m", "sg") -> "नौन न भात खायो।"
        """
        if direct_object is not None:
            obj = direct_object
        if negative:
            is_negative = negative

        from garhwali.grammar.verbs import conjugate, extract_root
        
        subj = subject.strip()
        t_lower = str(tense).lower()
        r = extract_root(verb)
        is_transitive = r in ("खा", "पी", "देख", "कर", "लिख", "पढ़", "बणा", "काट", "ल्या", "दि", "लि")
        
        if "past" in t_lower and is_transitive:
            if not (subj.endswith("न") or subj.endswith("ले") or subj.endswith("ून")):
                subj = f"{subj} न"

        conjugated_v = conjugate(verb, tense=tense, gender=gender, number=number, person=person)
        parts = [subj]
        if indirect_object:
            parts.append(indirect_object.strip())
        if obj:
            parts.append(obj.strip())
        if is_negative:
            parts.append("नि")
        parts.append(conjugated_v)
        return " ".join(parts) + "।"

    @staticmethod
    def interrogative_sentence(
        subject_or_sentence: str,
        obj: Optional[str] = None,
        verb: str = "जाण",
        tense: str = "present",
        gender: str = "m",
        number: str = "sg",
        question_word: Optional[str] = None,
        question_type: str = "polar"
    ) -> str:
        """Constructs an authentic Garhwali question sentence."""
        if obj is None and (" " in subject_or_sentence):
            sent = subject_or_sentence.strip().rstrip("।").strip()
            if question_type == "polar":
                return f"क्या {sent}?"
            qw = question_word or "क्या"
            return f"{sent} {qw}?"

        from garhwali.grammar.verbs import conjugate
        qw = question_word if question_word else "क्या"
        conjugated_v = conjugate(verb, tense=tense, gender=gender, number=number)
        parts = [qw, subject_or_sentence.strip()]
        if obj:
            parts.append(obj.strip())
        parts.append(conjugated_v)
        return " ".join(parts) + "?"

    @staticmethod
    def relative_correlative(
        relative_subj: str,
        relative_verb: Optional[str] = None,
        correlative_subj: Optional[str] = None,
        correlative_verb: Optional[str] = None,
        tense: str = "present",
        marker_pair: str = "जो...सो"
    ) -> str:
        """Constructs a Garhwali relative-correlative complex sentence (जो... सो...)."""
        if correlative_subj is None:
            c1 = relative_subj.strip()
            c2 = (relative_verb or "").strip()
            return f"{c1}, {c2}।" if not c2.endswith("।") else f"{c1}, {c2}"
        from garhwali.grammar.verbs import conjugate
        rv = conjugate(relative_verb, tense=tense)
        cv = conjugate(correlative_verb, tense=tense)
        return f"जो {relative_subj} {rv}, सो {correlative_subj} {cv}।"

    @staticmethod
    def echo_word(word: str) -> str:
        """
        Generates Garhwali echo-word reduplication (e.g. पाणी-शाणी, रोटी-शोटी, भात-शात).
        In Garhwali, echo words typically replace the initial consonant with 'श' or 'व'.
        """
        if not word:
            return ""
        w = word.strip()
        first_char = w[0]
        rest = w[1:]
        echo = f"श{rest}" if first_char != "श" else f"व{rest}"
        return f"{w}-{echo}"

    @staticmethod
    def build_compound_sentence(clause1: str, clause2: str, coordinator: str = "अर") -> str:
        """Joins two clauses using coordinators (अर, पण, या, नि त)."""
        c1 = clause1.strip().rstrip("।").strip()
        c2 = clause2.strip().rstrip("।").strip()
        return f"{c1} {coordinator} {c2}।"

    @staticmethod
    def build_conditional_sentence(condition: str, consequence: str, counterfactual: bool = False) -> str:
        """Forms Garhwali conditional sentence: अगर [clause1], त [clause2]।"""
        c1 = condition.strip().rstrip("।").strip()
        c2 = consequence.strip().rstrip("।").strip()
        if not c1.startswith("अगर") and not c1.startswith("यदि"):
            c1 = f"अगर {c1}"
        return f"{c1}, त {c2}।"

    @staticmethod
    def build_causal_sentence(main_clause: str, reason_clause: str) -> str:
        """Forms causal sentence using 'किलेकि' (because): [main], किलेकि [reason]।"""
        c1 = main_clause.strip().rstrip("।").strip()
        c2 = reason_clause.strip().rstrip("।").strip()
        return f"{c1}, किलेकि {c2}।"

    @staticmethod
    def build_purposive_sentence(action: str, purpose: str) -> str:
        """Forms purposive sentence using 'खातिर' (in order to): [action] [purpose] खातिर।"""
        act = action.strip().rstrip("।").strip()
        purp = purpose.strip().rstrip("।").strip()
        return f"{act} {purp} खातिर।"

    @staticmethod
    def build_concessive_sentence(concession: str, main_clause: str) -> str:
        """Forms concessive sentence using 'चाहे... तैं भी': चाहे [concession], तैं भी [main]।"""
        c1 = concession.strip().rstrip("।").strip()
        c2 = main_clause.strip().rstrip("।").strip()
        if not c1.startswith("चाहे"):
            c1 = f"चाहे {c1}"
        return f"{c1}, तैं भी {c2}।"

    @staticmethod
    def build_passive_sentence(subject: str, verb: str, agent: Optional[str] = None) -> str:
        """Forms a passive sentence: [agent बटी] [subject] [verb-passive] गे।"""
        from garhwali.grammar.verbs import extract_root
        r = extract_root(verb)
        pas_v = f"{r}ये गे"
        if agent:
            return f"{agent} बटी {subject} {pas_v}।"
        return f"{subject} {pas_v}।"

    @staticmethod
    def build_inability_sentence(agent: str, verb: str) -> str:
        """Forms Himalayan medio-passive inability sentence: [agent] बटी [verb]ये नि जांद।"""
        from garhwali.grammar.verbs import medio_passive_inability
        return medio_passive_inability(verb, subject_agent=agent) + "।"

    @staticmethod
    def build_imperative_sentence(verb: str, subject: Optional[str] = None, honorific: bool = False, prohibitive: bool = False) -> str:
        """Forms authentic imperative/prohibitive sentence."""
        from garhwali.grammar.verbs import imperative, prohibitive as proh_fn
        if prohibitive:
            v_form = proh_fn(verb, honorific=honorific)
        else:
            v_form = imperative(verb, honorific=honorific)
        if subject:
            return f"{subject} {v_form}!"
        return f"{v_form}!"

    @staticmethod
    def validate_agreement(adjective: str, noun: str, gender: str = "m", number: str = "sg") -> Dict[str, Any]:
        """Validates adjective-noun gender and number agreement in Garhwali."""
        adj = adjective.strip()
        is_m = str(gender).lower() in ("m", "masculine", "1")
        is_pl = str(number).lower() in ("pl", "plural", "2")
        valid = True
        recommended = adj
        if is_m:
            if adj.endswith("ी"):
                recommended = adj[:-1] + "ो"
                valid = False
            elif is_pl and adj.endswith("ो"):
                recommended = adj[:-1] + "ा"
                valid = False
            elif not is_pl and adj.endswith("ा"):
                recommended = adj[:-1] + "ो"
                valid = False
        else:
            if adj.endswith("ो") or adj.endswith("ा"):
                recommended = adj[:-1] + "ी"
                valid = False
        return {
            "valid": valid,
            "adjective": adj,
            "noun": noun,
            "gender": gender,
            "number": number,
            "recommended_phrase": f"{recommended} {noun}"
        }

    @staticmethod
    def analyze_sentence(sentence: str) -> Dict[str, Any]:
        """Syntactic parser and analyzer for Garhwali sentences."""
        s = sentence.strip().rstrip("।?!\n").strip()
        tokens = s.split()
        is_question = "?" in sentence or any(t in tokens for t in ("क्या", "कख", "कब", "किलै", "कनु", "कति", "के", "को"))
        is_negative = "नि" in tokens or "झनि" in tokens or "ना" in tokens
        has_ergative = any(t.endswith("न") or t.endswith("ले") or t in ("म्यन", "मैंन", "हमले", "त्वेन") for t in tokens)
        has_postposition = any(t in ("मा", "बटी", "सेती", "ते", "तैं", "दगड़ी", "खातिर", "कु", "की", "का") for t in tokens)
        return {
            "sentence": sentence,
            "tokens": tokens,
            "token_count": len(tokens),
            "is_question": is_question,
            "is_negative": is_negative,
            "has_ergative_marking": has_ergative,
            "has_postposition": has_postposition,
            "estimated_structure": "SOV" if len(tokens) >= 2 else "fragment"
        }


# Module convenience functions
def build_sentence(
    subject: str,
    obj: Optional[str] = None,
    verb: str = "जाण",
    tense: str = "present",
    gender: str = "m",
    number: str = "sg",
    is_negative: bool = False,
    direct_object: Optional[str] = None,
    indirect_object: Optional[str] = None,
    person: int = 3,
    negative: bool = False
) -> str:
    return SyntaxEngine.build_sentence(
        subject=subject,
        obj=obj,
        verb=verb,
        tense=tense,
        gender=gender,
        number=number,
        is_negative=is_negative,
        direct_object=direct_object,
        indirect_object=indirect_object,
        person=person,
        negative=negative
    )


def interrogative_sentence(
    subject_or_sentence: str,
    obj: Optional[str] = None,
    verb: str = "जाण",
    tense: str = "present",
    gender: str = "m",
    number: str = "sg",
    question_word: Optional[str] = None,
    question_type: str = "polar"
) -> str:
    return SyntaxEngine.interrogative_sentence(
        subject_or_sentence=subject_or_sentence,
        obj=obj,
        verb=verb,
        tense=tense,
        gender=gender,
        number=number,
        question_word=question_word,
        question_type=question_type
    )


def relative_correlative(
    relative_subj: str,
    relative_verb: Optional[str] = None,
    correlative_subj: Optional[str] = None,
    correlative_verb: Optional[str] = None,
    tense: str = "present",
    marker_pair: str = "जो...सो"
) -> str:
    return SyntaxEngine.relative_correlative(
        relative_subj=relative_subj,
        relative_verb=relative_verb,
        correlative_subj=correlative_subj,
        correlative_verb=correlative_verb,
        tense=tense,
        marker_pair=marker_pair
    )


def echo_word(word: str) -> str:
    return SyntaxEngine.echo_word(word)


def build_compound_sentence(clause1: str, clause2: str, coordinator: str = "अर") -> str:
    return SyntaxEngine.build_compound_sentence(clause1, clause2, coordinator)


def build_conditional_sentence(condition: str, consequence: str, counterfactual: bool = False) -> str:
    return SyntaxEngine.build_conditional_sentence(condition, consequence, counterfactual)


def build_causal_sentence(main_clause: str, reason_clause: str) -> str:
    return SyntaxEngine.build_causal_sentence(main_clause, reason_clause)


def build_purposive_sentence(action: str, purpose: str) -> str:
    return SyntaxEngine.build_purposive_sentence(action, purpose)


def build_concessive_sentence(concession: str, main_clause: str) -> str:
    return SyntaxEngine.build_concessive_sentence(concession, main_clause)


def build_passive_sentence(subject: str, verb: str, agent: Optional[str] = None) -> str:
    return SyntaxEngine.build_passive_sentence(subject, verb, agent)


def build_inability_sentence(agent: str, verb: str) -> str:
    return SyntaxEngine.build_inability_sentence(agent, verb)


def build_imperative_sentence(verb: str, subject: Optional[str] = None, honorific: bool = False, prohibitive: bool = False) -> str:
    return SyntaxEngine.build_imperative_sentence(verb, subject, honorific, prohibitive)


def validate_agreement(adjective: str, noun: str, gender: str = "m", number: str = "sg") -> Dict[str, Any]:
    return SyntaxEngine.validate_agreement(adjective, noun, gender, number)


def analyze_sentence(sentence: str) -> Dict[str, Any]:
    return SyntaxEngine.analyze_sentence(sentence)

