# -*- coding: utf-8 -*-
"""Comprehensive unit test suite for new Garhwali advanced features, grammar, numbers, voice, and culture."""

import unittest
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import garhwali
from garhwali.constants import ISO_639_3, ISO_639_NAME, Gender, Tense, Dialect, DAYS_OF_WEEK
from garhwali.grammar import (
    pluralize, to_feminine, to_masculine, to_oblique, make_diminutive, make_augmentative, decline_noun,
    attach_case, get_marker, extract_root, conjugate_to_be, conjugate, conjunctive_participle,
    causative, passive, medio_passive_inability, compound_verb, conditional, imperative, prohibitive,
    modal_ability, modal_obligation, modal_desiderative, build_sentence, interrogative_sentence,
    relative_correlative, echo_word, SyntaxEngine
)
from garhwali.numbers import num_to_words, words_to_num, fraction, from_devanagari_numerals, to_devanagari_numerals
from garhwali.voice import voice_translate, VoiceTranslator, GarhwaliVoiceSynthesizer
from garhwali.culture import FolkloreTreasury, GarhwaliHoliSong


class TestGarhwaliAdvanced(unittest.TestCase):

    def test_constants_and_iso(self):
        self.assertEqual(garhwali.ISO_639_3, "gbm")
        self.assertEqual(garhwali.ISO_639_NAME, "Garhwali")
        self.assertTrue(any("सोम" in d for d in DAYS_OF_WEEK))
        self.assertEqual(garhwali.Tense.PRESENT.value, "present")
        self.assertEqual(garhwali.Gender.MASCULINE.value, "m")

    def test_noun_morphology(self):
        self.assertEqual(pluralize("लड़का"), "लड़का")
        self.assertEqual(pluralize("घोड़ा"), "घोड़ा")
        self.assertEqual(to_feminine("लड़का"), "लड़की")
        self.assertEqual(to_feminine("घोडो"), "घोडी")
        self.assertIn(to_masculine("लड़की"), ("लड़का", "लड़को"))
        self.assertEqual(to_oblique("लड़का", number="singular"), "लड़का")
        self.assertEqual(to_oblique("लड़का", number="plural"), "लड़कौं")
        self.assertIn(make_diminutive("डांडा"), ("डांडी", "डांडू"))
        self.assertIn(make_augmentative("गाड़"), ("गाड़ा", "गडोला"))
        
        dec = decline_noun("लड़का", gender="M")
        self.assertIn("direct_sg", dec)
        self.assertIn("ergative_sg", dec)
        self.assertIn("ablative", dec)

    def test_postpositions_and_cases(self):
        from garhwali.grammar import CASE_MARKERS
        m = CASE_MARKERS["ergative"]
        self.assertEqual(m.name, "ergative")
        self.assertIn("न", m.allomorphs)
        
        marker_str = get_marker("ergative")
        self.assertIn(marker_str, ("न", "ले"))
        
        att_erg = attach_case("राम", "ergative")
        self.assertEqual(att_erg, "राम न")
        
        att_abl = attach_case("श्रीनगर", "ablative")
        self.assertIn("बटी", att_abl)
        
        att_acc = attach_case("मोहन", "accusative_dative")
        self.assertIn("ते", att_acc)


    def test_verb_derivations(self):
        self.assertEqual(extract_root("खाणु"), "खा")
        self.assertEqual(extract_root("जाण"), "जा")
        
        aux_pres = conjugate_to_be(person=3, number="singular", tense="present")
        self.assertIn(aux_pres, ("च", "छ"))
        
        aux_pl = conjugate_to_be(person=3, number="plural", tense="present")
        self.assertEqual(aux_pl, "छन")
        
        cp = conjunctive_participle("खाणु")
        self.assertEqual(cp, "खाईक")
        
        c1 = causative("खाणु", grade=1)
        self.assertEqual(c1, "खिलौण")
        
        c2 = causative("खाणु", grade=2)
        self.assertEqual(c2, "खिलवाण")
        
        pas = passive("खाणु")
        self.assertIn(pas, ("खाये जाण", "खााईण", "खवाईण"))
        
        mp = medio_passive_inability("खाणु", "मि")
        self.assertIn("नि जांद", mp)
        
        comp = compound_verb("खाणु", "लेणु")
        self.assertIn("खाइ", comp)
        
        cond = conditional("घाम लगलो", "चलौला")
        self.assertIn("त", cond)
        
        imp_pl = imperative("खाणु", honorific=True, plural=True)
        self.assertEqual(imp_pl, "खावा")
        
        proh = prohibitive("खाणु", honorific=True)
        self.assertEqual(proh, "झनि खावा")
        
        mod_ab = modal_ability("खाणु", person=3, gender="M", tense="present")
        self.assertIn("सकदू", mod_ab)
        
        mod_ob = modal_obligation("जाणु", "मिते", urgency="need")
        self.assertIn("चैं", mod_ob)
        
        mod_des = modal_desiderative("खाणु", "मी", tense="present")
        self.assertIn("चांदू", mod_des)

    def test_syntax_engine(self):
        sent = build_sentence("राम", direct_object="भात", verb="खाणु", tense="present", person=3, gender="m")
        self.assertIn("राम", sent)
        self.assertIn("भात", sent)
        
        polar_q = interrogative_sentence("तुम घर जाणा छा", question_type="polar")
        self.assertIn("क्या", polar_q)
        
        rc = relative_correlative("जो मेहनत करलो", "सो फल पालो")
        self.assertIn("जो", rc)
        self.assertIn("सो", rc)
        
        echo = echo_word("रोटी")
        self.assertEqual(echo, "रोटी-शोटी")
        echo_p = echo_word("पाणी")
        self.assertEqual(echo_p, "पाणी-शाणी")

    def test_numbers_and_fractions(self):
        w = num_to_words(25)
        self.assertEqual(w, "बीस पाँच")
        
        n_parsed = words_to_num("एक सौ बीस")
        self.assertEqual(n_parsed, 120)
        
        dev_digits = to_devanagari_numerals(42)
        self.assertEqual(dev_digits, "४२")
        
        latin_digits = from_devanagari_numerals("४२")
        self.assertEqual(latin_digits, "42")
        
        self.assertEqual(fraction("आधा"), 0.5)
        self.assertEqual(fraction("डेढ़"), 1.5)
        self.assertEqual(fraction("ढाई"), 2.5)
        self.assertEqual(fraction("सवा"), 1.25)
        self.assertEqual(fraction("पौणा"), 0.75)

    def test_voice_translation_and_synthesizer(self):
        vt_res = voice_translate("Hello, how are you?", generate_audio=True)
        self.assertIsNotNone(vt_res.translated_text)
        self.assertIsNotNone(vt_res.romanized)
        self.assertTrue(len(vt_res.syllables) > 0)
        self.assertIn("<speak>", vt_res.ssml)
        self.assertIsNotNone(vt_res.audio_wav_base64)
        
        wav_bytes = GarhwaliVoiceSynthesizer.generate_pcm_wav(duration_seconds=0.2, freq=440.0)
        self.assertTrue(wav_bytes.startswith(b"RIFF"))
        self.assertIn(b"WAVE", wav_bytes)

    def test_folklore_and_holi_songs(self):
        holi_songs = FolkloreTreasury.list_holi_songs()
        self.assertEqual(len(holi_songs), 20)
        
        song1 = FolkloreTreasury.get_holi_song(1)
        self.assertIsNotNone(song1)
        self.assertEqual(song1.title, "गोरी प्यारी लागे है तेरो झनकारो")
        self.assertEqual(song1.raag, "Kafi")
        
        searched = FolkloreTreasury.search_holi_songs("अलकनंदा")
        self.assertTrue(len(searched) > 0)
        
        stats = FolkloreTreasury.stats()
        self.assertEqual(stats["total_holi_songs"], 20)
        self.assertEqual(stats["total_folk_songs"], 45)

        # New genre convenience methods
        jagar = FolkloreTreasury.get_jagar_songs()
        self.assertGreaterEqual(len(jagar), 4)

        mangal = FolkloreTreasury.get_mangal_geet()
        self.assertGreaterEqual(len(mangal), 4)

        pawada = FolkloreTreasury.get_pawada_songs()
        self.assertGreaterEqual(len(pawada), 3)

        khudei = FolkloreTreasury.get_khudei_songs()
        self.assertGreaterEqual(len(khudei), 2)

        dance = FolkloreTreasury.get_dance_songs()
        self.assertGreaterEqual(len(dance), 4)

    def test_lexicon_expansion_statistics(self):
        lex = garhwali.GarhwaliDictionary()
        self.assertGreaterEqual(len(lex.words), 3000)
        
        cats = set(w.get("category", "") for w in lex.words)
        self.assertGreaterEqual(len(cats), 80)
        
        phrases_list = lex.all_phrases()
        self.assertGreaterEqual(len(phrases_list), 150)
        
        proverbs_list = lex.all_proverbs()
        self.assertGreaterEqual(len(proverbs_list), 90)

    def test_grammar_rules_registry(self):
        from garhwali.grammar import RuleRegistry, GARHWALI_GRAMMAR_RULES, RuleCategory
        self.assertGreaterEqual(len(GARHWALI_GRAMMAR_RULES), 40)
        
        r1 = RuleRegistry.get_rule("GARH-SYN-001")
        self.assertIsNotNone(r1)
        self.assertEqual(r1.name, "Canonical Subject-Object-Verb (SOV) Word Order")
        self.assertGreater(len(r1.examples), 0)
        
        syntax_rules = RuleRegistry.list_by_category("syntax")
        self.assertGreaterEqual(len(syntax_rules), 7)

        # Check new rules
        r_abl = RuleRegistry.get_rule("GARH-CASE-004")
        self.assertIsNotNone(r_abl)
        self.assertIn("Ablative", r_abl.name)

        r_hon = RuleRegistry.get_rule("GARH-HON-001")
        self.assertIsNotNone(r_hon)
        self.assertIn("Three-Tiered", r_hon.name)

        r_phon = RuleRegistry.get_rule("GARH-PHON-004")
        self.assertIsNotNone(r_phon)
        self.assertIn("Retroflex", r_phon.name)
        
        found = RuleRegistry.search_rules("ergative")
        self.assertGreater(len(found), 0)
        
        stats = RuleRegistry.stats()
        self.assertEqual(stats["total_rules"], 81)
        self.assertEqual(stats["categories_count"], 8)
        self.assertGreaterEqual(stats["total_annotated_examples"], 175)

    def test_advanced_sentence_builders(self):
        from garhwali.grammar import (
            build_compound_sentence,
            build_conditional_sentence,
            build_causal_sentence,
            build_purposive_sentence,
            build_concessive_sentence,
            build_passive_sentence,
            build_inability_sentence,
            build_imperative_sentence,
            validate_agreement,
            analyze_sentence,
        )
        # Compound
        comp = build_compound_sentence("राम ऐगे", "मोहन चलिगे")
        self.assertIn("अर", comp)
        self.assertTrue(comp.endswith("।"))
        
        # Conditional
        cond = build_conditional_sentence("बरखा होलि", "फसल भली होलि")
        self.assertTrue(cond.startswith("अगर"))
        self.assertIn("त", cond)
        
        # Causal
        caus = build_causal_sentence("मि स्कूल नि गे", "मि बिमार थौ")
        self.assertIn("किलेकि", caus)
        
        # Purposive
        purp = build_purposive_sentence("वो सहर गयो", "पढ़ण")
        self.assertIn("खातिर", purp)
        
        # Concessive
        conc = build_concessive_sentence("ठंड च", "हम जाउला")
        self.assertIn("चाहे", conc)
        self.assertIn("तैं भी", conc)
        
        # Passive
        pas = build_passive_sentence("किताब", "लिखण", agent="राम")
        self.assertIn("बटी", pas)
        
        # Inability
        inab = build_inability_sentence("मि", "हिंडण")
        self.assertIn("नि जांद", inab)
        
        # Imperative & Prohibitive
        imp = build_imperative_sentence("खाणु", honorific=True)
        self.assertEqual(imp, "खावा!")
        proh = build_imperative_sentence("खाणु", honorific=True, prohibitive=True)
        self.assertIn("झनि", proh)
        
        # Agreement validation
        agr_good = validate_agreement("कालो", "घ्वड़ो", gender="m", number="sg")
        self.assertTrue(agr_good["valid"])
        agr_bad = validate_agreement("काली", "घ्वड़ो", gender="m", number="sg")
        self.assertFalse(agr_bad["valid"])
        self.assertIn("कालो घ्वड़ो", agr_bad["recommended_phrase"])
        
        # Sentence analyzer
        analysis = analyze_sentence("राम न मोहन ते किताब दी?")
        self.assertTrue(analysis["is_question"])
        self.assertTrue(analysis["has_ergative_marking"])
        self.assertTrue(analysis["has_postposition"])
        self.assertEqual(analysis["estimated_structure"], "SOV")

    def test_pronominal_system_and_dialects(self):
        from garhwali.grammar import (
            decline_pronoun,
            get_demonstrative,
            get_indefinite,
            get_relative_pair,
            list_all_pronouns,
        )
        self.assertGreater(len(list_all_pronouns()), 8)
        
        # 1sg direct & ergative
        p_dir = decline_pronoun("1sg", case="direct")
        self.assertIn("मि", p_dir)
        p_erg = decline_pronoun("1sg", case="ergative")
        self.assertIn("न", p_erg)
        
        # Demonstrative
        prox = get_demonstrative(proximity="proximate", case="direct")
        self.assertIn("यो", prox)
        rem = get_demonstrative(proximity="remote", case="direct")
        self.assertIn("वो", rem)
        
        # Indefinite & relative
        indef = get_indefinite("animate")
        self.assertTrue("क्वी" in indef or "कोइ" in indef)
        rel_pair = get_relative_pair("entity")
        self.assertEqual(rel_pair, ("जो", "सो"))

    def test_verbal_aspects_and_full_paradigm(self):
        from garhwali.grammar import (
            subjunctive,
            habitual_past,
            progressive,
            inceptive,
            completive,
            conjugate_full_paradigm,
        )
        # Subjunctive
        sub_1sg = subjunctive("जाण", person=1, number="sg")
        self.assertEqual(sub_1sg, "जां")
        sub_3sg = subjunctive("जाण", person=3, number="sg")
        self.assertEqual(sub_3sg, "जाउ")
        
        # Habitual past
        hab = habitual_past("खाणु", gender="m", number="sg")
        self.assertIn("खांदो थौ", hab)
        
        # Progressive & Inceptive & Completive
        prog = progressive("खाणु", gender="m")
        self.assertIn("खांदौ", prog)
        inc = inceptive("खाणु", gender="m")
        self.assertIn("लगिगे", inc)
        comp = completive("खाणु")
        self.assertIn("हाळ", comp)
        
        # Full paradigm
        matrix = conjugate_full_paradigm("खाणु", gender="m")
        self.assertIn("present", matrix)
        self.assertIn("past", matrix)
        self.assertIn("future", matrix)
        self.assertIn("1sg", matrix["present"])
        self.assertIn("3pl", matrix["future"])

    def test_web_handler_routes(self):
        from garhwali.web.app import GarhwaliApiHandler
        self.assertTrue(hasattr(GarhwaliApiHandler, "do_GET"))
        self.assertTrue(hasattr(GarhwaliApiHandler, "do_POST"))


if __name__ == "__main__":
    unittest.main()

