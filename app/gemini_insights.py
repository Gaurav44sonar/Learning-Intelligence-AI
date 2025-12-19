# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()


# def generate_gemini_summary(student_insights: dict, chapter_difficulty: list) -> str:

#     genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#     model = genai.GenerativeModel("models/gemini-2.5-flash")

#     system_prompt = """
# You are a Learning Intelligence Assistant designed to support mentors and administrators of an internship or training platform.

# Your role is strictly limited to:
# - Summarizing structured analytics provided by the system
# - Explaining insights in clear, simple, and professional language
# - Suggesting high-level, non-technical recommendations

# IMPORTANT RULES:
# - Use ONLY the data explicitly provided in the input
# - Do NOT add new facts, assumptions, or predictions
# - Do NOT perform analysis, calculations, or risk scoring
# - Do NOT contradict or override system-generated results
# - Do NOT generate technical or statistical explanations

# Your output should:
# - Be concise and easy to understand
# - Highlight key observations
# - Suggest actionable next steps for mentors
# - Maintain a neutral and professional tone
# """

#     user_prompt = f"""
# Student Risk Insights:
# {student_insights}

# Chapter Difficulty Analysis:
# {chapter_difficulty}
# """

#     response = model.generate_content(
#         contents=[
#             {"role": "system", "parts": [{"text": system_prompt}]},
#             {"role": "user", "parts": [{"text": user_prompt}]}
#         ]
#     )

#     return response.text.strip()



import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def generate_gemini_summary(student_insights: dict, chapter_difficulty: list) -> str:
    """
    Convert structured insights into a human-readable summary
    using Gemini API. Gemini does NOT make predictions or analysis.
    """

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Gemini API key not configured."

    genai.configure(api_key=api_key)

    # ✅ SYSTEM PROMPT goes here (Gemini way)
    system_prompt = """
You are a Learning Intelligence Assistant designed to support mentors and administrators of an internship or training platform.

Your role is strictly limited to:
- Summarizing structured analytics provided by the system
- Explaining insights in clear, simple, and professional language
- Suggesting high-level, non-technical recommendations

IMPORTANT RULES:
- Use ONLY the data explicitly provided in the input
- Do NOT add new facts, assumptions, or predictions
- Do NOT perform analysis, calculations, or risk scoring
- Do NOT contradict or override system-generated results
- Do NOT generate technical or statistical explanations

Your output should:
- Be concise and easy to understand
- Highlight key observations
- Suggest actionable next steps for mentors
- Maintain a neutral and professional tone
- Keep the summary concise while still being actionable.

"""

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_prompt
    )

    # ✅ USER PROMPT (data only)
    user_prompt = f"""
Student Risk Insights:
{student_insights}

Chapter Difficulty Analysis:
{chapter_difficulty}
"""

    response = model.generate_content(user_prompt)

    return response.text.strip()

