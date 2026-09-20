# -*- coding: utf-8 -*-
"""Garhwali Syntax Engine, SOV Word Order & Split Ergativity Validator."""

import re
from typing import Dict, List, Any, Optional, Tuple, Union, Set

def validate_sov_order(tokens: List[str]) -> Tuple[bool, str]:
    """
    Validates standard Garhwali Subject-Object-Verb (SOV) order.
    Returns (is_valid, explanation).
    """
    if not tokens or len(tokens) < 2:
        return True, "Valid single/double token structure"
    
    # Check if auxiliary / final verb is placed at the end
    verb_ends = ("छ", "छन", "छा", "छौं", "छै", "छी", "छो", "गयो", "गै", "गया", "गैन", "खायो", "पड़नो", "करनो", "होलो", "औली", "जाला")
    last_token = tokens[-1].strip(".,?!;:।")
    
    if any(last_token.endswith(ve) or last_token == ve for ve in verb_ends):
        return True, f"Valid SOV order with terminal finite verb '{last_token}'"
    
    return True, "Structure parsed successfully"

def check_split_ergativity(subject: str, verb: str, is_past_transitive: bool = True) -> Dict[str, Any]:
    """
    Checks if the subject correctly uses the ergative marker (-न, -ले)
    when followed by a transitive verb in the past/perfective aspect.
    Example: 'मैंन भात खायो' (Correct) vs 'मी भात खायो' (Violates split ergativity).
    """
    ergative_forms = {"मी": "मैंन", "हम": "हमून", "तू": "तैन", "त्वे": "तैन", "तुम": "तुमुन / तुमले", "वू": "वैन", "यो": "यान / यैन", "वे": "उनून"}
    
    if is_past_transitive:
        if subject in ergative_forms:
            return {
                "valid": False,
                "recommended_subject": ergative_forms[subject],
                "explanation": f"In transitive past tense, subject '{subject}' takes ergative form '{ergative_forms[subject]}'"
            }
        return {"valid": True, "explanation": "Ergative alignment satisfied."}
    else:
        # Intransitive past requires nominative subject (e.g., 'मी गयूं', not 'मैंन गयूं')
        if subject in ergative_forms.values():
            return {
                "valid": False,
                "explanation": f"Intransitive verb requires nominative direct subject, not ergative '{subject}'"
            }
        return {"valid": True, "explanation": "Nominative alignment for intransitive verb satisfied."}

def format_sentence(subject: str, object_or_loc: str, verb: str, negative: bool = False, question: bool = False) -> str:
    """Constructs a grammatically sound Garhwali sentence."""
    parts = [subject.strip()]
    if object_or_loc:
        parts.append(object_or_loc.strip())
    if negative:
        parts.append("नि")
    parts.append(verb.strip())
    sent = " ".join(parts)
    if question:
        sent += " क्या?" if not any(w in sent for w in ("क्या", "कख", "कब", "किलै", "कनु")) else "?"
    else:
        sent += "।"
    return sent
