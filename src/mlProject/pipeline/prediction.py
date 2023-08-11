import joblib 
import numpy as np
import pandas as pd
from pathlib import Path
from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()

        obj = DataTransformation(config=data_transformation_config)
        data = obj.single_predict(data)
        prediction = self.model.predict(data)
        
        return prediction
