import requests
import json

# Load input data from the JSON file
with open('input_data.json', 'r') as f:
    data = json.load(f)

# Send a POST request to the API
response = requests.post("http://127.0.0.1:5000/predict_file", json=data)

# Print the prediction response
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Error:", response.status_code, response.text)
