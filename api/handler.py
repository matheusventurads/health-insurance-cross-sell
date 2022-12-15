import pickle
import pandas as pd
from flask                     import Flask, Response, request
from insurance.HealthInsurance import HealthInsurance

# loading model
path = '/home/matheus/repos/health-insurance-cross-sell/'
model = pickle.load(open(path + 'src/models/model_Insurance.pkl', 'rb'))

# initialize API
app = Flask(__name__)

@app.route('/insurance/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance(test_json, dict):# unique example
            test_raw = pd.DataFrame(test_json, index=[0])
        else: # multiple example
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
    
        # Instantiate Rossmann class
        pipeline = HealthInsurance()    
    
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature enginnering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
        
        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)