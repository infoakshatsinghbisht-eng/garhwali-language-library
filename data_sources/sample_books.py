import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
RAW_DIR = os.path.join(os.path.dirname(__file__), 'raw_texts')

for fname in os.listdir(RAW_DIR):
    if not fname.endswith('.txt'):
        continue
    fpath = os.path.join(RAW_DIR, fname)
    size = os.path.getsize(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        # Read first 1000 chars
        sample = f.read(800).replace('\n', ' ')
    print(f"=== {fname} ({size/1024:.1f} KB) ===")
    print(sample[:300])
    print()
