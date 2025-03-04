# lifestyle-health-risk-forecasting
# Early Prediction of Lifestyle Diseases

This is a Flask-based web application that predicts lifestyle diseases based on user inputs. The model is trained to assess the likelihood of Hypertension, Depression, and Diabetes based on various lifestyle factors.

## Features
- User-friendly web interface built with Flask and Flask-Material.
- Accepts user inputs related to lifestyle habits.
- Uses a pre-trained machine learning model to predict the likelihood of lifestyle diseases.
- Displays disease predictions along with preventive countermeasures.
- Provides a dataset preview for analysis.

## Technologies Used
- Flask (Python)
- Flask-Material
- Pandas & NumPy
- Machine Learning (Pickle model)
- HTML, CSS (Material Design)

## Installation and Setup
### Prerequisites
Ensure you have Python installed along with the following dependencies:
```sh
pip install flask flask-material pandas numpy
```

### Clone the Repository
```sh
git clone https://github.com/your-repo/early-prediction-of-lifestyle-diseases.git
cd early-prediction-of-lifestyle-diseases
```

### Model Setup
Ensure that your trained machine learning model (`model.pkl`) is placed at the correct path specified in `MODEL_PATH` inside the Python script.

### Running the Application
```sh
python app.py
```
The app will run on `http://127.0.0.1:5000/`.

## Usage
1. Open the web interface in your browser.
2. Enter your health and lifestyle details.
3. Click the analyze button to get a disease prediction.
4. Review the results and suggested countermeasures.

## Project Structure
```
/early-prediction-of-lifestyle-diseases
│── templates/           # HTML templates
│── static/              # CSS & JS files
│── app.py               # Main Flask application
│── model.pkl            # Pre-trained ML model
│── dataset.csv          # Dataset used for training
│── README.md            # Project Documentation
```

## Routes
- `/` → Home page
- `/index` → Prediction form
- `/analyze` → Process user input and predict disease
- `/preview` → View the dataset
- `/hypertension`, `/diabetes`, `/depression` → Disease-specific pages

## Troubleshooting
- **Model not found?** Ensure the `model.pkl` file exists at the defined path.
- **Invalid input errors?** Ensure all input fields contain numerical values.
- **Dataset preview not working?** Confirm that `dataset.csv` is available at the correct path.

## Contributing
Feel free to fork the repository and submit pull requests with improvements.

