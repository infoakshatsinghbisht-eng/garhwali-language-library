import os
import sys
import json
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = os.path.join(os.path.dirname(__file__), 'raw_texts')
os.makedirs(DEST_DIR, exist_ok=True)

ITEMS = [
    {
        'id': 'ezqp-garhwali-bhasha-aur-uska-sahitya-by-haridatta-bhat',
        'short': 'haridatta_bhatt_garhwali_bhasha_aur_sahitya_1976',
        'title': 'Garhwali Bhasha Aur Uska Sahitya',
        'author': 'Dr. Haridatta Bhatta Shailesh',
        'year': 1976
    },
    {
        'id': 'in.ernet.dli.2015.263968',
        'short': 'govind_chatak_garhwali_bhasha_1959',
        'title': 'Garhwali Bhasha',
        'author': 'Dr. Govind Chatak',
        'year': 1959
    },
    {
        'id': 'dli.ernet.426855',
        'short': 'govind_chatak_gadwali_lok_gathayen_1958',
        'title': 'Gadwali Lok Gathayen',
        'author': 'Dr. Govind Chatak',
        'year': 1958
    },
    {
        'id': 'in.ernet.dli.2015.481404',
        'short': 'govind_chatak_garhwali_lok_geet_1956',
        'title': 'Garhwali Lok Geet',
        'author': 'Govind Chatak',
        'year': 1956
    },
    {
        'id': 'in.ernet.dli.2015.426866',
        'short': 'shyam_chand_negi_gadwali_sahitya_1954',
        'title': 'Gadwali Sahitya Ki Bhumika',
        'author': 'Shyam Chand Negi',
        'year': 1954
    },
    {
        'id': 'in.ernet.dli.2015.481134',
        'short': 'shanti_chaudhary_garhwali_lokkala_1994',
        'title': 'Garhwali Lokkala Aur Loksahitya Ka Tulnatmak Anusilan',
        'author': 'Shanti Chaudhary',
        'year': 1994
    },
    {
        'id': 'ycbf_madhya-pahadi-bhasha-garhwali-kumauni-ka-anushilan-aur-uska-hindi-se-samban',
        'short': 'gunanand_juyal_madhya_pahadi_bhasha_1967',
        'title': 'Madhya Pahadi Bhasha Garhwali Kumauni Ka Anushilan',
        'author': 'Dr. Gunanand Juyal',
        'year': 1967
    },
    {
        'id': 'cu31924089930774',
        'short': 'upreti_proverbs_folklore_garhwal_1894',
        'title': 'Proverbs & Folklore of Kumaun and Garhwal',
        'author': 'Pandit Ganga Datt Upreti',
        'year': 1894
    },
    {
        'id': 'in.ernet.dli.2015.32110',
        'short': 'grierson_lsi_vol9_pt4_garhwal_1916',
        'title': 'Linguistic Survey of India: Central Pahari / Garhwali',
        'author': 'Sir George Abraham Grierson',
        'year': 1916
    },
    {
        'id': 'in.ernet.dli.2015.532407',
        'short': 'oakley_gairola_himalayan_folklore_1935',
        'title': 'Himalayan Folklore',
        'author': 'Rev. E.S. Oakley and Tara Dutt Gairola',
        'year': 1935
    }
]

def get_best_file(metadata):
    files = metadata.get('files', [])
    # Preference: _djvu.txt, .txt, .pdf (if < 30MB)
    txt_file = None
    pdf_file = None
    for f in files:
        name = f.get('name', '')
        size = int(f.get('size', 0) or 0)
        fmt = f.get('format', '')
        if name.endswith('_djvu.txt') or fmt == 'DjVuTXT':
            return f, 'txt'
        elif name.endswith('.txt') and not name.endswith('_meta.txt') and not name.endswith('_files.xml'):
            if not txt_file or size > int(txt_file.get('size', 0) or 0):
                txt_file = f
        elif name.endswith('.pdf') and size > 0:
            if not pdf_file or (size < 40*1024*1024 and size > int(pdf_file.get('size', 0) or 0)):
                pdf_file = f
    if txt_file:
        return txt_file, 'txt'
    if pdf_file:
        return pdf_file, 'pdf'
    return None, None

import ssl

def download_file(url, out_path):
    print(f"Downloading from {url} to {out_path} ...", flush=True)
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
        with open(out_path, 'wb') as out_f:
            total = 0
            while True:
                chunk = resp.read(65536)
                if not chunk:
                    break
                out_f.write(chunk)
                total += len(chunk)
                if total % (1024*1024*5) == 0:
                    print(f"  ... {total / (1024*1024):.1f} MB downloaded", flush=True)
    print(f"  Done ({total / 1024:.1f} KB).", flush=True)

results = []

for item in ITEMS:
    ident = item['id']
    short = item['short']
    print(f"\nProcessing {ident} ({item['title']})...")
    meta_url = f"https://archive.org/metadata/{ident}"
    try:
        ctx = ssl._create_unverified_context()
        req = urllib.request.Request(meta_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            data = json.loads(resp.read().decode('utf-8'))
        
        f, ftype = get_best_file(data)
        if not f:
            print(f"No suitable file found for {ident}")
            continue
        
        fname = f['name']
        fsize = int(f.get('size', 0) or 0)
        ext = '.txt' if ftype == 'txt' else '.pdf'
        out_file = os.path.join(DEST_DIR, f"{short}{ext}")
        
        # Check if already exists and has size
        if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
            print(f"Already downloaded: {out_file} ({os.path.getsize(out_file)} bytes)")
            item['local_file'] = out_file
            item['file_size'] = os.path.getsize(out_file)
            item['file_type'] = ext
            results.append(item)
            continue
            
        file_url = f"https://archive.org/download/{ident}/{urllib.parse.quote(fname)}"
        download_file(file_url, out_file)
        item['local_file'] = out_file
        item['file_size'] = os.path.getsize(out_file)
        item['file_type'] = ext
        results.append(item)
    except Exception as e:
        print(f"Error downloading {ident}: {e}")

with open(os.path.join(DEST_DIR, 'downloaded_books_index.json'), 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDownload summary saved to downloaded_books_index.json.")
