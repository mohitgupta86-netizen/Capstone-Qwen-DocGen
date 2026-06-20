from datasets import load_dataset
from collections import Counter
import statistics


print("Loading dataset...")

dataset = load_dataset(
    "code_search_net",
    "python"
)

train = dataset['train']


styles = Counter()
lengths = []

samples = {}


for sample in train:

    doc = sample[
        'func_documentation_string'
    ].strip()

    words = len(doc.split())

    lengths.append(words)


    category = None


    if ':param' in doc:
        category = 'sphinx'

    elif 'Args:' in doc:
        category = 'google'

    elif '>>>' in doc:
        category = 'example'

    elif 'Swagger:' in doc:
        category = 'swagger'

    elif 'Ref:' in doc:
        category = 'reference'

    elif 'TODO' in doc.upper():
        category = 'todo'

    elif words <= 5:
        category = 'brief'

    else:
        category = 'natural'


    styles[category] += 1


    if category not in samples:
        samples[category] = doc



print()
print("="*80)
print("STYLE DISTRIBUTION")
print("="*80)


for k, v in sorted(styles.items(),
                   key=lambda x: x[1],
                   reverse=True):


    pct = v / len(train) * 100


    print(
        f"{k:<15}"
        f"{v:<10}"
        f"{pct:>6.2f}%"
    )



print()
print("="*80)
print("LENGTH ANALYSIS")
print("="*80)


print()

print(
    f"Average words : "
    f"{statistics.mean(lengths):.2f}"
)


print(
    f"Median words  : "
    f"{statistics.median(lengths)}"
)


print(
    f"Max words     : "
    f"{max(lengths)}"
)




print()
print("="*80)
print("REPRESENTATIVE EXAMPLES")
print("="*80)



for cat in samples:


    print()

    print("-"*80)

    print(cat.upper())

    print("-"*80)

    print()

    print(samples[cat])

    print()