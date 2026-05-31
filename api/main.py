
# uvicorn api.main:app --reload          تشغيل api


from fastapi import FastAPI

from api.schemas import FamilyData, PredictionResponse
from src.models.predict import predict_priority

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Aid Priority API is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(data: FamilyData):

    result = predict_priority(data.model_dump())

    return result


