# -*- coding: utf-8 -*-
"""
Universal Multi-Language Pivot Translator for Garhwali.
Translates from ANY world language (French, Spanish, German, Japanese, Russian, Arabic, etc.)
into Garhwali by bridging through English/Hindi with zero required external API keys.
"""

import urllib.request
import urllib.parse
import json
from typing import Tuple, Optional
from garhwali.translator.rule_based import RuleBasedTranslator


class PivotTranslator:
    """
    Translates from any language into Garhwali using an intermediate pivot bridge.
    """

    def __init__(self):
        self.rule_translator = RuleBasedTranslator()
        self._cache = {}

    def translate_to_garhwali(
        self,
        text: str,
        source_lang: str = "auto",
        dialect: str = "srinagariya",
        timeout_seconds: float = 4.0
    ) -> Tuple[str, str, float]:
        """
        Translates text from any world language to Garhwali.
        Returns: (garhwali_translation, intermediate_english, confidence)
        """
        text = text.strip()
        if not text:
            return "", "", 0.0

        src_clean = source_lang.lower().strip()
        cache_key = (text, src_clean, dialect)
        if cache_key in self._cache:
            return self._cache[cache_key]

        # 1. If already English
        if src_clean in ("en", "eng", "english"):
            res = self.rule_translator.translate(text, source="en", target="garhwali", dialect=dialect)
            out = (res.text, text, res.confidence)
            self._cache[cache_key] = out
            return out

        # 2. If Hindi
        if src_clean in ("hi", "hin", "hindi"):
            res = self.rule_translator.translate(text, source="hi", target="garhwali", dialect=dialect)
            out = (res.text, text, res.confidence)
            self._cache[cache_key] = out
            return out

        # 3. Foreign language -> Pivot to English via public lightweight endpoint
        intermediate_en = ""
        try:
            url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair={src_clean}|en"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) GarhwaliTranslator/1.2"}
            )
            with urllib.request.urlopen(req, timeout=timeout_seconds) as response:
                payload = json.loads(response.read().decode("utf-8"))
                if payload.get("responseData") and payload["responseData"].get("translatedText"):
                    intermediate_en = payload["responseData"]["translatedText"].strip()
        except Exception:
            intermediate_en = text

        if not intermediate_en:
            intermediate_en = text

        # 4. English -> Garhwali
        res = self.rule_translator.translate(intermediate_en, source="en", target="garhwali", dialect=dialect)
        confidence = min(0.85, res.confidence)
        out = (res.text, intermediate_en, confidence)
        self._cache[cache_key] = out
        return out


def pivot_translate(
    text: str,
    source_lang: str = "auto",
    dialect: str = "srinagariya"
) -> Tuple[str, str, float]:
    """Convenience function for pivot translation."""
    return PivotTranslator().translate_to_garhwali(text, source_lang=source_lang, dialect=dialect)
