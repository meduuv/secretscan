import argparse
from pathlib import Path
from .core import scan

def main():
 p=argparse.ArgumentParser(description='Scan source text for likely secrets'); p.add_argument('path'); a=p.parse_args()
 text=Path(a.path).read_text(encoding='utf-8',errors='replace')
 for f in scan(text): print(f'{a.path}:{f.line}: {f.rule}: {f.value}')
 return 1 if scan(text) else 0
