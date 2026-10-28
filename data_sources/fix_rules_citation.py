# -*- coding: utf-8 -*-
with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace('citation="Stowell (1916)', 'linguistic_citation="Stowell (1916)')
text = text.replace('citation="Verma (2003)', 'linguistic_citation="Verma (2003)')

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Replaced citation= with linguistic_citation=")

