# -*- coding: utf-8 -*-
with open("tests/test_garhwali_advanced.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('self.assertEqual(stats["total_rules"], 66)', 'self.assertEqual(stats["total_rules"], 69)')
text = text.replace('self.assertGreaterEqual(stats["total_annotated_examples"], 145)', 'self.assertGreaterEqual(stats["total_annotated_examples"], 150)')

with open("tests/test_garhwali_advanced.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated tests/test_garhwali_advanced.py for Wave 8.")

