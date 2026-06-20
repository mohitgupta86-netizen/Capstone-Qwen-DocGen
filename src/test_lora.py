from generate_qwen_lora import generate_doc


code = """

def extract_video_id(url):
    pass

"""


doc = generate_doc(code)

print()
print("="*80)
print("GENERATED")
print("="*80)

print(doc)