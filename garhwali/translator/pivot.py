# -*- coding: utf-8 -*-
"""Universal Multilingual Pivot Translation Engine for Garhwali."""

from .engine import translate, TranslationResult

def pivot_translate(text: str, source_lang: str = "en", target_lang: str = "garhwali", dialect: str = "srinagariya") -> TranslationResult:
    return translate(text, source=source_lang, target=target_lang, dialect=dialect)
