# -*- coding: utf-8 -*-
"""Garhwali Main Translation Engine."""

import re
from typing import Dict, List, Any, Optional, Tuple, Union, Set, NamedTuple, Callable
from .rule_based import (
    CONVERSATIONAL_HINGLISH_GARHWALI_MAP,
    CONVERSATIONAL_EN_GARHWALI_MAP,
    CONVERSATIONAL_HI_GARHWALI_MAP,
    apply_dialect,
    RuleBasedTranslator
)
from ..phonetics import latin_to_devanagari, devanagari_to_latin


class TranslationResult(NamedTuple):
    text: str
    source_lang: str
    target_lang: str
    confidence: float
    dialect: str
    romanized: Optional[str] = None
    method: str = "rule_based"


def translate(
    text: str,
    source: str = "auto",
    target: str = "garhwali",
    dialect: str = "srinagariya",
    method: str = "auto",
    api_key: Optional[str] = None,
) -> TranslationResult:
    """
    Translates text into Garhwali using rule-based patterns, pivot routing, or LLM adapters.
    """
    clean = text.strip()
    if not clean:
        return TranslationResult("", source, target, 1.0, dialect, "", method)

    # 1. Explicit LLM routing
    if method == "llm" or (api_key and method == "auto"):
        from .llm_adapter import LLMTranslator
        llm = LLMTranslator(api_key=api_key)
        res_data = llm.translate(clean, source_lang=source, dialect=dialect)
        if "error" not in res_data and "garhwali" in res_data:
            dev = res_data["garhwali"]
            rom = res_data.get("romanized", devanagari_to_latin(dev))
            return TranslationResult(
                text=dev,
                source_lang=source,
                target_lang=target,
                confidence=0.98,
                dialect=dialect,
                romanized=rom,
                method="llm"
            )

    # 2. Pivot routing for non-Hindi/non-English source languages (e.g. French, German, Spanish, etc.)
    source_clean = source.lower()
    if method == "pivot" or (source_clean not in ("auto", "en", "hi", "hinglish", "english", "hindi") and method == "auto"):
        from .pivot import PivotTranslator
        piv = PivotTranslator()
        piv_res = piv.translate(clean, source_lang=source, dialect=dialect)
        return TranslationResult(
            text=piv_res.translated_text,
            source_lang=source,
            target_lang=target,
            confidence=piv_res.confidence,
            dialect=dialect,
            romanized=devanagari_to_latin(piv_res.translated_text),
            method=piv_res.method
        )

    clean_low = clean.lower()
    clean_no_punct = re.sub(r'[^\w\s]', '', clean_low)

    # 3. Check Hinglish patterns
    for p, kmy in CONVERSATIONAL_HINGLISH_GARHWALI_MAP:
        if re.search(p, clean_low) or re.search(p, clean_no_punct):
            out = apply_dialect(kmy, dialect)
            return TranslationResult(out, "hinglish", target, 1.0, dialect, devanagari_to_latin(out), "rule_based")

    # 4. Check English patterns
    for p, kmy in CONVERSATIONAL_EN_GARHWALI_MAP:
        if re.search(p, clean_low) or re.search(p, clean_no_punct):
            out = apply_dialect(kmy, dialect)
            return TranslationResult(out, "en", target, 1.0, dialect, devanagari_to_latin(out), "rule_based")

    # 5. Check Hindi patterns
    for p, kmy in CONVERSATIONAL_HI_GARHWALI_MAP:
        if re.search(p, clean) or re.search(p, clean_no_punct):
            out = apply_dialect(kmy, dialect)
            return TranslationResult(out, "hi", target, 1.0, dialect, devanagari_to_latin(out), "rule_based")

    # 6. Lexicon & RuleBasedTranslator cache check
    rule_trans = RuleBasedTranslator()
    if re.search(r'[\u0900-\u097F]', clean):
        res_text, conf = rule_trans.translate_hi_to_gbm(clean)
        out = apply_dialect(res_text, dialect)
        return TranslationResult(out, "hi" if source == "auto" else source, target, conf, dialect, devanagari_to_latin(out), "rule_based")
    else:
        res_text, conf = rule_trans.translate_en_to_gbm(clean)
        out = apply_dialect(res_text, dialect)
        return TranslationResult(out, "en" if source == "auto" else source, target, conf, dialect, devanagari_to_latin(out), "rule_based")
