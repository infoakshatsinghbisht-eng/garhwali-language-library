# -*- coding: utf-8 -*-
"""
Garhwali (गढ़वाली) Language Library.
Comprehensive NLP and Cultural Heritage toolkit for the Garhwali Language:
- 300,000+ Inflected Word Forms
- Multi-dialect Translation (Srinagariya, Rathwali, Tehri, Salani, Badhani)
- Phonetics & Syllabification
- Case Declensions & Verb Conjugations
- Himalayan Calendar, Proverbs (अखाण/पखाण), Riddles (आणा), Literature
- Voice Synthesis & SSML
"""

__version__ = "1.0.0"
__author__ = "Akshat Singh Bisht"

from .translator.engine import translate, TranslationResult
from .lexicon.dictionary import GarhwaliDictionary
from .lexicon.morphology import get_morphology_engine, MorphAnalysis
from .phonetics import devanagari_to_latin, latin_to_devanagari, syllables
from .numbers.converter import num_to_words, to_devanagari_numerals, ordinal
from .culture.calendar import GARHWALI_MONTHS, GARHWALI_RITUS, get_current_season
from .culture.festivals import list_festivals
from .culture.literature import poems, epics, authors
from .voice.engine import GarhwaliVoiceSynthesizer

# Global instances for simple top-level access
_DICT = GarhwaliDictionary()
phrases = type("Phrases", (), {"all": _DICT.all_phrases, "random": _DICT.random_phrase})()
proverbs = type("Proverbs", (), {"all": _DICT.all_proverbs, "random": _DICT.random_proverb})()
riddles = type("Riddles", (), {"all": _DICT.all_riddles, "random": _DICT.random_riddle})()

def lookup(word: str):
    return _DICT.lookup(word)

def search(query: str):
    return _DICT.search(query)

def analyze(word: str):
    engine = get_morphology_engine()
    return engine.analyze(word)

def total_word_forms() -> int:
    return get_morphology_engine().total_forms_count()

def get_months():
    return GARHWALI_MONTHS

def get_seasons():
    return GARHWALI_RITUS

__all__ = [
    "translate", "TranslationResult",
    "lookup", "search", "analyze", "total_word_forms",
    "syllables", "devanagari_to_latin", "latin_to_devanagari",
    "num_to_words", "to_devanagari_numerals", "ordinal",
    "get_months", "get_seasons", "get_current_season",
    "list_festivals", "poems", "epics", "authors",
    "phrases", "proverbs", "riddles",
    "GarhwaliVoiceSynthesizer"
]
