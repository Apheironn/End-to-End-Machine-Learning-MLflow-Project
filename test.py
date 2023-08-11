from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager


data = ["Honda",2017,87150,"Petrol","Manual","Grey",
        "First","Corporate",1198.0,"FWD",3990.0,1680.0,1505.0,
        5.0,35.0,109.0,4500.0,87.0,6000.0]


config = ConfigurationManager()
data_transformation_config = config.get_data_transformation_config()

obj = DataTransformation(config=data_transformation_config)
data = obj.single_predict(data)
print(data)