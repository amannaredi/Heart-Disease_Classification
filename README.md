# Heart Disease Prediction Web Application

This project is a Flask-based web application for predicting whether a patient is likely to have heart disease based on user-provided input. The prediction is powered by a pre-trained machine learning model using a MinMaxScaler for feature scaling and a binary classifier.

## Project Structure

- **templates/**
  - Contains HTML templates used by the Flask application (e.g., `temp.html`).
- **model.pkl**
  - A pre-trained machine learning model serialized using `pickle`.
- **heart-disease.csv**
  - Dataset used to train the model (if available).
- **main.py**
  - The main script containing the Flask application.
- **Deepiotics_heartDisease.pdf**
  - Documentation or report related to the project.
- **heart-disease (1).ipynb**
  - Jupyter Notebook used for data analysis and model training.

## Features

- **Web Interface**: A user-friendly web interface built with HTML templates.
- **Model Integration**: Predicts the likelihood of heart disease using a pre-trained model.
- **Feature Scaling**: Automatically scales user-provided input using MinMaxScaler.
- **Interactive Prediction**: Displays results dynamically based on user input.

## Prerequisites

To run this project, ensure the following dependencies are installed:

- Python 3.7+
- Flask
- scikit-learn
- NumPy

Install the dependencies using the following command:

```bash
pip install flask scikit-learn numpy
```

## How to Run the Application

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name/Heart-Disease_Classification.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Heart-Disease_Classification
   ```
3. Run the Flask application:
   ```bash
   python main.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Input Features

The application takes 13 features as input from the user. These features are scaled using the MinMaxScaler and passed to the model for prediction. Ensure the input values are numeric.

## Model Details

The machine learning model is trained on a heart disease dataset and serialized using `pickle`. It predicts one of the following outcomes:

- **1**: The patient is not likely to have heart disease.
- **0**: The patient is likely to have heart disease.

## Example

1. Navigate to the homepage (`temp.html`).
2. Input the required features into the form.
3. Click the "Predict" button to receive the result.


## Future Enhancements

- Add more user-friendly input forms with dropdowns for categorical variables.
- Enhance the UI using CSS frameworks like Bootstrap.
- Deploy the application on a public server for accessibility.
- Incorporate more sophisticated models for better accuracy.

