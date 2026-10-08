# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Deities, Kshetrapals, Nagrajas, Shaktipeeths, and Jagar Invocations."""

import unittest
from garhwali.culture.deities import DeitiesTreasury, GarhwaliDeity


class TestGarhwaliDeities(unittest.TestCase):
    """Test suite for Garhwali deities and sacred lore."""

    def test_deities_list(self):
        deities = DeitiesTreasury.list()
        self.assertGreaterEqual(len(deities), 15, "Should contain at least 15 documented deities")
        self.assertIsInstance(deities[0], GarhwaliDeity)

    def test_get_deity(self):
        dhari = DeitiesTreasury.get("dhari_devi")
        self.assertIsNotNone(dhari)
        self.assertIn("धारी देवी", dhari.name_garhwali)
        self.assertEqual(dhari.category, "shakti")

        mahasu = DeitiesTreasury.get("botha_mahasu")
        self.assertIsNotNone(mahasu)
        self.assertIn("महासू", mahasu.name_garhwali)
        self.assertTrue(any("Hanol" in s for s in mahasu.primary_shrines))

        sem = DeitiesTreasury.get("sem_mukhem_nagraja")
        self.assertIsNotNone(sem)
        self.assertTrue(any("Sem" in s for s in sem.primary_shrines))

    def test_search_deities(self):
        nagas = DeitiesTreasury.search("नागराज")
        self.assertGreaterEqual(len(nagas), 1)

        bairavs = DeitiesTreasury.search("भैरव")
        self.assertGreaterEqual(len(bairavs), 1)

    def test_stats(self):
        stats = DeitiesTreasury.stats()
        self.assertGreaterEqual(stats["total_deities"], 18)
        self.assertIn("categories", stats)
        self.assertIn("by_category", stats)


if __name__ == "__main__":
    unittest.main()
