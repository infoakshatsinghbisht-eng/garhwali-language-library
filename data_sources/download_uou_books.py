import os
import sys
import ssl
import urllib.request
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

DEST_DIR = os.path.join(os.path.dirname(__file__), 'raw_texts')
os.makedirs(DEST_DIR, exist_ok=True)

UOU_BOOKS = [
    {
        'url': 'https://www.uou.ac.in/sites/default/files/slm/AECC-G-101.pdf',
        'pdf_name': 'uou_aecc_g_101.pdf',
        'txt_name': 'uou_aecc_g_101_text.txt',
        'title': 'Garhwali Bhasha Aur Sahitya (AECC-G-101)',
        'author': 'Uttarakhand Open University',
        'year': 2020,
        'genre': 'Academic Course Textbook'
    },
    {
        'url': 'https://www.uou.ac.in/sites/default/files/slm/CGL-102.pdf',
        'pdf_name': 'uou_cgl_102.pdf',
        'txt_name': 'uou_cgl_102_text.txt',
        'title': 'Chayanit Garhwali Gadya (CGL-102)',
        'author': 'Uttarakhand Open University',
        'year': 2021,
        'genre': 'Garhwali Prose & Literature'
    },
    {
        'url': 'https://www.uou.ac.in/sites/default/files/slm/CGL-103.pdf',
        'pdf_name': 'uou_cgl_103.pdf',
        'txt_name': 'uou_cgl_103_text.txt',
        'title': 'Garhwali Lok Sahitya (CGL-103)',
        'author': 'Uttarakhand Open University',
        'year': 2021,
        'genre': 'Folk Literature, Epics & Songs'
    },
    {
        'url': 'https://www.uou.ac.in/sites/default/files/slm/CGL-104.pdf',
        'pdf_name': 'uou_cgl_104.pdf',
        'txt_name': 'uou_cgl_104_text.txt',
        'title': 'Garhwali Bhasha Evam Vyakaran (CGL-104)',
        'author': 'Uttarakhand Open University',
        'year': 2021,
        'genre': 'Grammar, Morphology & Lexicon'
    }
]

ctx = ssl._create_unverified_context()

for b in UOU_BOOKS:
    pdf_path = os.path.join(DEST_DIR, b['pdf_name'])
    txt_path = os.path.join(DEST_DIR, b['txt_name'])
    
    print(f"\nProcessing {b['title']}...")
    if not os.path.exists(pdf_path) or os.path.getsize(pdf_path) < 1000:
        print(f"Downloading {b['url']} -> {pdf_path} ...", flush=True)
        req = urllib.request.Request(b['url'], headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp, open(pdf_path, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {b['pdf_name']} ({os.path.getsize(pdf_path)} bytes).", flush=True)
    else:
        print(f"PDF already exists: {pdf_path}", flush=True)
        
    # Extract text using pypdf
    if not os.path.exists(txt_path) or os.path.getsize(txt_path) < 1000:
        print(f"Extracting text to {txt_path} ...", flush=True)
        reader = pypdf.PdfReader(pdf_path)
        extracted_pages = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ''
            extracted_pages.append(f"\n--- Page {i+1} ---\n" + text)
        full_text = "\n".join(extracted_pages)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"Extracted {len(reader.pages)} pages ({len(full_text)} chars) -> {txt_path}", flush=True)
    else:
        print(f"Extracted text already exists: {txt_path}", flush=True)

print("\nAll UOU books downloaded and extracted successfully!")
