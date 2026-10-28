# -*- coding: utf-8 -*-
"""
Appends Wave 8 formal grammar rules to garhwali/grammar/rules.py:
1. GARH-NOM-010: Spatial Deictic Distal-Proximal Adjective Inversion (पल्लो vs वल्लो)
2. GARH-VRB-016: Sudden-Inceptive Compound Verb Formation with Auxiliary -बैठण / -उठण
3. GARH-SYN-014: Direct Speech Quotative Frame with Clause-Final बोलिक (Reportative Particle)
"""

import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WAVE8_RULES = '''    GrammarRule(
        rule_id="GARH-NOM-010",
        name="Spatial Deictic Distal-Proximal Adjective Inversion (पल्लो vs वल्लो)",
        category=RuleCategory.NOMINAL_MORPHOLOGY,
        rule_statement="Spatial deixis across mountain gorges and river valleys contrasts the proximal adjective वल्लो ('on this near side/ridge') with the distal adjective पल्लो ('on that far side/ridge'), which obligatorily decline for gender and number (वल्लो/वल्ली/वल्ला vs पल्लो/पल्ली/पल्ला) and govern locative postpositions.",
        description="Fundamental to Himalayan geography: वल्ला पाखा (on this near hillside), पल्ला डांडा मा (on that farther mountain crest), पल्ली धार (the ridge across the gorge).",
        pattern="[वल्लो/पल्लो][Gender/Number] + Toponym/Noun + [Locative Postposition]",
        examples=[
            GrammarExample("वल्ला गौं का लोग पल्ला डांडा मा घास काटदा।", "इस गांव के लोग उस पार के पहाड़ पर घास काटते हैं।", "The people of this near village cut grass on the farther mountain ridge.", "Contrasting proximal वल्ला with distal पल्ला"),
            GrammarExample("पल्ली धार मा हिंवाळ चमकणू च।", "उस पार की चोटी पर बर्फ चमक रही है।", "The snow is glistening on the opposite ridge across the gorge.", "Feminine distal adjective पल्ली modifying ridge noun धार")
        ],
        counter_examples=["इस तरफ और उस तरफ (Analytical Hindi directional adverbs without declinable Pahari deictic adjectives)"],
        dialect_variations={
            "srinagariya": "वल्लो / पल्लो",
            "tehri": "वल्लो / पल्लो",
            "salani": "वल्ला / पल्ला",
            "rathwali": "वल्लो / पल्लो"
        },
        linguistic_citation="Grierson (1916), LSI Central Pahari; Ibbotson (1933), Garhwal Settlement"
    ),
    GrammarRule(
        rule_id="GARH-VRB-016",
        name="Sudden-Inceptive Compound Verb Formation with Auxiliary -बैठण / -उठण",
        category=RuleCategory.VERBAL_MORPHOLOGY,
        rule_statement="Sudden, involuntary, or impulsive action is expressed by a compound verb comprising the root or conjunctive stem followed by the inflected auxiliary बैठण (denoting sudden regretful/uncontrollable action) or उठण (denoting explosive/inceptive emergence), agreeing with the subject in intransitive clauses or the patient in transitive past.",
        description="Encodes sudden mountain accidents or spontaneous reactions: हूँ रोई बैठ्युँ (I burst out crying suddenly / couldn't help weeping), चट्टान सरकी उठी (The rock suddenly slid away).",
        pattern="Verb_Root + बैठण/उठण[Tense/Person/Gender]",
        examples=[
            GrammarExample("अन्धेर मा बाटू भटकी बैठ्युँ।", "अंधेरे में रास्ता भटक बैठा।", "In the pitch-black darkness I inadvertently lost my way.", "Compound verb भटकी बैठ्युँ expressing sudden inadvertent action"),
            GrammarExample("गधेरा मा पाणी उफणी उठ्यो।", "गधेरे में पानी अचानक उफान पर आ गया।", "The stream water suddenly surged in spate.", "Inceptive surge denoted by compound उफणी उठ्यो")
        ],
        counter_examples=["रास्ता भूल गया (Standard non-compound declarative)"],
        dialect_variations={
            "srinagariya": "भटकी बैठ्युँ",
            "tehri": "भटकी बैठुं",
            "salani": "भटकी बैठा",
            "rathwali": "भटकी बैठ्युँ"
        },
        linguistic_citation="Grierson (1916), LSI Central Pahari; Bhandari (1946), Snow Balls of Garhwal"
    ),
    GrammarRule(
        rule_id="GARH-SYN-014",
        name="Direct Speech Quotative Frame with Clause-Final बोलिक (Reportative Particle)",
        category=RuleCategory.SYNTAX,
        rule_statement="Direct quoted speech, folk dialogue, or reported intentions are syntactically closed by the clause-final reportative complementizer बोलिक (conjunctive participle of बोलण 'having spoken / saying'), preceding or governing the matrix cognitive/communicative verb.",
        description="Standard in Garhwali oral ballads (Pawadas), folk tales, and everyday testimony: 'हूँ भोल औंलो' बोलिक भागि ग्ये ('I will come tomorrow', saying this he departed), 'पानी नि च' बोलिक मना करै ('There is no water', saying which he refused).",
        pattern="[Quoted_Clause] + बोलिक + Matrix_Verb",
        examples=[
            GrammarExample("'हूँ भोल श्रीनगर जांलो' बोलिक चलि ग्ये।", "'मैं कल श्रीनगर जाऊंगा' कहकर चला गया।", "Saying 'I will go to Srinagar tomorrow', he set off.", "Quoted direct speech closed by reportative participle बोलिक"),
            GrammarExample("'जाड़ों मा डांडा झनि जाया' बोलिक सयाणों न चेताया।", "'सर्दियों में पहाड़ों पर मत जाना' कहकर बुजुर्गों ने चेतावनी दी।", "Saying 'Do not go to the high peaks in winter', the elders warned.", "Reported elder warning framed by बोलिक")
        ],
        counter_examples=["कि मैं जाऊंगा (Hindi subordinating conjunction कि without native Pahari conjunctive quotative particle)"],
        dialect_variations={
            "srinagariya": "बोलिक",
            "tehri": "बोलिकी",
            "salani": "बोलीक",
            "rathwali": "बोलिक"
        },
        linguistic_citation="Grierson (1916), LSI Central Pahari; Chatak (1958), Gadwali Lok Gathayen; Bhandari (1946)"
    )
'''

with open("garhwali/grammar/rules.py", "r", encoding="utf-8") as f:
    text = f.read().replace("\r\n", "\n")

conc005_pos = text.find('rule_id="GARH-CONC-005"')
if conc005_pos == -1:
    print("ERROR: Could not find GARH-CONC-005")
    sys.exit(1)

close_paren = text.find("    )", conc005_pos)
if close_paren == -1:
    print("ERROR: Could not find end of GARH-CONC-005")
    sys.exit(1)

end_pos = close_paren + len("    )")
reg_pos = text.find("class RuleRegistry:")

updated = text[:end_pos] + ",\n" + WAVE8_RULES + "\n]\n\n\n" + text[reg_pos:]

with open("garhwali/grammar/rules.py", "w", encoding="utf-8") as f:
    f.write(updated)

print("Appended Wave 8 rules to garhwali/grammar/rules.py successfully!")

