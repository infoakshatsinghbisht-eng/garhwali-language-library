# -*- coding: utf-8 -*-
"""Test suite for Garhwali Translator accuracy across English, Hindi, Hinglish."""

import unittest
import sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import garhwali

class TestGarhwaliTranslator(unittest.TestCase):
    def test_hinglish_translation(self):
        res = garhwali.translate("are yah chal kyon nahin raha hai")
        self.assertIn("किलै नि चलनो छ", res.text)
        self.assertEqual(res.source_lang, "hinglish")

    def test_english_translation(self):
        res = garhwali.translate("Where is mom?")
        self.assertIn("ब्वै", res.text)

    def test_kinship_terms(self):
        res = garhwali.translate("dad is at home")
        self.assertIn("बुबा", res.text)

    def test_dialect_inflection(self):
        std = garhwali.translate("What is your name?", dialect="srinagariya")
        rath = garhwali.translate("What is your name?", dialect="rathwali")
        sal = garhwali.translate("What is your name?", dialect="salani")
        self.assertIn("तुमरो", std.text)
        self.assertIn("तमरो", rath.text)
        self.assertIn("तुमारू", sal.text)

if __name__ == "__main__":
    unittest.main()
