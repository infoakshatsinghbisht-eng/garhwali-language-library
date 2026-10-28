# -*- coding: utf-8 -*-
"""
Appends Wave 3 formal grammar rules cleanly to garhwali/grammar/rules.py with all fields.
"""

CLEAN_WAVE3_RULES = '''    GrammarRule(
        rule_id="GARH-PHON-006",
        name="Medial Hiatus Epenthesis with Palatal Glide (-य्-)",
        category=RuleCategory.PHONOLOGY,
        rule_statement="When a verbal or nominal open stem ending in -आ, -ओ, or -ऊ takes an inflectional suffix beginning with a front vowel (-इ, -ए), an epenthetic palatal glide (-य-) is systematically inserted to eliminate vowel hiatus.",
        description="Prevents vowel clash at morpheme boundaries: खा + -इ -> खायि / खायो (ate), हो + -ए -> ह्वै / ह्वे गे (became).",
        pattern="Stem[-V_open] + [-य-] + Suffix[-V_front]",
        examples=[
            GrammarExample("उन खाना खायो।", "उसने खाना खाया।", "He ate food.", "Glide -य- inserted after open stem खा-"),
            GrammarExample("सब काम ह्वै गे।", "सारा काम हो गया।", "All work was completed.", "Glide transition from root हो to front vowel")
        ],
        counter_examples=["खाइ (hiatus without glide in Hindi)"],
        dialect_variations={
            "srinagariya": "खायो / खायि",
            "tehri": "खायु",
            "salani": "खाया",
            "rathwali": "खायो"
        },
        linguistic_citation="Bailey (1908), Languages of the Northern Himalayas; Verma (1978)"
    ),
    GrammarRule(
        rule_id="GARH-NOM-007",
        name="Synthetic Instrumental-Locative Suffixal Fusion (-आं / -यां)",
        category=RuleCategory.NOMINAL_MORPHOLOGY,
        rule_statement="In classical folk ballads (Pawada) and poetic speech, spatial and bodily nouns form an archaic synthetic locative or instrumental without analytic postpositions by affixing -आं or -यां directly to the consonant stem.",
        description="Preserved in oral literature and customary legal oaths: हाथां (with one's own hands), घरां (at home), रातां (at night).",
        pattern="Noun_Stem + -आं / -यां",
        examples=[
            GrammarExample("उन अपणा हाथां तीर चलै।", "उसने अपने हाथों से तीर चलाया।", "He shot an arrow with his own hands.", "Synthetic instrumental हाथां without separate postposition ले"),
            GrammarExample("ऊ रात-रातां गौं पौंछी गे।", "वह रात ही रात में गांव पहुंच गया।", "He reached the village in the dead of night.", "Synthetic locative रातां")
        ],
        counter_examples=["हाथ से (Analytical Hindi construction)"],
        dialect_variations={
            "srinagariya": "हाथां / घरां",
            "tehri": "हाथुं / घरुं",
            "salani": "हाथां / घरां",
            "rathwali": "हाथां"
        },
        linguistic_citation="Grierson (1916), LSI IX-IV; Upreti (1900), Hill Dialects of Kumaun"
    ),
    GrammarRule(
        rule_id="GARH-PRON-006",
        name="Quantitative Indefinite Distributive Reduplication (क्य-क्य, कत्ति-कत्ति)",
        category=RuleCategory.PRONOMINAL,
        rule_statement="Interrogative and indefinite pronouns undergo complete lexical reduplication to denote plurality, variety, or distributive assignment among multiple referents.",
        description="Forms distributive and selective interrogative clauses: क्य-क्य (what various things), कु-कु (which respective people), कत्ति-कत्ति (in what varying quantities).",
        pattern="Pronoun[Int/Indef] + Pronoun[Int/Indef]",
        examples=[
            GrammarExample("तुमुल बजार बटी क्य-क्य बिसणी ल्याई?", "तुमने बाजार से क्या-क्या सामान लाया?", "What diverse provisions did you buy from the market?", "Distributive interrogative reduplication"),
            GrammarExample("कौथिग मा कु-कु लोग ऐ छा?", "मेले में कौन-कौन लोग आए थे?", "Which various people had come to the fair?", "Pluralized person query")
        ],
        counter_examples=["क्य सामान (Singular non-reduplicated query)"],
        dialect_variations={
            "srinagariya": "क्य-क्य / कु-कु",
            "tehri": "कि-कि / कु-कु",
            "salani": "क्या-क्या / कुण-कुण",
            "rathwali": "क्य-क्य / कु-कु"
        },
        linguistic_citation="Verma (1978), Pahari Language; Chatak (1959), Garhwali Bhasha"
    ),
    GrammarRule(
        rule_id="GARH-VRB-011",
        name="Inceptive Aspectual Periphrasis with Oblique Infinitive (-ण लगणु)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="The inchoative or inceptive aspect marking the start of an ongoing action is constructed with the oblique verbal infinitive in -ण followed by the finite inflected auxiliary लगणु (to begin).",
        description="Encodes the inception of an action or state: हुण लगी (started happening), रुण लग्या (began weeping).",
        pattern="Verb_Root + -ण + लगणु[Tense/Aspect/Gender/Number]",
        examples=[
            GrammarExample("डांडा मा बरखा हुण लगी।", "पहाड़ पर बारिश होने लगी।", "Rain began to fall on the mountain ridge.", "Inchoative auxiliary लगी with oblique infinitive हुण"),
            GrammarExample("नौना जोर-जोर से रुण लग्या।", "बच्चे जोर-जोर से रोने लगे।", "The boys began crying loudly.", "Plural masculine inceptive form लग्या")
        ],
        counter_examples=["बारिश शुरू हुई (Non-periphrastic loan construction)"],
        dialect_variations={
            "srinagariya": "हुण लग्यु / हुण लगी",
            "tehri": "हुण लगु / लगि",
            "salani": "होणा लग्या / लगी",
            "rathwali": "हुण लग्यो"
        },
        linguistic_citation="Grierson (1916), LSI IX-IV; Bailey (1915), Linguistic Studies"
    ),
    GrammarRule(
        rule_id="GARH-SYN-009",
        name="Correlative Relative Clause Fronting (जै-सो / जो-सो Paradigm)",
        category=RuleCategory.SYNTAX,
        rule_statement="In complex hypotactic constructions, the relative clause introduced by relative markers (जो, जै, जौं) obligatorily precedes the matrix correlative clause (सो, तै, तों), with the topic noun introduced in the relative clause and elided or pronominalized in the matrix.",
        description="Relative correlative syntax requiring clause fronting: जै मान्छे न मिहनत करी, तै तैं फल मिललो.",
        pattern="[Relative: जै/जो + Noun ... ] + [Correlative: तै/सो ... Verb]",
        examples=[
            GrammarExample("जै मान्छे न मिहनत करी, तै तैं फल मिललो।", "जिस मनुष्य ने मेहनत की, उसको फल मिलेगा।", "Whichever person worked hard, that person shall receive the fruit.", "Relative correlative fronted construction"),
            GrammarExample("जख पाणी छौ, तख हरियाली ह्वे।", "जहां पानी था, वहां हरियाली हुई।", "Where there was water, there greenery flourished.", "Spatial relative-correlative pair")
        ],
        counter_examples=["फल तै तैं मिललो जै न मिहनत करी (Dispreferred postposed relative)"],
        dialect_variations={
            "srinagariya": "जै ... तै तैं / जख ... तख",
            "tehri": "जै ... तै कु / जखा ... तखा",
            "salani": "जिन ... उन तैं / जां ... तां",
            "rathwali": "जै ... तै तैं"
        },
        linguistic_citation="Bailey (1915), Linguistic Studies from the Himalayas; Dobhal (2018)"
    ),
    GrammarRule(
        rule_id="GARH-CONC-004",
        name="Modal Vector Auxiliary Ergative Blocking (सकणु / पाणु Auxiliary Shift)",
        category=RuleCategory.CONCORD_AGREEMENT,
        rule_statement="When a transitive verb stem takes an intransitive modal potential auxiliary (सकणु 'to be able', पाणु 'to manage'), the ergative subject marking is strictly blocked in past perfective contexts; the subject remains in the nominative/direct case with nominative verb agreement.",
        description="The intransitive potential auxiliary governs the case alignment, blocking the split-ergative marker on the subject.",
        pattern="Subject[NOM] + Verb_Transitive_Stem + सक्यो/सकी/सक्या (NO ergative -न/-ले)",
        examples=[
            GrammarExample("ऊ भारी ढुंगो नी उठै सक्यो।", "वह भारी पत्थर नहीं उठा सका।", "He could not lift the heavy boulder.", "Nominative subject ऊ required; ergative उन strictly ungrammatical"),
            GrammarExample("हम समै पर गौं नी पौंछी पाया।", "हम समय पर गांव नहीं पहुंच पाए।", "We could not reach the village on time.", "Modal vector agreement shift")
        ],
        counter_examples=["उन भारी ढुंगो नी उठै सक्यो (Ergative subject with modal auxiliary is ungrammatical)"],
        dialect_variations={
            "srinagariya": "ऊ उठै नी सक्यो",
            "tehri": "ऊ उठै नी सकु",
            "salani": "वो उठै नी सक्या",
            "rathwali": "ऊ उठै नी सक्यो"
        },
        linguistic_citation="Verma (1978), Pahari Language; Grierson (1916), Central Pahari"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read()

# Normalize
text = text.replace("\r\n", "\n")

# Find where GARH-HON-003 ends
hon003_pos = text.find('rule_id="GARH-HON-003"')
if hon003_pos != -1:
    # Find closing `)` of GARH-HON-003
    close_paren = text.find("    )", hon003_pos)
    if close_paren != -1:
        end_rule_pos = close_paren + len("    )")
        reg_pos = text.find("class RuleRegistry:")
        
        # New text: everything up to end of GARH-HON-003 + comma + new rules + closing bracket + RuleRegistry
        updated = text[:end_rule_pos] + ",\n" + CLEAN_WAVE3_RULES + "\n]\n\n\n" + text[reg_pos:]
        with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
            f.write(updated)
        print("Updated rules.py with all 6 Wave 3 rules flawlessly!")
    else:
        print("close_paren for GARH-HON-003 not found")
else:
    print("GARH-HON-003 not found")
