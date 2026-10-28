# -*- coding: utf-8 -*-
with open("tests/test_garhwali_advanced.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('self.assertEqual(stats["total_rules"], 53)', 'self.assertEqual(stats["total_rules"], 57)')
text = text.replace('self.assertGreaterEqual(stats["total_annotated_examples"], 120)', 'self.assertGreaterEqual(stats["total_annotated_examples"], 130)')

with open("tests/test_garhwali_advanced.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated tests/test_garhwali_advanced.py to 57 rules and 130 examples.")

