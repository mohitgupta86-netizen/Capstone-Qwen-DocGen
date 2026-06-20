from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch


MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

print("Model loaded")


def generate_doc(code):

    prompt = f"""
Task: Code Summarization

Given a Python function, generate ONLY its short docstring.

Requirements:
- One sentence only
- No markdown
- No code
- No examples
- No implementation details
- Output should resemble CodeSearchNet targets

Function:

{code}

Docstring:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    return response.strip()