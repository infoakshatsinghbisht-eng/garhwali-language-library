# -*- coding: utf-8 -*-
"""Unit tests for full-text digital books and page-by-page reader."""

import unittest
import garhwali
from garhwali.culture.books import BooksCorpus, BookPage, GarhwaliDigitalBook


class TestGarhwaliBooksCorpus(unittest.TestCase):
    """Test suite for full-text Garhwali digital books corpus and reader."""

    def test_list_books(self):
        books = garhwali.list_digital_books()
        self.assertIsInstance(books, list)
        self.assertGreaterEqual(len(books), 10)
        book_ids = [b["id"] for b in books]
        self.assertIn("grierson_1916_central_pahari", book_ids)
        self.assertIn("upreti_1894_proverbs_folklore", book_ids)
        self.assertIn("chatak_1959_garhwali_bhasha", book_ids)

    def test_total_pages_count(self):
        total_pages = BooksCorpus.total_pages_in_library()
        self.assertGreaterEqual(total_pages, 3000)

    def test_get_book(self):
        book = garhwali.get_digital_book("grierson_1916_central_pahari")
        self.assertIsNotNone(book)
        self.assertIsInstance(book, GarhwaliDigitalBook)
        self.assertEqual(book.author, "Sir George Abraham Grierson")
        self.assertGreater(book.total_pages, 900)

    def test_get_page(self):
        page = garhwali.read_book_page("chatak_1959_garhwali_bhasha", 1)
        self.assertIsNotNone(page)
        self.assertIsInstance(page, BookPage)
        self.assertEqual(page.page_number, 1)
        self.assertGreater(len(page.text), 10)
        snippet = page.snippet(max_chars=50)
        self.assertIsInstance(snippet, str)

    def test_book_search(self):
        book = garhwali.get_digital_book("chatak_1959_garhwali_bhasha")
        self.assertIsNotNone(book)
        results = book.search("भाषा")
        self.assertGreater(len(results), 0)
        first = results[0]
        self.assertIn("भाषा", first.snippet)
        self.assertGreaterEqual(first.page_number, 1)

    def test_cross_book_search(self):
        results = garhwali.search_digital_books("गढ़वाल")
        self.assertGreater(len(results), 5)


if __name__ == "__main__":
    unittest.main()
