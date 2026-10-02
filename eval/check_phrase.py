import json
import re
import sys

def norm(s):
    return re.sub(r"\s+", " ", s).lower()

chunks = json.load(open("data/chunks.json"))
phrase = norm(sys.argv[1])
pages = [c["page"] for c in chunks if phrase in norm(c["text"])]
print(pages if pages else "NOT FOUND")