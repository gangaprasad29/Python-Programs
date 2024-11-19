# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load models
models = {
    'KNN': joblib.load('KNN_model.pkl'),
    'SVC': joblib.load('SVC_model.pkl'),
    'SGD': joblib.load('SGD_model.pkl'),
    'MLP': joblib.load('MLP_model.pkl')
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form
    # Convert form data to a list of feature values
    features = [
        float(form_data['age']), float(form_data['ca']), float(form_data['chol']),
        float(form_data['cp']), float(form_data['exang']), float(form_data['fbs']),
        float(form_data['oldpeak']), float(form_data['restecg']), float(form_data['sex']),
        float(form_data['slope']), float(form_data['thal']), float(form_data['thalach']),
        float(form_data['trestbps'])
    ]
    
    selected_model = form_data['model']
    model = models[selected_model]
    prediction = model.predict([features])[0]

    result = "No heart disease detected" if prediction == 1 else "Heart disease detected"
    return render_template('index.html', prediction_text=f'{selected_model} Model Prediction: {result}')

if __name__ == "__main__":
    app.run(debug=True)
