# -*- coding: utf-8 -*-
"""LLM Adapter for Neural Garhwali Translation."""

from typing import Dict, List, Any, Optional, Tuple, Union, Set

def get_garhwali_prompt(text: str, source_lang: str = "en", dialect: str = "srinagariya") -> str:
    return f"""You are an expert native Garhwali (गढ़वाली) linguist.
Translate the following {source_lang} text into authentic, natural, colloquial Garhwali ({dialect} dialect):

Source Text: "{text}"
Garhwali Translation:"""
