import pandas as pd
from fastapi import UploadFile, HTTPException

REQUIRED_COLUMNS = {
    "student_id",
    "course_id",
    "chapter_order",
    "time_spent",
    "score",
    "completed"
}

def read_csv(file: UploadFile) -> pd.DataFrame:
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    try:
        df = pd.read_csv(file.file)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    missing_cols = REQUIRED_COLUMNS - set(df.columns)
    if missing_cols:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required columns: {list(missing_cols)}"
        )

    return df
