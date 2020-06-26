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
        try:
            # JSON to pandas DataFrame
            input_data = pd.DataFrame(input_data, index=[0])
            # fill missing values
            input_data.fillna(self.values_fill_missing)
            # convert categoricals
            for column in [ "state_name", "district_name", "season", "crop"]:
                categorical_convert = self.encoders[column]
                input_data[column] = categorical_convert.transform(input_data[column])

            return input_data
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('RRRRRRR$$$$$$$$$$$$$$$$$$')
            print()
            print(exc_type)
            print('RRRRRRR$$$$$$$$$$$$$$$$$$')
            print()
            print(fname)
            print('RRRRRRR$$$$$$$$$$$$$$$$$$')
            print()
            print(exc_tb.tb_lineno)
            print('RRRRRRR$$$$$$$$$$$$$$$$$$')
            print()
            print(str(e))
            return ''

    
    def predict(self, input_data):
        return self.model.predict_proba(input_data)


    def postprocessing(self, input_data):
        label = "Poor"
        if input_data[1] > 0.5:
            label = ">50K"
        return {
            "probability": input_data[1], 
            "label": label, 
            "status": "OK"
        }


    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('+++++++++++++++++++++++++++++++')
            print()
            print(exc_type)
            print('+++++++++++++++++++++++++++++++')
            print()
            print(fname)
            print('+++++++++++++++++++++++++++++++')
            print()
            print(exc_tb.tb_lineno)
            print('+++++++++++++++++++++++++++++++')
            print()
            print(str(e))
            return {
                "status": "Error", 
                "message": str(e)
            }

        return prediction
