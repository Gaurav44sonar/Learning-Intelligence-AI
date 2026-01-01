import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from app.preprocess import preprocess_data
from app.features import create_student_features


def train_model():
    
    df = pd.read_csv("data/sample_learners.csv")

    # Preprocess and create features
    df = preprocess_data(df)
    features_df = create_student_features(df)

    # Features and target
    X = features_df[["avg_score", "avg_time_spent", "chapters_attempted"]]
    y = features_df["completed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Logistic Regression
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    lr_acc = accuracy_score(y_test, lr_model.predict(X_test))

    # Random Forest
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    rf_acc = accuracy_score(y_test, rf_model.predict(X_test))

    print(f"Logistic Regression Accuracy: {lr_acc}")
    print(f"Random Forest Accuracy: {rf_acc}")

    if rf_acc > lr_acc:
        best_model = rf_model
        print("Selected Model: Random Forest")
    else:
        best_model = lr_model
        print("Selected Model: Logistic Regression")

    # Save model
    joblib.dump(best_model, "models/completion_model.pkl")
    print("Best model saved successfully!")


if __name__ == "__main__":
    train_model()
