# -*- coding: utf-8 -*-
"""Garhwali Translation Package."""

from .engine import translate, TranslationResult
from .rule_based import apply_dialect, RuleBasedTranslator
from .pivot import PivotTranslator, pivot_translate
from .llm_adapter import LLMTranslator, translate_with_llm, GARHWALI_SYSTEM_PROMPT, get_garhwali_prompt

__all__ = [
    "translate",
    "TranslationResult",
    "apply_dialect",
    "RuleBasedTranslator",
    "PivotTranslator",
    "pivot_translate",
    "LLMTranslator",
    "translate_with_llm",
    "GARHWALI_SYSTEM_PROMPT",
    "get_garhwali_prompt",
]
