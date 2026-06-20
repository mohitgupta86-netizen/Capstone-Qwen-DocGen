from datasets import load_dataset
import random

dataset = load_dataset(
    "code_search_net",
    "python"
)

train = dataset['train']


categories = {
    'very_short':[],
    'param':[],
    'example':[],
    'url':[],
    'todo':[],
    'good':[]
}


for sample in train:


    doc = sample[
        'func_documentation_string'
    ].strip()



    if len(doc.split()) < 3:

        categories['very_short'].append(doc)



    elif ':param' in doc:

        categories['param'].append(doc)



    elif '>>>' in doc:

        categories['example'].append(doc)



    elif 'http' in doc:

        categories['url'].append(doc)



    elif 'TODO' in doc.upper():

        categories['todo'].append(doc)



    elif len(doc.split()) > 8:

        categories['good'].append(doc)




for k in categories:


    print()
    print("="*80)

    print(k.upper())

    print("="*80)



    for x in random.sample(

        categories[k],

        min(10,len(categories[k]))

    ):


        print()
        print(x)