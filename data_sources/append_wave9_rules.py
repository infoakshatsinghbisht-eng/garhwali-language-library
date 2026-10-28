# -*- coding: utf-8 -*-
"""
Appends Wave 9 formal grammar rules to garhwali/grammar/rules.py:
1. GARH-VRB-017: Continuative-Durative Aspect with Auxiliary Verb जाण / जांद
2. GARH-SYN-015: Contrastive Focus and Topic Marker Particle त / ता in Discursive Clauses
3. GARH-CASE-010: Allative-Directive Postposition कन्नी / तरफ (Directional Motion toward Mountain Landmarks)
4. GARH-HON-004: Reverential Deferential Imperative in Pilgrim and Ascetic Directives (-इयो / -इया)
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WAVE9_RULES = '''    GrammarRule(
        rule_id="GARH-VRB-017",
        name="Continuative-Durative Aspect with Auxiliary Verb जाण / जांद (Progressive Movement / Continuous Action)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="In Garhwali, continuous gradual action or ongoing motion along a mountain path is constructed by attaching the imperfective participle in -दो / -दी / -दा to the auxiliary verb जाण (to go, conjugated for tense/person: जांदो / जांदी / जांदा / जाला), expressing an action that progresses steadily over time or space (e.g., बाटो चढ़दा जाण - to keep climbing the path, पाणी बग्दा जांदू - the water keeps flowing on).",
        description="Peculiar to Himalayan spatial descriptions and progressive processes: उकाली चढ़दा जांदा (they keep climbing the steep incline), घाम लगदा जांदू (it gradually keeps getting sunnier), बर्फ पिघलदा जांदी (the snow keeps melting away).",
        pattern="[Verb_Root + -दा/-दी/-दो] + [जाण Aux Conjugated]",
        examples=[
            GrammarExample("यात्री उकाली चढ़दा जांदा।", "तीर्थयात्री खड़ी चढ़ाई चढ़ते चले जाते हैं।", "The pilgrims keep climbing steadily up the steep mountain ascent.", "Imperfective participle चढ़दा followed by auxiliary जांदा"),
            GrammarExample("हिमशिखर का बीच हिमनद सरकदा जांदू च।", "बर्फ की चोटियों के बीच हिमनद खिसकता चला जाता है।", "Between the snowy peaks, the glacier keeps slowly sliding onwards.", "Durative aspect सरकदा जांदू expressing continuous glacial progression")
        ],
        counter_examples=["चढ़ते रहना (Analytical Hindi aspectual compound with रहना instead of native Central Pahari auxiliary जाण)"],
        dialect_variations={
            "srinagariya": "चढ़दा जांदा",
            "tehri": "चढ़दा जाण",
            "salani": "चढ़दा जांदा",
            "rathwali": "चढ़दा जांदा"
        },
        linguistic_citation="Smythe (1932), Kamet Conquered; Grierson (1916), LSI Central Pahari; Sharma (1938), Badrinath-Kedarnath Yatra"
    ),
    GrammarRule(
        rule_id="GARH-SYN-015",
        name="Contrastive Focus and Topic Marker Particle त / ता in Discursive Clauses",
        category=RuleCategory.SYNTAX,
        rule_statement="Garhwali employs the enclitic discourse particle त (or ता in Rathwali and Salani) immediately following a nominal constituent, pronoun, or clause boundary to mark contrastive focus, topicalization, or emphatic assertion ('as for X', 'indeed', 'on the other hand'), contrasting two distinct alternatives, entities, or propositions.",
        description="Widely used in dialogues, mountain narratives, and route directions: हम त बद्रीनाथ जाला (as for us, we shall go to Badrinath), वल्ला बाटो त तंग च (this near path is indeed narrow, in contrast to the other).",
        pattern="[Constituent] + त/ता + [Predicate]",
        examples=[
            GrammarExample("हम त बद्रीनाथ जाला, तुम कख जौला?", "हम तो बद्रीनाथ जाएंगे, आप कहां जाएंगे?", "As for us, we will proceed to Badrinath; where will you go?", "Contrastive topic marking on first-person pronoun हम त"),
            GrammarExample("इन्धी त बाटो भारी डाँठ च, उनधी सौंलो च।", "इस तरफ तो रास्ता बेहद तंग दर्रा है, उस तरफ सुगम है।", "On this side the path is indeed a narrow rocky defile, whereas on that side it is gentle.", "Spatial contrastive focus marking with इन्धी त")
        ],
        counter_examples=["लेकिन/परंतु (Analytical Sanskritized disjunctive conjunctions without native enclitic topic focus marker त)"],
        dialect_variations={
            "srinagariya": "त",
            "tehri": "त",
            "salani": "ता",
            "rathwali": "ता"
        },
        linguistic_citation="Chatak (1959), Garhwali Bhasha; Grierson (1916), LSI Central Pahari; Khan (1978), History of Srinagar"
    ),
    GrammarRule(
        rule_id="GARH-CASE-010",
        name="Allative-Directive Postposition कन्नी / तरफ (Directional Motion toward Mountain Landmarks)",
        category=RuleCategory.CASE_SYSTEM,
        rule_statement="Spatial direction and allative movement towards a mountain landmark, ridge, holy shrine, or settlement is marked by the postposition कन्नी (or तरफ / बटि), which governs the oblique or genitive base of the preceding noun (e.g., डांडा कन्नी 'towards the mountain crest', गौं कन्नी 'towards the village', तप्तकुंड कन्नी 'towards the thermal spring').",
        description="Ubiquitous in alpine navigation, pilgrim guidance, and pastoral movements across Garhwal valleys: धार कन्नी (towards the high ridge), नदी कन्नी (towards the riverbed).",
        pattern="[Noun/Toponym] + [Oblique Marker] + कन्नी/तरफ",
        examples=[
            GrammarExample("ग्वालिया डांडा कन्नी गाय-बख्री ले जांदू।", "ग्वाला पहाड़ की ओर गाय-बकरियां ले जाता है।", "The cowherd takes the cattle and goats towards the high mountain ridge.", "Directive postposition कन्नी following toponym noun डांडा"),
            GrammarExample("तीर्थयात्री अलकनंदा का तप्तकुंड कन्नी चलिन।", "तीर्थयात्री अलकनंदा के तप्तकुंड की ओर चले।", "The pilgrims walked towards the sacred thermal spring of the Alaknanda.", "Allative direction marked by तप्तकुंड कन्नी")
        ],
        counter_examples=["पहाड़ की तरफ (Standard Hindi directional phrasal postposition without native Garhwali allative postposition कन्नी)"],
        dialect_variations={
            "srinagariya": "कन्नी",
            "tehri": "कणी / कानी",
            "salani": "कन्नी",
            "rathwali": "कन्नी"
        },
        linguistic_citation="Grierson (1916), LSI Central Pahari; Sharma (1938), Badrinath-Kedarnath Yatra; Smythe (1932), GJv79"
    ),
    GrammarRule(
        rule_id="GARH-HON-004",
        name="Reverential Deferential Imperative in Pilgrim and Ascetic Directives (-इयो / -इया)",
        category=RuleCategory.HONORIFICS,
        rule_statement="When addressing elders, revered holy ascetics, hermits, or honored guests in the Himalayas, Garhwali employs the highly deferential respectful imperative suffix -इयो (or -इया), appended to the verb root (e.g., आइजियो 'please come', बैठिजियो 'please be seated', देखिजियो 'please behold / observe', धरीजियो 'please place/step').",
        description="Culturally paramount in pilgrimage hospitality, hermitages (ashrams), and respectful village assemblies across Garhwal: महाराज चरण धरीजियो (Revered swami, please step forward), प्रसाद लीजियो (Please accept the holy prasad).",
        pattern="[Verb_Root] + [-इयो / -इया] (Reverential Honorific)",
        examples=[
            GrammarExample("महाराज, हमरा आश्रम मा चरण धरीजियो।", "महाराज, हमारे आश्रम में चरण रखिए।", "Revered sage, please grace our hermitage with your sacred footsteps.", "Deferential imperative धरीजियो used with ascetic address महाराज"),
            GrammarExample("बद्री-विशाल का कपाट दर्शन करिजियो।", "भगवान बद्री-विशाल के कपाट दर्शन कीजिएगा।", "Please behold the sacred sanctum opening of Lord Badri-Vishal.", "Respectful pilgrim imperative करिजियो for sacred viewing")
        ],
        counter_examples=["तू आ / तुम आओ (Informal or non-honorific imperative suffixes lacking deferential -इयो)"],
        dialect_variations={
            "srinagariya": "-इयो",
            "tehri": "-इया",
            "salani": "-इयो",
            "rathwali": "-इयो"
        },
        linguistic_citation="Swami Sivananda (1966), Himalayan Forest Academy; Sharma (1938), Badrinath-Kedarnath Yatra; Juyal (1967)"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

syn014_pos = text.find('rule_id="GARH-SYN-014"')
if syn014_pos == -1:
    print("ERROR: Could not find GARH-SYN-014")
    sys.exit(1)

close_paren = text.find("    )", syn014_pos)
if close_paren == -1:
    print("ERROR: Could not find end of GARH-SYN-014")
    sys.exit(1)

end_pos = close_paren + len("    )")
reg_pos = text.find("class RuleRegistry:")

updated = text[:end_pos] + ",\n" + WAVE9_RULES + "\n]\n\n\n" + text[reg_pos:]

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(updated)

print("Appended Wave 9 rules to garhwali/grammar/rules.py successfully!")

