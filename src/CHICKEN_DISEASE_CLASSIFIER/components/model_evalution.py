import time
from CHICKEN_DISEASE_CLASSIFIER.entity.config_entity import CallBacks,Model_train,Base_Model,evaluation_config
import tensorflow as tf
import os
from pathlib import Path
from CHICKEN_DISEASE_CLASSIFIER.utils.common import save_json



class Evaluation:
    def __init__(self,config:evaluation_config):
        self.config=config

    def _valid_generator(self):

        data_generator_kwargs=dict(
            rescale=1./255,
            validation_split=0.30
        )

        dataflow_kwargs=dict(
            target_size=self.config.param_image_size[:-1],
            batch_size=self.config.param_batch_size,
            interpolation='bilinear',
            )
        valid_generaor=tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs 
            )
        self.valid_generator=valid_generaor.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs

               
        )
    @staticmethod
    def load_model(path:Path)->tf.keras.Model:
            return tf.keras.models.load_model(path)
        
    def evaluation_model(self):
            self.model=self.load_model(path=self.config.path_of_model)
            self._valid_generator()
            self.score=self.model.evaluate(self.valid_generator)

    def save_score(self):
        scores={'loss':self.score[0],"accuracy":self.score[1]}
        save_json(path=Path("scores.jason"),data=scores)
        


