import joblib 
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.elasticnet = joblib.load(Path('artifacts/model_trainer/ElasticNet.joblib'))
        self.decisiontree = joblib.load(Path('artifacts/model_trainer/DecisionTree.joblib'))

    
    def predict(self, data):
        elasticnet_prediction = self.elasticnet.predict(data)
        decisiontree_prediction = self.decisiontree.predict(data)

        prediction = (elasticnet_prediction + decisiontree_prediction) / 2

        return prediction