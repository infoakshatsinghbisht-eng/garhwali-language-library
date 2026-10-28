# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Lexicon, Dictionary, Proverbs, Phrases, and Riddles."""

import unittest
import garhwali
from garhwali.lexicon.dictionary import GarhwaliDictionary


class TestGarhwaliLexicon(unittest.TestCase):
    """Test suite for Garhwali Lexicon."""

    def setUp(self):
        self.d = GarhwaliDictionary()

    def test_total_words_count(self):
        words = self.d.all_words()
        self.assertGreaterEqual(len(words), 3300, "Dictionary should have at least 3300 authenticated words")

    def test_extracted_words_lookup(self):
        # Topography & Nature
        danda = self.d.lookup("डांडा")
        self.assertIsNotNone(danda)
        self.assertEqual(danda["category"], "nature")
        self.assertIn("mountain", danda["english"].lower())

        bugyal = self.d.lookup("बुग्याल")
        self.assertIsNotNone(bugyal)
        self.assertIn("alpine meadow", bugyal["english"].lower())

        buransh = self.d.lookup("बुराँश")
        self.assertIsNotNone(buransh)
        self.assertIn("rhododendron", buransh["english"].lower())

        kafal = self.d.lookup("काफल")
        self.assertIsNotNone(kafal)
        self.assertIn("bayberry", kafal["english"].lower())

        # Implements & Architecture
        ukhal = self.d.lookup("उखल")
        self.assertIsNotNone(ukhal)
        self.assertIn("mortar", ukhal["english"].lower())

        ghatt = self.d.lookup("घट्ट")
        self.assertIsNotNone(ghatt)
        self.assertIn("watermill", ghatt["english"].lower())

        tibaari = self.d.lookup("तिबारी")
        self.assertIsNotNone(tibaari)
        self.assertIn("veranda", tibaari["english"].lower())

        # Food & Cuisine
        kafli = self.d.lookup("कफली")
        self.assertIsNotNone(kafli)
        self.assertIn("spinach", kafli["english"].lower())

        phaandu = self.d.lookup("फांडू")
        self.assertIsNotNone(phaandu)
        self.assertIn("lentil", phaandu["english"].lower())

        # Music & Instruments
        hurka = self.d.lookup("हुड़का")
        self.assertIsNotNone(hurka)
        self.assertIn("drum", hurka["english"].lower())

        damau = self.d.lookup("दमाऊँ")
        self.assertIsNotNone(damau)
        self.assertIn("kettle-drum", damau["english"].lower())

    def test_newly_mined_words_lookup(self):
        # Historical & administrative terms
        garhpati = self.d.lookup("गढपति")
        self.assertIsNotNone(garhpati)
        self.assertIn("fortress", garhpati["english"].lower())

        thaatwan = self.d.lookup("थातवान")
        self.assertIsNotNone(thaatwan)
        self.assertIn("landowner", thaatwan["english"].lower())

        # Alpine topography & geography
        dhura = self.d.lookup("धुरा")
        self.assertIsNotNone(dhura)
        self.assertIn("pass", dhura["english"].lower())

        prayag = self.d.lookup("प्रयाग")
        self.assertIsNotNone(prayag)
        self.assertIn("confluence", prayag["english"].lower())

        # Rituals & pilgrimage
        rajjaat = self.d.lookup("राजजात")
        self.assertIsNotNone(rajjaat)
        self.assertIn("pilgrimage", rajjaat["english"].lower())

        # Verbs & actions
        hernu = self.d.lookup("हेरणु")
        self.assertIsNotNone(hernu)
        self.assertEqual(hernu["pos"], "verb")
        self.assertIn("search", hernu["english"].lower())

        # Descriptors
        dhundlo = self.d.lookup("धुंदळो")
        self.assertIsNotNone(dhundlo)
        self.assertIn("hazy", dhundlo["english"].lower())

        # Domestic life & dairy culture
        ghyoo = self.d.lookup("घ्यू")
        self.assertIsNotNone(ghyoo)
        self.assertIn("butter", ghyoo["english"].lower())

        # Customary matrimonial & adornment
        taka = self.d.lookup("टका-ब्याव")
        self.assertIsNotNone(taka)
        self.assertIn("marriage", taka["english"].lower())

        hansuli = self.d.lookup("हंसुली")
        self.assertIsNotNone(hansuli)
        self.assertIn("silver", hansuli["english"].lower())

    def test_dictionary_search(self):
        results = self.d.search("mother")
        self.assertGreater(len(results), 0)
        self.assertTrue(any(r["garhwali"] in ["ब्वै", "ब्वे", "माई"] for r in results))

        results_water = self.d.search("water")
        self.assertGreater(len(results_water), 0)

    def test_proverbs(self):
        pr_list = self.d.all_proverbs()
        self.assertGreaterEqual(len(pr_list), 20)

        # Check Madho Singh / Maletha proverb
        gaje_pr = [p for p in pr_list if "मलेथे" in p.get("pakhana", "")]
        self.assertEqual(len(gaje_pr), 1)

        # Check Kafua proverb
        kaphua_pr = [p for p in pr_list if "कफू पाको" in p.get("pakhana", "")]
        self.assertEqual(len(kaphua_pr), 1)

    def test_phrases_and_idioms(self):
        ph_list = self.d.all_phrases()
        self.assertGreaterEqual(len(ph_list), 35)

        # Check khuded idiom
        khuded_ph = [p for p in ph_list if "खुदेड़" in p.get("garhwali", "")]
        self.assertGreaterEqual(len(khuded_ph), 1)

    def test_riddles(self):
        r_list = self.d.all_riddles()
        self.assertGreaterEqual(len(r_list), 10)

    def test_top_level_wrappers(self):
        w = garhwali.lookup("बुराँश")
        self.assertIsNotNone(w)

        all_pr = garhwali.proverbs.all()
        self.assertGreaterEqual(len(all_pr), 20)

        rand_pr = garhwali.proverbs.random()
        self.assertIsNotNone(rand_pr)

        forms_count = garhwali.total_word_forms()
        self.assertGreater(forms_count, 1000000)


if __name__ == "__main__":
    unittest.main()
