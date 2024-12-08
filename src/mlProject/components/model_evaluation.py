import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.mlProject.entity.config_entity import ModelEvaluationConfig
from src.mlProject.utils.common import save_json
from pathlib import Path

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/hamza.bouajila/End-to-End-MLOPS.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="hamza.bouajila"
os.environ["MLFLOW_TRACKING_PASSWORD"]="b8974c8a3d11e3c09f47ea162fd3e766ec534bee"
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        EN = joblib.load(self.config.ElasticNet_path)
        DT = joblib.load(self.config.DecisionTree_path)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            EN_predicted_qualities = EN.predict(test_x)
            (EN_rmse, EN_mae, EN_r2) = self.eval_metrics(test_y, EN_predicted_qualities)
            
            DT_predicted_qualities = DT.predict(test_x)
            (DT_rmse, DT_mae, DT_r2) = self.eval_metrics(test_y, DT_predicted_qualities)
            
            # Saving metrics as local
            scores = {"EN_rmse": EN_rmse, "EN_mae": EN_mae, "EN_r2": EN_r2,"DT_rmse": DT_rmse, "DT_mae": DT_mae, "DT_r2": DT_r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)
            mlflow.log_metrics(scores)
            mlflow.log_params(self.config.all_params)
           


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                mlflow.sklearn.log_model(EN, "ElasticNet", registered_model_name="ElasticnetModel")
                mlflow.sklearn.log_model(DT, "DecisionTree", registered_model_name="DecisionTreeModel")
            else:
                mlflow.sklearn.log_model(EN, "ElasticNet")
                mlflow.sklearn.log_model(DT, "DecisionTree")

    
