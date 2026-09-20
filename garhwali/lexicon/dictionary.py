# -*- coding: utf-8 -*-
"""Garhwali Dictionary and Lexical Lookup Engine."""

import json
import random
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union, Set

DATA_DIR = Path(__file__).resolve().parent / "data"

class GarhwaliDictionary:
    def __init__(self):
        self._words = {}
        self._phrases = []
        self._proverbs = []
        self._riddles = []
        self._load_data()

    def _load_data(self):
        w_file = DATA_DIR / "words.json"
        if w_file.exists():
            with open(w_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self._words[item["garhwali"]] = item
        p_file = DATA_DIR / "phrases.json"
        if p_file.exists():
            with open(p_file, "r", encoding="utf-8") as f:
                self._phrases = json.load(f)
        pr_file = DATA_DIR / "proverbs.json"
        if pr_file.exists():
            with open(pr_file, "r", encoding="utf-8") as f:
                self._proverbs = json.load(f)
        r_file = DATA_DIR / "riddles.json"
        if r_file.exists():
            with open(r_file, "r", encoding="utf-8") as f:
                self._riddles = json.load(f)

    def lookup(self, word: str) -> Optional[Dict[str, Any]]:
        return self._words.get(word.strip())

    def search(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower().strip()
        results = []
        for w, item in self._words.items():
            if (q in w.lower() or 
                q in item.get("hindi", "").lower() or 
                q in item.get("english", "").lower()):
                results.append(item)
        return results

    def all_words(self) -> List[Dict[str, Any]]:
        return list(self._words.values())

    def all_phrases(self) -> List[Dict[str, Any]]:
        return self._phrases

    def all_proverbs(self) -> List[Dict[str, Any]]:
        return self._proverbs

    def all_riddles(self) -> List[Dict[str, Any]]:
        return self._riddles

    def random_phrase(self) -> Optional[Dict[str, Any]]:
        return random.choice(self._phrases) if self._phrases else None

    def random_proverb(self) -> Optional[Dict[str, Any]]:
        return random.choice(self._proverbs) if self._proverbs else None

    def random_riddle(self) -> Optional[Dict[str, Any]]:
        return random.choice(self._riddles) if self._riddles else None
