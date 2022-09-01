import numpy as np
import pickle
from flask import Flask, request, render_template , url_for
from sklearn.preprocessing import MinMaxScaler

def pipeline(features):
    x = MinMaxScaler().fit_transform(features)
    return np.array(x)

# Load ML model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('temp.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # pipeline function
    scaled_feats = pipeline(array_features)
    scaled_feats = scaled_feats.reshape(-1,13)
    # Predict features
    prediction = model.predict(scaled_feats)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('temp.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('temp.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run(debug = True)