# Machine Learning API

## 📌 Overview
This repository contains an API that serves a Machine Learning model for predictions. The API is built using FastAPI and serves a pre-trained model stored in a pickle file. It receives input in JSON format, processes it, and returns predictions.

## 🚀 Features
- Trains a Machine Learning model and serializes it using `joblib`
- Provides an API endpoint to make predictions
- Accepts JSON input for inference
- Includes a sample `.json` file for testing
- Supports API request handling via a separate script

## 📂 Project Structure
```
📦 ML_API_Repository
 ┣ 📜 model.pkl                # Trained Machine Learning model
 ┣ 📜 api.py                    # FastAPI implementation
 ┣ 📜 request.py                # Script to send test requests to API
 ┣ 📜 sample_input.json         # Example input file
 ┣ 📜 requirements.txt          # List of dependencies
 ┗ 📜 README.md                 # This documentation file
```

## 🛠 Setup & Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📡 Running the API
1. **Start the API Server**
   ```bash
   uvicorn api:app --reload
   ```
   The API will run on `localhost:8000`

2. **Test the API** (Use `request.py` or `curl`)
   ```bash
   python request.py
   ```
   OR
   ```bash
   curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d @sample_input.json
   ```

## 📤 Making a Prediction Request
- Example JSON input (`sample_input.json`):
  ```json
  {
    "feature1": value1,
    "feature2": value2,
    "feature3": value3
  }
  ```
- Example Response:
  ```json
  {
    "prediction": "predicted_value"
  }
  ```

## 📜 Commit & Share
1. **Commit the necessary files**:
   ```bash
   git add api.py model.pkl request.py sample_input.json README.md
   git commit -m "Initial commit - ML API setup"
   git push origin main
   ```
2. **Share the Repository**:
   - Ensure the repository is accessible to the instructor (Icedgarr)
   - Submit the repository link as required

## 🔗 References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn ASGI Server](https://www.uvicorn.org/)
- [Joblib for Model Serialization](https://joblib.readthedocs.io/en/latest/)

## 📌 Notes
- Ensure that the `.pkl` file is stored in the same directory as `api.py`
- The API should be structured to handle errors gracefully
- Modify `request.py` to test with different inputs

🚀 Happy coding!

