from datasets import load_dataset

from generate_qwen import generate_doc

from nltk.translate.bleu_score import (
    sentence_bleu,
    SmoothingFunction
)

from rouge_score import rouge_scorer


# ==========================================
# CONFIG
# ==========================================

TEST_SAMPLES = 20


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


bleu_scores = []
rouge_scores = []


# ==========================================
# EVALUATION LOOP
# ==========================================

for i in range(TEST_SAMPLES):

    sample = test_data[i]

    code = sample['whole_func_string']

    expected = sample[
        'func_documentation_string'
    ]

    generated = generate_doc(code)


    # -------------------
    # BLEU
    # -------------------

    bleu = sentence_bleu(

        [expected.split()],

        generated.split(),

        smoothing_function=smoothie

    )


    bleu_scores.append(
        bleu
    )


    # -------------------
    # ROUGE
    # -------------------

    rouge_l = rouge.score(

        expected,

        generated

    )['rougeL'].fmeasure


    rouge_scores.append(
        rouge_l
    )


    # -------------------
    # Print first 3
    # -------------------

    if i < 3:

        print()

        print("="*100)
        print(f"RECORD {i+1}")
        print("="*100)

        print()

        print("EXPECTED")
        print("-"*80)

        print(expected)


        print()

        print("GENERATED")
        print("-"*80)

        print(generated)


        print()

        print(
            f"BLEU : {bleu:.4f}"
        )

        print(
            f"ROUGE-L : {rouge_l:.4f}"
        )


# ==========================================
# FINAL RESULTS
# ==========================================


avg_bleu = sum(

    bleu_scores

)/len(bleu_scores)



avg_rouge = sum(

    rouge_scores

)/len(rouge_scores)



print()
print()

print("█"*80)
print("QWEN BASELINE")
print("█"*80)

print()

print(
    f"Average BLEU : {avg_bleu:.4f}"
)

print(
    f"Average ROUGE-L : {avg_rouge:.4f}"
)

print()

print("Done")