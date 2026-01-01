import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()




# def generate_gemini_summary(student_insights: dict, chapter_difficulty: list) -> str:
#     api_key = os.getenv("GEMINI_API_KEY")
#     if not api_key:
#         return "Gemini API key not configured."

#     genai.configure(api_key=api_key)

#     # -----------------------------
#     # System Prompt (UNCHANGED)
#     # -----------------------------
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
# - Keep the summary concise while still being actionable.
# """

#     # -----------------------------
#     # User Data Prompt
#     # -----------------------------
#     user_prompt = f"""
# Student Risk Insights:
# {student_insights}

# Chapter Difficulty Analysis:
# {chapter_difficulty}
# """

#     # -----------------------------
#     # Gemini Model
#     # -----------------------------
#     model = genai.GenerativeModel("gemini-2.5-flash")

#     # -----------------------------
#     # Combine system + user prompt
#     # -----------------------------
#     final_prompt = f"""
# {system_prompt}

# --- DATA PROVIDED BELOW (DO NOT ADD EXTERNAL INFORMATION) ---

# {user_prompt}
# """

#     try:
#         response = model.generate_content(final_prompt)
#         return response.text.strip()

#     except Exception as e:
#         return f"Gemini summary generation failed: {str(e)}"


def generate_gemini_summary(student_insights: dict, chapter_difficulty: list) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Gemini API key not configured."

    genai.configure(api_key=api_key)

    # -----------------------------
    # System Prompt (UNCHANGED)
    # -----------------------------
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

    # -----------------------------
    # USER PROMPT (IMPROVED FORMAT)
    # -----------------------------
    user_prompt = f"""
You must format the response using STRICT Markdown rules.

FORMAT RULES (MANDATORY):
- Use numbered section headers exactly as:
  **1. Student Risk Insights**
  **2. Chapter Difficulty Analysis**

- Inside each section, use ONLY these subheadings (bold):
  **Observation**
  **Key Factors**
  **Mentor Recommendations**

- Use bullet points ONLY with "-" (dash)
- Do NOT use paragraphs for lists
- Do NOT invent data
- Do NOT include emojis
- Do NOT include introductions or conclusions
- Do NOT include titles outside the numbered sections

--------------------
DATA PROVIDED BELOW:
--------------------

Student Risk Insights:
{student_insights}

Chapter Difficulty Analysis:
{chapter_difficulty}
"""

    # -----------------------------
    # Gemini Model
    # -----------------------------
    model = genai.GenerativeModel("gemini-2.5-flash")

    # -----------------------------
    # Final Prompt
    # -----------------------------
    final_prompt = f"""
{system_prompt}

--- DATA PROVIDED BELOW (DO NOT ADD EXTERNAL INFORMATION) ---

{user_prompt}
"""

    try:
        response = model.generate_content(final_prompt)
        return response.text.strip()

    except Exception as e:
        return f"Gemini summary generation failed: {str(e)}"
