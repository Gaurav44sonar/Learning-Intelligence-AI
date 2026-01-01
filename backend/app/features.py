import pandas as pd

def create_student_features(df: pd.DataFrame) -> pd.DataFrame:

    # Group data by student
    student_features = df.groupby("student_id").agg(
        avg_score=("score", "mean"),
        avg_time_spent=("time_spent", "mean"),
        chapters_attempted=("chapter_order", "count"),
        completed=("completed", "max")
    ).reset_index()

    return student_features
