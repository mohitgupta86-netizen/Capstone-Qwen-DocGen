Model	    BLEU	ROUGE	Characteristics
CodeGen 	0.013	0.176	Code completion
CodeT5 Base	0.001	0.105	Weak baseline
CodeT5 FT	0.022	0.228	Learns target style
Qwen 0.5B	0.047	0.193	Strong semantic understanding - actual data is not proper
Qwen-FT     0.762   0.9217  Very very strong documentation
Qwen-FT-100 0.726   0.8380  100 samples tested, looks really good.


Existing code summarization datasets contain inconsistent and non-standard documentation targets. Traditional lexical metrics such as BLEU and ROUGE may undervalue instruction-tuned LLMs that generate semantically richer and more developer-friendly documentation.

total                412178
long                 281487
multiline            272671
short                111627
param                70740
very_short           19064
example              15511
url                  14637
returns              26895
from                 569
todo                 2087
comment              144


================================================================================
STYLE DISTRIBUTION
================================================================================
natural        253098     61.41%
sphinx         70740      17.16%
brief          45684      11.08%
google         31158       7.56%
example        10113       2.45%
todo           1353        0.33%
reference      32          0.01%

================================================================================
LENGTH ANALYSIS
================================================================================

Average words : 37.71
Median words  : 19.0
Max words     : 6371

================================================================================


================================================================================
Fine tuning
================================================================================
### Fine-Tuning Observations – Qwen 2.5 0.5B (LoRA)

* Base Model: **Qwen2.5-0.5B-Instruct (~496M parameters)**
* Fine-tuning Technique: **LoRA (Low Rank Adaptation)**
* Dataset: **CodeSearchNet (Python)** with **50,000 training samples** (~12% of full dataset)
* Epochs: **1**
* LoRA Configuration:

  * Rank (r): **16**
  * Alpha: **32**
  * Dropout: **0.05**
  * Target Modules: **q_proj, k_proj, v_proj, o_proj**
* Trainable Parameters: **2,162,688 (~0.44% of total model parameters)**
* Frozen Parameters: **~494M (99.56%)**
* Training Environment: **Google Colab Free Tier (T4 GPU)**
* Total Training Time: **~1.87 hours (6,710 seconds)**
* Training Steps: **3,125**
* Effective Batch Size: **16**
* Final Training Loss: **0.685**
* Saved Adapter Size: **8.3 MB**
* Total Artifact Size (including tokenizer): **~24 MB**
* Approximate Compression Benefit: **~230× smaller than storing a fully fine-tuned model**

### Key Learnings

* LoRA enabled efficient adaptation of a 500M parameter model while training less than **0.5% of parameters**.
* Fine-tuning was successfully completed using only free cloud resources.
* Dataset profiling revealed that CodeSearchNet contains heterogeneous documentation styles, which may limit the correlation between low training loss and documentation quality.
* Future improvements may include dataset curation, filtering noisy examples, and experimenting with larger training subsets (100K+) or higher-quality documentation datasets.
