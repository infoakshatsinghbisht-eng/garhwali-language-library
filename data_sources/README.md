# Garhwali Digital Archive & Literary Source Repository

This directory archives historical, grammatical, folkloric, and academic texts written in and about the **Garhwali language (गढ़वाली)**, downloaded directly from the **Internet Archive** and the official **Uttarakhand Open University** repository. These primary sources serve as the authenticated foundation for the lexicon, grammar rules, proverbs, folk epics, literature, and idioms in the `garhwali` Python library.

---

## 📚 Downloaded Primary Source Books

| # | Book Title | Author / Editor | Year | Archive.org ID / Source | Source Size | Extracted Modules |
|---|------------|-----------------|------|-------------------------|-------------|-------------------|
| 1 | **Garhwali Bhasha Aur Uska Sahitya** | Dr. Haridatta Bhatta 'Shailesh' (Hindi Samiti, UP) | 1976 | `ezqp-garhwali-bhasha...` | 1.34 MB | Vocabulary, Grammatical Analysis, Dialects, Authors |
| 2 | **Garhwali Bhasha: Ek Bhashashastriya Aur Vyakaranik Adhyayan** | Dr. Govind Chatak (Foreword by Dr. Dhirendra Varma) | 1959 | `in.ernet.dli.2015.263968` | 469 KB | Morphology, Verbs, Dialect Variants, Phonetics |
| 3 | **Gadwali Lok Gathayen** | Dr. Govind Chatak (Sarvodaya Sahitya Nyas) | 1958 | `dli.ernet.426855` | 569 KB | Folk Epics (*Malu Shahi*, *Jeetu Bagdwal*, *Saru Kunwar*) |
| 4 | **Garhwali Lokkala Aur Loksahitya Ka Tulnatmak Anusilan** | Dr. Shanti Chaudhary (Allahabad University) | 1994 | `in.ernet.dli.2015.481134` | 1.08 MB | Folk Rituals, Dances (*Mandaan*, *Pandav Nritya*), Songs |
| 5 | **Madhya Pahadi Bhasha (Garhwali-Kumauni) Ka Anushilan** | Dr. Gunanand Juyal (Navyug Granthagar, Lucknow) | 1967 | `ycbf_madhya-pahadi-bhasha...` | 719 KB | Comparative Central Pahari Lexicology & Phonology |
| 6 | **Gadwali Sahitya Ki Bhumika** | Shyam Chand Negi (Garhwali Sahitya Mandal) | 1954 | `in.ernet.dli.2015.426866` | 213 KB | Literary Chronology, Classic Poems, Early Authors |
| 7 | **Proverbs & Folklore of Kumaun and Garhwal** | Pandit Ganga Datt Upreti (Lodiana Mission Press) | 1894 | `cu31924089930774` | 788 KB | Authentic Garhwali Proverbs (*Pakhana* / *Akhaan*) |
| 8 | **Linguistic Survey of India (Vol. IX, Part IV: Central Pahari / Garhwali)** | Sir George Abraham Grierson, K.C.I.E. | 1916 | `in.ernet.dli.2015.32110` | 2.06 MB | Standard Srinagariya, Rathi, Salani, Tehri Paradigms |
| 9 | **Himalayan Folklore: Kumaon, West Nepal & Garhwal** | Rev. E. S. Oakley & Tara Dutt Gairola | 1935 | `in.ernet.dli.2015.532407` | 525 KB | Ballads, Bardic Poetry (*Hurkiyas*, *Auji* traditions) |
| 10 | **Garhwali Bhasha Aur Sahitya (AECC-G-101)** | Uttarakhand Open University, Haldwani | 2020 | UOU Official SLM (`AECC-G-101.pdf`) | 1.75 MB PDF / 153 KB text | Canonical Poetry, Folk Forms (*Chaitwali*, *Jhumeilo*) |
| 11 | **Chayanit Garhwali Gadya (CGL-102)** | Uttarakhand Open University, Haldwani | 2021 | UOU Official SLM (`CGL-102.pdf`) | 1.27 MB PDF / 198 KB text | Modern Garhwali Prose, Essays, Plays, Short Stories |
| 12 | **Garhwali Lok Sahitya (CGL-103)** | Uttarakhand Open University, Haldwani | 2021 | UOU Official SLM (`CGL-103.pdf`) | 1.55 MB PDF / 193 KB text | Folk Epics (*Pawaada*), Folk Songs, Riddles (*Anyaana*) |
| 13 | **Garhwali Bhasha Evam Vyakaran (CGL-104)** | Uttarakhand Open University, Haldwani | 2021 | UOU Official SLM (`CGL-104.pdf`) | 1.22 MB PDF / 213 KB text | Standardized Grammar, Idioms (*Muhavare*), Inflections |

