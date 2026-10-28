# -*- coding: utf-8 -*-
with open("tests/test_garhwali_advanced.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('self.assertEqual(stats["total_rules"], 60)', 'self.assertEqual(stats["total_rules"], 63)')
text = text.replace('self.assertGreaterEqual(stats["total_annotated_examples"], 135)', 'self.assertGreaterEqual(stats["total_annotated_examples"], 140)')

with open("tests/test_garhwali_advanced.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated tests/test_garhwali_advanced.py")
