# -*- coding: utf-8 -*-
"""Garhwali Syntax and Word Order Analyzer."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

def validate_sov_order(sentence: str) -> Dict[str, Any]:
    clean = sentence.strip()
    words = clean.split()
    if not words:
        return {"valid": True, "structure": "empty"}
    last_word = words[-1].strip(",.?!;:।")
    verb_endings = ("छ", "छन", "छी", "छ्या", "छूँ", "छा", "लो", "ली", "ला", "ग्यो", "ग्यी", "ग्या")
    is_verb_final = any(last_word.endswith(end) for end in verb_endings) or last_word in verb_endings
    return {
        "valid": is_verb_final,
        "token_count": len(words),
        "structure": "SOV" if is_verb_final else "Non-standard",
        "final_token": last_word
    }
