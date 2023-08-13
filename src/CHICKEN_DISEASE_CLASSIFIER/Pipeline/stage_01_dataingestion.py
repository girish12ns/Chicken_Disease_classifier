from CHICKEN_DISEASE_CLASSIFIER.config.configuration import ConfigurationManager
from CHICKEN_DISEASE_CLASSIFIER.components.data_ingestion import DataIngestion
from CHICKEN_DISEASE_CLASSIFIER import logger


stage_name="01_data_ingestion_stage"
class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        ingestion=ConfigurationManager()
        data_ingestion_config=ingestion.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.get_the_data()



if __name__=="__main__":
    try:
        logger.info("data_ingestination_started at {stage_name}")

        obj=DataIngestionPipeline()
        obj.main()
        logger.info("data_ingestion_complets {stage_name}")
    except Exception as e:
        logger.exception(e)
        raise e

