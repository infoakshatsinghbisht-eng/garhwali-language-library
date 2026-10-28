# -*- coding: utf-8 -*-
"""
Fixes Wave 4 rules in garhwali/grammar/rules.py cleanly.
"""

CLEAN_WAVE4_RULES = '''    GrammarRule(
        rule_id="GARH-VRB-012",
        name="Continuative Durative Aspectual Periphrasis with Auxiliary रौणु (-दो रौणु)",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="The continuative or persistent durative aspect denoting uninterrupted continuation of an activity is constructed by the imperfective participle in -दो/-दा/-दी followed by finite forms of the auxiliary रौणु (to remain/stay).",
        description="Encodes continuous unceasing action: बोलदो रौ (keep talking), चलदा रयां (they kept walking), रौंदी रै (she kept crying).",
        pattern="Verb_Root + -दो/-दा/-दी + रौणु[Tense/Aspect/Agreement]",
        examples=[
            GrammarExample("तुम अपणो काम करदा रवां।", "आप अपना काम करते रहिए।", "Please keep continuing your work.", "Polite imperative continuative with auxiliary रवां"),
            GrammarExample("ऊ रातभर पढ्दो रै।", "वह रातभर पढ़ता रहा।", "He kept studying throughout the night.", "Past masculine continuative aspect")
        ],
        counter_examples=["काम करते रहो (Hindi auxiliary loan construction)"],
        dialect_variations={
            "srinagariya": "करदो रौ / करदा रवां",
            "tehri": "करदु रौ / करदा रवां",
            "salani": "करदा रा / करदा रवां",
            "rathwali": "करदो रौ"
        },
        linguistic_citation="Grierson (1916), Central Pahari; Verma (2003), Pahari Dictionary Vol. 1"
    ),
    GrammarRule(
        rule_id="GARH-NOM-008",
        name="Vocative Plural Interpellative Clitic (-हो / -ओ) in Communal Assembly",
        category=RuleCategory.NOMINAL_MORPHOLOGY,
        rule_statement="Direct communal address and interpellation in village councils (sayana-sabha) or festive gatherings attaches the vocative plural bound marker -हो or -ओ to the direct nominal stem, triggering penultimate vowel lengthening.",
        description="Preserved in oral assemblies, panchayats, and bardic calls: भाइहो (O brothers!), सयाणहो (O honored elders!), गौंत्यारो (O fellow villagers!).",
        pattern="Noun_Stem + -हो / -ओ",
        examples=[
            GrammarExample("भाइहो! सब मिलिक फैसला करा।", "भाइयो! सब मिलकर निर्णय करो।", "O brothers! Come together and decide.", "Communal vocative marker -हो"),
            GrammarExample("सयाणहो! हमरी विनती सुणा।", "हे सयाणो! हमारी प्रार्थना सुनो।", "O village elders! Listen to our humble petition.", "Council vocative address")
        ],
        counter_examples=["भाइयों (Standard Hindi vocative loan without -हो)"],
        dialect_variations={
            "srinagariya": "भाइहो / सयाणहो",
            "tehri": "भैयों / सयाणों",
            "salani": "भाइयो / सयाणा",
            "rathwali": "भाइहो"
        },
        linguistic_citation="Stowell (1916), Kumaun & Garhwali Rulings; Dabral (1965), Bhotantik Alaknanda"
    ),
    GrammarRule(
        rule_id="GARH-SYN-010",
        name="Conditional Consequential Clause Linking with तबे / तौ (Condition-Nexus)",
        category=RuleCategory.SYNTAX,
        rule_statement="In conditional complex sentences, the protasis (condition) introduced optionally by यदि or agar is obligatorily linked to the apodosis (consequence) by the indigenous Pahari consequential discourse particles तबे (only then) or तौ (then).",
        description="Connects condition to consequence: घाम लगलो तबे बरखा रुकली (Only when the sun comes out will rain cease).",
        pattern="[Protasis: Condition + Verb] + तबे / तौ + [Apodosis: Consequence + Verb]",
        examples=[
            GrammarExample("घाम लगलो तबे बरखा रुकली।", "धूप निकलेगी तभी बारिश रुकेगी।", "Only when the sun comes out will the rain cease.", "Conditional consequential nexus marker तबे"),
            GrammarExample("तुम औला तौ हम बजार जाला।", "तुम आओगे तो हम बाजार जाएंगे।", "If you come, then we shall go to the market.", "Consequential marker तौ")
        ],
        counter_examples=["धूप निकलेगी तो ही बारिश रुकेगी (Hindi focal loan syntax)"],
        dialect_variations={
            "srinagariya": "तबे / तौ",
            "tehri": "तबि / तौ",
            "salani": "तब / ता",
            "rathwali": "तबे / तौ"
        },
        linguistic_citation="Stowell (1916), Customary Law Rulings; Bailey (1915), Linguistic Studies"
    ),
    GrammarRule(
        rule_id="GARH-CASE-008",
        name="Emphatic Source Ablative Suffixation (-बटीक / -बिटिन Compound Ablation)",
        category=RuleCategory.CASE_SYSTEM,
        rule_statement="To emphasize absolute provenance, origin from the interior of an entity, or direct temporal commencement, the simple ablative postposition बटी takes an emphatic bound clitic -क or fuses into बिटिन / बटीन.",
        description="Emphasizes exact starting point or origin: बदरीनाथ बटीक (all the way from Badrinath), सबेर बिटिन (since early morning).",
        pattern="Noun[OBL] + -बटीक / -बिटिन",
        examples=[
            GrammarExample("ऊ बदरीनाथ बटीक सीधा घर ऐ गे।", "वह बदरीनाथ से सीधे घर आ गया।", "He returned home directly all the way from Badrinath.", "Emphatic ablative marker बटीक"),
            GrammarExample("सबेर बिटिन बरखा हुणी च।", "सुबह से ही वर्षा हो रही है।", "It has been raining continuously since early morning.", "Temporal source ablative बिटिन")
        ],
        counter_examples=["बदरीनाथ से (Unmarked analytical Hindi postposition)"],
        dialect_variations={
            "srinagariya": "बटीक / बिटिन",
            "tehri": "बटिक / बिटन",
            "salani": "बटिन / सेन",
            "rathwali": "बटीक / बिटिन"
        },
        linguistic_citation="Verma (2003), Pahari Dictionary; Grierson (1916), LSI Central Pahari"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

# Find where GARH-CONC-004 ends
conc004_pos = text.find('rule_id="GARH-CONC-004"')
if conc004_pos != -1:
    close_paren = text.find("    )", conc004_pos)
    if close_paren != -1:
        end_pos = close_paren + len("    )")
        reg_pos = text.find("class RuleRegistry:")
        
        updated = text[:end_pos] + ",\n" + CLEAN_WAVE4_RULES + "\n]\n\n\n" + text[reg_pos:]
        with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
            f.write(updated)
        print("Cleaned up Wave 4 grammar rules in rules.py!")

