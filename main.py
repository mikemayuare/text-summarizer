from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from textSummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)
from textSummarizer.logging import logger


stage_name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
