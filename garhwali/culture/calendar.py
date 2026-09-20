# -*- coding: utf-8 -*-
"""Garhwali Calendar, Months, Ritus, and Days of the Week."""

import datetime
from typing import Dict, List, Any, Optional, Tuple, Union, Set

GARHWALI_MONTHS = {
    1: {"name": "चैत", "english": "Chait", "gregorian": "Mid March - Mid April"},
    2: {"name": "बैसाख", "english": "Baisakh", "gregorian": "Mid April - Mid May"},
    3: {"name": "जेठ", "english": "Jeth", "gregorian": "Mid May - Mid June"},
    4: {"name": "असाड़", "english": "Asadh", "gregorian": "Mid June - Mid July"},
    5: {"name": "साउन", "english": "Saun", "gregorian": "Mid July - Mid August"},
    6: {"name": "भादौ", "english": "Bhado", "gregorian": "Mid August - Mid September"},
    7: {"name": "आसोज", "english": "Aasoj", "gregorian": "Mid September - Mid October"},
    8: {"name": "कातिक", "english": "Katik", "gregorian": "Mid October - Mid November"},
    9: {"name": "मंगसिर", "english": "Mangasir", "gregorian": "Mid November - Mid December"},
    10: {"name": "पूस", "english": "Poos", "gregorian": "Mid December - Mid January"},
    11: {"name": "माघ", "english": "Maagh", "gregorian": "Mid January - Mid February"},
    12: {"name": "फागुन", "english": "Phagun", "gregorian": "Mid February - Mid March"}
}

GARHWALI_RITUS = {
    "बसंत": {"hindi": "वसंत", "english": "Spring", "months": ["चैत", "बैसाख"]},
    "रूड़ि": {"hindi": "ग्रीष्म", "english": "Summer", "months": ["जेठ", "असाड़"]},
    "चौमास": {"hindi": "वर्षा", "english": "Monsoon / Rainy", "months": ["साउन", "भादौ"]},
    "सरद": {"hindi": "शरद", "english": "Autumn", "months": ["आसोज", "कातिक"]},
    "स्यूँद": {"hindi": "हेमंत", "english": "Early Winter", "months": ["मंगसिर", "पूस"]},
    "जाड़": {"hindi": "शिशिर", "english": "Late Winter", "months": ["माघ", "फागुन"]}
}

GARHWALI_DAYS = {
    "रविवार": "ऐतवार", "सोमवार": "सोमवार", "मंगलवार": "मंगर",
    "बुधवार": "बुधवार", "गुरुवार": "बिफे", "शुक्रवार": "सुक्कुर", "शनिवार": "सनिच्चर"
}

def get_current_season() -> Dict[str, str]:
    m = datetime.datetime.now().month
    if m in (3, 4): return {"name_garhwali": "बसंत", "name_hindi": "वसंत", "english_season": "Spring"}
    elif m in (5, 6): return {"name_garhwali": "रूड़ि", "name_hindi": "ग्रीष्म", "english_season": "Summer"}
    elif m in (7, 8): return {"name_garhwali": "चौमास", "name_hindi": "वर्षा", "english_season": "Monsoon / Rainy"}
    elif m in (9, 10): return {"name_garhwali": "सरद", "name_hindi": "शरद", "english_season": "Autumn"}
    elif m in (11, 12): return {"name_garhwali": "स्यूँद", "name_hindi": "हेमंत", "english_season": "Early Winter"}
    else: return {"name_garhwali": "जाड़", "name_hindi": "शिशिर", "english_season": "Late Winter"}

def get_current_himalayan_month() -> Dict[str, Any]:
    now = datetime.datetime.now()
    # Himalayan months start approx mid-gregorian month
    m_idx = now.month - 2
    if m_idx < 1:
        m_idx += 12
    return GARHWALI_MONTHS[m_idx]
