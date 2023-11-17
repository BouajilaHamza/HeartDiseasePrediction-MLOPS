import json
from flask import Flask, jsonify, render_template, request
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
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)            

            return render_template('results.html', prediction = str(round(float(predict[0]),3)))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')






@app.route('/dashboard')
def dashboard():
    db = pd.read_csv(r'C:\Users\LENOVO\Desktop\Hamza Bouajila\3IDSD SD\MLOPS\Projects\End-to-End-MLOPS\artifacts\data_ingestion\winequality-red.csv')
    Labels = dict(db.quality.value_counts()).keys()
    Values = [str(i) for i in dict(db.quality.value_counts()).values()]
    volatil_acidity_mean = [str(round(i, 3)) for i in dict(db.groupby('quality').mean()['volatile acidity']).values()]
    

    return render_template('dashboard.html',
                            labels=json.dumps(list(Labels)),
                            values = json.dumps(list(Values)),
                            V_acidity = json.dumps(volatil_acidity_mean),
                            db_data = jsonify(db.to_dict(orient='records'))
                        )

if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)
