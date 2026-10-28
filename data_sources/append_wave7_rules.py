# -*- coding: utf-8 -*-
"""
Appends Wave 7 formal grammar rules to garhwali/grammar/rules.py:
1. GARH-VRB-015: Habitual-Iterative Aspectual Suffixation with Participle रन्- (-दो रन्-)
2. GARH-SYN-013: Additive-Inclusive Focus Enclitic -ई / -यी ('Even / Also / Too')
3. GARH-CONC-005: Partitive-Genitive Quantitative Concord with Indefinite Quantifiers (सबुकी, थ्वैकी)
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WAVE7_RULES = '''    GrammarRule(
        rule_id="GARH-VRB-015",
        name="Habitual-Iterative Aspectual Suffixation with Participle रन्- (-दो रन्-)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Habitual, iterative, or sustained continuous aspect ('keeps on doing / habitually does') is formed by combining the imperfective participle in -दो / -दी / -दा with the inflected auxiliary verb stem रन्- (to remain/continue), agreeing in gender and number with the subject.",
        description="Encodes ongoing customs, environmental processes, or perpetual pastoral habits: नदी बग्दी रन्दी (The river keeps on flowing), पहाड़ी लोग काम करदा रन्दा (The mountain folk keep on working diligently).",
        pattern="Subject[Gender/Number] + Verb_Root + -दो/-दी/-दा + रन्-[Tense/Concord]",
        examples=[
            GrammarExample("गंगा नदी रात-दिन बग्दी रन्दी।", "गंगा नदी रात-दिन बहती रहती है।", "The river Ganga keeps on flowing day and night.", "Feminine singular imperfective participle बग्दी paired with auxiliary रन्दी"),
            GrammarExample("पहाड़ी लोग सदा मेहनत करदा रन्दा।", "पहाड़ी लोग सदा मेहनत करते रहते हैं।", "Mountain people always keep on working hard.", "Masculine plural participle concord करदा with auxiliary रन्दा")
        ],
        counter_examples=["बहती रहती है (Hindi analytical compound without Central Pahari participle concord)"],
        dialect_variations={
            "srinagariya": "बग्दी रन्दी / करदा रन्दा",
            "tehri": "बग्दी रंदी / करदा रंदा",
            "salani": "बगदी रंदी / करदा रंदा",
            "rathwali": "बग्दी रन्दी"
        },
        linguistic_citation="Shrestha (2000), A Grammar of Pahari; LSI Pahari Survey (2023); Grierson (1916), LSI Central Pahari"
    ),
    GrammarRule(
        rule_id="GARH-SYN-013",
        name="Additive-Inclusive Focus Enclitic -ई / -यी ('Even / Also / Too')",
        category=RuleCategory.SYNTAX,
        rule_statement="Additive focus or scalar inclusion ('even / also / too') is encoded by suffixing the emphatic focus enclitic -ई (after consonants) or -यी (after vowels) directly to nominals, pronouns, or postpositions, distinct from the coordinating conjunction अर ('and').",
        description="Direct morphological cognate of Hindi भी, but functioning as an agglutinative enclitic in Central Pahari: तूँई (even you / you too), ऊँई (even they), बर्फ माई (even in the snow).",
        pattern="Word_Stem + -ई / -यी (Scalar Focus Enclitic)",
        examples=[
            GrammarExample("कठिन चढ़ाई मा तूँई जा सकदी।", "कठिन चढ़ाई में तुम भी जा सकती हो।", "Even you can go up the arduous climb.", "Pronominal host तूँ taking scalar focus enclitic -ई"),
            GrammarExample("जाड़ों मा हिमताल माई बर्फ जम जांद।", "सर्दियों में हिमताल में भी बर्फ जम जाती है।", "In winter, ice freezes even upon the glacial tarn.", "Locative postposition मा taking emphatic focus enclitic -ई")
        ],
        counter_examples=["तुम भी (Hindi invariant analytical focus particle)"],
        dialect_variations={
            "srinagariya": "तूँई / माई",
            "tehri": "तुई / मई",
            "salani": "तूँई / माई",
            "rathwali": "तूँई"
        },
        linguistic_citation="Shrestha (2000), A Grammar of Pahari; Chatak (1959), Garhwali Bhasha"
    ),
    GrammarRule(
        rule_id="GARH-CONC-005",
        name="Partitive-Genitive Quantitative Concord with Indefinite Quantifiers (सबुकी, थ्वैकी)",
        category=RuleCategory.CONCORD_AGREEMENT,
        rule_statement="When an indefinite quantifier or collective pronominal base (सबु- 'all', थ्वै- 'some') heads a partitive or collective nominal phrase, the genitive postposition inflects with feminine diminutive concord in -की to express generalized collective totality or human consensus.",
        description="Ubiquitous in village customary deliberations and council consensus: सबुकी राय (everyone's consensus / collective opinion), थ्वैकी बात (some people's view).",
        pattern="Quantifier[Oblique] + -की + Noun[F.SG: Collective Consensus]",
        examples=[
            GrammarExample("गाँव मा सबुकी राय से फैसला ह्वै।", "गांव में सबकी राय से निर्णय हुआ।", "The decision was made with everyone's collective consensus in the village.", "Oblique quantifier सबु- taking feminine genitive marker -की with राय"),
            GrammarExample("थ्वैकी मदद लेण मा संकोच नि करौ।", "कुछ लोगों की मदद लेने में संकोच मत करो।", "Do not hesitate to accept the help of some people.", "Oblique indefinite base थ्वै- taking collective genitive -की")
        ],
        counter_examples=["सबका निर्णय (Masculine invariant default without collective feminine concord)"],
        dialect_variations={
            "srinagariya": "सबुकी राय",
            "tehri": "सबुकि राय",
            "salani": "सबकी राय",
            "rathwali": "सबुकी राय"
        },
        linguistic_citation="LSI Pahari Survey (2023); Juyal (1967), Madhya Pahadi Bhasha"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

case009_pos = text.find('rule_id="GARH-CASE-009"')
if case009_pos == -1:
    print("ERROR: Could not find GARH-CASE-009")
    sys.exit(1)

close_paren = text.find("    )", case009_pos)
if close_paren == -1:
    print("ERROR: Could not find end of GARH-CASE-009")
    sys.exit(1)

end_pos = close_paren + len("    )")
reg_pos = text.find("class RuleRegistry:")

updated = text[:end_pos] + ",\n" + WAVE7_RULES + "\n]\n\n\n" + text[reg_pos:]

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(updated)

print("Appended Wave 7 rules to garhwali/grammar/rules.py successfully!")

