# -*- coding: utf-8 -*-
"""
Garhwali (गढ़वाली) Language Library.
Comprehensive Linguistic, Computational, Cultural Heritage & Knowledge toolkit for the Garhwali Language:
- 2,390,000+ Inflected Word Forms across 5 dialects (Srinagariya, Rathwali, Tehri, Salani, Badhani)
- Multi-dialect & Pivot Neural/Rule-based Translation Engine
- Voice Synthesis, Phonetic Syllabification & SSML Generation
- Master Bibliography & Digitized Literary Corpus (80+ Canonical Books Catalogued, 13 Full Books with 3,076 Pages)
- Classical Baithki & Khadi Holi Ragas, Traditional Folk Songs, Shamanic Jagars & Digital Archives
- Folk Epics (पवाड़े / जागर), Classical Poems & Canonical Authors
- Sacred Geography & Heritage Places of Garhwal (Panch Kedar, Panch Badri, Panch Prayag, Bugyals, Historical Towns)
- Local Deities, Kshetrapals, Nagrajas & Shaktipeeths of Kedarkhand
- Garhwali Surnames, Clans, Lineages, Gotras & Social Structure
- Himalayan Ethnobotanical Flora (Sacred Trees, Alpine Herbs, Wild Fruits, Millets)
- Temple Implements, Sacred Vessels, Hawan Paraphernalia & Ritual Attire
- Himalayan Calendar, Festivals, Proverbs (अखाण/पखाण), Riddles (आणा), Phrases (मुहावरे)
- Functional Grammar, Noun Morphology, Case Markers & Verb Conjugation Engine
- Numbers, Numerals, Ordinals & Himalayan Fraction System
- Interactive Web GUI Playground & REST API Server
"""

__version__ = "1.2.0"
__author__ = "Akshat Singh Bisht"
__email__ = "infoakshatsinghbisht@gmail.com"
__maintainer__ = "Akshat Singh Bisht"
__copyright__ = "Copyright (c) 2026 Akshat Singh Bisht"

# Constants & Enums
from .constants import (
    ISO_639_3,
    ISO_639_NAME,
    NATIVE_NAME,
    Dialect,
    Script,
    PartOfSpeech,
    Tense,
    Gender,
    GrammaticalNumber,
    DAYS_OF_WEEK,
)

# Translation Subsystems
from .translator.engine import translate, TranslationResult
from .translator.pivot import PivotTranslator, pivot_translate
from .translator.llm_adapter import LLMTranslator, translate_with_llm, GARHWALI_SYSTEM_PROMPT, get_garhwali_prompt
from .translator.rule_based import apply_dialect, RuleBasedTranslator

# Lexicon & Dictionary
from .lexicon.dictionary import GarhwaliDictionary
from .lexicon.morphology import get_morphology_engine, MorphAnalysis

# Phonetics
from .phonetics import devanagari_to_latin, latin_to_devanagari, syllables

# Numbers & Fractions
from .numbers.converter import (
    num_to_words,
    words_to_num,
    to_devanagari_numerals,
    from_devanagari_numerals,
    ordinal,
    fraction,
    GARHWALI_FRACTIONS,
)

# Grammar & Morphology Engine
from .grammar.nouns import (
    pluralize,
    to_feminine,
    to_masculine,
    to_oblique,
    make_diminutive,
    make_augmentative,
    decline_noun,
)
from .grammar.postpositions import (
    CaseMarker,
    CASE_MARKERS,
    GARHWALI_POSTPOSITIONS,
    get_marker,
    attach_case,
)
from .grammar.verbs import (
    extract_root,
    conjugate_to_be,
    conjugate,
    conjunctive_participle,
    causative,
    passive,
    medio_passive_inability,
    compound_verb,
    conditional,
    imperative,
    prohibitive,
    modal_ability,
    modal_obligation,
    modal_desiderative,
    subjunctive,
    habitual_past,
    progressive,
    inceptive,
    completive,
    conjugate_full_paradigm,
)
from .grammar.syntax import (
    SyntaxEngine,
    build_sentence,
    interrogative_sentence,
    relative_correlative,
    echo_word,
    build_compound_sentence,
    build_conditional_sentence,
    build_causal_sentence,
    build_purposive_sentence,
    build_concessive_sentence,
    build_passive_sentence,
    build_inability_sentence,
    build_imperative_sentence,
    validate_agreement,
    analyze_sentence,
)
from .grammar.pronouns import (
    GARHWALI_PRONOUNS_TABLE,
    get_pronoun_form,
    decline_pronoun,
    get_demonstrative,
    get_indefinite,
    get_relative_pair,
    list_all_pronouns,
)
from .grammar.rules import (
    RuleCategory,
    GrammarRule,
    RuleRegistry,
    GARHWALI_GRAMMAR_RULES,
)

