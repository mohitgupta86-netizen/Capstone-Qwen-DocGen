from pathlib import Path

from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

from peft import PeftModel




BASE_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"



BASE_DIR = Path(__file__).resolve().parent.parent

ADAPTER_PATH = BASE_DIR / "model" / "qwen_lora_docgen"



print()
print("Adapter path")
print(ADAPTER_PATH)

print()
print("Exists")
print(ADAPTER_PATH.exists())




########################################################
# Tokenizer
########################################################

print()
print("Loading tokenizer...")


tokenizer = AutoTokenizer.from_pretrained(

        BASE_MODEL

)




########################################################
# Base model
########################################################

print()
print("Loading base model...")


model = AutoModelForCausalLM.from_pretrained(

        BASE_MODEL

)



########################################################
# LoRA
########################################################

print()
print("Loading LoRA adapters...")


model = PeftModel.from_pretrained(

        model,

        str(ADAPTER_PATH)

)



model.eval()



print()
print("Model ready!")




########################################################
# Inference
########################################################


def clean_docstring(text):


    bad = [


        "Return type",

        "Python Version",

        "Args:",

        "Returns:",

        "Examples:",

        "```",

        "java",

        "python"

    ]



    for item in bad:


        if item in text:


            text=text.split(item)[0]



    text=text.split("\n")[0]



    return text.strip()


##############################################


def generate_doc(code,language):



    prompt = f"""
Generate ONLY ONE sentence.

Rules:

- One sentence
- No markdown
- No examples
- No return types
- No implementation details
- No Arguments

Programming Language: 

{language}


Function:


{code}



Summary:

"""



    inputs = tokenizer(

        prompt,

        return_tensors="pt"

    )



    outputs = model.generate(

        **inputs,


        max_new_tokens=20,


        do_sample=False


    )




    response = tokenizer.decode(

        outputs[0][inputs['input_ids'].shape[1]:],


        skip_special_tokens=True

    )



    response = clean_docstring(

            response
    )



    return response