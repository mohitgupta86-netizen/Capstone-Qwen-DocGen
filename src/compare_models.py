from datasets import load_dataset

from generate_qwen import generate_doc as base_generate
from generate_qwen_lora import generate_doc as lora_generate


from nltk.translate.bleu_score import (
    sentence_bleu,
    SmoothingFunction
)

from rouge_score import rouge_scorer


# ==========================================
# CONFIG
# ==========================================

TEST_SAMPLES = 100



# ==========================================
# LOAD DATASET
# ==========================================

print("Loading dataset...")


dataset = load_dataset(
    "code_search_net",
    "python"
)


test_data = dataset["test"]


print("Dataset loaded")
print()



# ==========================================
# METRICS
# ==========================================

smoothie = SmoothingFunction().method4


rouge = rouge_scorer.RougeScorer(

        ['rougeL'],

        use_stemmer=True

)



base_bleu = []
base_rouge = []



lora_bleu = []
lora_rouge = []



# ==========================================
# LOOP
# ==========================================


for i in range(TEST_SAMPLES):


    sample = test_data[i]


    code = sample['whole_func_string']


    expected = sample[
        'func_documentation_string'
    ]



    #####################################
    # BASE
    #####################################


    base = base_generate(
        code
    )


    bleu = sentence_bleu(

            [expected.split()],

            base.split(),

            smoothing_function=smoothie

    )


    rouge_l = rouge.score(

            expected,

            base

    )['rougeL'].fmeasure



    base_bleu.append(
        bleu
    )


    base_rouge.append(
        rouge_l
    )



    #####################################
    # LORA
    #####################################


    lora = lora_generate(
        code
    )


    bleu = sentence_bleu(

            [expected.split()],

            lora.split(),

            smoothing_function=smoothie

    )


    rouge_l = rouge.score(

            expected,

            lora

    )['rougeL'].fmeasure



    lora_bleu.append(
        bleu
    )


    lora_rouge.append(
        rouge_l
    )



    #####################################
    # PRINT
    #####################################


    if i < 5:


        print()

        print("="*100)
        print(f"RECORD {i+1}")
        print("="*100)



        print()

        print("EXPECTED")
        print("-"*80)

        print(expected)



        print()

        print("BASE")
        print("-"*80)

        print(base)



        print()

        print("LORA")
        print("-"*80)

        print(lora)



        print()

        print(
            f"BASE BLEU : {base_bleu[-1]:.4f}"
        )


        print(
            f"BASE ROUGE-L : {base_rouge[-1]:.4f}"
        )



        print()



        print(
            f"LORA BLEU : {lora_bleu[-1]:.4f}"
        )


        print(
            f"LORA ROUGE-L : {lora_rouge[-1]:.4f}"
        )




# ==========================================
# SUMMARY
# ==========================================


avg_base_bleu = sum(

        base_bleu

)/len(base_bleu)



avg_base_rouge = sum(

        base_rouge

)/len(base_rouge)




avg_lora_bleu = sum(

        lora_bleu

)/len(lora_bleu)



avg_lora_rouge = sum(

        lora_rouge

)/len(lora_rouge)




print()
print()


print("█"*80)
print("BASE MODEL")
print("█"*80)


print()

print(

f"Average BLEU : {avg_base_bleu:.4f}"

)


print(

f"Average ROUGE-L : {avg_base_rouge:.4f}"

)





print()
print()



print("█"*80)
print("LORA MODEL")
print("█"*80)



print()

print(

f"Average BLEU : {avg_lora_bleu:.4f}"

)


print(

f"Average ROUGE-L : {avg_lora_rouge:.4f}"

)




print()
print()



print("█"*80)
print("IMPROVEMENT")
print("█"*80)



print()


print(

f"BLEU Improvement : {((avg_lora_bleu-avg_base_bleu)/avg_base_bleu)*100:.2f}%"

)



print(

f"ROUGE Improvement : {((avg_lora_rouge-avg_base_rouge)/avg_base_rouge)*100:.2f}%"

)



print()

print("Done")