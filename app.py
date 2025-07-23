# app.py

import gradio as gr
from pdfminer.high_level import extract_text
from quiz_generator import generate_mcqs
from chunking import embed_and_store, search_chunks
from utils import save_as_pdf, save_as_txt
import os

# For Hugging Face secret usage
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def handle_quiz_generation(pdf_file, num_questions, export_format):
    if not pdf_file:
        return "Please upload a PDF file."

    # Extract text from PDF
    pdf_path = pdf_file.name
    text = extract_text(pdf_path)

    # Store chunks and search top content
    embed_and_store(text)
    top_chunks = search_chunks(text, top_k=4)
    combined_text = "\n".join(top_chunks)

    # Generate MCQs using the top content
    mcqs = generate_mcqs(combined_text, num_questions)

    # Save and return based on export format
    if export_format == "PDF":
        file_path = save_as_pdf(mcqs)
    else:
        file_path = save_as_txt(mcqs)

    return mcqs, file_path

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 📚 Mock MCQ Quiz Generator from PDFs")
    with gr.Row():
        pdf_input = gr.File(label="📄 Upload Study Material (PDF)", file_types=[".pdf"])
        num_input = gr.Number(value=5, label="❓ Number of Questions", precision=0)
        format_choice = gr.Radio(["PDF", "TXT"], value="PDF", label="📝 Export Format")

    with gr.Row():
        generate_btn = gr.Button("🚀 Generate Quiz")

    output_text = gr.Textbox(label="📋 Generated Questions", lines=20)
    download_output = gr.File(label="📥 Download Exported File")

    generate_btn.click(
        handle_quiz_generation,
        inputs=[pdf_input, num_input, format_choice],
        outputs=[output_text, download_output]
    )

demo.launch()
