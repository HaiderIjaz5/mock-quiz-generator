import openai
import os

openai.api_key = os.getenv("GROQ_API_KEY")

def generate_mcqs(text, num_questions=5):
    prompt = f"""
You are an expert teacher. Based on the following content, generate {num_questions} multiple-choice questions.
Each question must have 4 options and clearly mention the correct answer.

Content:
{text[:3000]}
"""

    response = openai.ChatCompletion.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You generate high-quality exam MCQs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response["choices"][0]["message"]["content"]