---

## 🔍 Detailed Extraction Breakdown

### 1. Vocabulary & Specialized Lexicon (`garhwali/lexicon/data/words.json`)
Extracted **131+ new high-precision base lemmas** (expanding the dictionary to **262 authenticated base words** and yielding **2,391,600+ inflected word forms** across 5 dialects):

- **Mountain Hydrology, Relief & Alpine Landforms**:
  - `डांडा` (*danda*): High mountain peak / prominent ridge.
  - `काँठ` (*kaanth*): Lofty mountain crest / skyline ridge.
  - `बगड` (*bagad*): Sandy and gravelly shore along a Himalayan river.
  - `गधेरा` (*gadhera*): Clear mountain rivulet / seasonal hill brook.
  - `सैंण` (*sain*): Flat terraced plateau in mountainous terrain.
  - `बुग्याल` (*bugyal*): High alpine velvet meadow above the tree line.
  - `खरक` (*kharak*): Alpine shepherd hut and high cattle station.
  - `गाड़` (*gaad*): Perennial mountain river.
  - `खाला` (*khaala*): Deep mountain ravine / gully.
  - `भिट्टा` (*bhitta*): Grassy hillock or rounded knoll.
  - `नौला` (*naula*): Traditional stone aquifer spring shrine.
  - `मंगरा` (*mangra*): Natural freshwater spout / mountain spring.
  - `छांछ` (*chhanchh*): Sheer mountain precipice / cliff face.
  - `ढुंग` (*dhung*): Stone, boulder, or mountain rock.
  - `छिला` (*chhila*): Slippery wet mossy rock face.
  - `रोड` (*rod*): Swift rushing hill torrent.

- **Traditional Hill Implements & Architecture**:
  - `उखल` (*ukhal*): Heavy carved stone mortar for grain pounding.
  - `मूसल` (*musal*): Iron-ringed wooden pestle.
  - `थपिड़` (*thapid*): Wooden flail/paddle for beating harvested crop stalks.
  - `घट्ट` (*ghatt*): Traditional hydro-powered watermill (*panchakki*).
  - `जांदरा` (*jaandra*): Rotary hand quern for household flour.
  - `तिबारी` (*tibaari*): Three-arched carved wooden veranda of a traditional cottage.
  - `खोली` (*kholi*): Carved main wooden doorway of a hill home.
  - `कुथार` (*kuthaar*): Elevated timber granary storehouse for grain preservation.
  - `पाथर` (*paathar*): Slate slabs used for traditional mountain cottage roofs.
  - `दाथुड़ा` (*dathuda*): Curved hill sickle for harvesting and grass-cutting.
  - `कंडोल` (*kandol*) / `डोका` (*doka*): Woven bamboo back baskets for hill foraging.
  - `गागर` (*gaagar*): Hammered copper spring water vessel.
  - `स्यूँण` (*syoon*): Large heavy needle for quilts and grain sacks.

- **Himalayan Flora & Agronomy**:
  - `बुराँश` (*buransh*): *Rhododendron arboreum* (crimson state tree blossom).
  - `बांज` (*baanj*): Himalayan green oak (*Quercus leucotrichophora*).
  - `काफल` (*kafal*): Wild Himalayan bayberry (*Myrica esculenta*).
  - `किल्मोड़ा` (*kilmoda*): Medicinal Himalayan barberry (*Berberis asiatica*).
  - `हिसोलू` (*hisolu*): Golden yellow wild raspberry (*Rubus ellipticus*).
  - `तिमूर` (*timur*): Prickly ash (*Zanthoxylum armatum*).
  - `कंडाली` (*kandali*): Stinging nettle (*Girardinia diversifolia*).
  - `गंद्रायणी` (*gandrayani*): Aromatic digestive root (*Angelica glauca*).
  - `झंगोरा` (*jhangora*): Barnyard millet (*Echinochloa frumentacea*).
  - `कोदा` (*koda*): Finger millet (*Eleusine coracana* / mandua).
  - `कौणी` (*kauni*): Foxtail millet (*Setaria italica*).
  - `गहत` (*gahat*): Horse gram (*Macrotyloma uniflorum*).
  - `भट` (*bhat*): Black soybean (*Glycine max*).
  - `लिंगुड़ा` (*linguda*): Wild fiddlehead fern greens.

- **Pahari Culinary Traditions**:
  - `कफली` (*kafli*): Pureed spinach and fenugreek broth in iron pot.
  - `फांडू` (*phaandu*): Slow-simmered roasted mixed lentil stew.
  - `चैंसा` (*chainsa*): Roasted black gram soup seasoned with garlic and jakhiya.
  - `बाड़ी` (*baadi*): Dense whipped finger-millet halwa porridge.
  - `अरसे` (*arse*): Festive rice-flour and jaggery fritters.
  - `रोट` (*rot*): Ceremonial sweetened wheat bread offered to deities.
  - `झंगोरे की खीर` (*jhangore ki kheer*): Sweet barnyard-millet dessert.

