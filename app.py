import gradio as gr
from quiz_generator import generate_mcqs
from pdf_reader import extract_text_from_pdf
from utils import save_to_txt, save_to_pdf
import os


def process_pdf(file, num_questions):
    if file is None:
        return "Please upload a PDF."

    text = extract_text_from_pdf(file)
    mcqs = generate_mcqs(text, num_questions)

    # Save MCQs to files
    txt_path = save_to_txt(mcqs)
    pdf_path = save_to_pdf(mcqs)

    return mcqs, txt_path, pdf_path


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 📚 Smart PDF MCQ Generator
    Upload a study PDF and generate multiple-choice questions!
    """)

    with gr.Row():
        pdf_file = gr.File(label="📄 Upload your PDF", file_types=[".pdf"])
        num_questions = gr.Number(label="🔢 Number of Questions", value=5)

    with gr.Row():
        generate_btn = gr.Button("🚀 Generate MCQs")

    mcq_output = gr.Textbox(label="📋 Generated MCQs", lines=20)
    txt_file_output = gr.File(label="⬇️ Download TXT")
    pdf_file_output = gr.File(label="⬇️ Download PDF")

    generate_btn.click(
        fn=process_pdf,
        inputs=[pdf_file, num_questions],
        outputs=[mcq_output, txt_file_output, pdf_file_output]
    )

if __name__ == "__main__":
    demo.launch()
