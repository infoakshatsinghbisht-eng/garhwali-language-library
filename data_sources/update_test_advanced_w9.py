# -*- coding: utf-8 -*-
with open("tests/test_garhwali_advanced.py", "rb") as f:
    content = f.read()

content = content.replace(b'self.assertEqual(stats["total_rules"], 69)', b'self.assertEqual(stats["total_rules"], 73)')
content = content.replace(b'self.assertGreaterEqual(stats["total_annotated_examples"], 150)', b'self.assertGreaterEqual(stats["total_annotated_examples"], 160)')

with open("tests/test_garhwali_advanced.py", "wb") as f:
    f.write(content)

print("Updated tests/test_garhwali_advanced.py successfully.")

