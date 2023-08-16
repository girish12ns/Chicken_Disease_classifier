from CHICKEN_DISEASE_CLASSIFIER.config.configuration import ConfigurationManager
from CHICKEN_DISEASE_CLASSIFIER.components.base_model import PrepareBaseModel
from CHICKEN_DISEASE_CLASSIFIER import logger
from CHICKEN_DISEASE_CLASSIFIER.components.model_evalution import Evaluation


stage_name_04="model evaluation "


class ModelEvalutionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            val_config = config.get_validation_data_config()
            evaluation = Evaluation(val_config)
            evaluation.evaluation_model()
            evaluation.save_score()

        except Exception as e:


            raise e
        

if __name__=="__main__":
    try:
        logger.info("model_evaluation at {stage_name_04}")
        eval=ModelEvalutionPipeline()
        eval_obj=eval.main()
        logger.info("base model_evalauation completed {stage_name_04}")
    except Exception as e:
        logger.exception(e)
        raise e

