# -*- coding: utf-8 -*-
"""
Synchronizes all project documentation, README, and LLM context files
with the Wave 11 verified statistics:
- Lexicon: 3,619 words across 92 categories
- Inflected word forms: 2,605,200+
- Digital Books: 86 complete books (23,856 pages)
- Catalogued Bibliography: 231 works
- Formal Grammar Rules: 81 rules across 8 categories (178 annotated examples)
- Unit Tests: 101 tests passing
"""

import os
import re

def sync_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")

    content = re.sub(r"3\. \*\*📖 [\d,]+\+ Verified Lexical Lemmas", "3. **📖 3,619+ Verified Lexical Lemmas", content)
    content = re.sub(r"10\. \*\*📚 Master Garhwali Bibliography & Literature \(`garhwali\.culture\.bibliography` & `literature`\)\*\*:\s+- \*\*[\d,]+\+? Canonical Books Catalogued\*\*", "10. **📚 Master Garhwali Bibliography & Literature (`garhwali.culture.bibliography` & `literature`)**:\n    - **231 Canonical Books Catalogued**", content)

    # Replace book list section
    start_str = "11. **📖 "
    end_str = "12. **⚖️ Split-Ergativity"
    start_pos = content.find(start_str)
    end_pos = content.find(end_str)

    if start_pos != -1 and end_pos != -1:
        replacement = """11. **📖 86 Complete Full-Text Digital Books & Page Reader (`garhwali.culture.books`)**:
    - **23,856 Complete Digitized Pages** available page-by-page directly in Python:
      - *Sir George Grierson (1916)*: Linguistic Survey of India (Central Pahari / Garhwali) — 977 pages
      - *Pandit Ganga Datt Upreti (1894)*: Proverbs & Folklore of Kumaun and Garhwal — 398 pages
      - *Rev. E.S. Oakley & Tara Dutt Gairola (1935)*: Himalayan Folklore — 313 pages
      - *Dr. Govind Chatak (1959)*: Garhwali Bhasha (Linguistic & Grammatical Study) — 102 pages
      - *Dr. Govind Chatak (1958)*: Gadwali Lok Gathayen (Pawada & Jagar Epics) — 114 pages
      - *Dr. Haridatta Bhatt 'Shailesh' (1976)*: Garhwali Bhasha Aur Uska Sahitya — 128 pages
      - *Dr. Gunanand Juyal (1967)*: Madhya Pahadi Bhasha (Central Pahari Phonology & Morphology) — 117 pages
      - *Shyam Chand Negi (1954)*: Gadwali Sahitya (Anthology & Critical History) — 151 pages
      - *Pt. Govind Prasad Ghildyal (1928)*: Garhwali Bhasha Aur Uska Vyakaran — 84 pages
      - *Pt. Hari Krishna Raturi (1928)*: Garhwal Ka Itihas (Ancient Inscriptions & Clans) — 381 pages
      - *Pt. Ganga Datt Upreti (1894)*: Proverbs & Folklore (Extended Edition) — 398 pages
      - *Dr. Govind Chatak (1956)*: Garhwali Lok Geet (Folk Songs of Garhwal) — 114 pages
      - *Shanti Chaudhary (1994)*: Garhwali Lokkala (Aipan, Murals & Ritual Arts) — 110 pages
      - *Edwin T. Atkinson (1882)*: The Himalayan Districts of the North-Western Provinces (Vol. 1) — 955 pages
      - *Edwin T. Atkinson (1884)*: The Himalayan Districts of the North-Western Provinces (Vol. 2) — 1,389 pages
      - *Edwin T. Atkinson (1883)*: Notes on the History of the Himalayan Districts — 684 pages
      - *Dr. Shiv Prasad Dabral 'Charan' (1961)*: Shri Uttarakhand Yatra Darshan — 451 pages
      - *Dr. Shiv Prasad Dabral 'Charan' (1971)*: Uttarakhand Ka Itihas (Bhag 1: Pragaithihasik Kaal) — 596 pages
      - *Dr. Shiv Prasad Dabral 'Charan' (1973)*: Uttarakhand Ka Itihas (Bhag 3: Garhwal Ka Naveen Itihas) — 624 pages
      - *E. K. Pauw (1896)*: Report on the Tenth Settlement of the Garhwal District — 662 pages
      - *H. G. Walton (1910)*: British Garhwal: A Gazetteer — 347 pages
      - *Pati Ram (1916)*: Garhwal: Ancient and Modern — 363 pages
      - *Rev. T. Grahame Bailey (1908)*: The Languages of the Northern Himalayas — 285 pages
      - *Rev. T. Grahame Bailey (1915)*: Linguistic Studies from the Himalayas — 267 pages
      - *L. D. Joshi (1929)*: The Khasa Family Law in the Himalayan Districts — 434 pages
      - *Mukandi Lal (1968)*: Garhwal Painting (Mola Ram & Garhwali School of Art) — 128 pages
      - *Dr. Siddheshwar Verma (1978)*: Pahari Language: A Linguistic Analysis — 97 pages
      - *Central Hindi Directorate (1989)*: Pahari-Hindi Shabdkosh — 123 pages
      - *George William Traill (1828)*: Statistical Sketch of Kumaon and Garhwal — 680 pages
      - *Pandit Ganga Datt Upreti (1900)*: Hill Dialects of the Kumaun Division (Central Pahari) — 119 pages
      - *H. G. Walton (1911)*: Dehra Dun: A Gazetteer (Vol. 1) — 441 pages
      - *Dr. Siddheshwar Verma (2004)*: Pahari Dictionary of 27 North-Western Himalayan Dialects — 395 pages
      - *Indian Institute of Advanced Study (2002)*: Pahari Bhasha Tatha Sahitya — 210 pages
      - *Dr. Shiv Prasad Dabral 'Charan' (1965)*: Uttarakhand Ke Bhotantik: Alaknanda Upatyaka Mein Pravas (Bhag 2) — 177 pages
      - *Edwin T. Atkinson (1886)*: The Himalayan Districts of the North-Western Provinces (Vol. 3) — 899 pages
      - *V. A. Stowell (1916)*: Kumaun Rulings for Civil Courts (Customary Law) — 185 pages
      - *Government of North-Western Provinces (1842)*: Historical Papers Relating to Kumaun and Garhwal 1809-1842 — 307 pages
      - *Rev. E. S. Oakley & Tara Dutt Gairola (1935)*: Himalayan Folklore (Extended Archival Edition) — 313 pages
      - *Dr. Siddheshwar Verma (2003)*: Dr. Siddheshwar Varma's Pahari Dictionary (Vol. 1) — 372 pages
      - *Imperial Gazetteer of India (1905)*: Imperial Gazetteer of India: Kumaun Division (Garhwal) — 69 pages
      - *A. L. Mumm (1909)*: Five Months in the Himalaya: Mountain Travel in Garhwal — 211 pages
      - *Government of United Provinces (1919)*: Kumaun and Garhwal: Local Customs and Usages — 105 pages
      - *Dr. Siddheshwar Verma (2003)*: Dr. Siddheshwar Varma's Pahari Dictionary (Part 3) — 270 pages
      - *Rev. E. S. Oakley (1920)*: Himalayan Folklore: Legends and Traditions of Kumaon and Garhwal — 269 pages
      - *T. R. Joshi (1911)*: Dictionary of Pahari Dialects of the Western and Central Himalayas — 154 pages
      - *Gypsy Davy and Lady Ba (1927)*: The Himalayan Letters of Gypsy Davy and Lady Ba (Garhwal Pilgrimage) — 319 pages
      - *Charles A. Sherring (1906)*: Western Tibet and the British Borderland: Garhwal and Bhotia Customs — 304 pages
      - *J. H. Batten (1851)*: Official Reports on the Province of Kumaon and Garhwal — 620 pages
      - *Dr. Harshwanti Bisht (1994)*: Tourism in Garhwal Himalaya: Pilgrimage, Culture and Economy — 215 pages
      - *Garhwal Exploration Society (1986)*: Peaks and Passes of the Garhwal Himalaya — 161 pages
      - *H. P. Bhatt et al. (1992)*: Garhwal Himalaya: Nature, Culture and Society — 143 pages
      - *Dr. Siddheshwar Varma (2003)*: Dr. Siddheshwar Varma's Pahari Dictionary of 27 Dialects (Part 2) — 72 pages
      - *Language Division, Govt. of India (2023)*: Linguistic Survey of India: Pahari Dialects — 596 pages
      - *Dr. Omkareshwor Shrestha (2000)*: A Grammar of Pahari: Phonology, Morphology and Syntax — 217 pages
      - *Todd Lewis (1995)*: The Himalayas: History, Anthropology, and Religion — 140 pages
      - *André Roch (1947)*: Garhwal Himalaya: Mountain Expeditions and High Passes — 131 pages
      - *BVP Research Collection (1998)*: Himachali and Pahari Shabdawali — 25 pages
      - *J. B. Auden (1936)*: The Structure of the Himalaya in Garhwal — 38 pages
      - *Sir George Grierson (1916)*: LSI Pahari Languages and Gujuri (IGNCA Edition) — 770 pages
      - *Forest Department (1897)*: Working Plan of the Tehri-Garhwal Leased Forests — 186 pages
      - *Iqbal Nazish (1995)*: Chalyaan Suraan: Pahari Rhythms, Songs and Verses — 57 pages
      - *N. S. Bhandari et al. (1946)*: Snow Balls of Garhwal: Folk Songs and Ballads — 50 pages
      - *Himalayan Natural History Society (1969)*: Birds and Natural History of Lower Garhwal — 38 pages
      - *A. W. Ibbotson (1933)*: Eleventh Revenue Settlement of Garhwal District — 26 pages
      - *Frank S. Smythe (1932)*: Kamet Conquered: Exploration in the Garhwal Himalaya and the Valley of Flowers — 378 pages
      - *Pt. Hariram Sharma (1938)*: Badrinath-Kedarnath Yatra: Holy Pilgrimage in the Garhwal Himalayas — 91 pages
      - *Frank S. Smythe (1932)*: Explorations in Garhwal around Kamet (Geographical Journal) — 31 pages
      - *Dr. Mohammad Ishaq Khan (1978)*: History of Srinagar: Socio-Cultural Change in the Central and Northern Himalayas — 319 pages
      - *Parvez Maanoos (2020)*: Parbaton Ki Khushbu: Selected Pahari Mountain Tales, Folklore and Idioms — 57 pages
      - *Swami Sivananda (1966)*: Himalayan Forest Hermitage: Health, Nature and Sacred Living in Garhwal — 183 pages
      - *Swami Prabodhanand (1961)*: Across Gangotri Glaciers: Explorations in Northern Garhwal — 50 pages
      - *Shiv Kumar Painuli et al. (2000)*: Shri Nanda Devi Raj Jat: The Royal Himalayan Pilgrimage of Garhwal — 23 pages
      - *Eric Shipton (1936)*: Nanda Devi: Exploration of the Great Himalayan Sanctuary — 235 pages
      - *Eric Shipton (1935)*: Nanda Devi and the Ganges Watershed: Mountain Topography of Garhwal — 33 pages
      - *Zoological Survey of India (1997)*: Fauna of Nanda Devi Biosphere Reserve: Wildlife and Avifauna — 116 pages
      - *K. S. Negi et al. (1985)*: Flora of Khatling Glacier in the Garhwal Himalaya (District Tehri) — 19 pages
      - *H. G. Ross (1874)*: Settlement of Pargana Jaunsar-Bawar: Customary Law and Land Tenure — 114 pages
      - *Dr. D. N. Majumdar (1960)*: Himalayan Polyandry: Kinship, Culture and Social Structure in Jaunsar-Bawar — 538 pages
      - *G. F. Hearth (1889)*: Working Plan of the Deoban Range, Jaunsar Forest Division — 391 pages
      - *Pt. Devendranath Sharma (1955)*: Himtirth Badrinath: The Holy Himalayan Sanctum and Sacred Geography — 39 pages
      - *H. W. Tilman (1937)*: The Ascent of Nanda Devi: First Historic Ascent of the Sanctuary Peak — 232 pages
      - *J. J. Languepin (1956)*: To Kiss High Heaven: Nanda Devi and Trishul Himalayan Expeditions — 176 pages
    - Full search API across all 23,856 pages with text snippets, keywords, and chapter detection.
"""
        content = content[:start_pos] + replacement + content[end_pos:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("README.md synced successfully.")

def sync_documentation():
    with open("DOCUMENTATION.md", "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")

    content = re.sub(r"archive of \d+ historical books \([\d,]+ pages\)", "archive of 86 historical books (23,856 pages)", content)
    content = re.sub(r"Read Digitized Canonical Books \([\d,]+ pages\)", "Read Digitized Canonical Books (23,856 pages)", content)
    content = re.sub(r"[\d,]+ rich dictionary entries", "3,619 rich dictionary entries", content)
    content = re.sub(r"across all [\d,]+ words and \d+ categories", "across all 3,619 words and 92 categories", content)
    content = re.sub(r"[\d,]+-page historical book reader", "23,856-page historical book reader", content)
    content = re.sub(r"\*\*Master Bibliography:\*\* \d+ canonical works", "**Master Bibliography:** 231 canonical works", content)
    content = re.sub(r"\*\*Digitized Books Corpus:\*\* \d+ complete books digitized across \*\*[\d,]+ pages\*\*", "**Digitized Books Corpus:** 86 complete books digitized across **23,856 pages**", content)
    content = re.sub(r"\*\*Formal Rules Registry \(`RuleRegistry`\):\*\* \d+ comprehensive grammatical rules across all \d+ linguistic categories", "**Formal Rules Registry (`RuleRegistry`):** 81 comprehensive grammatical rules across all 8 linguistic categories", content)

    # Add Wave 11 citations
    wave11_citations = """75. **H. G. Ross (1874):** *Settlement of Pargana Jaunsar-Bawar: Customary Law and Land Tenure*, Government Press, Allahabad.
76. **Dr. D. N. Majumdar (1960):** *Himalayan Polyandry: Structure, Functioning and Culture Change in Jaunsar-Bawar*, Asia Publishing House, Bombay & London.
77. **G. F. Hearth / Forest Department (1889):** *Working Plan of the Deoban Range, Jaunsar Forest Division (N.-W. Provinces)*, Government Press, Allahabad.
78. **Pt. Devendranath Sharma (1955):** *Himtirth Badrinath: The Holy Himalayan Sanctum and Sacred Geography*, Shri Badrinath Kedar Temple Committee, Chamoli.
79. **H. W. Tilman (1937):** *The Ascent of Nanda Devi: First Historic Ascent of the Sanctuary Peak*, Cambridge University Press, Cambridge.
80. **J. J. Languepin (1956):** *To Kiss High Heaven: Nanda Devi and Trishul Himalayan Expeditions*, William Kimber & Co. Ltd., London.
"""
    if "75. **H. G. Ross" not in content:
        content = content.replace("74. **K. S. Negi, J. K. Tiwari & R. D. Gaur (1985):** *Flora of Khatling Glacier in the Garhwal Himalaya (District Tehri)*, Journal BNHS / HNB Garhwal University Srinagar.\n", "74. **K. S. Negi, J. K. Tiwari & R. D. Gaur (1985):** *Flora of Khatling Glacier in the Garhwal Himalaya (District Tehri)*, Journal BNHS / HNB Garhwal University Srinagar.\n" + wave11_citations)

    with open("DOCUMENTATION.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("DOCUMENTATION.md synced successfully.")

def sync_llm_context():
    with open("garhwali_llm_context.xml", "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")

    content = re.sub(r"# 7\. Digitized Historical Books \(\d+ books, [\d,]+ pages\)", "# 7. Digitized Historical Books (86 books, 23,856 pages)", content)
    content = re.sub(r"Master digital library \(\d+ books, [\d,]+ pages\), \d+ complete folk songs, \d+ classical Holi songs, \d+ sacred shrines, \d+ catalogued bibliography records", "Master digital library (86 books, 23,856 pages), 45 complete folk songs, 20 classical Holi songs, 48 sacred shrines, 231 catalogued bibliography records", content)
    content = re.sub(r'Look up words in the [\d,]+-entry lexicon', 'Look up words in the 3,619-entry lexicon', content)

    with open("garhwali_llm_context.xml", "w", encoding="utf-8") as f:
        f.write(content)
    print("garhwali_llm_context.xml synced successfully.")

def sync_books_py():
    with open("garhwali/culture/books.py", "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")

    header_replacement = '''# -*- coding: utf-8 -*-
"""
Full-Text Digital Book Corpus and Page-by-Page Reader for Garhwali Language.

Provides access to 86 complete digitised historical, linguistic, and literary books
comprising 23,856 pages of authentic Garhwali texts, grammars, folk epics,
gazetteers, and linguistic surveys.
"""'''
    import_idx = content.find("import json")
    if import_idx != -1:
        content = header_replacement + "\n\n" + content[import_idx:]
        with open("garhwali/culture/books.py", "w", encoding="utf-8") as f:
            f.write(content)
        print("garhwali/culture/books.py synced successfully.")

def sync_data_sources_readme():
    with open("data_sources/README.md", "r", encoding="utf-8") as f:
        content = f.read().replace("\r\n", "\n")

    wave11_rows = """| 81 | **Settlement of Pargana Jaunsar-Bawar** | H. G. Ross | 1874 | `dli.pahar.0789` | 209 KB text (114 pages) | Dastur-ul-Amal Customary Law, Khat System, Sayana Elders, Village Commons |
| 82 | **Himalayan Polyandry (Jaunsar-Bawar)** | Dr. D. N. Majumdar | 1960 | `dli.pahar.3163` | 973 KB text (538 pages) | Kinship Terminology (Jodidar, Dhyanti, Rainti), Mahasu Devta Cult, Bissu Archery |
| 83 | **Deoban Range Forest Working Plan** | G. F. Hearth | 1889 | `wbsl.14555` | 764 KB text (391 pages) | Native Conifers (Rai Spruce, Deodar), Timber Flumes, Grazing Commons (Dhab) |
| 84 | **Himtirth Badrinath Sanctum Treatise** | Pt. Devendranath Sharma | 1955 | `in.ernet.dli.2015.452383` | 195 KB text (39 pages) | Panch Badri (Yogdhyan, Bhavishya, Vridha, Adi Badri), Mana Caves (Vyas, Ganesh) |
| 85 | **The Ascent of Nanda Devi** | H. W. Tilman | 1937 | `in.ernet.dli.2015.79797` | 440 KB text (232 pages) | Historic First Ascent (25,645 ft), Rishi Gorge, Alpine Ridge Climbing, Porter Lore |
| 86 | **To Kiss High Heaven: Nanda Devi & Trishul** | J. J. Languepin | 1956 | `languepin-1956...` | 343 KB text (176 pages) | High Glacial Bivouacs, Spindrift Blizzards, Mountain Waystations, Porter Routes |
"""
    if "| 81 |" not in content:
        target = "| 80 | **Flora of Khatling Glacier (Tehri Garhwal)** | K. S. Negi, J. K. Tiwari, R. D. Gaur | 1985 | `biostor-153424` | 39 KB text (19 pages) | Bhilangna Headwaters, Alpine Medicinal Plants (Jambu, Gandrani, Dolu, Salampanja) |\n"
        content = content.replace(target, target + wave11_rows)

    with open("data_sources/README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("data_sources/README.md synced successfully.")

if __name__ == "__main__":
    sync_readme()
    sync_documentation()
    sync_llm_context()
    sync_books_py()
    sync_data_sources_readme()
