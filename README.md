# 🌸 Iris Flower Classifier — Dockerized

A fully Dockerized Machine Learning web application for classifying Iris flowers (*Setosa*, *Versicolor*, or *Virginica*) using sepal and petal measurements.

The project uses a **Random Forest** classifier implemented with `scikit-learn`, exposed through a **FastAPI** REST API, and includes a clean browser-based user interface.

To ensure reproducibility and simplify deployment, the entire application environment has been containerized using **Docker** and orchestrated with **Docker Compose**.

---

# 📁 Project Structure

```text
iris-classifier/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── model/
│   └── train.py          # Trains and saves the model
└── app/
    ├── main.py           # FastAPI application
    └── index.html        # Frontend web interface
````

---

# ⚙️ System Requirements

Before running the project, ensure the following software is installed:

* Docker Desktop

Download Docker Desktop from:

* [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

After installation, make sure Docker Desktop is actively running before executing any commands.

---

# 🚀 Running the Application

## Option A — Docker Compose (Recommended)

Open a terminal inside the project directory and execute:

```bash
docker compose up --build
```

### First-Time Build Note

During the initial execution, Docker will:

* Build the container image
* Install all Python dependencies
* Train the Random Forest model
* Start the FastAPI server

This process may take several minutes depending on internet speed and system performance.

Subsequent executions will be significantly faster.

---

## Option B — Plain Docker

### Build the Docker Image

```bash
docker build -t iris-classifier .
```

### Run the Container

```bash
docker run -p 8000:8000 iris-classifier
```

---

# 🌐 Accessing the Application

Once the container is running, open your browser and navigate to:

## Web Interface

```text
http://localhost:8000
```

## Interactive API Documentation

```text
http://localhost:8000/docs
```

The `/docs` endpoint provides automatically generated OpenAPI documentation where API requests can be tested directly from the browser.

---

# 🔌 API Endpoints

## POST `/predict`

Predicts the Iris flower species from input measurements.

### Request Body

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Example Response

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

## GET `/health`

Checks server and model status.

### Example Response

```json
{
  "status": "ok",
  "model_loaded": true
}
```

---

# 🤖 Model Details

| Property         | Value                         |
| ---------------- | ----------------------------- |
| Algorithm        | Random Forest Classifier      |
| Number of Trees  | 100                           |
| Dataset          | sklearn Iris Dataset          |
| Dataset Size     | 150 Samples                   |
| Train/Test Split | 80% / 20%                     |
| Accuracy         | ~96–100%                      |
| Target Classes   | setosa, versicolor, virginica |

---

# 🧪 cURL Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length":6.3,"sepal_width":3.3,"petal_length":6.0,"petal_width":2.5}'
```

---

# 🛑 Stopping the Application

To stop the running container:

```bash
Ctrl + C
```

If using Docker Compose, containers can also be stopped with:

```bash
docker compose down
```

---

# 📦 Why Dockerization Was Used

Dockerization was adopted to:

* Eliminate dependency conflicts
* Avoid manual Python environment setup
* Ensure platform-independent execution
* Improve reproducibility across systems
* Simplify evaluation and deployment

The Docker container encapsulates:

* Python runtime environment
* Machine learning dependencies
* Trained model artifacts
* FastAPI application server
* Frontend interface

This guarantees consistent behavior across Windows, macOS, and Linux environments.

---

# ⚠️ Troubleshooting

## Docker daemon is not running

Ensure Docker Desktop is open and fully initialized before running commands.

---

## Port 8000 is already in use

Another application may already be using port `8000`.

Either:

* Stop the conflicting application, or
* Run the container on a different port.

Example:

```bash
docker run -p 8080:8000 iris-classifier
```

Then access:

```text
http://localhost:8080
```

---

## Browser cannot connect to localhost

The application may still be initializing during the first build. Wait a few moments and refresh the page.

---

```
