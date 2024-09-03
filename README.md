# Text Summarizer

This repository contains an end-to-end text summarization model built using the `transformers` library. The model is fine-tuned from the `google/pegasus-cnn_dailymail` model using the SAMSum dataset, which is designed for summarizing conversations. The fine-tuning is performed with sequence-to-sequence (seq2seq) learning.

## Project Structure

- **src/**: Contains all the source code, including the training scripts, data processing, and model evaluation.
  - **src/textSummarizer/components/data_preprocessing.py**: Handles the preprocessing of the dataset.
  - **src/textSummarizer/components/model_training.py**: Contains the logic for fine-tuning the Pegasus model.
  - **src/textSummarizer/components/model_evaluation.py**: Provides methods for evaluating the fine-tuned model on test data.
  - **src/utils/common.py**: Utility functions used across the project.

- **config.yaml**: Contains the configuration for the project, including the model, tokenizer, and dataset paths.
- **parameters.yaml**: Specifies the hyperparameters for training, such as batch size, learning rate, and the number of epochs.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- `transformers`
- `datasets`
- `pytorch`
- `pyyaml`

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Training the Model

To fine-tune the model with the SAMSum dataset, run:

```main.py```

This will start the entire process using the configuration and parameters specified in the `config.yaml` and `parameters.yaml` files.


## Customization

### Using a Different Model or Dataset

You can easily modify this project to use different models, datasets, or even tasks by adjusting the YAML configuration files and corresponding classes in the `src` folder:

- **Model**: To change the model, update the `model_name` field in `config.yaml`.
- **Dataset**: To use a different dataset, change the dataset path in `config.yaml` and update the preprocessing steps in `src/data_preprocessing.py`.
- **Training Parameters**: Modify hyperparameters such as learning rate, batch size, and number of epochs in `parameters.yaml`.

### Extending to Other Tasks

If you want to extend this project to other NLP tasks (e.g., translation, text generation), you can:

1. Update the data preprocessing logic in `src/data_preprocessing.py` to fit the new task.
2. Modify the training and evaluation scripts to accommodate the different task requirements.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The fine-tuning is based on the [Transformers](https://github.com/huggingface/transformers) library by Hugging Face.
- The SAMSum dataset is provided by the [SAMSum](https://arxiv.org/abs/1911.12237) authors.

