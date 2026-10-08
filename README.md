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

## 🌟 Key Capabilities & Modules

1. **📚 2,390,000+ Morphological Word Forms (`garhwali.lexicon.morphology`)**:
   - Dynamic inflectional engine covering noun declensions (8 cases $\times$ gender $\times$ number), pronoun cases, full verb aspectual/temporal matrices, and postpositional compounds across 5 dialects.
2. **🔄 Multi-Dialect Translation Engine (`garhwali.translator`)**:
   - Fast, rule-based & phonetic translation across **English $\leftrightarrow$ Garhwali**, **Hindi $\leftrightarrow$ Garhwali**, and **Hinglish $\leftrightarrow$ Garhwali**.
   - Supports 5 distinct dialect regions:
     - **Srinagariya** (Standard Pauri Garhwal)
     - **Rathwali** (Eastern Pauri / Rath region)
     - **Tehri** (Tehri Garhwal & Bhagirathi Valley)
     - **Salani** (Southern Pauri / Kotdwar)
     - **Badhani** (Chamoli / Alaknanda Valley)
3. **📖 1,000+ Verified Lexical Lemmas (`garhwali.lexicon.dictionary`)**:
   - Richly categorized vocabulary database with dialect variants across 27 domains:
     - **Kinship & Family**: *बुबा, दद्दा, भुली, दीदी, भुलू, नौनी, नौना, ब्वारी, जंवाई, कक्यो, काकी, मामा, मामी, बूबू, दादी, नाती, सौरास, मैत, ध्याणी, समधी, जेठ, देवर, ननद, साला, साली, पुरखा*
     - **Marriage & Wedding Culture**: *ब्याव, मंगणी, बन्ना, बन्नी, धूली-अर्घ, मंगल-गीत, कन्यादान, फेरा, बिदाई, रौंतेली, बरात, जनेती, नथुली, गुलोबंद, पिछौड़ा, अरसा, नेग, न्यौता*
     - **Social Relationships**: *दगाड़ी, संगी, पड़ोसी, पाहुणा, सयाणा, अणजाण, गौंंत्यार, जैती, कौथिग्यार*
     - **Traditional Occupations & Crafts**: *अनवाल, घस्यारी, औजी, ढकी, जगरिया, डांगरिया, तामटा, ओढ़, हलिया, घट्ट्या*
     - **Household, Kitchen & Architecture**: *तिबारी, खोली, पाथर, भकार, ओखली, मूसल, सिलबट्टा, जांदो, दातुलि, गागरी, चिमटा, कंडी, चलनी, दीया*
     - **Traditional Cuisine & Condiments**: *काफ़ुली, चैनसूं, झोली, थटवाणी, चुड़कानी, गुटका, बाड़ी, सिंगोरी, पिस्यूं-लूण, भात, जख्या, फरन, गंधरायण, भंगजीरा*
     - **Nature, Weather & Geography**: *बुग्याल, गधेरा, सेरा, ओड्यार, हिंवल, बयार, कुहासा, छरछरा, ढुंगो, माटी, धारो, नौला, गाड़, खड्ड, चोटी, बादल, बिजुली, उज्यालो, अन्हारो*
     - **Fauna & Wildlife**: *घुरल, कस्तूरी-मृग, गुलदार, मोनाल, हिलांस, काकड़, जुँक, गौ, बल्द, भैंसी, बाछो, बाखरो, कुक्कुर, बिलाव, घोड़ो, खच्चर, स्याल, बांदर, काग, चील, उल्लू, तितली, माछी*
     - **Ethnobotanical Trees & Plants**: *बाँझ, मोरू, खर्सू, बुरांश, सिमरू, देवदार, चीड़, कैल, भोजपत्र, पंया, भीमल, खरिक, उतीस, तिमरू, बेल, मालू, ब्रह्मकमल, फेनकमल, जटामांसी, कूट, अतीस, मीठा-बिख, सलामपंजा, कीड़ाजड़ी, काफल, हिसालू, किल्मोड़ा, बेडू, तिमला, कंडाली, लिंगुड़ा, मंडुवा, झंगोरा, मर्सा, उगल, गहत, भट्ट*
     - **Body, Health & Emotions**: *मुंड, खुट्टा, मया, नराई, रिस, औखद, चरण, पसीना, स्वाभिमान*
     - **Numbers, Time & Seasons**: *ब्याली, आजि, काल, रूड़ी, चौमासा, स्यूंंद, एक से सौ तक संख्याएँ, पहिलो, दूसरो, तीसरो*
     - **Modern Technology & Digital**: *चलभाष, संगणक, अंतरजाल, जालस्थल, अनुप्रयोग, कृत्रिम-बुद्धिमत्ता, साइबर-सुरक्षा*
     - **Governance, Law & Public Services**: *पटवारी, प्रधान, कचहरी, दरखास्त, रपट, कानून, आपातकाल*
     - **School & Education**: *स्कूल, पाटी (स्लेट), खड़िया (चाक), कलम, दवात, सिहाई (स्याही), कापी, पोथी (किताब), मास्टरजी, विद्यार्थी, इम्तिहान (परीक्षा), नतीजा, छुट्टी, घंटी, हाजिरी, गृहकार्य, वजीफा (छात्रवृत्ति)*
     - **Government Jobs & Employment**: *सरकारी-नौकरी, भर्ती (रैली), साक्षात्कार (इंटरव्यू), तरक्की (पदोन्नति), बदली (स्थानांतरण), पेंशन, हाकिम (साहब/अफसर), बाबू (क्लर्क), चपरासी (अर्दली)*
     - **Business, Trading & Commerce**: *ब्योपार, दूकानदार, थोक-ब्योपार, फुटकर, पूँजी, मुनाफा, घाटो (नुकसान), मंडी, पर्चा (बिल), रसीद, साझेदारी, उधार, साहूकार (महाजन)*
     - **Job Scams, Corruption & Crime**: *घपलो (घोटाला), पर्चा-लीक (पेपर लीक), घूस (रिश्वत), भ्रष्टाचार, दलाल (बिचौलिया), फर्जी (जाली), धोखो, डाका (डकैती), लूट, चोर, सेंधमारी, जेबकतरा, उगाही, थाना, थानेदार, गिरफ्तारी, हथकड़ी, हवालात, जमानत, बयान (गवाही), सजा, मुजरिम (दोषी), मुकद्दमा (केस)*
     - **Office Supplies & Things**: *नस्ती (फाइल/मिसिल), रजिस्टर, मोहर (सील), लिफाफा, नत्थी (टैगिंग), मेज, कुर्सी*
     - **Home Furniture & Household**: *खाट (चारपाई), पलंग, गद्दा, सिरहाना (तकिया), रजाई, कंबल, चादर, अलमारी, सीसा (दर्पण), बुहारी (झाड़ू), पोछा, बाल्टी, मग्गो, अरगनी (डोरी), संदूक (बक्सा), ताला, कुंजी (चाबी), चटाई, पीढ़ा (पाटा)*
     - **Crockery & Kitchen Utensils**: *थाली, कटोरा, कचौड़ी (कटोरी), गिलास, प्याला (कप), तश्तरी (प्लेट), जग, चमचा, काँटा, चाकू, पतीला (भगोना), कड़ाही, ढक्कन, कद्दूकस, छिलनी, छलनी, चकला, बेलन, मटका (घड़ा), सुराही, डिब्बा (टिफिन), सँड़सी, तवा*
     - **Children: Stages, Movement, Babble & Games**: *लल्ला (शिशु), पालना, लोरी, स्तनपान, घुटन्यूं-चलणु (घुटनों के बल चलना), डगमग-चलणु (डगमगाते कदम), रून-झुन (घुंघरू चाल), तोतलो-बोलणु (तोतली बोली), किलकारी, बिलखणु (सिसकना), मचलणु (बालहठ), चिपकणु (मां से लिपटना), कांख (गोद/कमर), कंचा, स्टापू, लट्टू, पतंग, झूला, कूदणु, छलांग-मारणु, ठोकर-खाणु*
     - **Childhood Life-Cycle Rituals**: *नामकरण (११वें दिन का संस्कार), झडूला (चूड़ाकर्म/मुंडन), अन्नप्राशन (पसनी/खीर चटाना), कर्णवेध (कान छेदन), विद्यारंभ (अक्षरारंभ), नजर-उतारणु (बुरी नजर उतारना)*
     - **Literature & Song Extractions**: *मंडाण, अचरी, जागर, भैलो, छंतोली, पव्वाड़ा, झुमेलो, गूल, भड़, रणसिंघा, भंकोरा, छैला, बांद, बांसुरी, नाद, दीप, डोली, मेढ़ा, सुदिन, सुहाग, शहनाई, छिल्ला, पूड़ी, शगुन, पराक्रम, बलिदान, वास, वंदना, संकट, शरण, कौथिग, डंका, घुंघरू, शिखर, सागर, चिनहार, गदा, बाण, धनुष, अमृत, कमाई, निर्भय, चौंफुला, थड्या, गौंत, गोबर, लीपणा, छींटा, जातरा, धियान, आशीर्वाद, असीस*
