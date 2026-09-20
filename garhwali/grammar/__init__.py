# -*- coding: utf-8 -*-
"""Garhwali Grammar Package."""

from .nouns import GarhwaliNoun, CORE_GARHWALI_NOUNS
from .pronouns import GARHWALI_PRONOUNS_TABLE, get_pronoun_form
from .verbs import GarhwaliVerb, CORE_GARHWALI_VERBS
from .postpositions import GARHWALI_POSTPOSITIONS
from .syntax import validate_sov_order

__all__ = [
    "GarhwaliNoun", "CORE_GARHWALI_NOUNS",
    "GARHWALI_PRONOUNS_TABLE", "get_pronoun_form",
    "GarhwaliVerb", "CORE_GARHWALI_VERBS",
    "GARHWALI_POSTPOSITIONS", "validate_sov_order"
]
