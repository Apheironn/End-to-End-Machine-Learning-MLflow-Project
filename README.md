# End-to-End-Machine-Learning-MLflow-Project

### Introduction About the Data :

**The dataset** The goal is to predict `price` of given house (Regression Analysis).

There are 19 independent variables:

*  `Make`                :   Company of the car
*  `Year`                :   Manufacturing Year of the car  
*  `Kilometer`           :   Total kilometers Driven 
*  `Fuel Type`           :   Fuel type of the car 
*  `Transmission`        :   Gear transmission of the car 
*  `Color`               :   Color of the car 
*  `Owner`               :   Number of previous owners 
*  `Seller Type`         :   Tells if car is sold by individual or dealer 
*  `Engine`              :   Engine capacity of the car in cc
*  `Drivetrain`          :   AWD/RWD/FWD
*  `Length`              :   Length of the car in mm
*  `Width`               :   Width of the car in mm
*  `Height`              :   Height of the car in mm
*  `Seating Capacity`    :   Maximum people that can fir in a car
*  `Fuel Tank Capacity`  :   Maximum fuel capacity of the car in litres
*  `TorquePower`         :   Torque power of the car
*  `TorquePowerRPM`      :   Torque power RPM of the car
*  `HorsePower`          :   Horse power of the car
*  `HorsePowerRPM`       :   Horse power RPM of the car

Target variable:
* `price`: Price of the given car.

Dataset Source Link :
https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho?select=car+details+v4.csv

# Screenshot of UI
![HomepageUI](./img/gui.png)
![PredictUI](./img/predict_gui.png)

# Screenshot of MLflow
![MLflow](./img/mlflow.png)


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.11 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
# Open up you local host and port
localhost:8080
```

First go to,
```bash
# You have to train your data first on:
localhost:8080/train
```

Finally,
```bash
# Go back to main address and enter values to estimate the price of the vehicle:
localhost:8080/
```





## dagshub

[dagshub]([https://dagshub.com/](https://dagshub.com/apheiron/End-to-End-Machine-Learning-MLflow-Project))

## MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model
   
[Documentation](https://mlflow.org/docs/latest/index.html)

