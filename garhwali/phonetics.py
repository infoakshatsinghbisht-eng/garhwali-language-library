# -*- coding: utf-8 -*-
"""Garhwali Phonetics & Transliteration Engine."""

import re
from typing import Dict, List, Any, Optional, Tuple, Union, Set
from .constants import DEVANAGARI_TO_LATIN_MAP, LATIN_TO_DEVANAGARI_MAP, GARHWALI_MATRAS, GARHWALI_CONSONANTS


def devanagari_to_latin(text: str) -> str:
    """Converts Garhwali Devanagari text into natural Romanized Latin phonetics."""
    if not text:
        return ""
    result = []
    i = 0
    n = len(text)
    while i < n:
        char = text[i]
        if char in GARHWALI_CONSONANTS:
            if i + 1 < n and text[i + 1] == "्":
                base = DEVANAGARI_TO_LATIN_MAP.get(char, char)
                if base.endswith("a"): base = base[:-1]
                result.append(base)
                i += 2
                continue
            elif i + 1 < n and text[i + 1] in GARHWALI_MATRAS:
                matra = text[i + 1]
                base = DEVANAGARI_TO_LATIN_MAP.get(char, char)
                if base.endswith("a"): base = base[:-1]
                vowel = DEVANAGARI_TO_LATIN_MAP.get(matra, "")
                result.append(base + vowel)
                i += 2
                continue
            else:
                result.append(DEVANAGARI_TO_LATIN_MAP.get(char, char))
                i += 1
                continue
        elif char in DEVANAGARI_TO_LATIN_MAP:
            result.append(DEVANAGARI_TO_LATIN_MAP[char])
            i += 1
        else:
            result.append(char)
            i += 1
    res_str = "".join(result)
    res_str = re.sub(r'(?:^|[.!?]\s+)([a-z])', lambda m: m.group(0).upper(), res_str)
    return res_str


def latin_to_devanagari(text: str) -> str:
    """Phonetically converts Romanized Hinglish/Garhwali text into Devanagari script."""
    if not text:
        return ""
    tokens = re.split(r'(\s+|[.,!?;:।])', text)
    converted_tokens = []
    direct_map = {
        "ija": "ईजा", "babu": "बाबु", "dajyu": "दाज्यू", "didi": "दीदी",
        "bubu": "बूबू", "aama": "आमा", "nantin": "नान्तिन", "paani": "पाणि",
        "pani": "पाणि", "bhaat": "भात", "bhat": "भात", "chah": "चाह", "chai": "चाह",
        "chha": "छ", "chhan": "छन", "chhi": "छी", "chhyo": "छ्यो", "chhya": "छ्या",
        "kahan": "कहाँ", "kahaan": "कहाँ", "kilai": "किलै", "kile": "किलै",
        "kas": "कस", "kasa": "कस", "kaisa": "कस", "kaise": "कस",
        "me": "मा", "maa": "मा", "se": "बटि", "bati": "बटि", "dagad": "दगड़",
        "gadi": "गाड़ी", "gaadi": "गाड़ी", "baato": "बाटो", "rasta": "बाटो",
        "ghar": "घर", "gaon": "गाँव", "gaao": "गाँव", "naam": "नाव",
        "ail": "ऐल", "bhyal": "ब्याल", "bhol": "भोल", "bhaal": "भाल",
        "pelag": "पैलाग", "dhanyawad": "धन्यवाद", "dhanyavad": "धन्यवाद"
    }
    for tok in tokens:
        if not tok or re.match(r'^\s+$|[.,!?;:।]', tok):
            converted_tokens.append(tok)
            continue
        w = tok.lower()
        if w in direct_map:
            converted_tokens.append(direct_map[w])
            continue
        res = []
        j = 0
        lw = len(w)
        while j < lw:
            if j + 4 <= lw and w[j:j+4] in LATIN_TO_DEVANAGARI_MAP:
                res.append(LATIN_TO_DEVANAGARI_MAP[w[j:j+4]])
                j += 4
            elif j + 3 <= lw and w[j:j+3] in LATIN_TO_DEVANAGARI_MAP:
                res.append(LATIN_TO_DEVANAGARI_MAP[w[j:j+3]])
                j += 3
            elif j + 2 <= lw and w[j:j+2] in LATIN_TO_DEVANAGARI_MAP:
                res.append(LATIN_TO_DEVANAGARI_MAP[w[j:j+2]])
                j += 2
            elif w[j] in LATIN_TO_DEVANAGARI_MAP:
                res.append(LATIN_TO_DEVANAGARI_MAP[w[j]])
                j += 1
            else:
                res.append(w[j])
                j += 1
        converted_tokens.append("".join(res))
    return "".join(converted_tokens)


def syllables(word: str) -> List[str]:
    """Splits a Garhwali Devanagari or Latin word into phonetic syllables."""
    clean = word.strip(",.?!;:। ")
    if not clean:
        return []
    if re.search(r'[ऀ-ॿ]', clean):
        pattern = r'[ऀ-ॿ](?:्[ऀ-ॿ])*(?:[ािीुूृेैोौँंः])?'
        tokens = re.findall(pattern, clean)
        return tokens if tokens else [clean]
    vowels = "aeiouy"
    syll_list = []
    current = ""
    for char in clean:
        current += char
        if char.lower() in vowels:
            syll_list.append(current)
            current = ""
    if current:
        if syll_list:
            syll_list[-1] += current
        else:
            syll_list.append(current)
    return syll_list
