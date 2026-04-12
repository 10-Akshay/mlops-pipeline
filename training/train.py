import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
import mlflow
import mlflow.sklearn

# Set MLflow experiment
mlflow.set_experiment("house_price_training")

# Load dataset
data = pd.read_csv("training/data/house_prices.csv")

# Features and target
X = data[["area", "bedrooms"]]
y = data["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Start MLflow run
with mlflow.start_run():

    # Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Accuracy
    r2 = r2_score(y_test, y_pred)
    print(f"R2 Score: {r2}")

    # Log parameters
    mlflow.log_param("model_type", "LinearRegression")

    # Log metrics
    mlflow.log_metric("r2_score", r2)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    # Save model locally
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

print("✅ Training complete. Model saved as model.pkl")