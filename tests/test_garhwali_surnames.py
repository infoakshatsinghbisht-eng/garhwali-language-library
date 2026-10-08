# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Surnames, Clans, Lineages, Gotras, and Social Structure."""

import unittest
from garhwali.culture.surnames import SurnamesTreasury, GarhwaliSurname


class TestGarhwaliSurnames(unittest.TestCase):
    """Test suite for Garhwali surnames and social structure."""

    def test_surnames_list(self):
        surnames = SurnamesTreasury.list()
        self.assertGreaterEqual(len(surnames), 20, "Should contain at least 20 documented lineages")
        self.assertIsInstance(surnames[0], GarhwaliSurname)

    def test_get_surname(self):
        khanduri = SurnamesTreasury.get("khanduri")
        self.assertIsNotNone(khanduri)
        self.assertEqual(khanduri.community, "Brahmin")
        self.assertIn("खंडूड़ी", khanduri.surname_garhwali)

        panwar = SurnamesTreasury.get("panwar")
        self.assertIsNotNone(panwar)
        self.assertEqual(panwar.community, "Rajput / Kshatriya")
        self.assertIn("Ajaypal", panwar.notable_historical_figures[1])

        bhandari = SurnamesTreasury.get("bhandari")
        self.assertIsNotNone(bhandari)
        self.assertIn("Madho Singh Bhandari", bhandari.notable_historical_figures[0])

        auji = SurnamesTreasury.get("auji_das")
        self.assertIsNotNone(auji)
        self.assertEqual(auji.community, "Shilpkar / Artisan")

    def test_social_concepts(self):
        concepts = SurnamesTreasury.social_concepts()
        self.assertIn("bhad", concepts)
        self.assertIn("dhol_sagar", concepts)
        self.assertIn("jagariya", concepts)
        self.assertIn("thokdaar", concepts)
        self.assertIn("beda_vart", concepts)

    def test_search_surnames(self):
        brahmins = SurnamesTreasury.search("Brahmin")
        self.assertGreaterEqual(len(brahmins), 8)

        rajputs = SurnamesTreasury.search("Rajput")
        self.assertGreaterEqual(len(rajputs), 8)

    def test_stats(self):
        stats = SurnamesTreasury.stats()
        self.assertGreaterEqual(stats["total_surnames"], 20)
        self.assertIn("communities", stats)
        self.assertGreaterEqual(stats["total_social_concepts"], 8)


if __name__ == "__main__":
    unittest.main()
