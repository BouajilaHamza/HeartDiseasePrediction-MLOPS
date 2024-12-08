import pandas as pd
import os
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
import joblib
from src.mlProject.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio)
        lr.fit(train_x, train_y)
        
        dt = DecisionTreeRegressor(criterion=self.config.criterion, 
                                    max_depth=self.config.max_depth, 
                                    splitter= self.config.splitter, 
                                    min_samples_split=self.config.min_samples_split, 
                                    min_samples_leaf=self.config.min_samples_leaf, 
                                    min_weight_fraction_leaf=self.config.min_weight_fraction_leaf, 
                                    max_features=self.config.max_features)
        dt.fit(train_x, train_y)
        
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.ElasticNet))
        joblib.dump(dt, os.path.join(self.config.root_dir, self.config.DecisionTree))