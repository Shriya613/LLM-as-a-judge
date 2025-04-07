# 245 Project: Language-Model-as-a-Judge Analysis

## Overview

Language models have demonstrated remarkable capabilities in producing high-quality generations across a wide range of tasks. Still, evaluation of the quality of these generations is a challenging task -- old standby metrics like BLEU and ROUGE are not always indicative of the quality of the generation, suffering from issues like over-penalizing shorter generations, and being unable to capture semantic differences between generations.

Recent work has considered using language models themselves to evaluate the quality of generations. This "language model as a judge" concept has, in certain scenarios, been shown to correlate highly with human judgment.

Still, the performance of LLMs as judgement is dependent on the quality of the prompt used to elicit the LLM to act as a judge, the nature and origin of the generations being judged, and the LLM used.

This project explores the interaction between generators and judges, examining how different language models perform in both roles across multiple datasets and evaluation criteria. We analyze a variety of open-weight models ranging from 12B to >100B parameters, evaluating their responses to information-seeking questions and their ability to judge other models' outputs across dimensions like factuality, coherence, and natural language quality.

Our work aims to:
- Understand biases and patterns in LLM-as-judge evaluations
- Compare judgments across different model architectures and sizes
- Assess the correlation between model performance as generators versus judges
- Identify potential improvements in LLM-driven evaluation methods

## Development Directions

1. Make sure the correct Python version as defined in `.python-version` is installed using Pyenv:
```bash
pyenv install 3.11.1
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

5. We use python-dotenv to manage environment variables. Create an `.env` file in the root directory and add the following:
```
OPENROUTER_API_KEY=<your-openrouter-api-key>
```

## Project Structure
- `analysis/`: Contains ipynb files for data analysis.
- `annotation/`: Contains the annotation data for our CR and QA datasets.
- `data/`: Contains input data CSVs formatted as (question_id, question) pairs, along with loaders for each dataset.
- `generations/`: Contains generations for each experiment
- `judgements/`: Contains judgements for each experiment
- `mistral_example/`: Kiara code for data analysis of Mistral Nemo model example for slides.
- `templates/`: Contains HTML templates for use with `view_generations.py` and `view_judgements.py`.
- `tests/`: Contains unit tests for the project.
- `venv/`: Contains the virtual environment. This file is git-ignored.
- `.env`: Contains the environment variables for the project (OpenRouter API key). Git ignored.
- `.gitattributes`: Git LFS configuration/attributes for large judgement files that are > 100MB in size.
- `.gitignore`: Describes files and directories that are git-ignored.
- `.python-version`: Specifies the Python version used in the project by Pyenv (assuming it's installed in Pyenv).
- `criteria.py`: Contains the criteria and criteria descriptions for the judgement task.
- `models.py`: Contains enums mapping OpenRouter models to their prefererd providers.
- `prompts.py`: Contains instructions and template functions for generation and judgement.
- `rate_limiting.py`: Contains the rate limiting logic for OpenRouter API calls.
- `README.md`: This file.
- `requirements.txt`: Contains the dependencies for the project.
- `run_generation.py`: Contains the high-level imperature code of the generation half of the experiment.
- `run_judgement.py`: Contains the high-level imperature code of the judgement half of the experiment.
- `setup.cfg`: Configures pytest.
- `utils.py`: Contains OpenRouter-related and other utility functions.
- `view_generations.py`: Runs flask app for viewing generations.
- `view_judgements.py`: Runs flask app for viewing judgements and related figures.