# Voice & Speech Synthesis
from .voice.synthesizer import GarhwaliVoiceSynthesizer
from .voice.engine import VoiceTranslator, VoiceTranslationResult, voice_translate

# Cultural Heritage, Literature, Folklore & Digitized Books
from .culture.calendar import GARHWALI_MONTHS, GARHWALI_RITUS, get_current_season
from .culture.festivals import list_festivals
from .culture.literature import (
    poems,
    epics,
    authors,
    FolkEpic,
    FolkPoem,
    GarhwaliAuthor,
    LiteratureTreasury,
    EPICS_DATA,
    POEMS_DATA,
    AUTHORS_DATA,
)
from .culture.bibliography import (
    GarhwaliBook,
    BibliographyTreasury,
    get_bibliography,
    search_books,
    get_book_by_id,
    get_works_in_garhwali,
    get_grammar_books,
    get_primary_corpus_books,
    get_reference_books,
)
from .culture.places import GarhwaliPlace, PlacesTreasury
from .culture.deities import GarhwaliDeity, DeitiesTreasury
from .culture.surnames import GarhwaliSurname, SurnamesTreasury
from .culture.flora import GarhwaliPlant, FloraTreasury
from .culture.rituals import GarhwaliRitualItem, RitualsTreasury
from .culture.folklore import GarhwaliSong, GarhwaliHoliSong, DigitalArchiveSource, FolkloreTreasury
from .culture.books import (
    BookPage,
    GarhwaliDigitalBook,
    BooksCorpus,
    read_book_page,
    list_digital_books,
    get_digital_book,
    search_digital_books,
)

# 20-Pillar Computational Corpus & NLP Framework
from .corpus import (
    CorpusPillar,
    CorpusTaxonomy,
    get_corpus_taxonomy,
    list_corpus_pillars,
    get_pillar,
    AnnotatedSentence,
    SentenceCorpus,
    get_sentence_corpus,
    search_sentences,
    get_annotated_sentence,
    GarhwaliIdiom,
    IdiomCorpus,
    get_idiom_corpus,
    search_idioms,
    random_idiom,
    list_proverbs,
)

# Global instances for simple top-level access
_DICT = GarhwaliDictionary()
phrases = type("Phrases", (), {"all": _DICT.all_phrases, "random": _DICT.random_phrase})()
proverbs = type("Proverbs", (), {"all": _DICT.all_proverbs, "random": _DICT.random_proverb})()
riddles = type("Riddles", (), {"all": _DICT.all_riddles, "random": _DICT.random_riddle})()
festivals = type("Festivals", (), {"list": list_festivals})()


def lookup(word: str):
    return _DICT.lookup(word)


