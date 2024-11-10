import streamlit as st
import requests

# API endpoint
url = "http://127.0.0.1:8000/predict"

st.title("Crop Recommendation System")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=300.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=300.0)
K = st.number_input("Potassium (K)", min_value=0.0, max_value=300.0)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0)

if st.button("Predict"):
    # Create input data for API
    input_data = {
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }
    
    # Make a POST request to the API
    response = requests.post(url, json=input_data)
    
    # Parse the response
    if response.status_code == 200:
        result = response.json()
        st.success(f"Recommended Crop: {result['recommended_crop']}")
    else:
        st.error("Error in prediction. Please check the input values.")

