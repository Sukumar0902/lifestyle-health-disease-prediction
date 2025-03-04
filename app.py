from flask import Flask, render_template, request
from flask_material import Material
import pandas as pd
import numpy as np
import os
import pickle

# Initialize Flask App
app = Flask(__name__)
Material(app)

# Define Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "D:/manaswini pro/early-prediction-of-lifestyle-diseases/model.pkl")  # Adjust to your actual path

# Load Model for Prediction
def load_model():
    try:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
        print(f" Model Loaded: {type(model)}")  
        return model if hasattr(model, "predict") else None
    except Exception as e:
        print(f" Error loading model: {e}")
        return None

# Helper Function for Prediction
def predict_disease(data, model):
    try:
        print("Input Data for Prediction:", data)

        if hasattr(model, "feature_names_in_"):
            feature_names = list(model.feature_names_in_)  # Get exact order
        else:
            feature_names = ['Age', 'Gender', 'Smoking', 'Excercise', 'Drinking', 
                             'Bmi', 'Sleep', 'Junk', 'Diabetes', 'Hypertension', 'Depression']

        # Convert input into a DataFrame and **reorder columns** to match training order
        data_df = pd.DataFrame([data], columns=feature_names)[feature_names]

        print("Formatted Data for Model:", data_df)

        # Make prediction
        result = model.predict(data_df)
        print("Prediction result:", result)
        return result.item()
    except Exception as e:
        print(f" Prediction Error: {e}")
        return None

# Routes
@app.route('/')
def home_redirect():
    return render_template("home.html")


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/hypertension')
def hypertension():
    return render_template("hypertension.html")

@app.route('/depression')
def depression():
    return render_template("depression.html")

@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")

@app.route('/analyze', methods=["POST"])
def analyze():
    if request.method == 'POST':
        try:
            # List of form fields
            fields = ['age_input', 'gender_choice', 'smoking_input', 'exercise_input', 
                      'drinking_input', 'bmi_input', 'sleep_input', 'junk_input', 
                      'diabetes_input', 'hypertension_input', 'depression_input']
            
            # Get the form data
            sample_data = [request.form.get(field, '0') for field in fields]
            
            # Convert the data to float for calculation and validation
            try:
                clean_data = [float(value) for value in sample_data]
            except ValueError:
                return render_template('index.html', error_message="Invalid input. Please enter numeric values.")
            
            # Extract the specific inputs from clean_data
            sleep = clean_data[6]     # sleep input (index 5)
            junk_food = clean_data[4] # junk food input (index 7)
            smoking = clean_data[7]   # smoking input (index 2)
            exercise = clean_data[3]  # exercise input (index 3)
            drinking = clean_data[2]  # drinking input (index 4)

            # Debug: Print the values to make sure they're correct
            print(f"Sleep: {sleep}, Junk Food: {junk_food}, Smoking: {smoking}, Exercise: {exercise}, Drinking: {drinking}")

            # Check if all the conditions are met for "No disease predicted"
            if sleep==2 and junk_food == 0 and smoking == 0 and exercise > 0 and drinking == 0:
                # If conditions are met, set the result to "No disease predicted"
                result_prediction = 4  # 4 corresponds to "No disease predicted"
                prediction_message = "You are healthy. No disease predicted.\nMaintain a healthy lifestyle and monitor your health."
            else:
                # If the conditions are not met, use the model for prediction
                model = load_model()
                if model:
                    result_prediction = predict_disease(clean_data, model)
                    if result_prediction is None:
                        prediction_message = "Error during prediction. Try again."
                    else:
                        disease_map = {1: "Depression", 2: "Diabetes", 3: "Hypertension", 4: "No disease predicted"}
                        countermeasures = {
                            "Depression": " leads to Cardiovascular disease, Cancer and Respiratory diseases so take care of yourself. Get enough sleep, eat well, and exercise regularly.",
                            "Diabetes": " Drink water as your primary beverage, avoid sugary drinks.",
                            "Hypertension": " leads to kidney disease, Heart disease, stroke, severe headaches and chest pain so reduce sodium in your diet, avoid excessive alcohol consumption.",
                            "No disease predicted": "Maintain a healthy lifestyle and monitor your health."
                        }
                        predicted_disease = disease_map.get(result_prediction, "Unknown disease")
                        prediction_message = f" {predicted_disease}\n{countermeasures.get(predicted_disease, 'No advice available.')}"
                else:
                    prediction_message = "Model not available."

            return render_template(
                'index.html',
                **{field: sample_data[i] for i, field in enumerate(fields)},
                result_prediction=prediction_message
            )
        except Exception as e:
            print(f" Error in analyze route: {e}")
            return render_template('index.html', error_message="An error occurred during analysis.")

def load_dataset():
    try:
        # Assuming the dataset is in a CSV file called 'dataset.csv'
        df = pd.read_csv('D:/manaswini pro/early-prediction-of-lifestyle-diseases/d_sih.csv')
        return df
    except FileNotFoundError:
        return None
@app.route('/preview')
def preview():
    df = load_dataset()
    if df is not None:
        return render_template("preview.html", df_view=df.to_html(classes='table table-striped'))
    else:
        return render_template("preview.html", error_message="Dataset not found!")
    
if __name__ == '__main__':
    app.run(debug=True)
