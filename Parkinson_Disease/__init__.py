from flask import Flask, request, render_template, Blueprint
import joblib
import pickle
import numpy as np
import os
parkinson_bp = Blueprint('parkinson', __name__, template_folder='templates', static_folder='static')

app = Flask(__name__)

# Load the trained model
'''
ValueError: node array from the pickle has an incompatible dtype
fix the model before loading it

'''
#model = joblib.load(open(os.path.join(os.path.dirname(__file__), 'model1.pkl'), "rb"))

# Home route
@parkinson_bp.route('/')
def index():
    return render_template('parkinsson.html')

# Prediction route
@parkinson_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = [float(request.form[feature]) for feature in [
            'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)',
            'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ',
            'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
            'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA',
            'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
        ]]

        # Predict using the model
        prediction = model.predict([data])
        result = "Parkinson's Detected" if prediction[0] == 1 else "No Parkinson's Detected"
        return render_template('index.html', result=result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
