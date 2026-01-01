import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    
    numeric_columns = ["chapter_order", "time_spent", "score", "completed"]

    # Convert columns to numeric
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Handle missing values, If any numeric value is missing, replace it with the column average
    for col in numeric_columns:
        if df[col].isnull().any():
            df[col].fillna(df[col].mean(), inplace=True)

    return df
