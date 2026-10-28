# -*- coding: utf-8 -*-
"""
Bumps package version from 1.2.0 to 1.3.0 across all package configuration files.
"""

import re

# 1. garhwali/__init__.py
with open("garhwali/__init__.py", "r", encoding="utf-8") as f:
    init_content = f.read()

init_content = init_content.replace('__version__ = "1.2.0"', '__version__ = "1.3.0"')
init_content = re.sub(
    r"- Master Bibliography & Digitized Literary Corpus \(.*?\)",
    "- Master Bibliography & Digitized Literary Corpus (231 Canonical Books Catalogued, 86 Full Books with 23,856 Pages)",
    init_content
)
with open("garhwali/__init__.py", "w", encoding="utf-8") as f:
    f.write(init_content)
print("Updated garhwali/__init__.py to 1.3.0")

# 2. setup.py
with open("setup.py", "r", encoding="utf-8") as f:
    setup_content = f.read()
setup_content = setup_content.replace('version="1.2.0"', 'version="1.3.0"')
with open("setup.py", "w", encoding="utf-8") as f:
    f.write(setup_content)
print("Updated setup.py to 1.3.0")

# 3. pyproject.toml
with open("pyproject.toml", "r", encoding="utf-8") as f:
    pyproject_content = f.read()
pyproject_content = pyproject_content.replace('version = "1.2.0"', 'version = "1.3.0"')
with open("pyproject.toml", "w", encoding="utf-8") as f:
    f.write(pyproject_content)
print("Updated pyproject.toml to 1.3.0")

# 4. DOCUMENTATION.md
with open("DOCUMENTATION.md", "r", encoding="utf-8") as f:
    doc_content = f.read()
doc_content = doc_content.replace("print(garhwali.__version__)  # 1.2.0", "print(garhwali.__version__)  # 1.3.0")
with open("DOCUMENTATION.md", "w", encoding="utf-8") as f:
    f.write(doc_content)
print("Updated DOCUMENTATION.md to 1.3.0")

# 5. garhwali_llm_context.xml
with open("garhwali_llm_context.xml", "r", encoding="utf-8") as f:
    xml_content = f.read()
xml_content = xml_content.replace('<library id="garhwali" version="1.2.0">', '<library id="garhwali" version="1.3.0">')
with open("garhwali_llm_context.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)
print("Updated garhwali_llm_context.xml to 1.3.0")

# 6. data_sources/final_audit.py
with open("data_sources/final_audit.py", "r", encoding="utf-8") as f:
    audit_script = f.read()
audit_script = audit_script.replace('"package_version": "1.2.0"', '"package_version": "1.3.0"')
with open("data_sources/final_audit.py", "w", encoding="utf-8") as f:
    f.write(audit_script)
print("Updated data_sources/final_audit.py to 1.3.0")

