import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import joblib

# Read data from CSV files
nakuru = pd.read_csv("C:\\ML PROJECT\\DSA App\\Nakuru.csv")
nyayo = pd.read_csv("C:\\ML PROJECT\\DSA App\\Nyayo Embakasi.csv")
obsterd = pd.read_csv("C:\\ML PROJECT\\DSA App\\Obesterd.csv")
sydney = pd.read_csv("C:\\ML PROJECT\\DSA App\\Sydney Australia.csv")
new_haven = pd.read_csv("C:\\ML PROJECT\\DSA App\\New Haven_ USA.csv")
belsk = pd.read_csv("C:\\ML PROJECT\\DSA App\\Belsk_USA.csv")
kaposvar = pd.read_csv("C:\\ML PROJECT\\DSA App\\Kaposvar_Canada.csv")

# Combine data from all cities
cities1 = pd.concat([nakuru, nyayo, obsterd, sydney, new_haven, belsk, kaposvar], ignore_index=True)

# Replace location names for clarity
cities1['location_name'] = cities1['location_name'].replace({
    'Malkia, Nakuru (DBUSY3473 → ATQJXRNT)': 'Nakuru_Kenya',
    'Nyayo Embakasi, Nairobi': 'Nairobi_Kenya',
    'Belsk Duży, IGF PAN': 'Belsk_USA',
    'Hauptstraße Oberstedten': 'Obsterd_USA',
    'Sydney, Australia': 'Sydney_Australia',
    'New Haven': 'New Haven_USA',
    'Kaposvár': 'Kaposvár_Canada'
})

# Pivot table for better data organization
#data = cities1.pivot_table(index=['location_name', 'datetimeLocal', 'timezone', 'latitude', 'longitude'],
                          # columns='parameter', values='value').reset_index()

# Handling missing values
data.fillna({
    "co": data["co"].mode()[0],
    "no": data["no"].mode()[0],
    "no2": data["no2"].mode()[0],
    "o3": data["o3"].mode()[0],
    "so2": data["so2"].mean(),
    "pm1": data["pm1"].mode()[0],
    "pm25": data["pm25"].std(),
    "pm10": data["pm10"].mean(),
    "um003": data["um003"].std(),
    "temperature": data["temperature"].mode()[0]
}, inplace=True)

# Calculating average AQI
data["Average"] = ((data['co'] + data['no'] + data['no2'] + data['o3'] + data['pm1'] + data['pm25'] +
                   data['temperature'] + data['so2'] + data['pm10']) / 9)

# Defining AQI levels
def average_aqi(x):
    if x <= 50:
        return "GOOD"
    elif x <= 100:
        return "MODERATE"
    elif x <= 150:
        return "POOR"
    else:
        return "SEVERE"

data["AQI Levels"] = data["Average"].apply(average_aqi)

# Features and target variable
X = data[['co', 'no', 'no2', 'o3', 'pm1', 'pm10', 'pm25', 'so2', 'temperature']].values
y = data['AQI Levels'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Scaling features
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

# Model training
model = LogisticRegression(solver='liblinear')
model.fit(X_train_scaled, y_train)

# Save the trained model
joblib.dump(model, 'Aqi_predict_model.pkl')

# Sample input data
input1 = {'co': 0.4, 'no': 0.20, 'no2': 0.30, 'o3': 10.40, 'pm1': 1.50,
          'pm10': 0.70, 'pm25': 0.060, 'so2': 2.09, 'temperature': 10}

def predict_input(model, single_input):
    # Make prediction
    pred = model.predict([single_input])[0]

    # Calculate probability of the predicted class
    prob = model.predict_proba([single_input])[0][list(model.classes_).index(pred)]
    prob_percentage = prob * 100  # Convert probability to percentage

    return pred, prob_percentage

# Call the predict_input function with the trained model and the input sample
pred, prob_percentage = predict_input(model, list(input1.values()))

# Print the predicted class and the probability as a percentage
print("Predicted AQI Level:", pred)
print("Probability (%):", round(prob_percentage, 1))
