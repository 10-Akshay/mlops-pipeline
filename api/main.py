from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "MLOps API is running"}

@app.post("/predict")
def predict(area: float, bedrooms: int):
    data = np.array([[area, bedrooms]])
    prediction = model.predict(data)
    return {"predicted_price": float(prediction[0])}