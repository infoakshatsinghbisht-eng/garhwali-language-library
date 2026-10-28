# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

candidates = [
    'in.ernet.dli.2015.530003', # Garhwal Ancient And Modern - Rai Pati Ram Bahadur (1916)
    'in.ernet.dli.2015.280083', # Garhwal Ancient And Modern
    'in.ernet.dli.2015.181556', # British Garhwal - A Gazetteer - H.G. Walton (1910)
    'in.ernet.dli.2015.309034', # Shri Uttarakhand Yatra Darshan - Shiv Prasad Dabral
    'languagesofnorth00bailrich', # The languages of the northern Himalayas - Bailey (1908)
    'linguisticstudie00bailrich', # Linguistic studies from the Himalayas - Bailey (1915)
    '1978-pahari-language-a-linguistic-analysis-verma', # Pahari Language: A Linguistic Analysis - Siddheshwar Verma
    '1989-pahari-hindi-shabdkosh-by-haacl_202108', # Pahari-Hindi Shabdkosh
    'in.ernet.dli.2015.46900', # The Himalayan Districts Vol. 1 - Atkinson (1882)
    'wbsl.15712', # Himalayan Districts - Atkinson
    'wbsl.19297', # Himalayan Districts - Atkinson
    'dli.csl.3107', # Tehri Garhwal Gazetteer
    'dli.csl.3036', # Garhwal Gazetteer
    'GarhwalGazetteer', # Garhwal Gazetteer
    'GarhwalPainting', # Garhwal Painting - Mukandi Lal
]

for item_id in candidates:
    url = f"https://archive.org/metadata/{item_id}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            meta = data.get('metadata', {})
            files = data.get('files', [])
            txt_files = [f for f in files if f.get('name', '').endswith('.txt') and not f.get('name', '').endswith('_meta.txt')]
            pdf_files = [f for f in files if f.get('name', '').endswith('.pdf')]
            print(f"ID: {item_id}")
            print(f"  Title: {meta.get('title')}")
            print(f"  Creator: {meta.get('creator')}")
            print(f"  Year: {meta.get('year')}")
            print(f"  Txt files: {[(f['name'], f.get('size')) for f in txt_files]}")
            print(f"  Pdf files: {[(f['name'], f.get('size')) for f in pdf_files[:2]]}")
    except Exception as e:
        print(f"Error {item_id}: {e}")

