from PIL import Image
import os
from CHICKEN_DISEASE_CLASSIFIER.entity.config_entity import DataIngestionconfig




class DataIngestion:
    def __init__(self,config:DataIngestionconfig):
        self.config=config

    def get_the_data(self):
        image_files = [filename for filename in os.listdir(self.config.source_dir) if filename.endswith('.jpg')]

        for image_filename in image_files:
            source_image_path = os.path.join(self.config.source_dir, image_filename)
            destination_image_path = os.path.join(self.config.root_dir, image_filename)

            image = Image.open(source_image_path)

            image.save(destination_image_path)


            image.close()

        return (f"Processed {len(image_files)} images.")