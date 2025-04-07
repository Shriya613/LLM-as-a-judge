import csv
import sys

from datasets import load_dataset
from tqdm import tqdm

"""
Reddit ELI5 is a dataset of questions and answers from Reddit's  "Explain Like I'm 5" subreddit.
https://huggingface.co/datasets/sentence-transformers/eli5
"""

dataset_name = "sentence-transformers/eli5"

# Create a streaming dataset; Uses a ~100MB buffer to stream these suckers in.
dataset = load_dataset(dataset_name, split="train", streaming=True)

# Define the fields we want to keep
fields = ["question_id", "question"]

# Open a CSV file to write the results
# Takes ~5 minutes with streaming.
# Ingest only the first 7500 examples of 325k.
# Note taht we aren't doing any shuffling, just taking the first 7500. Lol.
with open("data/datasets/eli5.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()

    # Process the dataset in streaming mode
    for idx, example in enumerate(
        tqdm(dataset.take(7500), total=7500, desc="Processing ELI5")
    ):
        if idx >= 7500:
            break
        # Extract only the fields we want
        row = {"question": example["question"], "question_id": idx}
        writer.writerow(row)

print("Done!")
# Force exit to ensure all background processes are terminated
sys.exit(0)
