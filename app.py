import pickle
from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

# Load the trained RandomForest model
with open('random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

# Route to serve the main page (HTML form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the prediction logic
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the HTML form
    data = request.form

    # Extract features from the form data
    customer_data = np.array([[
        data['gender'], 
        data['SeniorCitizen'], 
        data['Partner'], 
        data['Dependents'],
        data['tenure'], 
        data['PhoneService'], 
        data['MultipleLines'], 
        data['InternetService'],
        data['OnlineSecurity'], 
        data['OnlineBackup'], 
        data['DeviceProtection'], 
        data['TechSupport'],
        data['StreamingTV'], 
        data['StreamingMovies'], 
        data['Contract'], 
        data['PaperlessBilling'],
        data['PaymentMethod'], 
        data['MonthlyCharges'], 
        data['TotalCharges']
    ]])

    # Preprocess categorical features (e.g., one-hot encoding, label encoding) if needed
    # Ensure that the model can accept this form of data

    # Make prediction using the RandomForest model
    prediction = rf_model.predict(customer_data)

    # Return the result to the user
    return render_template('index.html', prediction_result=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True)
