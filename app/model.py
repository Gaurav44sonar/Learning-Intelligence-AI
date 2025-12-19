import joblib
import pandas as pd

model = joblib.load("models/completion_model.pkl")

def predict_completion(features_df: pd.DataFrame) -> pd.DataFrame:
   
    X = features_df[["avg_score", "avg_time_spent", "chapters_attempted"]]

    # Prediction: 1 = complete, 0 = dropout
    predictions = model.predict(X)

    features_df["prediction"] = predictions
    return features_df
