# -*- coding: utf-8 -*-
r"""Test suite for Garhwali grammar, declensions, conjugations, and syntax."""

import unittest
import sys
from pathlib import Path
root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import garhwali
from garhwali.grammar.nouns import GarhwaliNoun, CORE_GARHWALI_NOUNS
from garhwali.grammar.verbs import GarhwaliVerb, CORE_GARHWALI_VERBS
from garhwali.grammar.syntax import validate_sov_order, check_split_ergativity, format_sentence

class TestGarhwaliGrammar(unittest.TestCase):
    def test_noun_declensions_masculine(self):
        noun = GarhwaliNoun("नौन", "m", english="boy", hindi="लड़का")
        decls = noun.declensions()
        self.assertEqual(decls["direct_sg"], "नौन")
        self.assertIn("नौन", decls["direct_pl"])
        self.assertIn("ले", decls["ergative_sg"])
        self.assertIn("मा", decls["locative"])

    def test_noun_declensions_feminine(self):
        noun = GarhwaliNoun("नौनी", "f", english="girl", hindi="लड़की")
        decls = noun.declensions()
        self.assertEqual(decls["direct_sg"], "नौनी")
        self.assertEqual(decls["direct_pl"], "नौनीयाँ")
        self.assertIn("ले", decls["ergative_sg"])
        self.assertIn("मा", decls["locative"])

    def test_verb_conjugation_transitive(self):
        verb = GarhwaliVerb("खा", "to eat", "खाना", is_transitive=True)
        conjs = verb.conjugate()
        self.assertEqual(conjs["infinitive"], "खाण")
        self.assertEqual(conjs["past_simple"]["3sg_m"], "खायो")
        self.assertEqual(conjs["future"]["1sg_m"], "खौलो")
        self.assertIn(conjs["imperative"]["polite_formal"], ("खावा", "खाया"))
        self.assertIn("झन्", conjs["imperative"]["prohibition_informal"])

    def test_verb_conjugation_intransitive(self):
        verb = GarhwaliVerb("जा", "to go", "जाना", is_transitive=False)
        conjs = verb.conjugate()
        self.assertEqual(conjs["infinitive"], "जाण")
        self.assertEqual(conjs["past_simple"]["3sg_m"], "गयो")
        self.assertEqual(conjs["past_simple"]["3sg_f"], "गै")

    def test_split_ergativity_transitive(self):
        res_invalid = check_split_ergativity("मी", "खायो", is_past_transitive=True)
        self.assertFalse(res_invalid["valid"])
        self.assertEqual(res_invalid["recommended_subject"], "मैंन")

        res_valid = check_split_ergativity("मैंन", "खायो", is_past_transitive=True)
        self.assertTrue(res_valid["valid"])

    def test_split_ergativity_intransitive(self):
        res_invalid = check_split_ergativity("मैंन", "गयूं", is_past_transitive=False)
        self.assertFalse(res_invalid["valid"])

        res_valid = check_split_ergativity("मी", "गयूं", is_past_transitive=False)
        self.assertTrue(res_valid["valid"])

    def test_sov_sentence_formation(self):
        sent = format_sentence("मी", "घौर", "जांदु छौं")
        self.assertEqual(sent, "मी घौर जांदु छौं।")
        
        neg_sent = format_sentence("मी", "घौर", "जांदु छौं", negative=True)
        self.assertEqual(neg_sent, "मी घौर नि जांदु छौं।")

        is_valid, _ = validate_sov_order(sent.split())
        self.assertTrue(is_valid)

if __name__ == "__main__":
    unittest.main()
