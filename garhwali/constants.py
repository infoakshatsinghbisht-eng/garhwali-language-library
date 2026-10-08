# -*- coding: utf-8 -*-
"""Garhwali Language Constants and Phoneme Definitions."""

GARHWALI_VOWELS = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", "अं", "अः"]
GARHWALI_MATRAS = ["ा", "ि", "ी", "ु", "ू", "ृ", "े", "ै", "ो", "ौ", "ं", "ः", "ँ", "्"]

GARHWALI_CONSONANTS = [
    "क", "ख", "ग", "घ", "ङ",
    "च", "छ", "ज", "झ", "ञ",
    "ट", "ठ", "ड", "ढ", "ण",
    "त", "थ", "द", "ध", "न",
    "प", "फ", "ब", "भ", "म",
    "य", "र", "ल", "व", "श", "ष", "स", "ह",
    "क्ष", "त्र", "ज्ञ", "ड़", "ढ़"
]

from enum import Enum
from typing import Dict, List, Optional


# ISO and Linguistic Metadata
ISO_639_3 = "gbm"
ISO_639_NAME = "Garhwali"
NATIVE_NAME = "गढ़वाली"

# Calendar Constants
DAYS_OF_WEEK = [
    "ऐतबार / आईतबार",   # Sunday
    "सोमबार",            # Monday
    "मंगलबार",           # Tuesday
    "बुधबार",            # Wednesday
    "बिपै / बृहस्पतबार", # Thursday
    "सुक्रबार",          # Friday
    "सनिच्चर / सनीबार",  # Saturday
]


class Gender(str, Enum):
    """Grammatical gender in Garhwali."""
    MASCULINE = "m"
    FEMININE = "f"
    NEUTER = "n"


class GrammaticalNumber(str, Enum):
    """Grammatical number in Garhwali."""
    SINGULAR = "sg"
    PLURAL = "pl"


class Tense(str, Enum):
    """Grammatical tenses in Garhwali."""
    PRESENT = "present"
    PAST = "past"
    FUTURE = "future"
    CONTINUOUS = "continuous"
    PERFECT = "perfect"


class PartOfSpeech(str, Enum):
    """Part-of-Speech categories."""
    NOUN = "noun"
    PRONOUN = "pronoun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    POSTPOSITION = "postposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"
    PARTICLE = "particle"


class Script(str, Enum):
    """Supported scripts for Garhwali."""
    DEVANAGARI = "devanagari"
    LATIN = "latin"


class Dialect(str, Enum):
    """Dialect zones of the Garhwali language."""
    SRINAGARIYA = "srinagariya"          # Standard Pauri Garhwal
    RATHWALI = "rathwali"                # Eastern Pauri / Rath region
    TEHRI = "tehri"                      # Tehri Garhwal & Bhagirathi Valley
    SALANI = "salani"                    # Southern Pauri / Kotdwar
    BADHANI = "badhani"                  # Chamoli / Alaknanda Valley
    JAUNSARI_BORDER = "jaunsari_border"  # Uttarkashi / Rawalti affinity


GARHWALI_DIALECTS = {
    "srinagariya": "Srinagariya (Standard Pauri Garhwal)",
    "rathwali": "Rathwali (Eastern Pauri / Tehri border)",
    "tehri": "Tehri / Gangapariya (Tehri Garhwal)",
    "salani": "Salani (Southern Pauri / Kotdwar)",
    "badhani": "Badhani / Chamoli (Chamoli / Alaknanda Valley)",
    "jaunsari_border": "Jaunsari / Rawalti affinity (Uttarkashi border)"
}

DEVANAGARI_TO_LATIN_MAP = {
    "अ": "a", "आ": "aa", "इ": "i", "ई": "ee", "उ": "u", "ऊ": "oo", "ऋ": "ri",
    "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au", "अं": "an", "अः": "ah", "ँ": "n",
    "क": "ka", "ख": "kha", "ग": "ga", "घ": "gha", "ङ": "nga",
    "च": "cha", "छ": "chha", "ज": "ja", "झ": "jha", "ञ": "nya",
    "ट": "ta", "ठ": "tha", "ड": "da", "ढ": "dha", "ण": "na",
    "त": "ta", "थ": "tha", "द": "da", "ध": "dha", "न": "na",
    "प": "pa", "फ": "pha", "ब": "ba", "भ": "bha", "म": "ma",
    "य": "ya", "र": "ra", "ल": "la", "व": "va",
    "श": "sha", "ष": "sha", "स": "sa", "ह": "ha",
    "क्ष": "ksha", "त्र": "tra", "ज्ञ": "gya", "ड़": "ra", "ढ़": "rha",
    "ा": "aa", "ि": "i", "ी": "ee", "ु": "u", "ू": "oo", "ृ": "ri",
    "े": "e", "ै": "ai", "ो": "o", "ौ": "au", "ं": "n", "ः": "h", "्": ""
}

LATIN_TO_DEVANAGARI_MAP = {
    "aa": "आ", "ee": "ई", "oo": "ऊ", "ai": "ऐ", "au": "औ",
    "ka": "क", "kha": "ख", "ga": "ग", "gha": "घ",
    "cha": "च", "chha": "छ", "ja": "ज", "jha": "झ",
    "ta": "त", "tha": "थ", "da": "द", "dha": "ध", "na": "न",
    "pa": "प", "pha": "फ", "ba": "ब", "bha": "भ", "ma": "म",
    "ya": "य", "ra": "र", "la": "ल", "va": "व", "wa": "व",
    "sha": "श", "sa": "स", "ha": "ह",
    "a": "अ", "i": "इ", "u": "उ", "e": "ए", "o": "ओ"
}

GARHWALI_STOPWORDS = {
    "छ", "छन", "छी", "छ्या", "छूँ", "छा", "मा", "माझ", "बटि", "से", "तैं",
    "कणी", "कथै", "कु", "की", "का", "को", "दगड़", "सती", "यों", "वो",
    "ऊ", "मैं", "हम", "तू", "तुम", "अपण", "अपुण", "ना", "नि", "नी", "झनि"
}
