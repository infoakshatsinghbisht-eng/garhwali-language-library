# -*- coding: utf-8 -*-
"""
Appends Wave 10 formal grammar rules to garhwali/grammar/rules.py:
1. GARH-NOM-011: Diminutive and Endearment Derivational Morphology via Suffix -उली / -उलो
2. GARH-VRB-018: Completive-Terminative Telic Auxiliary with -छोड़ण (Exhaustive Fulfillment)
3. GARH-SYN-016: Iterative Temporal Reduplication in Adverbial Clauses (चलदा-चलदा, खोजदा-खोजदा)
4. GARH-CONC-006: Attributive Adjective Agreement with Postpositional Case Stems (Oblique Inflection -आ / -ए)
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WAVE10_RULES = '''    GrammarRule(
        rule_id="GARH-NOM-011",
        name="Diminutive and Endearment Derivational Morphology via Suffix -उली / -उलो",
        category=RuleCategory.NOMINAL_MORPHOLOGY,
        rule_statement="Garhwali forms affective diminutives, hypocoristics, and names of small geographical or natural objects by affixing -उली (feminine) or -उलो (masculine) to nominal and adjectival stems (e.g., धार ridge -> धरोली small gentle crest, खाडू ram -> खडौलो young tender lamb, छंतोली ceremonial bamboo parasol, नौनी girl -> नौनउली dear little girl).",
        description="Pervasive in Pahari pastoral folklore and emotional verse: नानी धरोली (little mountain knoll), मैंसुलो (little man / dear fellow), डांडउली (small hillock).",
        pattern="[Noun/Adj_Stem] + [-उली (Fem) / -उलो (Masc)]",
        examples=[
            GrammarExample("खडौलो घास चरणा बाना बग्याल मा ग्ये।", "छोटा मेढ़ा घास चरने के लिए बुग्याल में गया।", "The dear young lamb went into the alpine meadow to graze on grass.", "Diminutive masculine hypocoristic खडौलो from root खाडू"),
            GrammarExample("पहाड़ की धरोली पर नंदा देवी की छंतोली चमकै।", "पहाड़ की छोटी चोटी पर नंदा देवी की पावन छतरी चमक उठी।", "On the small mountain crest, Goddess Nanda's sacred ceremonial parasol shone brightly.", "Feminine diminutive धरोली and ritual diminutive छंतोली")
        ],
        counter_examples=["छोटा मेढ़ा / छोटी धार (Analytical periphrastic Hindi constructions with छोटा without morphological diminutive suffixation)"],
        dialect_variations={
            "srinagariya": "-उली / -उलो",
            "tehri": "-उळी / -उळो",
            "salani": "-उली / -उलो",
            "rathwali": "-उली / -उलो"
        },
        linguistic_citation="Painuli et al. (2000), Shri Nanda Devi Raj Jat; Juyal (1967), Madhya Pahadi Bhasha; Grierson (1916)"
    ),
    GrammarRule(
        rule_id="GARH-VRB-018",
        name="Completive-Terminative Telic Auxiliary with -छोड़ण (Exhaustive Fulfillment)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Telic completed actions that exhaustively finalize a strenuous effort, long mountain journey, or difficult task are marked by the conjunctive stem coupled with the auxiliary verb छोड़ण (literally 'to leave/release'), functioning as a completive-terminative vector (e.g., पहुंचि छोड़ण - to succeed in reaching finally, करि छोड़ण - to finish completely).",
        description="Expresses decisive resolution and completion against high physical obstacles: पार करि छोड़ो (crossed despite immense difficulty), पुजि छोड़िन (arrived finally at the sacred high tarn).",
        pattern="[Verb_Conjunctive_Stem] + [छोड़ण Conjugated]",
        examples=[
            GrammarExample("यात्रियों न दुर्गम बाटो पार करि छोड़ो।", "तीर्थयात्रियों ने दुर्गम रास्ता पार करके ही दम लिया।", "The pilgrims persevered and finally completed crossing the impassable mountain path.", "Telic completive aspect करि छोड़ो with ergative subject"),
            GrammarExample("कुली भारी बोझ उठाक डांडा पर पहुंची छोड़िन।", "कुली भारी बोझ उठाकर पहाड़ की चोटी पर पहुंच ही गए।", "Carrying heavy loads, the porters finally made it to the mountain summit.", "Intransitive terminative vector पहुंची छोड़िन")
        ],
        counter_examples=["पार कर लिया (Standard Hindi auxiliary लेना without the distinct Central Pahari perseverance/terminative nuance of छोड़ण)"],
        dialect_variations={
            "srinagariya": "करि छोड़ो",
            "tehri": "करीक छोडो",
            "salani": "करि छोड़ो",
            "rathwali": "करि छोड़ो"
        },
        linguistic_citation="Shipton (1936), Nanda Devi; Chatak (1959), Garhwali Bhasha; Negi (1954)"
    ),
    GrammarRule(
        rule_id="GARH-SYN-016",
        name="Iterative Temporal Reduplication in Adverbial Clauses (चलदा-चलदा, खोजदा-खोजदा)",
        category=RuleCategory.SYNTAX,
        rule_statement="Reduplication of the imperfective verbal participle in -दा expresses simultaneous progressive duration during an ongoing action ('while in the continuous act of walking/searching'), functioning as a temporal framing adverbial clause preceding the main predicate without any subordinating conjunction.",
        description="Extensively attested in mountain travel narratives and folktales: जांदा-जांदा (while going along), देखदा-देखदा (while watching on), खोजदा-खोजदा (while searching far and wide).",
        pattern="[Participle in -दा] + [Participle in -दा] + Main_Clause",
        examples=[
            GrammarExample("चलदा-चलदा हम रूपकुंड का कड़ा तक पुजि ग्या।", "चलते-चलते हम रूपकुंड की सीधी खड़ी चट्टान तक पहुंच गए।", "Walking steadily on and on, we reached the sheer cliff precipice of Roopkund.", "Iterative temporal reduplication चलदा-चलदा framing path progression"),
            GrammarExample("धूप-लकड़ी खोजदा-खोजदा गड़ेरिया खतलिंग हिमनद मा पुजिन।", "धूप की जड़ें खोजते-खोजते चरवाहे खतलिंग हिमनद तक पहुंच गए।", "Searching continuously for incense roots, the shepherds reached all the way to Khatling glacier.", "Iterative durative search action खोजदा-खोजदा")
        ],
        counter_examples=["जब हम चल रहे थे (Subordinating temporal conjunction jab without native Pahari participle reduplication)"],
        dialect_variations={
            "srinagariya": "चलदा-चलदा",
            "tehri": "हिंडदा-हिंडदा",
            "salani": "चलदा-चलदा",
            "rathwali": "चलदा-चलदा"
        },
        linguistic_citation="Painuli et al. (2000), Shri Nanda Devi Raj Jat; Shipton (1935), GJv85; Grierson (1916)"
    ),
    GrammarRule(
        rule_id="GARH-CONC-006",
        name="Attributive Adjective Agreement with Postpositional Case Stems (Oblique Inflection -आ / -ए)",
        category=RuleCategory.CONCORD_AGREEMENT,
        rule_statement="When a masculine singular noun ending in -ओ is governed by any case postposition (such as locative मा, genitive कु, dative तैं, or ablative से/बटि), the noun and all preceding attributive adjectives obligatorily shift concord from direct nominative -ओ to the oblique inflection -आ (or -ए in western dialects), maintaining strict morphosyntactic concord agreement.",
        description="A cardinal rule of Central Pahari noun-phrase concord: बड़ो डांडो (great mountain) -> बड़ा डांडा मा (on the great mountain); कालो खाडू (black ram) -> काळा खाडू कु (of the black ram).",
        pattern="[Adj_Root + -आ/-ए] + [Noun_Root + -आ/-ए] + [Postposition]",
        examples=[
            GrammarExample("बड़ा डांडा मा हिंवाळ पड़णी च।", "बड़े पहाड़ पर बर्फ पड़ रही है।", "Snow is falling on the great mountain ridge.", "Direct बड़ो डांडो inflects to oblique बड़ा डांडा before locative postposition मा"),
            GrammarExample("काळा खाडू कु सींग चार छन।", "काले मेढ़े के चार सींग हैं।", "The black ram has four horns.", "Direct कालो खाडू shifts to oblique काळा खाडू before genitive marker कु")
        ],
        counter_examples=["बड़ो डांडा मा (Grammatical discord: failure of attributive adjective to undergo oblique concord with its governed noun)"],
        dialect_variations={
            "srinagariya": "बड़ा डांडा मा",
            "tehri": "बडे डांडा मा / बडा डांडा मा",
            "salani": "बड़ा डांडा मा",
            "rathwali": "बड़ा डांडा मा"
        },
        linguistic_citation="Grierson (1916), LSI Central Pahari; Upreti (1900), Hill Dialects; Juyal (1967)"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

hon004_pos = text.find('rule_id="GARH-HON-004"')
if hon004_pos == -1:
    print("ERROR: Could not find GARH-HON-004")
    sys.exit(1)

close_paren = text.find("    )", hon004_pos)
if close_paren == -1:
    print("ERROR: Could not find end of GARH-HON-004")
    sys.exit(1)

end_pos = close_paren + len("    )")
reg_pos = text.find("class RuleRegistry:")

updated = text[:end_pos] + ",\n" + WAVE10_RULES + "\n]\n\n\n" + text[reg_pos:]

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(updated)

print("Appended Wave 10 rules to garhwali/grammar/rules.py successfully!")
