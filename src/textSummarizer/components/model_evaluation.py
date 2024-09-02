from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from textSummarizer.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def generate_batch_sized_chuncks(self, list_of_elements: list, batch_size: int):
        """Split dataset into smaller batches that can be processed simultaneously
        Yield successive batch-sized chunks from list of elements.

        Args:
            list_of_elements (list): List with elements to be split on batches
            batch_size (int): Number of elements per batch

        Yield:
            list: Batches
        """
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]

    def calculate_test_metric(
        self,
        dataset,
        metric,
        model,
        tokenizer,
        batch_size: int=16,
        device: str="cuda" if torch.cuda.is_available() else "cpu",
        column_text: str="article",
        column_summary: str="highlights",
    ) -> float:
        """_summary_

        Args:
            dataset (datasets.arrow_dataset.Dataset): _description_
            metric (str): _description_
            model (transformers.models.pegasus.modeling_pegasus.PegasusForConditionalGeneration): _description_
            tokenizer (transformers.models.pegasus.tokenization_pegasus_fast.PegasusTokenizerFast): _description_
            batch_size (int): _description_
            column_text (str, optional): _description_. Defaults to "article".
            column_summary (str, optional): _description_. Defaults to "highlights".

        Returns:
            float: _description_
        """
        article_batches = list(
            self.generate_batch_sized_chuncks(dataset[column_text], batch_size)
        )
        target_batches = list(
            self.generate_batch_sized_chuncks(dataset[column_summary], batch_size)
        )

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)
        ):

            inputs = tokenizer(
                article_batch,
                max_length=1024,
                truncation=True,
                padding="max_length",
                return_tensors="pt",
            )
            summaries = model.generate(
                input_ids=inputs["input_ids"].to(device),
                attention_mask=inputs["attention_mask"].to(device),
                length_penalty=0.8,
                num_beams=8,
                max_length=128,  # avoid long sequences
            )

            decoded_summaries = [
                tokenizer.decode(
                    s,
                    skip_special_tokens=True,
                    clean_up_tokenization_spaces=True,
                )
                for s in summaries
            ]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            metric.add_batch(predictions=decoded_summaries, references=target_batch)

        return metric.compute()

    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model_path
        ).to(device)

        dataset_pt = load_from_disk(self.config.data_path)

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = load_metric("rouge")
        score = self.calculate_test_metric(
            dataset_pt["test"],
            rouge_metric,
            model_pegasus,
            tokenizer,
            batch_size=8,
            column_text="dialogue",
            column_summary="summary",
        )

        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)

        df = pd.DataFrame(rouge_dict, index=["pegasus"])
        df.to_csv(self.config.metric_file_name, index=False)