4. **🗺️ Sacred Geography & Places of Garhwal (`garhwali.culture.places`)**:
   - Comprehensive catalogue of **48 documented sacred landmarks** across all 7 districts of Garhwal:
     - **Panch Kedar (पंच केदार)**: Kedarnath, Madhyamaheshwar, Tungnath, Rudranath, Kalpeshwar.
     - **Panch Badri (पंच बद्री)**: Badrinath, Adi Badri, Bhavishya Badri, Vriddha Badri, Dhyan Badri.
     - **Panch Prayag (पंच प्रयाग)**: Devprayag, Rudraprayag, Karnaprayag, Nandaprayag, Vishnuprayag.
     - **High Alpine Bugyals**: Auli, Chopta, Dayara, Bedni.
     - **Historic Towns & Cultural Centers**: Srinagar Garhwal, Joshimath, Gopeshwar, Pauri, Uttarkashi, Ukhimath, Guptkashi, Rishikesh, Haridwar, Khirsu.
     - **Sacred Mountains & Shrines**: Surkanda Devi, Chandrabadani, Kunjapuri, Dhari Devi, Triyuginarayan, Khait Parvat, Hanol Mahasu.
5. **🙏 Local Deities, Shrines & Jagar Lore (`garhwali.culture.deities`)**:
   - Structured records of **18 canonical Garhwali deities**:
     - *Dhari Devi, Botha Mahasu, Chalda Mahasu, Sem Mukhem Nagaraja, Danda Nagaraja, Nanda Devi, Latu Devta, Kandoliya Devta, Surkanda Devi, Chandrabadani Devi, Kunjapuri Devi, Jwalpa Devi, Ghandiyal Devta, Bhumyal Devta (Kshetrapal), Bhairav Devta, Aanchhariyan (Alpine Fairies), Guru Gorakhnath, Pandav Devtas*.
     - Contains iconographies, legends, traditional invocations (जागर बोल), and cultural significance.
