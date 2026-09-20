# -*- coding: utf-8 -*-
"""Comprehensive Rule-Based Garhwali Translation Engine."""

import re
from typing import Dict, List, Any, Optional, Tuple, Union, Set

CONVERSATIONAL_HINGLISH_GARHWALI_MAP = [
    # Questions & Troubleshooting
    (r"\b(?:are|arey|oye)?\s*(?:yah|yeh|ye)\s*(?:chal\s*)?(?:kyon|kyu|kyun)\s*nah?in?\s*(?:chal\s*)?raha\s*hai\??\b", "अरे यो किलै नि चलनो छ?"),
    (r"\b(?:are|arey)?\s*(?:ye|yeh|yah)\s*kya\s*ho\s*raha\s*hai\??\b", "अरे यो क्या हुणो छ?"),
    (r"\b(?:ye|yeh|yah)\s*kaam\s*nah?in?\s*kar\s*raha\s*(?:hai)?\??\b", "यो काम नि करनो छ।"),
    (r"\b(?:kya|kyaa)\s*bol\s*rahe\s*ho\??\b|\bkya\s*bola\??\b", "तुम क्या कूंछा?"),
    
    # Greetings & Identity
    (r"\b(?:kya|kaise)\s*haal\s*(?:hai|chha)\s*(?:bhai|dajyu)?\b", "दाज्यू, क्या हालचाल छन?"),
    (r"\bkaise\s*ho\s*(?:bhai|dajyu|bro|yaar)?\??\b", "त्वे कनु छै भुला?"),
    (r"\baap\s*kaise\s*hain\??\b", "पैलाग, तुमु कना छा?"),
    (r"\bmain\s*(?:theek|achha|badiya)\s*hoon\b", "मी बिल्कुल ठीक छौं।"),
    (r"\baaj\s*mausam\s*kaisa\s*hai\??\b", "आज मौसम कनु छ?"),
    (r"\b(?:aapka|tera|tumhara)\s*naam\s*kya\s*hai\??\b", "तुमरो नौ क्या छ?"),
    (r"\bmera\s*naam\s+([a-zA-Z]+)\s+hai\b", r"म्यारु नौ \1 छ।"),
    (r"\btum\s*kaun\s*ho\??\b|\baap\s*kaun\s*hain\??\b", "तुम को छा?"),
    (r"\btum\s*kahan\s*se\s*ho\??\b|\baap\s*kahan\s*se\s*hain\??\b", "तुमु कख बटी छा?"),
    (r"\btum\s*kahan\s*rehte\s*ho\??\b|\baap\s*kahan\s*rehte\s*ho\??\b", "तुमु कख रौँछा?"),
    (r"\b(?:aapka|tera|tumhara)\s*ghar\s*kahan\s*hai\??\b", "तुमरो घौर कख छ?"),
    
    # Travel & Logistics
    (r"\bkitna\s*time\s*lagega\??\b|\bkitna\s*samay\s*lagega\??\b", "कतुक देर लागली?"),
    (r"\bkitni\s*door\s*hai\??\b", "कतगा दूर छ?"),
    (r"\b(?:ye|yeh|yah)\s*rasta\s*kahan\s*jata\s*hai\??\b", "यौ बाट कख जांदु?"),
    (r"\baspataal\s*kahan\s*hai\??\b|\bhospital\s*kahan\s*hai\??\b", "अस्पताल कख छ?"),
    (r"\bhotel\s*kahan\s*(?:milega|hai)\??\b|\bkamra\s*kahan\s*(?:milega|hai)\??\b", "होटल या कमरा कख मिललो?"),
    (r"\bbus\s*stand\s*kahan\s*hai\??\b", "बस स्टेशन कख छ?"),
    (r"\b(?:gadi|gaadi|bus)\s*kab\s*aayegi\??\b", "गाड़ी कब औली?"),
    (r"\b(?:gadi|gaadi|bus)\s*kab\s*chalegi\??\b", "गाड़ी कब चलली?"),
    (r"\byahan\s*roko\b|\bgaadi\s*roko\b", "यहाँ रुका दाज्यू!"),
    
    # Food & Hospitality
    (r"\bkuch\s*khane\s*ko\s*milega\??\b|\bkhana\s*kahan\s*milega\??\b", "के खाण मिललो क्या?"),
    (r"\bpani\s*milega\s*kya\??\b|\bpaani\s*milega\s*kya\??\b", "पाणि मिललो क्या?"),
    (r"\bpani\s*(?:lao|do|chahiye|pila do)\b", "मूकै पाणि चैं।"),
    (r"\bcha[ih]\s*(?:lao|do|chahiye|pila do)\b", "मूकै च्या चैं।"),
    (r"\bkhana\s*kha\s*liya\??\b", "भात खा ली क्या?"),
    (r"\b(?:mujhe|mujhko)\s*bhookh\s*lagi\s*hai\b", "मूकै भौत भूख लागि गै।"),
    (r"\b(?:mujhe|mujhko)\s*pyas\s*lagi\s*hai\b", "मूकै प्यास लागि गै।"),
    (r"\b(?:mujhe\s*)?thand\s*lag\s*rahi\s*hai\b", "मूकै जाड़ लागणो छ।"),
    
    # Family & Kinship
    (r"\bmummy\s*kahan\s*hai\??\b|\bmaa\s*kahan\s*hai\??\b", "ब्वै कख छिन?"),
    (r"\bpapa\s*kahan\s*hai\??\b|\bpitaji\s*kahan\s*hain\??\b", "बुबा कख छिन?"),
    (r"\bpapa\s*ghar\s*par\s*hain\b", "बुबा घौर मा छन।"),
    (r"\bdada\s*ji\s*so\s*rahe\s*hain\b", "बूबू सुत्यूँ छन।"),
    (r"\bbache\s*khel\s*rahe\s*hain\b", "नान्तिन खेलणा छन।"),
    
    # Emergencies & Politeness
    (r"\bpolice\s*ko\s*bulao\b|\bpolice\s*bulao\b", "पुलिस कणी बुलावा!"),
    (r"\bambulance\s*bulao\b", "एम्बुलेंस बुलावा!"),
    (r"\bmadad\s*karo\b|\bmadad\s*chahiye\b", "मेरी मदद करा दाज्यू!"),
    (r"\btheek\s*hai\b|\bachha\s*hai\b", "ठीक छ, भल छ।"),
    (r"\byahan\s*aao\b", "यहाँ आवा!"),
    (r"\bwahan\s*mat\s*jao\b", "उहाँ झन् जाया!"),
    (r"\bbaith\s*jao\b", "बसा दाज्यू!"),
    (r"\b(?:bahut\s+)?dhanyav?ad\b|\bshukriya\b", "भौत-भौत धन्यवाद!"),
    (r"\bshubh\s*ratri\b", "शुभ राति!")
]

