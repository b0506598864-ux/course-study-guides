"""Repair UTF-8 transcript text misdecoded as Windows-1255; retain source bytes."""
from pathlib import Path
import argparse
import re

p = argparse.ArgumentParser()
p.add_argument('source', type=Path)
p.add_argument('destination', type=Path)
p.add_argument('stem')
a = p.parse_args()
raw = a.source.read_bytes()
text = raw.decode('utf-8-sig')
inverse = {}
for i in range(256):
    try:
        inverse[bytes([i]).decode('cp1255')] = i
    except UnicodeDecodeError:
        inverse[chr(i)] = i
fixed = bytes(inverse[c] for c in text).replace(b'\xd7 ', b'\xd7\xa0').decode('utf-8', errors='strict')
pattern = r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}'
times = re.findall(pattern, text)
assert times == re.findall(pattern, fixed)
assert '\ufffd' not in fixed
assert fixed.startswith('WEBVTT')
a.destination.mkdir(parents=True, exist_ok=True)
for suffix, data in [('-source.vtt', raw), ('-hebrew.vtt', fixed.encode('utf-8-sig'))]:
    path = a.destination / (a.stem + suffix)
    if path.exists() and path.read_bytes() != data:
        raise FileExistsError(path)
    path.write_bytes(data)
print(f'{len(times)} cues: {times[0]} / {times[-1]}')
