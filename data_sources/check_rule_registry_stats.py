# -*- coding: utf-8 -*-
import os, sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))

from garhwali.grammar.rules import RuleRegistry

rules = RuleRegistry.all_rules()
print(f"Total rules: {len(rules)}")
for r in rules[-4:]:
    print(f"  {r.rule_id} -> {r.name}")
total_examples = sum(len(r.examples) for r in rules)
print(f"Total annotated examples: {total_examples}")

