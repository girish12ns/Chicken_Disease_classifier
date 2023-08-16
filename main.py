from CHICKEN_DISEASE_CLASSIFIER import logger
from CHICKEN_DISEASE_CLASSIFIER.Pipeline.stage_01_dataingestion import DataIngestionPipeline
from CHICKEN_DISEASE_CLASSIFIER.Pipeline.stage_02_base_model import BaseModelPipeline
from CHICKEN_DISEASE_CLASSIFIER.Pipeline.stage_03_model_trainer import ModelTrainerPipeline



stage_name="01_data_ingestion_stage"
try:
  logger.info("data_ingestination_started at {stage_name}")

  obj=DataIngestionPipeline()
  obj.main()
  logger.info("data_ingestion_complets {stage_name}")
except Exception as e:
        logger.exception(e)
        raise e

stage_name_2="base_model_creation"

try:
  logger.info("base_model_creation at {stage_name_2}")
  model_obj=BaseModelPipeline()
  obj=model_obj.main()
  logger.info("base model creation completes {stage_name_2}")
except Exception as e:
  logger.exception(e)
  raise e

try:
  logger.info("model_traineing at {stage_name_3}")
  model_trainer=ModelTrainerPipeline()
  obj=model_trainer.main()
  logger.info("mode_trainer completed {stage_name_3}")
except Exception as e:
  logger.exception(e)
  raise e



