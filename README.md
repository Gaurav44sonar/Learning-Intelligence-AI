# Learning-Intelligence-AI

## 1. Overview

The Learning Intelligence AI Tool is a practical, executable AI system built to analyze learner data from internship or training programs. It processes learner interaction records and produces predictions and analytics that help mentors and administrators monitor student progress and engagement.

The tool predicts course completion outcomes, flags students at risk of dropping out, and identifies challenging course chapters based on engagement and performance metrics. It is designed to demonstrate real-world AI engineering practices, including offline model training, structured pipelines, and API-based inference.

## 2. What the AI Tool Does
   The system provides the following capabilities:
      ### 1. Course Completion Prediction
              Predicts whether a student will complete a course (binary classification).
      ### 2. Early Risk Detection
              Identifies students likely to drop out early based on behavior and performance.
      ### 3. Chapter Difficulty Detection
              Detects difficult chapters using engagement time, assessment scores, and dropout rates.
      ### 4. Insight Generation
              Produces structured insights and optional human-readable summaries for mentors and administrators.

## 3. System Architecture
   ### The tool follows a production-style AI pipeline:

                CSV Upload
                    ↓
              Data Ingestion
                    ↓
               Preprocessing
                    ↓
            Feature Engineering
                    ↓
      Machine Learning Model Inference
                    ↓
    Rule-based Chapter Difficulty Analysis
                    ↓
            Structured Insights
                    ↓
      Gemini-based Human-readable Summary

   ### Model training is performed offline
   ### Prediction and analysis are executed inside the running tool

## 4. AI Models and Feature Choices
   ### Machine Learning Model
   
   1. Problem Type: Binary Classification (Course Completion)

   2. Algorithms Explored:
      1. Logistic Regression
      2. Random Forest

   3. Model Selection:
      The final model is selected based on validation accuracy.

   4. Model Persistence:
      The trained model is saved and loaded using joblib.

## 5. Feature Engineering

   ### Student-level features engineered from raw learner data:
   1. Average assessment score

   2. Average time spent per chapter

   3. Number of chapters attempted

   These features were selected to capture learner engagement and performance patterns.

## 6. Chapter Difficulty Detection

   ### Chapter difficulty is identified using rule-based analytics to ensure transparency and explainability.

   Metrics used:

   1. Dropout rate per chapter

   2. Average time spent

   3. Average assessment score

   ### A normalized difficulty index is computed to classify chapters as:

   1. LOW

   2. MEDIUM

   3. HIGH

This approach avoids unnecessary machine learning and keeps the logic interpretable.

## 7. Input Format

   ### The tool accepts learner data in CSV format with the following required columns:

   1. student_id

   2. course_id

   3. chapter_order

   4. time_spent

   5. score

   6. completed

## 8. Output Format

   ### The API returns a JSON response containing:

   Student-level completion predictions

   High-risk student identification

   Chapter difficulty analysis

   Structured insights

   Optional human-readable summary for mentors and admins

## 9. How to Run the Tool Locally
   
   1. Clone the Repository
      ```bash
      git clone <your-github-repo-url>
      cd Learning-Intelligence-AI
      
   2. Create and Activate a Virtual Environment
      Windows
      ```bash
            python -m venv venv
            venv\Scripts\activate

   3. Install Required Dependencies
      ```bash
         pip install -r requirements.txt
   
   4. Configure Environment Variables (Gemini API)
      Add the following line to your `.env` file:

      `GEMINI_API_KEY=your_gemini_api_key_here`
      Make sure .env is added to .gitignore.
   
   5. Run the FastAPI Server
      ```bash
         uvicorn app.main:app --reload
   If the server starts successfully, you should see output similar to:

   `Uvicorn running on http://127.0.0.1:8000`

   6. Use the API

      Open your browser and go to:
         `http://127.0.0.1:8000/docs`

      Use the /upload-csv endpoint to upload a learner data CSV file.

      ### The API will return:

      Student completion predictions

      High-risk student identification

      Chapter difficulty analysis

      Structured insights

      Optional human-readable summary



AI Usage Disclosure (Mandatory)
What AI Assistance Was Used

ChatGPT was used during development for:

Concept clarification

Architectural guidance

Documentation refinement

Gemini API is used inside the tool only to generate human-readable summaries from structured insights.

What Logic Was Written Independently

Machine learning model training and inference

Feature engineering

Early risk detection logic

Chapter difficulty analysis

API implementation and system architecture

Data preprocessing and validation

How Outputs Were Verified

Model predictions were validated using train-test splits and accuracy metrics.

Chapter difficulty analysis was verified using computed engagement and performance statistics.

Gemini output is constrained by a strict system instruction and only summarizes system-generated results.

Gemini does not perform predictions, analysis, or decision-making.

Responsible AI Statement

Generative AI is used strictly as an explainability layer.
All analytical decisions are deterministic, reproducible, and handled by the system’s own logic.

Compliance Statement

This project is a fully executable AI tool, not a notebook-based experiment.
It adheres to all assessment requirements regarding transparency, reproducibility, and responsible AI usage.
