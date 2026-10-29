[readme_del_repositorio.md](https://github.com/user-attachments/files/34107144/readme_del_repositorio.md)
# Sistema de Detección de Fraude con Machine Learning y Docker

Solución integral para la clasificación y detección de transacciones fraudulentas en tiempo real, empaquetada mediante microservicios con FastAPI, serialización de modelos de Machine Learning y contenedores Docker.

## 📋 Tabla de Contenidos

* [Descripción General](#-descripción-general)

* [Estructura del Proyecto](#-estructura-del-proyecto)

* [Tecnologías Utilizadas](#-tecnologías-utilizadas)

* [Instalación y Ejecución con Docker](#-instalación-y-ejecución-con-docker)

* [Endpoints de la API](#-endpoints-de-la-api)

* [Pruebas y Validación](#-pruebas-y-validación)

* [Estrategia de Despliegue en la Nube](#-estrategia-de-despliegue-en-la-nube)

* [Autor](#-autor)

## 🔍 Descripción General

El sistema evalúa el riesgo de fraude en transacciones bancarias a partir de tres variables clave:

1. **Monto:** Cantidad monetaria de la operación (\$).

2. **Hora:** Momento del día en el que se ejecuta la transacción (0 a 23 hrs).

3. **País riesgoso:** Indicador binario (1 = País de alto riesgo, 0 = País habitual).

El modelo analítico corresponde a una **Regresión Logística** serializada en `model.pkl`, servida a través de una API REST con **FastAPI** y consumida por una interfaz web ligera (**Frontend**).

## 📁 Estructura del Proyecto

```
fase2/
├── backend/
│   ├── app.py                # Servicio web REST con FastAPI
│   ├── model.pkl             # Modelo entrenado serializado
│   ├── requirements.txt      # Dependencias de Python fijadas
│   └── Dockerfile            # Configuración para construcción del contenedor
├── frontend/
│   ├── index.html            # Interfaz gráfica para pruebas
│   ├── styles.css            # Estilos de la aplicación
│   └── script.js             # Lógica de consumo de API vía Fetch
└── README.md                 # Documentación técnica del repositorio

```

## 🛠 Tecnologías Utilizadas

* **Lenguaje:** Python 3.10

* **Framework API:** FastAPI + Uvicorn

* **Machine Learning:** Scikit-Learn, NumPy

* **Validación de Datos:** Pydantic

* **Contenedores:** Docker (`python:3.10-slim`)

* **Frontend:** HTML5, CSS3, JavaScript (ES6)

## 🚀 Instalación y Ejecución con Docker

### Requisitos previos

* Motor de Docker instalado (Docker Desktop, Linux Docker Engine o entorno interactivo como Killercoda).

### Paso 1: Clonar el repositorio

```
git clone https://github.com/carlosaguayoa-commits/fase2.git
cd fase2/backend

```

### Paso 2: Construir la imagen Docker

```
docker build -t modelo_fraude .

```

### Paso 3: Ejecutar el contenedor

```
docker run -d -p 8000:8000 --name contenedor_fraude modelo_fraude

```

Verificar que el contenedor se encuentre en estado `Up`:

```
docker ps

```

## 🌐 Endpoints de la API

La API expone documentación interactiva Swagger UI de manera nativa en:

`http://localhost:8000/docs`

| **Método** | **Endpoint** | **Descripción** | **Ejemplo de Entrada** | 
| `GET` | `/` | Comprobación de servicio activo | N/A | 
| `GET` | `/health` | Verificación de estado de salud del contenedor | N/A | 
| `POST` | `/predict` | Evaluación de fraude y probabilidades | Ver payload abajo | 

### Ejemplo de Payload (`/predict`)

**Petición JSON:**

```
{
  "monto": 900.0,
  "hora": 1,
  "pais_riesgoso": 1
}

```

**Respuesta JSON:**

```
{
  "prediccion": 1,
  "resultado": "Fraude",
  "probabilidad_legitima": 0.0,
  "probabilidad_fraude": 1.0
}

```

## 🧪 Pruebas y Validación

### Validación directa vía cURL

**Prueba de disponibilidad:**

```
curl http://localhost:8000/

```

**Prueba de inferencia de transacción:**

```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"monto": 900.0, "hora": 1, "pais_riesgoso": 1}'

```

## ☁️ Estrategia de Despliegue en la Nube

El proyecto está diseñado bajo una arquitectura de **Contenedores Serverless / PaaS** (por ejemplo, Render o Cloud Run):

1. **Integración Continua:** Vinculación directa con este repositorio de GitHub.

2. **Entorno Aislado:** Ejecución idéntica en entornos locales y productivos gracias al `Dockerfile`.

3. **Desacoplamiento:** El servicio backend se aloja como un Web Service en contenedor, mientras que el frontend puede servirse de forma estática conectándose mediante HTTPS.

## 👤 Autor

* **Carlos Aguayo** - Repositorio: [@carlosaguayoa-commits](https://github.com/carlosaguayoa-commits)