6. **👥 Garhwali Surnames, Clans & Social Concepts (`garhwali.culture.surnames`)**:
   - Comprehensive cataloguing of **24 documented heritage lineages**:
     - **Brahmin Clans**: *Khanduri, Nautiyal, Bahuguna, Gairola, Uniyal, Semwal, Dimri, Bhatt, Thapliyal, Raturi, Dhasmana, Chamoli*.
     - **Rajput / Kshatriya Clans**: *Panwar, Negi, Rawat, Bisht, Bhandari, Chauhan, Bartwal, Gusain, Aswal, Kathait, Sajwan, Kaintura, Rana*.
     - **Alpine Transhumant Communities**: *Marchha, Tolchha, Jadh*.
     - **Shilpkar & Artisan Lineages**: *Auji / Das, Tamta, Dhaki, Beda, Lohar*.
     - **Garhwali Social Concepts**: *Thokdaar, Gauntyaar / Sayana, Bhad (वीर भड़), Jagariya, Dangariya, Dhol Sagar, Beda-Vart, Jaiti, Dhandak*.
7. **🌿 Himalayan Ethnobotanical Flora (`garhwali.culture.flora`)**:
   - Master catalogue of **30+ indigenous trees, alpine herbs, wild fruits, and crops** of Garhwal:
     - Botanical families, habitat altitudes, traditional uses, temple offerings, and cultural folklore.
