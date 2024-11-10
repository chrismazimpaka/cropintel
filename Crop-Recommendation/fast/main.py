from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the saved model and scaler
model = joblib.load('crop_recommendation_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

app = FastAPI()


# Define the input data structure
class CropRecommendationRequest(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


@app.post("/predict")
def predict_crop(data: CropRecommendationRequest):
    # Convert input data to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Ensure the order of features is correct
    input_data = input_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]

    # Scale the input data
    scaled_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_data)

    # Decode the prediction
    decoded_prediction = label_encoder.inverse_transform(prediction)

    return {"recommended_crop": decoded_prediction[0]}

# To run the app, use: `uvicorn main:app --reload`
