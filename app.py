from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            print("post")
            brand       =   str(request.form["brand"]) 
            year        =   int(request.form["year"])  
            kilometer   =   int(request.form["kilometer"])  
            fuel_type   =   str(request.form["fuel_type"]) 
            transmission =   str(request.form["transmission"]) 
            color        =   str(request.form["color"]) 
            owner        =  str(request.form["owner"]) 
            seller_type   =   str(request.form["seller_type"]) 
            engine        =  int(request.form["engine"])
            drivetrain    =  str(request.form["drivetrain"]) 
            length        =  int(request.form["length"])
            width        =   int(request.form["width"])
            height       =  int(request.form["height"])
            seating    =   int(request.form["seating"])
            fuel_tank  =   int(request.form["fuel_tank"])
            torque_power    =   int(request.form["torque_power"])
            tp_rpm    =   int(request.form["tp_rpm"])
            horse_power     =   int(request.form["horse_power"])
            hp_rpm    =  int(request.form["hp_rpm"])

            data = [brand, year, kilometer, fuel_type, transmission, color,
                    owner, seller_type, engine, drivetrain, length, width,
                    height, seating, fuel_tank, torque_power, tp_rpm, horse_power, hp_rpm]
            
            obj = PredictionPipeline()
            predict = obj.predict(data)
            print(predict)

            return render_template('results.html', prediction = str("{:.2f}".format(predict[0])))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)