8. **🪔 Temple Implements, Vessels & Ritual Objects (`garhwali.culture.rituals`)**:
   - Catalogue of **24 sacred implements, vessels, hawan paraphernalia, and attire**:
     - *Pithya, Akshat, Dhago/Kalawa, Janyo, Tamakundi, Dhoopdani, Panchaarti, Shankh, Garud-Ghanti, Havan Kund, Sruva & Sruk, Samidha, Doli, Chhantoli, Chaunr, Nishan, Dhol, Damau, Ransingha, Bhankora, Kansya Thali, Tehri Nath, Guloband, Hansuli, Dhagula, Rot, Arsa, Malu Pattal & Duna*.
9. **🎶 Complete Folk Songs Corpus & Digital Archives (`garhwali.culture.folklore`)**:
   - **20 Complete Authenticated Garhwali Songs** saved as full text in `data_sources/raw_texts/songs/` and catalogued in `songs.json`:
     - *Bedu Pako Baramasa, Chaita Ki Chaitwali, Thando Re Thando Mera Pahada Ko Paani, Ghughuti Na Baas Mait Ki, Dhari Devi Jagar, Nanda Raj Jat, Mangal Geet, Igas Bagwal, Phooldei Chham Chham, Maletha Ki Gool (Madho Singh Bhandari), Jeetu Bagdwal, Surkanda Mata Vandana, Saruli Meru Jiya Lagi, Hilaans Pakhi, Chhori Garhwali, Jai Badrinath Kedarnath, Tehri Doobon, Buransh Phooli Ge, Pandav Nritya Mandaan, Kodu Jhangora Khani*.
   - **7 Active Digital Heritage Archives** indexed in `digital_sources.json`.
10. **📚 Master Garhwali Bibliography & Literature (`garhwali.culture.bibliography` & `literature`)**:
    - **80+ Canonical Books Catalogued** across works written in Garhwali, grammar/linguistics treatises, and cultural studies.
    - **6 Classical Folk Epics (पवाड़े)**, **4 Canonical Poems**, and **10 Distinguished Authors**.
11. **📖 13 Complete Full-Text Digital Books & Page Reader (`garhwali.culture.books`)**:
    - **3,070+ Complete Digitized Pages** available page-by-page directly in Python:
      - *Sir George Grierson (1916)*: Linguistic Survey of India (Central Pahari / Garhwali) — 977 pages
      - *Pandit Ganga Datt Upreti (1894)*: Proverbs & Folklore of Kumaun and Garhwal — 398 pages
      - *Rev. E.S. Oakley & Tara Dutt Gairola (1935)*: Himalayan Folklore — 313 pages
      - *Dr. Govind Chatak (1959)*: Garhwali Bhasha (Linguistic & Grammatical Study) — 102 pages
      - *Dr. Govind Chatak (1958)*: Gadwali Lok Gathayen (Pawada & Jagar Epics) — 114 pages
      - *Dr. Haridatta Bhatt 'Shailesh' (1976)*: Garhwali Bhasha Aur Uska Sahitya — 301 pages
      - *Dr. Gunanand Juyal (1967)*: Madhya Pahadi Bhasha (Garhwali-Kumauni) — 161 pages
      - *Shanti Chaudhary (1994)*: Garhwali Lokkala Aur Loksahitya — 231 pages
      - *Shyam Chand Negi (1954)*: Gadwali Sahitya Ki Bhumika — 46 pages
      - *Uttarakhand Open University*: CGL-102 (Prose), CGL-103 (Poetry), CGL-104 (Grammar), AECC-G-101 (General Studies) — 433 pages
    - Full search API across all 3,070+ pages with text snippets, keywords, and chapter detection.
