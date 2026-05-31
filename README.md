
# Aid Priority System

## Overview

Aid Priority System is a Machine Learning project designed to prioritize families for humanitarian aid distribution based on socioeconomic factors.

The system:

* Cleans and preprocesses data
* Applies feature engineering
* Calculates priority scores
* Trains a machine learning model
* Exposes predictions through a FastAPI service

---

## Project Structure

aid-priority-system/

* data/

  * raw/
  * processed/

* notebooks/

  * experiments.ipynb

* src/

  * preprocessing/
      * __init__.py
      * clean_data.py
      * load_data.py

  * features/
      * __init__.py
      * encoding.py
      * feature_engineering.py

  * scoring/
      * priority_score.py

  * models/
      * model_loader.py
      * predict.py
      * train.py
      
* api/

  * main.py
  * schemas.py

* models/

  * priority_model.pkl
  * scaler.pkl

---

## Features

* Data Cleaning
* Feature Engineering
* Priority Score Calculation
* Machine Learning Prediction
* REST API with FastAPI
* Input Validation
* Health Monitoring Endpoint

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Run API

uvicorn api.main:app --reload

---

## API Endpoints

### Home

GET /

Response:

{
"message": "Aid Priority API is running"
}

---

### Health Check

GET /health

Response:

{
"status": "healthy"
}

---

### Predict

POST /predict

Request:

{
"SpecialCase": 1,
"Income": 1500,
"FamilyMembers": 8,
"Housing": 1
}

Response:

{
"PriorityScore": 0.79,
"PriorityLevel": "Medium"
}

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* FastAPI
* Uvicorn
* OpenPyXL

---

## Future Improvements

* Docker Support
* CI/CD Pipeline
* Cloud Deployment
* Advanced Feature Engineering
* Real-time Data Integration


