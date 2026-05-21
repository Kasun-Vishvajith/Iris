import os
import pickle
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

MODEL_PATH = "/app/model/iris_model.pkl"

app = FastAPI(title="Iris Flower Classifier", version="1.0.0")

# Load model at startup
payload = None

@app.on_event("startup")
def load_model():
    global payload
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model not found at {MODEL_PATH}. Run train.py first.")
    with open(MODEL_PATH, "rb") as f:
        payload = pickle.load(f)
    print(f"Model loaded. Accuracy: {payload['accuracy']:.4f}")


class IrisInput(BaseModel):
    sepal_length: float = Field(..., ge=4.3, le=7.9, example=5.1)
    sepal_width:  float = Field(..., ge=2.0, le=4.4, example=3.5)
    petal_length: float = Field(..., ge=1.0, le=6.9, example=1.4)
    petal_width:  float = Field(..., ge=0.1, le=2.5, example=0.2)


class PredictionResult(BaseModel):
    flower: str
    confidence: float
    probabilities: dict
    model_accuracy: float


@app.get("/", response_class=HTMLResponse)
def root():
    with open("/app/app/index.html") as f:
        return f.read()

@app.get("/flower.png")
def flower_img():
    from fastapi.responses import FileResponse
    return FileResponse("/app/app/flower.png")


@app.post("/predict", response_model=PredictionResult)
def predict(data: IrisInput):
    if payload is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    model = payload["model"]
    target_names = payload["target_names"]

    features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width,
    ]])

    proba = model.predict_proba(features)[0]
    pred_idx = int(np.argmax(proba))

    return PredictionResult(
        flower=target_names[pred_idx],
        confidence=round(float(proba[pred_idx]), 4),
        probabilities={name: round(float(p), 4) for name, p in zip(target_names, proba)},
        model_accuracy=round(payload["accuracy"], 4),
    )


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": payload is not None}
