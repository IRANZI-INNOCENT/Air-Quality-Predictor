# AQI Prediction System

## Overview
This project is an **Air Quality Index (AQI) Prediction System** built using **Streamlit** and **scikit-learn**. The system predicts the AQI levels based on user-input atmospheric parameters like CO, NO, NO2, O3, PM1, PM10, PM2.5, SO2, and temperature. The system outputs the predicted AQI category along with the probability of the prediction.

## Project Structure
- `app.py`: Contains the Streamlit web interface that allows users to input air quality parameters and get the predicted AQI level.
- `aqi_predict.py`: Contains the function used to load the pre-trained model and make predictions.
- `Aqi_predict_model.pkl`: A serialized Logistic Regression model trained to predict AQI categories.
- `requirements.txt`: Lists the dependencies required to run the project.

## Features
- **User-friendly Web Interface**: Streamlit-powered web application for entering air quality parameters.
- **Accurate AQI Prediction**: Utilizes a pre-trained model to predict the AQI category.
- **Probability Estimation**: Displays the confidence level (in percentage) of the predicted AQI category.
- **Model Training**: The Logistic Regression model is trained on combined datasets from various global locations to predict AQI categories such as "GOOD", "MODERATE", "POOR", and "SEVERE".
- **Multiple Air Quality Datasets**: Uses air quality data from locations like Nakuru (Kenya), Nairobi (Kenya), Sydney (Australia), New Haven (USA), and more.

## Input Parameters
The following air quality and weather parameters are used to predict AQI:
- **CO** (µg/m³)
- **NO** (ppm)
- **NO2** (µg/m³)
- **O3** (µg/m³)
- **PM1** (µg/m³)
- **PM10** (µg/m³)
- **PM2.5** (µg/m³)
- **SO2** (µg/m³)
- **Temperature** (°C)

## Installation

### Requirements
The project uses Python 3.7+ and the following libraries:
- `streamlit`
- `pandas`
- `scikit-learn`
- `joblib`

To install the necessary packages, run:
```bash
pip install -r requirements.txt
```

### Running the Application
To run the Streamlit web application locally:
```bash
streamlit run app.py
```
This command will open a browser window with the AQI Prediction interface, allowing users to input air quality parameters and get predictions.

## Model Details
- **Model Type**: Logistic Regression
- **Training Data**: The model is trained on air quality data from various cities worldwide, including cities from Kenya, USA, Canada, and Australia.

## Datasets
The AQI prediction system uses air quality data collected from various locations:
- Nakuru, Kenya
- Nairobi, Kenya
- Sydney, Australia
- New Haven, USA
- Belsk, USA
- Kaposvár, Canada

The combined data is pre-processed to handle missing values and standardize units.

## Future Enhancements
- **Add more parameters**: Including additional parameters like humidity and wind speed.
- **Expand datasets**: Incorporating more cities and live AQI data sources.
- **Improve model accuracy**: Experimenting with more advanced machine learning models to improve prediction accuracy.

## Developer
Developed by [IRANZI INNOCENT](https://github.com/IRANZI-INNOCENT/Data-Sciennce).
