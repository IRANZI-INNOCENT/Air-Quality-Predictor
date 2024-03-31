import joblib
import pandas as pd

def predict_input(model_path, single_input):
    # Load the pre-trained AQI prediction model
    aqi_model = joblib.load(model_path)

    # Convert the single_input dictionary into a DataFrame
    input_df = pd.DataFrame([single_input])

    # Make prediction
    pred = aqi_model.predict(input_df)[0]

    # Calculate probability of the predicted class
    prob = aqi_model.predict_proba(input_df)[0][list(aqi_model.classes_).index(pred)]
    prob_percentage = prob * 100  # Convert probability to percentage

    return pred, prob_percentage

if __name__ == "__main__":
    # Example input data
    input1 = {'co':'0.4',
              'no':'0.20',
              'no2':'0.30',
              'o3':'10.40',
              'pm1':'1.50',
              'pm10':'0.70',
              'pm25':'0.060',
              'um003':'1.08',
              'so2':'2.09',
              'temperature':'10'}

    # Path to the pre-trained model file
    model_path = "C:\\ML PROJECT\\DSA App\\Aqi_predict_model.pkl"

    # Call the predict_input function with both arguments
    pred, prob_percentage = predict_input(model_path, input1)

    # Print the predicted class and the probability as a percentage
    print("Predicted AQI Level:", pred)
    print("Probability (%):", round(prob_percentage, 1))
