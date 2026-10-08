# -*- coding: utf-8 -*-
"""
Unit tests for the Garhwali Computational Corpus & NLP Framework:
- 20-Pillar Computational Corpus Taxonomy (CorpusTaxonomy, CorpusPillar)
- Annotated Sentence Corpus (SentenceCorpus, AnnotatedSentence)
- Idioms & Proverbs Corpus (IdiomCorpus, GarhwaliIdiom)
- Strict Corpus Eligibility Partitioning in Bibliography
"""

import unittest
from garhwali.corpus import (
    CorpusTaxonomy,
    CorpusPillar,
    get_corpus_taxonomy,
    list_corpus_pillars,
    get_pillar,
    SentenceCorpus,
    AnnotatedSentence,
    get_sentence_corpus,
    search_sentences,
    get_annotated_sentence,
    IdiomCorpus,
    GarhwaliIdiom,
    get_idiom_corpus,
    search_idioms,
    random_idiom,
    list_proverbs,
)
from garhwali.culture.bibliography import (
    BibliographyTreasury,
    get_primary_corpus_books,
    get_reference_books,
)


class TestGarhwaliCorpusTaxonomy(unittest.TestCase):
    """Test the 20-Pillar Computational Taxonomy."""

    def test_twenty_pillars_loaded(self):
        pillars = CorpusTaxonomy.list_pillars()
        self.assertEqual(len(pillars), 20, "Must contain exactly 20 computational pillars")

    def test_pillar_numbering(self):
        pillars = CorpusTaxonomy.list_pillars()
        for idx, p in enumerate(pillars, 1):
            self.assertEqual(p.pillar_number, idx)
            self.assertTrue(len(p.id) > 0)
            self.assertTrue(len(p.name_en) > 0)
            self.assertTrue(len(p.name_garhwali) > 0)
            self.assertTrue(len(p.subcategories) > 0)
            self.assertTrue(len(p.canonical_sources) > 0)
            self.assertTrue(len(p.computational_applications) > 0)

    def test_get_pillar_by_number_and_id(self):
        # By number
        p1 = CorpusTaxonomy.get_pillar(1)
        self.assertIsNotNone(p1)
        self.assertEqual(p1.id, "novels")

        # By ID string
        p_idioms = CorpusTaxonomy.get_pillar("proverbs_idioms")
        self.assertIsNotNone(p_idioms)
        self.assertEqual(p_idioms.pillar_number, 7)

        # By string number
        p7 = CorpusTaxonomy.get_pillar("7")
        self.assertIsNotNone(p7)
        self.assertEqual(p7.id, "proverbs_idioms")

    def test_search_taxonomy(self):
        res = CorpusTaxonomy.search("novel")
        self.assertTrue(len(res) >= 1)
        self.assertTrue(any(p.id == "novels" for p in res))

        res_jagar = CorpusTaxonomy.search("जागर")
        self.assertTrue(len(res_jagar) >= 1)


class TestGarhwaliSentenceCorpus(unittest.TestCase):
    """Test the Annotated Sentence Corpus."""

    def test_sentences_loading(self):
        sentences = SentenceCorpus.all()
        self.assertGreaterEqual(len(sentences), 20, "Should have at least 20 annotated sentences")

    def test_sentence_schema_completeness(self):
        sentences = SentenceCorpus.all()
        for s in sentences:
            self.assertTrue(s.id.startswith("sent_"))
            self.assertTrue(len(s.text) > 0)
            self.assertEqual(s.language, "garhwali")
            self.assertTrue(len(s.source) > 0)
            self.assertTrue(len(s.author) > 0)
            self.assertTrue(len(s.genre) > 0)
            self.assertGreater(s.year, 1800)
            self.assertTrue(len(s.translation_hi) > 0)
            self.assertTrue(len(s.translation_en) > 0)
            self.assertTrue(len(s.tokens) > 0)
            self.assertEqual(len(s.tokens), len(s.pos), f"Tokens and POS tags must match in {s.id}")
            self.assertEqual(len(s.tokens), len(s.morphology), f"Tokens and Morphology must match in {s.id}")

    def test_get_sentence_by_id(self):
        s1 = SentenceCorpus.get("sent_001")
        self.assertIsNotNone(s1)
        self.assertIn("माधो भंडारी", s1.text)
        self.assertEqual(s1.genre, "folk_epic")

    def test_filter_by_author_and_genre(self):
        bartwal_sents = SentenceCorpus.filter(author="चन्द्रकुंवर बर्त्वाल")
        self.assertGreaterEqual(len(bartwal_sents), 2)

        epic_sents = SentenceCorpus.filter(genre="folk_epic")
        self.assertGreaterEqual(len(epic_sents), 2)

    def test_pos_search_and_distribution(self):
        noun_sents = SentenceCorpus.find_by_pos("NOUN")
        self.assertGreater(len(noun_sents), 0)

        verb_sents = SentenceCorpus.find_by_pos("VERB")
        self.assertGreater(len(verb_sents), 0)

        pos_dist = SentenceCorpus.pos_distribution()
        self.assertIn("NOUN", pos_dist)
        self.assertIn("VERB", pos_dist)

    def test_train_test_split(self):
        splits = SentenceCorpus.train_test_split(train_ratio=0.8, val_ratio=0.1, test_ratio=0.1)
        self.assertIn("train", splits)
        self.assertIn("validation", splits)
        self.assertIn("test", splits)
        total = len(splits["train"]) + len(splits["validation"]) + len(splits["test"])
        self.assertEqual(total, len(SentenceCorpus.all()))


