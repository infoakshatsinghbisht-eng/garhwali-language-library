# -*- coding: utf-8 -*-
"""
Annotated Sentence Corpus for Garhwali Computational Linguistics and NLP.

Each sentence is annotated with:
- Raw Devanagari text
- Precise tokenization
- Universal Part-of-Speech (UPOS) tags
- Morphological features (Gender, Number, Case, Tense, Aspect, Person, Mood)
- Sentence-level Hindi translation
- Sentence-level English translation
- Exact literary citation (Author, Work, Year, Genre, Region, Source Page)
"""

import json
import os
import random
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field


@dataclass
class AnnotatedSentence:
    id: str
    text: str
    language: str
    source: str
    author: str
    genre: str
    year: int
    region: str
    translation_hi: str
    translation_en: str
    tokens: List[str] = field(default_factory=list)
    pos: List[str] = field(default_factory=list)
    morphology: List[Dict[str, Any]] = field(default_factory=list)
    source_page: int = 1

    @property
    def token_count(self) -> int:
        return len(self.tokens)

    @property
    def pos_tags(self) -> List[str]:
        return self.pos

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "language": self.language,
            "source": self.source,
            "author": self.author,
            "genre": self.genre,
            "year": self.year,
            "region": self.region,
            "translation_hi": self.translation_hi,
            "translation_en": self.translation_en,
            "tokens": self.tokens,
            "pos": self.pos,
            "morphology": self.morphology,
            "source_page": self.source_page
        }


_SENTENCES_CACHE: Optional[List[AnnotatedSentence]] = None


def _load_sentences() -> List[AnnotatedSentence]:
    global _SENTENCES_CACHE
    if _SENTENCES_CACHE is not None:
        return _SENTENCES_CACHE

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'sentences.json')
    if not os.path.exists(json_path):
        _SENTENCES_CACHE = []
        return _SENTENCES_CACHE

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sentences = []
    for d in data:
        sentences.append(
            AnnotatedSentence(
                id=d.get('id', ''),
                text=d.get('text', ''),
                language=d.get('language', 'garhwali'),
                source=d.get('source', ''),
                author=d.get('author', ''),
                genre=d.get('genre', ''),
                year=int(d.get('year', 0)),
                region=d.get('region', ''),
                translation_hi=d.get('translation_hi', ''),
                translation_en=d.get('translation_en', ''),
                tokens=d.get('tokens', []),
                pos=d.get('pos', []),
                morphology=d.get('morphology', []),
                source_page=int(d.get('source_page', 1))
            )
        )
    _SENTENCES_CACHE = sentences
    return _SENTENCES_CACHE


