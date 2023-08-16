from PIL import Image
import os
from CHICKEN_DISEASE_CLASSIFIER.entity.config_entity import DataIngestionconfig




from PIL import Image
import os

from pathlib import Path
import shutil

class DataIngestion:
    def __init__(self,config:DataIngestionconfig):
        self.config=config

    def get_the_data(self):
        
        for filename in os.scandir(self.config.source_dir):
            
            if filename.name.startswith('salmo') or filename.name.startswith('pcrsalmo'):
                image_path = filename.path
                shutil.copy(image_path, self.config.category_1_dir)
            elif filename.name.startswith('cocci') or filename.name.startswith('pcrcocci'):
                image_path = filename.path
                shutil.copy(image_path, self.config.category_2_dir)
            elif filename.name.startswith('healthy') or filename.name.startswith('pcrhealthy'):
                image_path = filename.path
                shutil.copy(image_path, self.config.category_3_dir)
            elif filename.name.startswith('ncd') or filename.name.startswith('pcrncd'):
                image_path = filename.path
                shutil.copy(image_path, self.config.category_4_dir)
