import urllib.request
import ssl

ctx = ssl._create_unverified_context()
urls = [
    'https://www.uou.ac.in/sites/default/files/slm/AECC-G-101.pdf',
    'https://www.uou.ac.in/sites/default/files/slm/CGL-101.pdf',
    'https://www.uou.ac.in/sites/default/files/slm/CGL-102.pdf',
    'https://www.uou.ac.in/sites/default/files/slm/CGL-103.pdf',
    'https://www.uou.ac.in/sites/default/files/slm/CGL-104.pdf',
    'https://www.uou.ac.in/sites/default/files/slm/BAHL-101.pdf',
    'https://www.uou.ac.in/sites/default/files/slm/AECC-G-102.pdf',
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            print(f"FOUND: {u} (size: {resp.headers.get('Content-Length')})")
    except Exception as e:
        print(f"Failed {u}: {e}")
