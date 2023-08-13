from CHICKEN_DISEASE_CLASSIFIER import logger
from CHICKEN_DISEASE_CLASSIFIER.Pipeline.stage_01_dataingestion import DataIngestionPipeline


stage_name="01_data_ingestion_stage"
try:
  logger.info("data_ingestination_started at {stage_name}")

  obj=DataIngestionPipeline()
  obj.main()
  logger.info("data_ingestion_complets {stage_name}")
except Exception as e:
        logger.exception(e)
        raise e


