import json
from flask import Flask, render_template, request,Response
import os 
import numpy as np
import pandas as pd
from src.mlProject.pipeline.prediction import PredictionPipeline
import logging
from main import main

logger = logging.getLogger(__name__)
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
            print(request.form)
            age = float(request.form['age'])
            sex = float(request.form['sex'])
            chest_pain_type = float(request.form['chest_pain_type'])
            resting_bp = float(request.form['resting_bp'])
            cholesterol = float(request.form['cholesterol'])

          
          
            if "fasting_blood_sugar" not in request.form.keys():
                fasting_blood_sugar = 0
            else:
                fasting_blood_sugar = float(request.form['fasting_blood_sugar'])

            resting_ecg = float(request.form['resting_ecg'])
            max_heart_rate = float(request.form['max_heart_rate'])
            if "exercise_angina" not in request.form.keys():
                exercise_angina = 0
            else:
                exercise_angina = float(request.form['exercise_angina'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            major_vessels = float(request.form['major_vessels'])
            thal = float(request.form['thal'])

            data = [age, sex, chest_pain_type, resting_bp, cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate, exercise_angina, oldpeak, slope, major_vessels, thal]
            data = np.array(data).reshape(1, 13)

            obj = PredictionPipeline()
            predict = obj.predict(data)
            return render_template('results.html', prediction = str(round(float(predict[0]),3)))

        except Exception as e:
            logger.error(f'The Exception message is: {e}')
            return Response("Error Occurred! %s" % e, status=500)

    else:
        return render_template('index.html')






@app.route('/dashboard')
def dashboard():
    db = pd.read_csv(rf'{os.getcwd()}/artifacts/data_ingestion/heart.csv')
    rdb = pd.read_csv(rf'{os.getcwd()}/artifacts/data_transformation/Resampled_data.csv')
    
    Labels = dict(db.target.value_counts()).keys()
    Values = [str(i) for i in dict(db.target.value_counts()).values()]
    R_Values = [str(i) for i in dict(rdb.target.value_counts()).values()]
    volatil_acidity_mean = [str(round(i, 3)) for i in dict(db.groupby('target').mean()['age']).values()]
    

    return render_template('dashboard.html',
                            labels=json.dumps(list(Labels)),
                            values = json.dumps(list(Values)),
                            V_acidity = json.dumps(volatil_acidity_mean),
                            R_values = json.dumps(list(R_Values))                         
                            )

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port = 8080, debug=True)
