# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="garhwali",
    version="1.0.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    maintainer_email="infoakshatsinghbisht@gmail.com",
    description="Garhwali (गढ़वाली) Language Library: 2.3M+ Inflections, Multi-dialect Translation, NLP Toolkit, and Himalayan Culture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infoakshatsinghbisht-eng/garhwali-language-library",
    project_urls={
        "Author": "https://github.com/infoakshatsinghbisht-eng",
        "Bug Tracker": "https://github.com/infoakshatsinghbisht-eng/garhwali-language-library/issues",
        "Documentation": "https://github.com/infoakshatsinghbisht-eng/garhwali-language-library#readme",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "garhwali.lexicon": ["data/*.json"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "garhwali=garhwali.cli:main",
        ],
    },
)
