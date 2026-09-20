# -*- coding: utf-8 -*-
"""Garhwali Translation Package."""

from .engine import translate, TranslationResult
from .rule_based import apply_dialect
from .pivot import pivot_translate
from .llm_adapter import get_garhwali_prompt

__all__ = [
    "translate", "TranslationResult",
    "apply_dialect", "pivot_translate",
    "get_garhwali_prompt"
]
