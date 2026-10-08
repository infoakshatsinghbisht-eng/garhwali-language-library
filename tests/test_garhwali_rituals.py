# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Ritual Items, Temple Implements, Vessels, and Attire."""

import unittest
from garhwali.culture.rituals import RitualsTreasury, GarhwaliRitualItem


class TestGarhwaliRituals(unittest.TestCase):
    """Test suite for Garhwali ritual items and temple implements."""

    def test_rituals_list(self):
        items = RitualsTreasury.list()
        self.assertGreaterEqual(len(items), 20, "Should contain at least 20 documented ritual objects")
        self.assertIsInstance(items[0], GarhwaliRitualItem)

    def test_get_ritual_item(self):
        pithya = RitualsTreasury.get("pithya")
        self.assertIsNotNone(pithya)
        self.assertIn("पिठ्याँ", pithya.name_garhwali)

        dhol = RitualsTreasury.get("dhol")
        self.assertIsNotNone(dhol)
        self.assertEqual(dhol.category, "Jagar & Musical Implement")

        bhankora = RitualsTreasury.get("bhankora")
        self.assertIsNotNone(bhankora)
        self.assertIn("सीधा", bhankora.name_hindi)

        nath = RitualsTreasury.get("tehri_nath")
        self.assertIsNotNone(nath)
        self.assertEqual(nath.category, "Sacred Attire & Ornaments")

    def test_search_rituals(self):
        implements = RitualsTreasury.search("copper")
        self.assertGreaterEqual(len(implements), 3)

        vessels = RitualsTreasury.search("Vessel")
        self.assertGreaterEqual(len(vessels), 3)

    def test_stats(self):
        stats = RitualsTreasury.stats()
        self.assertGreaterEqual(stats["total_ritual_items"], 20)
        self.assertIn("categories", stats)


if __name__ == "__main__":
    unittest.main()