12. **⚖️ Split-Ergativity & SOV Syntax Validator (`garhwali.grammar.syntax`)**:
    - Enforces authentic Central Pahari ergative case markings (`-न / -ले` in transitive perfective clauses).
13. **🔢 Garhwali Numbers Engine (`garhwali.numbers`)**:
    - Converts any integer (0 to 1 crore) into Garhwali words, ordinals, and Devanagari numerals.
14. **🎙️ Voice Synthesis & SSML (`garhwali.voice`)**:
    - Himalayan pitch envelope generator, SSML formatter, and uncompressed PCM WAV synthesis.

---

## 🚀 Installation & Quick Start

```bash
pip install garhwali
```

### 💻 Python Usage Examples

```python
import garhwali

# ==================== 1. SACRED GEOGRAPHY & PLACES ====================
print(f"Total documented places: {len(garhwali.PlacesTreasury.list())}")

# Panch Kedar
for kedar in garhwali.PlacesTreasury.panch_kedar():
    print(f"- {kedar.name_garhwali} ({kedar.district}): {kedar.title}")

# Panch Badri & Panch Prayag
badris = garhwali.PlacesTreasury.panch_badri()
prayags = garhwali.PlacesTreasury.panch_prayag()

# Lookup specific place
dhari = garhwali.PlacesTreasury.get("dhari_devi")
print(dhari.spiritual_or_historical_significance)

# ==================== 2. LOCAL DEITIES & SHRINES ====================
deity = garhwali.DeitiesTreasury.get("botha_mahasu")
print(deity.name_garhwali)  # "बोथा महासू"
print(deity.invocation_or_jagar)

# ==================== 3. SURNAMES & SOCIAL STRUCTURE ====================
bhandari = garhwali.SurnamesTreasury.get("bhandari")
print(bhandari.title)  # "Hereditary Royal Treasurers & Legendary Heroic Warriors (Bhad)"
print(bhandari.notable_historical_figures)

# Garhwali social concepts
concepts = garhwali.SurnamesTreasury.social_concepts()
print(concepts["bhad"]["meaning_english"])  # "Legendary Epic Warrior / Champion Hero"

# ==================== 4. HIMALAYAN FLORA & ETHNOBOTANY ====================
buransh = garhwali.FloraTreasury.get("buransh")
print(buransh.scientific_name)  # "Rhododendron arboreum"
print(buransh.cultural_folklore)

# ==================== 5. TEMPLE IMPLEMENTS & RITUALS ====================
dhol = garhwali.RitualsTreasury.get("dhol")
print(dhol.sacred_purpose)
print(dhol.cultural_context)

# ==================== 6. COMPLETE SONGS CORPUS ====================
song = garhwali.FolkloreTreasury.get_song("GSN-0001")
print(song.title)  # "बेडू पाको बारामासा"
for verse in song.verses:
    print(f"  {verse}")

# Digital archive repositories
archives = garhwali.FolkloreTreasury.list_sources()
print(f"Active preservation repositories: {len(archives)}")

# ==================== 7. VOCABULARY & DICTIONARY ====================
word = garhwali.lookup("काफ़ुली")
print(word)
# {'garhwali': 'काफ़ुली', 'hindi': 'काफ़ुली (पालक-मेथी का गाढ़ा साग)', 'category': 'food', ...}

# ==================== 8. BIBLIOGRAPHY & LITERATURE ====================
chatak_books = garhwali.search_books("चातक")
for b in chatak_books:
    print(f"- {b.title} ({b.year}) by {b.author}")

# ==================== 9. FULL-TEXT BOOKS & PAGE-BY-PAGE READER ====================
print(f"Total digitized pages in library: {garhwali.BooksCorpus.total_pages_in_library()}")

# Read page 15 of Grierson's 1916 Linguistic Survey of India
page = garhwali.read_book_page("grierson_1916_central_pahari", 15)
print(f"Page {page.page_number}:\n{page.snippet(max_chars=300)}")

# Search across all 13 digitised books
results = garhwali.search_digital_books("माधो सिंह भण्डारी")
for r in results[:3]:
    print(f"[{r.book_title} - Page {r.page_number}]: {r.snippet}")

# ==================== 10. COMPUTATIONAL CORPUS & NLP FRAMEWORK ====================
# 20-Pillar Computational Taxonomy
taxonomy = garhwali.get_corpus_taxonomy()
print(f"Total Computational Pillars: {len(taxonomy.list_pillars())}")
pillar_novel = taxonomy.get_pillar("novels")
print(f"Pillar 1: {pillar_novel.name_garhwali} - {pillar_novel.description}")

# Annotated Sentence Corpus (Tokens, UPOS, Morphology, Translations, Citations)
sents = garhwali.get_sentence_corpus().all()
print(f"Total Annotated Sentences: {len(sents)}")
s1 = garhwali.get_annotated_sentence("sent_001")
print(f"Text: {s1.text}")
print(f"Tokens: {s1.tokens}")
print(f"UPOS: {s1.pos}")
print(f"Hindi: {s1.translation_hi}")
print(f"English: {s1.translation_en}")

# Split for Model Training / Evaluation (Train / Val / Test)
splits = garhwali.SentenceCorpus.train_test_split(train_ratio=0.8, val_ratio=0.1, test_ratio=0.1)
print(f"Train: {len(splits['train'])}, Val: {len(splits['validation'])}, Test: {len(splits['test'])}")

# Comprehensive Idioms & Proverbs Corpus (10-Field Schema)
idioms = garhwali.get_idiom_corpus()
sample_idiom = idioms.get("idh_001")
print(f"Idiom: {sample_idiom.idiom} ({sample_idiom.transliteration})")
print(f"Figurative: {sample_idiom.figurative_meaning}")
print(f"Hindi Equivalent: {sample_idiom.hindi_equivalent}")
print(f"English Gloss: {sample_idiom.english_gloss}")
print(f"Example: {sample_idiom.example_sentence}")

# ==================== 11. MULTI-DIALECT TRANSLATION ====================
res = garhwali.translate("Where are you from?", dialect="tehri")
print(res.text)  # "तुमु कथी बटी छा?"
```

