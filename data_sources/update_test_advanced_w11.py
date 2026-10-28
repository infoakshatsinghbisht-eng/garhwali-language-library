# -*- coding: utf-8 -*-
with open("tests/test_garhwali_advanced.py", "rb") as f:
    content = f.read()

content = content.replace(b'self.assertEqual(stats["total_rules"], 77)', b'self.assertEqual(stats["total_rules"], 81)')
content = content.replace(b'self.assertGreaterEqual(stats["total_annotated_examples"], 165)', b'self.assertGreaterEqual(stats["total_annotated_examples"], 175)')

with open("tests/test_garhwali_advanced.py", "wb") as f:
    f.write(content)

print("Updated tests/test_garhwali_advanced.py for Wave 11.")

