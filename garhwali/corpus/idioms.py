# -*- coding: utf-8 -*-
"""
Idiom, Proverb, and Figurative Phrase Corpus of the Garhwali Language.

Mined from authoritative sources:
- 'गढ़वाली मुहावरों-कहावतों का वृहद् संग्रह' (पुष्कर सिंह कण्डारी, 2016, वाणी प्रकाशन, 392 pp.)
- 'गढ़वाली पखाणा' (शालीग्राम वैष्णव, 1930, नन्दप्रयाग)
- 'Proverbs & Folklore of Kumaun and Garhwal' (पं० गंगा दत्त उप्रेती, 1894)
- 'गढ़वाली भाषा' (डॉ० गोविन्द चातक, 1959)
"""

import json
import os
import random
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class GarhwaliIdiom:
    id: str
    idiom: str
    transliteration: str
    literal_meaning: str
    figurative_meaning: str
    hindi_equivalent: str
    english_gloss: str
    example_sentence: str
    example_translation_hi: str
    example_translation_en: str
    grammatical_category: str
    theme: str
    region: str
    source: str


_IDIOMS_CACHE: Optional[List[GarhwaliIdiom]] = None


def _load_idioms() -> List[GarhwaliIdiom]:
    global _IDIOMS_CACHE
    if _IDIOMS_CACHE is not None:
        return _IDIOMS_CACHE

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'idioms.json')
    if not os.path.exists(json_path):
        _IDIOMS_CACHE = []
        return _IDIOMS_CACHE

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    items = []
    for d in data:
        items.append(
            GarhwaliIdiom(
                id=d.get('id', ''),
                idiom=d.get('idiom', ''),
                transliteration=d.get('transliteration', ''),
                literal_meaning=d.get('literal_meaning', ''),
                figurative_meaning=d.get('figurative_meaning', ''),
                hindi_equivalent=d.get('hindi_equivalent', ''),
                english_gloss=d.get('english_gloss', ''),
                example_sentence=d.get('example_sentence', ''),
                example_translation_hi=d.get('example_translation_hi', ''),
                example_translation_en=d.get('example_translation_en', ''),
                grammatical_category=d.get('grammatical_category', ''),
                theme=d.get('theme', ''),
                region=d.get('region', ''),
                source=d.get('source', '')
            )
        )
    _IDIOMS_CACHE = items
    return _IDIOMS_CACHE


class IdiomCorpus:
    """Interface to access, search, and analyze Garhwali idioms and proverbs."""

    @staticmethod
    def all() -> List[GarhwaliIdiom]:
        """Return all idioms and proverbs in the corpus."""
        return _load_idioms()

    @staticmethod
    def get(idiom_id: str) -> Optional[GarhwaliIdiom]:
        """Get an idiom by unique ID (e.g., 'idh_001')."""
        for item in _load_idioms():
            if item.id == idiom_id:
                return item
        return None

    @staticmethod
    def search(query: str) -> List[GarhwaliIdiom]:
        """
        Search idioms by keyword across Garhwali text, transliteration,
        Hindi equivalent, English gloss, literal meaning, or figurative meaning.
        """
        q = query.strip().lower()
        res = []
        for item in _load_idioms():
            if (
                q in item.idiom.lower()
                or q in item.transliteration.lower()
                or q in item.hindi_equivalent.lower()
                or q in item.english_gloss.lower()
                or q in item.literal_meaning.lower()
                or q in item.figurative_meaning.lower()
                or q in item.theme.lower()
            ):
                res.append(item)
        return res

    @staticmethod
    def filter(
        category: Optional[str] = None,
        theme: Optional[str] = None,
        region: Optional[str] = None
    ) -> List[GarhwaliIdiom]:
        """Filter idioms by grammatical category, theme, or dialect region."""
        res = _load_idioms()
        if category:
            cat_lower = category.strip().lower()
            res = [i for i in res if cat_lower in i.grammatical_category.lower()]
        if theme:
            theme_lower = theme.strip().lower()
            res = [i for i in res if theme_lower in i.theme.lower()]
        if region:
            reg_lower = region.strip().lower()
            res = [i for i in res if reg_lower in i.region.lower()]
        return res

    @staticmethod
    def random() -> Optional[GarhwaliIdiom]:
        """Return a random idiom or proverb."""
        items = _load_idioms()
        return random.choice(items) if items else None

    @staticmethod
    def themes() -> List[str]:
        """Get unique themes present in the corpus."""
        return sorted(list({i.theme for i in _load_idioms() if i.theme}))

    @staticmethod
    def categories() -> List[str]:
        """Get unique grammatical categories present in the corpus."""
        return sorted(list({i.grammatical_category for i in _load_idioms() if i.grammatical_category}))

    @staticmethod
    def regions() -> List[str]:
        """Get unique dialect regions represented in the corpus."""
        return sorted(list({i.region for i in _load_idioms() if i.region}))

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Return summary metrics of the idiom corpus."""
        items = _load_idioms()
        from collections import Counter
        cat_counts = Counter(i.grammatical_category for i in items)
        return {
            "total_items": len(items),
            "proverbs_count": sum(c for k, c in cat_counts.items() if "पखाणा" in k or "लोकोक्ति" in k),
            "idioms_count": sum(c for k, c in cat_counts.items() if "मुहावरा" in k),
            "unique_themes": len(IdiomCorpus.themes()),
            "unique_regions": len(IdiomCorpus.regions())
        }


# Convenience module functions
def get_idiom_corpus() -> IdiomCorpus:
    """Return the IdiomCorpus interface."""
    return IdiomCorpus


def search_idioms(query: str) -> List[GarhwaliIdiom]:
    """Search idioms across English, Hindi, and Garhwali keywords."""
    return IdiomCorpus.search(query)


def random_idiom() -> Optional[GarhwaliIdiom]:
    """Get a random idiom or proverb."""
    return IdiomCorpus.random()


def list_proverbs() -> List[GarhwaliIdiom]:
    """List all traditional Garhwali proverbs (पखाणा / लोकोक्तियाँ)."""
    return IdiomCorpus.filter(category="पखाणा")
