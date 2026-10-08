# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Places, Panch Kedar, Panch Badri, Panch Prayag, and Sacred Geography."""

import unittest
from garhwali.culture.places import PlacesTreasury, GarhwaliPlace


class TestGarhwaliPlaces(unittest.TestCase):
    """Test suite for Garhwali sacred geography and places."""

    def test_places_list(self):
        places = PlacesTreasury.list()
        self.assertGreaterEqual(len(places), 40, "Should contain at least 40 documented places")
        self.assertIsInstance(places[0], GarhwaliPlace)

    def test_panch_kedar(self):
        kedars = PlacesTreasury.panch_kedar()
        self.assertEqual(len(kedars), 5, "Panch Kedar must contain exactly 5 shrines")
        kedar_ids = {k.id for k in kedars}
        self.assertIn("kedarnath", kedar_ids)
        self.assertIn("tungnath", kedar_ids)
        self.assertIn("rudranath", kedar_ids)
        self.assertIn("madhyamaheshwar", kedar_ids)
        self.assertIn("kalpeshwar", kedar_ids)

    def test_panch_badri(self):
        badris = PlacesTreasury.panch_badri()
        self.assertEqual(len(badris), 5, "Panch Badri must contain exactly 5 shrines")
        badri_ids = {b.id for b in badris}
        self.assertIn("badrinath", badri_ids)
        self.assertIn("bhavishya_badri", badri_ids)
        self.assertIn("vriddha_badri", badri_ids)
        self.assertIn("dhyan_badri", badri_ids)
        self.assertIn("adi_badri", badri_ids)

    def test_panch_prayag(self):
        prayags = PlacesTreasury.panch_prayag()
        self.assertEqual(len(prayags), 5, "Panch Prayag must contain exactly 5 confluences")
        prayag_ids = {p.id for p in prayags}
        self.assertIn("devprayag", prayag_ids)
        self.assertTrue(any("rudraprayag" in p for p in prayag_ids))
        self.assertIn("karnaprayag", prayag_ids)
        self.assertIn("nandaprayag", prayag_ids)
        self.assertIn("vishnuprayag", prayag_ids)


    def test_get_place(self):
        kedar = PlacesTreasury.get("kedarnath")
        self.assertIsNotNone(kedar)
        self.assertIn("केदारनाथ", kedar.name_garhwali)
        self.assertEqual(kedar.district, "Rudraprayag")

        badri = PlacesTreasury.get("badrinath")
        self.assertIsNotNone(badri)
        self.assertEqual(badri.id, "badrinath")

    def test_search_places(self):
        chamoli_places = PlacesTreasury.search("Chamoli")
        self.assertGreaterEqual(len(chamoli_places), 10)

        bugyals = PlacesTreasury.list(category="bugyal")
        self.assertGreaterEqual(len(bugyals), 4)

    def test_stats(self):
        stats = PlacesTreasury.stats()
        self.assertGreaterEqual(stats["total_places"], 45)
        self.assertIn("categories", stats)
        self.assertIn("districts", stats)


if __name__ == "__main__":
    unittest.main()