---

## 🧪 Testing

The library includes a comprehensive unit test suite covering all modules:

```bash
python -m unittest discover -s tests -v
```

All 86 unit tests pass with 100% success across:
- `test_garhwali_core.py` (Version, exports, top-level APIs)
- `test_garhwali_corpus.py` (20-pillar taxonomy, annotated sentence corpus, UPOS tags, train/val/test splits, idioms & proverbs, strict bibliography separation)
- `test_garhwali_books.py` (Full-text digital books, 3,076 pages, page-by-page reader API)
- `test_garhwali_lexicon.py` (Dictionary lookup, search, 27 categories, dialect variants)
- `test_garhwali_grammar.py` (Morphology engine, noun declensions, verb conjugations, syntax)
- `test_garhwali_translator.py` (Multi-dialect translations, rule engine)
- `test_garhwali_culture.py` (Bibliography treasury, folk epics, canonical authors, poems)
- `test_garhwali_places.py` (Panch Kedar, Panch Badri, Panch Prayag, districts, search)
- `test_garhwali_deities.py` (Deity categories, invocations, shrines, search)
- `test_garhwali_surnames.py` (Clans, gotras, historical figures, social concepts)
- `test_garhwali_flora.py` (Ethnobotany, scientific names, habitats, cultural lore)
- `test_garhwali_rituals.py` (Ritual items, implements, vessels, sacred attire)
- `test_garhwali_folklore.py` (Folk songs, verses, translation, digital sources)

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