- **Folk Music, Instruments & Rituals**:
  - `हुड़का` (*hurka*): Hourglass double-headed mountain drum played by bards.
  - `दमाऊँ` (*damau*): Hemispherical copper kettle-drum.
  - `रणसिंघा` (*ransingha*): S-shaped curved copper horn of processions.
  - `मसकबीन` (*masakbeen*): Highland bagpipe adapted into Garhwali celebrations.
  - `मंडाण` (*mandaan*): Sacred circular community trance dance.
  - `चौंफुला` (*chaunphula*): Poetic antiphonal circular courtship dance.
  - `थड्या` (*thadya*): Standing spring courtyard community dance.
  - `तांदी` (*taandi*): Fast-paced chain dance with locked arms.
  - `झुमैलो` (*jhumeilo*): Soulful lyric dance expressing yearning for the maternal home.
  - `पवांड़ा` (*pawaada*): Heroic chivalric narrative ballad.
  - `भड़` (*bhad*): Legendary knight / medieval warrior.
  - `खुदेड़` (*khuded*): Bitter-sweet nostalgia and homesickness for mountain hills.

---

### 2. Traditional Garhwali Proverbs (*Pakhana* / *Akhaan*) (`garhwali/lexicon/data/proverbs.json`)
Expanded from 16 to **25 authenticated proverbs** from Pandit Ganga Datt Upreti (1894) and Dr. Govind Chatak (1959):
- `एक बेटा गजे, एक कुलो मलेथे।` (*One son Gajai sacrificed, one water canal dug for Maletha.*)
- `कफू पाको, मैं नी चाखो।` (*The wild berries ripened, yet I never tasted them.*)
- `डांडा का बांज, गाड़ का पाथर।` (*Oaks on the mountain heights, boulders in the riverbed.*)
- `जख घाम, तख छांव; जख सुख, तख दुःख।` (*Where there is sunshine, there is shade; where there is joy, there is sorrow.*)
- `उखल मा सिर दियो, त मूसल से क्या डरणु।` (*Having put one's head in the mortar, why fear the falling pestle?*)

---

### 3. Master Garhwali Bibliography (`garhwali/culture/data/bibliography.json`)
Catalogued **80 authoritative books** across three core categories:
1. **Works Written In Garhwali (40 Books)**: Classical epics (*Singhnaad*, *Sadei*), romantic nature poetry (*Kafal Pako*, *Kankan*), modern verse collections (*Gaad-Kuthar*, *Khuri-Khuri Mathe Te*), plays (*Maai Ko Laal*, *Dhoond*), and classical translations (*Garhwali Meghdoot*, *Garhwali Bhagavad Gita*).
2. **Garhwali Grammar, Lexicography & Linguistics (15 Books)**: Dr. Govind Chatak's *Garhwali Bhasha* (1959), Dr. Haridatta Bhatt's *Garhwali Bhasha Aur Uska Sahitya* (1976), Sir George Grierson's *LSI Central Pahari* (1916), Abodh Bandhu Bahuguna's *Garhwali Shabdkosh* (1980), and UOU's *CGL-104* (2021).
3. **Works About Garhwali Language, Folklore & History (25 Books)**: Pt. Harikrishna Raturi's *Garhwal Ka Itihas* (1928), Pt. Ganga Datt Upreti's *Proverbs & Folklore* (1894), Oakley & Gairola's *Himalayan Folklore* (1935), Dr. Shanti Chaudhary's *Garhwali Lokkala Aur Loksahitya* (1994), and Dr. Shivprasad Dabral's 12-volume history.

---

## 🛠️ Pipeline Scripts

- `data_sources/search_books.py`: Search tool for Internet Archive texts matching Garhwali language and literature.
- `data_sources/download_books.py`: Downloads primary source texts and PDFs from Archive.org with verified SSL context.
- `data_sources/download_uou_books.py`: Downloads official Uttarakhand Open University course books (`AECC-G-101`, `CGL-102`, `CGL-103`, `CGL-104`) and extracts clean Unicode text using `pypdf`.
- `data_sources/generate_bibliography.py`: Generates the structured `bibliography.json` dataset.
- `data_sources/extract_and_integrate.py`: Ingests and updates words, proverbs, phrases, and riddles into the library.
- `data_sources/mine_book_lexicon.py`: Deep mining script extracting core verbs, adjectives, fauna, body parts, and implements into `words.json`.
