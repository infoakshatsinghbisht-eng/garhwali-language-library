import sys

rule_based_code = """

class RuleBasedTranslator:
    \"\"\"Rule-based translator leveraging Garhwali phrase caches, lexicon lookups, and syntactic patterns.\"\"\"

    def __init__(self):
        from ..lexicon import get_lexicon
        self.lexicon = get_lexicon()
        self._build_phrase_cache()

    def _build_phrase_cache(self):
        self._en_phrases: Dict[str, str] = {}
        self._hi_phrases: Dict[str, str] = {}
        
        for p in self.lexicon.get_phrases():
            en_raw = p.get("english", "")
            en_clean = self._clean_key(en_raw)
            en_base = re.sub(r'\\(.*?\\)', '', en_raw).strip()
            en_base_clean = self._clean_key(en_base)
            
            hi_raw = p.get("hindi", "")
            hi_clean = self._clean_key(hi_raw)
            hi_base = re.sub(r'\\(.*?\\)', '', hi_raw).strip()
            hi_base_clean = self._clean_key(hi_base)
            
            gbm = p.get("garhwali", "")
            if en_clean and en_clean not in self._en_phrases:
                self._en_phrases[en_clean] = gbm
            if en_base_clean and en_base_clean not in self._en_phrases:
                self._en_phrases[en_base_clean] = gbm
            if hi_clean and hi_clean not in self._hi_phrases:
                self._hi_phrases[hi_clean] = gbm
            if hi_base_clean and hi_base_clean not in self._hi_phrases:
                self._hi_phrases[hi_base_clean] = gbm

    @staticmethod
    def _clean_key(text: str) -> str:
        text = re.sub(r'[-_]', ' ', text)
        return re.sub(r'[^\\w\\s]', '', text).strip().lower()

    def translate_en_to_gbm(self, text: str) -> Tuple[str, float]:
        clean_input = self._clean_key(text)
        if not clean_input:
            return text, 0.0
        
        if clean_input in self._en_phrases:
            return self._en_phrases[clean_input], 1.0

        w = self.lexicon.lookup(clean_input)
        if w and w.garhwali:
            return w.garhwali, 1.0

        for pattern, replacement in CONVERSATIONAL_EN_GARHWALI_MAP:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                return re.sub(pattern, replacement, text, flags=re.IGNORECASE).strip(), 0.95

        for pattern, replacement in CONVERSATIONAL_HINGLISH_GARHWALI_MAP:
            m = re.search(pattern, text, re.IGNORECASE)
            if m:
                return re.sub(pattern, replacement, text, flags=re.IGNORECASE).strip(), 0.95

        words = text.split()
        translated_words = []
        translated_count = 0
        for wd in words:
            clean_wd = self._clean_key(wd)
            matched = self.lexicon.lookup(clean_wd)
            if matched and matched.garhwali:
                translated_words.append(matched.garhwali)
                translated_count += 1
            else:
                translated_words.append(wd)
        
        conf = (translated_count / len(words)) if words else 0.0
        return " ".join(translated_words), max(0.4, conf)

    def translate_hi_to_gbm(self, text: str) -> Tuple[str, float]:
        clean_input = self._clean_key(text)
        if not clean_input:
            return text, 0.0
        
        if clean_input in self._hi_phrases:
            return self._hi_phrases[clean_input], 1.0

        for hi_key, gbm_val in self._hi_phrases.items():
            if hi_key in clean_input or clean_input in hi_key:
                return gbm_val, 0.9

        for pattern, replacement in CONVERSATIONAL_HI_GARHWALI_MAP:
            m = re.search(pattern, text)
            if m:
                return re.sub(pattern, replacement, text).strip(), 0.95

        w = self.lexicon.lookup_by_hindi(clean_input)
        if w and w.garhwali:
            return w.garhwali, 1.0

        words = text.split()
        translated_words = []
        translated_count = 0
        for wd in words:
            matched = self.lexicon.lookup_by_hindi(wd)
            if matched and matched.garhwali:
                translated_words.append(matched.garhwali)
                translated_count += 1
            else:
                translated_words.append(wd)
        conf = (translated_count / len(words)) if words else 0.0
        return " ".join(translated_words), max(0.4, conf)

    def translate(self, text: str, source: str = "en", target: str = "garhwali", dialect: str = "srinagariya"):
        source = source.lower()
        if source in ("hi", "hin", "hindi"):
            res_text, conf = self.translate_hi_to_gbm(text)
        else:
            res_text, conf = self.translate_en_to_gbm(text)
        
        if dialect and dialect != "srinagariya":
            res_text = apply_dialect(res_text, dialect)
        
        from .engine import TranslationResult
        return TranslationResult(
            text=res_text,
            source_lang=source,
            target_lang=target,
            confidence=conf,
            dialect=dialect
        )

    translate_en_to_kmy = translate_en_to_gbm
    translate_hi_to_kmy = translate_hi_to_gbm
"""

with open('garhwali/translator/rule_based.py', 'r', encoding='utf-8') as f:
    orig = f.read()

if "class RuleBasedTranslator" not in orig:
    with open('garhwali/translator/rule_based.py', 'w', encoding='utf-8') as f:
        f.write(orig + rule_based_code)
    print("RuleBasedTranslator added successfully.")
else:
    print("RuleBasedTranslator already present.")
