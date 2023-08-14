from CHICKEN_DISEASE_CLASSIFIER.config.configuration import ConfigurationManager
from CHICKEN_DISEASE_CLASSIFIER.components.base_model import PrepareBaseModel
from CHICKEN_DISEASE_CLASSIFIER import logger




stage_name="stage_02_base_model"
try:
    class BaseModelPipeline:
        def __init__(self):
            pass
        def main(self):
            base_model=ConfigurationManager()
            prepare_base= base_model.get_prepare_base_model()
            model_obj=PrepareBaseModel(config=prepare_base)
            model_obj.get_base_model()
            model_obj.update_base_model()
except Exception as e:
    raise e


if __name__=="__main__":
    try:
        logger.info("base_model_creation at {stage_name}")
        model_obj=BaseModelPipeline()
        obj=model_obj.main()
        logger.info("base model creation complets {stage_name}")
    except Exception as e:
        logger.exception(e)
        raise e
