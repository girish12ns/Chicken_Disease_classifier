

from pathlib import Path
import os
from CHICKEN_DISEASE_CLASSIFIER.constants import config_file_path,param_file_path
from CHICKEN_DISEASE_CLASSIFIER.utils.common import read_yaml,create_directories
from CHICKEN_DISEASE_CLASSIFIER.entity.config_entity import (DataIngestionconfig,Base_Model,
                                                            CallBacks,Model_train,evaluation_config)

class ConfigurationManager:
    def __init__(self,
                 config_filepath=config_file_path,
                 param_filepath=param_file_path):
            
            self.config=read_yaml(config_filepath)
            self.params=read_yaml(param_filepath)

            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionconfig:
          
          config=self.config.Data_ingestion

          create_directories([config.root_dir])
          

          create_directories([config.root_dir,config.category_1_dir,config.category_2_dir,
                              
                             config.category_3_dir,config.category_4_dir])

          
          data_ingestion_config=DataIngestionconfig(
                root_dir=config.root_dir,
                source_dir=config.source_dir,
                category_1_dir=config.category_1_dir,
                category_2_dir=config.category_2_dir,
                category_3_dir=config.category_3_dir,
                category_4_dir=config.category_4_dir)
          
          return data_ingestion_config

          
          
          
          
          
    
    def get_prepare_base_model(self)->Base_Model:

        config=self.config.Prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model=Base_Model(
            root_dir=config.root_dir,
            base_model_dir=config.base_model_dir,
            updated_base_model_dir=config.updated_base_model_dir,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGHTS,
            params_classes= self.params.CLASSES)
        return prepare_base_model
       
    
    def get_call_backs(self)->CallBacks:
        config=self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([Path(config.tensorboard_root_log_dir),Path(model_ckpt_dir)])

        prepare_callback=CallBacks(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback
    

    def get_training_model(self)->Model_train:
        training=self.config.training
        prepare_base_model=self.config.Prepare_base_model
        params=self.params
        training_data_dir=os.path.join(self.config.Data_ingestion.root_dir)

        create_directories([training.root_dir])

        training_config=Model_train(
                root_dir=Path(training.root_dir),
                trained_model_path=Path(training.trained_model_path),
                updated_base_model_path=prepare_base_model.updated_base_model_dir,
                training_data= Path(training_data_dir),
                params_epochs=params.EPOCHS,
                params_batch_size= params.BATCH_SIZE,
                params_is_augmentation= params.AUGMENTATION,
                params_image_size= params.IMAGE_SIZE)
        
        return training_config

    
    def get_validation_data_config(self)->evaluation_config:
        
        eval_config=evaluation_config(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion",
            all_params=self.params,
            param_image_size=self.params.IMAGE_SIZE,
            param_batch_size=self.params.BATCH_SIZE


        )
        return eval_config

 

    
