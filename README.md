# 🌸 Iris Flower Classifier

A Machine Learning web application that classifies Iris flowers (*Setosa*, *Versicolor*, or *Virginica*) using sepal and petal measurements.

The project uses a **Random Forest Classifier** implemented with `scikit-learn`, exposed through a **FastAPI** REST API, and includes a browser-based user interface.

---

# 📁 Project Structure

```text
iris-classifier/
├── requirements.txt
├── model/
│   └── train.py          # Trains and saves the model
└── app/
    ├── main.py           # FastAPI application
    └── index.html        # Frontend web interface
```

---

# ⚙️ System Requirements

Please ensure the following software is installed:

- Python 3.10 or newer
- pip (Python package manager)

Verify installation:

```bash
python --version
pip --version
```

---

# 📥 Installation

## Step 1: Extract the Project

Download and extract the project files to a convenient location.

---

## Step 2: Open a Terminal

Navigate to the project folder:

```bash
cd iris-classifier
```

---

## Step 3: Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:

- FastAPI
- Uvicorn
- Scikit-learn
- NumPy
- Joblib
- Other required libraries

---

# 🤖 Train the Model

Before starting the application, train the Random Forest model:

```bash
python model/train.py
```

The script will:

- Load the Iris dataset
- Train the classifier
- Evaluate performance
- Save the trained model

---

# 🚀 Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

You should see output similar to:

```text
Application startup complete.
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 Accessing the Application

Once the server is running, open:

## Web Interface

```text
http://localhost:8000
```

## API Documentation

```text
http://localhost:8000/docs
```

The API documentation allows endpoints to be tested directly from the browser.

---

# 🔌 API Endpoints

## POST `/predict`

Predicts the Iris flower species.

### Request

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Response

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

```json
{
  "status": "ok",
  "model_loaded": true
}
```

---

# 🤖 Model Details

| Property | Value |
|-----------|--------|
| Algorithm | Random Forest Classifier |
| Number of Trees | 100 |
| Dataset | Iris Dataset |
| Dataset Size | 150 Samples |
| Train/Test Split | 80% / 20% |
| Accuracy | ~96–100% |
| Classes | Setosa, Versicolor, Virginica |

---

# 🧪 Example Request Using cURL

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d "{\"sepal_length\":6.3,\"sepal_width\":3.3,\"petal_length\":6.0,\"petal_width\":2.5}"
```

---

# 🛑 Stopping the Application

Press:

```bash
Ctrl + C
```

in the terminal running the FastAPI server.

---

# ⚠️ Troubleshooting

## Module Not Found Error

Ensure all dependencies have been installed:

```bash
pip install -r requirements.txt
```

---

## Model File Missing

Run:

```bash
python model/train.py
```

before starting the application.

---

## Port 8000 Already in Use

Run on a different port:

```bash
uvicorn app.main:app --reload --port 8080
```

Then open:

```text
http://localhost:8080
```

---
