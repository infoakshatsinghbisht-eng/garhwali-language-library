import json

with open('garhwali/lexicon/data/words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

new_entries = [
    {'garhwali': 'च', 'hindi': 'है', 'english': 'is (present copula)', 'pos': 'verb', 'gender': 'M', 'category': 'copula', 'dialect_variants': {'srinagariya': 'च', 'rathwali': 'छी', 'tehri': 'छ', 'salani': 'छ'}},
    {'garhwali': 'छन', 'hindi': 'हैं', 'english': 'are (plural present copula)', 'pos': 'verb', 'gender': 'M', 'category': 'copula', 'dialect_variants': {'srinagariya': 'छन', 'rathwali': 'छिन', 'tehri': 'छिन', 'salani': 'छन'}},
    {'garhwali': 'रोटी-शोटी', 'hindi': 'रोटी आदि (प्रतिध्वनि शब्द)', 'english': 'bread and other food (echo reduplication)', 'pos': 'noun', 'gender': 'F', 'category': 'reduplication', 'dialect_variants': {'srinagariya': 'रोटी-शोटी', 'rathwali': 'रोटी-शोटी', 'tehri': 'रोटी-शोटी', 'salani': 'रोटी-शोटी'}},
    {'garhwali': 'पाणी-शाणी', 'hindi': 'पानी आदि', 'english': 'water etc. (echo reduplication)', 'pos': 'noun', 'gender': 'M', 'category': 'reduplication', 'dialect_variants': {'srinagariya': 'पाणी-शाणी', 'rathwali': 'पाणी-शाणी', 'tehri': 'पाणी-शाणी', 'salani': 'पाणी-शाणी'}},
    {'garhwali': 'सूंघणु', 'hindi': 'सूँघना / गंध लेना', 'english': 'to smell / sense fragrance', 'pos': 'verb', 'gender': 'M', 'category': 'sense', 'dialect_variants': {'srinagariya': 'सूंघणु', 'rathwali': 'सूंघणु', 'tehri': 'सूंघणु', 'salani': 'सूंघणु'}},
    {'garhwali': 'छुनुक-छुनुक', 'hindi': 'पायल की छनछनाहट', 'english': 'sound of tinkling bells/anklets', 'pos': 'noun', 'gender': 'F', 'category': 'sound', 'dialect_variants': {'srinagariya': 'छुनुक-छुनुक', 'rathwali': 'छुनुक-छुनुक', 'tehri': 'छुनुक-छुनुक', 'salani': 'छुनुक-छुनुक'}},
    {'garhwali': 'पकाउणु', 'hindi': 'पकाना / भोजन तैयार करना', 'english': 'to cook / prepare food', 'pos': 'verb', 'gender': 'M', 'category': 'cooking', 'dialect_variants': {'srinagariya': 'पकाउणु', 'rathwali': 'पकाउणु', 'tehri': 'पकाउणु', 'salani': 'पकाउणु'}},
    {'garhwali': 'दौड़', 'hindi': 'दौड़ / भाग', 'english': 'running / race / sprint', 'pos': 'noun', 'gender': 'F', 'category': 'action', 'dialect_variants': {'srinagariya': 'दौड़', 'rathwali': 'दौड़', 'tehri': 'दौड़', 'salani': 'दौड़'}}
]

seen = {w['garhwali'].strip() for w in words}
for e in new_entries:
    if e['garhwali'].strip() not in seen:
        words.append(e)

with open('garhwali/lexicon/data/words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

cats = set(w.get('category', '') for w in words)
print('Total categories now:', len(cats))
print('Total words now:', len(words))
