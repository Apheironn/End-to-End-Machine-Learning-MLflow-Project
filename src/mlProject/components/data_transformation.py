import os
from mlProject import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def pipeline(self):
        data = pd.read_csv(self.config.data_path)
        cat_features = data.select_dtypes(include="object").columns
        encoder = OneHotEncoder()

        encoded_features = encoder.fit_transform(data[cat_features])

        data = pd.get_dummies(data, columns=cat_features)
        self.data = data
        print(data.head(1))
        logger.info("Pipeline applied")
        logger.info(data.shape)
        print(data.shape)

    def train_test_spliting(self):
        data = self.data
        # Split the data into training and test sets. (0.80, 0.20) split.
        train, test = train_test_split(data,test_size=0.2,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)