class TestGarhwaliIdiomCorpus(unittest.TestCase):
    """Test the Idiom & Proverb Corpus."""

    def test_idioms_loading(self):
        items = IdiomCorpus.all()
        self.assertGreaterEqual(len(items), 20, "Should have at least 20 verified idioms/proverbs")

    def test_idiom_schema_completeness(self):
        items = IdiomCorpus.all()
        for i in items:
            self.assertTrue(i.id.startswith("idh_"))
            self.assertTrue(len(i.idiom) > 0)
            self.assertTrue(len(i.transliteration) > 0)
            self.assertTrue(len(i.literal_meaning) > 0)
            self.assertTrue(len(i.figurative_meaning) > 0)
            self.assertTrue(len(i.hindi_equivalent) > 0)
            self.assertTrue(len(i.english_gloss) > 0)
            self.assertTrue(len(i.example_sentence) > 0)
            self.assertTrue(len(i.example_translation_hi) > 0)
            self.assertTrue(len(i.example_translation_en) > 0)
            self.assertTrue(len(i.grammatical_category) > 0)
            self.assertTrue(len(i.theme) > 0)
            self.assertTrue(len(i.source) > 0)

    def test_search_idioms(self):
        res = IdiomCorpus.search("पानी")
        self.assertGreater(len(res), 0)

        res_en = IdiomCorpus.search("mountain")
        self.assertGreater(len(res_en), 0)

    def test_filter_by_category(self):
        proverbs = IdiomCorpus.filter(category="पखाणा")
        self.assertGreater(len(proverbs), 0)

        idioms = IdiomCorpus.filter(category="मुहावरा")
        self.assertGreater(len(idioms), 0)

    def test_random_idiom(self):
        item = IdiomCorpus.random()
        self.assertIsNotNone(item)
        self.assertIsInstance(item, GarhwaliIdiom)


class TestBibliographyPartitioning(unittest.TestCase):
    """Test clean partitioning between Primary Garhwali texts and Secondary works."""

    def test_bibliography_separation(self):
        primary = get_primary_corpus_books()
        reference = get_reference_books()

        self.assertGreater(len(primary), 0, "Must have verified primary texts")
        self.assertGreater(len(reference), 0, "Must have verified reference works")

        # Ensure no overlap
        primary_ids = {b.id for b in primary}
        ref_ids = {b.id for b in reference}
        self.assertEqual(len(primary_ids.intersection(ref_ids)), 0, "Primary and reference IDs must not intersect")

        # Verify eligibility tags
        for b in primary:
            self.assertEqual(b.corpus_eligibility, "primary_native_corpus")
        for b in reference:
            self.assertEqual(b.corpus_eligibility, "reference_lexical_index_only")

    def test_specific_canonical_authors_present(self):
        # Abodh Bandhu Bahuguna
        bahuguna = BibliographyTreasury.list_books(author="अबोध")
        self.assertGreater(len(bahuguna), 0)

        # Govind Chatak
        chatak = BibliographyTreasury.list_books(author="चातक")
        self.assertGreater(len(chatak), 0)

        # Umesh Chamola
        chamola = BibliographyTreasury.list_books(author="चमोला")
        self.assertGreater(len(chamola), 0)

        # Pushkar Singh Kandari
        kandari = BibliographyTreasury.list_books(author="कण्डारी")
        self.assertGreater(len(kandari), 0)


if __name__ == "__main__":
    unittest.main()
