import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipe:
    def __init__(self,filename):    
        self.filename=filename

    def prediction(self):
        model=load_model(os.path.join("artifacts","training","model.h5"))

        imagename=self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
        print(result)


        if result[0]==1:
            Prediction="Coccidiosis"
            return [{'image':Prediction}]
        elif result[0]==2:
            Prediction="Healthy"
            return [{'image':Prediction}]
        elif result[0]==3:
            Prediction="New Castle Disease"
            return [{'image':Prediction}]
        else:
            result[0]==4
            Prediction="Coccidiosis"
            return [{'image':Prediction}]
        
           

