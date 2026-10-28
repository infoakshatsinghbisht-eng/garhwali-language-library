# -*- coding: utf-8 -*-
"""
Appends Wave 3 formal grammar rules to garhwali/grammar/rules.py.
"""

NEW_RULES_CODE = '''    # --- WAVE 3 ADVANCED GRAMMATICAL RULES ---

    GrammarRule(
        rule_id="GARH-PHON-006",
        name="Medial Hiatus Epenthesis with Palatal Glide (-य्-)",
        category=RuleCategory.PHONOLOGY,
        description="When a verbal or nominal open stem ending in -आ, -ओ, or -ऊ takes an inflectional suffix beginning with a front vowel (-इ, -ए), an epenthetic palatal glide (-य-) is systematically inserted to eliminate vowel hiatus.",
        pattern="Stem[-V_open] + [-glide: -य-] + Suffix[-V_front]",
        examples=[
            {
                "garhwali": "उन खाना खायो / खाई",
                "hindi": "उसने खाना खाया",
                "english": "He ate food (epenthetic -य- prevents hiatus between stem खा and past vowel)",
            },
            {
                "garhwali": "काम ह्वै गे / ह्वे गे",
                "hindi": "काम हो गया",
                "english": "The work became done (glide transition from root हो to front vowel)",
            },
        ],
        exceptions="In rapid Salani colloquial speech, the glide is occasionally elided into an open diphthong.",
        dialect_variations={
            "srinagariya": "खायो / खायि",
            "tehri": "खायु",
            "salani": "खाया",
            "rathwali": "खायो",
        },
        citation="Bailey (1908: Languages of the Northern Himalayas), Verma (1978: Pahari Language Phonology)",
    ),

    GrammarRule(
        rule_id="GARH-NOM-007",
        name="Synthetic Instrumental-Locative Suffixal Fusion (-आं / -यां)",
        category=RuleCategory.NOMINAL_MORPHOLOGY,
        description="In classical folk ballads (Pawada) and poetic speech, spatial and bodily nouns form an archaic synthetic locative or instrumental without analytic postpositions by affixing -आं or -यां directly to the consonant stem.",
        pattern="Noun_Stem + -आं / -यां",
        examples=[
            {
                "garhwali": "उन अपणा हाथां तीर चलै",
                "hindi": "उसने अपने हाथों से तीर चलाया",
                "english": "He released an arrow with his own hands (synthetic instrumental हाथां without 'ले')",
            },
            {
                "garhwali": "ऊ रात-रातां गौं पौंछी गे",
                "hindi": "वह रात ही रात में गांव पहुंच गया",
                "english": "He reached the village in the dead of night (synthetic locative रातां)",
            },
        ],
        exceptions="Modern colloquial speech prefers the analytical postposition मा or सेती.",
        dialect_variations={
            "srinagariya": "हाथां / घरां",
            "tehri": "हाथुं / घरुं",
            "salani": "हाथां / घरां",
            "rathwali": "हाथां",
        },
        citation="Grierson (1916: LSI IX-IV), Upreti (1900: Hill Dialects of the Kumaun Division)",
    ),

    GrammarRule(
        rule_id="GARH-PRON-006",
        name="Quantitative Indefinite Distributive Reduplication (क्य-क्य, कत्ति-कत्ति)",
        category=RuleCategory.PRONOMINAL,
        description="Interrogative and indefinite pronouns undergo complete lexical reduplication to denote plurality, variety, or distributive assignment among multiple referents.",
        pattern="Pronoun[Int/Indef] + Pronoun[Int/Indef] (क्य-क्य, कत्ति-कत्ति, कु-कु)",
        examples=[
            {
                "garhwali": "तुमुल बजार बटी क्य-क्य बिसणी ल्याई?",
                "hindi": "तुमने बाजार से क्या-क्या सामान लाया?",
                "english": "What various items did you buy from the market?",
            },
            {
                "garhwali": "कौथिग मा कु-कु लोग ऐ छा?",
                "hindi": "मेले में कौन-कौन लोग आए थे?",
                "english": "Which diverse people had come to the fair?",
            },
        ],
        exceptions="Does not reduplicate when referring to a singular undifferentiated entity.",
        dialect_variations={
            "srinagariya": "क्य-क्य / कु-कु",
            "tehri": "कि-कि / कु-कु",
            "salani": "क्या-क्या / कुण-कुण",
            "rathwali": "क्य-क्य / कु-कु",
        },
        citation="Verma (1978: Pahari Language), Chatak (1959: Garhwali Bhasha)",
    ),

    GrammarRule(
        rule_id="GARH-VRB-011",
        name="Inceptive Aspectual Periphrasis with Oblique Infinitive (-ण लगणु)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        description="The inchoative or inceptive aspect marking the start of an ongoing action is constructed with the oblique verbal infinitive in -ण followed by the finite inflected auxiliary लगणु (to begin).",
        pattern="Verb_Root + -ण + लगणु[Tense/Aspect/Gender/Number]",
        examples=[
            {
                "garhwali": "डांडा मा बरखा हुण लगी",
                "hindi": "पहाड़ पर बारिश होने लगी",
                "english": "Rain began to fall on the mountain ridge",
            },
            {
                "garhwali": "नौना जोर-जोर से रुण लग्या",
                "hindi": "बच्चे जोर-जोर से रोने लगे",
                "english": "The boys began crying loudly",
            },
        ],
        exceptions="If the action is accidental or instantaneous, the vector auxiliary बैठणु or पड़णु is used instead of लगणु.",
        dialect_variations={
            "srinagariya": "हुण लग्यु / हुण लगी",
            "tehri": "हुण लगु / लगि",
            "salani": "होणा लग्या / लगी",
            "rathwali": "हुण लग्यो",
        },
        citation="Grierson (1916: LSI IX-IV), Bailey (1915: Linguistic Studies)",
    ),

    GrammarRule(
        rule_id="GARH-SYN-009",
        name="Correlative Relative Clause Fronting (जै-सो / जो-सो Paradigm)",
        category=RuleCategory.SYNTAX,
        description="In complex hypotactic constructions, the relative clause introduced by relative markers (जो, जै, जौं) obligatorily precedes the matrix correlative clause (सो, तै, तों), with the topic noun introduced in the relative clause and elided or pronominalized in the matrix.",
        pattern="[Relative: जै/जो + Noun ... ] + [Correlative: तै/सो ... Verb]",
        examples=[
            {
                "garhwali": "जै मान्छे न मिहनत करी, तै तैं फल मिललो",
                "hindi": "जिस मनुष्य ने मेहनत की, उसको फल मिलेगा",
                "english": "Whichever person worked hard, that person shall receive the fruit",
            },
            {
                "garhwali": "जख पाणी छौ, तख हरियाली ह्वे",
                "hindi": "जहां पानी था, वहां हरियाली हुई",
                "english": "Where there was water, there greenery flourished",
            },
        ],
        exceptions="In modern colloquial speech influenced by Hindi, postposed relative clauses occasionally appear.",
        dialect_variations={
            "srinagariya": "जै ... तै तैं / जख ... तख",
            "tehri": "जै ... तै कु / जखा ... तखा",
            "salani": "जिन ... उन तैं / जां ... तां",
            "rathwali": "जै ... तै तैं",
        },
        citation="Bailey (1915: Linguistic Studies from the Himalayas), Dobhal (2018)",
    ),

    GrammarRule(
        rule_id="GARH-CONC-004",
        name="Modal Vector Auxiliary Ergative Blocking (सकणु / पाणु Auxiliary Shift)",
        category=RuleCategory.CONCORD_AGREEMENT,
        description="When a transitive verb stem takes an intransitive modal potential auxiliary (सकणु 'to be able', पाणु 'to manage'), the ergative subject marking is strictly blocked in past perfective contexts; the subject remains in the nominative/direct case with nominative verb agreement.",
        pattern="Subject[NOM] + Verb_Transitive_Stem + सक्यो/सकी/सक्या (NO ergative -न/-ले)",
        examples=[
            {
                "garhwali": "ऊ भारी ढुंगो नी उठै सक्यो",
                "hindi": "वह भारी पत्थर नहीं उठा सका (न कि 'उसने')",
                "english": "He could not lift the heavy boulder (subject ऊ remains nominative, not ergative उन, because auxiliary सक्यो is intransitive)",
            },
            {
                "garhwali": "हम समै पर गौं नी पौंछी पाया",
                "hindi": "हम समय पर गांव नहीं पहुंच पाए",
                "english": "We could not reach the village on time",
            },
        ],
        exceptions="Lexicalized transitive auxiliaries like देणु (allow) maintain regular ergative subject marking.",
        dialect_variations={
            "srinagariya": "ऊ उठै नी सक्यो",
            "tehri": "ऊ उठै नी सकु",
            "salani": "वो उठै नी सक्या",
            "rathwali": "ऊ उठै नी सक्यो",
        },
        citation="Verma (1978: Pahari Language), Grierson (1916: Central Pahari)",
    ),
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read()

# Normalize line endings
text = text.replace("\r\n", "\n")

target_str = "\n]\n\n\nclass RuleRegistry:"
if target_str in text:
    updated = text.replace(target_str, NEW_RULES_CODE + target_str, 1)
    with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
        f.write(updated)
    print("Successfully appended Wave 3 rules to rules.py!")
else:
    # Try alternative matching
    reg_idx = text.find("class RuleRegistry:")
    if reg_idx != -1:
        bracket_idx = text.rfind("]", 0, reg_idx)
        if bracket_idx != -1:
            updated = text[:bracket_idx] + NEW_RULES_CODE + text[bracket_idx:]
            with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
                f.write(updated)
            print("Successfully inserted Wave 3 rules before RuleRegistry!")
        else:
            print("Bracket before RuleRegistry not found")
    else:
        print("RuleRegistry not found")
