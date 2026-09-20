# -*- coding: utf-8 -*-
"""Garhwali Lexicon & Morphology Package."""

from .dictionary import GarhwaliDictionary
from .morphology import GarhwaliMorphologyEngine, get_morphology_engine, MorphAnalysis

__all__ = [
    "GarhwaliDictionary",
    "GarhwaliMorphologyEngine",
    "get_morphology_engine",
    "MorphAnalysis"
]
