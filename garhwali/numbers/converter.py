# -*- coding: utf-8 -*-
"""Garhwali Numbers and Numeric Conversion Engine."""

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

def ordinal(n: int) -> str:
    w = num_to_words(n)
    return w + "वाँ" if not w.endswith("वाँ") else w
