import os
import sys

import joblib
import pandas as pd


class RandomForestClassifier:
    def __init__(self):
        path_to_artifacts = "/Users/sidharthraizada/Krishi-Karma/research/"
        self.values_fill_missing =  joblib.load(path_to_artifacts + "train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "random_forest.joblib")

    
    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        input_data.fillna(self.values_fill_missing)
        # convert categoricals
        for column in [ "state_name", "district_name", "season", "crop"]:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])

        return input_data

    
    def predict(self, input_data):
        return self.model.predict(input_data)


    def postprocessing(self, input_data):
        label = input_data[0]
        if label == 'P':
            label = 'Poor'
        elif label == 'G':
            label = 'Good'
        elif label == 'V':
            label = 'Very Good'
        else:
            label = 'Excellent'
        return {
            "label": label,
            "status": "OK",
            "response": "The crop yield is "+label
        }


    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        
        except Exception as e:
            return {
                "status": "Error", 
                "message": str(e)
            }

        return prediction
