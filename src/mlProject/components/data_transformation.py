import os
from src.mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlProject.entity.config_entity import DataTransformationConfig
from imblearn.over_sampling import SVMSMOTE


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def resampling_data(self):
        data = pd.read_csv(self.config.data_path)
        X = data.drop(columns=['target'])
        y = data['target']
        sm = SVMSMOTE()
        X_res, y_res = sm.fit_resample(X, y)
        Resampled_data = pd.concat([X_res, y_res], axis=1)
        Resampled_data.to_csv(os.path.join(self.config.root_dir, "Resampled_data.csv"),index = False)
        logger.info("Resampling data to be balanced")
        logger.info(data.target.value_counts())
        logger.info(Resampled_data.target.value_counts())



    def train_test_spliting(self):
        data = pd.read_csv(os.path.join(self.config.root_dir, "Resampled_data.csv"))
        train, test = train_test_split(data)
        
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        
        