import pandas as pd


def generate_insights(df: pd.DataFrame) -> dict:
    """
    Generate structured insights from model predictions.
    These insights are later converted into natural language
    summaries using Gemini.
    """

    # Identify high-risk students (predicted dropout)
    high_risk_students = df[df["prediction"] == 0]["student_id"].tolist()

    insights = {
        "total_students": int(len(df)),
        "high_risk_students_count": int(len(high_risk_students)),
        "high_risk_students": high_risk_students,
        "key_factors": [
            "Low average assessment scores",
            "Low engagement time across chapters"
        ]
    }

    return insights
