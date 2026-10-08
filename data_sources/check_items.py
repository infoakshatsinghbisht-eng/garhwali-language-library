import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ids = [
    'in.ernet.dli.2015.263968',  # Garhwali Bhasha - Govind Chatak
    'in.ernet.dli.2015.426866',  # Gadwali Sahitya Ki Bhumika - Shyam Chand Negi
    'in.ernet.dli.2015.481134',  # Garhwali Lokkala Aur Loksahitya - Shanti Chaudhary
    'cu31924089930774',          # Proverbs & Folklore of Kumaun and Garhwal - Upreti
    'in.ernet.dli.2015.32110',   # LSI Vol 9 Pt 4 (Garhwali section) - Grierson
    'in.ernet.dli.2015.532407',  # Himalayan Folklore - Oakley & Gairola
]

for identifier in ids:
    url = f"https://archive.org/metadata/{identifier}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            meta = data.get('metadata', {})
            files = data.get('files', [])
            print(f"=== {identifier} ===")
            print(f"Title: {meta.get('title')}")
            print(f"Creator: {meta.get('creator')}")
            print(f"Year: {meta.get('year') or meta.get('date')}")
            
            # Look for pdf, txt, or djvu_txt
            txt_files = [f for f in files if f.get('name', '').endswith('.txt') or f.get('name', '').endswith('_djvu.txt') or f.get('name', '').endswith('.pdf')]
            for f in txt_files[:5]:
                print(f"  File: {f.get('name')} | Size: {f.get('size')} | Format: {f.get('format')}")
    except Exception as e:
        print(f"Error for {identifier}: {e}")
