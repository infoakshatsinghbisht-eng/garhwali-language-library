# Garhwali (गढ़वाली) Language Library — Complete Documentation Manual

```
██████╗  █████╗ ██████╗ ██╗  ██╗██╗    ██╗ █████╗ ██╗     ██╗
██╔════╝ ██╔══██╗██╔══██╗██║  ██║██║    ██║██╔══██╗██║     ██║
██║  ███╗███████║██████╔╝███████║██║ █╗ ██║███████║██║     ██║
██║   ██║██╔══██║██╔══██╗██╔══██║██║███╗██║██╔══██║██║     ██║
╚██████╔╝██║  ██║██║  ██║██║  ██║╚███╔███╔╝██║  ██║███████╗██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚═╝
```

> **The Universal Computational Linguistics, Speech Synthesis, NLP & Cultural Knowledge Suite for the Garhwali Language (Central Pahari • ISO 639-3: `gbm`).**

---

## 📑 Table of Contents

1. [Introduction & Language Overview](#1-introduction--language-overview)
2. [Library Architecture & Philosophy](#2-library-architecture--philosophy)
3. [Installation & Setup](#3-installation--setup)
4. [Quick Start Guide](#4-quick-start-guide)
5. [Module Reference Guide](#5-module-reference-guide)
   - [5.1 Universal Translation Engine (`garhwali.translator`)](#51-universal-translation-engine)
   - [5.2 Voice Translation & Speech Synthesis (`garhwali.voice`)](#52-voice-translation--speech-synthesis)
   - [5.3 Lexicon, Dictionary & 2.39M+ Inflectional Analyzer (`garhwali.lexicon`)](#53-lexicon-dictionary--morphological-analyzer)
   - [5.4 Functional Grammar & Syntactic Engine (`garhwali.grammar`)](#54-functional-grammar--syntactic-engine)
   - [5.5 Numbers, Customary Fractions & Numerals (`garhwali.numbers`)](#55-numbers-customary-fractions--numerals)
   - [5.6 Script Conversion & Phonetics (`garhwali.phonetics`)](#56-script-conversion--phonetics)
   - [5.7 Cultural Heritage, Master Bibliography & Digitized Reader (`garhwali.culture`)](#57-cultural-heritage-literature--digital-reader)
   - [5.8 20-Pillar Computational Corpus & NLP Framework (`garhwali.corpus`)](#58-20-pillar-computational-corpus--nlp-framework)
6. [Command-Line Interface (CLI)](#6-command-line-interface-cli)
7. [Interactive Web Developer Playground & REST API (`garhwali.web`)](#7-interactive-web-developer-playground)
8. [Real-World Application Recipes](#8-real-world-application-recipes)
9. [Primary Literature & Ingested Digital Sources](#9-primary-literature--ingested-digital-sources)
10. [Automated Testing & Verification](#10-automated-testing--verification)
11. [Complete Master API Function Reference](#11-complete-master-api-function-reference)

---

## 1. Introduction & Language Overview

### What is Garhwali?
**Garhwali** (गढ़वाली / गढ़वाळी, ISO 639-3: `gbm`) is an Indo-Aryan language belonging to the **Central Pahari** sub-branch of the Northern Indo-Aryan group, predominantly spoken by over 2.5 million people in the Garhwal division of Uttarakhand, India (including the districts of Pauri Garhwal, Tehri Garhwal, Chamoli, Rudraprayag, Uttarkashi, and Dehradun).

### Distinctive Linguistic Features
- **Phonology:** Retention of retroflex lateral flap [ɭ] (ळ), voiced aspirates, diphthongal preservation, and distinct tonal contours in high-altitude valleys.
- **Substantive Auxiliary:** The substantive auxiliary verb is based on the root **छ-** (*chha-*), inflecting in the present as *छौं* (1st person), *छै* (2nd person), *च / छ* (3rd person sg.), and *छन* (3rd person pl.).
- **Ergative Case Alignment:** Split-ergative syntax where transitive past tense subjects take the ergative postposition **-न** (*-na*) or **-ले** (*-le*): e.g., *राम न भात खायो* ("Ram ate rice").
- **Dative/Accusative:** Marked by **-ते** (*-te*) or **-तैं** (*-tain*) (e.g., *मिते* "to me", *त्वेते* "to you").
- **Ablative Marker:** Marked by **-बटी** (*-batee*) or **-बटि** ("from").
- **Conjunctive Participle:** Marked by **-िक** (*-ik*) / **-ईक** (*-eek*) (e.g., *खाईक* "having eaten", *जाईक* "having gone").
- **Dialectal Variation:** 5 major documented dialects:
  1. **Srinagariya (श्रीनगरिया):** Standard literary dialect of the historical royal capital of Srinagar.
  2. **Rathwali (राठवाली):** Spoken in the Rath region of eastern Pauri Garhwal.
  3. **Tehri / Gangapariya (टिहरी / गंगापरिया):** Spoken along the Bhagirathi valley in Tehri.
  4. **Salani (सलाणी):** Spoken in southern Pauri bordering Kotdwar and the plains.
  5. **Badhani (बधाणी):** Spoken in Chamoli near Badhan and the Alaknanda watershed.

---

## 2. Library Architecture & Philosophy

The `garhwali` package is engineered from the ground up to provide a complete computational stack:
1. **Zero External Dependencies:** Built entirely with Python's standard library (`urllib`, `http.server`, `json`, `math`, `struct`, `re`, `pathlib`). Runs immediately on any standard Python 3.8+ environment.
2. **Deterministic Rules + Neural Adapters:** Fast, offline, rule-based morphosyntactic engines with seamless optional zero-key pivot routing and neural LLM adapters.
3. **Massive Inflectional Coverage:** Indexes **2,391,600+ full inflected word forms** mapped to canonical dictionary lemmas.
4. **Rich Cultural Heritage:** Digitized archive of 13 historical books (3,076 pages), 20 classical Baithki & Khadi Holi ragas, 20 folk songs & jagars, 40+ sacred shrines, 80+ catalogued bibliography sources, and 20 computational corpus pillars.

---

## 3. Installation & Setup

### Standard Installation
```bash
pip install garhwali
```

### Installation from Source
```bash
git clone https://github.com/infoakshatsinghbisht-eng/garhwali-language-library.git
cd garhwali-language-library
pip install -e .
```

Verify your installation:
```python
import garhwali
print(garhwali.__version__)  # 1.2.0
print(garhwali.ISO_639_3)    # gbm
```

---

## 4. Quick Start Guide

```python
import garhwali

# 1. Universal Translation across dialects
res = garhwali.translate("Where does this mountain road go?", source="en", dialect="srinagariya")
print(res.text)       # 'ये डांडी को बाटो कख जांदू?'
print(res.romanized)  # 'Ye daandi ko baato kakh jaandoo?'

# 2. Voice Synthesis and Phonetic Syllables
v_res = garhwali.voice_translate("Welcome to our village!", generate_audio=True)
print(v_res.translated_text)   # 'हमार गांव अर घर मा तुमरो स्वागत च।'
print(v_res.syllables)         # ['ह', 'मा', 'र', 'गां', 'व', ...]
print(v_res.audio_wav_base64)  # 16-bit PCM WAV base64 string

# 3. Dictionary Lookup & Morphological Analysis
word = garhwali.lookup("काफल")
print(word.english)      # 'bayberry / Himalayan box myrtle'
analysis = garhwali.analyze("खान्दू")
print(analysis.lemma)    # 'खाणु'

# 4. Verb Conjugation
conj = garhwali.conjugate("खाणु", tense=garhwali.Tense.PRESENT, person=1, gender=garhwali.Gender.MASCULINE)
print(conj)              # 'खौंदो छौं' / 'खान्दू'

# 5. Himalayan Numbers & Customary Fractions
print(garhwali.num_to_words(25))    # 'बीस पाँच'
print(garhwali.fraction("डेढ़"))      # 1.5
print(garhwali.words_to_num("पच्चीस")) # 25

# 6. Read Digitized Canonical Books (3,076 pages)
books = garhwali.list_digital_books()
page = garhwali.read_book_page(books[0]['id'], page_number=1)
print(page.text[:150])
```

---

## 5. Module Reference Guide

### 5.1 Universal Translation Engine

`garhwali.translator` provides multi-tier translation routing:
- **Rule-Based Engine:** Conversational patterns, idiom preservation, and kinship term handling.
- **Dialect Transformation:** Dynamic phonetic inflection for Srinagariya, Rathwali, Tehri, Salani, and Badhani.
- **Zero-Key Multi-Language Pivot:** Free HTTP pivot translation translating 100+ global languages via English/Hindi intermediate pivot.
- **Neural LLM Adapter:** Built-in zero-dependency client connecting to Google Gemini, OpenAI, Claude, and local Ollama instances.

```python
import garhwali

# Direct rule-based translation
res = garhwali.translate("What is your name?", dialect="srinagariya")
print(res.text)  # तुमरो नौ क्या छ?

# Rathwali dialect variation
rath = garhwali.translate("What is your name?", dialect="rathwali")
print(rath.text) # तमरो नौ क्या छ?

# Multi-lingual pivot from Spanish
sp_res = garhwali.pivot_translate("¿Dónde está el hospital?", source_lang="es")
print(sp_res.translated_text) # अस्पताल कख छ?
```

### 5.2 Voice Translation & Speech Synthesis

`garhwali.voice` bridges text translation with speech technology:
- Generates speech synthesis markup (SSML) optimized for Himalayan languages.
- Phonetic transcription and syllable segmentation.
- Situational phrasebook with curated mountain situations (greetings, travel, dining, bazaar, health).
- Built-in 16-bit PCM WAV waveform audio generation.

```python
import garhwali

res = garhwali.voice_translate("Please give me cold spring water.", generate_audio=True)
print(res.translated_text)   # मिते धारो को ठंडो पाणी द्यावा।
print(res.romanized)         # Mite dhaaro ko thhando paanee dyaawa.
print(res.syllables)         # ['मि', 'ते', 'धा', 'रो', 'को', 'ठं', 'डो', 'पा', 'णी', 'द्या', 'वा']
print(res.ssml)              # <speak><prosody rate="medium" pitch="+5%">...</speak>
```

### 5.3 Lexicon, Dictionary & Morphological Analyzer

`garhwali.lexicon` indexes **2,428 rich dictionary entries** across **83 categories** and **2.39M+ full inflected forms**:
- Search by Garhwali, English, or Hindi meaning.
- Categories include: `education`, `governance`, `work`, `crime`, `kitchen`, `crockery`, `children`, `family`, `rituals`, `nature`, `verbs`, `anatomy`, `tools`, `clothing`, `ornament`, etc.
- Deep morphological analyzer analyzing root lemma, part of speech, tense, person, number, and gender.

```python
import garhwali

# Dictionary lookup
w = garhwali.lookup("बुरांश")
print(f"{w.garhwali} ({w.english}): {w.hindi}")

# Lemmatization of inflected forms
analysis = garhwali.analyze("खान्दू")
print(f"Lemma: {analysis.lemma}, POS: {analysis.pos}")

# Total indexed word forms
print(f"Total inflected forms: {garhwali.total_word_forms():,}") # 2,391,600
```

### 5.4 Functional Grammar, Formal Rules & Syntactic Engine

`garhwali.grammar` encapsulates complete Central Pahari morphological, syntactic, and formal linguistic rules:
- **Formal Rules Registry (`RuleRegistry`):** 15+ comprehensive grammatical rules across phonology, nominal morphology, split-ergativity, case systems, and syntax with authentic citations (Grierson, Bahuguna, Chatak, Dobhal).
- **Noun Morphology:** `pluralize`, `to_feminine`, `to_masculine`, `to_oblique`, `make_diminutive`, `make_augmentative`, `decline_noun`.
- **Case System:** Direct, Ergative (`-न / -ले`), Accusative/Dative (`-ते / -तैं`), Instrumental (`-सेती`), Ablative (`-बटी`), Genitive (`-को / -रो`), Locative (`-मा / -माझ`), Comitative (`-दगड़ी`).
- **Pronominal System:** `decline_pronoun` (across cases & dialects), `get_demonstrative`, `get_indefinite`, `get_relative_pair`, `list_all_pronouns`.
- **Verb Derivations & Aspects:** `extract_root`, `conjugate`, `conjugate_to_be`, `conjunctive_participle`, `causative` (Grade 1 & 2), `passive`, `medio_passive_inability`, `compound_verb`, `conditional`, `imperative`, `prohibitive` (`झनि`), `subjunctive`, `habitual_past`, `progressive`, `inceptive`, `completive`, `conjugate_full_paradigm`.
- **Modals:** Ability (`-सकणु`), Obligation (`-चैं / -पड़लो`), Desiderative (`-चाणु`).
- **Comprehensive Sentence Builders:**
  - `build_sentence` (SOV declarative with automatic ergative alignment)
  - `build_compound_sentence` (with coordinators *अर, पण, या, नि त*)
  - `build_conditional_sentence` (*अगर... त*)
  - `build_causal_sentence` (*किलेकि...*)
  - `build_purposive_sentence` (*खातिर...*)
  - `build_concessive_sentence` (*चाहे... तैं भी*)
  - `build_passive_sentence` (*[agent बटी] [subject] [verb-passive] गे*)
  - `build_inability_sentence` (*मि बटी हिंडे नि जांद*)
  - `build_imperative_sentence` (*खावा! / झनि खावा!*)
  - `validate_agreement` (adjective-noun gender & number concord verification)
  - `analyze_sentence` (syntactic parser detecting SOV structure, ergativity, postpositions, and interrogative/negative polarity)

```python
import garhwali

# 1. Grammar Rules Registry
rule = garhwali.RuleRegistry.get_rule("GARH-SYN-001")
print(rule.name)            # 'Canonical Subject-Object-Verb (SOV) Word Order'
print(rule.rule_statement)  # 'The basic, unmarked clause structure of Garhwali is strictly Subject - Object - Verb (SOV).'

# 2. Advanced Sentence Builders
print(garhwali.build_compound_sentence("राम ऐगे", "मोहन चलिगे"))
# 'राम ऐगे अर मोहन चलिगे।'

print(garhwali.build_conditional_sentence("बरखा होलि", "फसल भली होलि"))
# 'अगर बरखा होलि, त फसल भली होलि।'

print(garhwali.build_causal_sentence("मि स्कूल नि गे", "मि बिमार थौ"))
# 'मि स्कूल नि गे, किलेकि मि बिमार थौ।'

print(garhwali.build_inability_sentence("मि", "हिंडण"))
# 'मि बटी हिंडे नि जांद।'

# 3. Adjective-Noun Agreement Concord
concord = garhwali.validate_agreement("काली", "घ्वड़ो", gender="m", number="sg")
print(concord["valid"])               # False
print(concord["recommended_phrase"]) # 'कालो घ्वड़ो'

# 4. Syntactic Analyzer
analysis = garhwali.analyze_sentence("राम न मोहन ते किताब दी?")
print(analysis["is_question"])           # True
print(analysis["has_ergative_marking"])  # True
print(analysis["estimated_structure"])   # 'SOV'

# 5. Full Verb Paradigm Matrix (18 forms)
matrix = garhwali.conjugate_full_paradigm("खाणु", gender="m")
print(matrix["present"]["1sg"])  # 'खौंदो छौं'
print(matrix["past"]["3sg"])     # 'खायो'
print(matrix["future"]["3pl"])    # 'खौलान'
```

### 5.5 Numbers, Customary Fractions & Numerals

`garhwali.numbers` handles Himalayan numerical systems:
- Integers to Garhwali words (`num_to_words`).
- Word parsing back to integers (`words_to_num`).
- Devanagari numeral conversions (`to_devanagari_numerals`, `from_devanagari_numerals`).
- Ordinals (`ordinal`).
- Himalayan fractions (`fraction`): *चौथाई* (0.25), *आधा* (0.5), *पौणा* (0.75), *सवा* (1.25), *डेढ़* (1.5), *ढाई* (2.5), *साढ़े* (+0.5).

```python
import garhwali

print(garhwali.num_to_words(150))               # एक सौ पचास
print(garhwali.to_devanagari_numerals(150))     # १५०
print(garhwali.from_devanagari_numerals("१५०")) # 150
print(garhwali.words_to_num("एक सौ बीस"))       # 120
print(garhwali.fraction("ढाई"))                 # 2.5
```

### 5.6 Script Conversion & Phonetics

`garhwali.phonetics` provides bi-directional phonetics and script transliteration:
- Devanagari to Latin phonetics (`devanagari_to_latin`).
- Latin to Devanagari (`latin_to_devanagari`).
- Syllabic boundary extraction (`syllables`).

```python
import garhwali

print(garhwali.devanagari_to_latin("जय बदरीविशाल")) # Jai Badreevishaal
print(garhwali.syllables("बदरीनाथ"))               # ['ब', 'द', 'री', 'ना', 'थ']
```

### 5.7 Cultural Heritage, Literature & Digital Reader

`garhwali.culture` contains unmatched cultural corpora:
- **Master Bibliography:** 80+ canonical works catalogued with full author, year, publisher, and summary metadata.
- **Digitized Books Corpus:** 13 complete books digitized across **3,076 pages** accessible via `read_book_page(book_id, page_number)`.
- **Classical Holi Corpus:** 20 compositions across Baithki, Khadi, and Mahila Holi covering classical ragas (Kafi, Pilu, Khamaj, Bhairavi, Basant, Yaman, Desh, Malkauns).
- **Traditional Folk Songs:** 20 catalogued songs and jagars with full verses, English translations, and cultural context.
- **Sacred Geography:** Panch Kedar (Kedarnath, Tungnath, Rudranath, Madhyamaheshwar, Kalpeshwar), Panch Badri, Panch Prayag, Bugyals, and historical shrines.
- **Local Deities:** Bhomiya, Ghandiyal, Narsingh, Goril, Achhari, Matrikas, and Kshetrapals.
- **Surnames & Clans:** Lineages, gotras, and historical origins of Garhwali communities.
- **Flora & Rituals:** 70+ ethnobotanical mountain plants and 60+ temple implements.
- **Proverbs & Riddles:** 95 traditional proverbs (*पखाणा*) and riddles (*आणा*).

```python
import garhwali

# Access Classical Holi compositions
holi_songs = garhwali.FolkloreTreasury.list_holi_songs(raag="Kafi")
print(f"Found {len(holi_songs)} songs in Raag Kafi")

# Read a page of historical literature
page = garhwali.read_book_page("bhatt_1976_garhwali_sahitya", page_number=5)
print(page.text[:200])

# Access random proverb
prov = garhwali.proverbs.random()
print(f"Proverb: {prov['pakhana']} -> {prov['meaning']}")
```

### 5.8 20-Pillar Computational Corpus & NLP Framework

`garhwali.corpus` provides standard NLP computational resources:
- 20-Pillar Corpus taxonomy (`CorpusTaxonomy`).
- High-quality parallel sentence pairs (`SentenceCorpus`).
- Curated linguistic idioms and metaphorical expressions (`IdiomCorpus`).

```python
import garhwali

pillars = garhwali.list_corpus_pillars()
print(f"Indexed {len(pillars)} NLP computational corpus pillars")

sentences = garhwali.search_sentences("बाटो")
print(f"Found {len(sentences)} parallel sentences matching 'बाटो'")
```

---

## 6. Command-Line Interface (CLI)

The package provides a built-in CLI tool:

```bash
# Translate text
garhwali translate "Where is the hospital?" --dialect srinagariya

# Look up words in dictionary
garhwali lookup "काफल"

# Conjugate verbs
garhwali conjugate "खाणु" --tense present --person 3 --gender m

# Convert numbers
garhwali numbers 125

# Read digital book pages
garhwali read-book bhatt_1976_garhwali_sahitya --page 1
```

---

## 7. Interactive Web Developer Playground

The library includes an interactive, zero-dependency Web GUI playground powered by Python's built-in `http.server`.

To launch the playground:
```bash
python -m garhwali.web.app 8080
```
Open `http://localhost:8080` in your browser.

The playground features 7 interactive tabs:
1. **Universal Translator:** Multi-lingual translation with real-time dialect switcher.
2. **Voice & Audio:** Interactive speech synthesizer with SSML generator and PCM audio player.
3. **Dictionary:** Instant search across all 2,428 words and 83 categories.
4. **Verb Engine:** Dynamic conjugation across all tenses, aspects, persons, and genders.
5. **Numbers:** Real-time numeral and customary fraction converter.
6. **Folklore & Holi:** Classical Baithki and Khadi Holi music player with verses and translations.
7. **Digital Reader:** 3,076-page historical book reader with page turning.

---

## 8. Real-World Application Recipes

### Recipe 1: Building a FastAPI Garhwali API Server
```python
from fastapi import FastAPI
import garhwali

app = FastAPI(title="Garhwali AI Service")

@app.post("/translate")
def translate_api(text: str, source: str = "auto", dialect: str = "srinagariya"):
    res = garhwali.translate(text, source=source, dialect=dialect)
    return res._asdict()

@app.get("/voice")
def voice_api(text: str):
    res = garhwali.voice_translate(text, generate_audio=True)
    return res.to_dict()
```

### Recipe 2: Linguistic Tokenization and Lemmatization Pipeline
```python
import garhwali

def process_garhwali_text(text: str):
    tokens = text.split()
    results = []
    for token in tokens:
        analysis = garhwali.analyze(token)
        results.append({
            "token": token,
            "lemma": analysis.lemma,
            "pos": analysis.pos,
            "syllables": garhwali.syllables(token)
        })
    return results
```

---

## 9. Primary Literature & Ingested Digital Sources

1. **Govind Chatak (1959):** *Garhwali Bhasha*, Dehradun.
2. **Mukund Ram Barthwal (1976):** *Garhwali Sahitya ka Itihas*, Srinagar Garhwal.
3. **Pt. Ganga Datt Upreti (1894):** *Proverbs & Folklore of Kumaun and Garhwal*, Ludhiana Mission Press.
4. **Shaligram Vaishnav (1930):** *Garhwali Pakhana*, Nandprayag.
5. **G. A. Grierson (1916):** *Linguistic Survey of India, Vol. IX, Part IV: Central Pahari Languages (Garhwali & Kumaoni)*, Calcutta.
6. **Uttarakhand Open University (2020):** *CGL-101, CGL-102, CGL-103, CGL-104 Garhwali Bhasha evam Sahitya Course Series*, Haldwani.
7. **Pushkar Singh Kandari (2016):** *Garhwali Muhavaron-Kahavaton ka Vrihad Sangrah*, Vani Prakashan, New Delhi.
8. **Mahavir Prasad Gairola & E. S. Oakley (1935):** *Himalayan Folklore*, Allahabad.

---

## 10. Automated Testing & Verification

Run the comprehensive unit test suite:
```bash
python -m unittest discover tests
```

The test suite covers:
- Translator accuracy across English, Hindi, and Hinglish.
- Dialectal inflections across all 5 dialects.
- Morphological lemmatization across regular and irregular stems.
- Functional verb conjugations and modal auxiliaries.
- Number conversions and fraction parsing.
- Digitized book page reading and search indexing.
- Voice translation and SSML speech markup generation.

---

## 11. Complete Master API Function Reference

### 🔤 1. Translation & Speech
- `garhwali.translate(text, source="auto", target="garhwali", dialect="srinagariya", method="auto", api_key=None)`
- `garhwali.pivot_translate(text, source_lang="auto", target_lang="garhwali", dialect="srinagariya")`
- `garhwali.translate_with_llm(text, source_lang="English", dialect="srinagariya", provider="auto")`
- `garhwali.voice_translate(text, source_lang="auto", method="auto", generate_audio=False, api_key=None)`
- `garhwali.GarhwaliVoiceSynthesizer.get_speech_ssml(text, rate="medium", pitch="+5%")`
- `garhwali.GarhwaliVoiceSynthesizer.generate_pcm_wav(duration_seconds=0.5, freq=440.0)`

### 📖 2. Lexicon & 2.39M+ Inflectional Analyzer
- `garhwali.lookup(word: str)`
- `garhwali.search(query: str, limit: int = 20)`
- `garhwali.analyze(word: str) -> MorphAnalysis`
- `garhwali.total_word_forms() -> int`
- `garhwali.phrases.all()`, `garhwali.phrases.random()`
- `garhwali.proverbs.all()`, `garhwali.proverbs.random()`
- `garhwali.riddles.all()`, `garhwali.riddles.random()`

### ⚡ 3. Verb Conjugation & Verbal Syntax
- `garhwali.extract_root(verb_infinitive: str) -> str`
- `garhwali.conjugate_to_be(person=3, number="singular", tense="present", dialect="srinagariya")`
- `garhwali.conjugate(verb, tense=Tense.PRESENT, person=3, gender=Gender.MASCULINE, number=GrammaticalNumber.SINGULAR, dialect="srinagariya")`
- `garhwali.conjunctive_participle(verb: str) -> str`
- `garhwali.causative(verb: str, grade: int = 1) -> str`
- `garhwali.passive(verb: str) -> str`
- `garhwali.medio_passive_inability(verb: str, subject_agent: str, dialect="srinagariya") -> str`
- `garhwali.compound_verb(main_verb: str, vector_verb: str) -> str`
- `garhwali.conditional(condition_clause: str, consequence_clause: str) -> str`
- `garhwali.imperative(verb: str, honorific=False, plural=False) -> str`
- `garhwali.prohibitive(verb: str, honorific=False) -> str`
- `garhwali.modal_ability(verb: str, person=3, gender="M", tense="present") -> str`
- `garhwali.modal_obligation(verb: str, subject: str, urgency="need") -> str`
- `garhwali.modal_desiderative(verb: str, subject: str, tense="present") -> str`

### 🏛️ 4. Sentence Construction & Syntax Engine
- `garhwali.build_sentence(subject, direct_object=None, indirect_object=None, verb="खाणु", tense=Tense.PRESENT, person=3, gender=Gender.MASCULINE, negative=False) -> str`
- `garhwali.interrogative_sentence(sentence, question_type="polar", question_word=None) -> str`
- `garhwali.relative_correlative(relative_clause, correlative_clause, marker_pair="जो...सो") -> str`
- `garhwali.echo_word(word: str) -> str`

### 🏷️ 5. Nouns, Postpositions & Declensions
- `garhwali.pluralize(noun: str) -> str`
- `garhwali.to_feminine(noun_or_adj: str) -> str`
- `garhwali.to_masculine(noun_or_adj: str) -> str`
- `garhwali.to_oblique(noun: str, number="singular") -> str`
- `garhwali.make_diminutive(noun: str) -> str`
- `garhwali.make_augmentative(noun: str) -> str`
- `garhwali.decline_noun(noun: str, gender="M") -> Dict`
- `garhwali.attach_case(noun: str, case_name: str, number="singular", dialect="srinagariya") -> str`
- `garhwali.get_marker(case_name: str) -> CaseMarker`

### 🔢 6. Numbers, Numerals & Fractions
- `garhwali.num_to_words(n: int, script="devanagari") -> str`
- `garhwali.words_to_num(text: str) -> int`
- `garhwali.to_devanagari_numerals(n: int) -> str`
- `garhwali.from_devanagari_numerals(text: str) -> str`
- `garhwali.ordinal(n: int) -> str`
- `garhwali.fraction(name: str) -> Union[float, str, None]`

### 🏔️ 7. Cultural Heritage, Literature & Digital Reader
- `garhwali.FolkloreTreasury.list_songs(genre=None)`
- `garhwali.FolkloreTreasury.list_holi_songs(form=None, raag=None)`
- `garhwali.FolkloreTreasury.get_holi_song(song_id)`
- `garhwali.read_book_page(book_id: str, page_number: int)`
- `garhwali.list_digital_books()`
- `garhwali.get_digital_book(book_id: str)`
- `garhwali.search_digital_books(query: str)`
- `garhwali.BibliographyTreasury.get_bibliography()`
- `garhwali.PlacesTreasury.list_places()`
- `garhwali.DeitiesTreasury.list_deities()`
- `garhwali.SurnamesTreasury.list_surnames()`
- `garhwali.FloraTreasury.list_plants()`
- `garhwali.RitualsTreasury.list_items()`

---

*Copyright (c) 2026 Akshat Singh Bisht. Released under the MIT License.*
