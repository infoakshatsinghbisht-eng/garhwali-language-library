# -*- coding: utf-8 -*-
"""Garhwali Voice Synthesis & SSML Generator."""

import math
from typing import Dict, List, Any, Optional, Tuple, Union, Set
from ..phonetics import syllables, devanagari_to_latin

class GarhwaliVoiceSynthesizer:
    @staticmethod
    def get_speech_ssml(text: str, rate: str = "medium", pitch: str = "+5%") -> str:
        return f"""<speak>
  <prosody rate="{rate}" pitch="{pitch}">
    <lang xml:lang="hi-IN">{text}</lang>
  </prosody>
</speak>"""

    @staticmethod
    def get_phonetic_script(text: str) -> Dict[str, Any]:
        return {
            "devanagari": text,
            "roman": devanagari_to_latin(text),
            "syllables": syllables(text),
            "language": "garhwali"
        }

    @staticmethod
    def generate_pcm_wav(duration_seconds: float = 0.5, freq: float = 440.0) -> bytes:
        import struct
        sample_rate = 16000
        num_samples = int(sample_rate * duration_seconds)
        data = bytearray()
        for i in range(num_samples):
            t = float(i) / sample_rate
            env = math.sin(math.pi * t / duration_seconds)
            val = int(32767.0 * 0.6 * math.sin(2.0 * math.pi * freq * t) * env)
            data.extend(struct.pack("<h", max(-32768, min(32767, val))))
        
        # WAV header
        header = bytearray(b'RIFF')
        header.extend(struct.pack('<I', 36 + len(data)))
        header.extend(b'WAVEfmt ')
        header.extend(struct.pack('<I', 16))
        header.extend(struct.pack('<H', 1))
        header.extend(struct.pack('<H', 1))
        header.extend(struct.pack('<I', sample_rate))
        header.extend(struct.pack('<I', sample_rate * 2))
        header.extend(struct.pack('<H', 2))
        header.extend(struct.pack('<H', 16))
        header.extend(b'data')
        header.extend(struct.pack('<I', len(data)))
        return bytes(header + data)
