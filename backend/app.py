from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# Permitir conexión desde cualquier frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo asegurando la ruta absoluta del archivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Modelo de datos recibido desde el formulario
class Transaccion(BaseModel):
    monto: float
    hora: int
    pais_riesgoso: int

@app.get("/")
def home():
    return {"mensaje": "API de modelo funcionando"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: Transaccion):
    caracteristicas = [[data.monto, data.hora, data.pais_riesgoso]]
    pred = int(model.predict(caracteristicas)[0])
    prob = model.predict_proba(caracteristicas)[0].tolist()
    
    return {
        "prediccion": pred,
        "resultado": "Fraude" if pred == 1 else "Legítima",
        "probabilidad_legitima": round(prob[0], 4),
        "probabilidad_fraude": round(prob[1], 4)
    }
