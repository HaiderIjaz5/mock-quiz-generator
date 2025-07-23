# quiz_generator.py

from openai import OpenAI
import os

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_mcqs(text, num_questions=5):
    prompt = f"""
You are a quiz generator bot. Based on the following content, generate {num_questions} MCQs with 4 options each (A, B, C, D) and provide the correct answer.

Content:
{text}

Format:
Q1. [question]
A. Option A
B. Option B
C. Option C
D. Option D
Answer: [Correct Option]
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an expert MCQ generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
