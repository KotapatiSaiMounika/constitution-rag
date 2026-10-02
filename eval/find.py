import json
import re
import sys

def norm(s):
    return re.sub(r"\s+", " ", s).lower()

chunks = json.load(open("data/chunks.json"))
word = norm(sys.argv[1])
for c in chunks:
    t = norm(c["text"])
    i = t.find(word)
    if i != -1:
        print(f"[page {c['page']}] ...{t[max(0, i - 40): i + 120]}...")