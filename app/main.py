from fastapi import FastAPI, UploadFile, File

from app.ingest import read_csv
from app.preprocess import preprocess_data
from app.features import create_student_features
from app.model import predict_completion
from app.insights import generate_insights
from app.chapter_analysis import analyze_chapter_difficulty
from app.gemini_insights import generate_gemini_summary



app = FastAPI(
    title="Learning Intelligence AI Tool",
    description="AI-powered tool to analyze learner behavior and predict outcomes for mentors and admins",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Learning Intelligence AI Tool is up and running"
    }

@app.post("/upload-csv")
def upload_csv(file: UploadFile = File(...)):

    raw_df = read_csv(file)
    processed_df = preprocess_data(raw_df)
    features_df = create_student_features(processed_df)

    predictions_df = predict_completion(features_df)
    chapter_difficulty = analyze_chapter_difficulty(processed_df)
    structured_insights = generate_insights(predictions_df)

    gemini_summary = generate_gemini_summary(
        structured_insights,
        chapter_difficulty
    )

    return {
        "message": "Learning intelligence analysis completed successfully",
        "student_predictions": predictions_df.to_dict(orient="records"),
        "chapter_difficulty": chapter_difficulty,
        "structured_insights": structured_insights,
        "summary": gemini_summary
    }
