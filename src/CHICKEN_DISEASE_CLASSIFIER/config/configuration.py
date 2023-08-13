


from CHICKEN_DISEASE_CLASSIFIER.constants import config_file_path,param_file_path
from CHICKEN_DISEASE_CLASSIFIER.utils.common import read_yaml,create_directories
from CHICKEN_DISEASE_CLASSIFIER.entity.config_entity import DataIngestionconfig

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
          
          data_ingestion_config=DataIngestionconfig(
                root_dir=config.root_dir,
                source_dir=config.source_dir)
          
          return data_ingestion_config