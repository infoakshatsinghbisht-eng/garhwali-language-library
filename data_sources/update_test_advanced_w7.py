# -*- coding: utf-8 -*-
with open("tests/test_garhwali_advanced.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('self.assertEqual(stats["total_rules"], 63)', 'self.assertEqual(stats["total_rules"], 66)')
text = text.replace('self.assertGreaterEqual(stats["total_annotated_examples"], 140)', 'self.assertGreaterEqual(stats["total_annotated_examples"], 145)')

with open("tests/test_garhwali_advanced.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated tests/test_garhwali_advanced.py for Wave 7.")

