# app.py

import gradio as gr
import tempfile
import os

from pdf_reader import extract_text_from_pdf
from quiz_generator import generate_mcqs
from vector_db import build_vector_db, retrieve_similar_chunks
from utils import save_as_txt, save_as_pdf

def handle_quiz_generation(pdf_file, question_count, export_type):
    if not pdf_file:
        return "Please upload a PDF file.", None

    # Save PDF to a temp location
    temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
    with open(temp_path, "wb") as f:
        f.write(pdf_file.read())

    # Extract text
    text = extract_text_from_pdf(temp_path)

    # Build vector DB from chunks
    build_vector_db(text)

    # Get relevant content for quiz (you can tweak this)
    query = "Generate MCQs"
    context = "\n\n".join(retrieve_similar_chunks(query, top_k=4))

    # Generate quiz
    quiz = generate_mcqs(context, question_count)

    # Export file
    export_path = save_as_pdf(quiz) if export_type == "PDF" else save_as_txt(quiz)

    return quiz, export_path

gr.Interface(
    fn=handle_quiz_generation,
    inputs=[
        gr.File(label="📄 Upload PDF", file_types=[".pdf"]),
        gr.Slider(1, 20, value=5, step=1, label="🧠 How many questions?"),
        gr.Radio(["PDF", "TXT"], label="📤 Export format")
    ],
    outputs=[
        gr.Textbox(label="📝 Generated MCQs", lines=20),
        gr.File(label="⬇️ Download MCQs File")
    ],
    title="🧪 Mock MCQ Quiz Generator",
    description="Upload a PDF, select number of questions, and download a generated quiz using Groq + LLaMA3. Powered by RAG (Chunking + Vector DB)."
).launch()
