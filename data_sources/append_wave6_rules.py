# -*- coding: utf-8 -*-
"""
Appends Wave 6 formal grammar rules to garhwali/grammar/rules.py.
Rules:
1. GARH-VRB-014: Optative-Benedictive Mood Suffixation (-ए / -इयै)
2. GARH-SYN-012: Prohibitive Negative Inversion with Preverbal झनि (Prohibitive झनि-Movement)
3. GARH-CASE-009: Perlative Spatial-Transitive Postposition ह्वैक ('Via / Through / Passing by')
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WAVE6_RULES = '''    GrammarRule(
        rule_id="GARH-VRB-014",
        name="Optative-Benedictive Mood Suffixation (-ए / -इयै)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Wishes, traditional blessings, ritual prayers, and optative invocations express desired futures through the synthetic optative suffix -ए (3rd singular/general) or -इयै (2nd/3rd honorific benedictive), distinct from the imperative and future subjunctive.",
        description="Widely used in elders' blessings, temple Jagar chants, and departure prayers: भगवान तेरु भलो करै (May God bless you and grant you well-being), सदा सुखी रइयै (May you ever remain in peace and joy).",
        pattern="Verb_Root + -ए / -इयै (Optative-Benedictive Mood)",
        examples=[
            GrammarExample("भगवान तेरु भलो करै।", "भगवान तुम्हारा भला करे।", "May God bless you and grant you well-being.", "Optative suffix -ए on verb stem कर- expressing benedictive desire"),
            GrammarExample("सदा जुग-जुग जियै अर सुखी रइयै।", "सदा युग-युग जियो और सुखी रहो।", "May you live for ages and ever remain in peace.", "Benedictive suffix -इयै in pastoral elder blessing")
        ],
        counter_examples=["भगवान तुम्हारा भला करेगा (Hindi indicative future with uninflected modal auxiliary)"],
        dialect_variations={
            "srinagariya": "करै / रइयै",
            "tehri": "करो / रइयो",
            "salani": "करै / रहियै",
            "rathwali": "करै / रइयै"
        },
        linguistic_citation="Grierson (1916), LSI Central Pahari; Chatak (1959), Garhwali Bhasha; Juyal (1967), Madhya Pahadi"
    ),
    GrammarRule(
        rule_id="GARH-SYN-012",
        name="Prohibitive Negative Inversion with Preverbal झनि (Prohibitive झनि-Movement)",
        category=RuleCategory.SYNTAX,
        rule_statement="Prohibitive commands ('do not / must not') strictly employ the dedicated prohibitive particle झनि (cognate with Sanskrit मा / Old Indo-Aryan मा-स्म), which obligatorily precedes the imperative verb stem, contrasting with standard clause-final negator नि.",
        description="Whereas declarative negation places नि immediately after or before the copula (हूँ नि जांदो 'I do not go'), prohibitive injunctions require झनि in strict preverbal position (झनि जा 'do not go!', उख झनि बिसरै 'do not forget there!').",
        pattern="Object/Complement + झनि + Verb_Imperative",
        examples=[
            GrammarExample("ऊँचे डांडा मा एक्ला झनि जा।", "ऊंचे पहाड़ पर अकेले मत जाओ।", "Do not go alone onto the high ridge!", "Preverbal prohibitive marker झनि placed before imperative जा"),
            GrammarExample("पुश्तैनी थात तैं कभे झनि बेच्यै।", "पुश्तैनी ज़मीन को कभी मत बेचना।", "Never sell your ancestral estate!", "Prohibitive झनि modifying prescriptive optative-imperative बेच्यै")
        ],
        counter_examples=["मत जाओ बाद में (Hindi permissive post-verbal negative particle)"],
        dialect_variations={
            "srinagariya": "झनि जा / झनि करा",
            "tehri": "जनि जा / जनि करो",
            "salani": "झनि जा / झनि कर",
            "rathwali": "झनि जा"
        },
        linguistic_citation="Batten (1851), Official Reports; Grierson (1916), LSI Central Pahari; Verma (1978), Pahari Language"
    ),
    GrammarRule(
        rule_id="GARH-CASE-009",
        name="Perlative Spatial-Transitive Postposition ह्वैक ('Via / Through / Passing by')",
        category=RuleCategory.CASE_SYSTEM,
        rule_statement="Traversal through a spatial landmark, mountain pass, or intermediate station ('via / by way of / through') is marked by the specialized perlative postposition ह्वैक (literally 'having transited', the conjunctive participle of the verb होण), governing the direct or locative base of the landmark.",
        description="Fundamental in Himalayan trade and pilgrim itineraries: माना दर्रा ह्वैक (via the Mana Pass), श्रीनगर ह्वैक बदरीनाथ जाणा (to travel to Badrinath via Srinagar), जंगल ह्वैक (passing through the dense forest).",
        pattern="Toponym/Landmark[Direct/Locative] + ह्वैक + Movement_Verb",
        examples=[
            GrammarExample("व्यापारी नीति दर्रा ह्वैक तिब्बत जांदा छा।", "व्यापारी नीति दर्रे से होकर तिब्बत जाते थे।", "The merchants used to travel to Tibet via the Niti pass.", "Perlative postposition ह्वैक marking transit through mountain pass"),
            GrammarExample("गौं का बाटा ह्वैक नदी का तीरा पुज्या।", "गांव के रास्ते से होकर नदी के तट पर पहुंचे।", "Passing through the village path, they reached the river bank.", "Spatial-transitive traversal marked by ह्वैक")
        ],
        counter_examples=["रास्ते से (Simple ablative instrumental without perlative traversal participle)"],
        dialect_variations={
            "srinagariya": "ह्वैक",
            "tehri": "ह्वैकि / ह्वेकी",
            "salani": "होइक",
            "rathwali": "ह्वैक"
        },
        linguistic_citation="Sherring (1906), Western Tibet & British Borderland; Bisht (1994), Tourism in Garhwal; Grierson (1916), LSI"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

syn011_pos = text.find('rule_id="GARH-SYN-011"')
if syn011_pos == -1:
    print("ERROR: Could not find GARH-SYN-011")
    sys.exit(1)

close_paren = text.find("    )", syn011_pos)
if close_paren == -1:
    print("ERROR: Could not find end of GARH-SYN-011")
    sys.exit(1)

end_pos = close_paren + len("    )")
reg_pos = text.find("class RuleRegistry:")

updated = text[:end_pos] + ",\n" + WAVE6_RULES + "\n]\n\n\n" + text[reg_pos:]

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(updated)

print("Appended Wave 6 rules to garhwali/grammar/rules.py successfully!")
