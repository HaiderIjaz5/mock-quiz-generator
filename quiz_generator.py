import openai
import os

openai.api_key = os.getenv("GROQ_API_KEY")  # use Hugging Face secrets

def generate_mcqs(text, num_questions=5):
    prompt = f"""Generate {num_questions} multiple-choice questions from the following text. 
Each question should have 4 options, with the correct answer marked clearly.

Text:
{text[:3000]}
"""
    response = openai.ChatCompletion.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a professional exam tutor who generates high-quality MCQs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
