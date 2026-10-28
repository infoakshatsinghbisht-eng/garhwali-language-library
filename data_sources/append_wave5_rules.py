# -*- coding: utf-8 -*-
"""
Appends Wave 5 formal grammar rules to garhwali/grammar/rules.py.
"""

CLEAN_WAVE5_RULES = '''    GrammarRule(
        rule_id="GARH-VRB-013",
        name="Deontic Prescriptive Modality with Participle चाहिन्दो (-ण चाहिन्दो)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Moral obligation, customary necessity, or deontic prescription ('ought to, should, must') is formed with the oblique infinitive in -ण followed by the inflected modal participle चाहिन्दो (M.SG), चाहिन्दी (F.SG), or चाहिन्दा (M.PL), which agrees in gender and number with the grammatical patient/theme.",
        description="Encodes prescriptive duty in customary and social codes: सच बोलण चाहिन्दो (Truth ought to be spoken), रीत निभैण चाहिन्दी (Custom ought to be maintained).",
        pattern="Theme[Gender/Number] + Verb_Root + -ण + चाहिन्दो/चाहिन्दी/चाहिन्दा",
        examples=[
            GrammarExample("सब तैं सच बोलण चाहिन्दो।", "सबको सच बोलना चाहिए।", "Everyone ought to speak the truth.", "Deontic modal participle चाहिन्दो with oblique infinitive बोलण"),
            GrammarExample("सयाणों की बात मान्ण चाहिन्दी।", "बुजुर्गों की बात माननी चाहिए।", "The counsel of elders ought to be obeyed.", "Feminine concord चाहिन्दी agreeing with बात")
        ],
        counter_examples=["बोलना चाहिए (Hindi invariable uninflected modal loan)"],
        dialect_variations={
            "srinagariya": "बोलण चाहिन्दो / चाहिन्दी",
            "tehri": "बोलण चाहिन्दु / चाहिन्दी",
            "salani": "बोलणा चाहिन्दा / चाहिन्दी",
            "rathwali": "बोलण चाहिन्दो"
        },
        linguistic_citation="UP Govt (1919), Kumaun & Garhwal Local Customs; Grierson (1916), LSI Central Pahari"
    ),
    GrammarRule(
        rule_id="GARH-NOM-009",
        name="Gender Diminution Morpheme Alternation (-ओ [M.AUG] -> -ई [F.DIM])",
        category=RuleCategory.NOMINAL_MORPHOLOGY,
        rule_statement="Inanimate topographic and physical objects shift grammatical gender from masculine in -ओ/-आ (augmentative or default large size) to feminine in -ई (diminutive, delicate, or affectionate size) through suffixal vowel alternation.",
        description="A foundational semantic derivation in Central Pahari topography: ढुंगो (large rock/boulder, M) -> ढुंगी (small pebble, F); गधेरो (mountain ravine/torrent, M) -> गधेरी (little brook/rill, F); रस्तो (broad road, M) -> रस्ती (footpath, F).",
        pattern="Noun[-ओ: Masculine/Augmentative] -> Noun[-ई: Feminine/Diminutive]",
        examples=[
            GrammarExample("गधेरो बडी दूर बटी औंदु, पर गधेरी गौं का पाखा मा बग्दी।", "बड़ा नाला बहुत दूर से आता है, पर छोटी नाली गांव के बगल में बहती है।", "The large ravine stream comes from afar, but the little brook flows beside the village.", "Contrasting masculine augmentative गधेरो with feminine diminutive गधेरी"),
            GrammarExample("हाथ मा छोटो ढुंगी उठा।", "हाथ में छोटी कंकड़ी उठाओ।", "Pick up a small pebble in your hand.", "Feminine diminutive ढुंगी derived from masculine ढुंगो")
        ],
        counter_examples=["बड़ा पत्थर और छोटा पत्थर (Analytical Hindi modification without morphological gender shift)"],
        dialect_variations={
            "srinagariya": "ढुंगो -> ढुंगी",
            "tehri": "ढुंगु -> ढुंगी",
            "salani": "ढुंगा -> ढुंगी",
            "rathwali": "ढुंगो -> ढुङ्गी"
        },
        linguistic_citation="Verma (2003), Pahari Dictionary; Chatak (1959), Garhwali Bhasha"
    ),
    GrammarRule(
        rule_id="GARH-SYN-011",
        name="Apophonic Echo-Word Reduplicative Coordination (भात-शूत, पाणी-शाणी)",
        category=RuleCategory.SYNTAX,
        rule_statement="Associative coordination or generalization ('and similar things/etcetera') is formed by apophonic echo reduplication, in which the initial consonant of the base noun is replaced by a sibilant (श-/ष-) or labial (व-/फ-), creating a rhyming echo compound.",
        description="Ubiquitous in colloquial speech and hospitality: भात-शूत (rice and allied dishes), पाणी-शाणी (water and refreshments), काम-शाम (work and related chores).",
        pattern="Base_Noun + Echo_Word[Onset -> श-/व-]",
        examples=[
            GrammarExample("पाहुणा तैं पैली पाणी-शाणी पिवा।", "अतिथि को पहले पानी इत्यादि पिलाओ।", "First serve water and refreshments to the guest.", "Echo reduplicative compound पाणी-शाणी denoting hospitality drinks"),
            GrammarExample("थके-हारे छवां, भात-शूत खावा।", "थक गए हैं, दाल-भात इत्यादि भोजन करो।", "We are exhausted, let us eat rice and related food.", "Echo compound भात-शूत denoting a full meal")
        ],
        counter_examples=["पानी और दूसरी चीजें (Analytical non-reduplicative coordination)"],
        dialect_variations={
            "srinagariya": "भात-शूत / पाणी-शाणी",
            "tehri": "भात-शूत / पाणी-शाणी",
            "salani": "भात-शात / पाणी-शाणी",
            "rathwali": "भात-शूत"
        },
        linguistic_citation="Verma (2003), Pahari Dictionary Part 3; Bailey (1915), Linguistic Studies"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

# Find where GARH-CASE-008 ends
case008_pos = text.find('rule_id="GARH-CASE-008"')
if case008_pos != -1:
    close_paren = text.find("    )", case008_pos)
    if close_paren != -1:
        end_pos = close_paren + len("    )")
        reg_pos = text.find("class RuleRegistry:")
        
        updated = text[:end_pos] + ",\n" + CLEAN_WAVE5_RULES + "\n]\n\n\n" + text[reg_pos:]
        with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
            f.write(updated)
        print("Successfully appended Wave 5 grammar rules to rules.py!")
    else:
        print("close_paren for GARH-CASE-008 not found")
else:
    print("GARH-CASE-008 not found")
