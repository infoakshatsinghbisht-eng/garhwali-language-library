# -*- coding: utf-8 -*-
"""Garhwali Numbers and Numeric Conversion Engine."""

from typing import Union, Optional, Dict, List

GARHWALI_DIGITS_MAP = {
    0: "शून्य", 1: "एक", 2: "दुई", 3: "तीन", 4: "चार", 5: "पाँच",
    6: "छ", 7: "सात", 8: "आठ", 9: "नौ", 10: "दस",
    11: "ग्यारह", 12: "बारह", 13: "तेरह", 14: "चौदह", 15: "पन्द्रह",
    16: "सोलह", 17: "सत्रह", 18: "अट्ठारह", 19: "उन्नीस", 20: "बीस",
    30: "तीस", 40: "चालीस", 50: "पचास", 60: "साठ", 70: "सत्तर", 80: "अस्सी", 90: "नब्बे",
    100: "सौ", 1000: "हजार", 100000: "लाख", 10000000: "करोड़"
}

DEVANAGARI_NUMERALS = {"0": "०", "1": "१", "2": "२", "3": "३", "4": "४", "5": "५", "6": "६", "7": "७", "8": "८", "9": "९"}

def num_to_words(n: int) -> str:
    if n in GARHWALI_DIGITS_MAP:
        return GARHWALI_DIGITS_MAP[n]
    if n < 100:
        tens = (n // 10) * 10
        rem = n % 10
        return f"{GARHWALI_DIGITS_MAP.get(tens, '')} {GARHWALI_DIGITS_MAP.get(rem, '')}".strip()
    if n < 1000:
        h = n // 100
        rem = n % 100
        h_str = f"{GARHWALI_DIGITS_MAP.get(h, '')} सौ"
        return f"{h_str} {num_to_words(rem)}" if rem > 0 else h_str
    if n < 100000:
        th = n // 1000
        rem = n % 1000
        th_str = f"{num_to_words(th)} हजार"
        return f"{th_str} {num_to_words(rem)}" if rem > 0 else th_str
    return str(n)

def to_devanagari_numerals(n: int) -> str:
    return "".join(DEVANAGARI_NUMERALS.get(d, d) for d in str(n))

def from_devanagari_numerals(text: str) -> str:
    """Converts Devanagari numerals (०-९) back to Latin digits."""
    reverse_map = {v: k for k, v in DEVANAGARI_NUMERALS.items()}
    return "".join(reverse_map.get(ch, ch) for ch in str(text))

def ordinal(n: int) -> str:
    w = num_to_words(n)
    if n == 1:
        return "पैलो / पहिलो"
    elif n == 2:
        return "दूसरो / दूसर"
    elif n == 3:
        return "तीसरो / तीसर"
    elif n == 4:
        return "चौथो / चौथ"
    return w + "वाँ" if not w.endswith("वाँ") else w

GARHWALI_FRACTIONS = {
    "चौथाई": 0.25,
    "पाव": 0.25,
    "आधा": 0.5,
    "आधो": 0.5,
    "पौन": 0.75,
    "पौण": 0.75,
    "पौणा": 0.75,
    "सवा": 1.25,
    "डेढ़": 1.5,
    "डैड": 1.5,
    "ढाई": 2.5,
    "अढाई": 2.5,
    "साढ़े": "half_plus",
}

def fraction(name: str) -> Union[float, str, None]:
    """
    Returns the decimal value of Garhwali fraction words.
    Example:
        fraction("आधा") -> 0.5
        fraction("सवा") -> 1.25
        fraction("डेढ़") -> 1.5
    """
    key = name.strip()
    return GARHWALI_FRACTIONS.get(key, None)

def words_to_num(text: str) -> int:
    """
    Parses Garhwali number words back into integer values.
    Example:
        words_to_num("एक सौ बीस") -> 120
        words_to_num("पाँच हजार दुई सौ") -> 5200
        words_to_num("पचास") -> 50
    """
    # Inverse map
    word_to_val = {v: k for k, v in GARHWALI_DIGITS_MAP.items() if isinstance(k, int)}
    # Add common variants
    word_to_val["एक"] = 1
    word_to_val["दुई"] = 2
    word_to_val["द्वी"] = 2
    word_to_val["तीन"] = 3
    word_to_val["चार"] = 4
    word_to_val["पाँच"] = 5
    word_to_val["पांच"] = 5
    word_to_val["छ"] = 6
    word_to_val["सात"] = 7
    word_to_val["आठ"] = 8
    word_to_val["नौ"] = 9
    word_to_val["दस"] = 10
    word_to_val["ग्यारह"] = 11
    word_to_val["बारह"] = 12
    word_to_val["तेरह"] = 13
    word_to_val["चौदह"] = 14
    word_to_val["पन्द्रह"] = 15
    word_to_val["सोलह"] = 16
    word_to_val["सत्रह"] = 17
    word_to_val["अट्ठारह"] = 18
    word_to_val["उन्नीस"] = 19
    word_to_val["बीस"] = 20
    word_to_val["इक्कीस"] = 21
    word_to_val["बाईस"] = 22
    word_to_val["तेईस"] = 23
    word_to_val["चौबीस"] = 24
    word_to_val["पच्चीस"] = 25
    word_to_val["छब्बीस"] = 26
    word_to_val["सत्ताईस"] = 27
    word_to_val["अट्ठाईस"] = 28
    word_to_val["उनतीस"] = 29
    word_to_val["तीस"] = 30
    word_to_val["सौ"] = 100
    word_to_val["हजार"] = 1000
    word_to_val["लाख"] = 100000
    word_to_val["करोड़"] = 10000000

    tokens = text.strip().split()
    total = 0
    current = 0

    for token in tokens:
        val = word_to_val.get(token)
        if val is None:
            continue
        if val == 100:
            current = (current if current != 0 else 1) * 100
        elif val in (1000, 100000, 10000000):
            current = (current if current != 0 else 1) * val
            total += current
            current = 0
        else:
            current += val

    return total + current

