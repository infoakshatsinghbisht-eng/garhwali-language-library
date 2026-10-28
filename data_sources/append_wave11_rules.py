# -*- coding: utf-8 -*-
"""
Appends Wave 11 formal grammar rules to garhwali/grammar/rules.py:
1. GARH-PRON-007: Reciprocal Pronominal Doubling with Case Cliticization (आपस मा / अपणा-आप)
2. GARH-VRB-019: Frequentative-Habitual Aspect Formed with Auxiliary Verb रौण (Continuous Customary State)
3. GARH-SYN-017: Preposed Conditional Inversion without Explicit Conjunction (अगर / यदि Ellipsis)
4. GARH-CASE-011: Perlative and Comitative Marker साथि / दगड़ी (Comitative Journeying across Passes)
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WAVE11_RULES = '''    GrammarRule(
        rule_id="GARH-PRON-007",
        name="Reciprocal Pronominal Doubling with Case Cliticization (आपस मा / अपणा-आप)",
        category=RuleCategory.PRONOMINAL,
        rule_statement="Reciprocal action ('among themselves', 'to one another') in Garhwali and Western Central Pahari is expressed through the reduplicated reflexive stem अपणा-आप or the locatively governed reciprocal pronoun आपस मा (governing plural concord on the verb), contrasting with unilateral actions.",
        description="Standard in traditional clan councils, communal agreements, and kinship interactions: आपस मा बांटण (to divide mutually among themselves), अपणा-आप मा मिलण (to meet among themselves).",
        pattern="[Subject_Plural] + [आपस मा / अपणा-आप] + [Predicate_Plural]",
        examples=[
            GrammarExample("खत का सयाणा आपस मा विचार करदा।", "खत के सयाणे आपस में विचार-विमर्श करते हैं।", "The elders of the territorial Khat consult mutually among themselves.", "Reciprocal pronoun आपस मा with plural habitual predicate करदा"),
            GrammarExample("जोड़ीदार अपणा-आप मा खेती बांटदा।", "सह-पति आपस में खेती-किसानी बांटते हैं।", "The fraternal joint husbands divide the agricultural duties among themselves.", "Reduplicated reciprocal अपणा-आप मा governing mutual labor division")
        ],
        counter_examples=["एक दूसरे से (Standard Hindi periphrastic reciprocal expression without native Pahari pronominal cliticization)"],
        dialect_variations={
            "srinagariya": "आपस मा",
            "tehri": "आपस मा / अपणा-आप",
            "salani": "आपस मा",
            "rathwali": "आपस मा"
        },
        linguistic_citation="Majumdar (1960), Himalayan Polyandry; Ross (1874), Settlement of Jaunsar-Bawar; Grierson (1916)"
    ),
    GrammarRule(
        rule_id="GARH-VRB-019",
        name="Frequentative-Habitual Aspect Formed with Auxiliary Verb रौण (Continuous Customary State)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Habitual customary practices, seasonal traditions, or perpetual mountain states are constructed by appending the imperfective participle in -दो / -दी / -दा to the conjugated auxiliary verb रौण ('to stay/remain': रौंदो / रौंदी / रौंदा / रयाँ), expressing customary continuity over generations.",
        description="Characterizes cyclic agricultural life and transhumance: शीतकाल मा निचला घाटी मा रौंदा (habitually staying in lower valleys in winter), छान मा दूध-दही जमा करदा रौंदा (continually gathering dairy at cattle-stations).",
        pattern="[Verb_Root + -दा/-दी/-दो] + [रौण Aux Conjugated]",
        examples=[
            GrammarExample("सर्दियों मा लोग छान मा दूध-दही जमा करदा रौंदा।", "सर्दियों में लोग छान (गोशाला) में दूध-दही इकट्ठा करते रहते हैं।", "During winters, the people continually gather milk and butter in the upland cattle stations.", "Imperfective participle करदा paired with auxiliary रौंदा"),
            GrammarExample("माणा का लोग शीतकाल मा निचला घाटी मा रौंदा।", "माणा के लोग सर्दियों में निचली घाटी में रहते हैं।", "The people of Mana village habitually reside in the lower valley during winter.", "Frequentative seasonal migration indicated by habitual auxiliary रौंदा")
        ],
        counter_examples=["रहते रहना (Hindi redundant aspectual chain without native Pahari participle-auxiliary fusion)"],
        dialect_variations={
            "srinagariya": "करदा रौंदा",
            "tehri": "करदा रौण",
            "salani": "करदा रौंदा",
            "rathwali": "करदा रौंदा"
        },
        linguistic_citation="Sharma (1955), Himtirtha Badrinath; Majumdar (1960), Himalayan Polyandry; Juyal (1967)"
    ),
    GrammarRule(
        rule_id="GARH-SYN-017",
        name="Preposed Conditional Inversion without Explicit Conjunction (अगर / यदि Ellipsis)",
        category=RuleCategory.SYNTAX,
        rule_statement="In spoken Garhwali dialogues and oral customary law formulas, conditional protases omit the overt subordinating conjunction (अगर / यदि) and rely on prospective or subjunctive inflection in the protasis followed immediately by the correlative particle त, producing paratactic conditional structures with fronted topic focus.",
        description="Frequent in customary rulings and mountain survival rules: बर्फ-तूफान ऐ ग्ये त यात्रा रुकि जाली (Should a blizzard strike, the journey will halt), सयाणा न बोलि द्ये त सब मानला (If the elder gives his word, everyone will comply).",
        pattern="[Protasis Clause (Subjunctive/Past)] + त + [Apodosis Clause (Future/Imperative)]",
        examples=[
            GrammarExample("बर्फ-तूफान ऐ ग्ये त यात्रा रुकि जाली।", "यदि बर्फीला तूफान आ गया तो यात्रा रुक जाएगी।", "Should a blizzard strike, the pilgrimage will halt.", "Conditional protasis with zero-conjunction marker and correlative त"),
            GrammarExample("स्याणा न बोलि द्ये त सब मानला।", "यदि सयाणे (मुखिया) ने कह दिया तो सब मानेंगे।", "If the elder chief gives his word, everyone will comply.", "Ergative past protasis without explicit 'if' followed by correlative resolution")
        ],
        counter_examples=["अगर बर्फ-तूफान आएगा तो (Standard Hindi conditional with overt Persian conjunction अगर)"],
        dialect_variations={
            "srinagariya": "त",
            "tehri": "त",
            "salani": "ता",
            "rathwali": "ता"
        },
        linguistic_citation="Ross (1874), Dastur-ul-Amal Jaunsar; Tilman (1937), Ascent of Nanda Devi; Chatak (1959)"
    ),
    GrammarRule(
        rule_id="GARH-CASE-011",
        name="Perlative and Comitative Marker साथि / दगड़ी (Comitative Journeying across Passes)",
        category=RuleCategory.CASE_SYSTEM,
        rule_statement="Joint accompaniment and associative movement across mountain trails are marked by the comitative postposition दगड़ी (or साथि), which governs the genitive or oblique form of the dependent noun or pronoun ([Noun] + का + दगड़ी or [Pronoun] + दगड़ी).",
        description="Ubiquitous in alpine expeditions, pastoral migrations, and family visits: पसंग का दगड़ी (accompanied by Pasang), मां का दगड़ी (along with mother).",
        pattern="[Noun/Pronoun] + [Genitive का] + दगड़ी/साथि",
        examples=[
            GrammarExample("यात्री पसंग का दगड़ी नंदा देवी का कड़ा कन्नी चलिन।", "तीर्थयात्री पसंग के साथ नंदा देवी की सीधी चट्टान की ओर चले।", "The climbers walked towards the sheer cliff wall of Nanda Devi along with Pasang.", "Comitative postposition दगड़ी following genitive marker का"),
            GrammarExample("ध्यांटी अपणी मां का दगड़ी मायके जांदी।", "विवाहिता पुत्री अपनी मां के साथ मायके जाती है।", "The married daughter travels to her maternal home accompanied by her mother.", "Associative movement marked by मां का दगड़ी")
        ],
        counter_examples=["पसंग के साथ (Standard Hindi directional/associative marker साथ without native Pahari postposition दगड़ी)"],
        dialect_variations={
            "srinagariya": "दगड़ी",
            "tehri": "दगडी",
            "salani": "दगड़ी",
            "rathwali": "दगड़ी"
        },
        linguistic_citation="Tilman (1937), Ascent of Nanda Devi; Majumdar (1960), Himalayan Polyandry; Grierson (1916)"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

conc006_pos = text.rfind('rule_id="GARH-CONC-006"')
if conc006_pos == -1:
    print("ERROR: Could not find GARH-CONC-006")
    sys.exit(1)

close_paren = text.find("    )", conc006_pos)
if close_paren == -1:
    print("ERROR: Could not find end of GARH-CONC-006")
    sys.exit(1)

end_pos = close_paren + len("    )")
reg_pos = text.find("class RuleRegistry:")

updated = text[:end_pos] + ",\n" + WAVE11_RULES + "\n]\n\n\n" + text[reg_pos:]

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(updated)

print("Appended Wave 11 rules to garhwali/grammar/rules.py successfully!")