CONVERSATIONAL_EN_GARHWALI_MAP = [
    (r"\bwhy\s+(?:is\s+)?(?:does\s+)?(?:it\s+|this\s+|that\s+)?(?:not\s+)?(?:working|work)\??\b", "यो किलै नि चलनो छ?"),
    (r"\bwhy\s+(?:it\s+|this\s+|that\s+)?(?:is\s+)?not\s+working\??\b", "यो किलै नि चलनो छ?"),
    (r"\b(?:it\s+|this\s+|that\s+)?(?:is\s+|does\s+)?not\s+working\b", "यो काम नि करनो छ।"),
    (r"\bwhy\s+are\s+you\s+not\s+coming\??\b", "तुम किलै नि आँछा?"),
    (r"\bwhat\s+are\s+you\s+doing\??\b", "तुमु क्या करणा छा?"),
    (r"\bwhat\s+did\s+you\s+say\??\b", "तुमले क्या कयो?"),
    (r"\bwhat\s+is\s+your\s+name\??\b", "तुमरो नौ क्या छ?"),
    (r"\bmy\s+name\s+is\s+([a-zA-Z]+)\b", r"म्यारु नौ \1 छ।"),
    (r"\bwhat\s+is\s+your\s+village\s+name\??\b", "तुमरा गाँव का नाव क्या छ?"),
    (r"\bwhere\s+are\s+you\s+going\??\b", "तुमु कख जाणा छा?"),
    (r"\bwhere\s+do\s+you\s+live\??\b", "तुमु कख रौँछा?"),
    (r"\bwhere\s+are\s+you\s+from\??\b", "तुमु कख बटी छा?"),
    (r"\bhow\s+are\s+you\??\b", "तुमु कना छा?"),
    (r"\bi\s+am\s+(?:fine|good|okay)\b", "मी बिल्कुल ठीक छौं।"),
    (r"\bhow\s+are\s+you[,\s]+(?:bro|brother|dajyu)\??\b", "दाज्यू, क्या हालचाल छन?"),
    
    # Kinship & Home
    (r"\bwhere\s+is\s+mom\??\b|\bwhere\s+is\s+mother\??\b|\bwhere\s+is\s+mum\??\b|\bwhere\s+is\s+mommy\??\b", "ब्वै कख छिन?"),
    (r"\bdad\s+is\s+at\s+home\b|\bpapa\s+is\s+at\s+home\b|\bfather\s+is\s+at\s+home\b", "बुबा घौर मा छन।"),
    (r"\bgrandpa\s+is\s+sleeping\b|\bgrandfather\s+is\s+sleeping\b", "बूबू सुत्यूँ छन।"),
    (r"\bgrandma\s+is\s+telling\s+a\s+story\b|\bgrandmother\s+is\s+telling\s+a\s+story\b", "बौजी बात कूंणी छ।"),
    (r"\bkids\s+are\s+playing\b|\bchildren\s+are\s+playing\b", "नान्तिन खेलणा छन।"),
    
    # Food & Hospitality
    (r"\bi\s+want\s+water\b|\bgive\s+me\s+water\b", "मूकै पाणि चैं।"),
    (r"\bi\s+want\s+tea\b|\bgive\s+me\s+tea\b", "मूकै च्या चैं।"),
    (r"\bhave\s+you\s+eaten(?:\s+food)?\??\b", "भात खा ली क्या?"),
    (r"\bthe\s+food\s+is\s+very\s+(?:tasty|delicious)\b", "भात भौत मीठु स्वादिलो छ।"),
    (r"\bwhere\s+is\s+the\s+hospital\??\b", "अस्पताल कख छ?"),
    (r"\bwhere\s+is\s+the\s+hotel\??\b|\bwhere\s+can\s+i\s+stay\??\b", "होटल या कमरा कख मिललो?"),
    (r"\bwhere\s+is\s+the\s+bus\s+stand\??\b", "बस स्टेशन कख छ?"),
    (r"\bwhere\s+can\s+i\s+get\s+a\s+taxi\??\b", "टैक्सी कख मिलली?"),
    (r"\bhow\s+much\s+does\s+this\s+cost\??\b|\bhow\s+much\s+is\s+this\??\b", "यो कतुक रुप्याक छ?"),
    (r"\bwhat\s+is\s+the\s+time\??\b", "क्या बज्यो छ?"),
    (r"\b(?:it\s+is\s+|it's\s+)?raining(?:\s+(?:today|now))?\b", "आज पाणि पड़नो छ।"),
    (r"\b(?:it\s+is\s+|it's\s+)?very\s+cold\b", "भौत जाड़ छ।"),
    (r"\bcall\s+(?:the\s+)?police\b", "पुलिस कणी बुलावा!"),
    (r"\bcall\s+(?:an\s+)?ambulance\b", "एम्बुलेंस बुलावा!"),
    (r"\b(?:please\s+)?help\s+me\b", "मेरी मदद करा दाज्यू!"),
    (r"\bstop\s+here\b|\bstop\s+the\s+car\b", "यहाँ रुका दाज्यू!"),
    (r"\blet\s*(?:us|'s)\s+go\b", "आवा जौल्या!"),
    (r"\bthank\s+you(?:\s+very\s+much)?\b", "भौत-भौत धन्यवाद!"),
    (r"\bgood\s+night\b", "शुभ राति!"),
    (r"\btake\s+care\b", "आपणी खैरियत रख्या।")
]

