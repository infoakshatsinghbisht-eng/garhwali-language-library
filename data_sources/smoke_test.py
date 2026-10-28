# -*- coding: utf-8 -*-
import os
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))

import garhwali
from garhwali.culture.books import BooksCorpus
from garhwali.grammar.rules import RuleRegistry
from garhwali.culture.bibliography import BibliographyTreasury

print(f"Library Version: {garhwali.__version__}")
print(f"Digitized Books: {len(BooksCorpus.list_books())}")
print(f"Total Digitized Pages: {BooksCorpus.total_pages_in_library():,}")
print(f"Grammar Rules: {len(RuleRegistry.all_rules())}")
print(f"Bibliography Records: {len(BibliographyTreasury.list_books())}")

print("\n--- Search across all 56 Books for 'Mana' ---")
results = BooksCorpus.search_all_books("Mana")
print(f"Total matching pages: {len(results)}")
for r in results[:3]:
    print(f"  [{r.book_id}] page {r.page_number} ({r.match_count} matches): {r.snippet[:90]}...")

print("\n--- Check Wave 6 Grammar Rule ---")
rule = RuleRegistry.get_rule("GARH-VRB-014")
print(f"Rule: {rule.rule_id} -> {rule.name}")
print(f"Statement: {rule.rule_statement}")
for eg in rule.examples:
    print(f"  Example: {eg.garhwali} -> {eg.hindi} ({eg.english})")

print("\nALL SYSTEMS FUNCTIONAL!")
