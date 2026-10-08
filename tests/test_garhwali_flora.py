# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Ethnobotanical Flora, Sacred Trees, Alpine Herbs, and Crops."""

import unittest
from garhwali.culture.flora import FloraTreasury, GarhwaliPlant


class TestGarhwaliFlora(unittest.TestCase):
    """Test suite for Garhwali flora and ethnobotany."""

    def test_flora_list(self):
        plants = FloraTreasury.list()
        self.assertGreaterEqual(len(plants), 25, "Should contain at least 25 documented plants")
        self.assertIsInstance(plants[0], GarhwaliPlant)

    def test_get_plant(self):
        banjh = FloraTreasury.get("banjh")
        self.assertIsNotNone(banjh)
        self.assertEqual(banjh.scientific_name, "Quercus leucotrichophora")
        self.assertIn("बाँझ", banjh.name_garhwali)

        buransh = FloraTreasury.get("buransh")
        self.assertIsNotNone(buransh)
        self.assertEqual(buransh.scientific_name, "Rhododendron arboreum")

        brahma = FloraTreasury.get("brahma_kamal")
        self.assertIsNotNone(brahma)
        self.assertEqual(brahma.scientific_name, "Saussurea obvallata")

        manduwa = FloraTreasury.get("manduwa")
        self.assertIsNotNone(manduwa)
        self.assertEqual(manduwa.scientific_name, "Eleusine coracana")

    def test_search_flora(self):
        alpine = FloraTreasury.search("alpine")
        self.assertGreaterEqual(len(alpine), 5)

        medicinal = FloraTreasury.search("medicinal")
        self.assertGreaterEqual(len(medicinal), 5)

    def test_stats(self):
        stats = FloraTreasury.stats()
        self.assertGreaterEqual(stats["total_plants"], 25)
        self.assertIn("categories", stats)


if __name__ == "__main__":
    unittest.main()