CONVERSATIONAL_HI_GARHWALI_MAP = [
    (r"^नमस्ते$|^प्रणाम$|^नमस्कार$", "पैलाग!"),
    (r"आप\s+कैसे\s+हैं\??|क्या\s+हाल\s+है\??", "तुमु कना छा?"),
    (r"तुम\s+कैसे\s+हो\??", "त्वे कनु छै?"),
    (r"मैं\s+ठीक\s+हूँ", "मी बिल्कुल ठीक छौं।"),
    (r"आपका\s+नाम\s+क्या\s+है\??|तुम्हारा\s+नाम\s+क्या\s+है\??", "तुमरो नौ क्या छ?"),
    (r"पानी\s+लाओ|पानी\s+दीजिये|पानी\s+दो", "पाणि ल्यावा।"),
    (r"खाना\s+खा\s+लिया\??|खाना\s+खाया\??", "भात खा ली क्या?"),
    (r"यह\s+रास्ता\s+कहाँ\s+जाता\s+है\??", "यौ बाट कख जांदु?"),
    (r"अस्पताल\s+कहाँ\s+है\??", "अस्पताल कख छ?"),
    (r"होटल\s+कहाँ\s+मिलेगा\??|कमरा\s+कहाँ\s+मिलेगा\??", "होटल या कमरा कख मिललो?"),
    (r"बैठिए|बैठो|कृप्या\s+बैठिए", "बसा दाज्यू!"),
    (r"माँ\s+कहाँ\s+हैं\??", "ब्वै कख छिन?"),
    (r"पिताजी\s+कहाँ\s+हैं\??", "बुबा कख छिन?"),
    (r"मुझे\s+बहुत\s+भूख\s+लगी\s+है", "मूकै भौत भूख लागि गै।"),
    (r"मुझे\s+बहुत\s+प्यास\s+लगी\s+है", "मूकै भौत प्यास लागि गै।"),
    (r"मुझे\s+ठंड\s+लग\s+रही\s+है", "मूकै जाड़ लागणो छ।"),
    (r"पुलिस\s+को\s+बुलाओ", "पुलिस कणी बुलावा!"),
    (r"एम्बुलेंस\s+बुलाओ", "एम्बुलेंस बुलावा!"),
    (r"मेरी\s+मदद\s+करो|मेरी\s+मदद\s+करें", "मेरी मदद करा दाज्यू!"),
    (r"गाड़ी\s+रोको|यहाँ\s+रोको", "यहाँ रुका दाज्यू!"),
    (r"धन्यवाद|बहुत\s+धन्यवाद", "भौत-भौत धन्यवाद!"),
    (r"शुभ\s+रात्रि", "शुभ राति!")
]

def apply_dialect(text: str, dialect: str = "srinagariya") -> str:
    """Applies authentic Garhwali dialectal phonetic inflections."""
    if not text or dialect == "srinagariya":
        return text
    words = text.split()
    res = []
    for w in words:
        punct = ""
        while w and w[-1] in ".,?!;:।":
            punct = w[-1] + punct
            w = w[:-1]
        if dialect == "rathwali":
            if w == "छन": w = "छिन"
            elif w == "छ": w = "छी"
            elif w in ("तुमरो", "तुमारु", "तुमार"): w = "तमरो"
            elif w == "नाव": w = "नौ"
            elif w == "ब्वै": w = "माई"
        elif dialect == "tehri":
            if w == "छन": w = "छिन"
            elif w == "छ": w = "छी"
            elif w == "ब्वै": w = "ब्वे"
            elif w == "कख": w = "कथी"
        elif dialect == "salani":
            if w == "छ": w = "छौ"
            elif w in ("तुमरो", "तुमारु", "तुमार"): w = "तुमारू"
            elif w == "ब्वै": w = "माजी"
        elif dialect == "badhani":
            if w == "छ": w = "छी"
            elif w == "मा": w = "माझ"
        res.append(w + punct)
    return " ".join(res)
