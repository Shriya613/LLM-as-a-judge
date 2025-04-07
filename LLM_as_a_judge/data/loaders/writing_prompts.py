import pandas as pd
from datasets import load_dataset

"""
Loading the WritingPrompts dataset from Huggingface.
This dataset contains creative writing prompts and responses.
https://huggingface.co/datasets/euclaise/writingprompts
"""

dataset_name = "euclaise/writingprompts"

# Load the validation split to keep consistent with other dataset loading scripts
dataset = load_dataset(dataset_name, split="validation")

# First, let's print the column names to see what's available
print("Available columns:", dataset.column_names)

# Convert to DataFrame
df = pd.DataFrame(dataset)
df = df[["prompt"]]
df = df.rename(columns={"prompt": "question"})

# Add an id column
df["question_id"] = [f"{i}" for i in range(len(df))]

# Reorder columns to put question_id first
df = df[["question_id", "question"]]


# Save to CSV
df.to_csv("data/datasets/writing_prompts.csv", index=False)
print(f"Saved {len(df)} writing prompts and responses to CSV")
