import json
import re

def norm(s):
    return re.sub(r"\s+", " ", s).lower()

chunks = json.load(open("data/chunks.json"))

for item in json.load(open("eval/questions.json")):
    p = norm(item["must_contain"])
    pages = sorted({c["page"] for c in chunks if p in norm(c["text"])})
    if not pages:
        status = "NOT FOUND"
    elif any(x <= 10 for x in pages):
        status = "TOC HIT"
    elif len(pages) > 3:
        status = "TOO GENERIC"
    else:
        status = "OK"
    print(f"{status:12} {pages}  {item['q']}")