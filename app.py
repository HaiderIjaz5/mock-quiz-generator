import gradio as gr
from pdf_reader import extract_text_from_pdf
from quiz_generator import generate_mcqs

def process_pdf(file, num_qs):
    text = extract_text_from_pdf(file)
    mcqs = generate_mcqs(text, num_qs)
    return mcqs

with gr.Blocks() as demo:
    gr.Markdown("📘 **Mock MCQ Quiz Generator**\n\nUpload a PDF (notes, textbook, etc.) to generate a quiz.")

    with gr.Row():
        file_input = gr.File(label="Upload PDF File", type="binary")
        num_questions = gr.Slider(1, 10, value=5, step=1, label="Number of MCQs")

    generate_btn = gr.Button("🧠 Generate Quiz")
    output = gr.Textbox(label="Generated Quiz", lines=20)

    generate_btn.click(fn=process_pdf, inputs=[file_input, num_questions], outputs=output)

demo.launch()
