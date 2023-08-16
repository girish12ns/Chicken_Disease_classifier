from CHICKEN_DISEASE_CLASSIFIER.config.configuration import ConfigurationManager
from CHICKEN_DISEASE_CLASSIFIER.components.base_model import PrepareBaseModel
from CHICKEN_DISEASE_CLASSIFIER import logger
from CHICKEN_DISEASE_CLASSIFIER.config.configuration import ConfigurationManager
from CHICKEN_DISEASE_CLASSIFIER.components.Model_train import Model_trainer,PrepareCallback


import os

stage_3="Model trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config=ConfigurationManager()
            get_callbacks_config=config.get_call_backs()
            get_callbacks=PrepareCallback(config=get_callbacks_config)
            callback_list=get_callbacks.get_tb_ckpt_callbacks()


 
            training_config=config.get_training_model()

            train_data=Model_trainer(config=training_config)

            train_data.base_model()
            train_data.train_valid_generator()
            train_data.train(callback_list=callback_list)

        except Exception as e:
            raise e
        
if __name__=="__main__":
    try:
        logger.info("model training at {stage_name}")
        model_obj=ModelTrainerPipeline()
        obj=model_obj.main()
        logger.info("base model_training completd {stage_name}")
    except Exception as e:
        logger.exception(e)
        raise e



