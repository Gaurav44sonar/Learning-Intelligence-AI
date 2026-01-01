# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from app.ingest import read_csv
# from app.preprocess import preprocess_data
# from app.features import create_student_features
# from app.model import predict_completion
# from app.insights import generate_insights
# from app.chapter_analysis import analyze_chapter_difficulty
# from app.gemini_insights import generate_gemini_summary



# app = FastAPI(
#     title="Learning Intelligence AI Tool",
#     description="AI-powered tool to analyze learner behavior and predict outcomes for mentors and admins",
#     version="1.0.0"
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # ✅ TEMPORARY
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def health_check():
#     return {
#         "status": "running",
#         "message": "Learning Intelligence AI Tool is up and running"
#     }

# @app.post("/upload-csv")
# def upload_csv(file: UploadFile = File(...)):

#     raw_df = read_csv(file)
#     processed_df = preprocess_data(raw_df)
#     features_df = create_student_features(processed_df)

#     predictions_df = predict_completion(features_df)
#     chapter_difficulty = analyze_chapter_difficulty(processed_df)
#     structured_insights = generate_insights(predictions_df)

#     gemini_summary = generate_gemini_summary(
#         structured_insights,
#         chapter_difficulty
#     )

#     return {
#         "message": "Learning intelligence analysis completed successfully",
#         "student_predictions": predictions_df.to_dict(orient="records"),
#         "chapter_difficulty": chapter_difficulty,
#         "structured_insights": structured_insights,
#         "summary": gemini_summary
#     }


from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# -----------------------------
# Internal imports
# -----------------------------
from app.ingest import read_csv
from app.preprocess import preprocess_data
from app.features import create_student_features
from app.model import predict_completion
from app.insights import generate_insights
from app.chapter_analysis import analyze_chapter_difficulty
from app.gemini_insights import generate_gemini_summary


# -----------------------------
# FastAPI App Init
# -----------------------------
app = FastAPI(
    title="Learning Intelligence AI Tool",
    description="AI-powered tool to analyze learner behavior and predict outcomes for mentors and admins",
    version="1.0.0"
)

# -----------------------------
# CORS (DEV MODE)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ DEV ONLY
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Learning Intelligence AI Tool is up and running"
    }

# -----------------------------
# CSV Upload & Analysis
# -----------------------------
# @app.post("/upload-csv")
# async def upload_csv(file: UploadFile = File(...)):
#     try:
#         # -----------------------------
#         # Validate file
#         # -----------------------------
#         if not file.filename.endswith(".csv"):
#             raise HTTPException(
#                 status_code=400,
#                 detail="Invalid file format. Please upload a CSV file."
#             )

#         # -----------------------------
#         # Pipeline execution
#         # -----------------------------
#         raw_df = read_csv(file)

#         if raw_df.empty:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Uploaded CSV is empty."
#             )

#         processed_df = preprocess_data(raw_df)
#         features_df = create_student_features(processed_df)

#         predictions_df = predict_completion(features_df)
#         chapter_difficulty = analyze_chapter_difficulty(processed_df)
#         structured_insights = generate_insights(predictions_df)

#         gemini_summary = generate_gemini_summary(
#             structured_insights,
#             chapter_difficulty
#         )

#         # -----------------------------
#         # Response
#         # -----------------------------
#         return {
#             "message": "Learning intelligence analysis completed successfully",
#             "student_predictions": predictions_df.to_dict(orient="records"),
#             "chapter_difficulty": chapter_difficulty,
#             "structured_insights": structured_insights,
#             "summary": gemini_summary
#         }

#     except HTTPException as e:
#         # Known validation errors
#         raise e

#     except Exception as e:
#         # Unknown runtime errors
#         raise HTTPException(
#             status_code=500,
#             detail=f"Internal server error: {str(e)}"
#         )


@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        print("📥 File received:", file.filename)

        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Only CSV files allowed")

        raw_df = read_csv(file)
        print("✅ CSV read successfully")

        processed_df = preprocess_data(raw_df)
        print("✅ Preprocessing done")

        features_df = create_student_features(processed_df)
        print("✅ Feature engineering done")

        predictions_df = predict_completion(features_df)
        print("✅ Prediction done")

        chapter_difficulty = analyze_chapter_difficulty(processed_df)
        print("✅ Chapter analysis done")

        structured_insights = generate_insights(predictions_df)
        print("✅ Insights generated")

        gemini_summary = generate_gemini_summary(
            structured_insights,
            chapter_difficulty
        )
        print("✅ Gemini summary generated")

        return {
            "message": "Learning intelligence analysis completed successfully",
            "student_predictions": predictions_df.to_dict(orient="records"),
            "chapter_difficulty": chapter_difficulty,
            "structured_insights": structured_insights,
            "summary": gemini_summary
        }

    except Exception as e:
        print("❌ ERROR:", str(e))   # 🔥 THIS IS KEY
        raise HTTPException(status_code=500, detail=str(e))