class SentenceCorpus:
    """Interface to explore, filter, search, and export the Annotated Garhwali Sentence Corpus."""

    @staticmethod
    def all() -> List[AnnotatedSentence]:
        """Return all annotated sentences in the corpus."""
        return _load_sentences()

    @staticmethod
    def get(sentence_id: str) -> Optional[AnnotatedSentence]:
        """Get an annotated sentence by ID (e.g. 'sent_001')."""
        for s in _load_sentences():
            if s.id == sentence_id:
                return s
        return None

    @staticmethod
    def filter(
        author: Optional[str] = None,
        genre: Optional[str] = None,
        region: Optional[str] = None,
        min_year: Optional[int] = None,
        max_year: Optional[int] = None
    ) -> List[AnnotatedSentence]:
        """Filter sentences by author, genre, region, and year range."""
        res = _load_sentences()
        if author:
            auth_lower = author.strip().lower()
            res = [s for s in res if auth_lower in s.author.lower()]
        if genre:
            genre_lower = genre.strip().lower()
            res = [s for s in res if genre_lower in s.genre.lower()]
        if region:
            reg_lower = region.strip().lower()
            res = [s for s in res if reg_lower in s.region.lower()]
        if min_year is not None:
            res = [s for s in res if s.year >= min_year]
        if max_year is not None:
            res = [s for s in res if s.year <= max_year]
        return res

    @staticmethod
    def search(query: str, in_translation: bool = True) -> List[AnnotatedSentence]:
        """
        Search sentences matching a keyword across Garhwali text,
        Hindi translation, English translation, or author.
        """
        q = query.strip().lower()
        res = []
        for s in _load_sentences():
            match = q in s.text.lower() or q in s.author.lower() or q in s.source.lower()
            if in_translation and not match:
                match = q in s.translation_hi.lower() or q in s.translation_en.lower()
            if match:
                res.append(s)
        return res

    @staticmethod
    def find_by_token(token: str) -> List[AnnotatedSentence]:
        """Find sentences containing an exact token."""
        token_clean = token.strip()
        return [s for s in _load_sentences() if token_clean in s.tokens]

    @staticmethod
    def find_by_pos(pos_tag: str) -> List[AnnotatedSentence]:
        """Find sentences containing tokens with a given Universal POS tag (e.g. 'NOUN', 'VERB', 'ADJ')."""
        pos_upper = pos_tag.strip().upper()
        return [s for s in _load_sentences() if pos_upper in s.pos]

    @staticmethod
    def vocabulary() -> Set[str]:
        """Extract unique vocabulary (tokens) across the entire corpus."""
        vocab = set()
        for s in _load_sentences():
            for t in s.tokens:
                if t not in (",", ".", "!", "?", "।", ";", ":", "-", "—"):
                    vocab.add(t)
        return vocab

    @staticmethod
    def pos_distribution() -> Dict[str, int]:
        """Calculate frequency distribution of POS tags in the corpus."""
        from collections import Counter
        counts = Counter()
        for s in _load_sentences():
            counts.update(s.pos)
        return dict(counts.most_common())

    @staticmethod
    def train_test_split(
        train_ratio: float = 0.8,
        val_ratio: float = 0.1,
        test_ratio: float = 0.1,
        seed: int = 42
    ) -> Dict[str, List[AnnotatedSentence]]:
        """Split corpus deterministically into train, validation, and test datasets."""
        sentences = list(_load_sentences())
        rng = random.Random(seed)
        shuffled = list(sentences)
        rng.shuffle(shuffled)

        n = len(shuffled)
        n_train = int(n * train_ratio)
        n_val = int(n * val_ratio)

        train = shuffled[:n_train]
        val = shuffled[n_train:n_train + n_val]
        test = shuffled[n_train + n_val:]

        return {
            "train": train,
            "validation": val,
            "test": test
        }

    @staticmethod
    def to_jsonl(output_path: str) -> str:
        """Export sentences to JSONL format for Hugging Face / NLP fine-tuning."""
        sentences = _load_sentences()
        with open(output_path, 'w', encoding='utf-8') as f:
            for s in sentences:
                f.write(json.dumps(s.to_dict(), ensure_ascii=False) + '\n')
        return output_path

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Return summary metrics of the sentence corpus."""
        sentences = _load_sentences()
        total_tokens = sum(s.token_count for s in sentences)
        unique_authors = sorted(list({s.author for s in sentences if s.author}))
        unique_genres = sorted(list({s.genre for s in sentences if s.genre}))
        vocab = SentenceCorpus.vocabulary()
        return {
            "total_sentences": len(sentences),
            "total_tokens": total_tokens,
            "vocabulary_size": len(vocab),
            "average_sentence_length": round(total_tokens / len(sentences), 2) if sentences else 0,
            "unique_authors_count": len(unique_authors),
            "genres_represented": unique_genres,
            "authors": unique_authors,
            "pos_distribution": SentenceCorpus.pos_distribution()
        }


# Convenience module functions
def get_sentence_corpus() -> SentenceCorpus:
    """Return the SentenceCorpus interface."""
    return SentenceCorpus


def search_sentences(query: str, in_translation: bool = True) -> List[AnnotatedSentence]:
    """Search annotated sentences across Garhwali, Hindi, or English."""
    return SentenceCorpus.search(query, in_translation=in_translation)


def get_annotated_sentence(sentence_id: str) -> Optional[AnnotatedSentence]:
    """Retrieve an annotated sentence by ID."""
    return SentenceCorpus.get(sentence_id)
