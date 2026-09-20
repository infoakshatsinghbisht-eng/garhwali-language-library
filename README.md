# 🏔️ Garhwali (गढ़वाली) Language Library

[![PyPI Version](https://img.shields.io/pypi/v/garhwali.svg)](https://pypi.org/project/garhwali/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/garhwali.svg)](https://pypi.org/project/garhwali/)
[![Python Versions](https://img.shields.io/pypi/pyversions/garhwali.svg)](https://pypi.org/project/garhwali/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repository](https://img.shields.io/badge/GitHub-garhwali--language--library-blue.svg)](https://github.com/infoakshatsinghbisht-eng/garhwali-language-library)
[![Website](https://img.shields.io/badge/Website-akshatsinghbisht.com-orange.svg)](https://akshatsinghbisht.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Akshat_Singh_Bisht-0077b5.svg)](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-Akshat_Bisht-00ccbb.svg)](https://www.researchgate.net/profile/Akshat-Bisht-8)
[![Amazon Author](https://img.shields.io/badge/Amazon-Author_Page-FF9900.svg)](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28?ref=sr_ntt_srch_lnk_1&qid=1789906571&sr=8-1&shoppingPortalEnabled=true)

A comprehensive Python library, NLP toolkit, and computational linguistics engine for the **Garhwali Language (गढ़वाली भाषा)** — spoken by over 3 million people across Uttarakhand's Garhwal Himalayas (Pauri, Tehri, Chamoli, Uttarkashi, Rudraprayag, Dehradun, and Haridwar).

---

## 🌟 Key Capabilities

1. **📚 2,390,000+ Morphological Word Forms (`garhwali.lexicon.morphology`)**:
   - Dynamic inflectional engine covering noun declensions (8 cases $\times$ gender $\times$ number), pronoun cases, full verb aspectual/temporal matrices, and postpositional compounds.
2. **🔄 Multi-Dialect Translation Engine (`garhwali.translator`)**:
   - Fast, rule-based & phonetic translation across **English $\leftrightarrow$ Garhwali**, **Hindi $\leftrightarrow$ Garhwali**, and **Hinglish $\leftrightarrow$ Garhwali**.
   - Supports 5 distinct dialect regions:
     - **Srinagariya** (Standard Pauri Garhwal)
     - **Rathwali** (Eastern Pauri / Rath region)
     - **Tehri** (Tehri Garhwal & Bhagirathi Valley)
     - **Salani** (Southern Pauri / Kotdwar)
     - **Badhani** (Chamoli / Alaknanda Valley)
3. **⚖️ Split-Ergativity & SOV Syntax Validator (`garhwali.grammar.syntax`)**:
   - Enforces authentic Central Pahari ergative case markings (`-न / -ले` in transitive perfective clauses) vs nominative direct alignment in intransitive past.
4. **📖 Rich Categorized Lexicon (`garhwali.lexicon.dictionary`)**:
   - Comprehensive databases across body parts (*मुंड, आँख, नाख*), traditional farming tools (*पुंगड़ी, दथुड़ा, हल*), Himalayan flora/wild fruits (*काफल, बुरांस, हिंसर, किलमोड़ा*), traditional ornaments (*नथुली, हंसुली, गुलूबंद*), cuisine (*झंगोरा, कोदा, फांणा, काफली*), and emotions (*यकूलांस, माया, दौल*).
5. **📜 Himalayan Lore & Culture (`garhwali.culture`)**:
   - Authentic Proverbs (*पखाणा / औखाण*), Interactive Folk Riddles (*आणा*), 12 Garhwali Months & 6 Ritus, Traditional Festivals (*Phooldei, Igas Bagwal, Nanda Devi Raj Jat, Harela*), and classic literary heroes (*Madho Singh Bhandari, Jeetu Bagdwal, Chandra Kunwar Bartwal, Narendra Singh Negi*).
6. **🔢 Garhwali Numbers Engine (`garhwali.numbers`)**:
   - Converts any integer (0 to 1 crore) into Garhwali words, ordinals, and Devanagari numerals.
7. **🎙️ Voice Synthesis & SSML (`garhwali.voice`)**:
   - Himalayan pitch envelope generator, SSML formatter, and uncompressed PCM WAV synthesis.

---

## 🚀 Installation & Quick Start

```bash
pip install garhwali
```

### 💻 Python Usage Examples

```python
import garhwali

# 1. Multi-Dialect Translation
res = garhwali.translate("Where are you from?", dialect="tehri")
print(res.text)  # "तुमु कथी बटी छा?"

res_hinglish = garhwali.translate("are yah chal kyon nahin raha hai")
print(res_hinglish.text)  # "अरे यो किलै नि चलनो छ?"

# 2. Dictionary & Vocabulary Lookup
word = garhwali.lookup("बुरांस")
print(word)
# {'garhwali': 'बुरांस', 'hindi': 'बुरांश का लाल फूल', 'english': 'rhododendron flower', 'category': 'flora', ...}

# 3. Numbers in Garhwali
print(garhwali.num_to_words(2026))  # "दुई हजार बीस छ"
print(garhwali.to_devanagari_numerals(2026))  # "२०२६"

# 4. Phonetics & Syllables
print(garhwali.syllables("गढ़वाली"))  # ['गढ़', 'वा', 'ली']
print(garhwali.devanagari_to_latin("ब्वै कख छिन?"))  # "Bwai kakh chhin?"

# 5. Himalayan Calendar & Culture
print(garhwali.get_current_season())  # {'name_garhwali': 'सरद', 'name_hindi': 'शरद', 'english_season': 'Autumn'}
print(garhwali.proverbs.random())  # {'pakhana': 'काफल पाको मैन नी चाखो।', 'meaning': '...'}
```

---

## 🧪 Testing

```bash
python -m unittest discover -s tests -v
```

---

## 👤 Author & Creator Profile

* **Creator & Author**: **Akshat Singh Bisht**
* **Official Website**: [https://akshatsinghbisht.com/](https://akshatsinghbisht.com/)
* **Email**: [infoakshatsinghbisht@gmail.com](mailto:infoakshatsinghbisht@gmail.com)
* **LinkedIn**: [Akshat Singh Bisht on LinkedIn](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
* **Amazon Author Profile**: [Akshat Singh Bisht on Amazon](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28?ref=sr_ntt_srch_lnk_1&qid=1789906571&sr=8-1&shoppingPortalEnabled=true)
* **ResearchGate**: [Akshat Bisht on ResearchGate](https://www.researchgate.net/profile/Akshat-Bisht-8)
* **GitHub**: [@infoakshatsinghbisht-eng](https://github.com/infoakshatsinghbisht-eng)
* **Repository**: [https://github.com/infoakshatsinghbisht-eng/garhwali-language-library](https://github.com/infoakshatsinghbisht-eng/garhwali-language-library)
* **PyPI Package**: [https://pypi.org/project/garhwali/](https://pypi.org/project/garhwali/)

---

## 📄 License
This project is licensed under the **MIT License** — dedicated to the computational preservation, linguistic research, and cultural advancement of the Himalayan languages of Uttarakhand.
