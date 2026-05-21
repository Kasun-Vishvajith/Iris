import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

def train_and_save():
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # Save model + metadata
    payload = {
        "model": model,
        "feature_names": iris.feature_names,
        "target_names": list(iris.target_names),
        "accuracy": acc,
    }
    with open("/app/model/iris_model.pkl", "wb") as f:
        pickle.dump(payload, f)
    print("Model saved to /app/model/iris_model.pkl")

if __name__ == "__main__":
    train_and_save()