def search(query: str, limit: int = 20):
    return _DICT.search(query, limit=limit)


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
    # Metadata & ISO Constants
    "ISO_639_3",
    "ISO_639_NAME",
    "NATIVE_NAME",
    "Dialect",
    "Script",
    "PartOfSpeech",
    "Tense",
    "Gender",
    "GrammaticalNumber",
    "DAYS_OF_WEEK",
    # Universal Translation
    "translate",
    "TranslationResult",
    "PivotTranslator",
    "pivot_translate",
    "LLMTranslator",
    "translate_with_llm",
    "GARHWALI_SYSTEM_PROMPT",
    "get_garhwali_prompt",
    "apply_dialect",
    "RuleBasedTranslator",
    # Voice Translation & Audio
    "voice_translate",
    "VoiceTranslator",
    "VoiceTranslationResult",
    "GarhwaliVoiceSynthesizer",
    # Lexicon & Morphology
    "lookup",
    "search",
    "analyze",
    "total_word_forms",
    "MorphAnalysis",
    "phrases",
    "proverbs",
    "riddles",
    "festivals",
    # Phonetics
    "syllables",
    "devanagari_to_latin",
    "latin_to_devanagari",
    # Numbers & Fractions
    "num_to_words",
    "words_to_num",
    "to_devanagari_numerals",
    "from_devanagari_numerals",
    "ordinal",
    "fraction",
    "GARHWALI_FRACTIONS",
    # Grammar & Morphology Engine
    "pluralize",
    "to_feminine",
    "to_masculine",
    "to_oblique",
    "make_diminutive",
    "make_augmentative",
    "decline_noun",
    "CaseMarker",
    "CASE_MARKERS",
    "GARHWALI_POSTPOSITIONS",
    "get_marker",
    "attach_case",
    "extract_root",
    "conjugate_to_be",
    "conjugate",
    "conjunctive_participle",
    "causative",
    "passive",
    "medio_passive_inability",
    "compound_verb",
    "conditional",
    "imperative",
    "prohibitive",
    "modal_ability",
    "modal_obligation",
    "modal_desiderative",
    "subjunctive",
    "habitual_past",
    "progressive",
    "inceptive",
    "completive",
    "conjugate_full_paradigm",
    "SyntaxEngine",
    "build_sentence",
    "interrogative_sentence",
    "relative_correlative",
    "echo_word",
    "build_compound_sentence",
    "build_conditional_sentence",
    "build_causal_sentence",
    "build_purposive_sentence",
    "build_concessive_sentence",
    "build_passive_sentence",
    "build_inability_sentence",
    "build_imperative_sentence",
    "validate_agreement",
    "analyze_sentence",
    "decline_pronoun",
    "get_demonstrative",
    "get_indefinite",
    "get_relative_pair",
    "list_all_pronouns",
    "RuleCategory",
    "GrammarRule",
    "RuleRegistry",
    "GARHWALI_GRAMMAR_RULES",
    # Calendar & Literature
    "get_months",
    "get_seasons",
    "get_current_season",
    "list_festivals",
    "poems",
    "epics",
    "authors",
    "FolkEpic",
    "FolkPoem",
    "GarhwaliAuthor",
    "LiteratureTreasury",
    "EPICS_DATA",
    "POEMS_DATA",
    "AUTHORS_DATA",
    # Master Bibliography
    "GarhwaliBook",
    "BibliographyTreasury",
    "get_bibliography",
    "search_books",
    "get_book_by_id",
    "get_works_in_garhwali",
    "get_grammar_books",
    "get_primary_corpus_books",
    "get_reference_books",
    # Sacred Geography & Shrines
    "GarhwaliPlace",
    "PlacesTreasury",
    "GarhwaliDeity",
    "DeitiesTreasury",
    # Surnames & Social Structure
    "GarhwaliSurname",
    "SurnamesTreasury",
    # Flora & Rituals
    "GarhwaliPlant",
    "FloraTreasury",
    "GarhwaliRitualItem",
    "RitualsTreasury",
    # Folklore, Songs & Classical Holi
    "GarhwaliSong",
    "GarhwaliHoliSong",
    "DigitalArchiveSource",
    "FolkloreTreasury",
    # Digitized Books & Reader
    "BookPage",
    "GarhwaliDigitalBook",
    "BooksCorpus",
    "read_book_page",
    "list_digital_books",
    "get_digital_book",
    "search_digital_books",
    # 20-Pillar Computational Corpus & NLP
    "CorpusPillar",
    "CorpusTaxonomy",
    "get_corpus_taxonomy",
    "list_corpus_pillars",
    "get_pillar",
    "AnnotatedSentence",
    "SentenceCorpus",
    "get_sentence_corpus",
    "search_sentences",
    "get_annotated_sentence",
    "GarhwaliIdiom",
    "IdiomCorpus",
    "get_idiom_corpus",
    "search_idioms",
    "random_idiom",
    "list_proverbs",
]
