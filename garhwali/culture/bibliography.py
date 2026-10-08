# -*- coding: utf-8 -*-
"""
Bibliography and Scholarly Corpus of the Garhwali Language.

Provides comprehensive cataloguing of:
1. Works written IN Garhwali (Classical Epics, Modern Poetry, Story Collections,
   Plays, Religious & Classical Translations such as Garhwali Meghdoot and Bhagavad Gita).
2. Works on Garhwali Grammar, Lexicography & Dialectology.
3. Scholarly and folkloric works ABOUT Garhwali language, oral epics, history, and culture.
"""

import json
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class GarhwaliBook:
    id: int
    title: str
    author: str
    year: str
    genre: str
    category: str  # "works_in_garhwali", "grammar_and_linguistics", "works_about_garhwali", "dictionaries"
    category_label: str
    language_status: str
    evidence: str
    publisher: str
    pages: str
    isbn: str
    source_url: str
    confidence: str
    corpus_eligibility: str = "primary_native_corpus"  # "primary_native_corpus" vs "reference_lexical_index_only"
    library_value: str = "★★★★★"


_BIBLIOGRAPHY_CACHE: Optional[List[GarhwaliBook]] = None


def _load_bibliography() -> List[GarhwaliBook]:
    global _BIBLIOGRAPHY_CACHE
    if _BIBLIOGRAPHY_CACHE is not None:
        return _BIBLIOGRAPHY_CACHE

    json_path = os.path.join(os.path.dirname(__file__), 'data', 'bibliography.json')
    if not os.path.exists(json_path):
        _BIBLIOGRAPHY_CACHE = []
        return _BIBLIOGRAPHY_CACHE

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    books = []
    for d in data:
        books.append(
            GarhwaliBook(
                id=d.get('id', 0),
                title=d.get('title', ''),
                author=d.get('author', ''),
                year=d.get('year', ''),
                genre=d.get('genre', ''),
                category=d.get('category', 'works_in_garhwali'),
                category_label=d.get('category_label', ''),
                language_status=d.get('language_status', ''),
                evidence=d.get('evidence', ''),
                publisher=d.get('publisher', ''),
                pages=d.get('pages', ''),
                isbn=d.get('isbn', ''),
                source_url=d.get('source_url', ''),
                confidence=d.get('confidence', ''),
                corpus_eligibility=d.get('corpus_eligibility', 'primary_native_corpus' if d.get('category') == 'works_in_garhwali' else 'reference_lexical_index_only'),
                library_value=d.get('library_value', '★★★★★')
            )
        )
    _BIBLIOGRAPHY_CACHE = books
    return _BIBLIOGRAPHY_CACHE


