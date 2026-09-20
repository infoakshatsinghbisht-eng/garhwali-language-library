# -*- coding: utf-8 -*-
"""Test suite for Garhwali core functionality."""

import unittest
import sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import garhwali

class TestGarhwaliCore(unittest.TestCase):
    def test_version(self):
        self.assertEqual(garhwali.__version__, "1.0.0")

    def test_total_word_forms(self):
        total = garhwali.total_word_forms()
        self.assertGreaterEqual(total, 300000, f"Expected >= 300,000 word forms, got {total}")

    def test_phonetics_and_syllables(self):
        sylls = garhwali.syllables("गढ़वाली")
        self.assertTrue(len(sylls) > 0)
        roman = garhwali.devanagari_to_latin("ब्वै कख छिन?")
        self.assertIn("kakh", roman.lower())

    def test_numbers_converter(self):
        self.assertEqual(garhwali.num_to_words(1), "एक")
        self.assertEqual(garhwali.num_to_words(5), "पाँच")
        self.assertEqual(garhwali.num_to_words(10), "दस")
        self.assertEqual(garhwali.to_devanagari_numerals(2026), "२०२६")

    def test_culture_and_lore(self):
        pr = garhwali.proverbs.all()
        self.assertTrue(len(pr) > 0)
        rd = garhwali.riddles.all()
        self.assertTrue(len(rd) > 0)
        fest = garhwali.list_festivals()
        self.assertTrue(len(fest) > 0)
        season = garhwali.get_current_season()
        self.assertIn("name_garhwali", season)

if __name__ == "__main__":
    unittest.main()
