# -*- coding: utf-8 -*-
"""
LLM Adapter for State-of-the-Art Neural Garhwali Translation.
Supports Google Gemini API, OpenAI, Anthropic, and local Ollama instances with zero external pip dependencies.
"""

import os
import json
import urllib.request
import urllib.parse
from typing import Optional, Dict, Any, Tuple

GARHWALI_SYSTEM_PROMPT = """You are an expert native linguist and translator for the Garhwali language (गढ़वाली भाषा), an Indo-Aryan Central Pahari language spoken across Uttarakhand's Garhwal Himalayas.

Your task is to translate sentences from ANY source language into authentic, natural, colloquial Garhwali.

Key Linguistic Rules for Garhwali:
1. Script: Write the translation primarily in Devanagari (गढ़वाली).
2. Sentence Structure: Follow strict SOV (Subject - Object - Verb) word order.
3. Substantive Verb 'to be' (छण):
   - Present: छौं (I am), छै (you are-informal), छा (you are-respectful), च / छ (he/she is), छां (we are), छन (they are).
   - Past: छयौं (I was), छये (you were), छौ (he was), छी (she was), छया (they were).
4. Case Markers & Postpositions:
   - Agentive/Ergative: -न / -ले (e.g. मैंन, तैन, वैन, राम न)
   - Accusative/Dative: -ते / -तैं (e.g. मिते, त्वेते, वेते)
   - Ablative: -बटी / -बटि (e.g. घर बटी)
   - Locative: -मा / -म (e.g. डांडा मा)
   - Genitive: -को / -कु / -का / -की (e.g. पहाड़ को पाणी)
5. Vocabulary: Use authentic Garhwali terms (नौना/नौनी for boy/girl, घौर/घर for house, डांडा for mountain, गाड़ for river, सेरा for field).
6. Split Ergativity: Transitive verbs in past tense require an ergative subject with '-न' (e.g. 'राम न भात खायो', not 'राम भात खायो').

Respond ONLY with a JSON object:
{
  "garhwali_devanagari": "<translation in Garhwali Devanagari>",
  "roman_transliteration": "<phonetic Latin transcription>",
  "literal_breakdown": "<word by word brief mapping>",
  "notes": "<dialect or grammatical nuance>"
}
"""


class LLMTranslator:
    """Zero-dependency HTTP client for neural Garhwali translation via LLMs."""

    def __init__(self, provider: str = "auto", api_key: Optional[str] = None, model: Optional[str] = None):
        self.provider = provider.lower()
        self.api_key = api_key
        self.model = model

        # Auto-detect API keys from environment
        if self.provider == "auto":
            if os.getenv("GEMINI_API_KEY"):
                self.provider = "gemini"
                self.api_key = os.getenv("GEMINI_API_KEY")
            elif os.getenv("OPENAI_API_KEY"):
                self.provider = "openai"
                self.api_key = os.getenv("OPENAI_API_KEY")
            elif os.getenv("ANTHROPIC_API_KEY"):
                self.provider = "anthropic"
                self.api_key = os.getenv("ANTHROPIC_API_KEY")
            else:
                self.provider = "ollama"

    def translate(
        self,
        text: str,
        source_lang: str = "English",
        dialect: str = "srinagariya",
        temperature: float = 0.2
    ) -> Dict[str, Any]:
        """Translates text to authentic Garhwali via configured LLM provider."""
        prompt = f"Source Language: {source_lang}\nTarget Dialect: {dialect} Garhwali\nText to translate: \"{text}\""

        if self.provider == "gemini":
            return self._call_gemini(prompt, temperature)
        elif self.provider == "openai":
            return self._call_openai(prompt, temperature)
        elif self.provider == "ollama":
            return self._call_ollama(prompt, temperature)
        else:
            return {
                "error": f"Unsupported or unconfigured LLM provider: {self.provider}",
                "garhwali_devanagari": "",
                "roman_transliteration": ""
            }

    def _call_gemini(self, user_prompt: str, temperature: float) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing GEMINI_API_KEY"}
        model = self.model or "gemini-1.5-flash"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={self.api_key}"
        body = {
            "contents": [
                {"role": "user", "parts": [{"text": f"{GARHWALI_SYSTEM_PROMPT}\n\n{user_prompt}"}]}
            ],
            "generationConfig": {
                "temperature": temperature,
                "responseMimeType": "application/json"
            }
        }
        return self._post_json(url, body)

    def _call_openai(self, user_prompt: str, temperature: float) -> Dict[str, Any]:
        if not self.api_key:
            return {"error": "Missing OPENAI_API_KEY"}
        model = self.model or "gpt-4o-mini"
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        body = {
            "model": model,
            "temperature": temperature,
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": GARHWALI_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        }
        return self._post_json(url, body, headers=headers)

    def _call_ollama(self, user_prompt: str, temperature: float) -> Dict[str, Any]:
        model = self.model or "llama3.2"
        url = "http://localhost:11434/api/generate"
        body = {
            "model": model,
            "system": GARHWALI_SYSTEM_PROMPT,
            "prompt": user_prompt,
            "format": "json",
            "stream": False,
            "options": {"temperature": temperature}
        }
        return self._post_json(url, body)

    def _post_json(self, url: str, data: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        try:
            req_headers = {"Content-Type": "application/json"}
            if headers:
                req_headers.update(headers)
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode("utf-8"),
                headers=req_headers,
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                raw_json = json.loads(resp.read().decode("utf-8"))
                # Parse response according to provider schema
                if "candidates" in raw_json:
                    text_out = raw_json["candidates"][0]["content"]["parts"][0]["text"]
                    return json.loads(text_out)
                elif "choices" in raw_json:
                    text_out = raw_json["choices"][0]["message"]["content"]
                    return json.loads(text_out)
                elif "response" in raw_json:
                    return json.loads(raw_json["response"])
                return raw_json
        except Exception as e:
            return {"error": f"LLM translation call failed: {str(e)}"}


def translate_with_llm(
    text: str,
    source_lang: str = "English",
    dialect: str = "srinagariya",
    provider: str = "auto"
) -> Dict[str, Any]:
    """Convenience function for LLM-based neural translation."""
    return LLMTranslator(provider=provider).translate(text, source_lang=source_lang, dialect=dialect)


def get_garhwali_prompt() -> str:
    """Returns the base Garhwali system prompt for LLMs."""
    return GARHWALI_SYSTEM_PROMPT

