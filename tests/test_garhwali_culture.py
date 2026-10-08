# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Culture, Bibliography, and Literature Modules."""

import unittest
from garhwali.culture.bibliography import (
    BibliographyTreasury,
    get_bibliography,
    search_books,
    get_book_by_id,
    get_works_in_garhwali,
    get_grammar_books,
    GarhwaliBook
)
from garhwali.culture.literature import (
    LiteratureTreasury,
    FolkEpic,
    FolkPoem,
    GarhwaliAuthor,
    poems,
    epics,
    authors,
    EPICS_DATA,
    POEMS_DATA,
    AUTHORS_DATA
)


class TestGarhwaliBibliography(unittest.TestCase):
    """Test suite for Master Garhwali Bibliography."""

    def test_bibliography_loading(self):
        books = get_bibliography()
        self.assertGreaterEqual(len(books), 50, "Bibliography should contain at least 50 catalogued books")
        self.assertIsInstance(books[0], GarhwaliBook)

    def test_bibliography_categories(self):
        stats = BibliographyTreasury.stats()
        self.assertIn("works_in_garhwali", stats)
        self.assertIn("grammar_and_linguistics", stats)
        self.assertIn("works_about_garhwali", stats)
        self.assertGreaterEqual(stats["works_in_garhwali"], 20)
        self.assertGreaterEqual(stats["grammar_and_linguistics"], 10)
        self.assertGreaterEqual(stats["works_about_garhwali"], 15)

    def test_search_books(self):
        chatak_books = search_books("चातक")
        self.assertGreaterEqual(len(chatak_books), 1, "Should find books by Dr. Govind Chatak")
        self.assertTrue(any("चातक" in b.author for b in chatak_books))

        grierson = search_books("Grierson")
        self.assertGreaterEqual(len(grierson), 1, "Should find Grierson's Linguistic Survey of India")

        meghdoot = search_books("मेघदूत")
        self.assertGreaterEqual(len(meghdoot), 1, "Should find Garhwali Meghdoot")

    def test_get_book_by_id(self):
        book1 = get_book_by_id(1)
        self.assertIsNotNone(book1)
        self.assertIn("सिंहनाद", book1.title)

        book_none = get_book_by_id(99999)
        self.assertIsNone(book_none)

    def test_category_filters(self):
        works = get_works_in_garhwali()
        self.assertGreater(len(works), 0)
        for w in works:
            self.assertEqual(w.category, "works_in_garhwali")

        grammar = get_grammar_books()
        self.assertGreater(len(grammar), 0)
        for g in grammar:
            self.assertEqual(g.category, "grammar_and_linguistics")

    def test_authors_list(self):
        auth_list = BibliographyTreasury.authors()
        self.assertGreaterEqual(len(auth_list), 20)
        self.assertTrue(any("चातक" in a for a in auth_list))


class TestGarhwaliLiterature(unittest.TestCase):
    """Test suite for Garhwali Literature, Folk Epics, and Authors."""

    def test_epics_data(self):
        epics_list = LiteratureTreasury.list_epics()
        self.assertGreaterEqual(len(epics_list), 5)

        madho = LiteratureTreasury.get_epic("madho_singh_bhandari")
        self.assertIsNotNone(madho)
        self.assertIn("माधो सिंह भंडारी", madho.title_garhwali)
        self.assertIn("मलेथा", madho.hero)

        jeetu = LiteratureTreasury.get_epic("jeetu_bagdwal")
        self.assertIsNotNone(jeetu)
        self.assertIn("जीतू", jeetu.hero)

        kaphua = LiteratureTreasury.get_epic("kaphua")
        self.assertIsNotNone(kaphua)
        self.assertIn("कफू पाको", kaphua.title_garhwali)

    def test_poems_data(self):
        poem_list = LiteratureTreasury.list_poems()
        self.assertGreaterEqual(len(poem_list), 3)

        chaitwali = [p for p in poem_list if p.id == "chaita_ki_chaitwali"][0]
        self.assertIn("बुराँश", chaitwali.verses_garhwali[0])

        bedu = [p for p in poem_list if p.id == "bedu_pako_baramasa"][0]
        self.assertIn("बेड़ू पाको", bedu.title_garhwali)

    def test_authors_data(self):
        auth_list = LiteratureTreasury.list_authors()
        self.assertGreaterEqual(len(auth_list), 8)

        bartwal = LiteratureTreasury.get_author("chandra_kunwar_bartwal")
        self.assertIsNotNone(bartwal)
        self.assertIn("कालिदास", bartwal.significance)

        negi = LiteratureTreasury.get_author("narendra_singh_negi")
        self.assertIsNotNone(negi)
        self.assertIn("गाड़-कुथार", negi.famous_works[0])

    def test_backward_compatibility(self):
        p = poems()
        self.assertIsInstance(p, list)
        self.assertGreater(len(p), 0)

        e = epics()
        self.assertIsInstance(e, list)
        self.assertGreater(len(e), 0)

        a = authors()
        self.assertIsInstance(a, list)
        self.assertGreater(len(a), 0)


if __name__ == "__main__":
    unittest.main()
