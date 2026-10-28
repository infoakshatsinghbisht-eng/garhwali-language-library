# -*- coding: utf-8 -*-
import sys

new_rules_text = '''    # Wave 2 Additions: Concord, Verbs, Cases, Syntax, Pronouns & Honorifics
    GrammarRule(
        rule_id="GARH-CONC-003",
        name="Genitive Postposition Gender-Number Concord with Possessed Head",
        category=RuleCategory.CONCORD_AGREEMENT,
        rule_statement="The nominal genitive postposition (-को / -का / -की) and pronominal genitive (-रो / -रा / -री) obligatorily inflect to agree in gender, number, and case with the possessed head noun, never the possessor.",
        description="राम को घ्वड़ो (Ram's horse [m.sg]), राम का घ्वड़ा (Ram's horses [m.pl]), राम की घोड़ी (Ram's mare [f.sg]), राम का घ्वड़ा पर (on Ram's horse [m.sg oblique]).",
        pattern="Possessor + Genitive[-o / -a / -i] + Possessed_Noun[Gender, Number, Case]",
        examples=[
            GrammarExample("राम को घर", "राम का घर", "Ram's house", "Masculine singular direct concord: -को"),
            GrammarExample("राम का घ्वड़ा", "राम के घोड़े", "Ram's horses", "Masculine plural direct concord: -का"),
            GrammarExample("राम की गाय", "राम की गाय", "Ram's cow", "Feminine singular concord: -की"),
            GrammarExample("मेरो भुलू", "मेरा छोटा भाई", "My younger brother", "1st person pronominal masculine concord: -रो")
        ],
        counter_examples=["राम का घर (Singular direct noun with plural genitive)"],
        dialect_variations={"srinagariya": "को / का / की", "rathwali": "कु / का / कि", "tehri": "को / का / की", "salani": "का / की"},
        linguistic_citation="Bailey (1915), Linguistic Studies from the Himalayas; Grierson LSI"
    ),
    GrammarRule(
        rule_id="GARH-VRB-009",
        name="Imperfective Habitual Past Periphrasis (-दो छौ / -दो थौ)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Habitual, repetitive, or customary actions in the past are constructed with the imperfective participle in -दो/-दा/-दी accompanied by the past copula छौ / थौ (chhau / thau).",
        description="Denotes past customary events: ऊ रोज नदी मा न्हौंदो छौ (He used to bathe in the river every day), हम स्कूल जांदा छा (We used to go to school).",
        pattern="Subject + Verb-Root + -दो/-दा/-दी + छौ/थौ [agrees in gender/number]",
        examples=[
            GrammarExample("ऊ रोज नदी मा न्हौंदो छौ।", "वह रोज नदी में नहाया करता था।", "He used to bathe in the river daily.", "Masculine singular habitual past"),
            GrammarExample("हम बगत पर स्कूल जांदा छा।", "हम समय पर स्कूल जाया करते थे।", "We used to go to school on time.", "Plural habitual past agreement")
        ],
        counter_examples=["वह रोज नदी में नहाता था (Standard Hindi past imperfective)"],
        dialect_variations={"srinagariya": "न्हौंदो छौ", "rathwali": "न्हौंदु थौ", "salani": "न्हांदा छा", "tehri": "न्हांदो छो"},
        linguistic_citation="Bailey (1915); Grierson LSI Vol IX Pt IV"
    ),
    GrammarRule(
        rule_id="GARH-CASE-007",
        name="Compound Postpositional Spatial Hierarchy (भीतर बटी, डांडा माथि, गाड़ पार)",
        category=RuleCategory.CASE_SYSTEM,
        rule_statement="Complex spatial relations are expressed by compound postpositional stacks where a secondary locational head follows the primary noun in oblique case.",
        description="Expresses nuanced direction: कमरा भीतर बटी (from inside the room), डांडा माथि (on top of the ridge), गाड़ पार (across the river), खोली का आगू (in front of the main doorway).",
        pattern="Noun[Oblique] + (का) + [भीतर / माथि / पार / आगू / तळे] + (बटी)",
        examples=[
            GrammarExample("ऊ कमरा भीतर बटी निकळिगे।", "वह कमरे के अंदर से बाहर निकल गया।", "He emerged from inside the room.", "Compound ablative भीतर बटी"),
            GrammarExample("डांडा माथि मंदिर च।", "पहाड़ की चोटी के ऊपर मंदिर है।", "There is a temple atop the mountain ridge.", "Compound locative डांडा माथि")
        ],
        counter_examples=["कमरे के अंदर से (Standard Hindi compound postposition)"],
        linguistic_citation="Verma (1978); Walton (1910)"
    ),
    GrammarRule(
        rule_id="GARH-VRB-010",
        name="Double Causative Stem Expansion with Medial -वाळ- (-vaal-)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Double (mediated) causatives expand the verb stem with the infix -वाळ- / -वा- (-vaal- / -vaa-) to designate that an action is commissioned through an intermediary.",
        description="Direct action: पढ़णु (to read); 1st causative: पढ़ाळणु (to teach directly); 2nd double causative: पढ़वाळणु (to get someone taught through a third person).",
        pattern="Verb-Root + -वाळ- / -वा- + -णु",
        examples=[
            GrammarExample("मास्टर जी न नौना तैं पढ़वाळ्यो।", "शिक्षक ने बच्चे को किसी और से पढ़वाया।", "The teacher had the child instructed via an assistant.", "Double causative infix -vaal-"),
            GrammarExample("बुबाजी न मकान बनवाळ्यो।", "पिता जी ने कारीगर से मकान बनवाया।", "Father had the house built through master stonemasons.", "Double causative बनवाळ्यो")
        ],
        counter_examples=["बनवाया (Plain Hindi double causative without retroflex lateral)"],
        linguistic_citation="Bailey (1915); Verma (1978); Chatak (1959)"
    ),
    GrammarRule(
        rule_id="GARH-SYN-008",
        name="Clitic Particle Focus Attachment (-इ / -ही)",
        category=RuleCategory.SYNTAX,
        rule_statement="Exclusive focus, emphatic certainty, or temporal immediacy is expressed by suffixing the bound clitic particle -इ (-i) or -ही directly to nouns, pronouns, and adverbs.",
        description="Fuses into stems: मै + इ -> मैइ (only I / I myself), आजि + इ -> आजिइ (this very day / today itself), इख + इ -> इखी (right here), सब + इ -> सब्बि (everyone / all of them).",
        pattern="Stem + -इ / -ही [Focus Clitic]",
        examples=[
            GrammarExample("यो काम मैइ करलो।", "यह काम मैं ही करूंगा।", "I myself alone will do this work.", "Clitic focus particle -इ on मै"),
            GrammarExample("ऊ आजिइ ऐगे।", "वह आज ही आ गया।", "He arrived this very day.", "Temporal focus clitic on आजि")
        ],
        counter_examples=["मैं ही करूंगा (Unfused separate Hindi particle 'hee')"],
        linguistic_citation="Verma (1978); Bahuguna (1986)"
    ),
    GrammarRule(
        rule_id="GARH-PRON-005",
        name="Reciprocal Reflexive Construction with आपस मा (aapas ma)",
        category=RuleCategory.PRONOMINAL,
        rule_statement="Reciprocal action ('each other, one another') is constructed with the invariant reflexive locative base आपस मा (aapas ma) placed immediately before the predicate.",
        description="Encodes mutual interchange: वौंले आपस मा बात करी (They spoke to each other), आपस मा झनि लढ़ा (Do not fight amongst yourselves!).",
        pattern="Subject[Plural] + आपस मा + Verb",
        examples=[
            GrammarExample("वौंले आपस मा बात करी।", "उन्होंने आपस में बातचीत की।", "They conversed with each other.", "Reciprocal marker आपस मा"),
            GrammarExample("आपस मा झनि लढ़ा! ", "आपस में मत लड़ो!", "Do not quarrel amongst yourselves!", "Prohibitive reciprocal")
        ],
        counter_examples=["एक-दूसरे से (Hindi reciprocal loan phrase)"],
        linguistic_citation="Joshi (1929), Khasa Family Law; Grierson LSI"
    ),
    GrammarRule(
        rule_id="GARH-HON-003",
        name="Kinship Deictic Cliticization in Oral Speech (ब्वै-जी, दादू-जी, सासू-जी)",
        category=RuleCategory.HONORIFICS,
        rule_statement="Deictic lineage address requires kinship stems to fuse with honorific bound particles -जी (-ji) or hypocoristic vowel shifts when addressing seniors in clan gatherings.",
        description="Observed across formal domestic and ceremonial assemblies: ब्वैजी (revered mother), दादूजी (elder brother), सासूजी (mother-in-law), सयाणाजी (village counselor).",
        pattern="Kinship_Noun + -जी",
        examples=[
            GrammarExample("सासूजी तैं प्रणाम करा।", "सासू जी को प्रणाम करो।", "Pay respectful greetings to honored mother-in-law.", "Ceremonial kinship honorific"),
            GrammarExample("सयाणाजी न फैसला सुणै।", "सयाणा जी ने निर्णय सुनाया।", "The village elder pronounced the verdict.", "Civic honorific suffix")
        ],
        counter_examples=["सासू को प्रणाम करो (Lack of honorific suffixation for elder)"],
        linguistic_citation="Joshi (1929); Pati Ram (1916)"
    )
'''

with open('garhwali/grammar/rules.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace closing of GARHWALI_GRAMMAR_RULES
marker = 'class RuleRegistry:'
parts = text.split(marker)
rules_part = parts[0]
registry_part = marker + parts[1]

# Find last occurrence of ']' in rules_part
last_bracket_idx = rules_part.rfind(']')
if last_bracket_idx != -1:
    before_bracket = rules_part[:last_bracket_idx].rstrip()
    if before_bracket.endswith(')'):
        before_bracket += ',\n'
    updated_rules_part = before_bracket + '\n' + new_rules_text + ']\n\n\n'
    final_content = updated_rules_part + registry_part
    with open('garhwali/grammar/rules.py', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Successfully appended Wave 2 rules to rules.py!")
else:
    print("Error: Could not find closing bracket in rules_part")

