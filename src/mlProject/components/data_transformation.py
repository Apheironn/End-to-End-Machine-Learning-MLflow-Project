import os
from mlProject import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig
from pathlib import Path

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_path)
        self.cat_features = self.data.select_dtypes(include="object").columns
        self.num_featues = self.data.select_dtypes(exclude="object").columns
        self.columns = self.data.columns
        
        self.encoder = OneHotEncoder(drop='first', sparse=False)
        self.encoded_data = self.encoder.fit_transform(self.data[self.cat_features])
        self.encoded_columns = self.encoder.get_feature_names_out(input_features=self.cat_features)

    def single_predict(self, data):
        data.insert(1,None)
        data = pd.DataFrame([data], columns=self.columns)
        
        encoded_single_record = self.encoder.transform(data[self.cat_features])   
        encoded_single_record_df = pd.DataFrame(encoded_single_record, columns=self.encoded_columns)
        encoded_single_record_df[self.num_featues] = data[self.num_featues]
        encoded_single_record_df.drop("Price",axis=1,inplace=True)
        
        return encoded_single_record_df

        
    def pipeline(self):

        encoded_df = pd.DataFrame(self.encoded_data, columns=self.encoded_columns)
        encoded_df[self.num_featues] = self.data[self.num_featues]
        
        self.encoded_data = encoded_df

        print(encoded_df.head(1))
        logger.info("Pipeline applied")
        logger.info(encoded_df.shape)
        print(encoded_df.shape)

    def train_test_spliting(self):
        data = self.encoded_data
        # Split the data into training and test sets. (0.80, 0.20) split.
        train, test = train_test_split(data,test_size=0.2,random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)