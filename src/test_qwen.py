from datasets import load_dataset

from generate_qwen import generate_doc




dataset=load_dataset(

    "code_search_net",

    "python"
)



sample=dataset['train'][5]



code=sample['whole_func_string']


expected=sample['func_documentation_string']




print()

print("EXPECTED")
print("="*80)

print(expected)



print()

print("QWEN")
print("="*80)




result=generate_doc(code)



print(result)
