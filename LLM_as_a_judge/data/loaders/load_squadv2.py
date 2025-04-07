import pandas as pd
from datasets import load_dataset

"""
I think open QA datasets would be a better test than SQuAD v2.
I don't think that {context} {question} are a good place to evaluate the criteria we're looking at.
Would prefer to have an open book/domain-type dataset.

DO NOT PROCEED
"""

dataset_name = "rajpurkar/squad_v2"

dataset = load_dataset(dataset_name, split="validation")

df = pd.DataFrame(dataset)

# Hm... Let's abandon this for now.
