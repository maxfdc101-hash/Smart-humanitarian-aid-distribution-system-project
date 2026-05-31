
import pandas as pd

from src.models.model_loader import model, scaler

from src.features.feature_engineering import feature_engineering



# Priority level

def get_priority_level(score):
   if score >= 0.8:
      return "High"

   elif score >= 0.5:
      return "Medium"

   else:
      return "Low"

# Prediction function

def predict_priority(data):

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # Apply feature engineering
    df = feature_engineering(df)



    # Scaling
    scaled_data = scaler.transform(df)

    # Prediction
    prediction = model.predict(scaled_data)

    score = float(prediction[0])

    level = get_priority_level(score)

    return {
        "PriorityScore": round(score, 3),
        "PriorityLevel": level
    }


