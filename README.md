# 🏔️ Garhwali (गढ़वाली) Language Library

A comprehensive Python library, NLP toolkit, and cultural heritage engine for the **Garhwali Language (गढ़वाली भाषा)** — spoken by over 3 million people across Uttarakhand's Garhwal Himalayas (Pauri, Chamoli, Tehri, Uttarkashi, Rudraprayag, Dehradun, and Haridwar).

---

## 🌟 Key Features

1. **📚 300,000+ Inflected Word Forms**:
   - High-performance morphological engine covering noun declensions, pronoun cases, verb tenses/aspects, and postpositional compounds.
2. **🔄 Multi-Strategy Translator**:
   - Fast, accurate translation across **English $\leftrightarrow$ Garhwali**, **Hindi $\leftrightarrow$ Garhwali**, and **Hinglish $\leftrightarrow$ Garhwali**.
3. **🏔️ Dialect Support**:
   - **Srinagariya** (Standard Pauri Garhwal)
   - **Rathwali / Tehri** (Tehri Garhwal)
   - **Salani** (Southern Pauri / Kotdwar)
   - **Badhani** (Chamoli / Alaknanda Valley)
4. **🗣️ Phonetics & Syllable Engine**:
   - Native syllabification, Devanagari $\leftrightarrow$ Romanized phonetic transliteration.
5. **📜 Himalayan Lore & Culture**:
   - Proverbs (*अखाण / पखाण*), Interactive Riddles (*आणा*), 12 Garhwali Months & 6 Ritus, Festivals (*Phooldei, Igas Bagwal, Nanda Devi Raj Jat*), and classic folk literature (*Chaita ki Chaitwali, Bedu Pako*).
6. **🔢 Garhwali Numbers**:
   - Converts any integer into Garhwali words, ordinals, and Devanagari numerals.
7. **🎙️ Voice Synthesis SSML & Audio**:
   - Himalayan pitch envelope generator, SSML formatter, and uncompressed PCM WAV synthesis.

---

## 🚀 Installation & Usage

```bash
pip install garhwali
```

### Quick Python Example

```python
import garhwali

# 1. Translate English or Hinglish to Garhwali
res = garhwali.translate("Where is mom?")
print(res.text)  # "ईजा कहाँ छ?"

res_hinglish = garhwali.translate("are yah chal kyon nahin raha hai")
print(res_hinglish.text)  # "अरे यो किलै नि चलनो छ?"

# 2. Dialect variations
print(garhwali.translate("What is your name?", dialect="rathwali").text)  # "तमरो नाव क्या छ?"
print(garhwali.translate("What is your name?", dialect="salani").text)    # "तुमारू नाव क्या छ?"

# 3. Numbers to Garhwali words
print(garhwali.num_to_words(2026))  # "दुई हजार छब्बीस"
print(garhwali.to_devanagari_numerals(2026))  # "२०२६"

# 4. Phonetics & Syllables
print(garhwali.syllables("गढ़वाली"))  # ['गढ़', 'वा', 'ली']
print(garhwali.devanagari_to_latin("ईजा कहाँ छ?"))  # "Ija kahaan chha?"

# 5. Culture & Calendar
print(garhwali.get_current_season())  # {'name_garhwali': 'सरद', 'english': 'Autumn'}
print(garhwali.proverbs.all()[0]["garhwali"])  # "अपणी घाम मा कुकुर भी राजा।"
```

---

## 🧪 Testing

```bash
python -m unittest discover tests
```

---

## 📄 License
MIT License. Open-source for the preservation and advancement of Himalayan languages.
