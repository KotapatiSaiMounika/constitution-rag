import json
import re
import sys

sys.path.append("src")
from retrieve import retrieve

def norm(s):
    return re.sub(r"\s+", " ", s).lower()

with open("eval/questions.json") as f:
    questions = json.load(f)

hits = 0
for item in questions:
    results = retrieve(item["q"], k=4)
    found = any(norm(item["must_contain"]) in norm(r["text"]) for r in results)
    hits += found
    print("PASS" if found else "FAIL", "-", item["q"])

print(f"\nHit rate@4: {hits}/{len(questions)} = {hits/len(questions):.0%}")