from fastapi import FastAPI
from pydantic import BaseModel

from src.generate_qwen_lora import generate_doc

from pathlib import Path
from datetime import datetime
import time


####################################################
# FastAPI App
####################################################

app = FastAPI(

    title="Qwen-LoRA Documentation Generator",

    description="Generate Python documentation using a fine-tuned Qwen-LoRA model",

    version="1.0"

)



####################################################
# Request Schema
####################################################

class Request(BaseModel):

    code:str

    language:str

    save_output:bool=True



####################################################
# API Endpoint
####################################################

@app.post("/generate-doc")

def generate(request:Request):


    try:


        start=time.time()



        documentation = generate_doc(

                request.code,
                request.language
        )



        end=time.time()


        ####################################################
        # Create Output Folder
        ####################################################

        output_dir = Path("outputs")


        output_dir.mkdir(

                exist_ok=True
        )



        ####################################################
        # File Name
        ####################################################

        filename = output_dir / datetime.now().strftime(

            "doc_%Y%m%d_%H%M%S.txt"

        )



        ####################################################
        # Save Documentation
        ####################################################


        with open(

                filename,

                "w",

                encoding="utf8"

        ) as f:



            f.write(

                documentation
            )




        ####################################################
        # Console Logs
        ####################################################


        print()


        print("="*70)

        print("Documentation Generated")

        print("="*70)


        print()


        print(documentation)


        print()


        print(

            f"Saved to : {filename}"

        )


        print()



        ####################################################
        # API Response
        ####################################################


        return{


            "status":"success",


            "model":"Qwen2.5-LoRA",


            "language":request.language,


            "documentation":documentation,


            "saved_to":str(filename),


            "inference_time":round(

                    end-start,

                    2

            )

        }



    except Exception as e:


        return{


            "status":"failed",


            "error":str(e)

        }