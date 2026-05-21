# 🌸 Iris Flower Classifier — Dockerized

## Overview

This project is a Dockerized Machine Learning web application that classifies Iris flowers (*Setosa*, *Versicolor*, or *Virginica*) using sepal and petal measurements.

The application uses:

- Random Forest Classifier (`scikit-learn`)
- FastAPI REST API
- Browser-based User Interface
- Docker & Docker Compose for deployment

The model is automatically trained during the Docker image build process and packaged inside the container.

---

# 📋 Prerequisites

Before running the project, ensure that:

1. Docker Desktop is installed.
2. Docker Desktop is running.

Download Docker Desktop:

https://www.docker.com/products/docker-desktop/

You do **not** need to install:

- Python
- pip
- scikit-learn
- FastAPI
- Any additional dependencies

Everything required is contained within the Docker image.

---

# 📁 Project Structure

```text
iris-classifier/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── model/
│   └── train.py
└── app/
    ├── main.py
    └── index.html
```

---

# 🚀 Running the Application

## Step 1: Open a Terminal

Navigate to the project directory:

```bash
cd iris-classifier
```

---

## Step 2: Build and Start the Application

Run:

```bash
docker compose up --build
```

### What happens?

Docker will automatically:

1. Create the application image
2. Install all required dependencies
3. Train the Random Forest model
4. Start the FastAPI server

The first build may take several minutes.

Wait until you see a message similar to:

```text
Application startup complete
```

or

```text
Uvicorn running on http://0.0.0.0:8000
```

---

# 🌐 Accessing the Application

Once the container is running, open a web browser and visit:

### Web Application

```text
http://localhost:8000
```

### API Documentation

```text
http://localhost:8000/docs
```

The API documentation page allows direct testing of the application's endpoints.

---

# 🔌 API Endpoints

## POST /predict

Example Request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example Response:

```json
{
  "flower": "setosa",
  "confidence": 1.0,
  "probabilities": {
    "setosa": 1.0,
    "versicolor": 0.0,
    "virginica": 0.0
  },
  "model_accuracy": 0.9667
}
```

---

## GET /health

Example Response:

```json
{
  "status": "ok",
  "model_loaded": true
}
```

---

# 🤖 Model Information

| Property | Value |
|-----------|-----------|
| Algorithm | Random Forest |
| Trees | 100 |
| Dataset | Iris Dataset |
| Samples | 150 |
| Train/Test Split | 80/20 |
| Accuracy | ~96–100% |

---

# 🧪 Testing with cURL

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"sepal_length":6.3,"sepal_width":3.3,"petal_length":6.0,"petal_width":2.5}'
```

---

# 🛑 Stopping the Application

In the terminal running Docker Compose, press:

```bash
Ctrl + C
```

Then remove the container:

```bash
docker compose down
```

---

# ⚠️ Troubleshooting

## Docker is not running

Start Docker Desktop and wait until it reports that Docker is running.

---

## Port 8000 already in use

Stop the application currently using port 8000, then run:

```bash
docker compose down
docker compose up --build
```

---

## Browser cannot connect

The container may still be starting.

Wait 1–2 minutes and refresh the page.

---

# 📦 Dockerization

This project is intentionally distributed as a Dockerized application to ensure:

- Consistent execution across different operating systems
- No dependency conflicts
- No manual Python installation
- Reproducible machine learning environment
- Simplified evaluation and deployment

All required software, libraries, and trained model artifacts are packaged inside the Docker container.
