import openai
import os

# Use your Hugging Face secret
openai.api_key = os.getenv("GROQ_API_KEY")

def generate_mcqs(text, num_questions=5):
    prompt = f"""
You are an expert tutor. Generate {num_questions} multiple-choice questions from the following text.
Each question should include 4 options and indicate the correct answer clearly.

Text:
{text[:3000]}
"""

    response = openai.ChatCompletion.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You generate high-quality exam-level multiple-choice questions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response['choices'][0]['message']['content']
