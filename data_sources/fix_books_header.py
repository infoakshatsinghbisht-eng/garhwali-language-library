# -*- coding: utf-8 -*-
with open("garhwali/culture/books.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_header = [
    "# -*- coding: utf-8 -*-\n",
    '"""\n',
    "Full-Text Digital Book Corpus and Page-by-Page Reader for Garhwali Language.\n",
    "\n",
    "Provides access to 37 complete digitised historical, linguistic, and literary books\n",
    "comprising 13,392 pages of authentic Garhwali texts, grammars, folk epics,\n",
    "gazetteers, and linguistic surveys.\n",
    '"""\n',
    "\n",
    "import json\n"
]

import_idx = -1
for i, line in enumerate(lines):
    if line.strip() == "import json":
        import_idx = i
        break

if import_idx != -1:
    updated = new_header + lines[import_idx+1:]
    with open("garhwali/culture/books.py", "w", encoding="utf-8") as f:
        f.writelines(updated)
    print("Fixed garhwali/culture/books.py header cleanly.")
