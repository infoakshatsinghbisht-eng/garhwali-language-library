# -*- coding: utf-8 -*-
"""
20-Pillar Computational Corpus Taxonomy for the Garhwali Language.

This module models the 20 fundamental corpus domains required for comprehensive
computational linguistics, natural language processing, speech synthesis/recognition,
and large language model development in Garhwali.
"""

import json
import os
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field


@dataclass
class CorpusPillar:
    pillar_number: int
    id: str
    icon: str
    name_en: str
    name_garhwali: str
    description: str
    subcategories: List[str] = field(default_factory=list)
    canonical_sources: List[str] = field(default_factory=list)
    lexical_mappings: List[str] = field(default_factory=list)
    computational_applications: List[str] = field(default_factory=list)


_TAXONOMY_CACHE: Optional[List[CorpusPillar]] = None


def _load_taxonomy() -> List[CorpusPillar]:
    global _TAXONOMY_CACHE
    if _TAXONOMY_CACHE is not None:
        return _TAXONOMY_CACHE

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'taxonomy.json')
    if not os.path.exists(json_path):
        _TAXONOMY_CACHE = []
        return _TAXONOMY_CACHE

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    pillars = []
    for d in data:
        pillars.append(
            CorpusPillar(
                pillar_number=d.get('pillar_number', 0),
                id=d.get('id', ''),
                icon=d.get('icon', ''),
                name_en=d.get('name_en', ''),
                name_garhwali=d.get('name_garhwali', ''),
                description=d.get('description', ''),
                subcategories=d.get('subcategories', []),
                canonical_sources=d.get('canonical_sources', []),
                lexical_mappings=d.get('lexical_mappings', []),
                computational_applications=d.get('computational_applications', [])
            )
        )
    _TAXONOMY_CACHE = pillars
    return _TAXONOMY_CACHE


class CorpusTaxonomy:
    """Interface to explore and utilize the 20-Pillar Computational Corpus Framework."""

    @staticmethod
    def list_pillars() -> List[CorpusPillar]:
        """Return all 20 computational corpus pillars in canonical order."""
        return _load_taxonomy()

    @staticmethod
    def get_pillar(identifier: Union[int, str]) -> Optional[CorpusPillar]:
        """
        Get a pillar by its number (1-20) or string identifier.

        Example:
            pillar = CorpusTaxonomy.get_pillar(1)
            pillar = CorpusTaxonomy.get_pillar("proverbs_idioms")
        """
        pillars = _load_taxonomy()
        if isinstance(identifier, int):
            for p in pillars:
                if p.pillar_number == identifier:
                    return p
        elif isinstance(identifier, str):
            ident_clean = identifier.strip().lower()
            for p in pillars:
                if p.id.lower() == ident_clean:
                    return p
                if str(p.pillar_number) == ident_clean:
                    return p
        return None

    @staticmethod
    def search(query: str) -> List[CorpusPillar]:
        """Search pillars across name, description, sources, and applications."""
        q = query.strip().lower()
        res = []
        for p in _load_taxonomy():
            if (
                q in p.name_en.lower()
                or q in p.name_garhwali
                or q in p.description.lower()
                or any(q in s.lower() for s in p.subcategories)
                or any(q in src.lower() for src in p.canonical_sources)
                or any(q in app.lower() for app in p.computational_applications)
            ):
                res.append(p)
        return res

    @staticmethod
    def summary() -> Dict[str, Any]:
        """Summary metrics of the 20-pillar corpus framework."""
        pillars = _load_taxonomy()
        total_subcats = sum(len(p.subcategories) for p in pillars)
        total_sources = sum(len(p.canonical_sources) for p in pillars)
        total_applications = sum(len(p.computational_applications) for p in pillars)
        return {
            "total_pillars": len(pillars),
            "total_subcategories": total_subcats,
            "total_canonical_sources": total_sources,
            "total_computational_applications": total_applications,
            "pillar_ids": [p.id for p in pillars]
        }


# Convenience module functions
def get_corpus_taxonomy() -> CorpusTaxonomy:
    """Return the CorpusTaxonomy interface."""
    return CorpusTaxonomy


def list_corpus_pillars() -> List[CorpusPillar]:
    """Return all 20 pillars."""
    return CorpusTaxonomy.list_pillars()


def get_pillar(identifier: Union[int, str]) -> Optional[CorpusPillar]:
    """Retrieve a specific corpus pillar."""
    return CorpusTaxonomy.get_pillar(identifier)
