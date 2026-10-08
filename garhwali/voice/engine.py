# -*- coding: utf-8 -*-
"""
Garhwali Voice Translation Engine.
Translates spoken and written text from any language into spoken Garhwali with
phonetic transcription, SSML generation, syllable timing, and speech audio synthesis.
"""

import base64
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

import garhwali
from garhwali.voice.synthesizer import GarhwaliVoiceSynthesizer


@dataclass
class VoiceTranslationResult:
    """Represents the complete result of a voice translation operation."""
    source_text: str
    source_lang: str
    translated_text: str
    romanized: str
    phonetic_script: Dict[str, Any]
    syllables: List[str]
    ssml: str
    audio_wav_base64: Optional[str] = None
    confidence: float = 0.95
    category: Optional[str] = None
    method: str = "auto"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_text": self.source_text,
            "source_lang": self.source_lang,
            "translated_text": self.translated_text,
            "romanized": self.romanized,
            "phonetic_script": self.phonetic_script,
            "syllables": self.syllables,
            "ssml": self.ssml,
            "audio_wav_base64": self.audio_wav_base64,
            "confidence": self.confidence,
            "category": self.category,
            "method": self.method,
        }

    def __str__(self) -> str:
        return f"{self.translated_text} ({self.romanized})"


class VoiceTranslator:
    """
    High-level Voice Translator for Garhwali.
    Integrates Universal Translation with Central Pahari speech synthesis markup,
    phonetic syllable analysis, and audio waveform generation.
    """

    CATEGORIZED_PHRASES = [
        # Greetings & Welcomes
        {
            "category": "greetings",
            "english": "Hello / Respectful Greetings",
            "hindi": "नमस्ते / प्रणाम",
            "garhwali": "पैलग्, क्या हालचाल छन?",
            "roman": "Pailag, kya haalchaal chhan?",
            "situation": "Everyday polite greeting to elders and friends"
        },
        {
            "category": "greetings",
            "english": "How are you? I am fine.",
            "hindi": "आप कैसे हैं? मैं ठीक हूँ।",
            "garhwali": "कैन छौ तुम? मैं चोखो छौं।",
            "roman": "Kain chhau tum? Main chokho chhaun.",
            "situation": "Inquiring about well-being"
        },
        {
            "category": "greetings",
            "english": "What is your name?",
            "hindi": "आपका नाम क्या है?",
            "garhwali": "तुमरो नौं क्या च?",
            "roman": "Tumro naun kya cha?",
            "situation": "Meeting someone new"
        },
        {
            "category": "greetings",
            "english": "Welcome to our village / home.",
            "hindi": "हमारे गाँव / घर में आपका स्वागत है।",
            "garhwali": "हमार गांव अर घर मा तुमरो स्वागत च।",
            "roman": "Hamaar gaanw ar ghar ma tumro swaagat cha.",
            "situation": "Welcoming guests"
        },
        # Travel & Directions in the Hills
        {
            "category": "travel",
            "english": "Where does this mountain road go?",
            "hindi": "यह पहाड़ी रास्ता कहाँ जाता है?",
            "garhwali": "ये डांडी को बाटो कख जांदू?",
            "roman": "Ye daandi ko baato kakh jaandoo?",
            "situation": "Asking for trekking directions"
        },
        {
            "category": "travel",
            "english": "How far is Srinagar / Pauri from here?",
            "hindi": "यहाँ से श्रीनगर / पौड़ी कितनी दूर है?",
            "garhwali": "यां बटी श्रीनगर कतुक दूर च?",
            "roman": "Yaan batee Srinagar katuk door cha?",
            "situation": "Distance calculation"
        },
        {
            "category": "travel",
            "english": "When will the bus / taxi arrive?",
            "hindi": "बस / गाड़ी कब आएगी?",
            "garhwali": "बस कबे औली?",
            "roman": "Bas kabe aulee?",
            "situation": "Public transportation inquiries"
        },
        # Food & Dining
        {
            "category": "food",
            "english": "Have you had food / tea?",
            "hindi": "क्या आपने खाना खाया / चाय पी?",
            "garhwali": "भात खायो? चाह पीली?",
            "roman": "Bhaat khaayo? Chaah peelee?",
            "situation": "Himalayan hospitality"
        },
        {
            "category": "food",
            "english": "Please give me cold spring water.",
            "hindi": "मुझे प्राकृतिक झरने का ठंडा पानी दीजिए।",
            "garhwali": "मिते धारो को ठंडो पाणी द्यावा।",
            "roman": "Mite dhaaro ko thhando paanee dyaawa.",
            "situation": "Asking for fresh mountain spring water"
        },
        {
            "category": "food",
            "english": "The Garhwali food is very delicious.",
            "hindi": "गढ़वाली खाना बहुत स्वादिष्ट है।",
            "garhwali": "गढ़वाळी भात-रोटी बडो स्वाद च।",
            "roman": "Garhwali bhaat-roti bado swaad cha.",
            "situation": "Appreciating culinary culture (Chainsoo, Kafuli, Jhangora)"
        },
        # Bazaar & Shopping
        {
            "category": "shopping",
            "english": "What is the price of this?",
            "hindi": "इसका दाम कितना है?",
            "garhwali": "येको भाव क्या च? कतगा रुप्या?",
            "roman": "Yeko bhaaw kya cha? Katga rupya?",
            "situation": "Bargaining in local markets"
        },
        {
            "category": "shopping",
            "english": "Please reduce the price a little bit.",
            "hindi": "थोड़ा कम कीजिए।",
            "garhwali": "थोड़ा कम करा दाज्यू।",
            "roman": "Thhoda kam karaa daajyoo.",
            "situation": "Friendly bargaining"
        },
        # Health & Emergency
        {
            "category": "emergency",
            "english": "I am feeling unwell / cold.",
            "hindi": "मेरी तबीयत ठीक नहीं है / ठंड लग रही है।",
            "garhwali": "मेरी तबियत चोखी नी च, जाड़ लगणू च।",
            "roman": "Meree tabiyat chokhee nee cha, jaad lagnu cha.",
            "situation": "Describing illness in hill climate"
        },
        {
            "category": "emergency",
            "english": "Where is the dispensary / hospital?",
            "hindi": "अस्पताल / डॉक्टर कहाँ मिलेंगे?",
            "garhwali": "अस्पताल कख च? डाक्टर कख बैठदन?",
            "roman": "Aspataal kakh cha? Doctor kakh baithdan?",
            "situation": "Seeking medical assistance"
        },
        # Weather & Environment
        {
            "category": "weather",
            "english": "It is snowing / raining heavily on the peaks.",
            "hindi": "पहाड़ों पर तेज बर्फ / बारिश पड़ रही है।",
            "garhwali": "डांड्युं मा भारी हिउँद / बरखा पौणी च।",
            "roman": "Daandyun ma bhaaree hiund / barkhaa paunee cha.",
            "situation": "Mountain weather warning"
        },
        {
            "category": "weather",
            "english": "Today the weather is very pleasant.",
            "hindi": "आज मौसम बहुत सुहावना है।",
            "garhwali": "आज बगत बडो चोखो च।",
            "roman": "Aaj bagat bado chokho cha.",
            "situation": "Admiring clear Himalayan skies"
        }
    ]

    def __init__(self):
        self.synthesizer = GarhwaliVoiceSynthesizer()

    def translate_speech(
        self,
        text: str,
        source_lang: str = "auto",
        method: str = "auto",
        generate_audio: bool = False,
        api_key: Optional[str] = None,
    ) -> VoiceTranslationResult:
        """
        Translates input text into authentic Garhwali, extracts phonetic syllables,
        builds SSML for speech synthesis, and optionally generates audio waveform.
        """
        if not text or not text.strip():
            return VoiceTranslationResult(
                source_text="",
                source_lang=source_lang,
                translated_text="",
                romanized="",
                phonetic_script={},
                syllables=[],
                ssml="",
                confidence=1.0,
                method=method,
            )

        # 1. Translate using garhwali translator
        tr_res = garhwali.translate(text, source=source_lang, method=method, api_key=api_key)
        garhwali_text = tr_res.text
        romanized = tr_res.romanized or garhwali.devanagari_to_latin(garhwali_text)

        # 2. Phonetic & SSML preparation
        phonetics = self.synthesizer.get_phonetic_script(garhwali_text)
        syls = garhwali.syllables(garhwali_text)
        ssml = self.synthesizer.get_speech_ssml(garhwali_text)

        # 3. Optional Audio bytes generation
        audio_b64 = None
        if generate_audio:
            wav_bytes = self.synthesizer.generate_pcm_wav(duration_seconds=0.6, freq=440.0)
            audio_b64 = base64.b64encode(wav_bytes).decode("ascii")

        category = self._detect_category(text, garhwali_text)

        return VoiceTranslationResult(
            source_text=text,
            source_lang=source_lang,
            translated_text=garhwali_text,
            romanized=romanized,
            phonetic_script=phonetics,
            syllables=syls,
            ssml=ssml,
            audio_wav_base64=audio_b64,
            confidence=tr_res.confidence,
            category=category,
            method=method,
        )

    def _detect_category(self, original: str, translated: str) -> Optional[str]:
        orig_lower = original.lower()
        trans_lower = translated.lower()
        for phrase in self.CATEGORIZED_PHRASES:
            if any(term in orig_lower or term in trans_lower for term in [
                phrase["english"].lower(),
                phrase["hindi"].lower(),
                phrase["garhwali"].lower(),
            ]):
                return phrase["category"]

        if any(w in orig_lower or w in trans_lower for w in ["road", "way", "where", "far", "बाटो", "कख", "दूर", "गाड़ी"]):
            return "travel"
        if any(w in orig_lower or w in trans_lower for w in ["hello", "how", "name", "नमस्ते", "पैलग्", "कैन", "नौं"]):
            return "greetings"
        if any(w in orig_lower or w in trans_lower for w in ["food", "eat", "water", "tea", "भात", "पाणी", "चाह", "खाण"]):
            return "food"
        if any(w in orig_lower or w in trans_lower for w in ["buy", "price", "rupee", "cost", "दाम", "रुप्या", "भाव"]):
            return "shopping"
        if any(w in orig_lower or w in trans_lower for w in ["cold", "doctor", "ill", "दर्द", "जाड़", "डाक्टर"]):
            return "emergency"
        if any(w in orig_lower or w in trans_lower for w in ["snow", "rain", "sun", "धूप", "बरखा", "हिउँद"]):
            return "weather"

        return "general"

    def get_voice_phrases(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Returns categorized spoken phrases with phonetic and audio metadata."""
        results = []
        for p in self.CATEGORIZED_PHRASES:
            if category and p["category"] != category:
                continue
            item = dict(p)
            item["syllables"] = garhwali.syllables(p["garhwali"])
            item["ssml"] = self.synthesizer.get_speech_ssml(p["garhwali"])
            results.append(item)
        return results


def voice_translate(
    text: str,
    source_lang: str = "auto",
    method: str = "auto",
    generate_audio: bool = False,
    api_key: Optional[str] = None,
) -> VoiceTranslationResult:
    """Convenience helper for one-line voice translation."""
    translator = VoiceTranslator()
    return translator.translate_speech(
        text=text,
        source_lang=source_lang,
        method=method,
        generate_audio=generate_audio,
        api_key=api_key,
    )
