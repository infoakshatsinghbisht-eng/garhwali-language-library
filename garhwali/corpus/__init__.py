# -*- coding: utf-8 -*-
"""
Garhwali Computational Corpus Framework.

Components:
1. 20-Pillar Computational Corpus Taxonomy (`CorpusTaxonomy`, `CorpusPillar`)
2. Annotated Sentence Corpus (`SentenceCorpus`, `AnnotatedSentence`)
   - UPOS tags, morphology, translations, literary citations
3. Idiom & Proverb Corpus (`IdiomCorpus`, `GarhwaliIdiom`)
   - 10-field comprehensive figurative linguistics schema
"""

from .taxonomy import (
    CorpusPillar,
    CorpusTaxonomy,
    get_corpus_taxonomy,
    list_corpus_pillars,
    get_pillar,
)
from .sentences import (
    AnnotatedSentence,
    SentenceCorpus,
    get_sentence_corpus,
    search_sentences,
    get_annotated_sentence,
)
from .idioms import (
    GarhwaliIdiom,
    IdiomCorpus,
    get_idiom_corpus,
    search_idioms,
    random_idiom,
    list_proverbs,
)

__all__ = [
    # 20-Pillar Taxonomy
    "CorpusPillar",
    "CorpusTaxonomy",
    "get_corpus_taxonomy",
    "list_corpus_pillars",
    "get_pillar",
    # Annotated Sentence Corpus
    "AnnotatedSentence",
    "SentenceCorpus",
    "get_sentence_corpus",
    "search_sentences",
    "get_annotated_sentence",
    # Idioms & Proverbs Corpus
    "GarhwaliIdiom",
    "IdiomCorpus",
    "get_idiom_corpus",
    "search_idioms",
    "random_idiom",
    "list_proverbs",
]