class BibliographyTreasury:
    """Interface to access the Master Garhwali Bibliography."""

    @staticmethod
    def list_books(
        category: Optional[str] = None,
        author: Optional[str] = None,
        genre: Optional[str] = None,
        query: Optional[str] = None
    ) -> List[GarhwaliBook]:
        """
        List catalogued books with optional filters.

        Args:
            category: "works_in_garhwali", "grammar_and_linguistics", or "works_about_garhwali"
            author: Substring to filter by author name
            genre: Substring to filter by genre
            query: Substring search across title, author, genre, category, and publisher
        """
        books = _load_bibliography()
        res = books
        if category:
            cat_lower = category.lower().strip()
            res = [b for b in res if b.category.lower() == cat_lower]
        if author:
            auth_lower = author.lower().strip()
            res = [b for b in res if auth_lower in b.author.lower()]
        if genre:
            genre_lower = genre.lower().strip()
            res = [b for b in res if genre_lower in b.genre.lower()]
        if query:
            q_lower = query.lower().strip()
            res = [
                b for b in res
                if q_lower in b.title.lower()
                or q_lower in b.author.lower()
                or q_lower in b.genre.lower()
                or q_lower in b.category_label.lower()
                or q_lower in b.publisher.lower()
            ]
        return res

    @staticmethod
    def get_book(book_id: int) -> Optional[GarhwaliBook]:
        """Retrieve a specific catalogued book by ID."""
        for b in _load_bibliography():
            if b.id == book_id:
                return b
        return None

    @staticmethod
    def search(query: str) -> List[GarhwaliBook]:
        """Search books by keyword across title, author, genre, or publisher."""
        return BibliographyTreasury.list_books(query=query)

    @staticmethod
    def primary_corpus_books() -> List[GarhwaliBook]:
        """Get verified primary texts written IN Garhwali, suitable for pure NLP corpora."""
        return [b for b in _load_bibliography() if getattr(b, 'corpus_eligibility', '') == 'primary_native_corpus']

    @staticmethod
    def reference_books() -> List[GarhwaliBook]:
        """Get scholarly reference books ABOUT Garhwali (grammars, dictionaries, studies)."""
        return [b for b in _load_bibliography() if getattr(b, 'corpus_eligibility', '') != 'primary_native_corpus']

    @staticmethod
    def categories() -> Dict[str, str]:
        """Get available categories and their human-readable labels."""
        return {
            "works_in_garhwali": "Works Written In Garhwali (Literature & Texts)",
            "grammar_and_linguistics": "Garhwali Grammar, Lexicography & Linguistics",
            "works_about_garhwali": "Works About Garhwali (Criticism, History & Folk Studies)",
            "dictionaries": "Garhwali Dictionaries & Lexicons"
        }

    @staticmethod
    def authors() -> List[str]:
        """Get unique list of authors in the bibliography."""
        seen = set()
        out = []
        for b in _load_bibliography():
            if b.author and b.author not in seen:
                seen.add(b.author)
                out.append(b.author)
        return sorted(out)

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Summary statistics of catalogued Garhwali literature."""
        books = _load_bibliography()
        from collections import Counter
        cat_counts = Counter(b.category for b in books)
        primary_count = sum(1 for b in books if getattr(b, 'corpus_eligibility', '') == 'primary_native_corpus')
        reference_count = len(books) - primary_count
        return {
            "total_books": len(books),
            "primary_corpus_books": primary_count,
            "reference_scholarly_books": reference_count,
            "works_in_garhwali": cat_counts.get("works_in_garhwali", 0),
            "grammar_and_linguistics": cat_counts.get("grammar_and_linguistics", 0),
            "works_about_garhwali": cat_counts.get("works_about_garhwali", 0),
            "dictionaries": cat_counts.get("dictionaries", 0),
            "unique_authors": len(BibliographyTreasury.authors())
        }


# Module convenience functions
def get_bibliography() -> List[GarhwaliBook]:
    """Return all catalogued Garhwali books."""
    return BibliographyTreasury.list_books()


def search_books(query: str) -> List[GarhwaliBook]:
    """Search Garhwali books by keyword."""
    return BibliographyTreasury.search(query)


def get_book_by_id(book_id: int) -> Optional[GarhwaliBook]:
    """Get a Garhwali book by ID."""
    return BibliographyTreasury.get_book(book_id)


def get_works_in_garhwali() -> List[GarhwaliBook]:
    """Get literature and books written in Garhwali."""
    return BibliographyTreasury.list_books(category="works_in_garhwali")


def get_grammar_books() -> List[GarhwaliBook]:
    """Get books on Garhwali grammar, lexicography and linguistics."""
    return BibliographyTreasury.list_books(category="grammar_and_linguistics")


def get_primary_corpus_books() -> List[GarhwaliBook]:
    """Return books suitable for training or building primary Garhwali NLP corpora."""
    return BibliographyTreasury.primary_corpus_books()


def get_reference_books() -> List[GarhwaliBook]:
    """Return scholarly reference works about Garhwali language and literature."""
    return BibliographyTreasury.reference_books()

