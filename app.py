import gradio as gr
from pdf_reader import extract_text_from_pdf
from vector_store import chunk_text, embed_chunks, build_faiss_index, get_top_chunks
from quiz_generator import generate_mcqs

def process(file, num_qs):
    raw_text = extract_text_from_pdf(file)
    chunks = chunk_text(raw_text)
    embeddings = embed_chunks(chunks)
    index = build_faiss_index(embeddings)
    top_chunks = get_top_chunks("Generate quiz", chunks, index, k=5)
    content_for_llm = "\n\n".join(top_chunks)
    mcqs = generate_mcqs(content_for_llm, num_qs)
    return mcqs

with gr.Blocks() as demo:
    gr.Markdown("""
    # 📘 Smart Mock Quiz Generator
    Upload your course notes or textbook as a PDF and get multiple-choice questions instantly! 🧠
    """)

    with gr.Row():
        file_input = gr.File(label="Upload PDF", type="binary")
        num_questions = gr.Slider(1, 10, value=5, step=1, label="Number of MCQs")

    btn = gr.Button("Generate Quiz 🧠")
    output = gr.Textbox(label="Generated Quiz", lines=20)

    btn.click(fn=process, inputs=[file_input, num_questions], outputs=output)

demo.launch()