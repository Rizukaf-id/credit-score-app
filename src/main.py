from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os

app = FastAPI(title='Credit Scorring API', version='1.0')

# Load Model
model_path = os.path.join(os.path.dirname(__file__), '../models/credit_scoring_model.pkl')

try:
    model = joblib.load(model_path)
    print(f'Model Loaded from : {model_path}')
except Exception as e:
    print(f'Error Loading MOdelL {e}')
    model = None

# Format Input Data
class CreditApplication(BaseModel):
    # Feature Character
    CODE_GENDER: str
    ONT_CHILDREN: int
    EXT_SOURCE_2: float

    # Feature Capacity
    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    
    # Feature Capital
    FLAG_OWN_CAR: str
    FLAG_OWN_REALTY: str

    # Feature Collateral
    AMT_GOODS_PRICE: float

    # Feature Condition
    NAME_INCOME_TYPE: str
    NAME_EDUCATION_TYPE: str
    REGION_RATING_CLIENT: int

# Create Endpoints
@app.get('/')
def home():
    return {'message': 'Credit Scorring API is Online!'}


@app.post('/predict')
def predict_credit_risk(data: CreditApplication):
    if not model:
        raise HTTPException(status_code=500, detail='Model not Loaded')
    
    # convert input user (JSON) to dataframe
    input_data = data.dict()
    df = pd.DataFrame([input_data])

    # Debt t0 Income Ratio
    df['DIR'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']

    # Credit to Income Ratio
    df['CREDIT_TO_INCOME'] = df['AMT_CREDIT'] / df['AMT_INCOME_TOTAL']

    # Loan to Value Ratio
    df['LTV'] = df['AMT_CREDIT'] / df['AMT_CREDIT'] / df['AMT_GOODS_PRICE']

    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Make Prediction
    try:
        prediction_prob = model.predict_proba(df)[0][1]
        prediction_class = model.predict(df)[0]

        result = {
            'prediction': 'Berisiko' if prediction_class == 1 else 'Lancar/Aman',
            'risk_score': float(prediction_prob),
            'status': 'DITOLAK' if prediction_prob > 0.6 else 'DISETUJUI' # treshold adjustable
        }

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))