# Qwen-LoRA DocGen


## Overview

Fine-tuned Qwen2.5-0.5B model using LoRA for Python documentation generation.


## Features

- Qwen2.5-0.5B-Instruct
- LoRA Fine-tuning
- FastAPI endpoint
- Swagger support
- Documentation persistence


## Metrics

BLEU : 0.72

ROUGE-L : 0.84


## Run


uvicorn api.app_doc_gen:app --reload



## Endpoint


POST /generate-doc


Request


{
    "code":"",
    "language":"python",
    "save_output":true
}



## Authors

IIIT-H Capstone Project