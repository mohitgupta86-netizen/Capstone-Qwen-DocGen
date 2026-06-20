from datasets import load_dataset
from collections import Counter
import re


print("Loading dataset...")

dataset = load_dataset(
    "code_search_net",
    "python"
)

train = dataset["train"]

print("Loaded", len(train))


stats = Counter()


sample_bad = []
sample_good = []



for sample in train:


    doc = sample["func_documentation_string"].strip()


    words = len(doc.split())


    stats["total"] += 1


    if words <= 3:
        stats["very_short"] += 1


    elif words <= 10:
        stats["short"] += 1


    else:
        stats["long"] += 1


    if "\n" in doc:
        stats["multiline"] += 1


    if ":param" in doc:
        stats["param"] += 1


    if "Returns:" in doc:
        stats["returns"] += 1


    if ">>>" in doc:
        stats["example"] += 1


    if "TODO" in doc.upper():
        stats["todo"] += 1


    if "From " in doc:
        stats["from"] += 1


    if "http" in doc:
        stats["url"] += 1


    if doc.startswith("#"):
        stats["comment"] += 1


    if words < 3:
        sample_bad.append(doc)


    elif words > 8:
        sample_good.append(doc)




print()
print("Statistics")
print("="*50)


for k,v in stats.items():

    print(

        f"{k:<20} {v}"

    )


print()


print("Bad examples")

print("="*50)

for x in sample_bad[:20]:

    print(x)

    print()




print()


print("Good examples")

print("="*50)

for x in sample_good[:20]:

    print(x)

    print()
