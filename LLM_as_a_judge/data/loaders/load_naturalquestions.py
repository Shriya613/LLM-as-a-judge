import csv

from datasets import load_dataset
from tqdm import tqdm

"""
Natural Questions dataset as introduced in Natural Questions: A Benchmark for Question Answering Research (Kwiatkowski et al.,2019)
Questions consist of real anonymized, aggregated queries issued to the Google search engine.
https://huggingface.co/datasets/google-research-datasets/natural_questions
"""

dataset_name = "google-research-datasets/natural_questions"

# Create a streaming dataset; Uses a ~100MB buffer to stream these suckers in.
dataset = load_dataset(dataset_name, split="validation", streaming=True)

# Define the fields we want to keep
fields_to_keep = ["question_id", "question"]

# Open a CSV file to write the results
# Takes ~5 minutes with streaming.
with open(
    "data/datasets/natural_questions.csv", "w", newline="", encoding="utf-8"
) as f:
    writer = csv.DictWriter(f, fieldnames=fields_to_keep)
    writer.writeheader()

    # Process the dataset in streaming mode
    for idx, example in enumerate(
        tqdm(dataset, total=7840, desc="Processing Natural Questions")
    ):
        # Extract only the fields we want
        row = {"question": example["question"]["text"], "question_id": idx}
        writer.writerow(row)
