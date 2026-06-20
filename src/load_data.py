from datasets import load_dataset

print("Loading CodeSearchNet...")

dataset = load_dataset(
    "code_search_net",
    "python"
)

print(dataset)

sample = dataset['train'][0]

print("\nKeys:")
print(sample.keys())


print("\nCODE")
print("="*80)

print(sample['whole_func_string'])


print("\nDOCSTRING")
print("="*80)

print(sample['func_documentation_string'])