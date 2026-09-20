# -*- coding: utf-8 -*-
"""Garhwali Main Translation Engine."""

import re
from typing import Dict, List, Any, Optional, Tuple, Union, Set, NamedTuple, Callable
from .rule_based import (
    CONVERSATIONAL_HINGLISH_GARHWALI_MAP,
    CONVERSATIONAL_EN_GARHWALI_MAP,
    CONVERSATIONAL_HI_GARHWALI_MAP,
    apply_dialect
)
from ..phonetics import latin_to_devanagari

class TranslationResult(NamedTuple):
    text: str
    source_lang: str
    target_lang: str
    confidence: float
    dialect: str

def translate(text: str, source: str = "auto", target: str = "garhwali", dialect: str = "srinagariya") -> TranslationResult:
    clean = text.strip()
    if not clean:
        return TranslationResult("", source, target, 1.0, dialect)

    clean_low = clean.lower()
    clean_no_punct = re.sub(r'[^\w\s]', '', clean_low)

    # 1. Check Hinglish patterns
    for p, kmy in CONVERSATIONAL_HINGLISH_GARHWALI_MAP:
        if re.search(p, clean_low) or re.search(p, clean_no_punct):
            return TranslationResult(apply_dialect(kmy, dialect), "hinglish", target, 1.0, dialect)

    # 2. Check English patterns
    for p, kmy in CONVERSATIONAL_EN_GARHWALI_MAP:
        if re.search(p, clean_low) or re.search(p, clean_no_punct):
            return TranslationResult(apply_dialect(kmy, dialect), "en", target, 1.0, dialect)

    # 3. Check Hindi patterns
    for p, kmy in CONVERSATIONAL_HI_GARHWALI_MAP:
        if re.search(p, clean) or re.search(p, clean_no_punct):
            return TranslationResult(apply_dialect(kmy, dialect), "hi", target, 1.0, dialect)

    # 4. Fallback: Devanagari transliteration & word replacements
    dev_text = latin_to_devanagari(clean) if not re.search(r'[\u0900-\u097F]', clean) else clean
    return TranslationResult(apply_dialect(dev_text, dialect), source, target, 0.90, dialect)
