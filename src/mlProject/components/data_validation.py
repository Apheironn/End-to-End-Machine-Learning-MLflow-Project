import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            df = pd.read_csv(self.config.unzip_data_dir)

            df["TorquePower"] = [None if str(i) == "nan" else int(i.split("@")[0]) if len(i.split(" ")) == 1 else int(i.split(" ")[0]) for i in df["Max Torque"]]
            df["TorquePowerRPM"] = [None if str(i) == "nan" else int(i.split("@")[1]) if len(i.split(" ")) == 1 else int(i.split(" ")[-2]) for i in df["Max Torque"]]
            df["HorsePower"] = [None if str(i) == "nan" else int(i.split("@")[0]) if len(i.split(" ")) == 1 else int(i.split(" ")[0]) for i in df["Max Power"]]
            df["HorsePowerRPM"] = [None if str(i) == "nan" else int(i.split("@")[1]) if len(i.split(" ")) == 1 else int(i.split(" ")[-2]) for i in df["Max Power"]]
            df["Engine"] = [None if str(i) == "nan" else int(i.split(" ")[0]) for i in df["Engine"]]
            df.drop(["Max Power","Model","Max Torque"], axis=1, inplace=True)
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
            df.drop_duplicates(inplace=True)
            num_features = df.select_dtypes(exclude="object").columns
            cat_features = df.select_dtypes(include="object").columns
            df[num_features] = df[num_features].fillna(df[num_features].mean())
            df[cat_features] = df[cat_features].fillna(df[cat_features].mode().iloc[0])
            
            data=df
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e