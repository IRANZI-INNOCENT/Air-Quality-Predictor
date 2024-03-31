import streamlit as st
import pandas as pd
from aqi_predict import predict_input

st.title('AIR QUALITY INDEX PREDICTION')
st.markdown('Predict the Air Quality Index (AQI) with accuracy. Set your input parameters below.')

# Input fields
input1 = {'co': 0.100,
          'no': 0.0003,
          'no2': 0.001,
          'o3': 0.000,
          'pm1': 0.000,
          'pm10': 0.150,
          'pm25': 0.000,
          'so2': 0.000,
          'temperature': 5}

st.header("AIR QUALITY PREDICTORS")

# Create input fields with 3 columns
col1, col2, col3 = st.columns(3)

with col1:
    st.text("ATMOSPHERIC AIR")
    co = st.number_input('CO (µg/m³)', min_value=0.100, max_value=1000, step=0.001, value=0.100)
    no = st.number_input('NO (ppm)', min_value=0.0003, max_value=0.0001, step=0.0001, value=0.0003)
    no2 = st.number_input('NO2 (µg/m³)', min_value=0.001, max_value=200, step=0.001, value=0.001)

with col2:
    st.text("PARTICULATE MATTERS")
    pm1 = st.number_input('PM1 (µg/m³)', min_value=0.000, max_value=1000, step=0.001, value=0.000)
    pm10 = st.number_input('PM10 (µg/m³)', min_value=0.150, max_value=1000, step=0.050, value=0.150)
    pm25 = st.number_input('PM2.5 (µg/m³)', min_value=0.000, max_value=1000, step=0.001, value=0.000)

with col3:
    st.text("OTHER PARAMETERS")
    so2 = st.number_input('SO2 (µg/m³)', min_value=0.000, max_value=100, step=0.001, value=0.000)
    temperature = st.number_input('Temperature (°C)', min_value=-20, max_value=50, step=1, value=5)
    o3 = st.number_input('O3 (µg/m³)', min_value=0.000, max_value=200, step=0.001, value=0.000)

# Update input data with user inputs
input1.update({
    'co': str(co),
    'no': str(no),
    'no2': str(no2),
    'o3': str(o3),
    'pm1': str(pm1),
    'pm10': str(pm10),
    'pm25': str(pm25),
    'so2': str(so2),
    'temperature': str(temperature)
})

# Path to the pre-trained model file
model_path = "Aqi_predict_model.pkl"

# Display Predict AQI button
if st.button("Predict AQI"):
    # Call predict_input function with model path and input data
    pred, prob_percentage = predict_input(model_path, input1)
    
    # Display the predicted category and probability
    st.markdown(f'<p style="font-size:36px;font-weight:bold;">Predicted AQI Category: {pred}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="font-size:24px;">Probability of AQI Category: {prob_percentage:.2f}%</p>', unsafe_allow_html=True)

st.text('')
st.text('')
st.markdown('Developed By: IRANZI INNOCENT | `Code:` [GitHub](https://github.com/IRANZI-INNOCENT/Data-Science)')
