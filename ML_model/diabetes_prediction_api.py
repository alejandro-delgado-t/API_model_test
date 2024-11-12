# Excercise 3
import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'random_forest_model.pkl')
model = joblib.load(model_path)

# Excercise 4

# Define an endpoint that accepts JSON files with batch input
@app.route('/predict_file', methods=['POST'])
def predict_file():
    # Check if the request has JSON data
    if request.is_json:
        # Parse the JSON data into a dictionary
        data = request.get_json()

        # Convert the dictionary to a DataFrame for prediction
        input_data = pd.DataFrame([data])
        
        # Select only the columns used by the model
        features_columns = [
            'age', 'height', 'weight', 'aids', 'cirrhosis', 
            'hepatic_failure', 'immunosuppression', 'leukemia', 
            'lymphoma', 'solid_tumor_with_metastasis'
        ]
        input_data = input_data[features_columns]

        # Make prediction using the model
        prediction = model.predict(input_data)[0]

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction)})
    else:
        # Return an error if the input is not JSON
        return jsonify({'error': 'Invalid input format. Please send JSON data.'}), 400

if __name__ == '__main__':
    app.run(debug=True)