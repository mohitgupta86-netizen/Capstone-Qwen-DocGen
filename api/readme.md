
# API endpoint
POST http://127.0.0.1:8000/generate-doc

# Request contract

{
    "code":"<source code>",

    "language":"python",

    "save_output":true
}

# Response contract

{
    "status":"success",

    "model":"Qwen-LoRA",

    "language":"python",

    "documentation":"Adds two numbers.",

    "saved_to":"outputs/doc_20260620_113500.txt",

    "inference_time":2.14
}

# Sample Client

import requests


code = """
def add(a,b):
    return a+b
"""


payload={

"code":code,

"language":"python",

"save_output":True

}


response=requests.post(

'http://127.0.0.1:8000/generate-doc',

json=payload

)



print(response.json())

# Start up guide

cd Qwen-docgen


venv\Scripts\activate


uvicorn api.app_doc_gen:app --reload
