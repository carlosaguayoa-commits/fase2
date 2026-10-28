from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Cargar el modelo
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "proyecto": "API de Detección de Fraude",
        "estado": "Activo",
        "version": "1.0.0"
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        monto = float(data["monto"])
        hora = int(data["hora"])
        pais_riesgoso = int(data["pais_riesgoso"])
        
        features = [[monto, hora, pais_riesgoso]]
        pred = int(model.predict(features)[0])
        probabilidades = model.predict_proba(features)[0].tolist()
        
        return jsonify({
            "prediccion": pred,
            "resultado": "Fraude" if pred == 1 else "Legítima",
            "probabilidad_legitima": round(probabilidades[0], 4),
            "probabilidad_fraude": round(probabilidades[1], 4)
        }), 200
    except KeyError as e:
        return jsonify({"error": f"Falta el campo obligatorio: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
