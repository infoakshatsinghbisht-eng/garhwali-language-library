# -*- coding: utf-8 -*-
"""Baseline Audit Script for Garhwali Language Library."""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.dirname(__file__))
GARHWALI_DIR = os.path.join(ROOT, 'garhwali')
DATA_DIR = os.path.join(GARHWALI_DIR, 'lexicon', 'data')
CULTURE_DATA = os.path.join(GARHWALI_DIR, 'culture', 'data')

def audit():
    words = json.load(open(os.path.join(DATA_DIR, 'words.json'), encoding='utf-8'))
    phrases = json.load(open(os.path.join(DATA_DIR, 'phrases.json'), encoding='utf-8'))
    proverbs = json.load(open(os.path.join(DATA_DIR, 'proverbs.json'), encoding='utf-8'))
    riddles = json.load(open(os.path.join(DATA_DIR, 'riddles.json'), encoding='utf-8'))
    
    bib_file = os.path.join(CULTURE_DATA, 'bibliography.json')
    bib = json.load(open(bib_file, encoding='utf-8')) if os.path.exists(bib_file) else []

    sys.path.insert(0, ROOT)
    import garhwali
    from garhwali.culture.literature import EPICS_DATA, POEMS_DATA, AUTHORS_DATA

    word_categories = set(w.get('category', 'uncategorized') for w in words)

    report = {
        "version": garhwali.__version__,
        "word_count": len(words),
        "phrase_count": len(phrases),
        "proverb_count": len(proverbs),
        "riddle_count": len(riddles),
        "total_word_forms": garhwali.total_word_forms(),
        "categories_count": len(word_categories),
        "categories": sorted(list(word_categories)),
        "books_in_bibliography": len(bib),
        "epics_count": len(EPICS_DATA),
        "poems_count": len(POEMS_DATA),
        "authors_count": len(AUTHORS_DATA),
        "songs_count": 0,
        "places_count": 0,
        "deities_count": 0,
        "surnames_count": 0,
        "flora_count": 0,
        "rituals_count": 0
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    with open(os.path.join(ROOT, 'data_sources', 'baseline_audit.json'), 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    audit()
