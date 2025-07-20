from fastapi import FastAPI, Query
from schemas.prediction import PredictionRequest
from service.predictor import predict

app = FastAPI(title="Personalized Learning Path API")

@app.post("/predict")
def predict_category(request: PredictionRequest):
    request.normalize_scores() 
    data = request.model_dump()
    scores = [data[field] for field in data]
    result = predict(scores, top_k=3)
    return {
        "status": "success",
        "threshold": result["threshold"],
        "predictions": result["result"]
    }