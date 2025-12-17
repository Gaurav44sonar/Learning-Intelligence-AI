from fastapi import FastAPI, UploadFile, File
from app.ingest import read_csv

app = FastAPI(
    title="Learning Intelligence AI Tool",
    description="AI-powered tool to analyze learner behavior and predict outcomes",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "LearnIntel AI Tool is up and running"
    }

@app.post("/upload-csv")
def upload_csv(file: UploadFile = File(...)):
    df = read_csv(file)

    return {
        "message": "CSV uploaded successfully",
        "rows": len(df),
        "columns": list(df.columns)
    }
