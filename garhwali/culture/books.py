# -*- coding: utf-8 -*-
"""
Full-Text Digital Book Corpus and Page-by-Page Reader for Garhwali Language.

Provides access to 13 complete digitised historical, linguistic, and literary books
comprising over 3,000 pages of authentic Garhwali texts, grammars, folk epics,
and linguistic surveys.
"""

import json
import os
import re
from typing import Dict, List, Optional, Any, Generator
from dataclasses import dataclass


@dataclass
class BookPage:
    page_number: int
    text: str
    book_id: str
    book_title: str

    def snippet(self, max_chars: int = 200) -> str:
        clean = " ".join(self.text.split())
        if len(clean) <= max_chars:
            return clean
        return clean[:max_chars] + "..."


@dataclass
class BookSearchResult:
    book_id: str
    book_title: str
    page_number: int
    snippet: str
    match_count: int


class GarhwaliBook:
    """Represents a complete digitised book with page-by-page access."""

    def __init__(self, data: Dict[str, Any]):
        self.id: str = data.get("id", "")
        self.title: str = data.get("title", "")
        self.author: str = data.get("author", "")
        self.year: int = data.get("year", 0)
        self.language: str = data.get("language", "")
        self.category: str = data.get("category", "")
        self.description: str = data.get("description", "")
        self.total_pages: int = data.get("total_pages", 0)
        self.chapters_detected: List[str] = data.get("chapters_detected", [])
        self._raw_pages: List[Dict[str, Any]] = data.get("pages", [])
        self._pages_cache: Optional[List[BookPage]] = None

    @property
    def pages(self) -> List[BookPage]:
        if self._pages_cache is None:
            self._pages_cache = [
                BookPage(
                    page_number=p.get("page_number", idx + 1),
                    text=p.get("text", ""),
                    book_id=self.id,
                    book_title=self.title
                )
                for idx, p in enumerate(self._raw_pages)
            ]
        return self._pages_cache

    def get_page(self, page_number: int) -> Optional[BookPage]:
        """Retrieve a specific page by 1-indexed page number."""
        if 1 <= page_number <= len(self.pages):
            return self.pages[page_number - 1]
        for p in self.pages:
            if p.page_number == page_number:
                return p
        return None

    def search(self, query: str, ignore_case: bool = True) -> List[BookSearchResult]:
        """Search for a keyword or phrase across all pages of this book."""
        results = []
        flags = re.IGNORECASE if ignore_case else 0
        pattern = re.compile(re.escape(query), flags)

        for p in self.pages:
            matches = list(pattern.finditer(p.text))
            if matches:
                # Find best snippet around first match
                m = matches[0]
                start = max(0, m.start() - 60)
                end = min(len(p.text), m.end() + 80)
                snip = " ".join(p.text[start:end].split())
                results.append(
                    BookSearchResult(
                        book_id=self.id,
                        book_title=self.title,
                        page_number=p.page_number,
                        snippet=f"...{snip}...",
                        match_count=len(matches)
                    )
                )
        return results

    def __repr__(self) -> str:
        return f"<GarhwaliBook '{self.title}' ({self.year}) by {self.author} - {self.total_pages} pages>"


class BooksCorpus:
    """Master repository and reader for complete Garhwali digital books."""

    _BOOKS_DIR = os.path.join(os.path.dirname(__file__), "data", "books")
    _INDEX_CACHE: Optional[List[Dict[str, Any]]] = None
    _LOADED_BOOKS: Dict[str, GarhwaliBook] = {}

    @classmethod
    def _load_index(cls) -> List[Dict[str, Any]]:
        if cls._INDEX_CACHE is not None:
            return cls._INDEX_CACHE
        index_file = os.path.join(cls._BOOKS_DIR, "index.json")
        if os.path.exists(index_file):
            with open(index_file, "r", encoding="utf-8") as f:
                cls._INDEX_CACHE = json.load(f)
        else:
            cls._INDEX_CACHE = []
        return cls._INDEX_CACHE

    @classmethod
    def list_books(cls) -> List[Dict[str, Any]]:
        """List all available complete books in the library with metadata and total pages."""
        return cls._load_index()

    @classmethod
    def get_book(cls, book_id: str) -> Optional[GarhwaliBook]:
        """Load and return a complete book by its identifier (e.g. 'grierson_1916_central_pahari')."""
        if book_id in cls._LOADED_BOOKS:
            return cls._LOADED_BOOKS[book_id]

        file_path = os.path.join(cls._BOOKS_DIR, f"{book_id}.json")
        if not os.path.exists(file_path):
            # Try fuzzy match in index
            for b in cls._load_index():
                if book_id.lower() in b["id"].lower():
                    file_path = os.path.join(cls._BOOKS_DIR, f"{b['id']}.json")
                    break

        if not os.path.exists(file_path):
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        book = GarhwaliBook(data)
        cls._LOADED_BOOKS[book.id] = book
        return book

    @classmethod
    def read_page(cls, book_id: str, page_number: int) -> Optional[BookPage]:
        """Read a specific page from a book directly."""
        book = cls.get_book(book_id)
        if book:
            return book.get_page(page_number)
        return None

    @classmethod
    def search_all_books(cls, query: str) -> List[BookSearchResult]:
        """Search across all 13 complete books in the library."""
        all_results = []
        for meta in cls.list_books():
            book = cls.get_book(meta["id"])
            if book:
                all_results.extend(book.search(query))
        return all_results

    @classmethod
    def total_pages_in_library(cls) -> int:
        """Calculate total number of digitised pages available across all books."""
        return sum(b.get("total_pages", 0) for b in cls.list_books())


GarhwaliDigitalBook = GarhwaliBook


def read_book_page(book_id: str, page_number: int) -> Optional[BookPage]:
    """Read a specific page from a digital book in the library."""
    return BooksCorpus.read_page(book_id, page_number)


def list_digital_books() -> List[Dict[str, Any]]:
    """List all available full-text digital books in the library."""
    return BooksCorpus.list_books()


def get_digital_book(book_id: str) -> Optional[GarhwaliDigitalBook]:
    """Get a full-text digital book by its ID."""
    return BooksCorpus.get_book(book_id)


def search_digital_books(query: str) -> List[BookSearchResult]:
    """Search for text across all digitised books in the library."""
    return BooksCorpus.search_all_books(query)
